# r34 · 生态公司全站爬取 verbatim 摘要（2026-10-21）

> 宪法第十条：本轮抓取全部信息落库。抓取通道=fetch_page 直连 + web_search；proxy InvalidAccessKeyId 一次（post-sitemap 第 1 次），改直连成功。
> 对平：24 个抓取目标（18 站成功 / 2 维护 / 2 不可达 / 1 404 链 / 1 搜索代偿）+ 语料上下文 16 处 verbatim。

## 0. 语料公司清单（grep `01-knowledge-base/wechat-conversation-aligned.md`，-i 命中数）

| 名称 | 命中 | 性质判定（r34 深挖后） |
| --- | --- | --- |
| Taylan | 65 | ⚠️ **人**（Angora CTO，L214/L302「our CTO」），非公司，不入司库 |
| Marvell | 55 | 芯片供应商（我方 AC 系列+Larch 全平台+Saga 主平台） |
| CENTEC | 30 | 芯片供应商（我方 L3 线，L627 verbatim 见 §6） |
| Turk Telekom | 33 | 终端客户/甲方（TT 项目线，既有档案） |
| Karen | 22 | 人（NEM Engineering 采购联系人，L6916 verbatim 见 §6） |
| D-Link | 26 | 全球品牌竞对（r34 新爬，110 行 90） |
| Maipu | 13 | 中国 OEM 竞对（r34 新爬，110 行 95） |
| TronX | 10 | ⭐ Angora 姊妹品牌（同厂 ODM 双品牌，110 行 96） |
| NetworkMarket | 10 | 死站（r31 结案，networkmarket.online） |
| Larch | 6 | 以色列白盒 OEM/ODM（⭐最高优先深挖，41 号 §10） |
| Rima | 6 | 土耳其安全集成商（111 行 13，r33 结案） |
| MikroTik | 6 | 全球品牌（官网维护中，记档） |
| Kyland | 5 | 中国铁路工业（110 行 89，r33 结案） |
| Moxa | 4 | 全球工业品牌（r34 新爬，110 行 92） |
| Dahua | 4 | 全球安防+数通（r34 新爬，110 行 91；L9275「Dahua won it?」） |
| Elips | 3 | ⭐ 竞标+资本伙伴（126 号；r34 法定实体名坐实 §4） |
| Netaş | 3 | 本土防务 IT（110 行 2；r34 官网增量 §2.11） |
| Hirschmann | 2 | Belden 工业品牌（110 行 93；L7848 NETAS 替换目标） |
| NEM Engine | 2 | SFP/GBIC 供应商（nemengine.com；Karen 在任） |
| Sagatele/Saga | 2（+Saga 4） | ⭐⭐ 我方深圳 ODM 工厂（§3 全证） |
| H3C | 1 | 定位基准（L10381）；r34 新爬（110 行 94） |
| D-Link 域名修正 | 26 | 原 grep=1 系大小写误低，-i 复核=26 |
| Hikvision | 1 | 全球安防（110 行 19 打包行已含；r34 官网增量 §2.8） |
| Connexite | 1 | 英国客户（Amazon Business 订单 Plan-DRAFT.pdf，L5813） |
| cryptoink | 1 | OEM 白牌（88 台死单后线，L10362；站不可达 §5） |
| UDE | 1（L2698 实名域） | 我方 RJ45 连接器供应商（TPEX:3689） |
| Saga | 4 | =Sagatele 同一实体（L528/L2368/L4042/L8765） |
| 域 | 7 | networkmarket.online / ude-corp.com / sagatelecom.com.cn / rimaelektronik.com / tronx.com.tr / mikrotik.com / drive.google.com |

## 1. Larch 第二波（larch-networks.com，全部直连成功）

### 1.1 post-sitemap.xml = 26 篇 blog 全列表（时间线）
FYUZ 2024 → Teledyne LeCroy SAI 开源测试平台 → electronica 2024 → MWC Barcelona 2024 → Embedded World 2025 → **Xsight Labs 合作**（design/develop/integrate Xsight 产品）→ case×3（vendor-agnostic SAI 解绑专有软件 / 恶劣天气 radio-link 视频 / OpenROS 同轴）→ 工业 16x/8x/48x PoE 产品页（48x=ISW-Rack-48GTPoE4XG_USB-2ch-DC）→ **Orama X25N/X400 PB 页** → FYUZ 2025 → **⭐2025-11-02 加入 SONiC Foundation** → Campus L2/L3 → **AC5/AC5X 有/无 MACsec** → PANTHEON 合作（2025-11-18）→ MWC Barcelona 2026-02 → **BFD+ 硬件加速 SONiC**（2026-02-05 case）→ productizing SONiC（2026-02-25）→ Embedded World 2026 → **SONiC on ARM edge**（2026-03-17）→ INNOVEX@COMPUTEX Taipei（2026-04-14）→ **Hardened SONiC on Marvell Ironman**（2026-05-19）→ AVNET Americas FAE Institute（2026-07-21）→ **autonomous mining 网络方案**（2026-08-11）→ electronica India（2026-09-15）→ **航空器内网鉴权 case**（2026-10-06）→ **Teledyne LeCroy 800G-validated SONiC AI networking@OCP**（2026-10-07）→ Dorado@OCP（2026-10-10）→ **Amphenol TSN for A&D @ Aerospace & Defense TSN Summit**（2026-10-20，最新）。

### 1.2 contacts（/about-larch-networks/contacts/）
11 Amal str, Rosh-Ha'ayin 4809239, Israel；+972 3-901-6117 / 6118；销售 +972 55-966-1282；info@larch-networks.com。

### 1.3 OCP Dorado 文（2026-10-09，booth B31，OCP 2026-10-13/15）
AI 以太网 fabric 演示 = **Marvell TeraLynx 10 spine-leaf + Larch Hardened SONiC + NVIDIA ConnectX-7 GPU 服务器 + Dorado Cruz**（发现/配置/遥测/负载感知调优）。立场原文要旨=「InfiniBand 供给短缺/多年交期/复杂出口许可 → 主流企业用以太网替代」；口号「democratize AI infrastructure」。预约联系人=**Irina Murzina**（hubspot imurzina，新 BD 线）。

### 1.4 工业线 /industrial-switches/（AC3 族，chipset **98DX226S**，ROS，LN-23xx-I 前缀，DIN/rack）
LN-2304M(-P 120W) / 2308M(-P 240W) 100M / 2304GP 120W / 2308GP 240W / 2308GP-4GF / 2308G-4GF / 2308G-2GF-2G（USB+console）/ **2308GBP-2XGF PoE++ 2×60W** / 2308GMP-2XGF / 2308G-2XGF…（chunk 2 未抓全）；8 台 SFP stacking；ITS/电力/智慧城市/监控；datasheet=drive.google.com 外链。新品 LN-2304-I-SERIES（98DX226S，DC10-58V，-40~+75°C，IP40 fanless，CCC/RoHS/FC/CE/ISO，8-15KV，MTBF 100Kh，L2+可选 L3/Stacking/ROS，无价格；WooCommerce 2026-05-19 开店）。

### 1.5 DC 线 /data-center-switches/（三芯片族，全表）
**Aldrin2=98DX8548**：LN-3516XGF-6Z（16×10+6×100）/ LN-3548XGF-6Z / LN-3524XGF-6Z / LN-3548XGF-6Z-PTP / LN-3516XGE-2Z（2×40G）/ LN-3524XGE-6Z / LN-3548XGE-6Z（48×10G+6×100G）/ **LN-3524XGEP-6Z PoE++1440W**。
**Aldrin3=98DX7332**：LN-3624Y-2Z（24×25+2×100）/ -PTP。
**Aldrin1=98DX8382**：LN-3424XGEBP-4XGF（PoE++740W）/ LN-3424XGEP-4XGF / LN-3424XGEP-4Y / LN-3432XGF（32×10）。
通用=dual hot-swappable PSU / 8GB DDR4 / 32GB eMMC / hot fans / **ROS+SONiC+OpenLAN 三 NOS**。
**Falcon 族**（chunk 2）：LN-4348Y-8Z（48×25+8×100，ARM，**98CX8514**，ROS/SONiC/OpenLAN）/ LN-I-4348Y-8Z（Intel CPU 版，SONiC/OpenLAN）/ LN-4332Z1（32×100，16GB RAM，**98CX8522**，ROS/SONiC）/ LN-4332Z4（32×400，**98CX8580**，ROS）/ LN-4324Y-8Z（24×25+8×100）/ LN-4332Z1-L（8GB lite）。
**Teralynx 表**：LN-4832Z4T（32×400，**Teralynx7，IVM77700**，SONiC）/ **LN-4864Z8T（64×800，Teralynx10，98TX9180，SONiC）**。
**X2 表（NVIDIA Spectrum 系）**：LN-XS-X232Z4（32×400，SONiC）/ LN-XS-X216Z8（16×800，SONiC）。

### 1.6 Campus 线 /campus-and-access-switches/（5 chunk，抓到 1-2）
**AC5+=98DX2538**：LN-2624GP-4XGF+（24×1G+4×10G PoE+400W）/ LN-2648GMP-4XGF+（48×1G+4×10G PoE+740W）/ LN-2624G / LN-2648G（2GB DDR+1GB flash，USB+OOB+console，ROS）+ HSP+HSF 版 LN-2624GP-4XGF-HSP-HSF / LN-2648GMP-4XGF-HSP-HSF / LN-2624G-4XGF-HSP-HSF / LN-2648G-4XGF-HSP-HSF。
**AC5lite=98DX2518**：LN-2624G-4XGF-L / LN-2612GP-2XGF-L（12×1G+2×10G PoE180W）。
**AC5X=98DX3510**：LN-3824GP-4XGF（740W）/ **LN-3848GMP-4XGF（48×1G+4×10G PoE+1440W）** / LN-3824G / LN-3848G；**MACsec 版=98DX3510(M) 12 SKU**：LN-3824GBP-6Y-M（24×1G+6×25G PoE++90W 400W）/ LN-3824GBPP-6Y-M（740W）/ LN-3848GBP-6Y-M（48×1G+6×25G 740W）/ LN-3848GMP-6Y-M（1480W）/ **LN-3824MGBPP-6Y-M（24×2.5G+6×25G 740W）** / **LN-3848MGBPPP-6Y-M（48×2.5G+6×25G 1440W）** / HSP 热插电源版 ×6（AC+AC / AC+DC）。
**AC5Y（L2 接入）**：LN-2108G-4XGF（8×1G+4×10G）/ LN-2124G-4XGF（24×1G+4×10G）。
**⚠️ Campus AC3 L2=98DX223S（≠工业 98DX226S！）**：2PSU RPS 版 LN-2348G(GP)-4XGF-RPS（740W/400W）/ LN-2324G(GP)-4XGF-RPS；8 口系列 12+ SKU 含 **LN-2308MG-2XGF（8×2.5G+2×10G，2.5G 接入）** / LN-2308GF-2XGF（全光）/ combo -4C 系列。

### 1.7 其他页
PB=/pb-line/：Orama X25N+X400，1RU，聚合/过滤/负载均衡+traffic manager，对标既有监控/安全工具。/ln-001/=LN-2304-I 全规格。/team/=5 高管（41 号 §5 既有）。/clients/=24 logo（Angora 第 4）。/partners/=8 家（41 号 §5 既有）。/shop/=WooCommerce 2026-05 开店。/hardware-production-localisation/=**404**（页已删/移）。

## 2. 生态公司首页（r34 新爬，18 站）

### 2.1 maipu.com（迈普通信，北京）
全线=路由器（core/agg/access/4G5G）+交换（DC/campus/SMB/工业）+WLAN+HCI/MDC+存储+GPU 服务器+防火墙（IFW/MSG/NSFW）+5G/4G M2M+GPON（OLT/ONU/工业 ONU）+VoIP（SIP/IPPBX/IP Phone）+光模块（1G/10G/25G/40G/100G）+Matrix NMS/Managed Cloud/BD-WAN 控制器；方案=BD-WAN/VPN/Campus Wi-Fi/**AI Compute Fabric**/**RoCEv2 lossless**/HCI/100G Metro-E/Managed CPE/Cloud 4G5G M2M/Cloud Wi-Fi/FTTR 酒店。2026 展会=Secutech Vietnam（×CNTTShop）/LEAP 沙特/Interop Tokyo/CommunicAsia（中东+亚洲扩张）。

### 2.2 centec.com（Centec，苏州）
2005-01 苏州工业园区创立；定位=Ethernet switch silicon vendor + SDN/whitebox；三页=Silicon / Software / Solutions。

### 2.3 h3c.com/en（新华三）
「The leader in digital and AI solutions」；行业方案（电信/政府/金融/教育/医疗）/云与虚拟化（**Gartner 服务器虚拟化 MQ Visionary**）/全栈 AI 基础设施/AI 计算网络；新品=CAS / Uniserver R4900 G7 / **S12500X-AF DC 云交换机** / WA7539 Wi-Fi 7 AP / UIS 3000 G7 HCI / SecPath M9000-X 防火墙 / SMB Aolynk（UAP612MG-AX30）。

### 2.4 moxa.com（Moxa，工业自动联网）
「Your Trusted Partner in Automation」；rugged x86 盒式机（BXP-C101/A101）/机器安全/Ignition 集成/**NAT-G102 工业 NAT（自动白名单+Secure Boot）**/ **RKS-G4030-PL 模块化机架交换（30 口 100M~10GbE，802.3bt PoE++ 90W/口 720W 总）**；**EcoVadis 金牌 2026（全球前 5%）**；分销商/连接设备/国家数=动态 JS 计数器。

### 2.5 marvell.com（Marvell，2026 定位）
「Marvell is how AI scales」=AI silicon 龙头；五组合=Interconnect / **Data Center Switching（scale-up/out/across）** / **Networking & Security（OEM switch/PHY/compute/security 芯片←我方 AC 系在此层）** / Memory & Storage / Custom；2026=新 Retimer 3.2T+AEC DSP 1.6T（OCP 2026 Alaska）/OCP DC 安全标准工作组/二代 Structera X（6 通道 CXL 3.2）/LiquidSecurity HSM/Investor Day 2026；统计=全头部 hyperscaler 合作/光 DSP 出货数亿/30+ 连接伙伴。

### 2.6 dlink.com（D-Link，2026-10-21 首页）
**⭐ 2026-09-11 新闻=「D-Link Launches Industrial Switch Portfolio with DIS-110G Series」**=D-Link 正式进入工业交换机（正面撞我方工业线+EGM 工业标场景）；Nuclias Unity/Cloud（企业网管）/DBR 系列/4G/5G M2M/Smart+ 管理型千兆（DGS-1210，L2+L3 静态+PoE）/S 系列（2026-08）/DAP-E3620 Wi-Fi 7 AP（2026-08-12）。

### 2.7 belden.com（Belden=Hirschmann 母公司）
「Network Infrastructure & Connectivity Solutions」from OT to IT and cloud；成员=5G-ACIA/EtherCAT/Margo/SPE/TIA；行业=CPG/数据中心/能源/酒店/轨道交通/仓储物流。hirschmann.com 直连×2 失败（记档）。

### 2.8 dahuatech.com（大华，浙江大华技术股份有限公司）
「以视频为核心的智慧物联解决方案提供商和运营服务商」；三级业务=城市级/企业级/中小企业；产品类=前端/热成像/后端/存储/显示/控制/**数通产品（交换机线）**/门禁/报警/汽车电子/消防/软件平台/安检/丰视/视听广播/自动化；2026=CIIF 上海 10/12-16「AI 赋能制造」+行业峰会 10/13/Tomorrow.City 10/08/环球跨文化之旅（12 大区 61 人，2026-09-21/24，杭州）；子品牌=华消科技/华视智检/丰视科技/华感科技。

### 2.9 hikvision.com/en（海康威视，2026）
「Leading the future of AIoT」；核心=**观澜（Guanlan）大模型**（Guanlan Encoding 存储 -30~50% / See Clearer / EaseEngine）；产品=Pro 系列摄像机/AOV SolarVu 太阳能 4G/SMB 融合/Quick Pass 门禁/TalkVu 可视对讲/AcuSeek NVR（文本搜视频）/DeepinViewX；HikTech Star 2026（TikTok 活动）/Trust Center。

### 2.10 kyland.com（北京东土科技，r33 已入 110 行 89）
老站（2018 模板）；campaign=**Aquam Series（铁路 EN50155，与 r33 证据互证）**/SICOM 3000A/Hoursis 工控机/DistribuTech 2018；菜单=工业互联网/中国工业 2025/支持下载。

### 2.11 netas.com.tr（Netaş，BIST:NETAS，r34 官网增量）
Bilişim 500 双奖=系统集成业务伙伴主类：软件「年度商业应用」+硬件「电信基础设施硬件」；**土耳其 R&D 250=行业公司 R&D 支出第 3 / 全公司第 29 / 硕博人员第 15 / 女性 R&D 人员第 7 / R&D 员工第 8**；**SSB EYDEP 防务工业能力 A 级认证**（产品设计与开发）；**Microsoft 土耳其年度业务伙伴奖**；**本土服务器=ZTE 世界冠军服务器本土化**（netastan-dunya-sampiyonu-yerli-sunucu）；**Microsoft LSP 授权（阿塞拜疆+哈萨克斯坦）**；9 大智能领域=金融/能源/教育/娱乐/交通/城市/健康/公共/通信；案例=**伊斯坦布尔机场 ICT 基础设施承建+5 年运营**/Enerjisa 生产上云（×Microsoft）/Hedef Filo（×Salesforce）/Pegasus 航空数字化；2026H1 营收利润双增（新闻）。

### 2.12 turktelekom.com.tr（TT 首页，2026-10-21）
消费者面=5G 新世代套餐/家宽 640TL 起（online 专属）/TurboBox 5G 移动路由/Tivibu Android 盒子/**iPhone 18 预约（emagaza）+iPhone Duo**/McAfee 捆绑；slogan=「Değerli Hissettirir」。/tr/kurumsal=404。

### 2.13 ude-corp.com（UDE，TPEX:3689）
「Ethernet Total Solution Provider」；三方案=局域网/高速计算/车载网络；产品=以太网连接器（**QSFP-DD-800 自研**/ICM 模块化/25G Press Fit 2XN Stacked ICM 2022-04/防水 10G/M12 X-code/SPE）；**投资者页=月度营收公告**（2026/9 10-19、2026/8 09-08、2026Q2 合并财报 09-03、2026/7 08-11）+2025 股东会（2025-07-08）。

### 2.14 rimaelektronik.com（Rima Elektronik，111 行 13）
「Kurumsal Güvenlik ve Bilişim Çözümleri」；服务=安全系统/弱电/R&D/数据分析/云/应用开发/AI/网络安全/软件/基础设施/网络/系统管理/硬件设计；自研=**Digifort**（AI 视频分析 VMS：情绪/性别/年龄检测、**人脸识别宣称 99.87%**、车牌、计数、口罩、社交距离）+**Axis 分销**（IP 摄像机/音频/雷达）+工业无人机+FLIR 海洋热成像+Milestone VMS 页；品牌墙=IBM/Seagate/Cisco/Broadcom/**D-Link/Dahua**/GE/DigiFort/Axis/HP/DynaColor/**Hikvision**/AJX/Western Digital。

### 2.15 nemengine.com（NEM Engineering，搜索所得）
SFP+/QSFP/DAC/AOC 供应商；代表=NM-280-RJ45（SFP+ to RJ45）；电话 4009664008（中国大陆 400 号）；=Karen 在任的 GBIC/SFP 供应方（L6916/L8765）。

### 2.16 PNetworks（SavunmaTR/AA 2021-04-02，搜索所得）
「Türkiye'nin Switch'i」发布会 @Teknopark İstanbul：PNetworks 本土研发首个土耳其 switch；技术=切换协议+**IEEE 1588v2 PTP+Sync-E**+L3 静态路由+电源冗余可选；PNetworks×Teknopark İstanbul×Pendik 市「Türkiye'nin Switch'ini Destekleme ve İşbirliği Protokolü」；发言=Özbilen（CTO 口径）+Pendik 市长 Ahmet Cin。

### 2.17 市场旁证（搜索附带，仅记档）
Keenetic Türkiye（blog.keenetic.com.tr 2026-05-14）=Keenetic 土耳其 2026-05 开始卖 switch（110 行 9 已有主体，增量记此）；RevenueBase 2026-09=土耳其 103 家企业级 IT reseller 榜 **Elips 列第 5**（29 联系人）。

### 2.18 不可达/异常清单（宪法第十条：状态本身入库）
cryptoink.com.tr=fetch 失败×3（www/非 www，2026-10-21）→ 站休眠/死站，与「88 台死单」叙事一致；hirschmann.com=失败×2（Belden 根页已代偿）；mikrotik.com=「Service temporarily down for maintenance」×2（连产品页）；marvell.com/switching.html=404（改首页成功）；dlink.com/en/enterprise-networking 与 /en/business/solutions/managed-switches=404（改首页成功）；turktelekom.com.tr/tr/kurumsal=404；larch /hardware-production-localisation/=404；belden.com/en-hr 段=HTTP 500（改根页成功）。

## 3. ⭐⭐ Sagatele / Saga Telecom（我方 ODM 工厂，双域名全抓）

### 3.1 官网 sagatelecom.com.cn（产品目录）
「Tailored Managed Networking Solutions Provider」SHENZHEN, CHINA；**40+ SKU / 3 产品线 / OEM/ODM/SKD/CKD / CE·FCC·RoHS·REACH·UKCA**；
**STI 工业**：STI-288DGGPM（8 口 PoE+ DI/DO/RS485 双 2.5G SFP，240W，ERPS，DIN，-40°C，原生串口 I/O 免外置网关）/ STI-4240XGGM（24 口 L3 工业 DI/DO/RS485+温湿度一体，4×10G SFP+，ERPS ≤20ms）；
**STC 商用**：「**Marvell Prestera-based** access switching…8-48 口，1G/2.5G 铜，PoE++ 90W/口，10G SFP+ uplink」；STC-448XGGPM-4BT-740W（48 口 PoE++ 4×90W 740W 4×10G 1U 双 AC）/ STC-448XGGMO（48 全光 L3，13K 路由表，OSPF/BGP）；
**STH 核心**：「**CENTEC-based L3**…Full L3/VXLAN/MPLS/MLAG，10G-800G」；STH-32QC-HSI（32×400G 25.6Tbps MPLS/VXLAN/EVPN MACsec 热插电源 6 风扇，AI/HPC）/ STH-2C24XF-HSI（半宽 24×10G+2×100G MLAG 热插电源 880Gbps，两单元占 1U）；
**战略库存**=「Buffer stock held on key **Marvell and CENTEC** chipsets」；工程支持=CLI/MIB/SNMP/固件售前售后；
联系=**WhatsApp +86 15237149683 / e.sagatelecom@gmail.com**；about 链=**sagatele.com**（第二域名）。

### 3.2 官网 sagatele.com（公司页）
定位=「An Engineering & Supply-Chain-First Telecom Partner」（深圳）；**芯片平台=Marvell·CENTEC·Realtek**；定制=OEM/ODM/SKD/CKD；供给=战略库存+快交期；
三支柱=**架构稳定**（「one platform, one roadmap」，承诺深耕 Marvell+CENTEC 不横向扩张）/持续供给（芯片 buffer stock，global allocation 收紧时客户不停线）/生命周期连续（EOL 提前通知，免每两年重新选型）；
**客户分层**：主客=OEM/ODM 品牌方（「many Shenzhen suppliers can't do it; large OEMs won't bother for your volumes」）+「**Marvell Ecosystem Clients — L2+ Access Layer Specialists**」；次客=SI/ISP/小运营商（「buying from Taiwanese alternatives…position against **Taiwanese brands** on performance parity」=正面打台系）+分销/电商；
**能力页原文**：「Primary Platform — Access Layer: **Marvell Prestera AC5 Lite · AC5 · AC5+ — L2+ Managed Switching**…8/16/24/48 口，PoE/PoE+/PoE++（af/at/bt，90W/口）」← **平台命名=语料「AC5/AC3」同源**；
**We Don't（明示不做）**=云管理平台/铁路 EN50155/IP67 三防/消费路由/UL 非标/KC 等非土韩认证（→ 我方 Kyland 铁路线不在此厂）；
口径=「We're not a marketing-driven company…we put resources into engineering and inventory」；「we don't compete on every deal…not whoever quotes the lowest unit price this quarter」。

### 3.3 ⭐ 语料直证（Saga=我方工厂链，100%）
- L528 Levent：「I just wanted to check if **Saga** can supply SFPs too」
- L2368-2370 Levent：「We have a great sales funnel for 2025. **All based on Saga products. Developing all business on Saga solutions now**」
- L4042 Levent：「That's a great option. **Trust and long term cooperation is 100% with Saga.** No problems.」
- L8765：「If you buy SFP module from NEM Engineering, can you arrange paperwork so **Saga does not pay VAT** to…」=Saga 为进口/VAT 支付主体
- L6916：「Karen at **NEM Engineering** needs her GBIC」（Karen=人，NEM Engineering 采购）
→ 结构=**Marvell/CENTEC 芯片 → Sagatele（深圳，OEM/ODM 工厂+战略库存+SFP 供货）→ Angora（土耳其品牌）/ TronX（姊妹品牌）**；Sagatele 公开站即我方产品线的公开目录（STC=Prestera AC 系=我方 TT 系列平台）。

## 4. ⭐ Elips Elektronik（r33 竞标伙伴，r34 法定实体坐实，搜索 10 源）

- **法定实体名=ELİPS ELEKTRONİK SANAYİ VE TİCARET LİMİTED ŞİRKETİ**（b2bhint：registry 268901，**成立 1990-10-03**，实缴 100,000 TRY，活动码 #631108 数据处理/托管；2024-12-01 非清算状态）——r33「1988/1990」双年解释=**1988 业务起步（品牌口径，站点/LinkedIn/Kariyer 一致）+ 1990-10-03 法定设立**
- 官网=**elips.com**（非 .tr；EMIS 记 elips.com.tr=旧站）；「+30 Sene Türk Bilişim Sektörüne Hizmet」（35+ 年口径）
- 地址=Esentepe Mah. Mithat Ulu Ünlü Sok. No:1/C 34394 Zincirlikuyu/Şişli/İstanbul；Tel 0212 337 02 00 / 0212 288 37 17；elips@elips.com
- LinkedIn（564 跟随者）=1988 始于 Şişli 80m² 公寓 3 人；**2009 Normdata 合作**（HPE 授权服务点，IT150 强）；今=**Zincirlikuyu 自有 1200m² 管理楼+4 家公司+120 人团队**；81 省服务网；51-200 人；私营
- EMIS=24 员工（2026）；2024 净销售 +20.05%/总资产 +45.61%/净利率 -41.41%
- ZoomInfo=85 员工；RocketReach=营收 **$5.8M**、44 人、**Novartis Sandoz helpdesk 20 年（20 人）**、HP 耗材分销、Garny AVM 机器人收银+Rosengrens RBM 电子收银=土耳其首家/唯一技术支持
- Kariyer.net=7 年 400% 增长；Bodrum+Antalya 办公室；İzmir+Ankara 伙伴；**持 iştirak（参股公司）**
- 服务线=Microsoft 方案与咨询/项目管理/咨询/专业服务/7x24 技术支持/质保包/销售/基础设施与结构化布线/IT outsource（SLA 响应+主动监控+驻场/远程/混合）
- RevenueBase 2026-09=土耳其 103 家企业级 IT reseller **第 5 名**（29 联系人，HQ İstanbul）
- 对照 r33：客户=TWIF/Gen. Staff/Farmasi/Tekfen；HP Zorlu portal；=「that is bidding partner and they are the money behind this deal」（2026-07-06 L9751-9755）

## 5. 110 行新增（90-98）对平

| 行 | 品牌 | 层级 | 依据 |
| --- | --- | --- | --- |
| 90 | D-Link | F 全球品牌（直接竞对，r34） | DIS-110G 工业线 2026-09 + 语料 26 命中 |
| 91 | Dahua | F 全球品牌（直接竞对，r34） | 数通产品类 + L9275「Dahua won it?」+ L8805 捆绑策略 |
| 92 | Moxa | F 全球品牌（工业，r34） | 语料 L4015/L4019/L7848（铁路+NETAS 替换） |
| 93 | Hirschmann (Belden) | F 全球品牌（工业，r34） | L7848 NETAS 替换目标 + Belden 根页 |
| 94 | H3C | F 全球品牌（定位基准，r34） | L10381「position like Maipu, H3C」 |
| 95 | Maipu | F 中国 OEM（竞标对手，r34） | L2191/L2201「partner against Maipu」 |
| 96 | TronX | B 本土品牌（⭐姊妹品牌，r34） | L4290/L4314/L4471 同厂双品牌+logo 源文件 |
| 97 | cryptoink | F 白盒 OEM（站休眠，r34） | L10362 + 站不可达×3 |
| 98 | Larch Networks | F 白盒 ODM（直接竞对/伙伴，r34） | 41 号 §10 全证；同 Marvell 平台 |

## 6. 语料 verbatim 关键行（16 处）

- L214：「Please let me know if you will share a new software that supports the features **Taylan** discussed yesterday」；L302：「I will get **Taylan, as our CTO** to review your responses.」（Taylan=Angora CTO）
- L2191 Levent：「We have a new inquiry from a partner against **Maipu** switches. Can you pls let me know the following」；L2201：「is this about competing with **Maipu** brand?」
- L226 Levent：「…check how is the possibility of a stacking feature in **Marvell** versions only」；L324 Simon：「for https, we have another **Marvell** chip as a solution, but it takes too long to stock and manufacture.」
- L627：「One important thing is, for this series we are using a domestic chip **CENTEC** (website is https://www.centec.com/). Its a very strong and competitive solution supplier in China.」；L640 Levent：「Yep. We know Centec. Not very popular here. But let's check」
- L528 Levent：「I just wanted to check if **Saga** can supply SFPs too」
- L2368-2370 Levent：「That's great. We have a great sales funnel for 2025. **All based on Saga products. Developing all business on Saga solutions now**」
- L2698：「according to our manufacturing dept, we are now short of one material, that is RJ45 connector **https://www.ude-corp.com/** we are using this brand / we kinda need to wait in line for the materials from this supplier」（UDE=我方 RJ45 BOM 供应商）
- L3761：「https://www.rimaelektronik.com/」（Rima 唯一语料行=网址）
- L4015：「btw: this channel also supplier original **Moxa** products, maybe sometimes it will be useful」；L4019：「**Kyland and Moxa** sometimes come up in railways projects. I will check with partner」
- L4042 Levent：「That's a great option. **Trust and long term cooperation is 100% with Saga.** No problems.」
- L4290：「I will need a favor with the new order. Since these are our models both for **Angora and TronX**, can you be…」；L4314 Simon：「together with software, its your option to decide it to be **angora or tronx**」；L4471：「btw: we need your source file(AI/PS) for **TronX** logo」
- L5813 Levent：「**Connexite**-Amazon-Biz-Plan-DRAFT.pdf 384.1K Not Downloaded」（=文件共享消息，Connexite 客户计划稿）
- L6916：「Since we still did not get the order for the Turk Telekom project, **Karen at NEM Engineering** needs her GBIC」
- L7848 Levent：「No worries about the NETAS. They are looking for a **Moxa or Hirschmann** replacement」
- L8765：「If you buy SFP module from NEM Engineering, can you arrange paperwork so **Saga does not pay VAT** to…」
- L8805：「(**Dahua**) on the switch side to get better pricing on the camera side. So this is risky.」；L9275：「I understand **Dahua** got it」；L9277 Simon：「**Dahua** won it?」
- L10362：「1– It is another OEM brand called **cryptoink.com.tr**」
- L10381 Levent：「Yes, we position ourselves as a vendor to scale out. We are not an integrator. We position ourselves like **Maipu, H3C**」

## 7. 对平总表（宪法第十条自查）

| 目标 | 状态 | 落库位置 |
| --- | --- | --- |
| Larch 第二波（20+ 页/sitemap/全目录 4 线） | ✅ 全抓（4 项低优先缺：AC5Y 后续 chunk/Ironman 模块页/sonic-sai/sonic-hardening） | 41 号 §10 + 127 §2 |
| maipu/centec/h3c/moxa/marvell/dlink/belden/dahua/hikvision/kyland/ude/rima/netas/TT/nemengine/PNetworks | ✅ 首页或搜索代偿 | 127 §3 + 99-raw §2 |
| Sagatele 双域名 | ✅ 全抓 | 127 §4 + 99-raw §3 |
| Elips 10 源 | ✅ | 127 §5 + 99-raw §4 |
| cryptoink 直连 | ❌ 不可达×3（状态入库） | 99-raw §2.18 + 110 行 97 |
| hirschmann.com / mikrotik.com / TT /kurumsal | ❌ 异常×3（状态入库） | 99-raw §2.18 |
| 语料 16 处 verbatim | ✅ | 99-raw §6 |
| 110 行 90-98 | ✅ 三件套同步 | 110 |
| 111 变更 | 无（Rima 行 13 r33 已入；Connexite=非土客户仅存档 127 §6） | — |
| 126 号变更 | 无新增（Elips 实体名增量记 127 §5 交叉引用） | 127 §5 |
