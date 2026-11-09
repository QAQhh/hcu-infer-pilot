#!/usr/bin/env python3
"""Version-matched heuristic search on powers-of-two points; does not start services."""
import argparse
import concurrent.futures
import os
from pathlib import Path
import subprocess
import time
from gemm_plan import checked_plan, hip_config, save, shape
from identity import check, sha

CLEAN = ('HIPBLASLT_TUNING_OVERRIDE_FILE', 'HIPBLASLT_TUNING_FILE', 'HIPBLASLT_LOG_MASK', 'ROCBLAS_TENSILE_LIBPATH', 'ROCBLAS_LAYER', 'TENSILE_DB', 'ROCBLAS_UNSELECT_CHECK')


def clean_env():
    env = dict(os.environ)
    for key in CLEAN:
        env.pop(key, None)
    return env


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--plan', required=True); p.add_argument('--bench', required=True); p.add_argument('--out', required=True)
    p.add_argument('--gpus', default='0', help='physical IDs, one worker per GPU, e.g. 0,1,2,3')
    p.add_argument('--cold-iters', type=int, default=3); p.add_argument('--iters', type=int, default=10); p.add_argument('--timeout', type=int, default=3600)
    a = p.parse_args()
    plan = checked_plan(a.plan); check(plan['identity'])
    bench = Path(a.bench).resolve()
    if not any(x['sha256'] == sha(bench) for x in plan['identity']['files']):
        raise ValueError('bench absent from runtime fingerprint')
    out = Path(a.out).resolve(); out.mkdir(parents=True, exist_ok=False)
    help_result = subprocess.run([str(bench), '--help'], capture_output=True, text=True, env=clean_env(), timeout=60)
    (out / 'bench-help.txt').write_text(help_result.stdout + help_result.stderr)
    for flag in ('algo_method', 'requested_solution', 'workspace', 'api_method', 'print_kernel_info'):
        if flag not in help_result.stdout + help_result.stderr:
            raise ValueError(f'unsupported bench adapter: {flag}')
    gpus = a.gpus.split(',')
    if len(set(gpus)) != len(gpus) or a.iters < 1 or a.cold_iters < 0:
        raise ValueError('invalid GPU list/iteration counts')
    tasks = [(f, n) for f in plan['families'] if f['library'] == 'hipblaslt' for n in f['points']]
    def worker(item):
        worker_id, gpu = item
        results = []
        for i, (family, n) in enumerate(tasks):
            if i % len(gpus) != worker_id:
                continue
            prefix = out / f'f{family["family"]}-m{n}'
            config = prefix.with_suffix('.config')
            flags = shape(family, n)
            # Explicitly search ALL heuristic candidates, rather than timing only default.
            flags.update({'--api_method': 'c', '--algo_method': 'heuristic', '--requested_solution': '-1', '--workspace': '0', '--cold_iters': str(a.cold_iters), '--iters': str(a.iters), '--initialization': 'rand_int'})
            command = [str(bench)] + [x for pair in flags.items() for x in pair] + ['--print_kernel_info']
            env = clean_env(); env.update(HIP_VISIBLE_DEVICES=gpu, HIPBLASLT_TUNING_FILE=str(config), OMP_NUM_THREADS='2', OPENBLAS_NUM_THREADS='2')
            started = time.monotonic()
            with prefix.with_suffix('.log').open('w') as log:
                result = subprocess.run(command, env=env, stdout=log, stderr=subprocess.STDOUT, timeout=a.timeout)
            if result.returncode:
                raise RuntimeError(f'bench failed: {prefix}')
            version, selected = hip_config(config)
            if version != 'Git Version: ' + plan['identity']['hipblaslt_git_version'] or len(selected) != 1:
                raise ValueError(f'incompatible native config: {prefix}')
            chosen = selected[0]
            if not chosen['gcnArchName'].startswith(plan['identity']['arch']) or int(chosen['CUs']) != plan['identity']['cu']:
                raise ValueError('GPU identity mismatch')
            for key in ('-m', '-n', '-k', '--lda', '--ldb', '--ldc', '--ldd', '--a_type', '--b_type', '--c_type', '--d_type', '--compute_type', '--scaleA', '--scaleB'):
                column = key.lstrip('-')
                if key in flags and chosen.get(column) != flags[key]:
                    raise ValueError(f'selected shape/type drift: {key}')
            record = {'plan_fingerprint': plan['fingerprint'], 'family': family['family'], 'token_m': n, 'flags': shape(family, n), 'chosen': chosen, 'version': version, 'gpu': gpu, 'elapsed_s': time.monotonic() - started, 'command': command}
            save(prefix.with_suffix('.json'), record); results.append(record)
            print(f'DONE family={family["family"]} M={n} us={chosen["us"]}', flush=True)
        return results
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(gpus)) as executor:
        results = sum(executor.map(worker, enumerate(gpus)), [])
    if len(results) != len(tasks) or not results:
        raise ValueError('incomplete tuning')
    check(plan['identity'])
    save(out / 'points.json', sorted(results, key=lambda x: (x['family'], x['token_m'])))


if __name__ == '__main__':
    main()
