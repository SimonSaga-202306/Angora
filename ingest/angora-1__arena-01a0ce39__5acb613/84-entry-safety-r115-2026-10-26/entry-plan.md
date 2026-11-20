# r115 入场保护计划

先按 `incoming-scope-before-read.csv` 逐项验证现有 868 个未跟踪路径，对照远端原路径或已保存的保护异版；不显示内容、不覆盖。只有每项都能明确匹配且远端快进安全时，才对事先冻结的路径清单选择性 stash、核对 stash 第三父树，再执行 `git merge --ff-only`。不得全量暂存、reset、clean、切分支或 pop stash。新建 r115 目录不包含在旧路径清单中。
