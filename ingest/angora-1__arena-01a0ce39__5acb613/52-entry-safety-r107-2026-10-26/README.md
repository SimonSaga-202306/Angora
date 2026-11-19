# r107 · 入场和历史字节保护

入场分支 `arena/5da004bd-angora`，本地与远端 HEAD 均为 `ef45d8165a55267f6f583cdc16af89ef6b698af8`，工作区和暂存区干净，见 [baseline](baseline.json)。环境时钟与会话提供日期不同，不能据此倒填旧网页采集日；未切分支、合并、重置或 stash。

先列 [6 项上轮安全／转存清单](prior-ledgers-scope-before-read.csv)，再完整读取并[哈希](prior-ledgers-read-inventory.csv)。据上轮清单先列 [31 个保护副本](protected-variants-scope-before-read.csv)，后核 [31/31、17,455,599 bytes](protected-variants-read-inventory.csv)，仅验字节、不解析档案。先列 [4 个历史追加文件的上轮最终状态](historical-append-final-scope-before-read.csv)，后[回读](historical-append-final-read-inventory.csv)：4/4 匹配 r105／r106 的最终哈希。

本轮对其中两份历史追加文件和另外三份 r106 文档，仅作末尾纠错追加。五份均先与入场 Git HEAD 全字节比较并列[追加计划](../53-source-evidence-r107-2026-10-26/append-plan-before-write.csv)，再记[原前缀／追加段／最终哈希](../53-source-evidence-r107-2026-10-26/append-log.csv)：**108,050 bytes 原前缀保留，追加 4,385 bytes**。其余两份旧追加文件整档未改。r106 原访谈转存不修改、不移动；另存[已知一处修订](../53-source-evidence-r107-2026-10-26/r106-transcription-correction-log.csv)，不声称其全文已核对。没有执行旧 verifier。
