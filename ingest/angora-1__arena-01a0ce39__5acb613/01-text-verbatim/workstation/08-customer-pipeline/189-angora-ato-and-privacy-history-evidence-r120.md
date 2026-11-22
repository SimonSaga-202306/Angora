# r120 · Angora：日期纠错、ATO 公开名册边界与官网自述回放核验

> **结论**：本轮首要完成对先前日期基准误报的公开致歉与 **v3 具名更正**（当前会话日期为 `2026-11-22 UTC`，与 r119 time.is 北京时间 `2026-11-22 15:09:20` / `07:09:20 UTC` 一致）。在业务主体研究方面，新查到安卡拉商会（ATO）第 8 信息技术委员会存在公开名册页，但仅见第 1 页前 20 条（共 6,695 条／335 页），且官方机构公开搜索与官网隐私页历史回放均未提供官方工商登记原件；**Angora Networks 法人主体仍未确认**。

[v3 日期更正](../../../../../constitution/issues/r119-r120-date-correction-v3.md) · [r120 来源目录](../../../106-source-evidence-r120/source-catalog.csv) · [结论锚](../../../106-source-evidence-r120/evidence-traceability.csv) · [问题与边界](../../../106-source-evidence-r120/issues-and-corrections.md) · [独立附录](../09-orders/120-angora-orders-dossier-2026-10-21.r120-appendix.md) · [主体映射](../09-orders/120-angora-orders-master-2026-10-21.mapping-r120.md) · [内部备忘](../../../107-followup-angora-r120/angora-networks.md) · [审计](../../../108-audit-r120.md)。

## 1. 日期基准 v3 更正与已推送成果修订

- **错误与修正**：r119 阶段材料及 r120 [`r120-progress-0002.txt`](../../../../../constitution/inbox/assistant-messages/r120-progress-0002.txt)、[`r120-time-conversion-clarification.md`](../../../../../constitution/issues/r120-time-conversion-clarification.md)、[`research-plan-before-requests.md`](../../../106-source-evidence-r120/research-plan-before-requests.md) 误将 `2026-10-26 UTC` 当作当前会话日期并声称存在冲突。现已发出 [`r120-date-correction-0004.txt`](../../../../../constitution/inbox/assistant-messages/r120-date-correction-0004.txt) 致歉纠正，并保留全部旧消息及 `constitution/history/r119-before-v3/` 字节备份。
- **时间事实边界**：当前会话日期为 `2026-11-22 UTC`。r119 来源中的 `2026-10-28`、`2026-10-30`、`2026-10-31` 均早于当前日期（但媒体／商会局部分块仍须按来源边界核实，且媒体未列 Angora 获奖）；`ticaretsicil.gov.tr` 公告的 `2026-12-01` 规则变更仍属未来；历史消息实际收发时刻依然未知，旧文件名中 `-2026-10-26`／`-2026-10-21` 不代表历史发送时间。

## 2. 安卡拉商会（ATO）公开路径核验：第 8 委员会名册与登录边界

| 观察对象 | 本轮实测最窄结果 | 不能推导的事项 |
|---|---|---|
| [ATO 第 8 委员会页 P01](../../../106-source-evidence-r120/pages/P01/chunk-1.protected-partial.json) | 公开显示 `8. BİLİŞİM TEKNOLOJİLERİ MESLEK KOMİTESİ`；第 2–6 块未取。 | 不证明 Angora 为该委员会会员或有公开登记号。 |
| [ATO 公开名册页 P02](../../../106-source-evidence-r120/pages/P02/chunk-1.protected-partial.json) | 显示 `8. KOMİTE LİSTESİ` 表头（含 `Ticaret Sicil No`、`Unvan` 等），页脚称 **6,695 条、显示 1–20 / 335 页**；第 1–20 条未见 Angora Networks。 | 工具 `hasMore=false` 仅指当前页抽取结束，**不等于查完 335 页**；未点击分页或下载全表，不能证明目标不在名册或非 ATO 会员。 |
| [ATO 会员信息页 P03](../../../106-source-evidence-r120/pages/P03/chunk-1.protected-partial.json) | 跳转链接指向 `portal.atonet.org.tr/.../login.htm`。 | 未点击或登录；不能据此断言全部 ATO 公开路径都要求登录。 |
| [ATO CDX 查询 A01/A02](../../../106-source-evidence-r120/archive-index/A01.cdx.tool-visible.manual.json) | `KomiteListe?komiteKodu=8` 在 `www` 与非 `www`、HTTP 200、`to=20261026` 过滤下返回 `[]`。 | 仅限该过滤参数（见 [r120 覆盖说明](../../../106-source-evidence-r120/date-scope-correction-v3.md)），不证明历史无捕获或企业未登记。 |

## 3. 官网隐私自述与 Wayback 历史回放：2021–2026 同一来源延续

- [当前英文隐私页 P04](../../../106-source-evidence-r120/pages/P04/chunk-1.protected-partial.json) 与 [Wayback 2021-04-11 19:01:59 UTC（北京时间 2021-04-12 03:01:59 +08:00）AR01](../../../106-source-evidence-r120/archive-replay/AR01.20210411190159.chunk-1.protected-partial.json)、[Wayback 2023-02-03 04:19:46 UTC（北京时间 2023-02-03 12:19:46 +08:00）AR02](../../../106-source-evidence-r120/archive-replay/AR02.20230203041946.chunk-1.protected-partial.json) 在第 0 块均自称 `Angora Networks Bilişim Teknolojileri A.Ş.`，而在独立请求的第 1 块中又同时出现单数 `ANGORA NETWORKS BİLİŞİM TEKNOLOJİ A.Ş`／`Angora Networks Bilişim Teknoloji A.Ş.` 与复数 `Teknolojileri A.Ş.`。
- **判断**：这种单复数混用自述至少自 2021-04-11 UTC 起即存在于同站模板中，并非近期变更；但 P04、r111 既录页面及 AR01/AR02 均属**同一品牌网站自述**，既不能充当多份独立证明，也不能替代官方工商原证或解决与 Find 候选全称 `ANGORA NETWORKS BİLİŞİM TEKNOLOJİ TİCARET SANAYİ ANONİM ŞİRKETİ` 之间的文字差异。

## 4. 官方机构公开索引与近名防混

- 公开搜索 [Q04](../../../106-source-evidence-r120/search-responses/Q04.tool-visible.manual.json)（`ticaretsicil.gov.tr`）、[Q07](../../../106-source-evidence-r120/search-responses/Q07.tool-visible.manual.json)（`turkpatent.gov.tr`）、[Q28](../../../106-source-evidence-r120/search-responses/Q28.tool-visible.manual.json)（`resmigazete.gov.tr`）、[Q29](../../../106-source-evidence-r120/search-responses/Q29.tool-visible.manual.json)（`kik.gov.tr`）、[Q32](../../../106-source-evidence-r120/search-responses/Q32.tool-visible.manual.json)（`sanayi.gov.tr`）均返回零结果；[Q30](../../../106-source-evidence-r120/search-responses/Q30.protected-partial.json)（`rekabet.gov.tr`）与 [Q31](../../../106-source-evidence-r120/search-responses/Q31.protected-partial.json)（`tubitak.gov.tr`）仅匹配无关企业或安哥拉动物研究论文。索引零结果不能作为实体不存在的否定证明。
- [Q02](../../../106-source-evidence-r120/search-responses/Q02.protected-partial.json) 与 [Q21](../../../106-source-evidence-r120/search-responses/Q21.protected-partial.json) 返回的 `angoratd.com` 载有北京／安卡拉商号与编号 `468722`，但指向近名不同域名网站，摘要未关联目标全称，**严禁合并或套用给 Angora Networks**。[Q01/Q20](../../../106-source-evidence-r120/search-responses/Q01.protected-partial.json) 仍只见对访客隐藏登记号的 Find 候选。

## 5. 诚实边界与停项保持

- 本轮全部 48 次工具请求均为人工保护性摘要／摘录或工具可见转录（无原始 HTML、无完整搜索响应、未抓取官网产品 PDF、未登录、未接触客户、未读取 Gmail／Drive 账户数据）。所有既有 PASS 持续有效；Ewind 无新增，分类不变。
