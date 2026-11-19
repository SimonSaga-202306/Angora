# r105 · 入场及历史字节保护

活动分支 `arena/5da004bd-angora` 入场本地 HEAD 和远端均为 `73d2c9d010ac36875a19fe23edfcd885234c73a6`；工作区及暂存区干净、无入场待保护变更。未切分支、合并、重置或创建／弹出 stash。[基线](baseline.json)保留时钟观察及日期冲突。

先列[上轮安全总表的路径和大小](prior-ledger-scope-before-read.csv)，再读取并[记录哈希](prior-ledger-read-inventory.csv)；从中分别列出 31 个受保护副本的[读取前清单](protected-variants-scope-before-read.csv)，逐项读取、哈希并与原入场字节比对，结果为 **31/31、17,455,599 bytes**；不解析或改变内容。

上轮对六个追加文件的最终字节有整档校验。本轮先列[上轮索引](../45-source-evidence-r105-2026-10-26/previous-index-scope-before-read.csv)，再核这六个文件**当时**的[完整最终字节不变](../45-source-evidence-r105-2026-10-26/r104-final-protection-inventory.csv)。此后为具名纠错，向其中两份及另外两份旧文件仅作末尾追加，先列[追加计划](../45-source-evidence-r105-2026-10-26/append-plan-before-write.csv)，记录四份原前缀和新增段的[字节与哈希](../45-source-evidence-r105-2026-10-26/append-log.csv)；原前缀 95,306 bytes 不变。单独建立 dossier 附录及 mapping，只在本轮两个新目录放置 `.gitattributes`，不改根属性。没有运行涉及停项的旧 verifier。
