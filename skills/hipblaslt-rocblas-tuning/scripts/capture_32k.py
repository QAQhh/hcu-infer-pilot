#!/usr/bin/env python3
"""Capture one exact-length request on an ALREADY RUNNING, dedicated SGLang service."""
import argparse
import json
from pathlib import Path
import time
import urllib.request


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base-url', required=True)
    p.add_argument('--out', required=True)
    p.add_argument('--log', action='append', required=True, help='readable local/shared rank log; repeat for all ranks/nodes')
    p.add_argument('--tokens', type=int, default=32768)
    p.add_argument('--token-id', type=int, required=True, help='valid non-special token ID for this model')
    p.add_argument('--profile-dir', help='absolute path visible to service; shared path for multi-node')
    p.add_argument('--warmup', type=int, default=1)
    a = p.parse_args()
    if a.tokens < 1 or a.warmup < 0:
        p.error('tokens positive, warmup nonnegative')
    out = Path(a.out); out.mkdir(parents=True, exist_ok=False)
    logs = [Path(x) for x in a.log]
    for path in logs:
        if not path.is_file():
            raise ValueError(f'log inaccessible: {path}')
    def save(name, obj):
        (out / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
    def api(path, data=None):
        request = urllib.request.Request(a.base_url.rstrip('/') + path, None if data is None else json.dumps(data).encode(), {'Content-Type': 'application/json'})
        with urllib.request.urlopen(request, timeout=3600) as response:
            body = response.read().decode()
        try:
            return json.loads(body)
        except json.JSONDecodeError:
            return body
    payload = {'input_ids': [a.token_id] * a.tokens, 'sampling_params': {'temperature': 0, 'max_new_tokens': 1, 'min_new_tokens': 1, 'ignore_eos': True}}
    save('server-info.json', api('/server_info'))
    save('request.json', payload)
    for i in range(a.warmup):
        save(f'warmup-{i}.json', api('/generate', payload))
    # Dedicated service only: flushing avoids measuring an all-prefix-cache hit.
    save('flush-cache.json', api('/flush_cache', {}))
    sources = [{'path': str(path.resolve()), 'start': path.stat().st_size} for path in logs]
    started = False
    try:
        if a.profile_dir:
            options = {'output_dir': a.profile_dir, 'activities': ['CPU', 'GPU'], 'record_shapes': True, 'with_stack': False, 'profile_id': 'gemm-32k-' + str(int(time.time())), 'merge_profiles': False}
            save('profile-options.json', options)
            save('profile-start.json', api('/start_profile', options)); started = True
        result = api('/generate', payload)
        save('response.json', result)
        meta = result['meta_info']
        if meta['prompt_tokens'] != a.tokens or meta['completion_tokens'] != 1 or meta.get('cached_tokens', 0) != 0:
            raise ValueError(f'invalid capture token/cache counts: {meta}')
    finally:
        if started:
            save('profile-stop.json', api('/stop_profile', {}))
        for source, path in zip(sources, logs):
            source['end'] = path.stat().st_size
        save('log-sources.json', sources)
    print(out)


if __name__ == '__main__':
    main()
