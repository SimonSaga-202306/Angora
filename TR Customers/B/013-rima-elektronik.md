# 13 · Rima Elektronik

> **评级**：B ｜ **我方评估**：**68**/100 ｜ **核验日期**：2026-10-21
> **一句话**：**安防/网络分销（工业线为主）**

---

## 身份卡

| 项 | 内容 |
|---|---|
| 公司 | Rima Elektronik |
| 层级 | B |
| 总部/城市 | Ankara |
| 场景/定位 | **安防/网络分销（工业线为主）** |
| 自有品牌 | 无（品牌分销） |
| 名单来源 | —（用户侧） |
| 源表位 | 13 |

## 我方核实的交换机产品线

**Antaira（全球工业 IT 品牌）工业 switch 线**：LNX-1002C-SFP（10 口 8×10/100+2G combo，冗余 DC，5 年保修）+ **switch 类目库存 103 项**

## 当前供应链（核实口径）

Antaira（黄灯专业品牌，全球供应商）

## 联系人（逐字抄录）

```
Salih Senyurt（Corp Sales Dir）/ Toyan Karahan（PM）/ Aycan Tuerkay（GM）
```

## 证据与核实等级

| 项 | 内容 |
|---|---|
| 证据来源（独立核实） | rimaelektronik.com 官网（Antaira LNX-1002C-SFP 产品页 + 库存数抓取） |
| 核验日期 | 2026-10-21 |
| AI-1 初筛 | 18% B |
| AI-2 初筛 | 20% B |
| 我方评估 | **68** / 100 |

> 说明：「联系人」列来自**用户侧**（展会/微信/名单），「证据来源」列是**我方独立抓取**到的内容。两者不要混用。

## 建议动作

Antaira 之外的第二供应源提案（我方工业 8 口对位 LNX-1002C 规格 + 价格）；Marvell 方案叙事（用户观察其网站适合推 Marvell，未独立核实）

## 备注

用户 #42；AI-2 的"zkr.com.tr"= 抓取错误，弃用 【r33/2026-10-21】官网重验：安防/IT 集成商；自有 Digifort AI 视频分析 VMS（人脸 99.87%）；品牌矩阵 = Axis/FLIR/Milestone/Dahua/Hikvision/D-Link/Broadcom/Cisco/IBM/HP/GE/Western Digital；Levent 2025-03-07 "We have not done business before" = 非 Angora 客户；潜在"相机+交换机"捆绑项目渠道【r37 2026-10-25】用户双评估 18B/20B+在售 Antaria 工业 switch（小众）+TCL 备注「网站适合推 Marvell」+联系人 Salih Senyurt 销售总监（+Toyan Karahan PM/Aycan Tuerkay GM）→B（Marvell 方案切入已指定）

---

## 附：B 档深挖（r46 · 2026-11-01）

> 本节为 **r46（2026-11-01）B 档深挖**新增，来源为公开网络（官网 / 企业登记 / 展会名录 / BGP / 第三方企业库），逐条标注证据等级；**未核实的项一律标为空白，不推测。**

### 一句话
**Rima Elektronik 是"风险/安全评估 + 方案设计 + 供货"三合一的集成商**（2008 成立，İstanbul Florya），而且它是 **Digifort（巴西 VMS 品牌）的土耳其合作方**——有自己的 VMS 技术栈。B 档里"技术含量"最高的一家。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **Rima Elektronik Bilişim ve Güvenlik Sistemleri San. ve Dış Tic. Ltd. Şti.** |
| 成立 | **2008** |
| 规模 | **11–50 人** |
| 地址 | İnönü Cad. Ateştur İş Hanı No:18 Kat:1 D:7, **Beşyol / Küçükçekmece, İstanbul 34295** |
| 邮箱 / 官网 | `bilgi@rimaelektronik.com` / `rimaelektronik.com` |
| LinkedIn | 160 关注者 |

### ⭐ 关键资产：Digifort 土耳其（`digifort.rimaelektronik.com`）
- 它运营 **Digifort 的土耳其本地化站点**，自述覆盖"需求分析 → 系统设计 → 产品选型 → 报价 → 调试 → 售后"全流程。
- 说明：**它不只是卖货，它掌握 VMS 层**。→ 它选的交换机必须**与 Digifort 兼容（组播/ONVIF/IGMP）**，这是它的硬指标。

### 业务与客户
- 自述专长：**güvenlik sistemleri、ip kamera、network alt yapı、kablosuz video transferi、nvr kayıt cihazı**。
- 服务形态：**风险评估（risk/güvenlik değerlendirmesi）→ 项目设计 → 供货**，本质是**项目型集成商**，不是纯分销。

### 与我方的切入点
1. **它做项目 → 需要"投标级参数"**：给规格书 + 兼容性声明（IGMP Snooping / QoS / 组播），比给价格重要。
2. **Digifort 栈 = 需要稳定组播** → 我方交换机必须明确写 **IGMP Snooping v1/v2/v3 + QoS 优先级**（PTP 更好）。
3. **它在 Küçükçekmece（批发带）但只有 11–50 人** → 单量中等，决策链短。

### 打法
- 首封给 `bilgi@rimaelektronik.com`，主题 **"Digifort uyumlu PoE switch — multicast/IGMP optimizasyonu"**。
- 附一页「**Digifort + 我方交换机 兼容性说明**」（把 IGMP/QoS/带宽算进去）——这是它最需要、别的中国厂不会给的东西。
- **不要谈"我们更便宜"**：它是方案商，赚项目钱。

### 证据等级与空白
- 已核实：法定名、2008 成立、11–50 人、地址、Digifort 土耳其合作方身份（官网 + Digifort 本地站双证）。
- 空白：营收、现交换机品牌、Digifort 合作是独家还是非独家。
