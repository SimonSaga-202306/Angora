# 🔴 2026-08-17 Saga 官方回复：L3 战略、芯片路线、CENTEC
> 来源：`Reply on SAGA Enterprise L3 Recommendation Report.docx`
> 全文：`workstation/01-knowledge-base/docx/reply-on-saga-enterprise-l3-recommendation-report-docx.md`
> **这是目前仓库里最权威的一份我方战略自述**，与用户口述的芯片代际真相完全印证。

---

## 1. 芯片路线：AC3 → AC5 已完成切换
> *"our Marvell solutions have fully shifted from AC3 series to AC5 series"*
- Saga **不再为 AC3 更新固件与研发**，只保留技术支持
- `lite-hotfix-7.3.13` 是**最后一个 AC3 版本**，已交付并集成进 Angora 的 NMS
- *"Our work is now and will be centered on AC5 series, covering R&D, marketing and stock etc. This will be long-term chip category and guarantee continuous supply. The period is for at least 5 years"*
  → **AC5 至少锁定 5 年**

✅ **印证用户口述**：AC3/AC5 是成本与产品策略选择，不是能力差距；SmartByte/Saga 全面 AC5。
✅ 我的"DX1500 会拉开代际差距"警告**再次确认作废**。

## 2. 资源投向：明确押注 L2+
> *"Currently our technical resources are poured into L2+ switching solutions, including commercial and industrial level models... However quite few in Saga Feature List_7.5.x_L3. Our positioning is clearly on Marvell L2+ solutions now and will keep investing to enrich the feature set."*
> *"we basically adopt a 'let it be' attitude for most L3 models due to ROI, demand and after-sales support effort"*

**仓库内的硬证据**（本轮新入库的 `Saga Feature List_7.5.x_L2+.xlsx`）：
- 7.5.x **L2+** 清单的 `IP Route` 大类**只有 Static Route**（IPv4/IPv6 静态路由、ARP、路由前缀表 4096）
- **没有** RIP / OSPF / BGP / ECMP / VRRP
- 而 **7.3.0 软件功能清单**里 RIP / OSPFv2 / BGP4 / ECMP / VRRP / Static Routing **全部存在**
→ 即：**L3 动态路由能力停留在 7.3.0 世代，7.5.x 未跟进**。这解释了 Levent 2026-08-30 问"STI-4xx XGGPM 是否支持 RIP/OSPF/BGP/ECMP/VRRP"时的尴尬。

## 3. ⭐ 官方战略定调：Marvell L2+ + CENTEC L3
> *"Till now, Saga has already fixed its chipset solutions on **Marvell L2+ and CENTEC L3**, this is a strategic move."*
> *"At Angora side, it is vital to view this chipset combo... Or preferably just keep CENTEC L3 as an option or for project use."*

**一句话路线图：Saga = Marvell（L2+） + CENTEC（L3）。**

**CENTEC 线索在仓库中的其他落点（现已串成一条线）**：
- 微信 2026-01-06：`CENTEC models are good`（Simon 语）
- 微信 2026-04-16：`they bought 3 samples from us`
- `INFO_2025.12.17/CENTEC web gui.jpg`（已入档但未解析图像）
- `INFO_2025.12.17/INFO.rar`（未解压）
- 微信 2026 末段：`just received a Cisco RFP`

## 4. 成本压力：一个新的、独立于芯片的信号
> *"In the last 6 months, we are suffering the **soaring prices of RAM/DDR and PCB boards**. This trend is spreading and impacting our operating cash inflows."*

→ 与 `95-smartbyte-price-trend-2024-vs-2026.md` 互相印证：
**上游（RAM/DDR/PCB + AC5）全面涨价，但 SmartByte 工业线 ≥16 口 2.5 年零涨价 → 毛利被两头挤压。**

## 5. 拟议对策（Saga 自提）
1. 快速测试并推广 **AC5 ready** 机型，据此调整市场方向
2. 复盘更新后的 L3 feature list，收集客户端反馈
3. **评估 CENTEC 方案是否可接受**（上述 L3 特性 CENTEC 全部现成可用）

## 6. 被点名"缺失或需评估"的 L3 特性清单（原文顺序）
`Stacking` · `USB Port` · `OOB Management` · `Dual PSU` · `Static routing` · `OSPF` · `VRRP` · `ECMP` · `BGP` · `IS-IS` · `VRF` · `MPLS`

> 原文定性：*"Some features are already available on L3 models, but **mostly unavailable**. It takes too much to develop those features, we are not seeing a decent economic return **though we clearly know Enterprise-Grade Layer 3 products are booming in demand**."*

---

## 7. 与既有结论的关系
| 既有结论 | 本文件 |
|---|---|
| 用户口述"SmartByte 永远领先 Scodeno，被超越不可能" | ✅ 印证（AC5 全面 + 锁定 5 年） |
| 战略重点是 L2+，不是做不到 L3 | ✅ **官方原文确认** |
| AC5 缺货 / 成本上涨三条佐证 | ✅ 新增第 4 条：RAM/DDR/PCB 涨价 |
| Levent 2026-08-30 问 L3 协议支持 | ✅ **本文件早于该提问 13 天（08-17），是背景与答案** |
| 我的 DX1500 "代际差距"警告 | ❌ **作废（二次确认）** |

---

## 8. 关联：内部中文策略文档 `加深关系绑定.docx`
全文：`workstation/01-knowledge-base/docx/shenhua-guanxi-bangding-strategy.md`
要点：
- **支持 LIRA（土耳其里拉）付款，已申请相关银行账户** —— 对应 2026 招标中的换汇痛点
- 拟在**伊斯坦布尔设 office + 小型 warehouse**，打通「深圳 → 伊斯坦布尔清关 → office → 安卡拉/欧洲」
- 视为**面向欧洲市场的战略跳板**（紧邻保加利亚）
- 绑定手段：User Manual/Label 全用客户版本、土耳其语 web GUI、PCB 印客户名、让 Angora 官网宣传我方
- ⭐ 原文论断：**"目前国内同行没人全线做 Marvell 芯片，独有的优势"** —— 再次印证芯片代际真相
