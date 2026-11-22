# r119 · Angora：工商原证路径、同名防误认与活动证据再核

> **结论**：本轮找到了土耳其商事公报的公开入口，但两条匿名查询入口均落到登录页；没有取得 Angora 的工商登记原件。Kırıkkale 商会索引摘要与另次 PDF 分块观察存在行号差异，不能据此认定编号、注销或分支法律关系。另一个近名企业由 Kocaeli 园区关联到不同域名，须单独保留、不可与 Angora Networks 自动合并，也不能断言二者绝无关系。沿用原档，**法人主体未确认**。

[来源目录](../../../103-source-evidence-r119/source-catalog.csv) · [逐项证据锚](../../../103-source-evidence-r119/evidence-traceability.csv) · [问题与更正](../../../103-source-evidence-r119/issues-and-corrections.md) · [独立附录](../09-orders/120-angora-orders-dossier-2026-10-21.r119-appendix.md) · [主体映射](../09-orders/120-angora-orders-master-2026-10-21.mapping-r119.md) · [内部备忘](../../../104-followup-angora-r119/angora-networks.md) · [审计](../../../105-audit-r119.md)。

## 1. 商事登记：找到了路径，不等于拿到了原证

[土耳其贸易登记公报首页 P13](../../../103-source-evidence-r119/pages/P13/ticaretsicil.gov.tr/index.protected-partial.manual.md)列出公告和名称查询入口，并显示免费查询的登录提示；当前通知还提到会员／电子政府登录以及自标 `01.12.2026` 的拟议变更。对首页列出的[名称查询 P15](../../../103-source-evidence-r119/pages/P15/response-metadata.json)和[公告查询 P16](../../../103-source-evidence-r119/pages/P16/response-metadata.json)，本轮匿名 GET 返回的 URL 均是登录页；工具没有提供完整 HTTP 重定向链。**未输入凭据、登录、提交表单或绕过验证码**。这只证明本次两个入口的可见结果，不等于所有官方登记途径都不可用，也不是 Angora 的登记证明。

[r118 Find 分支候选](../../../99-source-evidence-r118/institutional-pages/P05/www.find.com.tr/Company/angoranetworksbilisimteknolojiticaretsanayianonimsirketikirikkalesubesi/chunk-0.visible.manual.md)仍是有价值但**未经验证**的商业目录条目：其称 Kırıkkale 分支、同一网站域名和 `24 Mart 2023` 成立，实际编号对访客隐藏。不能把此日期写成已核工商成立日、实际入园日或法律母子关系。

[商会搜索 Q33](../../../103-source-evidence-r119/search-responses/Q33.protected-partial.json)再次把目标名称与 `336 / 009581` 放在同一搜索摘要；但[另三次商会 PDF 分块观察 P02](../../../103-source-evidence-r119/pages/P02/protected-blocks-observations.json)中，块 7 的第 336 行是其他主体，块 5 可见 `009572` 后接 `009610`。另次取回的[第 0 块表头](../../../103-source-evidence-r119/pages/P02/kirikkaletso.org.tr/ktso/basin/uyeler/4.GRUP.pdf/chunk-0-header.protected-partial.manual.md)自标 `31.10.2026`；不同请求及索引可能对应不同版本。本轮没有完整 PDF 原字节或全文件负检，故**不能核实 009581、认定不存在／注销或确定历史身份**；搜索 `pageAge` 也不是 PDF 日期。Q33/Q34 只是重复索引，不是新的独立登记。

## 2. 两个近名主体：分开保留，不猜法律关系

| 来源中的条目 | 本轮可见的最窄事实 | 处置 |
|---|---|---|
| `ANGORA Teknoloji Çözümleri San. ve Tic. Ltd. Şti.` | [Kocaeli 大学科技园名单](../../../103-source-evidence-r119/pages/P04/kouteknopark.com/firmalarimiz/chunk-0.protected-partial.manual.md)和[同一园区详情](../../../103-source-evidence-r119/pages/P06/kouteknopark.com/firma-detay/id-50/chunk-0.protected-partial.manual.md)把近名、Kocaeli 园区地址语境及 `angoratech.com` 放在同一条目。 | 是**防误认线索**，不是已核法人；不当作现有 Angora Networks 客户，也不断言它与目标绝无关联。 |
| `Angora Networks Bilişim` | [CompAtlas Kırıkkale 目录](../../../103-source-evidence-r119/pages/P08/compatlas.com.tr/sehir/kirikkale/gomulu/chunk-0.protected-partial.manual.md)列短名称；[单次双域名搜索 Q32](../../../103-source-evidence-r119/search-responses/Q32.tool-visible.manual.json)的摘要另把此短名称与 `angoranetworks.com` 关联。 | 搜索摘要可能跨段拼接，目录信息也可能来自企业／园区；不能靠名称、域名或地区推断工商主体或法律关系。 |

[CompAtlas 的 Kocaeli 条目](../../../103-source-evidence-r119/pages/P07/compatlas.com.tr/sehir/kocaeli/gomulu/chunk-0.protected-partial.manual.md)与 Kırıkkale 条目同属一个商业目录，不算两个独立工商登记。智慧城市近名详情请求 [P03 返回 HTTP 500](../../../103-source-evidence-r119/pages/P03/response-0.error.json)，不能把搜索摘要称为已取得的政府正文。

**增补而不取代 r118**：2023-09-21 18:44:25 UTC 的 `www` 园区回放换算为 **2023-09-22 02:44:25 北京时间**；r118 保存的四份人工文字对 `angora` 字面扫描为零。r116 保存的 2024-09-20 另一主机回放列名及域名。不同主机／版式和潜在别名使二者无法推导入园区间，也不能否定 Find 的候选；2023 年采访所称 `teknokent` 未点名 Kırıkkale。各来源分别保留。

## 3. 能源项目：候选、结果报道与日期不可混为一谈

| 材料 | 来源实际写了什么 | 限定 |
|---|---|---|
| [r115 行业媒体预告](../../../85-source-evidence-r115-2026-10-26/external-visible/www.enerjimagazin.com/haber-epdk-ve-elder-in-enerjim-sensin-programinda-finalistler-aciklandi-12770.html/chunk-0.visible.md) | 当前文字自标 `20 Ekim 2026 14:53`，援引 ELDER，列包括 Angora Networks 在内的 20 个候选，并称 10 月 28 日展示。 | 没有取得该页在会话日的可信历史快照；自标日期不是已验证发表时刻，候选不等于采购或获奖。 |
| [ELDER 组织方 P11](../../../103-source-evidence-r119/pages/P11/elder.org.tr/bilgi-bankasi/haberler/enerjim-sensin-2026/chunk-0.visible.manual.md) | 自标 `25 Eylül 2026`，说明项目培训、实验室、投资与奖金机会；保存文字未列 Angora 名称。 | 它是一般项目介绍，不是目标最终名单，也不能用零命中证明目标未参与或已获得支持。 |
| [Ekonomim P01](../../../103-source-evidence-r119/pages/P01/www.ekonomim.com/ekonomi/enerji-ihtiyaclarina-iyi-cozum-getiren-3-proje-odullendirildi-haberi-927872/chunk-0.visible.manual.md)；[Yeşil Haber P09](../../../103-source-evidence-r119/pages/P09/yesilhaber.net/enerjim-sensin-2026-uc-girisime-4-milyon-tl/chunk-1.protected-partial.manual.md) | Ekonomim 正文自标 **10 月 30 日**发表，称 10 月 28 日决赛，三名获奖者为 Pulse Systech、AT-AK、VoltGuard；Angora 在另列的方案段落而非获奖段。Yeşil Haber 声称依据 ELDER 的结果，三个名字相同。 | **这些是来源自述**；前述决赛／发表日期晚于本轮提供的 10 月 26 日会话基准，不能声称当日已发生或奖项已核。两家媒体可能依赖同一 ELDER 信息，不等于两个独立亲历证人；尤其不能称 Angora 获奖。 |

[文字比较](../../../103-source-evidence-r119/claims-comparison-result.json)在保存的两个媒体转录中，将 20 个候选名与 20 个方案标题作文本匹配，其中 5 个匹配依赖人工别名；不能据此认定 20 个法律主体、实际出席或项目成功。三项报道金额的文本相加为 400 万土耳其里拉，**不是本轮独立核实的授奖或拨款**。P01 的搜索 `pageAge` 为 10 月 29 日，与正文自标 10 月 30 日不同；[转录错误和重取分别保留](../../../103-source-evidence-r119/P01-transcription-correction-and-P12.md)。

## 4. 2022 活动：修正搜索拼接和本轮正文漏认

Q31 搜索摘要把 `17 Kasım 2022` 标题与 Taylan 的名字放近；[当前组织方议程第 0 块](../../../103-source-evidence-r119/pages/P17/kamubib-bimy.org/2022/program/chunk-0.protected-partial.manual.md)显示 17、18、19 日连续标题，并在 **19 日**闭门会议名单列 Levent。独立请求的[第 1 块](../../../103-source-evidence-r119/pages/P17/kamubib-bimy.org/2022/program/chunk-1.protected-partial.manual.md)列 Taylan 的另一分会，但本块没有前置日期；不能将搜索摘要直接当成 17 日分会，亦不能强拼独立请求成同一快照。r114 的 2022-12-04 归档同样分块，较早 7 月版还混有 2021 年日期，[具体对照](../../../103-source-evidence-r119/2022-agenda-search-splice-observation.md)。

**修正本轮一度称“尚未抓 KobiEfor 正文”**：r111 已保存[活动媒体报道正文](../../../69-source-evidence-r111-2026-10-26/external-visible/kobi-efor.com.tr/kapak/tbdden-kamu-bib25-ve-bimy29-butunlesik-etkinligidijital-h15774/index.visible.md)，r114 也已据此说明：媒体自称活动赞助商并报道 Taylan 的发言，未获原音；闭门会议报道没有点名 Levent 实际到场。组织方议程和媒体赞助商可能信息相互依赖，**议程、报道、实际采购／交付不可互相替代**。

## 5. 时钟、范围及下一步

- 本轮提供的日期为 **2026-10-26 UTC**，不是用户设定的截止；[time.is 工具可见文本](../../../103-source-evidence-r119/time-reference/time.is/Beijing/chunk-0.visible.manual.md)显示 **2026-11-22 15:09:20 北京时间**，与会话日期冲突，未经独立校准。网页自标日期、Wayback UTC 捕获、动态观察及历史消息的真实收发时间分别记载，未知就保持未知。[第二版更正](../../../../../constitution/issues/r119-time-and-source-date-correction-v2.md)。
- 本轮 40 次搜索索引含 109 个结果项（包括重复和删节），5 次零结果；25 次页面分块请求、5 次归档索引和 1 次时间参考，其中 4 次失败。[单请求索引](../../../103-source-evidence-r119/request-outcomes.csv)。文本为人工转录、重构或保护性摘录；缺原始 HTML／PDF、部分分块、第三方资料、现场原音及工商原件，详见[来源说明](../../../103-source-evidence-r119/README.md)与[审计](../../../105-audit-r119.md)。
- **全量读取完成（仅限定清单）**：先列的 r115–r118／相关规则与来源 **1,081/1,081 路径、83,394,100 bytes**，抽检 35/35；另对 r114/r111 活动材料作补救先列后重读 **22/22、186,101 bytes**，抽检 8/8。扩展材料此前曾先看局部，已公开说明；这些范围有重叠，不代表全仓、原网页逐字节一致或人工语义全审。
- 本轮不联系客户；Gmail／Drive 开关已启用但没有读取、修改或发送账户数据。所有既有 PASS 持续有效；后续仅在合法授权下被动核官方原证或可信旧快照，不要凭搜索结果向任何人联系。Ewind：本轮无新增事实（实际观察时刻未知），相对 r118 分类无变化；Ewind 是对手，Larch／NEM 不是。
