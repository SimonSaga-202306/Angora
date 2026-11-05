# -*- coding: utf-8 -*-
"""r53 补录（2026-11-01）：CLR 2.5G 线功率与 bt 实锤（推翻 r52 判断）+ CRL 工业线换牌实证 + Technopc 交换机目录为空。"""

D = {}

# ---------------- A / 001 Telkolink + GelecekBT ----------------
D['1'] = """
### ⭐⭐ r53：`CLR-MRS-8330P` 规格到手 —— **它 1–4 口就是 802.3bt 90 W**，我 r52 的判断被推翻

#### A. 🛑 修正 r52（本档 2026-11-01 r52 附录 E 节、`121` §一.4、`116` 2.5G/bt 两行）
r52 写的是「**没有一款 2.5G SKU 标 802.3bt**」「`CLR-MRS-8330P` 的 PoE 功率未知」「2.5G PoE 只有 100 W」。
r53 拿到 `CLR-MRS-8330P` 产品页**完整技术表**，三条全部**不成立**：

| r52 原判断 | r53 实测（原文） | 判定 |
|---|---|---|
| 2.5G 线无 802.3bt | **`Ethernet: 24* 100/1000/2500 Mbps PoE Ports (Ports 1-4 support IEEE802.3bt(90W))`**；PoE Standard 栏同时列 **af 15.4W / at 30W / **bt 90W** | ❌ **推翻** |
| `-8330P` 功率未知 | **`PoE: PoE Total Power maximum 400W`**，整机功耗 **max 52 W**，电源 **DC 54V 7.69A + 12V 5A** | ✅ 已核实 **400 W** |
| 2.5G PoE 上限 100 W | 100 W 只是 `-8109P`（8 口）；24 口那台是 **400 W** | ❌ **口径错**，已改 |

→ **结论改写**：CLR 的 2.5G 线**已经是「24 口 2.5G PoE / 400 W / 前 4 口 bt 90 W / 6×10G SFP+ / L3」**。
**它真正剩下的缝只有一条，但要说得准**：**24 个 2.5G 口里只有 4 个是 bt，总预算 400 W（≈16.7 W/口均摊）**；
→ 我方切入点 = **「24 口全 bt + 800 W 级」**（`EW-PIS5728GM-AP-BT`：28 口 L3 / 800 W / 24×bt），
而**不是**r52 说的「它没有 bt」。

#### B. `CLR-MRS-8330P` 完整技术表（产品页原文逐项）
| 项 | 值 |
|---|---|
| 端口 | **24×100/1000/2500 Mbps PoE（1–4 口 802.3bt 90 W）+ 6×10G SFP+ + 1×RJ45 Console** |
| 交换容量 / 转发 | **240 Gbps / 178.56 Mpps** |
| 内存 | DDR **512 MB** / Flash **32 MB** / Buffer 16 Mbit / MAC **32K** / Jumbo **10K** |
| VLAN | 1–4094，最大活跃 4K |
| PoE | **af 15.4 W / at 30 W / bt 90 W**；**总预算 400 W** |
| 协议 | 802.3/3u/3ab/3z/3ae/3x/**3az**/3ad、**1AB LLDP**、**1D/1w/1s**、**1Q/1p**、**1X** |
| EMC | EN61000-4-2 (ESD)、**EN61000-4-5 (Surge)** |
| 工作温度 | **−10~50 °C**（存储 −40~70 °C） |
| 尺寸 / 重量 | **440×281×44 mm** / **N.W 4.37 kg** / 5 台/箱 26.7 kg |
| 灯 | PWR/SYS/Link/ACT + **PoE 使用率灯（<90% 灭 / 90–95% 闪 / >95% 常亮）** + 超温超压告警灯 |
| 复位 | 短按 <5 s 重启、长按 >5 s 恢复出厂 |
| L3 | IPv4/IPv6 VLAN 接口、IPv4 静态路由、ARP |
| 认证 | CE / FCC / RoHS |

⭐ **注意两个短板**（谈判用）：① **工作温度 −10~50 °C**（商用级，不是工业级）；② **L3 只写到「IPv4 静态路由」这一层**（产品页 L3 栏没有 OSPF/VRRP，与 `CRL-SW-L3-2404-10G`（有 OSPF+VRRP）**不同档**）。→ **谈路由能力时它有缝**。

#### C. `CLR-MRS-8312P` 的 PoE 口径（第二个证据点）
产品页「Şartnameler」原文：**「8 个 PoE 口全部支持 802.3af / 802.3at」**、**「每口最高 25 W」**、**「总 PoE 预算 250 W」**。
→ 即 **8 口 2.5G PoE，25 W/口上限，250 W 总预算**（**低于 at 的 30 W 满档**）。

#### D. r53 新增的 CLR 型号（此前未入档）
| 型号 | 规格 | 我方对位 |
|---|---|---|
| ⭐ **`CLR-SWT-7514C`** | **12×10G RJ45 + 2×SFP+ 全 10G 网管**（"Full 10G anahtar"） | 我方 **`EW-S6809`/`S6818`** 只到 2.5G；**这是它比我方强的一档**（10G 电口 12 口） |
| `CLR-SWT-7520F` | 8×GE RJ45 + **12×SFP+** L2 网管 | `EW-810GS-10` 系（10G SFP+ 汇聚） |
| `CLR-SWT-7312F` | **12×1G/10G SFP+ L3** 光纤骨干 | 同上 |
| `CLR-SWT-4804N` | 48×GE + 4×10G SFP+ 网管 | **`EW-S5748GM-AP`**（48 PoE + 4×10G） |
| `CLR-SWG-1724` | 24×GE 非网管机架金属壳 | `EW-S1824` 系 |
| `CLR-IES-T120N` | **12×1G/10G SFP+ 工业骨干**，**240 Gbps / 178.56 Mpps**，双核 1 GHz，4 Gbit DRAM / 128 Mbit Flash，**32K MAC**，**DC 12–48 V 凤凰端子 + 防反接**，**−40~+85 °C**，25 W，166×150×75 mm（导轨） | `EW-EPIS3910-8GE` 只到 8 口 GE；**它在工业 10G 骨干这档比我方全** |

→ ⚠ **必须承认的一条**：**在「10G 电口」和「工业 10G SFP+ 骨干」这两个细分档，CLR 的型号比我方齐**。**不要在场景里挑这两档正面比**，改打 **2.5G 全口 bt + 大功率** 与 **2.5G 长距 300 m**。

### 证据等级（r53）
- 已核实：**`CLR-MRS-8330P` 全表**（产品页技术规格原文）、**`CLR-MRS-8330N`**（同页 N 版：240 Gbps / 178.56 Mpps / 512 MB DDR / 32 MB Flash / 32K MAC）、**`CLR-MRS-8312P` 的 25 W×8 / 250 W**、**6 个新增型号与端口配置**、`CLR-IES-T120N` 全表。
- 仍空白：`CLR-MRS-8226N/8218N` 的交换容量、`CLR-MRS-8109P` 的 100 W 是否含 90 W 口、CLR 独家性、CLR 的深圳工厂名。
"""

# ---------------- A / 005 CryptoLink ----------------
D['5'] = """
### ⭐⭐ r53：两份工业线 datasheet 读到 —— **PDF 里还留着原厂牌子「CrystalWAN」**

#### A. 换牌实证（比"Authorized Dealer"更硬）
`DatasheetofCRLISW-14.pdf` 的**封面页眉原文就是 `CrystalWAN Network Solutions`**，而内页型号写作 **`CRLISW-414`**；`CRLISW-08.pdf` 内页型号写作 **`CRLISW-8P`**。
→ **同一份 PDF 里同时出现三个名字（CrystalWAN / CRLISW-414 / CryptoLINK）** ⇒ **它不是品牌方，是把 OEM 的 PPT 直接改个封面**。这条与 r52 的「Authorized Dealer」页脚互为印证，**r52 的「代理品牌」判定成立且证据升级**。

#### B. 两个工业型号全表
| 项 | **`CRLISW-08`（PDF 内 = `CRLISW-8P`）** | **`CRLISW-14P`（PDF 内 = `CRLISW-414`）** |
|---|---|---|
| 品名 | 10 ports Gigabit Managed Industrial PoE Switch | 12 Port Gigabit Yönetilebilir Endüstriyel PoE Switch |
| 端口 | **8×10/100/1000 PoE + 2×GE SFP + 1 Console** | **8×10/100/1000 PoE + 4×GE SFP + 1 Console** |
| PoE | **af 15.4 W / at 30 W**；**总 240 W**；DC48V 输出；自动识别 af/at | **af 15.4 W / at 30 W**；**总 120 W**；DC48V |
| 交换 | 24 Gbps / 4 M buffer / 1.488 Mpps 每口 | 24 Gbps / 4 M buffer / 1.488 Mpps 每口 |
| MAC | 8K | **16K** |
| 冗余 | **STP/RSTP/MSTP + ERPS**、静态+LACP 聚合、VLAN/QoS/ACL、**PD Alive Check (WatchDog)** | 同左（+ NTP） |
| 管理 | **WEB / Telnet / CLI / SSH / SNMP v1v2v3 / RMON** | 同左 |
| 供电 | **双路 DC48–55 V 凤凰端子（V1± V2±）+ 防反接** | 同左 |
| 温度 | **−40~85 °C** | **−40~85 °C** |
| 防护 | **IP40 金属壳**、防雷 **6 kV / 差模 4 kV / ESD 15 kV** | 同左 |
| 尺寸 | 166×120×60 mm，0.5 kg，导轨/壁挂 | 同左 |
| MTBF | 100,000 h | **800,000 h** |
| 光模块支持 | 多模 2 km；单模 1310 nm 20 km / **1550 nm 60/80/100/120 km** | 同左 |

#### C. 与我方对位（结论：**工业段它只有 af/at 30 W，这是我方最干净的一刀**）
| 它的型号 | 我方 | 差距 |
|---|---|---|
| `CRLISW-8P`（8 PoE + 2 SFP，**240 W**，af/at） | **`EW-PIS1810-8GE`** / **`EW-EPIS3910-8GE`** / ⭐ **`EW-PIS3810M-8GE-BT`** | 我方 **bt 60/90 W + 12/24 V 被动 + 云 + 单口远程重启** |
| `CRLISW-414`（8 PoE + 4 SFP，**120 W**，af/at） | **`EW-EPIS3910-8GE`**（8 口 + 2 SFP） | 它 4 个光口；我方 2 个 → **可提「4 SFP 版」定制** |

→ **一句话**：**它的工业线 100% 停在 af/at 30 W、温度好但功率小**；对「边界安全 / 车牌识别 / 政府项目」这类**要多摄像头 + 加热器/云台**的场景，**bt 60 W 是硬需求**。
**首封补一句**：`CRLISW serisi 30W'ta kalıyor; 802.3bt 60W endüstriyel modelimiz aynı fiyat aralığında.`

### 证据等级（r53）
- 已核实：两份 PDF **全表**（`CrystalWAN` 字样、内部型号 `CRLISW-8P` / `CRLISW-414`、PoE 预算 240 W / 120 W、−40~85 °C、IP40、MTBF）。
- 仍空白：`CRL-MC02`、`CRL-SFP-10G-LC`、`CRL-SFP-125 LC` 三份 PDF 未读；它是否也卖别家工业交换机。
"""

# ---------------- A / 075 TechnoPC ----------------
D['75'] = """
### ⭐⭐ r53：**它的「Network Çözümleri」里没有交换机** —— 目录是空的

#### A. 官网实证
`technopc.com.tr/network-urunleri/` 的营销文案写得很满：
> 「**gigabit ve 10G destekli switch modelleri**, PoE çözümleri, firewall, Access Point, **VLAN desteği, Layer 2/Layer 3 yönetilebilir switch seçenekleri ve bulut tabanlı yönetim**」

但**实际渲染出来的产品只有 5 个，全是防火墙与 SD-WAN，一台交换机都没有**：

| 型号 | 类别 | 配置 |
|---|---|---|
| `FW801` | Firewall | Intel 6./7. nesil / 16 GB DDR3 / 2×2.5" HDD / **SIM kart** |
| `FW622` | Firewall | Celeron N3060 / 8 GB / 2 TB / **6×Gigabit LAN** |
| `FW57` | Firewall | Celeron 3205U / 16 GB / 2 TB / **2×COM + 2×LAN** |
| `NSW 4500` | SD-WAN | **Intel Atom 2.2 GHz** / 2×SO-DIMM DDR4 / 1×2.5" / **6×LAN + 4G LTE** |
| `NTSN 6500F` | SD-WAN | **Atom C3558** / 128 GB DDR4 / **6×LAN + 2×SFP** |

页面底部直接写 **「Seçilen filtrelere uygun ürün bulunamadı.」**；`technopc.com.tr/switch/` → **404**。

#### B. 结论与打法（A- 档，55 分 → 应上调到 **70**）
1. **它是「想卖交换机但还没有交换机」的厂商** —— 营销页已经把 **gigabit/10G、L2/L3、PoE、bulut yönetim** 写进 promise，但**产品位是空的**。
2. ⭐ **身份卡里的「工业 PoE 采购 E-wind」是既成事实** ⇒ **这是全名单里唯一一个「已经是我方客户、且公开承认要卖交换机、却还没有交换机产品」的 A 档**。
3. **打法不是"新客户开发"，是"扩品类"**：把 `EW-S1927CG-AP`（24 PoE）→ `EW-S2926GM-AP`（24 PoE 网管）→ `EW-S5748GM-AP`（48 PoE + 4×10G）→ **`EW-S6826`（24×2.5G）** 做成 **`Technopc` 牌的 Network 目录第一屏**，配 **`EwindCloud` 云** 正好对应它写的「bulut tabanlı yönetim」。
4. **它的强项是 x86（Atom/Celeron/Intel）**，交换机是纯外购 —— **不存在自研冲突**，比 Telkolink 好谈得多。

**首封主题**：`Technopc Network kataloğu için switch hattı: 8/24/48 PoE + 2.5G + bulut yönetim (E-wind üretimi)`
**必问三句**：① Network 页要什么时候上交换机？② 要 `Technopc` 牌还是白盒？③ 防火墙客户里有多少同时要 PoE 交换机（捆绑率）？

### 证据等级（r53）
- 已核实：**`network-urunleri` 页面全文与 5 个在售型号**、**「Seçilen filtrelere uygun ürün bulunamadı.」**、**`/switch/` = 404**、营销文案里的 **gigabit/10G、L2/L3、bulut** 承诺。
- 仍空白：**是否已有未上架的交换机 SKU 在渠道销售**（需问客户或查 Trendyol/Hepsiburada）、`technopc®` 商标注册号。
"""
