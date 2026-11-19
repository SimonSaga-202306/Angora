# r108 入场与历史字节保护

入场分支 `arena/5da004bd-angora`，本地／远端 HEAD 均为 `d78a855e196b4ded8b8ca5e67c1373b5c180fa86`，工作区及暂存区干净，见 [baseline](baseline.json)。会话提供日期与环境时钟不同，目录标签和环境读数都不能证明历史采集日；未切分支、合并、重置或 stash。

- 先列 [6 项上轮安全和转存清单](prior-ledgers-scope-before-read.csv)，再[完整读取和哈希](prior-ledgers-read-inventory.csv)。
- 按上轮记录先列 [31 个保护副本](protected-variants-scope-before-read.csv)，后核 [31/31、17,455,599 bytes](protected-variants-read-inventory.csv)；仅检查字节，不解析禁项材料。
- 按 r107 五个追加文件的最终状态和此前仍未变更的两项，去重列出 **7 个不同目标**，先列[安全范围](historical-append-final-scope-before-read.csv)，再核[7/7 最终哈希](historical-append-final-read-inventory.csv)。这只是清单去重，不合并原文件；其中两个是本轮继续追加目标，其他五个全档未改。
- 本轮四份旧文（含上述两个）均先与入场 Git blob 逐字节比较，列[计划](../57-source-evidence-r108-2026-10-26/append-plan-before-write.csv)，再仅末尾追加并记[哈希链](../57-source-evidence-r108-2026-10-26/append-log.csv)：保留 **132,111 bytes 原前缀，最终追加 4,196 bytes**。两份本轮新增后缀分别为澄清上传与公开日期、避免转存完整性过度表述作过修订，见[前后日志](../57-source-evidence-r108-2026-10-26/append-revision-log.csv)，原前缀未改。不运行旧 verifier；新 verifier 只检查新一轮状态。
