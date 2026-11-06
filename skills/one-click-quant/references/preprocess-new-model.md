# Preprocess: new model checklist

Full design: `docs/preprocess.md` (repo root).

## Architecture (do not reinvent)

```text
WeightStore / pipeline / absorb / transforms   ← shared, reuse
adapters/<model>.py                            ← per model
recipes/<model>.yaml                           ← per model
```

| Transform | Needs from adapter | Recipe seeds |
|-----------|-------------------|--------------|
| `quarot` | `build_ln_fuse_map`, `build_rotate_pairs` | optional `quarot.*`; list in `transforms` |
| `flex_awq_ssz` | `resolve_up_down` | `flex_awq_ssz.include` (up / gate_up seeds) |
| `flex_smooth_quant` | `build_ln_fuse_map` / `resolve_norm_linear` | `flex_smooth_quant.include` (norm seeds) |

Optional: `prepare_weights` (e.g. MXFP4→BF16). DeepSeek block FP8 uses recipe `unpack_fp8: true` → staging `{save-dir}.bf16_staging`.

Registered transforms: `quarot`, `flex_awq_ssz`, `flex_smooth_quant`.

## Checklist

Copy and track:

```text
- [ ] adapters/<model>.py implementing ModelAdapter
- [ ] Register in preprocess/adapters/__init__.py ADAPTER_REGISTRY (+ aliases if needed)
- [ ] recipes/<model>.yaml with adapter: <name> and transforms/include
- [ ] python3 .cursor/skills/one-click-quant/scripts/check_recipe.py recipes/<model>.yaml
- [ ] Smoke: recipe quarot.max_layers (or small model) → float HF out dir
- [ ] Downstream: slimquant_ptq / model_free_ptq with --from-preprocessed
```

## Adapter skeleton

```python
# preprocess/adapters/my_model.py
from preprocess.adapters.base import ModelAdapter

class MyModelAdapter(ModelAdapter):
    name = "my_model"

    def build_ln_fuse_map(self, cfg, num_layers=None):
        ...

    def build_rotate_pairs(self, cfg, *, block_size=32, num_layers=None, num_experts=None):
        # Return [], {} if QuaRot unused
        return [], {}

    def resolve_up_down(self, up_module: str):
        # e.g. "*.up_proj" -> "*.down_proj"
        ...
```

Register:

```python
# preprocess/adapters/__init__.py
from preprocess.adapters.my_model import MyModelAdapter
ADAPTER_REGISTRY[MyModelAdapter.name] = MyModelAdapter
```

## Recipe skeleton

```yaml
adapter: my_model
transforms:
  - flex_awq_ssz
  - flex_smooth_quant

flex_awq_ssz:
  search_step: 0.1
  ssz_step: 10
  use_calib_acts: false
  include:
    - model.layers.*.mlp.up_proj

flex_smooth_quant:
  search_step: 0.1
  use_calib_acts: false
  include:
    - model.layers.*.input_layernorm
    - model.layers.*.post_attention_layernorm
```

Reference recipes: `preprocess/recipes/deepseek_v3.yaml`, `preprocess/recipes/qwen3_8_flash_next.yaml`.

## Run

```bash
python3 main.py --alg preprocess \
  --model /path/Model \
  --save-dir /path/Model-preprocessed \
  --recipe preprocess/recipes/my_model.yaml \
  --transforms flex_awq_ssz,flex_smooth_quant \
  --preprocess-gpus 8
```

- `--preprocess-gpus N`: layer-parallel weight rewrite (not MoE EP). Single GPU: default `1`, optional `--preprocess-device cuda:0`.
- CLI `--transforms` overrides recipe order.
- True Flex calib: collect `acts.pt`, pass `--act-stats`, set `use_calib_acts: true` in recipe (see docs/preprocess.md).

## Acceptance

- Output is float weights, no `compression_config`.
- Quant path accepts it with `--from-preprocessed`.
- Core `absorb` / `pipeline` / transforms unchanged for the new model.
