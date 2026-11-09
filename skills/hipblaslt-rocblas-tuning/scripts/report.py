#!/usr/bin/env python3
"""Summarize measured per-shape performance and retain every regression."""
import argparse
import csv
import math
from pathlib import Path
import statistics
from gemm_plan import checked_plan, read, save, write_csv
from identity import sha


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--plan', required=True); p.add_argument('--csv', required=True); p.add_argument('--library', required=True, choices=['hipblaslt', 'rocblas']); p.add_argument('--out', required=True)
    a = p.parse_args(); plan = checked_plan(a.plan)
    provenance = read(str(a.csv) + '.provenance.json')
    if provenance['plan_fingerprint'] != plan['fingerprint'] or provenance['csv_sha256'] != sha(a.csv):
        raise ValueError('measurement provenance mismatch')
    with Path(a.csv).open() as stream:
        rows = list(csv.DictReader(stream))
    expected = {(f['family'], n) for f in plan['families'] if f['library'] == a.library for n in range(1, f['max_token_m'] + 1)}
    if len(rows) != len(expected) or {(int(r['family']), int(r['token_m'])) for r in rows} != expected:
        raise ValueError('duplicate/missing shapes')
    for r in rows:
        b, t = float(r['baseline_us']), float(r['tuned_us'])
        if not math.isfinite(b) or not math.isfinite(t) or b <= 0 or t <= 0:
            raise ValueError('nonfinite/nonpositive timing')
        if int(r['mismatches']) or int(r.get('baseline_mismatches', 0)):
            raise ValueError('accuracy failure')
        r['speedup'] = b / t
    out = Path(a.out); out.mkdir(parents=True, exist_ok=False)
    summaries = []
    for f in plan['families']:
        family = [r for r in rows if int(r['family']) == f['family']]
        if not family:
            continue
        upper = next(r for r in family if int(r['token_m']) == f['max_token_m'])
        speedups = sorted(r['speedup'] for r in family)
        summaries.append({'family': f['family'], 'max_token_m': f['max_token_m'], 'max_m_baseline_us': upper['baseline_us'], 'max_m_tuned_us': upper['tuned_us'], 'max_m_speedup': upper['speedup'], 'shapes': len(family), 'min_speedup': min(speedups), 'median_speedup': statistics.median(speedups), 'geomean_speedup': math.exp(statistics.mean(math.log(s) for s in speedups)), 'regression_shapes': sum(s < 1 for s in speedups), 'regressions_over_5pct': sum(s < 1/1.05 for s in speedups)})
    write_csv(out / 'families.csv', summaries)
    regressions = [r for r in rows if r['speedup'] < 1]
    if regressions:
        write_csv(out / 'regressions.csv', regressions)
    save(out / 'summary.json', {'library': a.library, 'shapes': len(rows), 'sampled_values': sum(int(r['sampled_values']) for r in rows), 'mismatches': 0, 'regression_shapes': len(regressions), 'families': summaries, 'measurement': 'operator GPU event timing; sampled synthetic precision. Config source timing is not target timing. Not end-to-end model/dataset accuracy.'})
    print(out / 'summary.json')


if __name__ == '__main__':
    main()
