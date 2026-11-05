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
