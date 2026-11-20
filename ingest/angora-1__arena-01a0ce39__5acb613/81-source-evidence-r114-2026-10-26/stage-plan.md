# r114 精确暂存计划（执行前）

只暂存本轮生成的 `80-entry-safety-r114-2026-10-26/`、`81-source-evidence-r114-2026-10-26/`、`82-followup-angora-r114-2026-10-26/` 下已经列出的逐文件路径，以及 r114 主报告、独立附录、映射、审计、两份验证脚本、主档的纯追加索引。所有路径先逐文件写入 `stage-paths.txt`，随后使用 Git 的 literal pathspec 文件暂存；不得使用全量 `git add .`、`git add -A`、reset、clean、切换分支或 stash pop。

`output-manifest-before-stage.csv` 对清单中除自身以外的每个文件记录字节和 SHA-256，包含 `stage-paths.txt` 本身；清单自身没有自引用哈希。先核对没有其他暂存文件、工作区变更路径与该清单完全一致，若不一致即停。主档内容只计算哈希，不展示旧正文。提交／推送只在当前 `arena/5da004bd-angora`，且远端 tip 未超出 r113 时进行。
