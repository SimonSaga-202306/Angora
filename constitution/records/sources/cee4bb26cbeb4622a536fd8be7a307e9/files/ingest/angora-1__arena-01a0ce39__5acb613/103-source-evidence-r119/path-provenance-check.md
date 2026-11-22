# r119 路径与受限变体核验

- 在仓库 `/home/user/Angora` 执行 `pwd`、`ls -ld` 和 `realpath`：`/home/user/Angora/ingest` 是普通目录，解析到自身；`/home/user/Angora/ingest/angora-1__arena-01a0ce39__5acb613/103-source-evidence-r119` 是普通目录，解析到自身。
- `/home/user/ingest` 和其假定的 r119 子目录不存在；本轮相对路径实际写入仓库内。未发现两个现存同名路径冲突，因此没有复制、移动、覆盖或删除外部目录。结论只描述检查当时，后续交付仍按仓库内路径逐项列清单、读回和哈希。
- `.arena/r119-private-withheld/search-responses/` 内两个受限初稿位于仓库工作目录但不适合公开；`.arena` 不受 Git 忽略规则保护，可能在 `git status` 出现，平台快照又排除此目录。**不得暂存或推送**；其持久性不能保证，不能称其已保全到远端。已公开路径只保留保护性转录与删节说明，不把摘要称为原始完整响应。
- 检查时本地分支及缓存远端引用均为 `82891bdcdac4b0968f4943027bd4fc9146f8ff80`；缓存引用不代替推送前 `fetch`／推送后 `ls-remote` 核验。
