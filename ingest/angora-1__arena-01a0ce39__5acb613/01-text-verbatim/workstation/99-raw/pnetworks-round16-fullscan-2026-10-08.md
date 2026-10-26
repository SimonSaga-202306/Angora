# 99-raw · 第 16 轮：PNetworks datasheets 全量收尾 + rehbersanayi 全量扫描边界 + TTK 招标原文 + Edgecore 发现（2026-10-08）

> 任务来源：用户第 16 轮指令「都搞了 需你邮箱这个啥意思？」= ① 执行第 15 轮 3 条低优线索（rehbersanayi 全量 547 条扫描 / PNetworks 其余 ≈19 份 datasheets / TTK 95.24Mpps 定制关系证实）② 解释"需你邮箱"（Volza/TradeData.pro 免费样例需注册邮箱，见本轮回复，非新信源）。
> 方法：datasheet PDF 经 fetch_page 逐份解析（剩余 15 份全部抓完）；rehbersanayi 穷举分页机制（?page=/?sayfa=/路径段/非 www 域名全测）+ `/ara` 站内搜索 + Google 索引检索；TTK 招标技术规格书 PDF 直抓（taskomuru.gov.tr 官方）。
> 结构化结论同步进 `06-competitors/110-turkey-local-competitors-*`（规则 5，§10 + 行 1 刷新）。

---

## 一、PNetworks datasheets 全量收尾（本轮 15 份；累计 26/27 唯一项，1 死链）

### 1.1 本轮解析的 15 份（含 WiFi）

| 型号 | 定位 | 端口/性能（PDF 原文） | 电源/环境 | 原文问题（QA 信号） |
|---|---|---|---|---|
| PN-LMS24GE2SFP PoE+ | 24GE+2×1G SFP | 26 口，52Gbps/"38Mbps"（=38Mpps 笔误）/26Gbps，16K MAC | 48-54VDC，−40/+70 IP53，482.6x43.65x160mm 1220g | 24 口设备印 8 口壳尺寸（复制错误） |
| PN-LMS24GE4SFP+ PoE+ | 24GE+4×10G SFP+ | 28 口，128Gbps/"95Mbps"（=95.24Mpps 笔误）/64Gbps，16K MAC | 48-54VDC，−40/+70 IP53，2465g | PoE 预算 240W（vs CMS24 PoE+ 的 500W → LMS=低预算系列）；"Sectors" 段仍写 PN-CMS8GE2CG PoE+（错型号） |
| PN-CMS8GE4SFP PoE+ | 8GE+4×1G SFP | 12 口，24Gbps/"17Mbps"（笔误）/12Gbps，16K MAC | 48-54VDC，−40/+70 IP53，220x46x145mm 1040g | PoE 预算 250W（与 CMS8GE2CG 的 240W 不一致）；无 IEC 61850-3 认证标注 |
| PN-CMS48GE6SFP+（非 PoE） | 48GE+6×10G SFP+ | 54 口（标题正确） | 48-54VDC，−40/+70 IP53，482.6x43.65x160mm 1220g | **整表是 24 口表**（"26 口/24/2×SFP"）+ 52Gbps/38Mpps（24 口数值）+ 8 口壳尺寸；"Sectors" 段写 PN-CMS8GE2CG PoE+；IEC 61850-3 有 |
| PN-CMS8GE2SFP+PoE+ | 8GE+4×1G SFP+2×10G SFP+（标题 14 口） | 正文"10 口/8+2×SFP+"，56Gbps/"42Mbps"（笔误）/28Gbps，16K MAC | 48-54VDC，−40/+70 IP53，1040g，IEC 61850-3 | 土耳其语版 datasheet（全线唯一）；L3 表独有 **IS-IS** 条目；正文与标题端口矛盾 |
| PN-CMS48GE4SFP2SFP+ | 48GE+4×1G SFP+2×10G SFP+（54 口） | 开头分类表正确 | 48-54VDC，−40/+70 IP53，482.6x43.65x160mm 1220g，IEC 61850-3 | 正文"24 Port managed switch"+端口表"26/24/2×SFP"+52Gbps/38Mpps（全 24 口数值）+8 口壳尺寸 |
| PN-CMS24GE4SFP PoE+ | 24GE+4×1G SFP（非 10G） | 28 口，56Gbps/"42Mbps"（笔误）/28Gbps，16K MAC，PoE 240W | 12VDC，−40/+70 IP53 | 面板照片 = **"PowerConnect"（华为系品牌）机** |
| PN-CMS48GE4SFP+ PoE+（=#30 同 URL） | 48GE+4×1G SFP | 52 口，104Gbps/"78Mbps"（笔误）/52Gbps，16K MAC | 48-54VDC，−40/+70 IP53，6195g | 分类表 PoE=370W vs 正文 240W（自相矛盾）；端口表=24 口表（28/24/4×SFP） |
| PN-CMS24GE4SFP（非 PoE） | 24GE+4×1G SFP | 28 口，56Gbps/"42Mbps"（笔误）/28Gbps，16K MAC | 12VDC，−40/+70 IP53，482.6x288x43.65mm 3000g | 端口表 uplink 写 2×SFP+（标题 4×1G SFP）；面板照片 = "PRESTIGE" |
| PN-CMS24GE2SFP+（非 PoE） | 24GE+2×10G SFP+ | 26 口，88Gbps/"66Mbps"（笔误）/44Gbps，16K MAC | 48-54VDC，−40/+70 IP53，2465g | 面板照片 = "PROTECTED" |
| PN-CMS24GE2SFP+ PoE+ | 同上+PoE | 88Gbps/"66Mbps"/44Gbps，PoE 240W（PoE++ 60W 可选） | 48-54VDC，2465g | 面板照片 = "PRESTIGE" |
| PN-CMS24SFP4SFP+ | **24×SFP(1000BASE-X)+4×10G SFP+** | 28 口，104Gbps/"78Mbps"（笔误）/52Gbps，16K MAC | 12VDC，−40/+70 IP53，6195g，USB3 | 唯一端口表与标题一致的 24 口 sheet；无 IEC 61850-3 |
| PN-CMS48GE4SFP（非 PoE） | 48GE+4×1G SFP | 52 口，104Gbps/"78Mbps"（笔误）/52Gbps，**128K MAC+30,000 TCAM**（vs 其他表 16K——跨表不一致） | 12VDC，−40/+70 IP53，482.6x400x43.65mm 6195g，USB3 | 开头分类表尺寸 440x220x44mm 10kg vs 正文 6195g（矛盾）；面板照片 = "MAGC1 12-RFK3-4"（带 VGA/HDMI，非交换机面板） |
| PN-LMS24GE2SFP（非 PoE） | 24GE+2×1G SFP | 正文 26 口 vs 表 28 口，52Gbps/"38Mbps"（笔误）/26Gbps，16K MAC | **28VDC**（异常值，疑 48V/12V 笔误），220x46x145mm 1040g（8 口壳尺寸！） | 尺寸=8 口壳；端口数自相矛盾 |
| **PN-AC2（WiFi，本轮补齐 AC 线）** | **Wi-Fi 6 AP + 4G LTE CPE 二合一** | 2.4G 300Mbps / 5G 1.3Gbps；LTE 上行 150/下行 600Mbps；4×RJ45+USB+2×2 MIMO+外置 LTE 天线 | 0/+40 °C IP30，12VDC 1A，22.5x140x270mm 290g | TR-069 远程管理、WPA3、4+4 SSID、16 HW 队列、OpenVPN/L2TP/IPsec、内容检查/杀毒；标题 Wi-Fi 6 但表写 802.11ac（矛盾）→ **是运营商 CPE 形态，非企业 AP** |

### 1.2 全量账（31 项清单 → 27 唯一内容项）
- 已解析 26 项（第 15 轮 11 项 + 本轮 15 项）
- **死链 1 项：PN-AC1（WiFi，404 勿重试）**
- 空项 2 项：#22 Energy Products / #23 System Products（官网自标 "veri yok" 无数据）
- 清单重复 URL 2 组：#3=#10（pn-lms24ge2sfp-poe.pdf）、#16=#30（pn-cms48ge4sfp-poe.pdf）
- 修正第 15 轮误记："pn-cms48ge4sfp.pdf 死链" 实际是取 URL 时打错——**PN-CMS48GE4SFP（大写 URL）可正常访问**，本轮已解析

### 1.3 ⭐ 白牌平台复用实锤（本轮最重要发现之一）
多份 datasheet 的**机前面板照片印着其他品牌**：PACIFIC WIRELESS（LMS24GE2SFP PoE+）、PRESTIGE/PRESTIGIOUS（LMS24GE4SFP+ PoE+、CMS24GE4SFP、CMS24GE2SFP+ PoE+）、**PowerConnect（华为系，CMS24GE4SFP PoE+）**、"PROTECTED"（CMS24GE2SFP+ 非 PoE）、"MAGC1 12-RFK3-4"（CMS48GE4SFP 非 PoE，带 VGA/HDMI 的非交换机面板）。
→ 解读：PNetworks 的 CMS/LMS 企业工业线是**白牌 ODM 平台 + 贴牌**（照片直接沿用 ODM 其他客户/公版照片），与"自有设计"叙事矛盾。结合 1.4 的 Edgecore 证据，PNetworks 全产品线 = **ODM 硬件（Edgecore/白牌平台）+ SONiC/OcNOS 软件 + PAVO 防务叙事 + Teknopark "Made in Türkiye" 标签**——与 Angora×Ewind 结构同构（"本土"= 本地化品牌与认证，硬件在华/在台 ODM）。

### 1.4 ⭐ Edgecore 战略合作（第 15 轮 About 页线索 → 本轮坐实）
- **Edgecore 官方新闻稿（MWC 巴塞罗那，2024-02-29）**：Edgecore × PNetworks 战略合作，面向土耳其市场交付 **AI/ML 解决方案：Intel Habana AI 加速器 + Broadcom 交换芯片 + SONiC 平台**；Edgecore 总裁 Heimdall Siao 与 **PNetworks CEO Can Okan Dirican**（注意：PNetworks 自己的 CEO 是 Dirican；Bilal Yıldız 是 PAVO 集团 CEO；2023 MWC 时 PNetworks 总经理 = Ömer Ragıp Özkan——高管已更替）联名
- PNetworks About 页（2024-10 更新）：与 Edgecore 合作 "extend Edgecore's provision of innovative networking solutions…capacities of **400G/100G/25G/10G/2.5G/1G** tailored for data centers, service providers, and enterprises" + IP Infusion 合作（OcNOS 自 2016 起支持 Edgecore 硬件）
- **结论**：TMS 数据中心线（1.86/3.6Tbps）+ 高端口密度企业线的硬件底座 = **Edgecore（台湾 ODM，Broadcom 芯片）**；SONiC = NOS 底座之一 → 第 14 轮"本土 switch"的"本土"成色进一步降级为**本地化品牌 + 软件集成 + 防务叙事 + 国家背书**
- **装机量自述**（About 页，未验证）："nearly **100,000 devices installed and actively operational across 80 provinces**"——若属实，说明其渠道渗透远超第 15 轮"渠道窄"判断；与 EKAP 0 命中并存的可能解释：大量走企业/运营商非公共标单渠道 + 官网营销口径，**标注：自述，待核**

### 1.5 零售价格情报（n11.com，PNetworks 品牌店，2026-10）
- **PN-CMS48GE4SFP+ PoE+：156,612 TL**（活动价 144,666 TL）
- "Pn48ge4sfp Poe+"（L2 可管 48+4 SFP PoE+）：**150,812 TL**（活动价 139,301 TL）
- → 48 口 1G+10G 上联 PoE+ 交换机零售 ≈ 14–15 万 TL 量级；PNetworks 已在电商（n11）公开零售，不只有 L&N 公共部门渠道

---

## 二、rehbersanayi 全量 547 条扫描 —— 方法与边界（多方法穷举后如实收口）

### 2.1 分页机制穷举（本轮新做）
| 尝试 | 结果 |
|---|---|
| `?page=2`（www / 非 www） | 返回与第 1 页**完全相同**的内容（参数被忽略） |
| `?sayfa=2` | 同上（参数被忽略） |
| 路径段 `/…/bilisim-…/2` | **404** |
| 第 1 页 chunk 0–3 全抓 | chunk 0–2 = 记录 01–60，chunk 3 = 页脚（数据源说明） |
| `/ara?q=pnetworks`（站内搜索，404 页暴露的端点） | **0 结果**（搜索只覆盖企业目录/OSB/行业/城市，不覆盖中标记录）；目录中无 PNetworks 注册企业 |
| Google 索引 `site:rehbersanayi.com` + pnetworks/angora/ewind | 0 命中（唯一 "angora" 结果 = 安卡拉房地产公司 PLATİN ANGORA GAYRİMENKUL，无关） |

### 2.2 结论（边界声明）
- 547 项中 **HTML 实际暴露 = 60 条（记录 01–60，2026-10-06 → 2026-09-28）**；其余 487 条由**客户端 JS 分页加载**（无公开 API 端点被发现）
- **更正第 15 轮口径**：第 15 轮记"已扫 ≈120/547 条"为误估（当时按"6 页 × 20 条"计）；实际第 1 页 HTML 共 60 条，即**已扫 60/547（≈11%，最新段 2026-10-06→09-28）**
- 60 条逐条扫描 + 站内目录搜索 + Google 索引三路：**PnetWorks/PNetworks/PAVO/Ewind/Angora（网络）0 中标命中**（0 家作为中标方出现）
- 补充市场信号（本轮 60 条内）：Bilgibim 36.5M TL 服务器/存储延保 **1 家投标**；CCC Command Control 58.1M TL 气象站硬件 **1 家投标**；Balkan Elektrik 93.2M TL 台式电脑 4 家 → "≤2 投标常态"再次得到样本支持
- 收口判定：在无浏览器环境下，rehbersanayi 的 IT 归档扫描**已到可穷举边界**（60/547 + 两路旁证）。若用户后续要求 100% 全量，需要：本地浏览器渲染 JS 分页 或 EKAP 官方 API 账号

---

## 三、TTK 招标原文核实（"95.24Mpps 定制"假设 → 降级）

### 3.1 原文（taskomuru.gov.tr 官方技术规格书 PDF：《2026 YILI TÜRKİYE TAŞKÖMÜRÜ KURUMU YEDEK SWİTCH TEMİNİ TEKNİK ŞARTNAMESİ》，6 页）
- **TTK = Türkiye Taşkömürü Kurumu（土耳其煤矿机构，宗古尔达克）**（更正第 15 轮"土耳其国铁"的误读——TTK 是煤矿，不是 TCDD 铁路）
- 2025-12-25 imzagazetesi 预告：30 台可管交换机（总管理处 + 下属企业合并），投标截止 2026-01-15 14:00，30 天交付宗古尔达克
- 规格书分 **3 类交换机**：
  - **2.1 24 口千兆骨干（Omurga）**：24×SFP(1/10/100M) + 8×GE combo + 4×10G SFP+（28 口不阻塞）；**128Gbps + 95.23Mpps**；16K MAC；L3 静态 + RIP/OSPF；802.1X；−10/+50 °C；端口 4kV 保护；**MTBF ≥760,000h**；CE/FCC/RoHS；19" 机架；**2.1.27 全部同品牌**
  - **2.2 24GE + 4×SFP+ 边缘（Kenar）**：24×Base-TX + 4×10G SFP+；**128Gbps + 95.24Mpps**；16K MAC；RADIUS/TACACS+；静态 124 v4/50 v6 路由；LBD、线缆诊断、双镜像、768 ACL（含时间基）；−5/+50 °C；**2.2.39 全部同品牌**
  - **2.3 48GE + 4×SFP+ 边缘**：48×Base-TX + 4×10G SFP+；**176Gbps + 130Mpps**；**32K MAC**；其余同 2.2；−5/+50 °C
- **⭐ 2.2.40（重大条款）**："Teklif edilecek Transceiver modüller (SFP/SFP+) omurga ve kenar anahtarlar ile **aynı markaya sahip olmalıdır. OEM markalar kabul edilmeyecektir**" = **所投 SFP/SFP+ 光模块必须与交换机同品牌，不接受 OEM 品牌光模块**
- 3.3：投标方须附**针对本次招标的制造商/分销商授权书**（sales & technical support authorization）
- 3.9：须附售后服务资质（Gümrük ve Ticaret Bakanlığı 售后能力证 或 TSE 服务点资质）
- 3.1/3.10：2 年保修；30 天交付

### 3.2 假设判定（本轮结论）
- **95.23/95.24 Mpps + 128Gbps = 24GE(+4×10G) 类交换机的市场标准线速参数**（24×1G+4×10G 全双工 = 128Gbps；按 64B 小包折算 ≈95Mpps）；176Gbps/130Mpps = 48GE+4×10G 的标准参数
- → 第 15 轮"TTK spec ≈ CMS24 datasheet 数值，疑似按招标定制"**降级为不成立**：TTK 写的是通用市场标准参数，PNetworks CMS24 datasheet 印的也是标准参数（还打错成 "95 Mbps"）。**无定制证据**；两者数值吻合 = 同源标准参数
- 但规格书整体与 PNetworks CMS/LMS 能力面**高度贴合**（24/48 口 GE+10G 上联、L3 静态+RIP/OSPF、802.1X/RADIUS、G.8032 之外的通用集、−5/+50 °C 远低于其 −40/+70 能力、2 年保修）→ PNetworks 是这类标的天然合格者；**我方 Marvell 线（24/48 口 GE+10G、L2+/L3、工业温度）同样完全合格**——TTK 型标单对我方不是不可进入的（前提：授权书 + 售后资质 + 同品牌光模块）
- **对我方的直接启示（2.2.40）**：此类标单要求**光模块与交换机同品牌且非 OEM** → 投标需自带自品牌 SFP（我方 SFP 成本 ¥25/只，无压力）；反之，"整机买 A 品牌 + 光模块买 B 品牌"的组合方案在此类标单直接出局——**全栈（含自产 optics）在土耳其公共标单是结构性优势**，与 PNetworks 自产 PN SFP 的战略价值互为印证

---

## 四、来源清单（本轮）
1. pnetworks.com.tr 15 份 datasheet PDF（fetch_page，2026-10-08）
2. edge-core.com 官方新闻稿 2024-02-29（Edgecore×PNetworks，Intel Habana+Broadcom+SONiC；PNetworks CEO Can Okan Dirican）
3. pnetworks.com.tr/about-us（2024-10：~100,000 devices/80 provinces 自述；Edgecore/IP Infusion 合作细节）
4. epnext.com 2023-03-07（MWC Barcelona；PNetworks GM Ömer Ragıp Özkan）
5. taskomuru.gov.tr/ihale/dosyalar/EK-4 Teknik Şartname（TTK 2026 备用交换机技术规格书 PDF，6 页全文）
6. imzagazetesi.com/ttkdan-switch-ihale（2025-12-25，30 台、2026-01-15 截止、30 天交付）
7. rehbersanayi.com（IT 归档 60 条 HTML 全量 + 分页机制穷举 + /ara 站内搜索 + Google 索引交叉）
8. n11.com/bilgisayar/…?m=Pnetworks（零售价 156,612 / 150,812 TL）
