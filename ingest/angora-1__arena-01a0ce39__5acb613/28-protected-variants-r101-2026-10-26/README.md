# r101 入场差异版本保护

入场时当前分支在 `691123abc7462489146cece19b81b4f917b58646`，有 868 个未跟踪文件；远端活动分支为 `43bbdbbdea59a9bb16db87e8ff7cf00cbfba96f5`，为本地 HEAD 的后代。**先列路径与大小，再逐字节和远端 Git blob 比较，最后才快进；没有 hard reset，也未覆盖原始差异。**

- [比较前路径、大小](entry-scope-before-comparison.csv)：868 项、46,015,150 bytes。
- [逐项比较及本地 SHA-256](entry-comparison.csv)：837 项相同、31 项不同、0 项远端缺失；不是 868 个新客户或新来源。
- 31 项差异中，27 项与 r97 逐原路径备份、1 项与 r99 逐原路径备份分别**完整字节一致**；在快进前用 `git show FETCH_HEAD:<备份路径>` 与各入场文件直接逐字节比较，不只是比较文件名或大小。
- 剩余 3 项在本目录 `original-paths/` 下，保留完整仓库相对路径：共 26,624 bytes。快进前先复制并核 SHA-256，快进后再次比较现存副本与新建安全 stash 的原文件字节。

| 入场文件（仓库相对路径） | bytes | SHA-256 |
|---|---:|---|
| `ingest/angora-1__arena-01a0ce39__5acb613/01-text-verbatim/workstation/00-COVERAGE-AUDIT-REPORT.md` | 7,679 | `d50b610b43451a06b9e3efc75c27ea15e7d63c86c27c7e7b13b150aef6695817` |
| `ingest/angora-1__arena-01a0ce39__5acb613/01-text-verbatim/workstation/01-knowledge-base/05-verified-quotes-by-speaker.md` | 13,669 | `2a87e4ea7b98430e26a41afc38b908ffdfe5bdd9eb1eb6e3f17d508c23b2ed8b` |
| `ingest/angora-1__arena-01a0ce39__5acb613/01-text-verbatim/workstation/01-knowledge-base/2026-08-17-l3-strategy-official-reply.md` | 5,276 | `e52e79b9ff0240f114e50fd60d6426389b5cbc770e755f2f0b534aa30b606193` |

本次新建安全 stash 当时为 `3d70319c43ce32ccf3f364fa88fcb79d216d99d3`，未 pop 或 drop；stash 可能不跨会话保留，**以上仓库内独立副本及先前 r97/r99 副本才是持久保护**。上一轮所见旧 stash 在本轮入场时不存在，不声称仍可恢复。
