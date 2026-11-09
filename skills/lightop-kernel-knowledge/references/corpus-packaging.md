# 可移植知识语料

来自所提供 LightOp 知识树的完整 3,695 页来源索引、别名和仓库映射打包在 `assets/corpus.tar.gz` 中。辅助工具在首次查询时校验 SHA-256，并解压到用户缓存。需要 Python 3.10+ 和 PyYAML 6+；索引查询不需要网络。

1.1 GB 的证据树和生成的候选不随包提供。搜索结果保留上游 URL、提交、产物路径和署名；仅命中索引不能证明底层代码。使用前需获取所引用的原始 PR、diff 或源码，核对修订和许可证。已准备完整语料时，将 `KERNEL_KNOWLEDGE_ROOT` 指向其知识目录。该配置是可选的；本地目标源码与官方来源路线无需这个 checkout 也能工作。

query/get_page 可使用内置索引。search-pr-diffs 和原始 validate.py 需要通过 `KERNEL_KNOWLEDGE_ROOT` 提供完整证据语料；缺失时必须报告，不能说验证成功。克隆仓库的命令需要网络，以及用户对各来源的访问授权。
