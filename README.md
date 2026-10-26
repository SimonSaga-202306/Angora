# Angora-1 全量入库仓库

本仓库保存 **[SimonSaga-202306/Angora-1](https://github.com/SimonSaga-202306/Angora-1)**
分支 `arena/01a0ce39-angora`（commit `5acb613`）的**全量读取入库结果**。

- 781 个文件 / 57 个子目录 / 最深 5 层，递归全覆盖，含隐藏文件与配置检查
- **不合并**：一个源文件 = 一个产物文件（781 : 781）
- 文本类文件逐字节原样副本；Office/PDF 全量文本抽取；二进制媒体保留字节级身份

入口：

- [`ingest/angora-1__arena-01a0ce39__5acb613/README.md`](ingest/angora-1__arena-01a0ce39__5acb613/README.md) — 入库总说明、统计、读取顺序、限制说明
- [`ingest/angora-1__arena-01a0ce39__5acb613/00-manifest/FULL-TREE.md`](ingest/angora-1__arena-01a0ce39__5acb613/00-manifest/FULL-TREE.md) — 完整递归目录树（逐文件带字节数）
- [`ingest/angora-1__arena-01a0ce39__5acb613/00-manifest/INGEST-CATALOG.md`](ingest/angora-1__arena-01a0ce39__5acb613/00-manifest/INGEST-CATALOG.md) — 按 0001→0781 顺序的逐文件目录（路径 + 大小 + sha256 + 产物 + 方法）
- [`ingest/angora-1__arena-01a0ce39__5acb613/00-manifest/VERIFICATION.md`](ingest/angora-1__arena-01a0ce39__5acb613/00-manifest/VERIFICATION.md) — 12 项完整性校验（全部 PASS）
- `tools/build_ingest.py` / `tools/verify_ingest.py` — 可复现的入库与校验脚本
