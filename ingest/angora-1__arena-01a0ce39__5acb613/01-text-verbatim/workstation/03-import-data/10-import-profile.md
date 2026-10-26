# Angora Networks — 土耳其进口情况调查

> 调查日期 2026-09-23 · 数据来源：Volza、TurkeyTradeData、ExportGenius、NBD 等公开海关数据平台

## ⚠️ 最重要的发现（先看）

**在 Angora 的海关进口记录中，前三大供应商是 Ewind、Larch Networks、Neme Engae —— 我方（郑州仨戛 / Saga Telecom）未进入前三。**

| 排名 | 供应商 | 国别 | 备注 |
|---|---|---|---|
| 1 | **Ewind Technology Co Ltd** | 中国 | 中国交换机厂商。我方《Turkey Client List》备注中曾出现"也有 **Ewind** 的" —— 是土耳其市场上与我方正面竞争的国产交换机品牌 |
| 2 | **Larch Networks Ltd** | **以色列** | larch-networks.com。**同时被 Angora 官网列为"Teknoloji Ortaklarımız（技术伙伴）"之一** |
| 3 | **Neme Engae Technology Co Ltd** | 中国 | 疑为"Neme Engineering Technology"，待核 |

> 这意味着：**Angora 的交换机供应链是多元化的**，Saga 只是其中之一，且从海关数据看并非主力。
> 这一点与其在《SAGA Enterprise L3 Recommendation Report》中"Angora 视 Saga 为基础制造伙伴（foundational manufacturing partner）"的表述**存在落差**，需要在谈判中警惕。
> 补充：以色列 Larch Networks 出现在供应商名单里，也解释了为何 Angora 能从以色列进口 7 票（15.56%）。

---

## 1. Volza 海关数据档案

**公司名（海关口径）**：`Angora Networks Informatics Technology Trade Industry Joint Stock Company`
**公司页**：https://www.volza.com/company-profile/angora-networks-informatics-technology-trade-industry-joint-stock-company-54698404/
（注：Volza 站点有反爬安全校验，直连被拦截；以下数据取自搜索引擎收录的页面摘要）

```
【进口 Import】
Shipments（票数）  : 45
Suppliers（供应商数）: 15
Competition        : 75,696

【出口 Export】
Shipments（票数）  : 2
Buyers（买家数）    : 2
Competition        : 21,281

【汇总】47 Bill of Ladings（提单），2 Buyers，15 Suppliers
【决策人】20 Decision Makers（付费可见）

【进口来源国】
  China   : 37 票（82.22%）
  Israel  :  7 票（15.56%）
  Germany :  其余（约 1 票 / 2.22%）

【进口商品 HS 编码】8517、8544、8471
【主要供应商】Ewind Technology Co Ltd、Larch Networks Ltd、Neme Engae Technology Co Ltd

【出口市场】Jordan（约旦）、Russia（俄罗斯）
【出口商品 HS】8517
【出口买家】Ltd Industr Al Network Solut Ons、Mubadara Eng Neer Ng Serv Ces Co Ltd
            （Volza 数据有字符脱敏/错切，原文如此）

【样本提单 Sample Bill of Lading】
  Date            : 08-11-2023
  Quantity        : 1
  Quantity Unit   : PCS
  Shipment Origin : China
  Marks Description : "Portable numerical (digital) Automatic Information Processing Machines
                       (at least one central trading unit in the same cabin, consisting of a
                       keyboard and a screen and do not exceed 10 kgm.)"
  → 按描述属 HS **8471**（便携式数字自动数据处理设备，即笔记本/工控机类），非交换机
  另一条：Quantity Unit UNT_2951543，Shipment Origin Turkey（出口方向）
```

### HS 编码释义
| HS | 含义 |
|---|---|
| **8517** | 电话/电报用电气设备；**8517.62** = 用于接收、转换、发送或再生语音/图像/数据的设备，**含交换与路由设备**（即交换机、路由器） |
| **8544** | 绝缘电线、电缆及其他绝缘电导体；光缆 |
| **8471** | 自动数据处理设备（计算机/笔记本/服务器等） |
| 土耳其本国细分类 | `851762009000`（Module 等）、`851762001000`（Switch） |

> 参考：我方（Saga）在 PI 上使用的 HS Code 为 **8517622990**。

---

## 2. TurkeyTradeData 档案

**公司名**：`Angora Networks Bilisim Teknoloji Ticaret Sanayi Anonim Sirketi`
**页面**：https://www.turkeytradedata.com/search/im/imp/co-angora-networks-bilisim-teknoloji-ticaret-sanayi-anonim-sirketi

```
统计区间 : 2023-08-01 ~ 2024-07-31
Total Shipments : 21
Total Importers : 1
来源国 : CHINA
产品 : Networks Switch
Total Value : $44.90K
```

**与我方记录的交叉核对（同一区间内的我方出货）**：

| 合同号 | 日期 | PI 金额 | 是否在 2023-08~2024-07 区间 |
|---|---|---|---|
| STSC20240508007 | 2024-05-08 | $1,265 | ✅ |
| STSC20241021007 | 2024-10-21 | $1,545（CI $2,345） | ❌（晚于 2024-07-31） |
| STSC20241028007 | 2024-10-28 | $200 | ❌ |
| STSC20241105007 | 2024-11-05 | $600 | ❌ |
| STSC20241129007 | 2024-11-29 | $1,755（未付款） | ❌ |
| STSC20250117007 | 2025-01-17 | $47,174 | ❌ |

> **结论**：TurkeyTradeData 统计的 21 票 / $44.9K（2023-08~2024-07）**基本不包含我方订单**，
> 说明该区间内 Angora 的进口主要来自 **Ewind / Larch / Neme Engae 等其他供应商**。
> 我方的大额订单（176 台 / $47,174）发生在 2025-01，落在该统计窗口之外。

---

## 3. 口径与局限说明

1. **土耳其海关数据本身有"贸易数据镜像"性质** —— 各平台（Volza / TurkeyTradeData / ExportGenius / NBD / tradedata.pro）抓取的是同一批提单，但**时间窗与去重规则不同**，故票数差异大（45 vs 21）。
2. **金额口径存疑**：$44.90K / 21 票 与我方已知订单金额量级不匹配，推测平台只覆盖了部分提单，或按 CIF/FOB 折算。
3. **供应商名存在脱敏/错切**：Volza 对供应商名做了字符级脱敏（如 "Ltd Industr Al Network Solut Ons" = "Ltd Industrial Network Solutions"），需以付费版原始数据为准。
4. **我方是否出现在完整供应商名单中，需付费解锁** —— Volza 页面明确 "20 Decision Makers / 15 Suppliers" 为付费内容。
5. 沙箱无法直连 Volza / LinkedIn，本文件数据均来自搜索引擎收录的页面摘要，**建议后续人工登录核对**。

---

## 4. 建议的下一步（需要时可做）

| 动作 | 价值 |
|---|---|
| 购买 Volza / ImportGenius 单份报告，拉出 15 家供应商全名单 + 逐票明细 | 确认 Saga 的真实份额排名 |
| 按 HS 8517.62 拉 Angora 近 24 个月进口明细，按供应商聚合 | 看清份额走势（我方是在上升还是下降） |
| 排查 **Ewind Technology** 的工商信息与产品线 | 明确主要竞争对手 |
| 排查 **Larch Networks（以色列）** 产品线 | 解释 Angora 为何有以色列进口；判断其是否为 Angora 高端机型来源 |
| 交叉比对：Angora 2026 新增的 **SYNAPSE / HITIT / VERGE(2026)** 型号，是否对应上述某家供应商 | **判断我方是否被替换** |

---

## 5. 相关：我方已知的出货记录（供比对）

| 合同号 | 日期 | 内容 | 数量 | PI 金额 | HS |
|---|---|---|---|---|---|
| STSC20240508007 | 2024-05-08 | ANW-3148-PX×1、ANW-3124-PX×1、ANW-3108-PG×2 | 4 | $1,265 | 8517622990 |
| STSC20241021007 | 2024-10-21 | ANW-2116-PG×8、ANW-1108-V×2、PVC×100、软件费 | 10 | $1,545（CI $2,345） | 8517622990 |
| STSC20241028007 | 2024-10-28 | ANW-2116-PG 软件改动 | 1 | $200 | 8517622990 |
| STSC20241105007 | 2024-11-05 | ANW-2116-PG×3 | 3 | $600 | 8517622990 |
| STSC20241129007 | 2024-11-29 | TronX 41 件（整机+SFP+AP） | 41 | $1,755（**未付款**） | 8517622990 |
| STSC20250117007 | 2025-01-17 | ANW-2116-PG×178 + 电源×178 | 356 行 | $47,174 | 8517622990 |
| STSC20250228007 | 2025-02-28 | ANW-2224-PX / ANW-2248-PX | 7 | $2,130（R3） | 8517622990 |
| STSC20250507007 | 2025-05-07 | ANW-2224-PX×3、ANW-2248-PX×3 | 6 | $1,920（R1） | 8517622990 |
| STSC20250526007 | 2025-05-26 | ANW-2224-PX×10、ANW-2248-PX×3 | 13 | $3,755 | 8517622990 |
| STSC20250619007 | 2025-06-19 | TT-2208-PG×6（Türk Telekom 演示） | 6 | $900 | 8517622990 |
| STSC20250711007 | 2025-07-11 | TT-2208-PG×10 | 10 | **无记录** | — |

> 运输方式：UPS / FedEx / DHL 空运门到门（DAP/CPT Ankara）；**快递渠道通常不产生正式海运提单（B/L）**，
> 这也可以部分解释为何海关提单数据与我方订单记录难以一一对应。
