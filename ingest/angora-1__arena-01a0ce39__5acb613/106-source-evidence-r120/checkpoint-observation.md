# r120 快照与提交前检查观察

- **限定本地验证**：[`validate_r120.py`](validate_r120.py) 先列后读 **175/175** 路径（256,379 bytes），流式随机抽检 **30/30**，解析 110 JSON 与 14 CSV，启发式隐私扫描 0 命中，核验 48 请求清单、14 来源与 4 条结论锚，检查 253 条 Markdown 本地链接（除延迟生成的 3 项结果文件外全部存在）。[`final-validation-summary.json`](final-validation-summary.json)。
- **入账与测试**：[`ledger_capture_r120.py`](ledger_capture_r120.py) 先列后读 171 项（288,121 bytes），共生成 225 条入账收据（171 source、48 request event、6 issue/verification event）；另含已分别入账的用户/助手消息、v3 致歉纠错消息 `baa6fd746f5f45bd88081adb04286de5`（取代 `00a4b33c4787485ab40a68c242a91d90`）、r119 草稿转移与推送观察记录。`tools/test_constitution_ledger.py` **34/34** 通过。
- **台账快照**：快照 `37beef908bb944729a0c11c5e9785cac` 先列后读 1,611 个记录文件（3,641,822 bytes），核验 **805 条记录／806 个载荷文件**（1 条保留既往失败、0 错误）。[`ledger-verify.stdout.json`](ledger-verify.stdout.json)。
- **边界**：上述检查只覆盖各自范围；`.arena/r119-private-withheld/` 不暂存不推送；提交后将再核 `git ls-remote`，本观察仅记录提交前状态与快照标识，不预填后续提交哈希。
