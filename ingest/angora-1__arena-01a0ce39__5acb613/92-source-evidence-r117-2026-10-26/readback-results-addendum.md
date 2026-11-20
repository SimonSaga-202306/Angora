# r117 回读与测试补充结果

**全量读取完成（仅本轮预列产物）**：原计划范围 **383/383 路径、74,434,255 bytes**；其中 1 个 NUL pathspec 按二进制读取，其余按 UTF-8 完整解码。[预列](round-readback-scope.csv)／[逐路径 SHA](round-readback-inventory.csv)／[汇总](round-readback-summary.json)。这包含新证据、安全目录、主报告／附录／映射／单主体备忘／审计和一次追加索引后的主档；主档旧内容只做字节完整性读取，没有展示或分析停项。

六项最终交付／主档 **6/6 路径、74,894 bytes**，独立先列后回读并记录 SHA：[范围](final-deliverables-scope-before-read.csv)／[结果](final-deliverables-inventory.csv)。它们已包含在 383 项中，不重复加总。

回读后新建的测试／清单等 11 项另行先列后完整回读 **11/11、128,352 bytes**：[附加范围](post-readback-artifacts-scope-before-read.csv)／[SHA](post-readback-artifacts-inventory.csv)。附加清单自身及本补充文本不自包含。首次测试 15/16，因最终日志尚未创建造成第 15 项链路失败；保留初次日志和修复计划。第二次预先创建日志，**16/16 通过**：[测试结果](test-outcome-note.md)。

所有数量只描述明确列出的本地文件，不代表全部互联网、源网页原始 HTML、所有会议材料或 Angora 全部商业史；16 份原始 Git 文件也不是 16 个独立证人。后续文件若变更，旧 SHA 不自动代表新版本。
