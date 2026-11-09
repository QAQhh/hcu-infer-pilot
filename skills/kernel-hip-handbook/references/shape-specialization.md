> 本节内容从 `SKILL.md` 拆出，用于保持入口文件精简；正文内容未做删改。

## 16. Shape 特化优化

当用户提供了目标模型的 **shape 信息**（kernel 在实际模型中的调用参数）时，可利用这些信息做更精准的优化决策——包括 block size 选择、reduction 方式、循环展开因子、LDS 分配等。

### 16.1 Shape 信息格式

用户提供的 shape 信息应包含 kernel 在目标模型中的**实际调用参数**。格式示例：

```yaml
# 目标模型 shape 配置
model: Sparse4D / Qwen3-VL / BEVFormer  # 模型名称
training_config:                          # 训练配置
  batch_size: 2
  num_gpus: 8

# 算子调用参数（从 profiling 或模型代码中提取）
kernel_shapes:
  deformable_aggregation:
    batch: 2
    num_anchors: 900
    num_embeds: 256       # channel 维度
    num_groups: 8         # 权重分组数
    num_pts: 12           # 采样点数
    num_cams: 6           # 相机数
    num_scale: 4          # 多尺度层级
    feat_h: [100, 50, 25, 13]    # 各尺度特征图高度
    feat_w: [176, 88, 44, 22]    # 各尺度特征图宽度

  ms_deform_attn:
    batch: 2
    num_queries: 40000
    num_heads: 8
    num_levels: 4
    num_points: 4
    embed_dim: 256

  rmsnorm:
    hidden_size: 3584
    dtype: float16
    typical_seq_len: 2048
```

**如何获取 shape 信息**：
1. 从模型代码中直接读取（`config.py` / `model.py`）
2. 在训练脚本中添加打印语句获取实际调用参数
3. 使用 profiler（如 `rocprof`）抓取 kernel 启动参数

### 16.2 特化策略

拿到 shape 信息后，以下维度可以进行**面向特定参数的精准优化**：

| 特化维度 | 通用版行为 | Shape 特化行为 | 典型收益 |
|---------|-----------|--------------|---------|
| **Block Size** | 默认 256 或简单自适应 | 根据 `num_embeds` 精确选择（如 256→512 over-provision） | 1.1-1.3× |
| **Group Reduction** | 通用 blockReduceSum | 根据 `group_size=num_embeds/num_groups` 选择 sub-warp shuffle (8.9) | 1.3-2× |
| **循环展开** | `#pragma unroll` 由编译器决定 | 根据 `num_pts×num_cams×num_scale` 的乘积决定展开因子 | 1.1-1.2× |
| **LDS 分配** | 保守分配避免 occupancy 下降 | 根据实际数据量精确分配，最大化 tile 复用 | 1.1-1.3× |
| **并行粒度** | 通用粒度适配多种配置 | 根据 `batch×anchors` vs CU 数选择最优粒度 | 1.2-2× |
| **特化 kernel dispatch** | 统一代码路径 | Host 端 `if (num_embeds==256 && num_groups==8)` 分发特化版 | 1.1-1.5× |

### 16.3 实施要点

1. **保留通用代码路径**：特化 kernel 通过 host 端 dispatch 调用，通用版作为 fallback：
   ```cpp
   void forward(/* params */) {
       if (num_embeds == 256 && num_groups == 8) {
           forward_specialized_256_8<<<grid, 512>>>(/* params */);
       } else {
           forward_generic<<<grid, select_block_size(num_embeds)>>>(/* params */);
       }
   }
   ```

2. **编译期常量**：将已知的 shape 参数用 `constexpr` 或模板参数固化，让编译器做更多优化：
   ```cpp
   template<int NUM_EMBEDS, int NUM_GROUPS>
   __global__ void forward_specialized(/* params */) {
       constexpr int GROUP_SIZE = NUM_EMBEDS / NUM_GROUPS;  // 编译期已知
       // 编译器可以完全展开 group 循环、精确分配寄存器
   }
   ```

3. **Shape 信息记录在报告中**：优化报告（12 节）的"优化措施"章节应注明使用了哪些 shape 参数进行特化，便于后续维护。

### 16.4 何时使用 Shape 特化

当以下任一条件成立时，建议采用 Shape 特化策略：

- 用户提供了目标模型的 shape 信息
- kernel 存在明确的参数特化机会（如 `group_size` 恰好是 wavefront 的整除分割）
- 算子在端到端模型中是热点（cumulative time > 10%），精准调优收益显著
- 通用优化后加速比仍有提升空间（Roofline 分析未达瓶颈）

---
