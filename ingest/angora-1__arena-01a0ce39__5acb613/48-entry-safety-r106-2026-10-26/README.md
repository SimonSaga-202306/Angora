# r106 · 入场和历史字节保护

活动分支 `arena/5da004bd-angora` 入场本地 HEAD 和远端均为 `61d47150ce7c73854225d69b9c3bc72dc7c90547`，工作区和暂存区干净。会话提供日期与环境时钟冲突，见 [baseline.json](baseline.json)；没有切分支、合并、重置或 stash。

先列 [4 条上轮安全／追加清单](prior-ledger-scope-before-read.csv)，再[完整读字节并哈希](prior-ledger-read-inventory.csv)。然后按 r105 清单先列 [31 个保护副本](protected-variants-scope-before-read.csv)，逐字节验证 [31/31、17,455,599 bytes](protected-variants-read-inventory.csv)，只核哈希，不解析内容。

按上轮追加日志先列 [4 个 r105 最终文件](r105-append-final-scope-before-read.csv)，随后核 [4/4 整档与上轮最终哈希相同](r105-append-final-read-inventory.csv)。其中两份后来为 r106 纠错再次仅作末尾追加：先列 [新追加计划](../49-source-evidence-r106-2026-10-26/append-plan-before-write.csv)，记录 [79,373 bytes 原前缀和本轮新增段](../49-source-evidence-r106-2026-10-26/append-log.csv)。另外两份保持整档不变。无旧 verifier 执行。
