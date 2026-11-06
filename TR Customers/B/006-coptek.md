# 6 · Coptek

> **评级**：B+ ｜ **我方评估**：**78**/100 ｜ **核验日期**：2026-10-08
> **一句话**：**综合网络分销（omurga+工业+无线+光）**

---

## 身份卡

| 项 | 内容 |
|---|---|
| 公司 | Coptek |
| 层级 | B+ |
| 总部/城市 | İstanbul/Balmumcu |
| 场景/定位 | **综合网络分销（omurga+工业+无线+光）** |
| 自有品牌 | 无自有品牌（多品牌分销） |
| 名单来源 | 谷歌（用户侧） |
| 源表位 | 6 |

## 我方核实的交换机产品线

**DCN（中国）omurga L2/L3**（24/48 口，PoE 125-740W，5 年保修，15 Tbps backplane）+ **DCN+Antaira 工业 switch 族** + **ONV 工业线**（IPS33018PFM 18 口 L2+ 受管 PoE/**IPS38168PFM 10G uplink 16 口 L2+ 受管 PoE**/IPS33108PF/IPS33064PF 等）+ SFP 模块全族（100FX-10G）+ **DONGWE 光纤转换器** + DCN 无线 AP/AC + DCN ES430 web smart

## 当前供应链（核实口径）

**DCN（主力，中国）+ Antaira + ONV（深圳）+ DONGWE（中国）= 全中国供应链**

## 联系人（逐字抄录）

```
Fuat Sarp Sok. 5/1 Balmumcu + +90 212-275 7953 + info@coptek.com.tr
```

## 证据与核实等级

| 项 | 内容 |
|---|---|
| 证据来源（独立核实） | coptek.com.tr 官网（products 页 + onv_endustriyel 页 + DCN ES430 datasheet 全抓） |
| 核验日期 | 2026-10-08 |
| AI-1 初筛 | 30% A |
| AI-2 初筛 | 25% B |
| 我方评估 | **78** / 100 |

> 说明：「联系人」列来自**用户侧**（展会/微信/名单），「证据来源」列是**我方独立抓取**到的内容。两者不要混用。

## 建议动作

替换/补充供货提案（DCN/ONV 同域竞品 = 我方 L2/L3+工业 PoE+SFP 全替换方案 + 5 年保修对位）

## 备注

用户 #31；备注提及印尼客户成单案例（用户侧，未核实）【r37 2026-10-25】用户双评估 30A/25B（在售 DCN 中国商业/工业+ONV 绿灯工业+SFP+MC；Claude：成单的那个印尼客户）→B+ 监控（绿灯双源，第二供应商窗口）

---

## 附：B 档深挖（r46 · 2026-11-01）

> 本节为 **r46（2026-11-01）B 档深挖**新增，来源为公开网络（官网 / 企业登记 / 展会名录 / BGP / 第三方企业库），逐条标注证据等级；**未核实的项一律标为空白，不推测。**

### 一句话
**Coptek = "Koptek Bilgisayar ve İletişim Sistemleri Ltd. Şti."**，是一家**只做企业网络、不做安防**的网络分销/集成商，产品页覆盖**Omurga(骨干) / Data Center / PoE / L3 / L2 / 工业以太网 / 无线AP+AC / 光纤以太网 / SFP / 光纤转换器**——**与我方交换机产品线 1:1 对口**。这是 B 档里最像"纯网络买家"的一家。

### 主体与坐标（公开可核实）
| 项 | 内容 |
|---|---|
| 法定名 | **Koptek Bilgisayar ve İletişim Sistemleri San. ve Tic. Ltd. Şti.**（站点写 Coptek / Koptek 两种拼法） |
| 地址 | Gayrettepe Mah. **Pazar Sk. No:16/A, Balmumcu-Beşiktaş / İstanbul**（页脚另写 Fuat Sarp Sok. No:5/1 Balmumcu） |
| 电话 / 传真 | **+90 212 275 79 53** / +90 212 288 43 36 |
| 邮箱 | `info@coptek.com.tr` |
| 官网 | `coptek.com.tr` |

### 它在卖什么（决定了它是不是我方客户）
- 产品分类逐条：**Omurga Switch / Data Center Switch / PoE Switch / Layer 3 Switch / Layer 2 Switch / Endüstriyel Ethernet / Wireless ve AP Controller / Fiber Ethernet / SFP Modül / Fiber Çevirici**。
- 具体型号举例：`S4600-28X-SI`（24×GE + **4×10G 上联**，L2 管理型，支持 Ethernet OAM 802.3ah/802.1ag、DDM、DHCP Snooping Option82、IGMP v1/v2/v3 Snooping、STP/RSTP/MSTP）——**这是典型的"深圳白牌网管交换机"规格写法**（S4600 是多家中国厂共用的型号族）。
- 站点结构为**静态 HTML 老站**（`.html` 后缀），无电商、无价格 → **它走"询价 + 项目报价"模式**，不是零售。

### 供应链推断（标为推断，不是已核实）
- 页面只写规格不写品牌 → **高度疑似"白牌贴自己的名字"或"代理某中国厂"**。
- 型号族 `S4600 / S5700` 在中国厂（如 H3C 系命名习惯）里极常见 → **它大概率已经在中国采购**，我方不是开荒，是**二供**。

### 与我方的切入点
1. **它产品线里没有 2.5G / 802.3bt**（页面全是 GE + 10G 上联）→ **这两档是空白**。
2. **工业以太网有分类但内容薄** → 我方 `EW-S1710FG-AP`（−20~+55 °C / IP30 / 4 kV）能直接补。
3. 它做 **AP + AC**，我方做不了 AP → **不要硬凑**，说"交换机侧我们更强，AP 你继续用现有的"。

### 打法
- 首封发给 `info@coptek.com.tr`，主题写 **"S4600 / S5700 同规格第二源 + 2.5G/bt 补位"**。
- **直接把 S4600-28X-SI 的规格抄进去做对位表**（证明我们看过它的目录，这是最强开场）。
- 问一句：**"你们现在这些 switch 是贴 Coptek 牌还是原厂牌？"** —— 一句话定生死（贴牌→OEM 谈法；原厂牌→二供谈法）。

### 证据等级与空白
- 已核实：法定名、地址、电话、产品分类、S4600 规格（官网）。
- 空白：**成立年、员工数、营收、负责人姓名、现有供应商**（公开面全无；站内无"关于我们"实质内容）。

---

## 附：r48 抓站补录（2026-11-01）

> 本节为 **r48（2026-11-01）第二轮抓站**后的**修正与新证据**，逐条标注来源；**与前面小节冲突时，以本节为准**（并已在本节内说明改了什么）。

#### r73 补：**法定名称订正 —— 是 `Koptek`，不是 Coptek**

| 项 | 内容 |
|---|---|
| 法人全称 | **Koptek Bilgisayar ve İletişim Sistemleri San. ve Tic. Ltd. Şti.** |
| 办公地址 | **Gayrettepe Mah. Pazar Sk. No:16/A, Balmumcu-Beşiktaş / İstanbul**（另登记：Gayrettepe Mah. Fuatsarp Sok. No:5/1，No:4/3） |
| 电话 / 传真 / 邮箱 | **+90 212 275 79 53** · Faks 0212 288 43 36 / 0212 288 63 92 · `info@coptek.com.tr` |
| **产品线（官网菜单逐条）** | **Omurga Switch（骨干）· Data Center Switch · PoE Switch · Layer 3 · Layer 2 · Endüstriyel Ethernet · Wireless + AP Controller · Fiber Ethernet · SFP 模块 · Fiber 转换器** |

⇒ **判读**：**它不做摄像头，只做网络** ⇒ 客户买交换机就是买交换机，**不做安防捆绑**。
⇒ **产品线与我方 100% 重叠**（骨干 / DC / 工业 / SFP）⇒ **B 级里最像「纯交换机买家」的一家**，谈判不需要品牌故事，只需要规格表与价格表。

---

## 附：r54 B 档型号级点算与价格锚点重建（2026-11-01）

> 本节为 **r54（2026-11-01）** 的 B 档型号级点算；USD/TRY 按 **50.02**（2026-11-04）折算。

### ⭐⭐ r54：Coptek 卖的是 **DCN（神州数码）+ ONV** 两条代理线 —— **2.5G / 40G / 740–1000 W PoE 全都有**

#### A. 型号全表（官网 `coptek.com.tr` 原文）
| 系列 | 型号 | 端口 / 关键规格 |
|---|---|---|
| **S4600-SI** | `S4600-10P-SI` | 8×10/100 + 2×GE + 2×SFP，20 Gbps，16K MAC |
| | `S4600-28P-SI` | 24×GE + 4×SFP，**56 Gbps / 41.7 Mpps**，128 MB/32 MB，16K MAC |
| | `S4600-52P-SI` | 48×GE + 4×SFP，**104 Gbps / 77 Mpps**，16K MAC |
| **S4600-SI PoE** | `S4600-28P-P-SI` | 24×GE **PoE** + 4×SFP，**370 W** |
| | `S4600-10P-P-SI` | 10×GE（PoE/PoE+）+ 2×SFP，**12 口 af/at 15.4/30 W**，20 Gbps，8K MAC |
| **S4600-X-SI** | `S4600-28X-SI` | 24×GE + **4×10G SFP+**，**128 Gbps / 95 Mpps**，16K MAC，21 W，0~50 °C |
| | `S4600-28X-P-SI` | 24×GE **PoE** + 4×10G，**370 W** |
| ⭐ | **`S4600-12X-P-SI`** | **24×100/1000M/2.5G + 4×10G SFP+ + 2×40G QSFP+，full 2.5G L3 PoE，530 W** |
| **S5750** | `S5750E-52X-P-SI(R2)` | 48×GE **PoE+** + 4×10G，**740 W**，双电源输入 |
| | `S5750X` 系 | 24/48 GE(+PoE) + **6×10G SFP+**，168/216 Gbps，125/161 Mpps，**1 GB DRAM**，32K MAC，**750 W PoE**，VSF 堆叠 |
| **CS6200X** | `CS6200X-24T6X-EI` / `-24T6X-P-EI` / `-48T6X-NO` | 24/48 口 + 6×10G，**最高 1000 W PoE** |
| **ES430** | `ES430-10P-POE` / `-18P-POE` / `-26P-POE` | 8/16/24 口 PoE + 2×SFP Web Smart |
| **机框** | `DCRS-9816` | 16 槽骨干机框 |

#### B. 品牌真相（原文自曝）
- 官网原文写 **「DCN firmasına ait olan MRPP Ring Koruma Sistemi her modelde standarttır」**、管理项写 **「DCN Private MIB」**；
- **ONV 线单独开一页** `coptek.com.tr/onv_poeswitch.html`：`POE3010PFM`（10 口 L2+ 管理）、**`POE33052PFM`（48 口管理 / 600 W 电源）**、`POE33024PF`、`POE33064PF`（6 口）、`POE56028PFM`。

⇒ **Coptek = DCN（神州数码）+ ONV 双代理**，不是自有品牌。

#### C. 这意味着什么（⚠ 与 r47 判断不同）
- **「B 档自有品牌只到 GE + af/at」这句话对 Coptek 不成立**：它卖的有 **2.5G + 40G QSFP+**（`S4600-12X-P-SI`）、**740 W / 1000 W PoE**、**6×10G + 1 GB DRAM 的 S5750X**。
- 它**不缺档位**，缺的是 **价格与交期**（DCN 是大厂，走的是项目报价）。
- **打法**：不谈"补位"，谈 **「同规格更低 FOB + 支持贴 Coptek 牌」**，主打 `EW-S5748GM-AP` 对 `S5750E-52X-P-SI`、`EW-S6826` 对 `S4600-12X-P-SI`。

**首封**：`S4600-12X-P-SI / S5750E-52X muadili — daha iyi FOB + Coptek markası`
**必问**：① DCN 是独家吗？② 2.5G 那台一年几台？③ 项目还是货架为主？

### 证据等级（r54）
- 已核实：**官网 6 个系列 + ONV 页的型号与规格**（`coptek.com.tr` 各产品页原文）、**「DCN Private MIB / DCN firmasına ait MRPP」原文**。
- 仍空白：DCN 代理协议范围、`S4600-12X-P-SI` 的实际成交价、ONV 是否独家。

---

## 附：r73 B 级客户身份卡（法名 / 税号 / 代理 / 自有品牌）

> 本节为 **r73（2026-11-06）**：**B 级客户工商档案 —— 打电话前先读这一节。**

#### r73 补：**法定名称订正 —— 是 `Koptek`，不是 Coptek**

| 项 | 内容 |
|---|---|
| 法人全称 | **Koptek Bilgisayar ve İletişim Sistemleri San. ve Tic. Ltd. Şti.** |
| 办公地址 | **Gayrettepe Mah. Pazar Sk. No:16/A, Balmumcu-Beşiktaş / İstanbul**（另登记：Gayrettepe Mah. Fuatsarp Sok. No:5/1，No:4/3） |
| 电话 / 传真 / 邮箱 | **+90 212 275 79 53** · Faks 0212 288 43 36 / 0212 288 63 92 · `info@coptek.com.tr` |
| **产品线（官网菜单逐条）** | **Omurga Switch（骨干）· Data Center Switch · PoE Switch · Layer 3 · Layer 2 · Endüstriyel Ethernet · Wireless + AP Controller · Fiber Ethernet · SFP 模块 · Fiber 转换器** |

⇒ **判读**：**它不做摄像头，只做网络** ⇒ 客户买交换机就是买交换机，**不做安防捆绑**。
⇒ **产品线与我方 100% 重叠**（骨干 / DC / 工业 / SFP）⇒ **B 级里最像「纯交换机买家」的一家**，谈判不需要品牌故事，只需要规格表与价格表。
