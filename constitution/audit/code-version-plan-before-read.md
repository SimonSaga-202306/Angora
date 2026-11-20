# 工具代码和测试版本保护计划（读取前）

独立读取检查点 `cb1246f` 的 `tools/constitution_ledger.py` 和 `tools/test_constitution_ledger.py` Git blob，并保存为各自单独的旧版副本；与当前版本分别入账，新版通过同类型 `supersedes` 链接旧版。先列 Git 对象大小和工作区文件大小，再逐个读取、计算哈希并直接比较旧版副本。符号链接缺口、修复前失败和修复后完整测试各单独记录，不以一次通过掩盖先前失败。
