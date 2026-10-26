# r35 深挖批原始抓取（2026-10-21）

范围：Sagatele 双站深挖 / D-Link DIS-110G / PNetworks(Pavo Group) 复活 / Keenetic TR / NEM Engine / Larch 缺项补全（Ironman 模块+Hardened SONiC+SKD/CKD）/ Levent×Connexite 穿透 / SERA / TronX 店页 / cryptoink 死档。宪法第十条：本文件=逐字底稿。

## 1. Sagatele（sagatelecom.com.cn / sagatele.com）

### 1.1 sagatele.com 精选 SKU（官网产品目录页）
- **STI-488XGGPM2B-2BT**：48 电口+2 SFP+ PoE+ BT（PoE Budget Total）
- **STC-424XGGPM-280W**：24 电口 PoE+ 280W 双 AC（规格带与我方 TT-2208 平台疑似同款）
- **STC-448XGGPM-4BT-740W**：1-4 口 90W BT，336Gbps，转发 <5µs
- **STC-448XGGMO**：全光 L3，13K 路由表，499.9Mpps，USB+Console
- **STC-448XGGM**：⚠️ 官网明写 **Marvell AC5** L3
- **STH-2C12XF12XE-HSI**：CENTEC 线
- **STH-2C24XF-HSI**：半宽 24×10G+2×100G，880Gbps，MLAG 双活，SDVoE
- **STH-8C48DX-HSI**：48×25G+8×100G
- **STH-32QC-HSI**：32×400G 25.6Tbps→可扩 64×400G；MPLS/VXLAN/EVPN+MACsec；2×1300W CRPS；MTBF≥90K
- **STI-21616GP**：16 口工业 PoE+ 非网管 240W，6KV，-40~+75℃ 户外（⚠️与 D-Link DIS-110G 正撞）

### 1.2 Prestera 全特性（官网特性页）
ERPS G.8032 <20ms / QinQ / 802.1X+RADIUS+TACACS+ / DAI / IPSG / DDoS 防护 / sFlow / **MQTT** / 双分区 / 光纤 bypass LC≤10ms / **DI-DO-RS485 Modbus** / 固件 **V7.5.x roadmap**。

### 1.3 CENTEC STH 线
全 L3 BGP/IS-IS，EVPN-VXLAN，MPLS，MLAG，stacking，10G-800G OSFP，DCB。
### 1.4 其他
Realtek=副线；定制=HW+FW(CLI/MIB)+UI 白牌「architecture changes not label changes」；Insights 2 篇 Coming soon（战略备货 / Marvell vs 白牌）；sagatelecom.com.cn ch1/3 与 sagatele.com 同源内容。

## 2. D-Link DIS-110G（press 2026-09-11 Taipei）
DIS-110G-05/-06P/-10/-10P = **非网管**工业 GbE：IP40 无风扇，-40~+75℃，6kV 全铜口，250m@10M 长距，PoE+ 30W（预算 240W/120W），**PD Alive 自动重启**，DIP Fast Ring，双 DC，802.3az。→ D-Link 工业入口=非网管低端（监控/楼宇/标牌）。

## 3. PNetworks = Pavo Group 品牌（pnetworks.com.tr 恢复可达）
- 产品线=**AI/ML + Cloud DC + Operator + Optics**
- CEO=**Bilal Yıldız**
- **2026-07-30 TWIF（土耳其主权基金）CFO&COO Dr. Mahmut Kayacık 拜访 Pavo CEO**（TWIF=Elips 客户→双线接触）
- 2026-08-27 Republikorp（印尼 Norman Joesoef）土-印尼防务
- social：IG/LI=pnetworkstr、X=@Pnetworks_；Become a Partner=pavo-group.com

## 4. Keenetic TR（keenetic.com.tr/en ch0/2）
消费/SMB 路由矩阵：Hero KN-1013 BE3600+10G SFP+ / TITAN SE KN-4210 BE7200 / **Stellar 6 KAP-650=IP65 PoE+ -40~+65 户外 AP 唯一 rugged** / Roamer 5G KN-5210 / DSL 系 / KN-4110/4010/2013/3611/2113/1812/3910/1012/3811 / KAP 530；KeeneticOS 云 demo=keenetic.demo.keenetic.pro；switch 线不在 ch0。

## 5. NEM Engine（nemengine.com）
NM-280-RJ45 SFP（10/5/2.5/1GbE MSA）+DAC+AOC（10G/40G/25G/100G）；站陈旧（2016 新闻仍在）。

## 6. Larch 补全

### 6.1 /network-switch-modules/（Ironman）
首个 10G Industry 4.0/IoT 芯片 **Marvell Ironman**（TSN/HSR）：ARMv8 双核 1.2GHz / DDR4 1G/2G / eMMC 256G / 可选全双工 **256b MACsec** / OOB 1GE 或 PCIe Gen3 / IEC 62439-3 HSR/PRP / TSN / 级联 **1K 模块** / 固件 RS232 CLI OOB、fast boot。
5 模块：**MO-P8Cx-4F(50G) / MO-16Cx-4F(72G) / MO-24Cx-6F(86G) / MO-48Cx-6F(110G) / MO-24Cx-28F(126G)**。
datasheet=wp-content/uploads/2026/06/ironman_module_full_datasheet.pdf（2026-06=新品）。

### 6.2 /sonic-sai/sonic-hardening/（正 URL；/sonic-hardening/=404）
流程=Q&A+security；whitepaper「LN SONiC.pdf」。支柱：High Availability（Fast Reboot/warm upgrade）/ Modular（BGP/VLAN/QoS 可加卸）/ Telemetry / Container / Cloud-Scale / **uCentral Cloud Mgmt（ZTP 开源）**。
功能表：VLAN/LACP/RPVST / OSPFv2v3+BGPv4v6+ECMP+GR / BGP-EVPN+VRF+NVGRE+VXLAN / Storm Control+L2L3L4 ACL+**TACACS/RADIUS** / QoS SP-WFQ-CIR-EIR-DSCP / gRPC+REST+ONIE+SONiC-to-SONiC upgrade / PoE af-at-60W / **工业可选：G.8032 ERPS + PTP 1588v1v2 + ITU-T G.8273**。

### 6.3 /hardware-development/hardware-production-localisation/（⭐SKD/CKD）
「we are fully prepared to help organize some domestic production of the network hardware」：
- Step1 Establishing Business：流程/物流/技支/品牌+本地产品
- **Step2 SKD：提供拆解状态设备含 PCBA；本地生产部分器件**
- **Step3 CKD：交付 PCB 做 SMT；交付全部元件或协助本地生产**
理由=本地供应链/生产与供应链安全/降本/国内产品。→ 对 Angora=「yerli」路径选项（Larch 设计+土本地 SKD/CKD 产线）。

## 7. Levent KILIÇ × CONNEXITE（穿透）
- LinkedIn（linkedin.com/in/kilic-levent）：**CONNEXITE, London**；Sabancı University；2K followers；公司网站同时挂 **connexite.co.uk + angoranetworks.com**；2026-08/09 连发 CONNEXITE OT/ICS 内容：「#DataDiode #OTGateway」「Forrester OT Security Wave Q3 2026」「the principle behind **ConnexONE**...regulatory frameworks, from Saudi Arabia's NCA OT controls to the UAE's NESA standards...We are Connexite, in the UK and serving the region directly」。
- **CONNEXITE LTD（Companies House 14770313）**：Private limited；**SIC 26200 Manufacture of computers and peripheral equipment**；284 Chase Road A Block 2nd Floor London N14 6HF；**股东 4×25%：MEHMET TAYLAN ESEN / MEHMET YASIN KORU / LEVENT KILIC / IBRAHIM BALCI**（⚠️ Mehmet Taylan Esen=我方 CTO）；2024-08-16 新董事 Donald Isufi；2024-07-10 报年报；成立 2022（RocketReach）；4 人。
- 团队：Levent Kiliç（Managing Partner/CEO）；**Mehmet Koru（Hardware&Software Engineer，Ankara；兼 mevaavionics.com）**；**Uras Acar（BD Manager，Brussels）**。
- become-partner 页：「Levent Kilic, **CEO, Connexite**」，Mon-Fri 8:00-19:00。
- → **Connexite Ltd=Angora 创始团队（GM Levent+CTO Taylan Esen 各 25%）英国实体（2022 起），SIC=计算机制造，业务=OT 安全（ConnexONE）+ 服务 UK+海湾（NCA/NESA 框架）**。

## 8. Larch 生态补遗（搜索所得）
- **SIDERA Intelligent Systems（UAE，sidera-is.com/about）**=「UAE-based technology brand of SIDERA Enterprises, created to develop and localize advanced networking and integrated AI infrastructure **in collaboration with Larch Networks**」（UAE 本地化品牌=与 Angora 模式同构）。
- **Dorado 联合发布（2026-10-12 EIN）**：OCP Global Summit 演示「Ethernet AI Fabric + Orchestration」；10× Larch Hardened SONiC switch + Dorado Cruz；**TeraLynx 10 架构**替代 InfiniBand（短缺/多年交期/出口管制）；doradosoftware.com 版本写 **booth #61**（Larch blog 版写 B31，两版并存待考）；Cruz=AI 网络 fabric+compute 集群+机架级编排。
- **Xsight Labs（xsightlabs.com 2025-03-21）**：Larch=其 **Hardened SONiC Center of Excellence**；Xsight 两线=**X-Series AI Ethernet switch + E-Series 800G SDN DPU**；Larch 提供 bare metal→full stack SAI+Hardened SONiC；「Larch manufactures over 50 diverse SKUs」。
- **at-a-glance 时间线**：1588 PTP 方案（Microsemi PLL）/ 12-24 口 DIN 工业 / IP Infusion 伙伴合同（Marvell 设备 NOS）/ **Falcon 换 Bobcat3（48×25+8×100，2Tbit）** / 全 NOS port（商用+SONiC SAI）/ **Miyagi 集成=远程管理 NOS**。
- **productizing SONiC（2025-11-02 文，2026-02-25 更新）**：「a major global brand approached us to deliver ToR switches with SONiC...green datacenters...now deployed in evaluation stages across regional offices」（未具名大品牌 ToR 盒式评估中）。
- **Network World（2026-10-21 当日）**：Dell'Oro：OLS 开放平台可跑 SONiC；「Representative vendors include Edgecore, Asterfusion, and Larch Networks」。
- **Embedded World 2026**：Larch 演示「Zero-Loss Redundancy with **PRP on Marvell Ironman**」（Eddie Preskovsky 转发）。
- Odoo 客户页：Larch=以色列公司，industrial switches/5G gateways/Marvell 方案（用 Odoo ERP）。
- **InnoVEX 2026**（COMPUTEX TAIPEI 2026-06-02~05）参展。

## 9. SERA
sera-network.com（news 2026-06-05）：COMPUTEX 2026 展示 **100G/400G/800G 高速交换平台**（AI server clusters/HPC/hyperscale DC，GPU 集群数据交换）=Larch 2026-09 新增伙伴。

## 10. TronX 店页
tronx.com.tr/shop/ 在线：地址 **Mustafa Kemal Mah. 2124 Cad. No:14/1 Çankaya/ANKARA**；**+90 312 309 19 54**；info@tronx.com.tr；「2008 yılında tıbbi ve hastane malzemeleri...başlayan TRONX BİLİŞİM VE SAĞLIK TEKNOLOJİLERİ LTD...günümüzde bilişim ve sağlık teknolojileri...üreten...lider」（2008 医疗起家→今生产+服务 IT 与健康科技）。法人/股东公开搜索未出（MERSİS 不可公开检索）。

## 11. 死档
- cryptoink 实体：全网搜索 0 土耳其实体命中（仅 CIK 币/CryptoINK LLC/e-ink 项目/cryptoink.online 噪声）→ 坐实仅语料 L10362 痕迹。
- Larch /sonic-hardening/=404（正 URL=/sonic-sai/sonic-hardening/）。
