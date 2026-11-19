# r104 · 入场文件安全比对

活动分支 `arena/5da004bd-angora` 的入场本地 HEAD 为 `691123abc7462489146cece19b81b4f917b58646`，远端为其后代 `a9ba52e0d0fbb1002e4ceae89763124bb68830a9`。先列路径及大小、再完整比较远端 blob 和入场工作区字节，确认保护后只快进，未 hard reset。

- [比较前范围](entry-scope-before-comparison.csv)：868 路径、46,015,150 bytes。
- [逐路径比较](entry-comparison.csv)：837 项完全相同、31 项不同、远端缺失 0；31/31 与 r97/r99/r101 的既有独立保护副本完整字节一致。
- 以精确路径建立 stash `76dec9b845c9425c41ee773b146f8a7a3f1754c4`，其第三父树恰有 868 个原路径；未 pop/drop。上一轮 stash 在本轮入场时不存在，不能依赖其跨会话保存；仓库内原路径异版副本才是持久保障。
