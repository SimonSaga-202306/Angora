# 116 · B/A 档「型号对位表」（r47 · 2026-11-01）

> **用途**：客户已经在卖交换机时，**唯一会被认真看的附件就是「你的型号 ↔ 我的型号」逐行对位表**。
> 本文件把 r46（B 档）+ r47（A 档）挖到的**客户在售型号**，与**我方/EWIND 产品线**逐条对位。
>
> **口径说明（必读）**
> - **客户侧型号与规格**：来自**客户官网产品页**（逐条抓取，标注型号）。凡属"从型号推断"的，均标 ⚠推断。
> - **我方型号与规格**：来自仓库内 `06-competitors/112-ewind-website-mirror-2026-10-21.md` 的产品目录（五个产品线 + OEM 定制），**不是本轮新抓的**。
> - **价格**：本文件只有 **1 个真实公开价锚点**（Winet，见 §二），其余一律不给价——**价格必须现报**。
> - 凡是"我方没有"的档位，**照实写"缺"**，不用"可定制"糊过去（可定制是真的，但要额外写交付周期 4–6 周）。

---

## 一、先看这张「缺口矩阵」（决定谈什么）

我方 5 条产品线对照客户在售型号，**客户普遍缺的 6 个档位**如下——这 6 行就是全部谈判空间：

| 缺口档位 | 客户侧现状（r46/r47 实测） | 我方有货的型号 | 我方也是空白 |
|---|---|---|---|
| **2.5G 电口** | **11 家里 0 家**有 2.5G（Coptek/NFS/Cebeci/iotsistem/ErETE XPS 全部是 GE + 10G 上联） | `EW-S6805F`(5×2.5G+1×10G)、`S6806`(4+2)、`S6809`(8+1)、`S6818`(16+2)、**`EW-S6826`(24×2.5G+2×10G)**、`W-S2910SM-DP`(8GE PoE+2×1/2.5G) | — |
| **802.3bt / 60–90 W** | 只有 ErETE（EtherWAN 60 W PSE 公告）、NFS（`SRX-*` 30 W 级）；**绝大多数只到 af/at 30 W** | `EW-S1810CF-AP`（7–8 口 **60 W/口**）、`EW-PIS3810M-8GE-BT`、`EW-PIS6812M-8GE-BT`、**`EW-PIS5728GM-AP-BT`（28 口 L3 / 800 W / 24×bt）** | — |
| **250–300 m 长距 PoE** | Coptek/Cebeci/iotsistem **0 家**；NFS 未见；只有 Longline/Ewind 系有 | `EW-S1810CF-AP` 拨码 **E = AI Extend 300 m**、`EW-ES` 系 Cloud 版同功能 | 商用受管大机未见长距拨码 |
| **云管理 / AI PoE** | 客户侧 **0 家**（ErETE 靠 IP Infusion NOS，不是云） | `EW-ES2010CF-AP`、`EW-ES3006CG-AP`、`EW-ES3028CG-AP`（24 口 400 W）、`EW-EPIS3910-8GE`（工业云） | EwindCloud 平台生态成熟度弱于 Omada/TP-Link |
| **工业宽温 + DC 宽压** | ErETE(XPS)、iotsistem(MLB)、NFS(SRX-IGS) 有，但**多为百兆为主、无 2.5G、无 bt** | `EW-PIS1810/1812-8GE`、`PIS3610M-8GE`、**`PIS3620M-16GE`（20 口 L2+）**、`PIS5712M-8GE`（4×10G SFP+）、**`PIS5728GM-AP`（28 口 L3 / 400 W）** | — |
| **40/100G 上联** | **0 家**（Coptek/NFS/Cebeci 最高 4×10G） | **`EW-S53928QM`（24×10G SFP+ + 4×100G）**、`EW-S57948QM`（48×2.5G + 4×100G L3） | — |

> ⭐ **结论**：这 11 家的产品线**全部停在「GE + 10G 上联」**。我方不打"同规格更便宜"，打 **「2.5G / bt / 长距 / 云 / 100G」这五个它没有的档**，价格战只在第 1 行（同规格替代）才用。

---

## 二、唯一硬价格锚点（Winet，A/053）

| 客户型号 | 规格（官网原文） | 页面价 |
|---|---|---|
| **`OEM-8-PORT-GB-POE`** | **WINET 8 口千兆 PoE 交换机：7 口 PoE（24/48 V）+ 1 口上行** | **2,916.76 ₺ + KDV（未税）** |

**怎么用**：
- 该型号**只有 24/48 V 手动、无 af/at 自动协商、无 bt、无长距**。
- 我方对位 = **`EW-S1710FG-AP`**（8×GE PoE + 2×SFP 非受管）或 **`EW-S1810CF-AP`**（带 E/V/D 拨码：300 m 长距 + 口隔离 + PoE Watchdog）。
- **话术**：*"Sitenizdeki 2.916,76 ₺'lik OEM-8-PORT-GB-POE yerine af/at + 250m + watchdog."* —— **引用客户自己的价格页**，是全套打法里最强的一句开场。
- ⚠ 该价是**零售未税页价**，不代表批发价；**不要用它反推我方 FOB**。

---

## 三、逐家对位表（11 家 B + 8 家 A）

### ① B/006 · Coptek（Koptek Bilgisayar）

| 它的型号 | 它的规格（官网） | 我方对位 | 差距 / 打法 |
|---|---|---|---|
| **`S4600-28X-SI`** | 24×GE + **4×10G 上联**，L2 网管（802.3ah/1ag、DDM、DHCP Snooping Opt82、IGMP v1/v2/v3 Snooping、STP/RSTP/MSTP） | **`EW-S2928GM`**（28 口 L2+：24×GE + 4×1G/2.5G/10G SFP+，RS232 console） | 规格基本 1:1 → **价格 + 交期战**；我方加 **2.5G 上行可选**（同口 2.5G）即差异化 |
| （L3 分类） | 官网有 Layer 3 Switch 分类，**无具体 10G/25G 型号公开** | **`EW-S5748GM-AP`**（L3：48×GE PoE + 4×10G）/ **`EW-S5954GM-AP`**（L3+：48 PoE + 6×1/2.5/10G，**OSPF v2 + VRRP**） | ⭐ 我方带**动态路由**，它的 L3 分类无人证 → **拿 OSPF/VRRP 打它的 L3 名不副实** |
| （PoE 分类） | 有 PoE Switch 分类，型号未公开 | **`EW-S2926GM-AP`**（24×GE PoE + 4 combo + 2 SFP）/ **`EW-S3910GM-AP`**（8 PoE + 2×10G SFP+） | 8 口带 10G 上联是**它的空档** |
| （SFP 分类） | 有 SFP 模块分类 | `EW-810GS-20`（1G 20 km）、`EW-10GSFP-SR`（10G） | **打包报价**（交换机 + 模块同柜） |
| **缺口** | 无 2.5G / 无 bt / 无 100G / 无云 | `EW-S6826`、`EW-PIS5728GM-AP-BT`、`EW-S53928QM`、`EW-ES3028CG-AP` | ⭐ **四个方向全是增量** |

**首封主题**：`S4600-28X-SI muadili + 2.5G / 802.3bt / 100G 补位`
**必问**：**"Bu switch'ler Coptek markasıyla mı geliyor, yoksa fabrika markası mı?"**（贴牌 → OEM 谈法；原厂牌 → 二供谈法）

---

### ② B/014 · NFS Teknoloji（Surenix / Oinone 线）

| 它的型号 | 它的规格（官网分类） | 我方对位 | 差距 / 打法 |
|---|---|---|---|
| `Surenix SRX-GS24PP+` | 24 口千兆 **PoE+** | **`EW-S2926GM-AP`**（24×GE PoE + 4 combo + 2 SFP，L2 受管） | 同规格 → 比价 |
| `Surenix SRX-MS16PP+` | 16 口 PoE+ | **`EW-S1616CGU`**（16×GE 金属 32 Gbps）+ PoE 版 | 我方 16 口 PoE 档位清晰 |
| `Surenix SRX-GS24PMX` | 24 口**模块化** | ⚠ **我方无模块化机型** | **照实说没有**；改推 `EW-S2926GM-AP` + 光模块组合 |
| `SRX-IGS4PP+ / IMS8PP+ / IGS8PP+` | 工业 4/8 口全千兆**管理型** PoE | **`EW-PIS3810M-8GE-BT`**（8×GE PoE **af/at/bt** + 2×SFP）/ `EW-EPIS3910-8GE`（云管理工业） | ⭐ **我方多一个"云 + bt"**，它只有本地管理 |
| `SRX-4GS24PP+` | 24 口全千兆 **PoE+ 管理型** | **`EW-S2926GM-AP`** / `EW-S2948GM-AP`（52 口 L2 PoE） | 同规格 |
| `SRX-10GS24P-L3-8PC` / `SRX-10GS24PX-L3` | **24×GE + 4×10G 上联，L3 管理** | **`EW-S5748GM-AP`**（L3 48 PoE + 4×10G）/ **`EW-S5954GM-AP`**（L3+ OSPF/VRRP） | ⭐ 我方 **OSPF/VRRP** 是硬差异（它的 L3 是否真有动态路由未知） |
| `ONSW-IMS8PP` | 8 口 PoE（af/at，单口 30 W） | **`EW-S1710FG-AP`**（8×GE PoE + 2 SFP）/ `EW-S1810CF-AP`（**60 W/口 + 300 m + watchdog**） | ⭐ 30 W → **60 W 是升级** |
| **缺口** | 无 2.5G / 无 100G / 无云 / 无 250 m | `EW-S6826`、`EW-S53928QM`、`EW-ES3028CG-AP` | 四个增量 |

**首封主题**：`SRX-4GS24PP+ / SRX-10GS24PX-L3 — alternative source`
**必问**：**"Surenix sizin markanız mı, yoksa fabrikanın mı?"**（决定 OEM 还是二供）

---

### ③ B/062 · Cebeci Grup（Cebeci Teleteks）

⚠ **r47 重要修正**：Cebeci 的**真实品牌宇宙是电信测试/FTTx**——代理 **Argus、Cifocs、CMG、Greenlee-Tempo、InterCoax、Micos、Trend Networks**；**`Cifocs` 即其工业交换机与光转换器品牌**（官网 "Endüstriyel Switchler" 分类首图 = `Cifocs CFC-4G2SFP-IPS`）。**`S5700` 系列是它的电商挂品，不是自有品牌线。**

| 它的型号 | 它的规格 | 我方对位 | 差距 / 打法 |
|---|---|---|---|
| **`S5700-24G-4FR`** | 24×GE + **4×GE SFP**，L3 网管 | **`EW-S2928GM`**（24×GE + 4×1/2.5/10G SFP+） | ⚠ 注意：它的 4 个 SFP 是 **1G**，我方是 **1/2.5/10G 自适应** → **同价位更强** |
| **`S5700-24G-4TFR`** | 24×GE + **4×10G SFP+**，L3 网管（ACL L2–L4、802.1X、DHCP Snooping、ARP/DoS 防护、SNMP v1/v2/v3、RMON、LLDP、IPv6、32 组聚合） | **`EW-S2928GM`**（L2+）→ 若要 **L3 动态路由**上 **`EW-S5748GM-AP`** / `EW-S5954GM-AP` | 功能表可 1:1 对位；⚠ **它的页面没写动态路由** → 我方 OSPF/VRRP 是加分项 |
| `Cifocs CFC-4G2SFP-IPS` | 工业交换机（4×GE + 2×SFP，工业级） | **`EW-IS1804`**（4 口非受管工业）/ **`EW-PIS1805-4GE`**（4×GE PoE + 1 SFP） | **PoE 版是它的缺口**（Cifocs 该款无 PoE 标注） |
| 光纤转换器线 | Cifocs CFC-2200 等百兆/千兆转换器 | `EW-610MM/SM`、`EW-810GS-20`、`EW-10GSFP-SR` | **打包**（它卖转换器，我方可补 10G 档） |
| **缺口** | 无 2.5G / 无 bt / 无云 / 无 100G | `EW-S6826`、`EW-PIS5728GM-AP-BT`、`EW-ES3028CG-AP`、`EW-S53928QM` | 增量 |

**首封主题**：`S5700-24G-4TFR muadili + 2.5G/bt 补位（Cifocs switch hattı için）`
**必问**：**"S5700 serisi sizin mi, yoksa tedarikçinin mi? Cifocs switch'leri kim üretiyor?"**

---

### ④ B/018 · iotsistem（`MLB-E4xxx` 自有工业线）

| 它的型号 | 它的规格（官网） | 我方对位 | 差距 / 打法 |
|---|---|---|---|
| `MLB-E4101-5` / `E4106-8-F` | 5 / 8 口**非受管**（带光纤） | `EW-IS1804`（4 口）/ **`EW-IS1802-2`+ 光纤口**；PoE 版 `EW-PIS1810-8GE` | 我方有 **PoE + 光纤**组合 |
| `MLB-E4103-5-P` / `E4104-5-P-F` | 5 口 **PoE** 非受管 | **`EW-PIS1805-4GE`**（4×GE PoE + 1 SFP）/ `EW-PIS1810-8GE` | 同档 |
| `MLB-E4202-10-F` / `-10-GF` | 10 口**管理型**（光纤 / 千兆光纤） | **`EW-PIS3610M-8GE`**（10 口 L2+：8×GE PoE + 2×SFP，20 Gbps/8K MAC） | ⭐ 我方该档**自带 PoE**，它的是纯电口 |
| `MLB-E4208-14-F` / `-14-G-F` | 14 口管理型 | `EW-PIS3620M-16GE`（20 口 L2+：16 PoE + 4 SFP）/ 14 口受管工业 PoE+4 上联 BT 款 | 我方有 **16 口 + 4 SFP** 与 **14 口 BT** |
| **`MLB-E4204-28-F` / `-28-G-F`** | ⭐ 28 口管理型，机架式，**100/240 VAC + DC 双冗余端子 + 反接保护** | **`EW-PIS5728GM-AP`**（28 口 L3：24×GE PoE + 4×10G SFP+，400 W，**AC+DC 双电**）/ **`-AP-BT` 800 W bt 版** | ⭐ **1:1 对位且我方有 bt + 10G 上行 + L3**；它的 28 口是百兆为主 |
| **缺口** | 无 2.5G / 无 bt / 无 10G 上行 / 无云 | `EW-S6826`、`EW-PIS6812M-8GE-BT`、`EW-EPIS3910-8GE` | 增量 |

**首封主题**：`MLB-E4xxx 同规格代工 + 2.5G / 802.3bt 补位`
**必问**：**"MLB serisini hangi fabrika üretiyor? Kendi firmware'iniz var mı?"**

---

### ⑤ B/010 · ErETE（XPS 自有牌 + EtherWAN + IP Infusion）★ r47 补全

⚠ **r47 重大补全**：ErETE 不只卖 XPS——它有 **`OPEN NETWORKING`** 与 **`NOS（Network Operating System）`** 两个独立分类，代理 **IP Infusion** 与 **EtherWAN**，还有 **LANDE** 布线。**这一家已经是"开放网络 + 工业网络"的完整分销商，等级应改判 A。**

| 它的型号 | 它的规格（官网产品页） | 我方对位 | 差距 / 打法 |
|---|---|---|---|
| **`XPS-I7120-6 / -10 / -14 / -16 / -24`** | 4 / 8 / 10 / 12 口 GE + SFP，**L2 管理** | `EW-PIS1810-8GE`（8 口）/ `EW-PIS3610M-8GE`（10 口 L2+）/ `EW-PIS3620M-16GE`（20 口 L2+） | 同档；我方 L2+ 带 16K MAC |
| **`XPS-I8120-16`** | ⭐ 12×GE + **4×10G SFP+**，**L2+ 管理** | **`EW-PIS5712M-8GE`**（12 口：8×GE PoE + **4×10G SFP+**，128 Gbps/16K MAC） | ⭐ **1:1 对位**（我方还多 PoE） |
| **`XPS-I8120-24F`** | 12×GE + **8×SFP** | `EW-PIS3620M-16GE`（16 PoE + 4 SFP）/ `EW-S3936GM`（8×GE + **24×GE SFP** + 4×10G） | ⭐ **`EW-S3936GM` 是高密度光纤汇聚的答案**（24 SFP） |
| **`XPS-I7120-6P / -10P / -14P / -16P`** | 4/8/10 口 PoE + SFP，L2 管理 | **`EW-PIS3810M-8GE-BT`**（8 口 **af/at/bt** + 2 SFP）/ `EW-EPIS3910-8GE`（工业云） | ⭐ 我方多 **bt + 云管理** |
| **`ECS4660-28F`** | L2/L3/L4 千兆工业 Metro Ethernet | `EW-S2928GM` / `EW-S5954GM-AP`（L3+） | 商用可换，工业 Metro 需说明 |
| **EtherWAN `EX89000/87000/77000/83000/61000A/70900/72000`** | 加固管理型 8–24 口百兆/千兆 | `EW-PIS3610M/3620M`、`EW-PIS5728GM-AP` | ⚠ **EtherWAN 是台湾老牌，认证与口碑强于我方** → **不要正面替代**，只打"经济层" |
| **EtherWAN `ER59000/ER58000`**（加固 PoE） | 16 / 8 口百兆 PoE，加固 | `EW-PIS1810-8GE` / `EW-PIS3620M-16GE` | 同上：经济层 |
| **IP Infusion（NOS）+ OPEN NETWORKING 分类** | ⭐ 开放网络操作系统 + 白盒 | ⚠ **我方在此档是"硬件供货"角色**：`EW-S53928QM`（24×10G+4×100G）、`EW-S3936GM`（24 SFP+ 4×10G） | ⭐⭐ **这是全场最值钱的一条线**：它已经在卖"白盒 + 第三方 NOS"，**硬件从哪来是它最关心的问题** |
| **缺口** | 无 2.5G / 无 100G（XPS 线最高 4×10G） | `EW-S6826`、`EW-S53928QM`、`EW-S57948QM`（48×2.5G + 4×100G L3） | 增量 |

**首封主题**：`XPS / OPEN NETWORKING için white-box switch tedariki（2.5G / 100G）`
**必问三句**：① **"XPS switch'leri hangi fabrika üretiyor?"** ② **"IP Infusion ile çalışırken donanımı nereden alıyorsunuz?"** ③ **"EGM onaylı ürünlerde fabrika sertifikası mı aranıyor?"**
**⚠ 纪律**：**永不贬低 EtherWAN**（它是 ErETE 的长期代理，贬低等于挑战其判断）。

---

### ⑥ B/079 · Eurocam Güvenlik（Ruijie 代理 + 3 个自有品牌）

| 它的位置 | 说明 | 我方对位 | 打法 |
|---|---|---|---|
| **Ruijie（锐捷）** | 企业级交换机 + AP，**有云（Reyee/云平台）** | ⚠ **正面打不过云生态** | **只打"Ruijie 之下的经济层"**：`EW-S2926GM-AP` / `EW-S1950CG-AP`（48×GE PoE + 2 SFP） |
| **Eurocam / Eurolink 自有品牌** | 摄像机、PDKS、已有贴牌能力 | ⭐ **`EW-S1810CF-AP`（OEM 定制款，E/V/D 拨码）最适合贴 Eurocam 牌** | **贴牌方案 + 4–6 周交付** |
| Dahua / Hikvision / Eleks / Teknim | 相机与本土品牌 | PoE 为相机配套：`EW-S1927CG-AP`（24 GE PoE）、`EW-S1616CGU` | 走"相机 + 交换机"同单 |
| **缺口** | 无 2.5G / 无 bt 90 W / 无 100G | `EW-S6826`、`EW-PIS5728GM-AP-BT`、`EW-S53928QM` | 增量 |

**首封主题**：`Ruijie yanında ekonomik katman: Eurocam markalı PoE switch`
**⚠ 纪律**：**绝不说"替代 Ruijie"**，要说 **"Ruijie 之上的项目用它，价格敏感的项目用我们的"**（帮它做价格分层）。

---

### ⑦ B/015 · Koza Güvenlik（PoE 分类很薄 + 自设进口部）

| 它的现状 | 我方对位 | 打法 |
|---|---|---|
| 有 **"PoE Switchler"** 分类，挂在录像设备之下，**款数很少** | 补齐梯度：`EW-S1710FG-AP`（8 口）→ `EW-S1616CGU`（16）→ `EW-S1927CG-AP`（24）→ `EW-S1950CG-AP`（48） | **"4/8/16/24/48 + 工业"六档一次给全** |
| 关联公司 **Greentech** 做安装/报警监控服务 | 安装商最怕返修 → **`EW-S1810CF-AP`（PoE Watchdog 相机掉线自动重启）** | ⭐ **卖"少一次上门"**，不卖价格 |
| 有 **Ar-Ge** 部门（可能改固件） | OEM 定制能力（拨码/固件/多语言包装） | 谈 **"定制固件 + 我方制造"** |
| **缺口** | 无 bt / 无云 / 无 2.5G | `EW-PIS5728GM-AP-BT`、`EW-ES3028CG-AP`、`EW-S6826` |

**首封主题**：`PoE switch 全梯度补位 + Greentech 项目配套（watchdog）`

---

### ⑧ B/019 · Lansan（强无源、弱有源）

| 它的现状 | 我方对位 | 打法 |
|---|---|---|
| `Switch ve Aktif Ürünler` 分类**内容最薄**；强项是 SFP/patch panel/防雷器 | `EW-S1608CGU`（8 GE）→ `EW-S1624CGU`（24 GE）→ `EW-S2926GM-AP`（24 PoE 管理） | **有源整块补位** |
| **自称配线架制造商**（有本地组装） | ⭐ **半散件（SKD）方案**：本地组装 + 贴 LANSAN 牌 | **利用它的组装能力，降低关税与交期** |
| 卖 SFP/QSFP/DAC | `EW-810GS-20` / `EW-10GSFP-SR` 打包 | 同柜报价 |
| **缺口** | 无 bt / 无工业 / 无云 | `EW-PIS3610M-8GE`、`EW-ES3006CG-AP` |

**首封主题**：`Switch & aktif ürünler — üreticiden doğrudan (SKD mümkün)`

---

### ⑨ B/033 · HCS Kablolama（A.Ş.，2000，无有源）

| 它的现状 | 我方对位 | 打法 |
|---|---|---|
| 结构化布线批发，**完全无有源产品** | 整套：`EW-S2926GM-AP`（24 PoE）+ `EW-810GS-20`（SFP）+ 机柜内配套 | ⭐ **"你们报布线，我们补有源，同一张 teklif"** |
| 项目型客户（企业/政府/医院/学校） | `EW-S1927CG-AP`（24 GE PoE + 2 RJ45 + 1 SFP）/ `EW-S1950CG-AP`（48 口） | 项目报价单上的"网络设备"一行 |
| **缺口** | 无品牌、无云、无工业 | `EW-ES3028CG-AP`（云 24 口 400 W）、`EW-PIS5728GM-AP` |

**首封主题**：`Proje bazlı switch tedariki — HCS markasıyla`

---

### ⑩ B/035 · Antalya Turkuaz（TP-Link Omada/VIGI 代理）

| 它的现状 | 我方对位 | 打法 |
|---|---|---|
| **TP-Link Omada**（交换机 + AP + 云） | ⚠ **不打 Omada 客户**（云生态强） | ⭐ 只打 **"非管理/轻管理批量"**：`EW-S1616CGU` / `EW-S1624CGU` / `EW-S1950CG-AP` |
| **VIGI**（TP-Link 的安防线） | 相机配套 PoE：`EW-S1710FG-AP`、`EW-S1927CG-AP` | 走"VIGI 相机 + 第三方 PoE" |
| **Teknim**（土本土消防/报警） | 门禁/报警控制器也吃 PoE → `EW-PIS1810-8GE`（工业） | 项目配套 |
| 酒店/度假村（安塔利亚） | **16/24 口 PoE + 长距**（走廊 >100 m）：`EW-S1810CF-AP`（300 m） | ⭐ **长距是酒店的真痛点** |
| **缺口** | 它有云（Omada），我方缺云生态 → **不要在这里比云** | — |

**首封主题**：`Otel projeleri için ekonomik PoE switch（Omada alternatifi değil, tamamlayıcı）`

---

### ⑪ B/049 · Zeytek（MOBESE 柜 + 户外柜，总经理出身 Legrand/Asrack）

| 它的现状 | 我方对位 | 打法 |
|---|---|---|
| **IP Korumalı Saha Kabinleri / MOBESE Kabinleri** | ⭐ **柜内交换机**：`EW-PIS1810-8GE`（宽温）/ `EW-PIS3610M-8GE`（L2+）/ `EW-PIS5728GM-AP`（28 口） | **"你们做柜子，我们填空——柜子里的 PoE"** |
| 品类有 **`Network Cihazları`（无品牌）** | 全部交换机线 | ⭐ **这就是我方位置**（它有分类、无品牌） |
| 环境监控（温湿度/门磁/水浸） | 交换机的 SNMP/告警可对接 | 提"SNMP trap 到你们的 ortam izleme 平台" |
| **缺口** | 无相机/无云（不是它的事） | — |

**首封主题**：`MOBESE / saha kabinleri içi switch tedariki`

---

### ⑫ A/052 · Nokta Elektronik（upTech 自有品牌 916 SKU）★ A 档最优先

| 它的位置 | 说明 | 我方对位 | 打法 |
|---|---|---|---|
| **upTech 自有品牌**（商标 2008/13951，续展至 2028；**916 SKU**） | ⭐ 自己承担保修与技术支持 → 贴牌是常规动作 | **`EW-S1810CF-AP`**（OEM 定制，E/V/D 拨码）＋ `EW-S1710FG-AP`、`EW-S1927CG-AP`、`EW-S1950CG-AP` 全线 | ⭐ **对位 upTech 现有型号逐行列表 → 报 FOB + MOQ** |
| **代理 Edge-Core** | 开放网络厂牌 | `EW-S3936GM`（24 SFP + 4×10G）、`EW-S53928QM`（24×10G+4×100G） | ⭐⭐ **说明它懂白盒 → 可直接谈 ODM** |
| **代理 Ruijie / Planet / ORing** | 企业级 → 工业级全覆盖 | 经济层：`EW-S2926GM-AP` / `EW-PIS3610M-8GE` | **做"它代理体系的下一层"** |
| **市场：土耳其 + 中东 + 突厥语共和国 + 巴尔干** | 转口能力已存在 | FOB İstanbul / FOB Shenzhen 双报价 | 中东/中亚转口 |
| **缺口** | upTech 目录未见 2.5G / 100G | `EW-S6826`、`EW-S57948QM`、`EW-S53928QM` | 增量 |

**首封主题**：`upTech markalı switch üretimi — mevcut tedarikçinize alternatif`

---

### ⑬ A/053 · Winet（`WINET-` / `OEM-` 自有品牌，公开标价）

| 它的型号 | 它的规格 | 我方对位 | 打法 |
|---|---|---|---|
| **`OEM-8-PORT-GB-POE`** | 7 口 PoE（24/48 V）+ 1 上行，**2,916.76 ₺ + KDV** | **`EW-S1710FG-AP`**（8×GE PoE + 2 SFP, af/at）→ 升级版 **`EW-S1810CF-AP`**（300 m + watchdog + bt 60 W） | ⭐ **引用它的页面价开场**；af/at + 长距 + watchdog = 三档升级 |
| （Hotspot / WIPoint / Firewall 线） | 酒店/园区网络 | `EW-ES3006CG-AP`（4 口云）/ `EW-ES3028CG-AP`（24 口 400 W 云） | ⭐ **云 PoE 补它的 Hotspot 方案** |
| **缺口** | 只见 8 口 PoE 一款（需核全站） | 16/24 口全档 + 工业 | 增量 |

**首封主题**：`OEM-8-PORT-GB-POE muadili + 16/24 port ekleme`

---

### ⑭ A/054 · TekniksatGroup（Teknoline 品牌 + 自建工厂）

| 它的位置 | 我方对位 | 打法 |
|---|---|---|
| 官网有 **`NETWORK ÜRÜNLERİ`** 分类（无自有网络品牌叙事） | 全线交换机 + 光模块 | ⭐ **先问该分类现有品牌，再决定"替换"还是"新增"** |
| **Teknoline**（转发器/编码器/RF 光端机/MediaBOX） | ⭐ **Teknoline 牌 PoE**（它已是品牌运营商） | 谈"再挂一条 Teknoline 交换机" |
| 强项：RF/IF 光端机、光纤分配 | `EW-810GS-20`、`EW-10GSFP-SR`、`EW-610SM-20` | **光 + 电打包** |
| **缺口** | 无自有网络品牌 | 贴牌 |

**首封主题**：`Teknoline markası için PoE switch + SFP paketi`

---

### ⑮ A/075 · Technopc（27,500 m² / 250+ 人 / 国产货证书 / SAHA+Ostim 双会员）★ 最大 OEM 机会

| 它的位置 | 我方对位 | 打法 |
|---|---|---|
| **工业电脑 / 服务器 / 存储 / AI 基础设施** | ① 工业 PoE：`EW-PIS1810-8GE`、`EW-PIS3610M-8GE` ② ToR/存储汇聚：**`EW-S53928QM`（24×10G+4×100G）**、`EW-S5954GM-AP`（L3+ OSPF/VRRP） | ⭐ **同一张 BOM**（工控机 + 柜内交换机） |
| **政府/国防/关键基础设施客户** | 需要 EGM/项目准入 + 土耳其语文件 + 长期供货 | 谈 **本地组装/贴牌 + 本地保修** |
| **Yerli Malı Belgesi（国产货证书）** | ⚠ 纯中国直发与其叙事冲突 | ⭐ **把"本地交付与保修"作为主卖点，别把"中国工厂"当卖点** |
| **缺口** | 它没有自家网络品牌 | 贴 technopc 牌 PoE/ToR |

**首封主题**：`Endüstriyel PC ve sunucu projeleriniz için switch tedariki（yerel garanti）`

---

### ⑯ A/099 · Viva Bilgisayar（Hatay，Hikvision Silver Partner）

| 它的位置 | 我方对位 | 打法 |
|---|---|---|
| **Hikvision Silver Partner**（项目集成 + 经销） | Hikvision 项目 PoE：`EW-S1927CG-AP`（24）/ `EW-S1710FG-AP`（8） | "非 Hikvision 牌"的合理替代 |
| **哈塔伊震后重建**（2023 地震灾区） | ⭐ **户外/临时部署**：`EW-PIS1810-8GE`（宽温）、`EW-PIS1802-1GE`（户外单口 PoE） | **防雷 + 宽温 + DC 宽压**是真需求 |
| ⚠ 账期风险高 | — | **前两单预付或信用证** |

**首封主题**：`Hatay yeniden yapılanma projeleri için saha tipi PoE switch`

---

### ⑰ A/090 · Cansıs Teknoloji（Konya Çumra，Armiya 经销商）

| 它的位置 | 我方对位 | 打法 |
|---|---|---|
| **Armiya Teknoloji 的 Çumra bayisi** | 直接供货：8/16 口 PoE；⭐ **更优路径 = 通过 Armiya 供货** | **Armiya 才是量所在**（本土品牌运营方 → 可谈其 OEM 工厂） |
| Konya 农业机械/金属加工 | 工业 PoE（宽温/防雷）：`EW-PIS1810-8GE` | 厂区场景 |
| **ASKON Konya 会员**（登记号 4474226） | — | ⭐ **ASKON 网络可复制到全国分会** |

**首封主题**：`Armiya bayisi — PoE switch tedariki`（并**并行联系 Armiya**）

---

## 四、还缺什么（照实说）

| 缺口 | 影响 | 补法 |
|---|---|---|
| **客户侧 6 家只有"分类"没有"型号"**（Coptek L3/PoE 分类、Koza、Lansan、HCS、Antalya Turkuaz 的部分品牌、Zeytek） | 对位表只能做到"档位级"，做不到"型号级" | 下次抓 `/urunler`、`/kategori`、`sitemap.xml` 全量列表 |
| **Ruijie / TP-Link / EtherWAN 型号规格未逐条抓** | 与它们正面对位时只能给"档"，给不出"行" | 需要时再抓品牌页 |
| **我方 `EW-S*` 的**实际可报价型号与 MOQ** 来自仓库目录快照（r24 索引），**不是 2026 年 11 月的最新价表** | 报价前必须与 Peter/内部对齐（见 TASK-STATUS 待办 7） | 报价前复核 |
| **模块化机型（`SRX-GS24PMX`）我方没有** | NFS 对位表断一行 | 照实说没有 |
| **EwindCloud 生态成熟度弱于 Omada / Ruijie 云** | 与 #35 打不了云战 | 只打非管理/轻管理批量 |

---

## 五、下一步（可直接派活的四件事）

1. **A/052 Nokta（upTech）**：抓 `noktaelektronik.net` 的 upTech 交换机全量型号页 → 出**逐行对位表**（916 SKU 里的交换机子集）。**这是全表最高 ROI 的一件事。**
2. **B/010 ErETE**：抓 `OPEN NETWORKING` 与 `NOS` 两个分类 → 确认**IP Infusion 是独家还是非独家** → 决定我方是"硬件供应商"还是"联合方案方"。
3. **B/062 Cebeci**：抓 `Cifocs` 品牌在土全系列 → 判断 `Cifocs` 是**自有商标**还是**代理**（若是自有，OEM 谈法成立）。
4. **A/053 Winet**：抓全站 PoE 分类 → 确认 8 口之外是否有 16/24 口（决定"补位"还是"替换"）。

---

**相关文件**
- 逐家详情：`TR Customers/B/*.md` 的「附：B 档深挖（r46）」、`TR Customers/A/*.md` 的「附：A 档深挖（r47）」
- B 档横向总表：`…/08-customer-pipeline/115-turkey-b-tier-deepdig-2026-11-01.md`
- 我方产品目录（对位表右列来源）：`…/06-competitors/112-ewind-website-mirror-2026-10-21.md`
- 生成脚本：`…/08-customer-pipeline/build_tr_customers_r44.py`（已内置 A/B 深挖注入）
