# 更正 Q19 的错误纠错，以及 Q16／Q19／Q31 缺状态字段

第一次按预列清单生成搜索结果索引失败，提示 `KeyError: 'status'`；追查 Q16、Q19 当前稿、Q31 三份人工封装均缺少 `status`。三次实际工具可见结果均为 `status: success`，结果正文不受该字段缺漏影响；修订稿分别新增该字段，仍是人工转存且未经协议字节比对。

**具名修正／取代 `search-responses/Q19-transcription-correction.md` 的错误说法**：重新读回 Q19 初稿 `Q19.tool-visible.manual.initial-version.json`，它只含一个结尾的 `status`，并非两个。此前错误地声称重复并删掉了唯一字段，造成 Q19 当前稿缺失状态。原初稿、错误的第一次纠正记录与当前稿全部保留；新增 `Q19.tool-visible.manual.revision-r2.json`，仅在结构化数据中恢复 `success` 状态。不能把这次错误说成工具数据错误。

Q16、Q31 的初稿也分别遗漏一次响应状态；新建 `revision-r1.json`，不覆盖各初稿。新增修订版本是依据工具当时可见状态作人工纠正，转录其他字段仍可能有误。首次构建失败及诊断另记，随后重跑的结果单独保存。
