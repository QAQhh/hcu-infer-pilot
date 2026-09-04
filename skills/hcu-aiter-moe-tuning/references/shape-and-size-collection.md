# Shape derivation and runtime size collection

Use this reference when adapting a new model or when the list of sizes is not yet
authoritative.

## 1. Identify the actual MoE contract

Inspect both the checkpoint config and the framework code that constructs/calls the
fused expert kernel. Record:

- quantization scheme and granularity;
- hidden size, expert intermediate size, number of experts, top-k, activation, and
  whether the MLP is gated;
- TP, expert-tensor-parallel, EP, DP, and PP settings;
- input activation dtype at the AITER call;
- `w1`, `w2`, scales, block shape, `global_num_experts`, `expert_map`, and
  `use_shuffle` after weights have been loaded and sharded.

For a conventional gated MoE with weights shaped as:

```text
w1: [E, 2*n, K]
w2: [E, K, n]
hidden_states: [M, K]
topk_ids: [M, topk]
```

the AITER tune CSV contains:

```text
token=M
inter_dim=n
model_dim=K
expert=E
topk=topk
```

The runtime API commonly receives `N1=2*n, N2=K, K=K`. `N2` in that API is the
down-projection output dimension; it is not the CSV `inter_dim`.

For a non-gated MoE, or a kernel whose packed weights use another layout, do not
apply `N1/2` mechanically. Inspect the current AITER `get_aiter_moe_config` gating
logic and actual post-load tensor shapes.

### TP and EP

If TP shards the gate/up output and down input, the usual candidate is
`n_local = n_global / moe_tp_size`. Confirm divisibility and confirm the loaded
weights. TP size and the tuner's `--mp` are unrelated: the former determines shape;
the latter only parallelizes candidate benchmarking.

With pure TP and no EP, `E` often remains the global expert count. Under EP,
framework versions differ in whether lookup is keyed by local or global experts and
how `expert_map` is used. Treat runtime AITER logs or the exact call arguments as
authoritative.

### Quantization fields

`indtype` is the input activation dtype, not the stored weight dtype. For the
channelwise flows validated on HCU:

| Checkpoint/kernel mode | AITER tune `quant_type` | Typical q sizes |
|---|---|---|
| INT8 weight + INT8 dynamic token activation, channel weight scale | `int8_w8a8_channel` | `0,0` |
| FP8 weight + INT8 dynamic token activation, channel weight scale | `f8_w8a8_channel` | `0,0` |
| INT8 W8A8 block scale | `int8_w8a8_block` | inspect block shape |
| FP8 W8A8 block scale | `f8_w8a8_block` | inspect block shape |

Do not infer channel versus block from a model name. Inspect the quantization config,
scale tensors, block shape passed by SGLang, and AITER's current quant mapping.

## 2. Collect runtime M and shape values

Static model dimensions cannot tell which `M` values serving will exercise. In the
observed AITER implementation, setting `ASM_MOE_LOG` before the first MoE call prints
lines similar to:

```text
Asm Moe Size: chunk:0, arch:gfx938, quant:f8_w8a8_channel, tokens:192, inter_dim:80, model_dim:2560, expert:512, topk:10
```

Important details:

- Set the variable before process startup because log-enable state may be cached.
- The implementation checks whether the variable exists. `ASM_MOE_LOG=0` can still
  enable logging; use `unset ASM_MOE_LOG` to disable it afterward.
- Parse every `Asm Moe Size` line, not only missing-config warnings. Once a shape has
  any table rows, lookup may silently use the nearest token entry.
- Current kernels may split inputs into chunks capped at 65536. Tune the logged chunk
  sizes, including any final remainder, rather than the original request token total.
- Collect all relevant ranks. Deduplicate only by the full input key, not by `M`
  alone, because one service can exercise multiple MoE shapes or quant modes.

Starting a server is insufficient for full coverage. Startup/warmup can exercise
CUDA graph sizes, but representative traffic is still required. Include:

- steady-state decode at batch/concurrency values from 1 through the production
  maximum;
- short, medium, and long prefill around chunked-prefill and scheduling boundaries;
- multiple concurrent prefills and mixed prefill/decode scheduling;
- maximum context and large requests that trigger kernel chunking;
- any speculative decoding, MTP, padding, graph-capture, or expert-parallel modes
  that production will enable.

Archive the server command, environment, requests, and raw logs. A parser cannot
recover sizes for workloads that were never run.

Extract a normalized input CSV with the bundled tool:

```bash
python3 scripts/aiter_moe_csv.py collect \
  server-rank*.log \
  --arch gfx938 \
  --indtype torch.bfloat16 \
  --output collected.csv
```

Then compare exact rows against the destination table and write only missing inputs:

```bash
python3 scripts/aiter_moe_csv.py coverage \
  --input collected.csv \
  --table tuned_fmoe_asm_w8a8_channel.csv \
  --arch gfx938 \
  --missing-output missing.csv
```

## 3. When production traffic is unavailable

Use a deliberate grid as a fallback, clearly labelling it synthetic rather than
observed. A grid used successfully for channelwise Qwen workloads was:

```text
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
20,24,28,32,34,36,40,44,48,56,64,68,72,80,88,96,
104,112,128,144,160,192,224,256,320,384,448,512,576,
640,704,768,832,896,960,1024,1152,1280,1408,1536,1664,
1792,1920,2048,2304,2560,2816,3072,3328,3584,3840,4096,
4608,5120,5632,6144,6656,7168,7680,8192,10240,12288,
14336,16384,17408,24576,32768,40960,49152,57344,65536
```

This is not universally complete. Add real scheduler boundaries and collected
remainders for the target deployment. Generate the input deterministically:

```bash
python3 scripts/aiter_moe_csv.py generate \
  --quant-type int8_w8a8_channel \
  --indtype torch.bfloat16 \
  --inter-dim 80 --model-dim 2560 --expert 512 --topk 10 \
  --token-grid hcu-89 \
  --output untuned.csv
```

## 4. Sanity checks before tuning

- Compare `w1/w2` shapes against the manifest and CSV.
- Confirm the destination gfx architecture through PyTorch, not a marketing name.
- Confirm the AITER runtime table name and current mapping in
  `fused_moe_asm_wna16.py`.
- Confirm whether exact rows exist; `get_aiter_moe_config(status=True)` alone is not
  an exact-coverage test.
- If the derived shape disagrees with runtime logs, stop and resolve the framework
  path, gating rule, TP/EP mapping, or quant-mode mismatch before tuning.
