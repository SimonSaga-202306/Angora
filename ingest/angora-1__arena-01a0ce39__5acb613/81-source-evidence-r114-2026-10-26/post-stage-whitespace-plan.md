# 暂存后空白检查与补充清单计划

精确暂存后，默认 `git diff --cached --check` 返回退出码 2：共 3,552 条 `trailing whitespace` 诊断、44 个 CSV 文件；这是 CSV 使用 CRLF 行尾时，Git 默认 whitespace 设置将行尾 CR 当作多余空白。使用仅对该次命令生效的 `git -c core.whitespace=cr-at-eol diff --cached --check` 后退出码为 0、无诊断。没有更改 Git 全局／仓库配置，也没有为消除报告而改写来源、清单或其哈希。

本检查发生在第一份清单暂存后。执行补充暂存前，先保存当时的 `stage-paths.txt` 和 `output-manifest-before-stage.csv` 为 `stage-attempt-2-paths.txt` 与 `stage-attempt-2-manifest.csv`，再将本说明和两份快照明确加入逐文件清单，重新生成当前清单及哈希。补充暂存的路径仅为：本说明、两份快照、更新后的 `stage-paths.txt` 和 `output-manifest-before-stage.csv`；不得全量暂存。然后重新校验全部暂存路径、清单哈希、只读验证和 CRLF 兼容的空白检查。
