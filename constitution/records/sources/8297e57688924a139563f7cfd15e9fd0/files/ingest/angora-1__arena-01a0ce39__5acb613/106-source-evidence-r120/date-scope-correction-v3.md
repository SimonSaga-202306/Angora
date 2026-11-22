# r120 日期基准与计划覆盖说明（v3 更正）

依据现行 [`constitution/issues/r119-r120-date-correction-v3.md`](../../../constitution/issues/r119-r120-date-correction-v3.md)，现具名覆盖并更正 r120 早期文件中的日期错误，原文件均保持字节不变：

1. [`research-plan-before-requests.md`](research-plan-before-requests.md) 的“时间限定”段误以 `2026-10-26 UTC` 作为当前会话基准，并称其与 11 月 22 日存在表面冲突。现更正：**当前会话日期为 `2026-11-22 UTC`**，与 r119 time.is（`2026-11-22 15:09:20` 北京时间 = `07:09:20 UTC`）一致；`2026-10-26` 既非当前日期也非用户截止日；`10-28`、`10-30`、`10-31` 均早于当前日期（但各事实仍须按来源核实），`12-01` 仍属未来。
2. [`ato-archive-plan-before-requests.md`](ato-archive-plan-before-requests.md) 与 [`privacy-archive-plan-before-requests.md`](privacy-archive-plan-before-requests.md) 在 Wayback CDX 查询参数中使用了 `&to=20261026`：该参数仅说明那 4 次 CDX 请求本身使用的检索日期过滤条件（A04 最新返回到 2026-02-18，A01–A03 返回空），**不代表当前日期是 2026-10-26**，也不是用户设置的研究截止日。
3. 历史消息真实收发时间未知，旧文件名日期不是历史发送时间。
