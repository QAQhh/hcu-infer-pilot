#!/usr/bin/env python3
"""Offline log extraction, explicit token-axis planning, and native config filling."""
import argparse
import collections
import copy
import csv
import hashlib
import json
from pathlib import Path
import re
import shlex


def read(path):
    return json.loads(Path(path).read_text())


def save(path, obj):
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()


def powers(cap):
    if cap < 1:
        raise ValueError('token cap must be positive')
    return sorted({1 << i for i in range(cap.bit_length())} | {cap})


def nearest(points, target):
    return sorted(points, key=lambda x: (abs(x - target), x))


def parse_logs(sources):
    counts = collections.Counter()
    rejected = []
    # One bench invocation per line. Interleaved rank output must be re-captured,
    # never repaired by guessing or by discarding duplicate flags.
    marker = re.compile(r'\b(hipblaslt|rocblas)-bench\b')
    for source in sources:
        path = Path(source['path'])
        start = int(source.get('start', 0))
        end = int(source.get('end', path.stat().st_size))
        if not 0 <= start <= end <= path.stat().st_size:
            raise ValueError(f'invalid byte range: {source}')
        with path.open('rb') as stream:
            stream.seek(start)
            content = stream.read(end - start).decode(errors='replace')
        for line_number, line in enumerate(content.splitlines(), 1):
            matches = list(marker.finditer(line))
            if not matches:
                continue
            try:
                if len(matches) != 1:
                    raise ValueError('interleaved bench invocations')
                match = matches[0]
                tokens = shlex.split(line[match.end():])
                flags = {}
                while tokens:
                    key = tokens.pop(0)
                    if not key.startswith('-'):
                        raise ValueError('unexpected trailing text')
                    if '=' in key:
                        key, value = key.split('=', 1)
                    else:
                        if not tokens or (tokens[0].startswith('-') and not re.fullmatch(r'-\d+(\.\d+)?', tokens[0])):
                            raise ValueError(f'missing value: {key}')
                        value = tokens.pop(0)
                    if key in flags:
                        raise ValueError(f'duplicate flag: {key}')
                    flags[key] = value
                required = {'-m', '-n', '-k', '--lda', '--ldb', '--ldc', '--a_type', '--d_type'}
                if not required <= flags.keys():
                    raise ValueError('missing shape/type flags')
                if any(int(flags[k]) < 1 for k in ('-m', '-n', '-k')):
                    raise ValueError('nonpositive dimension')
                counts[(match[1], tuple(sorted(flags.items())))] += 1
            except (ValueError, IndexError) as exc:
                rejected.append({'path': str(path), 'line_in_slice': line_number, 'reason': str(exc), 'text': line})
    return [{'library': lib, 'flags': dict(flags), 'count': n} for (lib, flags), n in sorted(counts.items())], rejected


def make_plan(rows, rules, identity):
    groups = {}
    for row in rows:
        flags = row['flags']
        matches = [r for r in rules if r['library'] == row['library'] and all(flags.get(k, '1' if k == '--batch_count' else None) == str(v) for k, v in r['match'].items())]
        if len(matches) != 1:
            raise ValueError(f'expect exactly one layout rule, got {len(matches)}: {row}')
        rule = matches[0]
        axis = rule['token_axis']
        cap = int(flags[axis])
        slopes = {}
        for key in rule.get('linear', []):
            if key in flags:
                value = int(flags[key])
                if value % cap:
                    raise ValueError(f'{key} not linear in {axis}: {flags}')
                slopes[key] = value // cap
        fixed = {k: v for k, v in flags.items() if k != axis and k not in slopes}
        key = (row['library'], axis, tuple(sorted(slopes.items())), tuple(sorted(fixed.items())))
        if key not in groups:
            groups[key] = {'library': row['library'], 'token_axis': axis, 'linear': slopes, 'fixed': fixed, 'captured': {}, 'rule': rule.get('name', '')}
        g = groups[key]
        g['captured'][cap] = g['captured'].get(cap, 0) + row['count']
    families = []
    for fid, g in enumerate(groups.values()):
        cap = max(g['captured'])
        g.update(family=fid, max_token_m=cap, points=powers(cap), calls=sum(g['captured'].values()))
        g['captured'] = {str(k): v for k, v in sorted(g['captured'].items())}
        families.append(g)
    if not families:
        raise ValueError('no families found')
    obj = {'schema': 1, 'identity': identity, 'families': families}
    obj['fingerprint'] = digest(obj)
    return obj


def shape(family, token_m):
    if not 1 <= token_m <= family['max_token_m']:
        raise ValueError('target outside captured cap')
    flags = dict(family['fixed'])
    flags[family['token_axis']] = str(token_m)
    flags.update({k: str(v * token_m) for k, v in family['linear'].items()})
    return flags


def checked_plan(path):
    plan = read(path)
    body = {k: v for k, v in plan.items() if k != 'fingerprint'}
    if digest(body) != plan['fingerprint']:
        raise ValueError('plan fingerprint mismatch; regenerate plan after edits')
    return plan


def hip_config(path):
    lines = Path(path).read_text().splitlines()
    if not lines or not lines[0].startswith('Git Version: '):
        raise ValueError('missing native Git Version header')
    header = None
    rows = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = next(csv.reader([line.strip()]))
        if values[0] == 'transA':
            header = values
        elif header is None or len(values) != len(header):
            raise ValueError('malformed native header/record')
        else:
            rows.append(dict(zip(header, values)))
    if not rows:
        raise ValueError('no native records')
    return lines[0], rows


def write_hip(path, version, rows):
    # The deployed build requires a repeated header before EACH native row.
    with Path(path).open('w', newline='\n') as stream:
        stream.write(version + '\n')
        for row in rows:
            stream.write('    ' + ','.join(row) + '\n')
            stream.write('    ' + ','.join(str(v) for v in row.values()) + '\n')


def fill_hip(plan, points, output, mapping_path, validation=None):
    by_key = {(int(p['family']), int(p['token_m'])): p for p in points}
    required_points = {(f['family'], n) for f in plan['families'] if f['library'] == 'hipblaslt' for n in f['points']}
    if len(by_key) != len(points) or set(by_key) != required_points:
        raise ValueError('duplicate, missing or extra tuned point')
    approved = None
    if validation:
        provenance = read(str(validation) + '.provenance.json')
        if provenance['plan_fingerprint'] != plan['fingerprint'] or hashlib.sha256(Path(validation).read_bytes()).hexdigest() != provenance['csv_sha256']:
            raise ValueError('validation fingerprint mismatch')
        with Path(validation).open() as stream:
            validated = list(csv.DictReader(stream))
        approved = {(int(r['family']), int(r['token_m'])): r for r in validated}
        if len(approved) != len(validated):
            raise ValueError('duplicate validation key')
    versions = set()
    rows, mapping = [], []
    expected_keys = set()
    for family in plan['families']:
        if family['library'] != 'hipblaslt':
            continue
        fid = family['family']
        if family['token_axis'] not in ('-m', '-n'):
            raise ValueError('native hip adapter supports BLAS m/n only')
        for point in family['points']:
            p = by_key[(fid, point)]
            if p['plan_fingerprint'] != plan['fingerprint']:
                raise ValueError('tuned point belongs to different plan/build')
            versions.add(p['version'])
        for target in range(1, family['max_token_m'] + 1):
            key = fid, target
            expected_keys.add(key)
            source = nearest(family['points'], target)[0]
            record = approved[key] if approved is not None else None
            if record:
                if int(record['mismatches']) or float(record.get('baseline_mismatches', 0)):
                    raise ValueError(f'accuracy failed: {key}')
                source = int(record['source_m'])
                if source not in family['points']:
                    raise ValueError('validation selected an untuned source')
            point = by_key[(fid, source)]
            row = copy.copy(point['chosen'])
            if record and int(row['solution_index']) != int(record['solution_index']):
                raise ValueError('validation solution differs from tuned point')
            flags = shape(family, target)
            for flag in [family['token_axis']] + list(family['linear']):
                column = flag.lstrip('-')
                if column not in row:
                    raise ValueError(f'native config lacks {column}')
                row[column] = flags[flag]
            rows.append(row)
            mapping.append({'family': fid, 'token_m': target, 'source_m': source, 'solution_index': row['solution_index'], 'status': 'operator_validated' if record else 'unvalidated_copy', 'source_bench_us': point['chosen'].get('us'), 'target_measured_us': record.get('tuned_us') if record else None})
    if approved is not None and set(approved) != expected_keys:
        raise ValueError('validation coverage differs from plan')
    if len(versions) != 1:
        raise ValueError('mixed or empty hipBLASLt versions')
    write_hip(output, versions.pop(), rows)
    save(mapping_path, mapping)


def roc_row(flags):
    if flags.get('--a_type') != 'bf16_r' or flags.get('--b_type') != 'bf16_r' or flags.get('--d_type') not in ('bf16_r', 'f32_r') or flags.get('--compute_type') != 'f32_r':
        raise ValueError('NMZ roc adapter only handles BF16 input, BF16/FP32 output')
    if flags.get('--c_type') != flags['--d_type']:
        raise ValueError('C/D dtype mismatch unsupported by vendor CSV adapter')
    row = {'gemmtype': 'bss' if flags['--d_type'] == 'f32_r' else 'bf16', 'TransA': flags['--transposeA'], 'TransB': flags['--transposeB'], 'M': flags['-m'], 'N': flags['-n'], 'K': flags['-k'], 'B': flags.get('--batch_count', '1')}
    for key in ('lda', 'ldb', 'ldc', 'ldd', 'stride_a', 'stride_b', 'stride_c', 'stride_d'):
        row[key] = flags.get('--' + key, flags['--ldc'] if key == 'ldd' else '0')
    row.update(alpha=flags.get('--alpha', '1'), beta=flags.get('--beta', '0'))
    return row


def write_csv(path, rows):
    if not rows:
        raise ValueError('no rows')
    with Path(path).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def roc_input(plan, output):
    rows = []
    native_keys = set()
    for f in plan['families']:
        if f['library'] != 'rocblas':
            continue
        for n in range(1, f['max_token_m'] + 1):
            r = roc_row(shape(f, n))
            key = tuple(r[k] for k in ('gemmtype', 'TransA', 'TransB', 'M', 'N', 'K', 'B'))
            if key in native_keys:
                raise ValueError('native roc dispatch key collision between distinct families/layouts')
            native_keys.add(key)
        rows.extend(roc_row(shape(f, n)) for n in f['points'])
    write_csv(output, rows)


def fill_roc(plan, source, output, mapping_path):
    source, output = Path(source), Path(output)
    if source.resolve() == output.resolve():
        raise ValueError('keep original powers result directory immutable')
    output.mkdir(parents=True, exist_ok=False)
    filled, mappings, used = {}, [], set()
    # Detect native key collisions even if the vendor result omits stride_d/ldd.
    roc_input(plan, output / 'input-powers.audit.csv')
    (output / 'input-powers.audit.csv').unlink()
    for f in plan['families']:
        if f['library'] != 'rocblas':
            continue
        pools = {}
        for n in f['points']:
            expected = roc_row(shape(f, n))
            name = expected['gemmtype'] + '_' + expected['TransA'] + expected['TransB'] + '.csv'
            with (source / name).open() as stream:
                records = list(csv.DictReader(stream))
            compare = ['M', 'N', 'K', 'B', 'lda', 'ldb', 'ldc', 'stride_a', 'stride_b', 'stride_c', 'alpha', 'beta']
            # Vendor CSVs omit unused single-batch stride_a/b and use packed stride_c.
            for field in ('stride_a', 'stride_b'):
                if expected['B'] == '1':
                    expected[field] = '0'
            if expected['B'] == '1' and expected['stride_c'] == '0':
                expected['stride_c'] = str(int(expected['ldc']) * int(expected['N']))
            matched = [r for r in records if all(k in r and float(r[k]) == float(expected[k]) for k in compare)]
            if len(matched) != 1 or not matched[0].get('bestkernel'):
                raise ValueError(f'missing/ambiguous vendor result: family={f["family"]}, n={n}')
            pools[n] = matched[0]
        for n in range(1, f['max_token_m'] + 1):
            src = nearest(f['points'], n)[0]
            row = dict(pools[src])
            expected = roc_row(shape(f, n))
            for key in ('M', 'N', 'K', 'B', 'lda', 'ldb', 'ldc', 'ldd', 'stride_a', 'stride_b', 'stride_c', 'stride_d'):
                if key in row:
                    row[key] = expected[key]
            if expected['B'] == '1':
                for key in ('stride_a', 'stride_b'):
                    if key in row:
                        row[key] = '0'
                if 'stride_c' in row and row['stride_c'] == '0':
                    row['stride_c'] = str(int(expected['ldc']) * int(expected['N']))
            name = expected['gemmtype'] + '_' + expected['TransA'] + expected['TransB'] + '.csv'
            filled.setdefault(name, []).append(row)
            used.add(name)
            mappings.append({'family': f['family'], 'token_m': n, 'source_m': src, 'bestkernel': row['bestkernel'], 'status': 'unvalidated_copy', 'source_gflops': pools[src].get('gflops')})
    for name in used:
        write_csv(output / name, filled[name])
    save(mapping_path, mappings)
    save(str(mapping_path) + '.provenance.json', {'plan_fingerprint': plan['fingerprint'], 'mapping_sha256': hashlib.sha256(Path(mapping_path).read_bytes()).hexdigest(), 'filled_csv_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in output.glob('*.csv')}})


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    e = sub.add_parser('extract'); e.add_argument('--sources', required=True); e.add_argument('--out', required=True); e.add_argument('--rejected', required=True)
    g = sub.add_parser('plan'); g.add_argument('--captured', required=True); g.add_argument('--rules', required=True); g.add_argument('--identity', required=True); g.add_argument('--out', required=True)
    h = sub.add_parser('fill-hip'); h.add_argument('--plan', required=True); h.add_argument('--points', required=True); h.add_argument('--out', required=True); h.add_argument('--mapping', required=True); h.add_argument('--validation')
    r = sub.add_parser('roc-input'); r.add_argument('--plan', required=True); r.add_argument('--out', required=True)
    r = sub.add_parser('fill-roc'); r.add_argument('--plan', required=True); r.add_argument('--source', required=True); r.add_argument('--out', required=True); r.add_argument('--mapping', required=True)
    a = p.parse_args()
    if a.command == 'extract':
        rows, rejects = parse_logs(read(a.sources)); save(a.out, rows); save(a.rejected, rejects)
        print(f'captured={len(rows)}, rejected={len(rejects)}')
        if rejects or not rows:
            raise SystemExit('Incomplete capture: inspect rejected log lines and capture separate rank logs')
    elif a.command == 'plan':
        plan = make_plan(read(a.captured), read(a.rules), read(a.identity)); save(a.out, plan)
        print(json.dumps({'families': len(plan['families']), 'tune_points': sum(len(f['points']) for f in plan['families']), 'filled_shapes': sum(f['max_token_m'] for f in plan['families'])}))
    elif a.command == 'fill-hip':
        fill_hip(checked_plan(a.plan), read(a.points), a.out, a.mapping, a.validation)
    elif a.command == 'roc-input':
        roc_input(checked_plan(a.plan), a.out)
    elif a.command == 'fill-roc':
        fill_roc(checked_plan(a.plan), a.source, a.out, a.mapping)


if __name__ == '__main__':
    main()
