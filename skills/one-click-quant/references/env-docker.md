# Environment & dataset

From repo `README.md`. Adjust image tags to what the team currently uses.

## Docker

Do **not** hardcode an image. Ask the user for either:

- **registry/image:tag** — remote; needs `docker pull`
- **image ID** (e.g. `d5b72d62e703`) — local only; **skip** `docker pull`

```bash
# Examples:
#   IMAGE="10.16.1.152:5000/jenkins/model_test_env/sglang:0.5.18-ubuntu22.04-dtk26041-py3.10-20260923-1040"
#   IMAGE="d5b72d62e703"   # local ID — do not pull
IMAGE="<user-provided-image-or-id>"
NAME="${NAME:-test_quant}"

# Pull only remote refs. Skip for local IDs / digests already on the host.
if [[ "$IMAGE" =~ ^[0-9a-fA-F]{12,64}$ || "$IMAGE" == sha256:* ]]; then
  echo "Local image ID/digest — skip pull"
else
  docker pull "$IMAGE"
fi

docker run --gpus all -itd --entrypoint /bin/bash --privileged=true \
  --network=host --device /dev/mem --shm-size=640g \
  --name "$NAME" "$IMAGE"
docker exec -it "$NAME" bash
apt update && apt install git
```

Agent checklist:

1. Ask for `IMAGE` (tag or ID) and optional container `NAME`.
2. If it looks like an image ID (short/long hex, no `/`), skip `docker pull`; only `docker run`.
3. If it is `registry/...:tag`, confirm the full string, then `pull` + `run`.
4. Prefer tag over ID when both exist — IDs are machine-local and not portable.

Large models need large `--shm-size`; reduce only for small smoke tests.

## Python deps

```bash
pip install llmcompressor
pip install 'lm_eval[vllm,api]'
```

If a release pair yields bad W8A8 precision, try llmcompressor main:

```bash
pip uninstall llmcompressor compressed-tensors -y
pip install git+https://github.com/vllm-project/llm-compressor.git
# or offline: clone repo, then pip install -e .
```

## Code & calibration data

```bash
git clone https://github.com/HYGON-AI/one-click-quant.git
cd one-click-quant
modelscope download --dataset HuggingFaceH4/ultrachat_200k --local_dir datasets/ultrachat_200k
```

Existing dataset: symlink or pass `--dataset /path/to/dir`.

Default calib path in CLI: `./datasets/ultrachat_200k`.

## Sanity

```bash
python3 main.py --help
```

## License reminders

- First-party code: Apache-2.0 file header (see README).
- Kimi modeling files and some datasets have **different** licenses; do not strip upstream notices. See `THIRD_PARTY_NOTICES.md`.
