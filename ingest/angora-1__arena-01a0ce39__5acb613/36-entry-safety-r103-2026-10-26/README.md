# r103 · 入场文件安全比对

入场活动分支 `arena/5da004bd-angora` 本地 HEAD 为 `691123abc7462489146cece19b81b4f917b58646`，远端为其后代 `bd8d330279a3ec58e59af254454d9fb0089c1dc5`。先只列入场路径与大小，再完整比较工作区字节和远端同路径 Git blob，确认保护后仅快进，未 hard reset。

- [比较前路径与大小](entry-scope-before-comparison.csv)：868 个路径，共 46,015,150 bytes。
- [逐路径比较和哈希](entry-comparison.csv)：837 项与远端完全相同，31 项不同，远端缺失 0；31 项逐个与仓库中 r97/r99/r101 的独立保护副本完整字节比较一致，原路径和备份路径均保留。
- stash `7f48ae43b38d7d98deda226d7d679ebae74db522` 按 868 个精确路径创建，已核对第三父树恰好包含这 868 条路径，未 pop/drop。上一会话 stash 在本轮入场时不存在；stash 本身不保证跨会话保留，仓库内持久保护副本是保障。
