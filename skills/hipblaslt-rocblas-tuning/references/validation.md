# 单算子验证范围与验收

## 附带 C++ 适配器的边界

| 适配器 | 支持 | reference / 覆盖 |
|---|---|---|
| `verify_hip.cpp` | TN、batch1，INT8 A/B、INT32 C、BF16 D，compute32I，F32 outer-vector A/B scale，alpha1/beta0，无 bias/activation，workspace0 | 独立 HIP integer dot + FP32 scales + BF16 cast；baseline 与 tuned 各查128点/形状；对全整数 tokenM 做 support check、计时 |
| `verify_roc.cpp` | TN，BF16 A/B，BF16 或 FP32 C/D，F32 compute，单 GEMM 或固定 A/B stride 的 batched，packed C/D，alpha1/beta0 | 独立 HIP dot + 输出 cast；覆盖 batch、首尾/伪随机位置；baseline/tuned 独立进程，各查128点/形状 |

输入是确定性的 `[-3,3]` 整数值；hip vector scales 是非1的2次幂。这样能发现 descriptor、索引、batch、stride、scale 应用等错误，并可以精确比较。**不代表真实 FP8/INT8 激活分布的全部数值精度，也不是整矩阵 reference。** `sampled_values` 是比较次数，小形状上位置可能重复。

本 skill 的 C++ 源码来自已运行过的 NMZ 验证器；本次可移植化改为任意 cap 分工、去除无指纹续跑、两侧一致迭代、hip baseline 精度检查。这些改动仅做过离线检查，当前 skill 创建过程中没有启动服务、重新编译 GPU 代码或重新执行 GPU 数值测试。实际使用时必须在目标头文件/库上编译验证。

特别注意该 NMZ INT8 合约的 `alpha/beta` 按整数指针传递；之前传 float 指针会把位模式误当整型造成严重错误。不要把它推广到 FP8/BF16；按当前库 API 的 compute/scale 类型约定确认。扩展支持域时同步改 descriptor、buffer size、reference 和 wrapper 的前置条件。

## 验证步骤

1. 从 plan 生成限定适配器输入，前置条件不满足立即报错。FP8、NN、不同输出、融合 bias/activation、非1/0 alpha/beta 等走匹配版 bench 验证或另写真实 descriptor 适配器。
2. hip 对每个整数目标 M 按 `(距离,sourceM)` 排序调优点，调用 `matmulIsAlgoSupported` 并确认 workspace0，然后运行候选；用 heuristic1 作为干净 baseline。验证通过后最终 config 使用**实际被选中 sourceM**。
3. roc 从干净进程分别加载系统 native 和本次完整 native；对调优后的全部整数 M 验证。复制 kernel 不兼容、报错、输出不正确都算失败。当前 roc 脚本遇错停止，手动/扩展适配器实现下一最近点，重新生成并验证；没有“自动 fallback 已验证”的保证。
4. wrapper 检查唯一 `(family,token_m)` 全覆盖、baseline/tuned mismatch=0、正且有限的时间。结果和 plan/库/config 哈希绑定；中断后目录中的半成品不能直接交付或无条件续跑。
5. 正式数值验收增加目标模型真实张量样本与独立 reference。测试 zero、正负极值/饱和、非2次幂且跨动态范围的 scales、边界/奇数 M、batch边界、输出尾部等实际支持输入。小 shape 可做整矩阵 reference；大 shape 抽样应披露样本数、分布和误差最大值/p99、相对误差/容差。容差依 dtype、输出舍入和累加方式制定，不能把合成整数输入的零容差直接套到 FP8/随机 BF16。
6. 配置原生加载必须另查选中 kernel：hip 的 direct index support 测试不验证 override parser；roc 默认回落可能仍算得正确但调优未生效。保留库加载路径、selected solution、trace kernel 对照。

## 性能比较与报告

- 基线不带 override/搜索日志；tuned 只增加对应配置。使用同一 GPU、stream、输入分布、buffer 分配和 workspace。两库验证依次执行；GPU 无其他任务，记录温度/频率/功耗状态。
- 默认双方 warmup3、迭代10，用 stream GPU event 除以迭代数得到单次 us。hip 按 M 奇偶交换 baseline/tuned 次序，roc 按 worker 交换两进程次序，降低固定顺序偏差；不能消除所有温度/缓存差异。
- 更改 `--cold-iters`/`--iters` 时两侧同步改变。完整全 M 基线可能很慢，先少量代表点估算总耗时。不要不披露地只跑1次 baseline 而 tuned 跑10次。
- 独立重复重点尺寸至少3轮，用新目录保留每轮数据，比较中位数与波动。短 kernel 的 host submission/queue gap、cache 与 rotating buffer 策略可能显著影响结果，必要时使用实际调用流重放。
- `speedup=baseline_us/tuned_us`。每个 family 单独展示 cap、最大 M 两侧 us、加速比、全 M 几何平均/中位/最低比、退化点列表。按形状等权平均不代表真实业务加速，需要实际调用分布加权且明确权重来源。
- 不删除退化值；显著退化时先排查测量噪声，再选择是否增调关键点、换兼容候选或保留 baseline 解，记录例外并重验。若用户只要求按最近复制，则如实汇报退化，不能暗改策略。
- 单算子精度、性能、模型端到端性能、数据集准确率分别报告。模型级性能对比需关闭或统一 profile/日志并统一 cache；数据集准确率必须另跑用户指定评测，不能由合成 reference 推导。
