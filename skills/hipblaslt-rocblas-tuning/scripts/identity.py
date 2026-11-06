#!/usr/bin/env python3
"""Fingerprint the EXACT runtime libraries/tools, with user-confirmed GPU/build identity."""
import argparse
import hashlib
import json
from pathlib import Path
import platform


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(4 * 1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def check(identity):
    for item in identity['files']:
        if sha(item['path']) != item['sha256']:
            raise ValueError(f'identity drift: {item["path"]}')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--arch', required=True)
    p.add_argument('--cu', required=True, type=int)
    p.add_argument('--hipblaslt-git-version', required=True, help='exact Git Version value emitted by MATCHED native bench/config')
    p.add_argument('--file', action='append', required=True, help='actual loaded libhipblaslt/librocblas plus bench executable; repeat')
    p.add_argument('--out', required=True)
    a = p.parse_args()
    obj = {'arch': a.arch, 'cu': a.cu, 'hipblaslt_git_version': a.hipblaslt_git_version, 'host': platform.node(), 'files': [{'path': str(Path(x).resolve()), 'sha256': sha(x)} for x in a.file]}
    Path(a.out).write_text(json.dumps(obj, indent=2) + '\n')


if __name__ == '__main__':
    main()
