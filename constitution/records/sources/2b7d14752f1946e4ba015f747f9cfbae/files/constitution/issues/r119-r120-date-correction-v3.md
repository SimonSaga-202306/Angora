# r119 / r120 时间与来源日期：第三版具名更正（现行口径）

**公开致歉与更正**：r119 阶段文件与 r120 [`r120-progress-0002.txt`](../inbox/assistant-messages/r120-progress-0002.txt)、[`r120-time-conversion-clarification.md`](r120-time-conversion-clarification.md) 及 [`research-plan-before-requests.md`](../../ingest/angora-1__arena-01a0ce39__5acb613/106-source-evidence-r120/research-plan-before-requests.md) 误将 `2026-10-26 UTC` 当作当前会话日期并声称其与 `2026-11-22` 存在冲突；该错误说明已于 [`r120-date-correction-0004.txt`](../inbox/assistant-messages/r120-date-correction-0004.txt)（取代消息记录 `00a4b33c4787485ab40a68c242a91d90`）向用户致歉纠正。

## 现行准确口径（v3）

1. **当前会话日期为 `2026-11-22 UTC`**：r119 采集的 [time.is 北京可见文字](../../ingest/angora-1__arena-01a0ce39__5acb613/103-source-evidence-r119/time-reference/time.is/Beijing/chunk-0.visible.manual.md)显示 `2026-11-22 15:09:20` 北京时间（UTC+08:00），换算为 **2026-11-22 07:09:20 UTC**，与当前会话日期一致且相容；沙箱系统钟当前同为 `2026-11-22 UTC`。
2. **`2026-10-26` 既非当前会话日期，也非用户指定截止日**：r117 曾纠正“用户指定 10-26 截止”的错误；v3 进一步纠正 r118–r120 沿用 `2026-10-26 UTC` 作为当前日期基准的误判。旧文件名中的 `-2026-10-26` 或 `-2026-10-21` 只是既有命名，**不是历史发送或实际采集时间**。
3. **10 月末来源日期早于当前日期，但仍须逐源核实**：Ekonomim（P01/P12）正文自标发表 `2026-10-30`、更新 `2026-10-30 06:36`（未标时区；搜索 `pageAge` 为 `2026-10-29`）并报道 `2026-10-28` 决赛，Yeşil Haber（P09）同报 `2026-10-28`（搜索 `pageAge` `2026-10-29`），Kırıkkale 商会 PDF 首块（P02）自标 `2026-10-31`——上述日期均**早于当前会话日期 `2026-11-22 UTC`**，不再按“晚于会话日期的未来事件”排除。尽管如此，日期已过不等于事实自动成立：网页仍为动态抓取或人工转录／局部节选，媒体之间可能同源依赖 ELDER，商会 PDF 局部块与搜索摘要存在行号差异，仍须按各自来源原件边界核实。
4. **`2026-12-01` 规则变更仍属未来**：土耳其商事公报首页（r119 P13）自标拟自 `01.12.2026` 起变更登录要求，相对当前日期 `2026-11-22 UTC` 仍属未来，不能声称其已经生效。
5. **历史消息实际收发时刻依然未知**：r119 time.is 动态展示与系统墙钟仅反映当时观察，不倒填任何早期用户或助手消息的真实收发时刻。所有错误原件、初版/二版说明及旧消息记录均逐字节保留，不在原位抹除。

## 追溯修订与保留清单

- **保留不改**：[`r119-time-observations-and-scope.md`](r119-time-observations-and-scope.md)（v1）、[`r119-time-and-source-date-correction-v2.md`](r119-time-and-source-date-correction-v2.md)（v2）、[`r120-time-conversion-clarification.md`](r120-time-conversion-clarification.md)、[`r120-progress-0002.txt`](../inbox/assistant-messages/r120-progress-0002.txt) 与 [`research-plan-before-requests.md`](../../ingest/angora-1__arena-01a0ce39__5acb613/106-source-evidence-r120/research-plan-before-requests.md)；修改前 r119 文本逐字节备份于 [`../history/r119-before-v3/`](../history/r119-before-v3/)。
- **已作 v3 追溯修订**：r119 主报告、订单附录、主体映射、单主体备忘、审计、来源目录、结论锚、问题说明、`P01/P02/P09/P12/P13` 相关元数据、`compare_claims.py` 及 `claims-comparison-result.json`；并另设 [r120 日期范围与计划覆盖说明](../../ingest/angora-1__arena-01a0ce39__5acb613/106-source-evidence-r120/date-scope-correction-v3.md)。
