# Angora 仓库全量解读（读库笔记）

> 生成日期：2026-09-23　｜　分支：`arena/01a0ce39-angora`
> 方法：全量扫描 350 个文件，对 158 个含文本的文件（docx / doc / xls / xlsx / pdf / pptx / pub / txt）做全文抽取，共 4,727,325 字符，**抽取失败 0 个**，仅 4 个扫描件 PDF 无文字层（质保书 ×2、商会注册证、LK-Passport 芯片资料）。图片/视频/PSD/CDR/AI/DXF 无文字，已按文件名与所在目录定位用途。

---

## 一、这个仓库到底是什么

**不是代码库，是一个外贸业务的"活档案"。** 记录的是一条中土（中国郑州 ↔ 土耳其安卡拉）B2B 网络设备供应链两年半的完整经营过程：

```
深圳凌特华盛 SmartByte（ODM 工厂，Peter Hu）
        │  采购合同（人民币、款到生产）
        ▼
郑州仨戛通讯器材有限公司 / Zhengzhou Saga Telecom（Simon Cheng，程天龙）  ← 本仓库主
        │  PI / CI / PL / 采购合同 / 运费（美元，T/T 预付）
        ▼
ANGORA NETWORKS BİLİŞİM TEKNOLOJİ TİC. SAN. A.Ş.（安卡拉，Levent KILIÇ / Taylan ESEN）
        │  贴牌为 ANW- / TT- / TRX- 系列
        ▼
终端：Türk Telekom、土耳其警察总局 EGM/ÇGKS、土耳其政企与工程项目、欧洲（潜在）
```

**两个法人主体，一套人马**（仓库里两个抬头交替出现）：

| 中文抬头 | 英文抬头 | 角色 |
|---|---|---|
| 郑州仨戛通讯器材有限公司 | Zhengzhou Saga Telecom Co., Ltd. | 签约卖方 / 采购买方（对 SmartByte） |
| — | ANGORA NETWORKS BİLİŞİM TEKNOLOJİ TİC. SAN. A.Ş. | 买方（客户，土耳其，税号 ID 069 052 0220，Yenimahalle Vd） |
| — | TRONX BİLİŞİM VE SAĞLIK TEKNOLOJİLERİ LTD. ŞTİ. | Angora 关联的第二个品牌公司（Mustafa Çalık），未付款 |

**关键人物**：Simon Cheng（我方，销售/对接）、Levent Kılıç（Angora 老板，商务/战略）、Taylan Esen（Angora 技术）、Peter Hu（SmartByte 工厂）、Mustafa Çalık（TronX）。

---

## 二、业务模式（这是理解全库的主线）

**本质：Marvell 芯片方案的 L2+ 交换机 ODM/贴牌出口，以土耳其为基地，目标是借道进入欧洲。**

- **交易结构**：全部 EXW / T/T 预付，非品牌中性包装（无中文字样），HS Code 8517622990，DAP/CPT 到安卡拉。
- **付款演进**：小单 100% 预付 → 大单 30/20/50 → 谈过 50/50 与 30/70（首单大货走了 30/70 变体）。
- **收款通道演进**：中国银行河南分行（2024.05）→ JPMorgan Chase 香港（2025）→ **Banking Circle 丹麦全球账户**（可收 TRY 里拉，2025.06 起，专门为客户规避换汇损失）。
- **运费单独计价并加价**：运费是独立利润中心，内部规则是 **"收客户钱一律按照收费利润率 >30%"**（《运费一览表》表头原文）。
- **2% RMA 备件**：每 100 台附 2 台免费备件（写在 datasheet 里），在官方订单量中扣减或额外多发。

---

## 三、型号映射体系（三层命名）

| 工厂/Saga 型号 | 客户品牌型号 | 形态 |
|---|---|---|
| LT-S8552XGP-4XS48GT / STC-448XGGPM | ANW-3148-PX → ANW-2248-PG/PX → **TRX-AS-48TP4X** | 48 口商用 PoE，4×10G SFP+ |
| LT-S8528XGP-4XS24GT / STC-424XGGPM / STC-424DGGPM-280W | ANW-3124-PX → ANW-2224-PG/PX → **TRX-AS-24TP4X** | 24 口商用 PoE |
| LT-S8310GP-2GX8GT / STC-28DGGPM | ANW-3108-PG → **TRX-AS-8TP2G** | 8 口商用 PoE |
| LT-IS6318GP-2GX16GT | **ANW-2116-PG** | 16 口工业 PoE（2×2.5G 光）← 大货主力 |
| LT-IS6310G-2GX8GT / STI-280DGGM | **ANW-1108-V** → **TT-2208-TG**（Türk Telekom 样品） | 8 口工业非 PoE |
| STI-288DGGPM | **TRX-IS-8TP2G** / **TT-2208-PG** | 8 口工业 PoE |
| STH 系列（VastLakes/PeakNetX 平台） | — | 数据中心/园区 L3（CENTEC 方案，2025.12 引入） |
| CNX-2208/2224/2248-PG | Connexite（英国亚马逊） | 参考：Connexite 商业计划 |

**四个终端品牌**：`ANW-`（Angora）、`TT-`（Türk Telekom 定制）、`TRX-`（TronX）、`CNX-`（Connexite，英国）。

---

## 四、订单全表（含成本与利润，来自《成本统计.xlsx》）

| # | 合同号 | 日期 | 内容 | 数量 | PI 金额(USD) | 成本(RMB) | 收款(RMB) | 利润(RMB) | 利润率 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | STSC20240508007 | 2024-05-08 | 样品：ANW-3148-PX×1、ANW-3124-PX×1、ANW-3108-PG×2 | 4 | 1,265 | 6,991.42 | 9,150.38 | 2,158.96 | **23.59%** ⚠ |
| 2 | STSC20241021007 | 2024-10-21 | ANW-2116-PG×8、ANW-1108-V×2、PVC×100、软件定制费 | 10 | 1,545 (CI 2,345) | 10,967.61 | 16,721.51 | 5,753.90 | **34.41%** |
| 2b | STSC20241028007 | 2024-10-28 | ANW-2116-PG 软件改动 | 1 | 200 | — | — | — | — |
| 2c | STSC20241105007 | 2024-11-05 | ANW-2116-PG×3 | 3 | 600 | — | — | — | — |
| 3 | **STSC20250117007** | 2025-01-17 | **ANW-2116-PG 工业 PoE 大货 + 电源** | **178**（PI 行 356=178 交换机+178 电源） | **47,174** | 288,123.96 | 342,420.22 | 54,296.26 | **15.86%** ⚠ |
| 4a | STSC20250228007 (R1→R3) | 2025-02-28 | ANW-2224-PX / ANW-2248-PX（**在 Unshipped 目录**） | 7 | 2,130 (R3) | 采购合同 9,110 | ? | ? | 存疑 |
| 4b | STSC20250507007 (R1) | 2025-05-07 | ANW-2224-PX×3、ANW-2248-PX×3 | 6 | 1,665→1,920 | 9,705.99 | 11,933.07 | 2,227.08 | **18.66%** ⚠ |
| 5 | STSC20250526007 (R1) | 2025-05-26 | ANW-2224-PX×10、ANW-2248-PX×3（含首批 TronX 双标签） | 13 | 3,755 | 17,577.19 | 26,827.99 | 9,250.80 | **34.48%** |
| 6 | STSC20250619007 (R1) | 2025-06-19 | STI-288DGGPM / **TT-2208-PG**×6（Türk Telekom 演示单） | 6 | 900（另有 TRY 版：900 TRY） | 4,948.45 | 7,050.57 | 2,102.12 | **29.81%** |
| 7 | **STSC20250711007** | 2025-07-11 | TT-2208-PG×10 | 10 | **？** | **？** | **？** | **？** | **❗ 无目录无成本表** |
| — | STSC20241129007 | 2024-11-29 | TronX（Mustafa Çalık）41 件整机+光模块+AP | 41 | 1,755 | — | **未收款** | — | **❗ 未付款 1** |

**已确认 Angora 主体开票合计 ≈ USD 58,769**（未计 4a 存疑单与第 7 单）。
**⚠ 三单低于 30% 内部红线**：首单 23.59%、176 台大货 15.86%、第 4b 单 18.66%。

### 运费利润表（《运费一览表.xlsx》）

| 合同号 | 均价/Kg | 收费(USD) | 实际成本(RMB) | 收费利润率 |
|---|---|---|---|---|
| STSC20240508007 | 13.33 | 200 | 991.42 | 30.67% |
| STSC20241021007 | 18.54 | 445 | 2,093.61 | 34.20% |
| STSC20250117007 | 8.89 | 4,000 | 22,425.96 | **21.59%** ⚠ |
| STSC20250507007 | 10.61 | 350 | 1,515.99 | 39.42% |
| STSC20250526007 | 10.00 | 700 | 2,829.55 | 43.47% |
| STSC20250619007 | 13.00 | 125 | 646.45 | 27.67% |

规律：重量大≈9 元/Kg，重量小≈13 元/Kg。大货单（176 台）运费利润率只有 21.59%，未达标。

---

## 五、项目漏斗（RFP / 在谈项目）

| 项目 | 规模 | 状态 |
|---|---|---|
| **Türk Telekom 工业交换机**（385 台 STI-280DGGM） | 385 台 | 客户内部 paperwork 卡住，长期 pending |
| **Türk Telekom 2026 采购周期**（TT-2208-PG/TT-2208-TG） | 6→10 台已出，目标 2,000–3,000 台 | 样品已交付并在 2025.02.03 送测；SFTP/HTTPS 为敲门砖 |
| **Türk Telekom 数据中心**（Type-1: 48×25G+6×100G / Type-2: 48×GE+4×10G） | — | RFP 已收（2025.12.17 包），需 MLAG/堆叠/MACsec/双电源 |
| **土耳其警察总局 EGM / ÇGKS 2026** | **3,294 台** | 规格已译完；**致命门槛：须持 EGM BİLTEM「C 型边缘交换机与流量整形测试报告」且结果为 SUCCESSFUL** |
| **KGYS 项目**（C 型以太网交换机） | — | 2024.07 RFP，STI-288DGGPM 应标 |
| **Turkcell 大 RFP**（2024.5.27，千条需求） | — | 大量 NON-COMPLIANT（PIM/NAT/BFD/VRF-Lite/OpenFlow/Y.1731/TWAMP/RTR Tracking） |
| **250/300+ 台工业交换机**（2024.06–07） | 250+250 台 | 卡在 SFTP 研发与 HTTPS 芯片切换 |
| **48 口 150 台报价**（2024.12.03） | 150 台 | 仅报价，无订单；L2+ $360 / L3 $560 |
| **国防 16 口项目**（2024.12） | 16 口 | 与 Maipu 竞标，价格报高，基本放弃 |

**技术能力边界（Saga Marvell 方案）**——反复出现的硬伤：
- ❌ 不支持：PIM、NAT、VRF-Lite、BFD、Y.1731、TWAMP、RTR Tracking、OpenFlow/Netconf-YANG、MPLS
- ⚠ 部分/待确认：OSPF（在 L3 型号有，CLI 需核实）、堆叠（3.5 层）、IS-IS、BGP、VRRP（均标 "L3 only"）
- ✅ 已攻克：**SFTP**（2024.07 立项，8~10 周，$110/台，8K USD 研发押金，可抵货款）、**HTTPS**（换 Marvell AC5 芯片解决）、ACL、sFlow
- ❌ 做不了：工业机 DI/DO（RS485 成熟，DI/DO 软件未就绪）、非 PoE 机型读取输入电压、输入电压显示

---

## 六、定制化规则体系（已固化的 SOP）

这是仓库里最"可复用"的资产，Angora 回复已逐条确认：

- **常规五改**：IP 地址、型号名、序列号、MAC、Logo（免费）
- **序列号规则**：以 `ANW` 开头，其余按 Saga 格式（如 `25012116XXX03`，XXX = 001~178）；基于生产日期
- **字体**：Helvetica 或 Arial（不用 Times New Roman）
- **标签**：**必须去掉 "Made in China"**；电源线欧标；型号描述用客户型号
- **Logo**：固定用 Angora 蓝色 logo（.ai 源文件已提供），除非客户明确更换
- **User Manual**：只换品牌名为 ANGORA NETWORKS，其余不动
- **质保**：出 Certificate of Warranty（无保修卡）；3 年质保 + 终身技术支持
- **PVC 面膜**：100 片 $2.3/片，300 片 $1.5/片；余料存 Saga 仓，按订单扣减（《PVCs.xlsx》已建台账）
- **MAC 地址**：用客户提供的段（`98:06:37:A0:57:xx` / `98:06:37:A1:00:00~A4:FF:FF` / `98:06:37:A5:00:xx`）
- **拍照**：发货前发实物照；**同型号重复采购不再重复拍照**
- **清关**：Saga 只在发货前改 CI 协助，土耳其进口清关由 Angora 自理
- **包装盒**：中性（因同箱型跨型号/跨客户复用），仅印 Logo

**MAC/序列号总账**：`mac_address&serial_number.xlsx`，1,537 行，已用到 `98:06:37:A5:00:22`。

---

## 七、供应链

- **ODM 工厂**：深圳凌特华盛科技有限公司 SmartByte（惠州厂区），联系人 Peter Hu `peter@smartbyte.com.cn`
- **电源供应商**：鹰峤（Yingjiao），为 176 台订单供 240W 电源（2 只样品已做中性测试）
- **货代/清关**：UPS / FedEx / DHL 空运门到门；`买单报关`（代理进口报关）模板已固化；土耳其入仓标签（WE 开头 PDF）
- **出货流程**：PI → 采购合同（对 SmartByte）→ 生产 → 拍照确认 → 尾款 → PL/CI → 买单报关表 → 快递发票 → 入仓标签 → AWB

---

## 八、战略演进时间线（这是全库的"剧情"）

| 时间 | 事件 |
|---|---|
| 2024-04-28 | Simon 冷邮件开发 Angora，主打 Marvell L3 工业交换机 |
| 2024-05 | 首单样品（$1,265） |
| 2024-06~07 | Türk Telekom 250 台项目；SFTP 研发谈判；HTTPS 芯片方案 |
| 2024-10-21 | 第二单 + **Simon 提交《Proposal》：邀请 Angora 做欧盟分销商** |
| 2024-10-31 | WeChat 会议：30/70 付款、CKD/SKD、库存投资、软件定制、欧盟拓展 |
| 2024-12 | 176 台大货谈判（ enclosure/PVC/付款/物流）；Türk Telekom 2,000~3,000 台 RFI |
| 2025-01 | **176 台大货落地（$47,174）**，Saga 首次大货，给 5% 折扣 |
| 2025-02 | TT 样品送测（TT-2208-TG）；SFTP/HTTPS/sFlow/ACL 是通关关键 |
| 2025-05~07 | 4/5/6 单连续出货；第 5 单起**同时出 Angora 与 TronX 两套标签**；TT-2208-PG 6 台 → 10 台 |
| 2025 全年 | 《加深关系绑定》：送样、本地化、软件定制、方案商、伊斯坦布尔 office、联合 GTM |
| **2025-12-17** | **Saga 战略转向：锁死 Marvell L2+ + CENTEC L3 双芯片方案**；释出 STH 系列（VastLakes / PeakNetX 平台）、STOS V2.4 |
| 2026-02-12 | 土耳其警方 ÇGKS 2026 规格批准（3,294 台） |
| **2026-07-31** | **Levent 反向提案：《SAGA Enterprise L3 Recommendation Report》——请求 Saga 开发企业级 L3** |
| **2026-08-17** | **Simon 拟回复《Reply on SAGA Enterprise L3...》：拒绝自研 L3，改推 CENTEC** |

---

## 九、当前核心矛盾（2026 年，最需要关注）

**Angora 要企业级 L3，Saga 给不了，只能转卖 CENTEC。**

Levent 的诉求（4 项硬件 + 全套 L3 软件）：
- 硬件：堆叠（4–8 台）、USB 固件升级口、OOB 管理口、冗余/热插拔双电源、PoE 802.3bt
- 软件：OSPFv2/v3、VRRP（含抢占）、BGP4/4+、VRF、ECMP/BFD（IS-IS/MPLS 放二期）
- 商务测算：企业级 24 口 $600–1,200 / 48 口 $1,500–2,500，是 Saga 现旗舰（$340/$530）的 **2–4 倍**。
- 承诺：联合路线图评审（4–6 周内）、提供现场需求与销量预测、谈**优先伙伴条款**。

Simon 的回复立场（2026-08-17）：
1. **Marvell 已从 AC3 全面切到 AC5**；AC3 只做技术支持，`lite-hotfix-7.3.13` 是最后一版（Angora 已集成进自家 NMS）
2. 技术资源全押 **L2+**；对多数 L3 型号持"let it be"态度（ROI、需求、售后成本）
3. 近 6 个月 **RAM/DDR 与 PCB 涨价**，公司经营现金流承压
4. **反提案**：① 先测 AC5 现成机型；② 重审 L3 功能清单收客户反馈；③ **评估 CENTEC 方案（上述功能现成）**——并明确"**Saga 已把芯片方案锁死在 Marvell L2+ + CENTEC L3，这是战略动作**"

> **风险点**：Angora 若不接受 CENTEC，可能转而自建 L3 供应（Levent 原文："a gap we would much rather close together... than address elsewhere"——这句是委婉的"否则我去别家"）。第 6 页明确写了要"Preferred-partner terms"。

---

## 十、我读出的 12 个缺口 / 异常（建议优先处理）

| # | 问题 | 位置 | 严重度 |
|---|---|---|---|
| 1 | **第 7 单 STSC20250711007（TT-2208-PG×10）无目录、无 PI、无成本表**，只在 MAC 台账出现 | `mac_address&serial_number.xlsx` | 🔴 高 |
| 2 | **Tronex 单 STSC20241129007（$1,755，41 件）长期未付款** | `未付款 1/` | 🔴 高 |
| 3 | **176 台大货 PI 文本错误**："SAY TOTAL IN USD ONE THOUSAND FIVE HUNDRED AND FORTY FIVE" —— 从上单复制粘贴未改，实际金额 $47,174 | `STSC20250117007.xls` | 🔴 高（清关/法律风险） |
| 4 | 第 6 单收款记录 **$990 vs PI $900**，差 $90 未说明 | `成本统计.xlsx` / `STSC20250619007` | 🟡 中 |
| 5 | 第 4b 单收款 $1,665，但 R1 版 PI 为 $1,920，差 $255 | `成本统计.xlsx` / R1 PI | 🟡 中 |
| 6 | 运费表 STSC20250526007 实际费用 **2,829.55** vs 成本统计 **2,947.19**，差 117.64 | 两份表 | 🟡 中 |
| 7 | **4a 单 STSC20250228007 状态不明**：位于 `Unshipped/` 却已有采购合同(RMB 9,110)、发货照片、付款记录、PL | `4th order/Unshipped/` | 🟡 中 |
| 8 | **三单利润率低于 30% 红线**（23.59% / 15.86% / 18.66%），大货单最低 | `成本统计.xlsx` | 🟡 中 |
| 9 | 大货运费利润率 21.59%，未达 >30% 内部规则 | `运费一览表.xlsx` | 🟢 低 |
| 10 | **警方项目致命门槛**：EGM BİLTEM「C 型边缘交换机与流量整形测试报告」未解决，3,294 台无从谈起 | `警察局项目/` | 🔴 高（若要投标） |
| 11 | 仓库存在**重复文件**：同款 User Manual 在 4th/5th 单各存 2 份；PL/CI 有 R1~R3 多版 | 多处 | 🟢 低（占空间） |
| 12 | `INFO_2025.12.17/INFO.rar`（51 MB）、`IoT Board/PC0012_Saga.7z`（9 MB）未解压，内容未知；`RFP/` 两个 MP4（85 MB + 32 MB）为沟通录像未看 | — | 🟢 低 |

---

## 十一、关键文件速查

| 想看什么 | 看哪个文件 |
|---|---|
| 全部订单成本利润 | `成本统计.xlsx` |
| 运费加价规则 | `运费一览表.xlsx` |
| MAC/序列号总账 | `mac_address&serial_number.xlsx` |
| PVC 面膜库存台账 | `PVCs.xlsx` |
| 土耳其潜在客户名单（300 行） | `Turkey Client List.xlsx` |
| 欧盟分销提案（原始版） | `Proposal.docx` |
| 客户绑定策略（含 GPT 建议） | `加深关系绑定.docx` |
| 2025/2024 年度会议议程 | `Agenda for WeChat meeting at 2025.docx` / `...2024.10.31.docx` |
| RFP 逐条技术应答 | `RFP/` 目录（9 个 docx + 2024.5.27_RFP.xlsx 千条需求） |
| Türk Telekom 测试项 | `RFP/Turk_Telekom_Test_Items.xlsx` |
| Saga 软件功能清单（AC3 vs AC5） | `RFP/Saga Software Function List-release 7.3.0.xlsx` |
| Saga 最新功能清单（STOS V2.4，2025.12.12） | `INFO_2025.12.17/Saga Software Function List_EN.pptx` |
| 数据中心交换机平台 | `INFO_2025.12.17/STH1G`、`STH25G`、`Performance of PeakNetX/VastLakes` |
| 警方项目规格（中/英/土） | `警察局项目/`（EGM.txt、KGYS.txt、ÇGKS.txt + 3 个 PDF） |
| **最新战略文件** | `SAGA Enterprise L3 Recommendation Report.pdf`（客户来，2026-07-31） |
| **我方拟回复** | `Reply on SAGA Enterprise L3 Recommendation Report.docx`（2026-08-17） |

---

*本文件为读库笔记，可随时删除。所有数字均直接来自原文件，未做推算；标注"存疑/未说明"处需人工核对原始凭证。*
