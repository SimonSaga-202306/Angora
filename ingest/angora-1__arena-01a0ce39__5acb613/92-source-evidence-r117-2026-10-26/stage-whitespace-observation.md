# 暂存差异中的空白诊断

`git diff --cached --check` 对两份 `pen-*-local.diff` 的 7 个单空格行报 trailing whitespace。它们是 `git diff --no-index --unified=3` 产生的**统一 diff 空白上下文标记**（单个前缀空格），且对应 diff hunks 已与 GitHub commit API 原 patch 精确核验；不是需去除的正文尾随空格。为保持可验证的原字节与 SHA，不自动去空格、不篡改它们。其余阶段性诊断未显示额外路径；如后续诊断不同须另记。网页工具提取文本和几 MB 原始 Git 文件也按 `-text`/`-diff` 保持原字节。
