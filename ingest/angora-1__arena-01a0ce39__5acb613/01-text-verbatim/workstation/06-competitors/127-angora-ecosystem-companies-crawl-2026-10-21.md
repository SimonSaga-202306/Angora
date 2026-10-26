# 127 · Angora 生态公司全景爬取档案（2026-10-21，r34）

> 任务=用户指令「语料出现的所有公司 → 网站全部爬取入库 + 与 Angora 的合作关系/结构多角度深挖 + 尤其 Larch Networks」。
> verbatim 全量=`99-raw/r34-ecosystem-crawl-2026-10-21.md`；Larch 深度=`41-larch-angora-partnership-timeline-2026-10-21.md` §10；竞品入表=110 行 90-98。

## 1. ⭐ 生态结构总图（本轮最大产出）

```
芯片层        Marvell Prestera(98DX25xx/98DX3510/98DX22xS) + TeraLynx(7/10) + Ironman
              CENTEC(L3 聚合/核心/DC，10G-800G) + Realtek(Saga 辅助平台) + NVIDIA Spectrum X2(Larch DC)
    │                │                              │
工厂层      Sagatele(深圳)⬅我方ODM            Larch Networks(以色列)
              40+ SKU 三产品线                   白盒品牌+ROS/SONiC/OpenLAN 软件方
              STI 工业/STC 商用(Prestera AC系)/    4 产品族(Aldrin/Falcon/TeraLynx/X2+
              STH 核心(CENTEC L3)                 campus AC3/AC5/AC5X/AC5Y+工业+PB)
              战略芯片库存·OEM/ODM/SKD/CKD         客户=国防/航天24家(Angora第4)
    │                │                              │
品牌层(土)  Angora(我方) ━━同厂ODM━━━━━━━━ TronX(姊妹品牌，L4290/4314/4471)
              PNetworks=唯一 yerli 自研(2021 Teknopark)
              Elips=竞标+资本伙伴(非品牌)   渠道:Kyland+Moxa 铁路渠道(Netaş 替换线)
客户层      TT(土耳其电信,TT项目线) / Netaş(买过3台样品,项目死) / Rima(安全集成,111行13)
              Connexite(英国,Amazon Business,L5813,非土仅存档)
供应链      UDE(TPEX:3689,RJ45 连接器 BOM,L2698) / NEM Engineering(Karen,SFP/GBIC,L6916/L8765)
              cryptoink(88台死单后 OEM 线,站休眠,L10362)
```

**三层关系结构（各角度）**：
| 角度 | 结构 | 证据锚 |
| --- | --- | --- |
| 供货 | 芯片→Sagatele→Angora/TronX 品牌 | L2368「All based on Saga products」；sagatele.com「Marvell Prestera AC5 Lite/AC5/AC5+」 |
| 同平台竞争 | Larch 与 Angora 共用 Marvell AC 平台（Larch=上游设计+软件，Angora=品牌+土耳其渠道）；Sagatele 公开目录=我方 TT 系列平台 | 41 号 §10 芯片号对照表 |
| 资本/竞标 | Elips=「bidding partner and the money behind this deal」（2026-07-06）；TronX=「for his sales only…backoffice」品牌/渠道层 | 126 号 §2-3 |
| 替换竞争 | Netaş 找 Moxa/Hirschmann 替换（L7848）；Dahua 捆绑策略（L8805）且赢过标（L9275）；Maipu=partner 对标的竞标对手（L2191） | 110 行 90-93/95 |
| 定位基准 | Angora 自述=「vendor 不是 integrator，像 Maipu、H3C」（L10381） | 110 行 94-95 |
| 供应链风险 | UDE RJ45 断料需排队（L2698）；NEM SFP 需 Saga 免税单证（L8765） | 99-raw §6 |

## 2. ⭐ Larch Networks 深挖（最高优先；全证=41 号 §10）

**公司**=以色列白盒网络产品开发商（2009 立/2018 BC3 SONiC+PB 线/2020 Falcon/2025 Ironman+FastBoot；r32 既有）；**2025-11-02 加入 SONiC Foundation**（r34 新证）。
**contacts**=11 Amal str, Rosh-Ha'ayin 4809239, Israel；+972 3-901-6117/6118；销售 +972 55-966-1282；info@larch-networks.com。
**team**=Alexander Cheskis CEO / Inna Cheskis Co-Founder / Oleksandr Kaganovskyi VP R&D / Eddie Preskovsky COO / Oleksandr Grybenko BD Executive（全乌克兰名→基辅研发主体；3 R&D 中心/90% 工程师/收入增长 50%）+ **新 BD 联系人 Irina Murzina**（OCP 2026 预约页，hubspot imurzina）。
**client 墙 24**（国防/航天权重极高）=adva / aitech / amphenol / **Angora(第 4)** / beeper / cobham / compas / crsi / ekinops / elbit / frank / gilat / harmonic / hfbr / iaia / kazdream / microsens / mrv / novelsat / qntm / quantex / sartura / techaya / xsight。
**partner 墙 8**=Dorado（doradosoftware.com，Cruz 编排，**负责 Larch switch 销售/服务/支持**）/ **Marvell**（「enabling Marvell to offer their customers full-featured routing software」=核心 franchise）/ AVNET Silica（2025-09 分销）/ SERA（2026-09 新，industrial/DC/private 网络设备商）/ Network Critical（网可视性）/ PANTHEON.tech（2025-12）/ Teledyne LeCroy Xena（2026-09，T 比特测试）/ IP Infusion（分句未完）。
**blog 26 篇时间线**=2024 FYUZ/LeCroy SAI 测试平台/electronica/MWC BC → 2025 Xsight 合作/case×3/工业 3 页/PB 页/FYUZ/⭐SONiC Foundation(11-02)/PANTHEON(11-18) → 2026 MWC BC/**BFD+ 硬件加速**(02-05)/productizing SONiC(02-25)/Embedded World/SONiC on ARM edge(03-17)/INNOVEX@COMPUTEX(04-14)/**Hardened SONiC on Ironman**(05-19)/AVNET FAE(07-21)/autonomous mining(08-11)/electronica India(09-15)/航空器内网鉴权(10-06)/LeCroy 800G-validated@OCP(10-07)/**OCP Dorado B31**(10-09/10)/Amphenol TSN A&D Summit(10-20 最新)。
**OCP 2026 演示**=Marvell TeraLynx 10 spine-leaf + Hardened SONiC + NVIDIA ConnectX-7 GPU + Dorado Cruz；叙事=以太网替代 InfiniBand（供给/交期/出口许可）「democratize AI infrastructure」。

**⭐ 产品族 ↔ 芯片号对照表（同芯片铁证，语料「AC3/AC5」来源解码）**：
| Larch 平台 | Marvell 芯片号 | 定位 | 对我方含义 |
| --- | --- | --- | --- |
| AC3（campus L2） | **98DX223S** | 8/24/48×1G(+2.5G 版)+4×10G，RPS 2PSU | 与我方 AC3 命名同源（⚠️ 校园 223S≠工业 226S） |
| AC3（industrial） | **98DX226S** | LN-23xx-I，DIN/rack，PoE/PoE++ | 同 Marvell 料号 |
| AC5/AC5+ | **98DX2538** | 24/48×1G+4×10G，PoE+400/740W，HSP/HSF | **=我方 TT-2208「AC5」同芯片** |
| AC5lite | **98DX2518** | 12/24×1G+2×10G，PoE180W | 同系 |
| AC5X | **98DX3510 / 98DX3510(M) MACsec** | 2.5G 接入+6×25G uplink，PoE++1440/1480W，HSP | 上一代平台（25G 上联） |
| AC5Y | （L2 接入，芯片未标） | 8/24×1G+4×10G | 入门 |
| Aldrin1/2/3 | 98DX8382/98DX8548/98DX7332 | DC 10G/25G 主流 | 参考 |
| Falcon | 98CX8514/8522/8580（ARM/Intel） | DC 25/100/400G | 参考 |
| Teralynx 7/10 | IVM77700 / 98TX9180 | 32×400 / **64×800** | AI fabric 线 |
| X2（NVIDIA） | — | 32×400 / 16×800 SONiC | 参考 |
| PB | — | Orama X25N/X400 1RU 网可视 | 参考 |
通用 NOS=**ROS+SONiC+OpenLAN**；DC 通用=dual hot-swap PSU/8GB DDR4/32GB eMMC/hot fans；campus=2GB DDR+1GB flash/USB+OOB+console；工业=8 台 SFP stacking。

## 3. 生态公司档案（18 站，摘要；全 verbatim=99-raw §2）

| 公司 | 站 | 一句话定位 | 与 Angora 关系/角度 | 关键情报 |
| --- | --- | --- | --- | --- |
| Marvell | marvell.com | AI silicon 龙头（2026「Marvell is how AI scales」） | 我方+Larch+Saga 共同芯片源；OEM 层（Networking & Security）含我方 AC 系 | 3.2T retimer+1.6T AEC DSP（OCP 2026）；OCP DC 安全标准组；TeraLynx10=Larch AI fabric 演示芯片 |
| CENTEC | centec.com | 2005 苏州，交换芯片+SDN/白盒 | 我方 L3 线芯片（L627 自述）；Levent「not very popular here」（土市场认知壁垒） | silicon/software/solutions 三页 |
| Sagatele/Saga | sagatelecom.com.cn + sagatele.com | 深圳 ODM 工厂（40+ SKU，STI/STC/STH） | **⭐我方 ODM 工厂（100% 证据 §4）**；公开站=我方产品线公开目录 | Prestera AC5 系+CENTEC L3（10G-800G）+Realtek；战略芯片库存；WhatsApp +86 15237149683 |
| Maipu 迈普 | maipu.com | 北京运营商级全线（路由/交换/WLAN/GPON/防火墙/光模块/HCI） | L2191 partner 对标竞标对手；L10381 定位基准 | 2026 中东/亚洲展会密集（LEAP 沙特/VN/东京/新加坡）；AI Compute Fabric+RoCEv2 |
| H3C 新华三 | h3c.com/en | 中国全栈数字+AI 巨头 | L10381 定位基准 | Gartner 虚拟化 MQ Visionary；S12500X-AF DC 交换 |
| Moxa | moxa.com | 全球工业自动联网龙头 | 铁路渠道共现（L4015/4019）；Netaş 替换目标（L7848） | RKS-G4030-PL（30 口模块，PoE++720W）；EcoVadis 金 2026 |
| Hirschmann (Belden) | belden.com（hirschmann.com 不可达） | Belden 工业品牌（OT-IT-cloud） | Netaş 替换目标（L7848）；铁路细分 | Belden=5G-ACIA/EtherCAT/SPE/TIA 成员；行业含 Mass Transit |
| D-Link | dlink.com | 台系全线（消费/SMB/企业/工业） | 语料 26 命中（$135 伙伴价锚=其 DIS300G 线，r33 既有） | **⭐2026-09-11 发布 DIS-110G 工业交换机组合=进入工业线**（撞我方工业线） |
| Dahua 大华 | dahuatech.com | 中国安防+数通（交换机/光模块） | **赢过标（L9275「Dahua won it?」）**；捆绑策略（L8805：用 switch 压 camera 价） | 数通产品类在册；CIIF 2026 上海；子品牌×4 |
| Hikvision 海康 | hikvision.com/en | 全球 AIoT（110 行 19 打包行已含） | 打包行竞对（L8805 同场景） | 观澜大模型 2026 主线；Guanlan Encoding 存储-30~50% |
| Kyland 东土 | kyland.com | 中国铁路工业国家队（300353，110 行 89） | 铁路渠道伙伴+竞对（r33 结案） | 官网老站；Aquam 系列 campaign 互证 |
| Netaş | netas.com.tr | 土耳其防务/电信 ICT（110 行 2） | 买过 3 台样品（项目死）；找 Moxa/Hirschmann 替换=机会 | **EYDEP A 级**（防务能力认证）；R&D 250 行业第 3；伊斯坦布尔机场 ICT 承建+5 年运营；ZTE 服务器本土化；Microsoft LSP（AZ/KZ）；2026H1 增收增利 |
| Türk Telekom | turktelekom.com.tr | 土耳其电信（终端客户/甲方） | TT 项目线（既有） | 2026 消费者面=iPhone 18 预约/TurboBox 5G/家宽 640TL 起 |
| UDE | ude-corp.com | 台系以太网连接器（TPEX:3689） | **我方 RJ45 BOM 供应商**（L2698 断料排队） | 月度营收公告（上市）；QSFP-DD-800 自研 |
| NEM Engineering | nemengine.com | 深圳 SFP/GBIC 供应商 | Karen 在任；SFP 供货（L6916）+VAT 单证流（L8765） | 4009664008；NM-280-RJ45 |
| Rima Elektronik | rimaelektronik.com | 土耳其安全/IT 集成商（111 行 13） | 客户（安全集成采购线） | 自研 Digifort AI VMS（人脸识别宣称 99.87%）；Axis 分销；品牌墙=D-Link/Dahua/Hikvision/Cisco 等 13 家 |
| PNetworks | （搜索：SavunmaTR/AA 2021-04-02） | 土耳其唯一 yerli 自研 switch | yerli 唯一参照（110 行 1） | Teknopark İstanbul 发布会；IEEE 1588v2 PTP+SyncE+L3 静态；Pendik 市合作备忘录 |
| Keenetic Türkiye | blog.keenetic.com.tr | 俄系品牌土耳其（110 行 9） | 市场旁证 | **2026-05-14 开始卖 switch**（新进入者） |
| Connexite | （搜索：ZoomInfo） | 英国网络安全/SD-WAN 软件（11-50 人） | **我方客户**（Amazon Business，L5813 Plan-DRAFT.pdf；非土仅存档） | 安全数据传输/SD-WAN（⚠️ r19：二极管类产品细节不入展示，仅记档） |
| Elips Elektronik | elips.com（搜索 10 源） | 土耳其企业 IT 集成（1988/1990） | **⭐竞标+资本伙伴（126 号；r33 结案，r34 实体坐实 §5）** | 法定实体名+4 公司 120 人+LSP 型全服务 |
| cryptoink | cryptoink.com.tr（不可达×3） | 白盒 OEM（88 台死单后线） | 死单关联线（L10362） | 站休眠=状态本身入库 |
| NetworkMarket | networkmarket.online（r31 死站结案） | 渠道（Ticimax 64180） | 渠道参照 | 2025-03 价目=价格锚（既有） |
| TronX | tronx.com.tr | ⭐Angora 姊妹品牌（110 行 96） | 同厂双品牌（§1 三层表） | ELS-L2PI-8GP-2F=TT 项目手册品牌（r33） |

## 4. ⭐⭐ Sagatele（Saga Telecom）= 我方 ODM 工厂（100% 证据链）

1. **语料四证**：L528「check if Saga can supply SFPs too」/ L2368「sales funnel for 2025. **All based on Saga products**」/ L4042「**Trust and long term cooperation is 100% with Saga**」/ L8765「so **Saga does not pay VAT**」（进口/VAT 主体）
2. **官网互证**：sagatele.com 能力页=「**Marvell Prestera AC5 Lite · AC5 · AC5+ — L2+ Managed Switching**」← 语料「AC5/AC3」平台命名同源；STC 商用线=「Marvell Prestera-based…PoE++ 90W/口」=我方商用系列规格带
3. **产品线**=STI 工业（STI-288DGGPM/STI-4240XGGM，DI/DO/RS485 原生）+ STC 商用（STC-448XGGPM-4BT-740W 等）+ STH 核心（STH-32QC-HSI 32×400G 25.6Tbps / STH-2C24XF-HSI 半宽 MLAG）
4. **供应链角色**=Marvell/CENTEC 战略 buffer stock（EOL 提前通知）+ SFP 供货（与 NEM Engineering 并行的 SFP 线）+ 深度固件/管理 UI 定制
5. **边界**=不做 EN50155（→铁路线走 Kyland 渠道）/不做 IP67/不做云管/不做消费；联系=WhatsApp +86 15237149683 / e.sagatelecom@gmail.com
6. **对我方含义**=① 我方公开产品目录=其公开站（谈判时注意公开价/规格口径一致）② 其「position against Taiwanese brands」定位=可借势打 D-Link/TP-Link ③ UDE 断料+芯片 buffer=交付风险双点（RJ45 排队 vs Saga 库存）

## 5. ⭐ Elips Elektronik（r34 法定实体坐实；详情=99-raw §4）

- **法定实体=ELİPS ELEKTRONİK SANAYİ VE TİCARET LİMİTED ŞİRKETİ**（registry 268901，成立 **1990-10-03**，实缴 100,000 TRY，#631108 数据处理/托管，非清算）→ r33「1988/1990」=品牌起步/法定设立双解
- 官网 **elips.com**（Zincirlikuyu，Mithat Ulu Ünlü Sok. 1/C，0212 337 02 00 / 288 37 17，elips@elips.com）
- 规模=LinkedIn 口径 **自有 1200m² 楼+4 家公司+120 人**；EMIS 24 人（2026）/ZoomInfo 85/RocketReach 44；营收 **$5.8M**（RocketReach）；2024 净销售 +20.05%
- 历史=1988 Şişli 80m² 3 人起步；**2009 Normdata 合作**（HPE 授权服务点）；Novartis Sandoz helpdesk 20 年（20 人）；Bodrum+Antalya 办公室
- 服务=Microsoft 方案/7x24/SLA/IT outsource/结构化布线/项目管理；**RevenueBase 土耳其 reseller 第 5（2026-09）**
- 与 126 号对平：r33 三层结构不变（①竞标+资本=Elips ②品牌/渠道=TronX ③执行轮动）；本轮仅实体名+规模坐实

## 6. 客户/供应商线（非竞品，存档）

- **Connexite**（UK，Amazon Business 客户，L5813）=非土，仅存档（r21 规则）
- **NEM Engineering**（深圳 SFP/GBIC，Karen）=SFP 供货+VAT 单证流（L6916/L8765）
- **UDE**（TPEX:3689，RJ45 连接器）=BOM 供应商，2025-01 断料排队（L2698）
- **cryptoink**（88 台死单后 OEM 线，L10362）=站休眠
- **Rima**（土安全集成，Digifort 自研）=111 行 13（r33 结案）

## 7. 边界与不可达（状态入库）

cryptoink.com.tr 不可达×3 / hirschmann.com×2（Belden 根页代偿）/ mikrotik.com 维护×2 / TT /tr/kurumsal 404 / Larch /hardware-production-localisation/ 404 / belden.com/en-hr 500（根页代偿）/ Larch 低优先缺项=AC5Y 后续 chunk、Ironman 模块页、sonic-sai、sonic-hardening（URL 已知，可后补）/ proxy OSS InvalidAccessKeyId 一次（直连重试成功）。

## 8. 对平表（宪法第十条自查=PASS）

语料 26 项名称=全部定性（人 2：Taylan CTO/Karen NEM；公司 24，全部有落库位置）；域 7 个=6 处理+drive.google.com（Larch datasheet 外链，非公司）；抓取 24 目标=18 成功+6 异常（状态入库）；110 行 90-98 新增=9 行三件套；111/126 无结构变更（增量交叉引用）；16 处语料 verbatim 全入 99-raw §6。

## 9. r35 深挖增量（2026-10-21）

### 9.1 Sagatele 完整目录（双站同源，逐字底稿=99-raw r35 §1）
SKU 12+：STI-488XGGPM2B-2BT / STC-424XGGPM-280W（⚠️≈我方 TT-2208 平台带）/ STC-448XGGPM-4BT-740W（1-4 口 90W，336Gbps，<5µs）/ STC-448XGGMO（全光 L3 13K 路由 499.9Mpps USB+Console）/ **STC-448XGGM=官网明写 Marvell AC5** / STH-2C12XF12XE-HSI / STH-2C24XF-HSI（半宽 24×10G+2×100G 880Gbps MLAG 双活 SDVoE）/ STH-8C48DX-HSI（48×25G+8×100G）/ STH-32QC-HSI（32×400G→64×400G，MPLS/VXLAN/EVPN+MACsec，2×1300W CRPS，MTBF≥90K）/ STI-21616GP（户外 16 口 PoE+ 非网管 6KV -40~+75，⚠️撞 D-Link DIS-110G）。
特性全集：ERPS G.8032<20ms / QinQ / 802.1X+RADIUS+TACACS+ / DAI / IPSG / DDoS / sFlow / MQTT / 双分区 / 光纤 bypass LC≤10ms / DI-DO-RS485 Modbus / **固件 V7.5.x roadmap**。STH 线=CENTEC（BGP/IS-IS/EVPN-VXLAN/MPLS/MLAG/stacking/800G OSFP/DCB）；Realtek=副线；白牌=HW+FW(CLI/MIB)+UI「architecture changes not label changes」；Insights 2 篇 Coming soon。
**判定：Sagatele 公开目录=我方 TT 线同平台带（Prestera+CENTEC 双芯策略与我方一致），V7.5.x=其固件版本线。**

### 9.2 PNetworks=**Pavo Group** 品牌（站恢复，2026 全面升级）
产品线=AI/ML + Cloud DC + Operator + Optics；CEO=Bilal Yıldız；**2026-07-30 土耳其主权基金 TWIF CFO&COO Dr. Mahmut Kayacık 会 Pavo CEO**（TWIF=Elips 客户→Elips 与 PNetworks 双线接触主权基金）；2026-08-27 Republikorp（印尼）防务；IG/LI=pnetworkstr、X=@Pnetworks_；pavo-group.com=伙伴入口。
**判定：PNetworks 已从 yerli switch 单点升级为集团化（Pavo）+主权基金背书+AI/DC 转型。**

### 9.3 ⭐ Levent KILIÇ×CONNEXITE 穿透（新实体发现）
**CONNEXITE LTD（Companies House 14770313，London N14 6HF，SIC 26200 计算机制造，2022 成立，4 人）股东 4×25%：MEHMET TAYLAN ESEN（=我方 CTO）/ MEHMET YASIN KORU / LEVENT KILIC（=我方 GM）/ IBRAHIM BALCI**；2024-08-16 董事 Donald Isufi；团队=Levent（MP/CEO）+Mehmet Koru（HW/SW 工程师，Ankara，兼 MEVA Avionics）+Uras Acar（BD，Brussels）；业务=OT 安全产品 **ConnexONE**+服务 UK+海湾（Saudi NCA/UAE NESA 框架）；Levent LinkedIn 双挂 connexite.co.uk+angoranetworks.com，2026-08/09 连发 OT/ICS 安全内容。
**判定：Connexite=Angora 创始团队英国实体（GM+CTO 各持 25%），非外部竞对；语料 Connexite-Amazon-Biz-Plan-DRAFT.pdf=该英国实体商业计划。**

### 9.4 Larch 补全（Ironman/Hardened/SKD-CKD/生态）
- **Ironman 模块线**（/network-switch-modules/）：Marvell Ironman=首个 10G Industry 4.0/IoT TSN/HSR 芯片；ARMv8 双核 1.2GHz/DDR4/eMMC 256G/可选 256b MACsec/OOB 1GE 或 PCIe Gen3/HSR-PRP/TSN/级联 1K；5 型号 MO-P8Cx-4F(50G)/MO-16Cx-4F(72G)/MO-24Cx-6F(86G)/MO-48Cx-6F(110G)/MO-24Cx-28F(126G)；datasheet 2026-06=新品；Embedded World 2026 演示 PRP on Ironman。
- **Hardened SONiC**（/sonic-sai/sonic-hardening/）：HA（Fast Reboot/warm）+Modular+Telemetry+Container+uCentral ZTP+工业可选 **G.8032 ERPS+PTP 1588+G.8273**；whitepaper=LN SONiC.pdf。
- **⭐SKD/CKD 本地化生产计划**（/hardware-development/hardware-production-localisation/）：Step1 建业务（品牌/物流/技支）→**Step2 SKD 拆解设备含 PCBA**→**Step3 CKD 交付 PCB 做 SMT+全部元件**；明言支持 local supply chain/safety/cost→ **Larch 官方「yerli 化」路径=设计+SKD/CKD 授权**。
- 生态：SIDERA Intelligent Systems（UAE 本地化品牌=与 Larch 共建）/ Xsight Labs CoE（X-Series AI switch+E-Series 800G DPU）/ Miyagi（远程管理 NOS）/ IP Infusion（历史合同）/ Falcon 换 Bobcat3 48×25+8×100 2T / PTP=Microsemi PLL / productizing SONiC=未具名大品牌 ToR 评估中 / Network World 2026-10-21 点名 OLS 代表厂商 / Odoo ERP 客户 / InnoVEX 2026 台北。

### 9.5 其他线
- **D-Link DIS-110G**（2026-09-11）：-05/-06P/-10/-10P 非网管工业 GbE（IP40/-40~+75/6kV/250m@10M/PoE+ 30W 240W 与 120W 预算/PD Alive/DIP Fast Ring/双 DC/802.3az）→ 低端工业入口，与 Sagatele STI-21616GP 同带。
- **Keenetic TR**：消费/SMB 路由矩阵（KN-1013/4210/5210/4110/4010/2013/3611/2113/1812/3910/1012/3811）+Stellar 6 KAP-650（IP65 PoE+ -40~+65 户外 AP 唯一 rugged）+KAP 530；KeeneticOS 云 demo。
- **NEM Engine**：NM-280-RJ45 SFP（10/5/2.5/1GbE MSA）+DAC+AOC 四档（10G/40G/25G/100G）；站陈旧。
- **SERA**（sera-network.com）：100/400/800G DC 交换平台（COMPUTEX 2026）=Larch 2026-09 新伙伴。
- **TronX**：店页在线（Çankaya/Ankara 2124 Cad. 14/1，+90 312 309 19 54，info@）；「2008 医疗起家→今生产+服务 IT/健康」自述；法人股东公开不可得。
- **cryptoink**：实体全网 0 命中（死档坐实）。

### 9.6 r35 对平自查
本轮抓取 13 项（Sagatele 2 站/D-Link/PNetworks/Keenetic/NEM/Larch×3/Connexite 穿透/SERA+Larch 生态搜索/TronX/cryptoink）=全部落库（99-raw r35 + 本节 + 110 行 1/9/90 更新 + 41 §10 补 + 123 补）。PASS。
