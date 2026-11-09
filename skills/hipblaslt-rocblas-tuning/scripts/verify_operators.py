#!/usr/bin/env python3
"""Compile/run scoped HIP adapters; validate every integer token M, not just tuned points."""
import argparse
import concurrent.futures
import csv
import math
import os
from pathlib import Path
import subprocess
from gemm_plan import checked_plan, read, save, shape, write_csv
from identity import check, sha
from tune_hip import clean_env


def require(flags, expected):
    for key, value in expected.items():
        if flags.get(key, '1' if key == '--batch_count' else None) != str(value):
            raise ValueError(f'scoped validation adapter does not support {key}={flags.get(key)}; expected {value}')


def family_row(f, lib):
    if f['token_axis'] != '-n':
        raise ValueError('scoped C++ adapters implement TN weight-left (token axis -n) only')
    b = shape(f, f['max_token_m'])
    require(b, {'--alpha': '1', '--beta': '0'})
    m, k, n = (int(b[x]) for x in ('-m', '-k', '-n'))
    lda, ldb, ldc = (int(b[x]) for x in ('--lda', '--ldb', '--ldc'))
    ldd = int(b.get('--ldd', ldc))
    if lda < k or ldb < k or ldc < m or ldd < m:
        raise ValueError('invalid leading dimensions')
    if lib == 'hipblaslt':
        require(b, {'--transA': 'T', '--transB': 'N', '--batch_count': '1', '--a_type': 'i8_r', '--b_type': 'i8_r', '--c_type': 'i32_r', '--d_type': 'bf16_r', '--compute_type': 'i32_r', '--scale_type': 'f32_r', '--scaleA': '2', '--scaleB': '2', '--activation_type': 'none'})
        for flag in ('--bias_vector', '--scaleC', '--scaleD', '--amaxD', '--grouped_gemm'):
            if b.get(flag, '0') != '0':
                raise ValueError('unsupported hip epilogue/scaling')
        return [f['family'], m, k, lda, ldb, ldc, ldd, n]
    require(b, {'--transposeA': 'T', '--transposeB': 'N', '--a_type': 'bf16_r', '--b_type': 'bf16_r', '--compute_type': 'f32_r'})
    if b['--d_type'] not in ('bf16_r', 'f32_r') or b['--c_type'] != b['--d_type'] or ldc != ldd or ldd != m:
        raise ValueError('roc adapter requires packed, matching C/D BF16 or FP32')
    batch = int(b.get('--batch_count', 1))
    if b.get('-f') != ('gemm_ex' if batch == 1 else 'gemm_strided_batched_ex') or b.get('--flags', '0') != '0' or b.get('--algo', '0') != '0':
        raise ValueError('unsupported roc operation/algorithm flags')
    if '--stride_a' in f['linear'] or '--stride_b' in f['linear']:
        raise ValueError('roc adapter requires fixed batched A/B stride')
    for key in ('--stride_c', '--stride_d'):
        if batch > 1 and (key not in f['linear'] or f['linear'][key] != ldd):
            raise ValueError('roc adapter requires stride C/D = ldd * tokenM')
    return [f['family'], m, k, lda, ldb, ldc, ldd, n, batch, b.get('--stride_a', 0), b.get('--stride_b', 0), int(b['--d_type'] == 'f32_r')]


def run(a):
    plan = checked_plan(a.plan); check(plan['identity'])
    families = [f for f in plan['families'] if f['library'] == a.library]
    if not families:
        raise ValueError('empty validation family set')
    # Fail before compilation/GPU execution if any descriptor is outside scope.
    inputs = [family_row(f, a.library) for f in families]
    gpus = a.gpus.split(',')
    if len(set(gpus)) != len(gpus) or a.iters < 1 or a.cold_iters < 0:
        raise ValueError('invalid GPUs/timing options')
    out = Path(a.out).resolve(); out.mkdir(parents=True, exist_ok=False)
    family_file = out / 'families.csv'
    family_file.write_text(''.join(','.join(map(str, row)) + '\n' for row in inputs))
    points_file = out / 'points.csv'
    if a.library == 'hipblaslt':
        if not a.points:
            raise ValueError('hip verification requires --points')
        points = read(a.points)
        expected = {(f['family'], n) for f in families for n in f['points']}
        if len(points) != len(expected) or {(p['family'], p['token_m']) for p in points} != expected or any(p['plan_fingerprint'] != plan['fingerprint'] for p in points):
            raise ValueError('point coverage/identity mismatch')
        points_file.write_text(''.join(f'{p["family"]},{p["token_m"]},{p["chosen"]["solution_index"]}\n' for p in points))
    else:
        if not a.roc_library or not a.roc_mapping:
            raise ValueError('roc verification requires --roc-library and --roc-mapping')
        mapping_provenance = read(str(a.roc_mapping) + '.provenance.json')
        if mapping_provenance['plan_fingerprint'] != plan['fingerprint'] or sha(a.roc_mapping) != mapping_provenance['mapping_sha256']:
            raise ValueError('roc mapping identity mismatch')
        library = Path(a.roc_library).resolve()
        generated = read(library.parents[3] / 'skill-generate-native.json')
        from roc_vendor import tree_sha
        if generated['plan_fingerprint'] != plan['fingerprint'] or generated['results_csv_sha256'] != mapping_provenance['filled_csv_sha256'] or generated['tree_sha256'] != tree_sha(library):
            raise ValueError('roc native config does not match filled mapping/build')
    cpp = Path(__file__).with_name('verify_hip.cpp' if a.library == 'hipblaslt' else 'verify_roc.cpp')
    binary = out / 'verify'
    command = [a.hipcc, '-std=c++17', '--offload-arch=' + plan['identity']['arch'].split(':')[0], '-O3', str(cpp), '-lhipblaslt' if a.library == 'hipblaslt' else '-lrocblas', '-o', str(binary)]
    with (out / 'compile.log').open('w') as stream:
        subprocess.run(command, check=True, stdout=stream, stderr=subprocess.STDOUT, timeout=600)
    save(out / 'compile.json', {'command': command, 'source_sha256': sha(cpp), 'binary_sha256': sha(binary)})
    def worker(item):
        worker_id, gpu = item
        modes = ['paired'] if a.library == 'hipblaslt' else (['baseline', 'tuned'] if worker_id % 2 == 0 else ['tuned', 'baseline'])
        for mode in modes:
            env = clean_env()
            env.update(HIP_VISIBLE_DEVICES=gpu, GEMM_COLD_ITERS=str(a.cold_iters), GEMM_ITERS=str(a.iters))
            if mode == 'tuned':
                env['ROCBLAS_TENSILE_LIBPATH'] = str(Path(a.roc_library).resolve())
            target = out / f'{mode}-{worker_id}.csv'
            args = [str(binary), str(family_file)]
            if a.library == 'hipblaslt':
                args.append(str(points_file))
            args += [str(target), str(worker_id), str(len(gpus))]
            with target.with_suffix('.log').open('w') as stream:
                subprocess.run(args, env=env, check=True, stdout=stream, stderr=subprocess.STDOUT, timeout=a.timeout)
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(gpus)) as executor:
        list(executor.map(worker, enumerate(gpus)))
    def collect(mode):
        rows = []
        for i in range(len(gpus)):
            with (out / f'{mode}-{i}.csv').open() as stream:
                rows.extend(csv.DictReader(stream))
        expected = {(f['family'], n) for f in families for n in range(1, f['max_token_m'] + 1)}
        keys = {(int(r['family']), int(r['token_m'])) for r in rows}
        if keys != expected or len(rows) != len(expected):
            raise ValueError('duplicate or missing validation shapes')
        for row in rows:
            if int(row['mismatches']) or int(row.get('baseline_mismatches', 0)) or float(row['max_abs_error']) != 0:
                raise ValueError(f'accuracy failure: {row}')
            for key in ('us', 'baseline_us', 'tuned_us'):
                if key in row and (not math.isfinite(float(row[key])) or float(row[key]) <= 0):
                    raise ValueError(f'invalid timing: {row}')
        return sorted(rows, key=lambda r: (int(r['family']), int(r['token_m'])))
    if a.library == 'hipblaslt':
        rows = collect('paired')
    else:
        before = {(r['family'], r['token_m']): r for r in collect('baseline')}
        after = {(r['family'], r['token_m']): r for r in collect('tuned')}
        mapping = read(a.roc_mapping)
        if len(mapping) != len(before) or {(str(r['family']), str(r['token_m'])) for r in mapping} != set(before):
            raise ValueError('roc mapping coverage mismatch')
        rows = []
        for item in mapping:
            key = str(item['family']), str(item['token_m'])
            b, t = before[key], after[key]
            rows.append(dict(item, status='operator_validated', baseline_us=b['us'], tuned_us=t['us'], speedup=float(b['us']) / float(t['us']), sampled_values=t['sampled_values'], mismatches=t['mismatches'], max_abs_error=t['max_abs_error'], baseline_mismatches=b['mismatches']))
    check(plan['identity'])
    csv_path = out / 'all-m.csv'; write_csv(csv_path, rows)
    save(str(csv_path) + '.provenance.json', {'plan_fingerprint': plan['fingerprint'], 'csv_sha256': sha(csv_path), 'cold_iters': a.cold_iters, 'iters': a.iters, 'reference': '128 sampled outputs/shape, deterministic integer-valued synthetic inputs; hip nonunit power-of-two vector scales; NOT full tensor/real-model accuracy', 'gpus': gpus, 'roc_native_library': a.roc_library})
    print(csv_path)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--library', choices=['hipblaslt', 'rocblas'], required=True); p.add_argument('--plan', required=True)
    p.add_argument('--out', required=True); p.add_argument('--hipcc', required=True); p.add_argument('--points'); p.add_argument('--roc-library'); p.add_argument('--roc-mapping')
    p.add_argument('--gpus', default='0'); p.add_argument('--cold-iters', type=int, default=3); p.add_argument('--iters', type=int, default=10); p.add_argument('--timeout', type=int, default=86400)
    run(p.parse_args())


if __name__ == '__main__':
    main()
