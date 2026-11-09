#!/usr/bin/env python3
"""Offline behavioral checks. No GPU, service, remote host, or external tuner needed."""
import argparse
import copy
import csv
import json
from pathlib import Path
import tempfile
import sys
import subprocess
from unittest.mock import patch
from gemm_plan import checked_plan, fill_hip, fill_roc, hip_config, make_plan, nearest, parse_logs, powers, read, roc_input, roc_row, save, shape, write_csv, write_hip
from identity import check, sha
from verify_operators import family_row

ROOT = Path(__file__).resolve().parent.parent
IDENTITY = {'arch': 'gfx938', 'cu': 64, 'hipblaslt_git_version': 'test', 'files': []}


def fails(fn, error=ValueError):
    try:
        fn()
    except error:
        return
    raise AssertionError('expected rejection')


def fixtures():
    hip = {'--transA': 'T', '--transB': 'N', '--batch_count': '1', '--a_type': 'i8_r', '--b_type': 'i8_r', '--c_type': 'i32_r', '--d_type': 'bf16_r', '--compute_type': 'i32_r', '--scale_type': 'f32_r', '--scaleA': '2', '--scaleB': '2', '--activation_type': 'none', '--alpha': '1', '--beta': '0', '-m': '16', '-n': '8', '-k': '4', '--lda': '4', '--ldb': '4', '--ldc': '16', '--ldd': '16', '--stride_a': '64', '--stride_b': '32', '--stride_c': '128', '--stride_d': '128'}
    roc = {'--transposeA': 'T', '--transposeB': 'N', '--batch_count': '16', '--a_type': 'bf16_r', '--b_type': 'bf16_r', '--c_type': 'bf16_r', '--d_type': 'bf16_r', '--compute_type': 'f32_r', '--alpha': '1', '--beta': '0', '-m': '16', '-n': '8', '-k': '4', '--lda': '4', '--ldb': '64', '--ldc': '16', '--ldd': '16', '--stride_a': '64', '--stride_b': '4', '--stride_c': '128', '--stride_d': '128', '-f': 'gemm_strided_batched_ex'}
    return hip, roc


def unit_checks(directory):
    assert powers(1) == [1]
    assert powers(4096) == [1 << i for i in range(13)]
    assert powers(3000)[-2:] == [2048, 3000]
    assert nearest([1, 2, 4, 8], 3)[:2] == [2, 4]
    fails(lambda: powers(0))
    hip, roc = fixtures()
    rules = read(ROOT / 'assets/layout-rules.nmz-tn.json')
    rows = [{'library': 'hipblaslt', 'flags': hip, 'count': 2}, {'library': 'rocblas', 'flags': roc, 'count': 3}]
    # Multiple lengths must collapse to one signature, with derived strides adjusted.
    shorter = dict(hip, **{'-n': '3', '--stride_b': '12', '--stride_c': '48', '--stride_d': '48'})
    rows.append({'library': 'hipblaslt', 'flags': shorter, 'count': 1})
    plan = make_plan(rows, rules, IDENTITY)
    assert len(plan['families']) == 2
    assert plan['families'][0]['calls'] == 3
    assert shape(plan['families'][0], 3)['--stride_b'] == '12'
    assert shape(plan['families'][1], 3)['--stride_b'] == '4'
    for f in plan['families']:
        family_row(f, f['library'])
    changed = dict(hip, **{'--scaleB': '1'})
    assert len(make_plan(rows + [{'library': 'hipblaslt', 'flags': changed, 'count': 1}], rules, IDENTITY)['families']) == 3
    fails(lambda: make_plan(rows, rules + [rules[0]], IDENTITY))
    fails(lambda: family_row(make_plan([{'library': 'hipblaslt', 'flags': changed, 'count': 1}], rules, IDENTITY)['families'][0], 'hipblaslt'))
    flags = ' '.join(f'{k} {v}' for k, v in hip.items())
    path = directory / 'log'
    warmup = 'hipblaslt-bench ' + flags + '\n'
    path.write_text(warmup + warmup + 'hipblaslt-bench ' + flags + ' -n 8\n')
    parsed, rejected = parse_logs([{'path': str(path), 'start': len(warmup.encode())}])
    assert len(parsed) == 1 and parsed[0]['count'] == 1 and len(rejected) == 1
    assert 'duplicate' in rejected[0]['reason']
    path.write_text(warmup.rstrip() + ' rocblas-bench ' + flags + '\n')
    assert parse_logs([{'path': str(path)}])[1][0]['reason'] == 'interleaved bench invocations'
    pf = directory / 'plan.json'; save(pf, plan); assert checked_plan(pf) == plan
    altered = copy.deepcopy(plan); altered['families'][0]['max_token_m'] = 16; save(pf, altered)
    fails(lambda: checked_plan(pf))
    save(pf, plan)
    # Exercise capture API ordering and exact token/cache assertions without a server.
    from capture_32k import main as capture_main
    captured_calls = []
    class Response:
        def __init__(self, obj): self.obj = obj
        def __enter__(self): return self
        def __exit__(self, *args): pass
        def read(self): return json.dumps(self.obj).encode()
    def fake_urlopen(request, timeout):
        endpoint = request.full_url.rsplit('/', 1)[-1]
        payload = json.loads(request.data) if request.data else None
        captured_calls.append((endpoint, payload))
        if endpoint == 'generate':
            with path.open('a') as log: log.write(warmup)
            return Response({'meta_info': {'prompt_tokens': 32768, 'completion_tokens': 1, 'cached_tokens': 0}})
        return Response({'ok': True})
    capture_dir = directory / 'capture'
    with patch('urllib.request.urlopen', fake_urlopen), patch.object(sys, 'argv', ['capture_32k.py', '--base-url', 'http://offline.invalid', '--out', str(capture_dir), '--log', str(path), '--token-id', '42', '--profile-dir', '/trace']):
        capture_main()
    assert [x[0] for x in captured_calls] == ['server_info', 'generate', 'flush_cache', 'start_profile', 'generate', 'stop_profile']
    payload = read(capture_dir / 'request.json')
    assert len(payload['input_ids']) == 32768 and payload['sampling_params']['max_new_tokens'] == 1
    boundary = read(capture_dir / 'log-sources.json')[0]
    assert boundary['end'] - boundary['start'] == len(warmup.encode())
    token_file = directory / 'identity-file'; token_file.write_text('original')
    identity = {'files': [{'path': str(token_file), 'sha256': sha(token_file)}]}; check(identity)
    token_file.write_text('changed'); fails(lambda: check(identity))
    points = []
    for n in plan['families'][0]['points']:
        chosen = {'transA': 'T', 'transB': 'N', 'm': '16', 'n': str(n), 'k': '4', 'stride_b': str(4*n), 'stride_c': str(16*n), 'stride_d': str(16*n), 'us': '100', 'solution_index': str(100+n), 'gcnArchName': 'gfx938', 'CUs': '64'}
        points.append({'family': 0, 'token_m': n, 'plan_fingerprint': plan['fingerprint'], 'version': 'Git Version: test', 'chosen': chosen})
    cfg = directory / 'hip.config'; mapping_path = directory / 'hip-map.json'
    fill_hip(plan, points, cfg, mapping_path)
    version, native = hip_config(cfg)
    assert len(native) == 8 and len(read(mapping_path)) == 8
    assert b'\r' not in cfg.read_bytes()
    assert cfg.read_text().count('    transA,') == 8
    assert read(mapping_path)[2]['source_m'] == 2
    assert native[2]['stride_b'] == '12'
    validation = []
    for n in range(1, 9):
        source = 4 if n == 3 else nearest([1, 2, 4, 8], n)[0]
        validation.append({'family': 0, 'token_m': n, 'source_m': source, 'solution_index': 100+source, 'mismatches': 0, 'baseline_mismatches': 0, 'baseline_us': 10, 'tuned_us': 5, 'sampled_values': 128, 'max_abs_error': 0})
    vf = directory / 'validation.csv'; write_csv(vf, validation)
    save(str(vf)+'.provenance.json', {'plan_fingerprint': plan['fingerprint'], 'csv_sha256': sha(vf)})
    fill_hip(plan, points, cfg, mapping_path, vf)
    assert read(mapping_path)[2]['source_m'] == 4
    assert hip_config(cfg)[1][2]['solution_index'] == '104'
    report_dir = directory / 'report'
    subprocess.run([sys.executable, str(ROOT / 'scripts/report.py'), '--library', 'hipblaslt', '--plan', str(pf), '--csv', str(vf), '--out', str(report_dir)], check=True, capture_output=True)
    summary = read(report_dir / 'summary.json')
    assert summary['shapes'] == 8 and summary['families'][0]['max_m_speedup'] == 2
    assert summary['families'][0]['max_m_tuned_us'] == '5'
    vf.write_text(vf.read_text() + '\n'); fails(lambda: fill_hip(plan, points, cfg, mapping_path, vf))
    roc_input(plan, directory / 'roc-input.csv')
    with (directory / 'roc-input.csv').open() as stream:
        assert len(list(csv.DictReader(stream))) == 4
    # Distinct layouts with the same native key cannot be encoded by this dispatcher.
    clash = dict(roc, **{'--lda': '8'})
    collision = make_plan(rows + [{'library': 'rocblas', 'flags': clash, 'count': 1}], rules, IDENTITY)
    fails(lambda: roc_input(collision, directory / 'collision.csv'))
    source = directory / 'roc-source'; source.mkdir()
    results = []
    for n in plan['families'][1]['points']:
        r = roc_row(shape(plan['families'][1], n)); r.pop('gemmtype'); r.pop('TransA'); r.pop('TransB')
        r.update(bestkernel=f'kernel{n}', gflops='100')
        results.append(r)
    write_csv(source / 'bf16_TN.csv', results)
    fill_roc(plan, source, directory / 'roc-filled', directory / 'roc-map.json')
    with (directory / 'roc-filled/bf16_TN.csv').open() as stream:
        filled = list(csv.DictReader(stream))
    assert len(filled) == 8 and filled[2]['bestkernel'] == 'kernel2'
    assert filled[2]['stride_b'] == '4' and filled[2]['stride_c'] == '48'
    # Wrong alpha must not be accepted as a source point.
    results[0]['alpha'] = '2'; write_csv(source / 'bf16_TN.csv', results)
    fails(lambda: fill_roc(plan, source, directory / 'bad-roc-filled', directory / 'bad-map.json'))


def historical_checks(run, directory):
    rows = [dict(r, library=lib) for lib in ('hipblaslt', 'rocblas') for r in read(run / f'{lib}-captured.json')]
    plan = make_plan(rows, read(ROOT / 'assets/layout-rules.nmz-tn.json'), IDENTITY)
    assert len(plan['families']) == 13
    assert sum(len(f['points']) for f in plan['families']) == 157
    assert sum(f['max_token_m'] for f in plan['families']) == 49153
    for family in plan['families']:
        family_row(family, family['library'])
    points = read(run / 'hip-tuned-points.json')
    for point in points:
        point['plan_fingerprint'] = plan['fingerprint']
    fill_hip(plan, points, directory / 'historical-hip.config', directory / 'historical-hip-map.json')
    assert len(hip_config(directory / 'historical-hip.config')[1]) == 24576
    assert len(read(directory / 'historical-hip-map.json')) == 24576
    fill_roc(plan, run / 'roc-tuned-power-results', directory / 'historical-roc-filled', directory / 'historical-roc-map.json')
    assert len(read(directory / 'historical-roc-map.json')) == 24577
    with (run / 'hip-all-m-performance-accuracy.csv').open() as stream:
        validation = list(csv.DictReader(stream))
    vf = directory / 'historical-hip.csv'; write_csv(vf, validation)
    save(str(vf)+'.provenance.json', {'plan_fingerprint': plan['fingerprint'], 'csv_sha256': sha(vf)})
    fill_hip(plan, points, directory / 'historical-hip-validated.config', directory / 'historical-hip-validated-map.json', vf)
    provisional = read(directory / 'historical-hip-map.json')
    approved = read(directory / 'historical-hip-validated-map.json')
    assert sum(a['source_m'] != b['source_m'] for a, b in zip(provisional, approved)) == 5
    print('Historical artifacts: 13 families, 157 points, 49153 filled rows, 5 compatibility substitutions: PASS')


def main():
    p = argparse.ArgumentParser(description=__doc__); p.add_argument('--historical-run', type=Path); a = p.parse_args()
    with tempfile.TemporaryDirectory(prefix='blas-skill-check-') as td:
        directory = Path(td); unit_checks(directory)
        print('Offline behavior checks: PASS')
        if a.historical_run:
            historical_checks(a.historical_run, directory)
    print('No services/GPU workloads were started.')


if __name__ == '__main__':
    main()
