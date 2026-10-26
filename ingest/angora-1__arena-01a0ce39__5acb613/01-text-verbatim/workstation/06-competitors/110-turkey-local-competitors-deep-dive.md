# 土耳其本土竞争者深度档案（2026-10-08，第 14 轮建档；第 15 轮更新）

> 任务来源：用户第 14 轮指令「继续深挖 angora 的土耳其本土竞争者 Pnetworks 就是一个典型 / 多挖 深挖 / 一定要头脑风暴来搞 拓展思路 深度挖掘 全部落库 / 并列成一个 csv 和 xlsx 和 MD 一共是 3 个文件 都搞一下 / **后续挖的也录入 这个算是一个规则**」
> 第 15 轮更新（2026-10-08，用户「都搞了」）：执行第 14 轮三条遗留线索——PNetworks 官网 datasheets 逐份解析（10/31 成功 + 2 死链）、rehbersanayi.com EKAP 中标归档首次扫描、ensun Top 14 补全。详见 §9 与 `99-raw/pnetworks-datasheets-extract-2026-10-08.md`。
> 第 16 轮更新（2026-10-08，用户「都搞了 需你邮箱这个啥意思？」）：执行第 15 轮三条低优线索——datasheets 全量收尾（累计 26/27 唯一项）、rehbersanayi 全量扫描穷举收口（60/547 + 三路旁证 0 命中，更正第 15 轮 ≈120 条误估）、TTK 招标原文核实（定制假设降级 + 同品牌光模块条款发现）。⭐ 两大新发现：PNetworks = Edgecore 硬件底座（Broadcom+SONiC）+ 白牌 ODM 贴牌（面板照片实锤）；n11 零售 14-15 万 TL。详见 §10 与 `99-raw/pnetworks-round16-fullscan-2026-10-08.md`。
> 第 23 轮更新（2026-10-21，用户「把你之前做的再过一次 看看有没有啥新发现 新的信息 / 继续挖掘angora的相关信息」）：全量复核 + 13 天新窗口挖掘——rehbersanayi 新 60 条窗口（10-09→10-19）110 在册公司 6 起新中标（Pantech 132.5M/Fonet 137.7M/Artı ve Artı 9M 含网络设备等）、Angora/PN/Ewind/Longline 0 命中；PNetworks n11 锚点不变 + 新增 PN8GE2CG 8 口 + Trendyol 渠道价差（78,307 vs 156,612）；⭐Ewind 2026 新品 EW-S3936GM（Microchip/Vitesse 芯片）+ 工业云管理系列；Keenetic 零售落地（1.6-3.3K TL/30 卖家）；Longline hepsiburada 扩至 116 产品 + 新 M3XF4GE24 工业 L3 PoE+ 137,900 TL；Angora 官网停更 32 个月；待核项 2 解决（Opax=Nevşehir 土耳其主体 / Fiberix=ISP 确认排除）+ 1 部分解决（Duzgun↔Toptansarf）。详见 §13 与 `99-raw/r23-recheck-mining-2026-10-21.md`。
> 第 24 轮更新（2026-10-21，用户「你把Ewind网站爬下来入库吧 必要时开workflow去爬」）：⭐ **Ewind 官网全量爬取入库** = 新建 `112-ewind-website-mirror-2026-10-21.md`（ewindnet.com 直连 3 次 OSS 故障 → site: 索引 workflow 6 轮检索，规格表级快照）：公司面（投资 $50.67M / 厂 5000㎡ / 500+ 员工 / 20 SMT / National High-tech / 100+ 国出口 / 四川省公安厅案例 / CPSE 2025）+ 五大产品线 90+ SKU（商用受管 13 / 2.5G-10G 7 / 非受管 12 / ⭐Cloud-AI PoE 6 / 工业 15+ / OEM 定制 / 光猫 9 / 注入分离 16）+ 2026 产品页时间线（官网持续月级更新）；关键情报：OEM 定制拨码 E/V/D = **300m 长距 + 口隔离 + AI-PoE Watchdog**（与 Longline 同卖点集）/ S3936GM = Microchip (Vitesse) 芯片 / 10G Managed PoE 类目 17 SKU / W- 前缀新系列 / OEM 交付 4-6 周。详见 §14 与 112 号档案。
> 第 25 轮更新（2026-10-21，用户「如果爬完了就去爬他们的宣传网站 反正只要关于EWIND的信息都要爬 都入库了」）：⭐ **Ewind 宣传面/全渠道入库** = 新建 `113-ewind-promo-full-presence-2026-10-21.md`：10 轮 site: 检索覆盖 **12 语言站 + Alibaba 宣传店铺（270+ SKU）+ Facebook×3 + LinkedIn + ZoomInfo + 展会全录**；⭐ 土耳其 = 官方 **Malatya 落地案例** + **1Net Telekom**（BTK 持牌运营商）总经理推广 Ewind；⭐ Alibaba 首批价格锚（$21.55-$115 阶梯）+ 认证/排名/主要市场；r24 缺口全部补齐（14 口/BT 注入器/20 口 300W/16 口 AI-PoE…）+ WiFi 13 款全录（含 WiFi7 Qualcomm/Broadcom 芯片）；详见 §15 与 113 号档案。
> 第 26 轮更新（2026-10-21，用户「EWIND信息都爬完了？」）：**收尾闭合** = 直连第 4 次仍 OSS 故障；3 轮收尾检索闭合两大类目（10G Managed PoE 17 SKU ≈ 全量 / Unmanaged 15 款全量）+ 新增 7+ 款（S53952QM 1760Gbps / S57948QM 5GE 线 / S5954GM-AP(RTL) = **Realtek 芯片版本** / PIS5736GM-8GF-AP-BT(VTS) 36 口 800W 工业）；⭐ **最终结论 = Ewind 信息层面 ≈95%+ 已爬完**，5 项硬边界已声明（详见 113 号档案 §11）；110 行 15 备注同步。
> 三件套：本 MD（叙事深挖）+ `110-turkey-local-competitors.csv`（结构化主清单 19 行，utf-8-sig）+ `110-turkey-local-competitors.xlsx`（Excel 版 + 图例页）。
> **规则 5（本轮起生效）**：后续任何轮次挖到的新竞争者或既有竞争者的新情报，必须**同步录入三件套**（CSV/XLSX 增改行 + 更新"核验日期"；MD 对应条目增改），只更新其中一份 = 违规。已写入 `workstation/README.md` §0。

---

## 一、方法与头脑风暴地图（"拓展思路"怎么做的）

没有只盯"PNetworks 的同类"，而是把"谁可能与 Angora 竞争"拆成 **7 层**逐层扫：

| 层 | 问题 | 结果 |
|---|---|---|
| A 本土 switch OEM | 土耳其还有谁自己做交换机？ | PNetworks（典型）+ 仅 2 家小型集成商（Trustnet 等）——本土 switch 制造是**稀薄市场**（ensun.io 2026 "Top 14" 里真正做硬件的本土公司 ≈ 5 家，且多数是线缆/机架/集成） |
| B 防务 IT / 运营商 | "yerli" 叙事的大玩家 | Netaş（100% 本土战略通信 + ZTE 本地化）、Aselsan（2027 本土手机）、TT/Argela（Netsia SEBA 150 万户） |
| C 本土基础设施 | 供应链侧 | UPCOM(TR) 光纤/机架/吹缆机（"all made in Turkey"） |
| D 安全 niche | Angora 的数据二极管/ModBUS 线对标谁？ | **DataFlowX（DataDiodeX + Tech Data 全球分销）**、Rovenma（Kindi）、MAY Siber（本土 NAC）——全在 Angora 同属的 TGSK 集群里 |
| E 接入线 | GPON/AP/新品类进入者 | V-SOL（**更正：中国品牌**，经 Poyraz 卖）、Keenetic Türkiye（JV，2026-06 进 switch）、本土 AP 制造商 = 空白 |
| F 中国/全球品牌 | 标单里的实际对手 + 我方直接竞对 | **Ewind（深圳，= Angora 头号供应商）**、IZIFI/Poetech（东莞）、Mikrotik（基准）、TP-Link/HPE/Ubiquiti/Hikvision |
| G 渠道 | 谁的分销网 | L&N（PNetworks 公共部门通道）、ARENA（Keenetic）、Prolink（HPE/Aruba VAD）、Netsite（Cisco）、Poyraz/ELCORE（我方候选） |

搜索策略：TR/EN 双语关键词（"yerli switch" / "ilk yerli" / "yerli data diode" / "yerli AP" / "ihale kazandı"）+ B2B 目录（ensun.io）+ 官网直抓（pnetworks.com.tr 含 31 项 datasheets 清单、pavo-group.com、netas.com.tr、upcom.com.tr）+ 新闻（AA/SavunmaTR/defenceturk/bthaber/gunes/milliyet）+ 零售货架（atommarket/sinerji/fiberden）交叉。

## 二、典型深挖：PNetworks（PAVO Group）

**集团真相（此前档案只写了"PNetworks"，本轮补齐）**
- PAVO Group = **防务+科技集团**：2003 年起步（Interdata），6-8 家子公司：**Pavotek**（旗舰：PSHIELD BSS 边境蜂窝拦截/干扰系统、Gökalp IHA、METE 制导炸弹、launcher drone、NICOW 移动网络、Fixpoint 作战中心、KBRN 防化）、**Pavelsis**（航电/FPGA）、Interdata、Andasis（通信）、Panod（机电集成）、Istanbul Defence Systems；**CEO = Bilal Yıldız**，董事长 = Dr. Alper Özbilen；出口占比 **60-70%**，市场=亚/海湾/非/欧/美洲
- 2026 年活跃度极高：07-24 拜访 **TUSAŞ**、07-30 会见 **Türkiye Wealth Fund** CFO、08-27 印尼 Republikorp 防务合作、SAHA EXPO/IDEX/Milipol 常客
- **PNetworks 品牌 2021 年才成立**（集团 19 年防务积累的品牌延伸，"把防务经验带给企业行业"——bthaber 2022-03-16 原话）

**产品线演进（2021 → 2026，官网 31 项 datasheets 实抓）**
- 2021 首发：工业无风扇 **−40/+70 °C**、全口 PoE+、L2 + **L3 静态路由**、IEEE 1588v2 PTP + Sync-E、冗余电源 —— "Türkiye'nin ilk yerli switch'i"
- 2026 现状（官网）：**PN-CMS/LMS** 8/24/48 口 GE 企业线（大量 PoE+ 变体）、**PN-TMS24QSFP4QSFP+ / PN-TMS48SFP+6QSFP+ = 数据中心 100G/25G 线**、PN-AC1/AC2 WiFi、PN-NMS 安全、SFP 模块；官网四大方向 = AI/ML、Cloud Data Center、Operator Network、Optics
- 解读：**从"一个工业 8 口"长成运营商+DC 全栈**——与 Angora（工业 8 口 L2+ 为主）的相对差距在拉大，不在缩小

**实体修正（第 15 轮，官网 About + RocketReach）**：PNetworks A.Ş. **2019 年注册**（Teknopark İstanbul）、实体仅 **3 名员工**（RocketReach；PAVO 集团 600+）→ 品牌 2021 首发 switch = 集团资源注入的轻实体，"本土制造"叙事更多依赖集团背书与 Teknopark 位置

**硬件底座真相（第 16 轮，Edgecore 官方新闻稿 + About 页 + datasheet 照片）**：
- **Edgecore 官方新闻稿（MWC 2024-02-29）**：Edgecore × PNetworks 战略合作 → 土耳其市场交付 **Intel Habana AI 加速器 + Broadcom 交换芯片 + SONiC 平台** 的 AI/ML 网络方案；About 页：借 Edgecore 设计覆盖 **400G/100G/25G/10G/2.5G/1G** DC/SP/企业产品 + IP Infusion（OcNOS，2016 起支持 Edgecore 硬件）
- **白牌贴牌实锤**：多份 datasheet 机前面板照片印着**其他品牌**（PACIFIC WIRELESS / PRESTIGE / **PowerConnect（华为系）** / "PROTECTED" / 带 VGA/HDMI 的非交换机面板 "MAGC1"）→ CMS/LMS 企业工业线 = 白牌 ODM 平台 + 贴牌，照片沿用 ODM 公版
- 高管更替：2023 MWC 总经理 = **Ömer Ragıp Özkan**；2024 起 CEO = **Can Okan Dirican**（Bilal Yıldız 是 PAVO 集团 CEO，非 PNetworks 实体）
- 装机量自述（About 页，**未验证**）："nearly **100,000 devices installed and actively operational across 80 provinces**"——若属实则渠道渗透远超 EKAP 可见度（走企业/运营商非公共标单渠道 + 营销口径）
- → **"Türkiye'nin ilk yerli switch'i" 成色定级：本地化品牌 + 软件集成（SONiC/OcNOS）+ 防务叙事 + 国家背书；硬件 = Edgecore/白牌 ODM（Broadcom 芯片）**——与 Angora×Ewind 结构同构

**datasheets 实测规格（第 15 轮，10/31 份 PDF 逐份解析，详见 §9 表）**
- **TMS24QSFP4QSFP+**：24×25G SFP+ + 4×40G QSFP+，**1.86Tbps**，4GB RAM，G.8032 环网 <50ms + IEEE 1588v2/Sync-E 硬件，**L3 可选（BGP/OSPFv3/PIM）**，802.1x/RADIUS/NAC
- **TMS48SFP+6QSFP+**：48×SFP+ + 6×40/100G QSFP+，**3.6Tbps L2+L3 线速**，2×450W 热插拔，**TWAMP**（ISP 性能测量）→ 已具备 100G 骨干交付能力
- **CMS/LMS 企业工业线**：8/24/48 口，−40/+70 °C IP53，IEC 61850-3，PoE 预算 **240–500W**（30W/口、可选 PoE++ 60W），DIN 导轨 12VDC 工业款
- **PN-NMS（独立软件，©2021）**：SNMP/NETCONF/**SDN-OpenFlow**/NetFlow、LLDP 拓扑、**ZTP 零接触部署**、**按设备许可收费**、FCAPS/LDAP/AD/HTTP API
- **PN SFP 模块 PN_S1–S8（自产光模块）**：1G LX/ZX、10G SX/LX、1G MMF，SFF-8472 DDM
- → **结论升级为"全栈竞争者"：交换机 + NMS 软件 + 光模块**，且 NMS 按设备许可 = 经常性收入模型（第 14 轮只看到硬件，本轮补齐软件腿）
- **QA 信号（竞争叙事可用）**：多份 datasheet 存在整表复制错误（48 口页印 52Gbps + 24 口端口表、正文错型号名）→ 产品线 5 年扩张 31 项，文档 QA 跟不上，轻实体（3 人）+ 集团背书的组织形态再次得到侧面印证

**招标/客户情报**
- 2021-04-02：Pendik 市 + Teknopark İstanbul "Türkiye'nin Switch'ini Destekleme ve İşbirliği Protokolü"（Pendik = 首用户）
- 2022-03-16：L&N Bilgisayar Ankara 发布会（公共部门推售；产品已在 UAV/战斗机/直升机/坦克/OBÜS 平台服役）
- 叙事武器：Özbilen 2023-09 "7 点宣言"（经济独立/反 Cisco-Huawei 垄断/数据主权/反间谍层）+ "Türkiye'nin tek yerli switch'i PNETWORKS'e sahip çık!"（X 平台 campaign）
- **EKAP 中标扫描（第 15 轮死角打通 → 第 16 轮收口）**：rehbersanayi.com 镜像 IT 归档 547 项；无浏览器环境穷举边界 = 第 1 页 HTML 60 条（2026-10-06→09-28）全扫 + 站内目录搜索（0）+ Google 索引（0）= **PnetWorks/PAVO/Ewind/Angora 0 中标命中**（更正第 15 轮 ≈120 条误估；剩余 487 条 = 客户端 JS 分页、无公开 API，需浏览器或 EKAP 官方 API 账号）
- **2026 标单情报**：Trabzon Büyükşehir İKN 2026/1272126（08-05）= 1 骨干 + 20 边缘 switch + **1 套网管软件** + 50 AP、**仅本土供应商** → 与 PNetworks 全栈完全对口（其理想画像）；**TTK 2025-12-25 30 台 managed switch（第 16 轮原文核实**：土耳其煤矿机构，3 类规格 128Gbps/95.23Mpps、128Gbps/95.24Mpps、176Gbps/130Mpps/32K MAC——均为市场标准参数，**"按 PNetworks 定制"假设不成立**；**2.2.40：SFP/SFP+ 必须与交换机同品牌、拒绝 OEM 光模块**；3.3 制造商授权书；2 年保修；2026-01-15 截止）；İSTTELKOM 2026-09-15 244.6M TL 服务器+交换机+备份**仅 1 家投标**（关系型市场信号）
- **零售价格（第 16 轮，n11.com PNetworks 品牌店）**：CMS48GE4SFP+ PoE+ **156,612 TL**（活动 144,666）；48GE PoE+ 款 150,812 TL（活动 139,301）→ 48 口 PoE+ 零售 14-15 万 TL 量级，电商公开在售（不止 L&N 公共部门渠道）

**对 Angora 的威胁 = 高**：它占着"唯一 yerli switch"的国家叙事 + 政府/防务/运营商/DC 全场景 + Teknopark 国家背书 + 集团 600+ 人。**对 Angora 的正面挤压方向**：凡是写"yerli"要求的公共标单，PNetworks 都天然占优。
**对我方的威胁 = 中**：它做高端（运营商/DC/防务），我方 Marvell 线打企业/ISP/工业价格带——**暂时不同台**；但若其下探企业级 managed 或把"yerli"叙事武器化到企业标单，升级警报。

## 三、其他本土玩家（摘要，细节见 CSV）

- **Netaş**：本土 switch 的真正"国家队"在防务侧——SGN/MAGN 洞室交换机、ULAK 基站、NETSWIFT 本土服务器、5 项本土产品认证、ZTE 本地化伙伴（服务器/DWDM/FTTx）。做公共/防务网叙事，不碰企业 L2/L3。**启示**：ZTE×Netaş 的"联合本地化换本土认证"模式值得我方研究（第 5 节）。
- **Aselsan × TT 本土手机**（2027）：本土硬件工业政策的温度计——国家信用 + Malatya 产能向消费电子延伸，网络设备线是潜在外溢。
- **TT/Argela Netsia BB Suite**：SEBA 软件 150 万户、自称"全球最大 live SEBA"——运营商接入网在软件定义化，硬件采购结构会变。
- **安全 niche（Angora 数据二极管线的同簇对手）**：**DataFlowX**（DataDiodeX：EAL4+ + Pardus + Tech Data 全球分销，2022 起；DataBrokerX 网关）> Rovenma（Kindi，芯片级自研）> MAY Siber（本土 NAC，250+ 客户）。Angora 的 Arrow 数据二极管在这个簇里**知名度最低**——差异化只能靠工业场景（ModBUS/OPC）+ EGM 认证绑定。
- **Keenetic Türkiye**：JV（俄品牌 × Zyxel 土耳其系创始人 Vefa Tarhan）+ ARENA 分销，2024-12 入市、2026-06 上 switch（5/8/16/24 口、2.5G、PoE+、unmanaged+QoS）。能量强但场景是家用/SMB/摄像头——**观察项**。
- **本土 AP 制造 = 空白**：搜遍无本土 AP 厂（货架全是 TP-Link/Hikvision/BDCOM 系）。Angora 进口里的 "WIRELESS CONTROLER SWITCH"（TTD 2024-04-15 票）说明它也在中国买无线——这个 niche 无本土对手。
- **UPCOM 重名陷阱**：UPCOM(TR)=光纤/机架本土厂（upcom.com.tr）；UPCOM(CN)=中国工业交换机厂（upcomnet.com）——客户/标单处易混淆，已入 CSV 两行分列。

## 四、关键认知更正："本土"幻觉

Angora 进口盘（第 13 轮 20 号档案）里的供应商：Ewind（深圳）、Fengrunda/IZIFI（东莞）、Eglobal（深圳）、Qiyang（郑州）、Larch/NEM……——**Angora 的"硬件国产化 17-19%"，本土部分 = 设计/组装/软件/认证/公共关系，进口部分 = 中国 ODM**。因此：
1. 真正的本土竞争只有 PNetworks（switch）+ Netaş（防务网）+ 安全簇（DataFlowX 等）；
2. **Angora 与我方共享同一批中国 ODM 供应池**——Ewind 既供 Angora 又直售土耳其（atommarket 在售 6+ 型号），意味着"我方 vs Angora 上游"与"我方 vs Ewind 品牌"是两场并行的价格战；
3. "yerli" 的护城河不在制造，在**国家叙事 + 认证 + 公共部门关系**——我方白牌路线无法复制（见 97 号档案白牌三选一）。

## 五、定位矩阵与空档（对我方 Marvell 线的机会）

| 场景 | PNetworks | Netaş/Aselsan | Angora | Ewind/IZIFI（中国系） | Mikrotik（基准） | **我方空档** |
|---|---|---|---|---|---|---|
| 防务/国家叙事 | ● 强 | ● 极强 | ○ 中 | — | — | × 不做 |
| 运营商/DC | ● 强（TMS 线） | ● 强 | — | — | ○ | × 暂不 |
| 公共标单（"yerli"要求） | ● 强 | ● 强 | ○ EGM 认证工业口 | — | × | ○ 借 Angora/ELCORE 通道 |
| 工业 8 口 L2+ | ○ | — | ● 主场 | ● Ewind 工业线同价带 | × | ● **正面战场**：875 RMB 成本价 + 串口/定制 |
| 企业 L2+/L3 edge（对标 Mikrotik） | ○ 下探风险 | — | ○ | ○ | ● 基准 | ● **第二战场**：经 ELCORE/Poyraz 场景映射 |
| GPON/FTTX 组合 | ○（Optics 方向） | — | — | ● V-SOL 占位 | — | ○ 观察（V-SOL 先例可行） |
| 家用/SMB/摄像头 | — | — | — | ○ | ○ | ○ Keenetic 占位中 |

**结论**：两个正面战场（工业 8 口 = 现在；企业 L2+/L3 对标 Mikrotik = 经 97 号双轨渠道推进）+ 一个观察项（GPON 组合）。PNetworks 下探企业级 = 我方最需要监控的信号。

## 六、威胁评级汇总（= CSV 两列威胁的摘要）

| 竞争者 | 对 Angora | 对我方 | 一句话 |
|---|---|---|---|
| PNetworks | **高** | 中 | 本土叙事垄断者，正向上做 DC |
| Netaş | 中（相邻） | 低-中 | 防务国家队；ZTE 模式可借鉴 |
| Aselsan×TT | 中 | 低 | 2027 手机 = 政策信号 |
| TT/Argela | 中 | 低 | SEBA 改接入网采购结构 |
| DataFlowX | **中（同簇）** | 低 | 数据二极管 + 全球分销 |
| Rovenma / MAY | 低-中 / 低 | 低 | 安全簇次席 |
| Keenetic TR | 低 | 低-中 | 强品牌新进入者，观察 12 个月 |
| Ewind（深圳） | 供应商 | **高** | 同源全产品线，价格战主力 |
| IZIFI/Fengrunda | 供应商 | 中 | 同源，PoE/L3/无线全有 |
| V-SOL（广州） | — | 中 | 占 TR GPON 位 |
| Mikrotik | — | 中（基准） | 规格映射对象 |
| TP-Link 等全球系 | 中 | 中 | 标单实际对手 |

## 七、观察清单与下轮挖掘线索

1. ~~**PNetworks 中标记录** + datasheets 逐份解析~~ → **✅ 第 15 轮执行 → ✅ 第 16 轮全部收尾**：datasheets 26/27 唯一项全解析（1 死链 PN-AC1）；EKAP 扫描收口 60/547 + 三路旁证 0 命中（剩余 487 条 = JS 分页，无浏览器环境不可穷举）；TTK 定制假设降级（原文标准参数 + 2.2.40 同品牌光模块条款新发现）。该线索簇**关闭**，后续增量 = 浏览器渲染（如需 100% 全量）
2. **Ewind 土耳其直售速度**：atommarket 库存/价格跟踪（本轮已见 6+ 型号在售）
3. **Netaş-ZTE 本地化协议范围**：年报 PDF（2022 已见，后续年度跟踪）
4. **DataFlowX 中标**：DataDiodeX 在能源/金融/防务的落单（TGSK 集群目录 + 新闻）
5. **Keenetic TR 12 个月**：是否进 managed/工业/运营商线
6. **Poyraz 所售中国品牌组合变化**（Ruijie/Tenda/V-Sol → 是否有 SmartByte 系/我方系进入）
7. 死角更新：**EKAP 官方 JS 应用仍死角，但 rehbersanayi.com 镜像已打通**（HTML 可抓，第 15 轮起可用）；Instagram/LinkedIn 403、Shodan/FOFA 无账号不变

## 八、数据边界（如实）

- ensun.io "Top 14"：第 11 位第 15 轮已恢复 = **Provider**（Pendik 2018，SI/IoT 集团，非 switch 硬件）；第 12-14 位名称仍未能取回（页面分块截断，二次抓取+搜索均无果，不重试）；该页统计口径"5 制造商 + 3 服务商"已记录
- Netaş/Aselsan/Trustnet 等"成立年份"标注**待核**（未获第二来源）
- HITIT（网络品牌）无独立 web 存在 → 维持第 4 轮判定：Ewind 白牌（印度海关证据），本轮搜索再次无独立信息（hitit.com = 航空软件公司，无关；hititetiket.com = 标签/缎带，无关）
- PNetworks datasheets（第 15 轮 → **第 16 轮全量收尾**）：26/27 唯一项解析完成（31 清单项 − 1 死链 PN-AC1 − 2 空项 − 2 组重复 URL）；第 15 轮"pn-cms48ge4sfp.pdf 死链"为取 URL 误记，**大写 URL PN-CMS48GE4SFP.pdf 可访问（已解析）**；WiFi 线仅 PN-AC2（Wi-Fi 6 + 4G LTE CPE 二合一）
- EKAP 中标扫描（第 15 轮 → **第 16 轮收口**）：rehbersanayi IT 归档无浏览器环境穷举边界 = **60/547 条**（第 1 页 HTML 全量 2026-10-06→09-28，三路径 0 命中；`?page=`/`?sayfa=` 无效、`/…/2` 404、无公开 API、`/ara` 仅目录、Google 索引 0）；**更正第 15 轮 ≈120 条误估**（第 1 页 HTML 实为 60 条）；剩余 487 条需浏览器渲染 JS 或 EKAP 官方 API 账号
- TTK 招标 spec 与 CMS24 datasheet "95.24Mpps" 数值吻合（第 15 轮假设）→ **第 16 轮降级为不成立**：taskomuru.gov.tr 官方技术规格书 3 类规格（95.23/95.24/130Mpps）= 市场标准线速参数，无定制证据；TTK 实为**土耳其煤矿机构**（非国铁）
- PNetworks 装机量 "~100,000 devices / 80 provinces"（官网 About 页自述）= **未验证营销口径**，与 EKAP 0 命中并存（解释：非公共标单渠道为主）

## 九、第 15 轮更新：PNetworks datasheets 实测 + EKAP 扫描 + ensun 补全（2026-10-08）

> 用户指令「都搞了」= 执行第 14 轮三条遗留线索。原始材料全量落库：`99-raw/pnetworks-datasheets-extract-2026-10-08.md`。

### 9.1 datasheets 实测规格表（10/31 份解析成功；2 死链 404）

| 型号 | 定位 | 端口 | 性能/电源 | 要点 |
|---|---|---|---|---|
| TMS24QSFP4QSFP+ | DC 25G/40G | 24×SFP+(1/10/25G) + 4×40G QSFP+ | 1.86Tbps，4GB RAM，128K MAC，0/+50 °C IP53 1U 6.2kg | G.8032 <50ms、1588v2/Sync-E、L3 可选 BGP/OSPFv3/PIM、8 HW 队列、802.1x/RADIUS/NAC/CoA |
| TMS48SFP+6QSFP+ | **DC 骨干 switch/router** | 48×SFP+ + 6×40/100G QSFP+ | **3.6Tbps L2+L3 线速**，2×450W 热插拔，IP20 8kg | +TWAMP（ISP 性能测量） |
| CMS8GE2CG（±PoE+） | 工业边缘 | 8GE + 2×1G SFP/Combo | 20Gbps，−40/+70 °C IP53，12VDC，DIN 1040g | PoE 30W/口·预算 240W·opt PoE++ 60W，IEC 61850-3 |
| CMS8GE4SFP | 工业边缘 | 8GE + 4×1G SFP | 24Gbps | 同上壳 |
| CMS24GE4SFP+（±PoE） | 企业/工业 24 口 | 24GE + 4×10G SFP+ | 128Gbps、95.24Mpps（原文误印 95 Mbps），1U 3kg | PoE 预算 **500W**；**TTK spec 疑似来源（待核）** |
| LMS24GE4SFP+ | 同壳 L 系 | 24GE + 4×10G SFP+ | 2465g | C/L 系列差异化不明（扩张痕迹） |
| CMS48GE6SFP+（PoE+） | 企业 48 口 | 48GE + 6×10G SFP+ | ⚠️ 原文 52Gbps = 复制 24 口表错误 | PoE 240W、IEC 61850-3、TWAMP |
| **PN-NMS**（©2021） | **Web NMS 独立软件** | — | 最低 50GB/24GB/4 核 | SNMP/NETCONF/SDN-OpenFlow/NetFlow、LLDP 拓扑、**ZTP**、**按设备许可**、FCAPS、LDAP/AD、HTTP API |
| **PN SFP PN_S1–S8** | **自产光模块** | 1G LX 1310/20km · 1G ZX 1550/80km · 10G SX/LX · 1G 850/0.5km | SFF-8472 DDM 可选 | 自产 optics |

**升级判定**：第 14 轮"硬件全栈（工业→DC 100G）" → 第 15 轮"硬件 + **NMS 软件（按设备许可 = 经常性收入）** + **自产 SFP**"全栈竞争者。对我方 STI/ANW 线的含义：企业 L2+/L3 第二战场面对的已不是单一硬件对手，而是"switch + 网管 + 光模块 + 本土叙事"打包——我方 Marvell 线优势仍是**单设备性价比与定制**（串口/协议栈/875 RMB 成本位），其 NMS 许可费与集团定价结构是持续监控点。

**QA 信号**：48 口页 52Gbps + 24 口端口表、多份正文错型号名 → 31 项产品线文档 QA 失控，3 人轻实体 + 集团背书的组织形态侧面印证（可用于"本土品牌"质疑叙事，谨慎使用）。

### 9.2 rehbersanayi EKAP 扫描（EKAP 死角首次打通）

- 数据源：`rehbersanayi.com/veri/ihale-sonuclari`（2026-06-30→10-06 共 **27,412 项 / 1,118.6M TL / 38% 中标 ≤2 家投标**）+ IT 行业归档 547 项
- 扫描范围（边界如实）：IT 归档第 1–6 页 ≈120/547 条（最新段 2026-09/10）；检索 PnetWorks/PNetworks/PAVO/Ewind/Angora/yerli switch → **0 命中**
  - ⚠️ **第 16 轮更正**："第 1–6 页 ≈120 条"为误估——站点服务器端 HTML 实际只渲染第 1 页 = **60 条**（chunk 0–3，第 4 chunk 为页脚）；`?page=2`/`?sayfa=2` 参数被忽略、`/…/2` 路径 404、无公开 API。正确口径 = **已扫 60/547（2026-10-06→09-28，0 命中）+ 站内目录搜索 0 + Google 索引 0**；剩余 487 条由客户端 JS 分页加载，无浏览器环境不可达（收口声明）
- 市场结构信号：**İSTTELKOM 2026-09-15 服务器+交换机+备份 244.6M TL 仅 1 家投标** → 大额 switch 采购关系驱动、竞争稀薄，品牌矩阵 ≠ 中标量
- 结论：PNetworks "渠道窄、中标量级不大"判断与第 14 轮一致（官方标单可见度低）；全量 547 条扫描 = 低优先级线索

### 9.3 2026 标单情报（与 PNetworks 画像对口度）

| 标单 | 日期 | 内容 | 意义 |
|---|---|---|---|
| Trabzon Büyükşehir İKN **2026/1272126** | 2026-08-05 | 1 骨干 + 20 边缘 switch + **1 套网管软件** + 50 AP，**yalnızca yerli istekliler** | PNetworks 全栈（TMS+CMS+PN-NMS+AC 无线）**完全对口**的理想画像单 |
| TTK（土耳其国铁） | 2025-12-25 | 30 台 managed switch | spec 95.24Mpps ≈ CMS24 datasheet 数值（疑似按规格定制或反向，**待核**）<br>⚠️ **第 16 轮原文核实更正**：TTK = 土耳其**煤矿**机构（Türkiye Taşkömürü Kurumu，宗古尔达克）；官方技术规格书 3 类（24SFP+8combo+4SFP+ 骨干 128Gbps/95.23Mpps、24GE+4SFP+ 128Gbps/95.24Mpps、48GE+4SFP+ 176Gbps/130Mpps/32K MAC）**均为市场标准线速参数 → 定制假设不成立**；**2.2.40 条款：SFP/SFP+ 必须与交换机同品牌、拒绝 OEM 光模块** + 3.3 制造商授权书 + 30 天交付 + 2 年保修，投标截止 2026-01-15 |
| İSTTELKOM | 2026-09-15 | 服务器+交换机+备份，244.6M TL，1 家投标 | 运营商级单存在但关系驱动 |

### 9.4 ensun Top 14 补全

- **#11 = Provider**（Pendik，2018，11–50 人）：区域 SI/IoT/大数据/云集团（另见 ensun 系统集成 Top 41）——非 switch 硬件制造商，第 14 轮"本土 switch 硬件 ≈ 5 家"结论不变
- #12–14：chunk 边界截断后二次抓取+搜索均无法恢复 → 数据边界，不重试

## 十、第 16 轮更新：datasheets 全量收尾 + EKAP 收口 + TTK 原文 + Edgecore 底座（2026-10-08）

> 用户指令「都搞了 需你邮箱这个啥意思？」= 执行第 15 轮 3 条低优线索 + 解释"需你邮箱"（Volza/TradeData.pro 免费样例注册邮箱，非新信源）。原始材料全量落库：`99-raw/pnetworks-round16-fullscan-2026-10-08.md`。

### 10.1 datasheets 全量收尾（本轮 15 份 → 累计 26/27 唯一项）

| 新增型号（本轮 15 份） | 端口/性能（原文） | 要点 |
|---|---|---|
| LMS24GE2SFP（±PoE+） | 24GE+2×1G SFP，52Gbps/"38Mbps" 笔误 | LMS=低 PoE 预算系（240W vs CMS 500W）；非 PoE 版标 28VDC（疑笔误） |
| LMS24GE4SFP+ PoE+ | 24GE+4×10G SFP+，128Gbps/"95Mbps" 笔误 | TTK 2.2 类（95.24Mpps）参数同源标准值 |
| CMS8GE4SFP PoE+ | 8GE+4×1G SFP，24Gbps | PoE 预算 250W（与 CMS8GE2CG 的 240W 不一致） |
| CMS8GE2SFP+PoE+（土耳其语版） | 标题 14 口 vs 正文 10 口，56Gbps | 全线唯一土语 datasheet；L3 表独有 IS-IS |
| CMS48GE4SFP2SFP+ | 48GE+4×1G SFP+2×10G SFP+（54 口） | 整表 = 24 口数值（52Gbps）+ 8 口壳尺寸 |
| CMS48GE4SFP+ PoE+（=#30 重复项） | 48GE+4×1G SFP，104Gbps | 分类表 PoE 370W vs 正文 240W 自相矛盾 |
| CMS48GE4SFP / CMS24GE4SFP（非 PoE 两款） | 104Gbps / 56Gbps | **CMS48 非 PoE：128K MAC + 30,000 TCAM**（vs 其他表 16K，跨表不一致）；12VDC |
| CMS24GE2SFP+（±PoE+） | 24GE+2×10G SFP+，88Gbps | 48-54VDC |
| **CMS24SFP4SFP+（新形态）** | **24×SFP(1000BASE-X)+4×10G SFP+**，104Gbps | 全光纤 28 口，唯一端口表与标题一致的 sheet |
| **PN-AC2（WiFi 线唯一存活项）** | Wi-Fi 6 AP + **4G LTE CPE 二合一**（LTE 上 150/下 600Mbps），4×RJ45+USB | TR-069/WPA3/4+4 SSID/OpenVPN/IPsec/内容检查；0/+40 °C IP30 → **运营商 CPE 形态，非企业 AP**；PN-AC1 死链 |

- **全量账**：31 清单项 = 26 解析 + 1 死链（PN-AC1）+ 2 空项（Energy/System 官网自标"veri yok"）+ 2 组重复 URL（#3=#10、#16=#30）
- **⚠️ 白牌贴牌实锤**：多份 datasheet 机前面板照片印着其他品牌（PACIFIC WIRELESS / PRESTIGE / **PowerConnect（华为系）** / PROTECTED / 带 VGA/HDMI 的非交换机面板）→ 企业工业线 = 白牌 ODM 平台 + 贴牌
- **⭐ Edgecore 底座坐实**：Edgecore 官方新闻稿（MWC 2024-02-29）= Intel Habana + **Broadcom 交换芯片** + **SONiC** 平台战略合作；About 页覆盖 400G→1G；IP Infusion OcNOS（2016 起支持 Edgecore HW）→ TMS 线硬件底座 = Edgecore（台湾 ODM）
- **⚠️ 装机量自述**："nearly 100,000 devices installed and actively operational across 80 provinces"（About 页，未验证；与 EKAP 0 命中并存 = 非公共标单渠道为主）
- **高管更替**：2023 GM = Ömer Ragıp Özkan → 2024 CEO = **Can Okan Dirican**（Bilal Yıldız = PAVO 集团 CEO，两者并存不冲突）
- **零售价格（n11.com 品牌店）**：CMS48GE4SFP+ PoE+ **156,612 TL**（活动 144,666）；48GE PoE+ 款 150,812 TL（活动 139,301）→ 14-15 万 TL 量级公开零售
- **QA 信号升级**：15 份新 datasheet 中 ≥9 份存在复制粘贴错误（错端口表/错性能/错尺寸/错电压/错品牌照片/自相矛盾 PoE 预算）→ 3 人实体运营 27+ SKU 的文档失管，"本土深度"叙事的组织侧佐证

### 10.2 rehbersanayi 全量扫描收口（边界声明）

| 方法 | 结果 |
|---|---|
| 第 1 页 HTML 全量（chunk 0–3） | **60 条**（2026-10-06→09-28），逐条扫描 0 厂商命中 |
| `?page=2` / `?sayfa=2`（www/非 www） | 参数被忽略（返回第 1 页） |
| 路径段 `/…/2` | 404 |
| 公开 API | 未发现 |
| `/ara?q=pnetworks`（站内搜索） | 0 结果（仅覆盖企业目录/OSB/行业/城市） |
| Google 索引 site: 检索 | 0 厂商命中 |

**收口**：无浏览器环境下可穷举 = **60/547 + 三路旁证，全部 0 命中**；剩余 487 条（更早月份）= 客户端 JS 分页，需浏览器渲染或 EKAP 官方 API 账号（用户如需要，下轮可上浏览器方案）。**更正第 15 轮 "≈120/547" 误估**（第 1 页 HTML 实为 60 条）。补充信号：60 条内 Bilgibim 36.5M TL 延保 1 家投标、CCC 58.1M TL 气象硬件 1 家投标 → 低竞争结构再验证。

### 10.3 TTK 招标原文核实（taskomuru.gov.tr 官方技术规格书，6 页）

- **TTK = Türkiye Taşkömürü Kurumu（土耳其煤矿机构，宗古尔达克）**——更正第 15 轮"国铁"误读（TCDD 才是国铁）
- 30 台可管交换机（总管理处+下属企业合并），2025-12-25 预告，**2026-01-15 14:00 截止**，30 天交付宗古尔达克，2 年保修
- 3 类规格：①2.1 骨干 24×SFP+8×GE combo+4×10G SFP+（28 口）128Gbps/95.23Mpps，16K MAC，L3 静态+RIP/OSPF，MTBF≥760,000h，端口 4kV 保护；②2.2 边缘 24GE+4×SFP+，128Gbps/95.24Mpps，16K MAC，静态 124v4/50v6，768 ACL（含时间基），RADIUS/TACACS+，LBD/线缆诊断/双镜像；③2.3 边缘 48GE+4×SFP+，**176Gbps/130Mpps/32K MAC**
- **⭐ 2.2.40（关键条款）**：SFP/SFP+ 光模块**必须与交换机同品牌，OEM 品牌光模块不接受**；**3.3**：制造商/分销商**针对本次招标的授权书**（sales & technical support）；3.9：售后资质（商务部售后能力证或 TSE 服务点）
- **假设判定**："95.24Mpps 按 PNetworks 定制" → **不成立**（95.23/95.24/130Mpps 均为 24GE+4×10G / 48GE+4×10G 的标准线速参数；PNetworks CMS24 印 "95 Mbps" 只是标准值的笔误）。但规格面与 PNetworks CMS 能力高度贴合（其 −40/+70 能力远超标书 −5/+50 要求）；**我方 Marvell 24/48 口线同样完全合格**——TTK 型标单对我方**不是禁区**，门槛 = 授权书 + 售后资质 + 同品牌光模块（我方 SFP ¥25/只，无成本压力）

### 10.4 战略含义（第 16 轮定稿）

1. **PNetworks "本土"成色最终定级**：本地化品牌 + 软件集成（SONiC/OcNOS）+ 防务叙事 + Teknopark/国家背书；**硬件 = Edgecore（Broadcom 芯片）+ 白牌 ODM 贴牌**（面板照片实锤）——与 Angora×Ewind（深圳 ODM）结构同构，"我方 vs Angora"与"我方 vs PNetworks"共享同一 ODM 上游池逻辑
2. **同品牌光模块条款（2.2.40 型）**：土耳其公共标单正在出现"整机+光模块同品牌、拒 OEM 光模块"条款 → **全栈（含自产/自品牌 optics）= 结构性投标资格优势**；我方进 TR 标单必须捆绑自品牌 SFP（成本 ¥25/只，无压力），PNetworks 自产 PN SFP 的战略价值在此类条款下兑现
3. **PNetworks 竞争位势修正**：第 15 轮"渠道窄"判断部分降级——若 ~100K 装机自述属实，其在企业/运营商**非公共标单**渠道渗透深；公共标单（EKAP）可见度低是**渠道结构**（直销+集团关系），不是能力弱。监控重点从"中标量"改为**企业/运营商侧客户案例与 n11 零售价变动**
4. **我方威胁模型不变但精化**：PNetworks 主战场 = 运营商/DC/防务/公共"yerli"单（高）；企业 L2+/L3 价格带仍由 Ewind（深圳，同源同价带）+ Mikrotik 主导——我方两个正面战场（工业 8 口 / 企业 L2+L3 对标 Mikrotik）结论维持

## 十一、第 17 轮更新：土耳其公司全量挖掘（角色分层，2026-10-08）

> 用户指令："继续挖掘相关的土耳其公司 越多越好"（角色分层：本土 OEM/品牌、白牌 ODM、渠道分销、集成商、DC 运营、消费品牌、企业买家）。原始记录：`workstation/99-raw/turkey-companies-round17-2026-10-08.md`。三件套扩容：**CSV 19→80 数据行 × 20 列**（新增 61 行；更新 Mikrotik/Keenetic/PNetworks/Netaş 4 行）；XLSX 同步 81×20（图例页 +H/I/J 三级）；tier 图例新增 H=数据中心/终端客户、I=公共 IT 集成生态、J=低相关仅记录。

### 11.1 新增角色层（按战略价值排序）

**① 直接竞对/本土品牌层（B 层新增 3）**
- **Longline（Longline Bilişim，Bayrampaşa）**——本轮最重要发现：土耳其本土白牌**工业交换机**品牌。LNG5700-8TP2S（8×1GE PoE+ + 2×1G SFP，L2 受管，56Gbps，8K MAC，**售 7,182 TL，标 "Menşei: Türkiye"**）+ LNG5863-24X2C（24×10G SFP+ L3 静态/RIP/OSPF，256Gbps）。结构推断 = 中国 ODM 底座 + 本地品牌/服务（同 PNetworks/Ewind 同构）。**与我方 STI 工业 8 口 L2+ PoE 线正面同价带（≈$190）**= 中-高威胁，第一战场监控对象。NetGaste 工业交换机指南（2025-10-14，−40/+75 °C DIN 口径）疑为其软文，细节待核
- **StorNET Networks / LinkREAL / LR-Link（Beylikdüzü 2015）**——网络/服务器配件分销 + **自有品牌 = 同 chipset（Intel/Broadcom/Mellanox）换牌** + 中国工业交换机品牌 LR-Link 土耳其分销 + 售 Marvell/QLogic chipset 产品。非制造商；**潜在供货对象**（我方 optics/DAC）
- **ALCATTEL Teletaş（BIST: ALCTL）**——1983 年 Ümraniye OSB，381 人，**86%+ 芬兰 Nokia 持股**，运营商级交换板/传输/光设备土耳其本土制造 = "yerli 制造"话语的硬参照系；不打企业 L2/L3 价格带（低直接威胁），但其存在定义了这个市场的"本土制造"叙事天花板

**② 安全簇（D 层新增 6 行）**：Barikat（300+ 人，本土防火墙第一品牌，**ICS 防火墙**与工控交换机同项目采购=场景交集）、Berqnet（Fast50 2020）、**Labris**（HARPP DDoS + UTM + **MNG 集中管理 appliance = 与 PN-NMS 同模式**）、PONIVA（Gaziantep，Turkuaz VPN）、Pozitif/UITSEC/İnnovera/Trapmine（打包）、**TÜBİTAK BİLGEM**（Derbent VPN/ORION DLP/Kuantum Pi = 国家研发天花板）。官方锚点：**总统府 2023-08-03 "16 家国家网络安全企业"名单**（cbddo.gov.tr）= Barikat/Labris/Türksat/STM/Adeo/TT/Procenne/Ölçsan/Vestel/Parta/Kron/Fileorbis/Turkcell/**PAVO Grup**/Gais/BugBounter——**PAVO（PNetworks 母公司）再次进入国家级名单**

**③ 数据中心层（H 层新增 20 行）= 我方 TMS/DC 线目标客户池**：Turkcell（8 DC 41.5MW + 2025 增 8.4MW/€100M）、TTK（12,700m²）、Vodafone（İzmir 与 Edgnex/DAMAC 共建）、银行 4 家（İşbank Atlas = Tier IV）、独立 DC 12 家（Telehouse = KDDI、Star of Bosphorus = NGN 16MW/2,000+ 机柜、**Equinix 收购本土 Zenium**、**Khazna = G42 最高 100MW**、Kyndryl 等）。结构性结论：TR DC 建设潮（2024–2026 外资+主权基金驱动）= 企业/DC 交换机需求引擎，且出现"本土玩家被跨国并购"先例（Zenium）

**④ 光纤/FTTx 生态（F 层新增 2 行）**：**OFT（Gaziantep，1985，自有 GEPON OLT/ONU = GPON niche 本土第二参照，V-SOL 之外）** + Turkuaz Kablo/OPTOKON/Netcom/Tekiz（线缆密度高、有源设备稀薄 = 结构性证据）

**⑤ 渠道层（G 层新增 2 行）= 双轨落地关键**：**Poyraz Network = Mikrotik 土耳其 Master Distribütör（2015 起）**，全品库存 + RouterOS 许可 + 项目集采 + 认证技术支持；**97 号双轨候选主力通道价值再证**（进入 Poyraz 体系 = 进入基准品牌主渠道）。渠道权力分散实证：Safir/wifianten/Ctech 均自称 master，Kablosuz Dünya 体系已含 **Ruijie**（中国系进 TR 渠道先例）

**⑥ 公共 IT 集成生态（I 层新增 24 行，打包）**：rehbersanayi 60 条中标（2026-09-28→10-06，İKN 可验真）提取 IT 硬件/软件中标商 ~30 家（Balkan 93.2M/CCC 58.1M/Bilgibim 36.5M/Venka 27.5M 企业网络集成/İnnova 24M/Arkenom 12.5M/Teknosis 12.1M/Fonet 11M/… 20 个打包行）= 公共标单同场者 + 潜在集成渠道候选池；医疗影像（J 层 1 打包行）+ 非 IT 类（J 层 1 打包行，含 Serkan Çankaya 32.2M 施工/Aygün 129.4M 运输 = 镜像分类噪声证据）

**⑦ 更新既有 4 行**：Mikrotik（+渠道多主代实证）、Keenetic Türkiye（+2026-05-14 专访 switch 线投产细节）、PNetworks（+PAVO 入 16 家国家名单）、Netaş（+800 R&D 工程师/5G 本土生产/V2X/GNSS 时钟/NETSWIFT 全产品线补全）

### 11.2 战略含义（第 17 轮）

1. **第一战场对手名单更新**：工业 8 口 L2+ 线 = 新增 **Longline**（7,182 TL，"yerli" 话术，小体量）与 Ewind（深圳）并列监控；我方 875 RMB 成本位 + 自品牌 optics 组合仍可正面打
2. **"yerli"叙事版图完成测绘**：制造叙事（Netaş/ALCTL-Nokia/Aselsan = 国家队，不抢我方价位）vs 白牌叙事（PNetworks/Longline/Ewind = 直接竞对，同源 ODM）vs 换牌分销（StorNET = 非竞对可供货）——三层分离，我方只需打第二层
3. **渠道 = 本轮最大可操作产出**：Poyraz（master 2015）确认 + 渠道多主代结构 = 双轨落地路径清晰（主力 Poyraz，分散化备选 Safir/wifianten/Kablosuz Dünya）；Ruijie 在 TR 渠道存在 = 中国系可行性验证
4. **DC 需求引擎确认**：TR DC 建设潮（41.5+8.4 MW 等）+ 外资并购本土 DC（Zenium）= TMS/DC switch 线的市场窗口；但进入路径 = 经 PNetworks/ELCORE/Angora 通道，非直销
5. **数据边界**：rehbersanayi 60 条 = 10 天窗口（非全量 547）；ensun top-14 名实全部识别完毕（#8 = StorNET）；Volza 公开页 = 注册墙（用户邮箱已登记，TTD 免费样本 2023-08→2024-07 已覆盖关键窗口）

## 十二、第 18 轮更新：最大努力继续挖掘（官方安全地图 + 渠道实证 + Longline 升级，2026-10-08）

> 用户指令："1 双轨 3选1 啥意思？ 2 不考虑合并 这个不要提了 3 继续 尽最大努力挖出最多的信息"（= ① 解释 97 号双轨/白牌三选一决策项〔已答复〕② **停止提及 PR 合并〔常设指示〕** ③ 继续最大努力挖掘）。原始记录：`workstation/99-raw/turkey-companies-round18-2026-10-08.md`。三件套扩容：CSV **80 → 88 数据行 × 20 列**（新增 8 行 + 更新 6 行）；XLSX 89×20 重建（图例刷新）。

### 12.1 官方安全产业地图（TSGK 集群，siberkume.org.tr，373 产品/26 类目/150+ 成员全名单）

- **⭐ 结构性发现：集群"网络设备"类目 = 仅 8 个产品**：ASELSAN×3（军规国产路由器族/工业国产路由器族/KKAC 加密 Wi-Fi AP）+ ULAK×3（MİLAT 虚拟交换机/UMAYA YT-GAA SD-WAN/UMAYA YT-VM SD-DC）+ PARTA×2（Targitas SD 安全路由/SD-WAN）→ **官方"本土网络设备"里没有企业级 L2/L3 管理交换机**；企业交换价位带 = 进口品牌 + 集群外的 PNetworks/Longline。PNetworks 用 IG bio "Turkey's First Domestic Switch Manufacturer" 占住这个空档叙事
- **数据二极管（跨域）= 6 个产品**：ASELSAN VERİ DİYODU（单向数据通道，军/民版）+ ASELSAN 虚拟气隙 + **CRYPTTECH**（2006，双 Teknopark，1,000+ 大客户，硅谷办公室）+ 其余（JS 渲染区，部分待核）
- **安全巨头成员**（此前未全部入表）：HAVELSAN/VESTEL/ARÇELİK/KOÇ SİSTEM/SABANCI DİJİTAL/KAM（银行）/BİTES/DeYTEK/Karel/Arvis/MİLSOFT/ÖLÇSAN/Procenne/Parta/PAVOTEK/ADEO/Gais/BugBounter/Kron/Fileorbis → 与总统府 16 家名单（2023）双层互证 = **安全域双层官方地图齐备**
- 新增厂商：EPATİ（Antikor NGFW/VFW/CLM/SD-WAN/VPN 产品族）、CRYPTTECH、SECUNNİX（XLOG FW）、Arjeta

### 12.2 ⭐ Longline 重大升级（直接竞对定级：中-高 → **高**）

- **LinkedIn 实锤：成立 2000，2008 年起自研产品族（首个产品 = SFP 光模块），11-50 人**（非"小店面"，是 SFP 起家的 20 年本土厂）
- **全产品线 10 型号**（makinaturkiye + hepsiburada）：桌面 5 口 750 TL → LNG5700-8T2S/8TP2S(7,182 TL)/24T4S → LNG5710-28TX（L3）→ **LNG5720-24MP6X（2.5G L3 PoE）** → **LNG5630-24TS4SX（Combo L3，49,000 TL）** → LNG5720-8H（L3 10G）→ 10G 48 口汇聚（New Arrival）→ **LNG3000-8TP2S-IK（工业 L3 PoE，直接对位我方 STI 线）**；SFP 全线（兼容 13 大厂商）；另售 Huawei S310
- **渠道实证**：hepsiburada 零售（24 月保修）+ makinaturkiye B2B + 自有站 → **与我方 SFP/工业 STI/企业 L2+L3/10G 汇聚逐线重叠 = 第一+第二战场双线交火**
- 我方打法：不与其争"yerli 老厂"叙事（2008），主武器 = 成本（875 RMB 位）+ 自品牌 optics 捆绑 + Poyraz 渠道；监控 = hepsiburada 周检价格带 + 新 SKU + 工业线出货

### 12.3 渠道实证（双轨两通道全量取证）

- **⭐ Poyraz 品牌矩阵（站内自证）**：Mikrotik = **Master Distribütör**；授权 = Ubiquiti/Aqara/Mimosa/Tachyon/Cudy/**V-Sol（中国 GPON 竞对品牌）/RF Element**；另售 = Tenda/Deltalink/Wiss Network/Ignitenet/**Ruijie（中国）/PN-Link（中国低价 PoE）**；10 年+/5,000+ SKU/15:00 当日发货/7/24 支持/B2B 经销商注册（Bayi Olun）/AI+Edge 愿景 → **中国品牌（V-Sol+Ruijie）已在组合 = 我方品牌入组合零排斥先例**
- **ELCORE 实测**：19 年/70+ 供应商/1,500+ 合作伙伴/8 子公司/100+ 团队；供应商墙 = Huawei/HPE/Dell/Nokia/Supermicro/Bosch/TrendAI/Motorola/Engenius/Kaytus/Paradox/Opentext/Scality/PentaSecurity/Sectona/NxLog +（97 号）MAIPU〔中国〕/Sangfor/Blackwall → 量级主力通道价值深化
- **PN-Link = 新重名陷阱**（Poyraz 店内中国低价被动 PoE，2,167 TL 级，与 PNetworks 缩写撞名）
- **L&N 利益冲突实锤**：c4defence 2022-03-17 = L&N 与 PNetworks 联合发布（L&N 负责公共机构渠道，口号"土耳其的数据交给土耳其的交换机"）→ 我方 97 号"L&N 辅助通道"需处理排他条款
- **PNetworks 增量**：总部 Teknopark İstanbul 4C Pendik；MWC 2024（GM Özkan，欧洲进入 = 出口启动）；"Made in Türkiye" 标签战略（about-us 2024-10）；Edgecore+IP Infusion 双伙伴

### 12.4 买家池定义（新 H 层行）

- **BTK/BTHK Q1 2025**：58 家持牌活跃 EHS；ISP 份额 2024 = %54/%39/%6（TT/Turkcell SO/Vodafone Net 三寡头）+ TurkNet/Türksat Kablo 等
- **dmo.gov.tr 政府设备目录**：230 交换机型号 + 7 路由器 + 95 SFP（多品牌开放含美系 EXTREME = "yerli" 非目录门槛）
- **目标客户池**：① WISP/酒店/宿舍（= Mikrotik 主力客群，Poyraz 博客自证 = 经 Poyraz 可及）② 政府目录（多品牌开放）③ 三大寡头 = 不直接打
- **ULAK（新 B 层行）**：ASELSAN 51%；MİLAT(MİLAT→MAYA SDN/NFV)；商用落地 = Türksat MAYA SD-WAN 生产网 + TT×农业林业部 500 点位 + 250 基站 → 运营商 SDN 域三强锁定（ULAK/Netaş/Argela），我方不进入

### 12.5 数据边界（第 18 轮）

- siberkume 类目页产品网格 = JS 渲染（静态 HTML 无产品；公司名单 + 类目结构 + Google 索引快照 = 本环境上限）
- n11 品类 URL = 404 + 搜索页 JS/反爬（维持第 16 轮品牌店口径）
- dmo.gov.tr 检索页 = JS 渲染（统计数字来自 Google 索引快照）
- Trabzon İKN 2026/1272126 中标结果未验证（08-05 开标，rehbersanayi 60 条窗口内无记录；EKAP 需 JS）

### 12.6 ⭐ 第 19 轮更新：Entegron = Longline 第二品牌（2026-10-08）

- **触发**：用户第 19 轮客户名单 #44 = entegronnetwork.com（备注"官网在售 E-wind/GXCOM"）——深搜判定**不是客户，是 Longline 的竞争者本体**
- **官网实锤**：about 页原文 "**Established in 2000, LONGLINE Technology Ltd** is one of the leading manufacturers of network communication products… specializes in PoE solutions and optical fiber communication products, including PoE Products, Managed/unmanaged ethernet switch, GEPON ONU, GEPON OLT and more"；地址 **Kartaltepe Mah. Hakan Sok. Longline Plaza No:18, 34040 Bayrampaşa**（与行 20 同址同年同公司）；0(212) 321 75 14/15
- **质量页原文**："Our primary goal, as **Longline**… Under the **Longline brand**… Every product produced is tested in the **Longline test center**" + **CE / RoHS / ISO 9001 / FCC** → 本地自有测试中心（比我方"纯 ODM 贴牌"推断更完整，品控体系需重新评估）
- **Entegron 品牌产品线（57 SKU）**：Ethernet Switch 11 + **PoE Switch 31** + EPON ONU 9 + GPON ONU 6 + **GEPON OLT（1U 8 口 GPON OLT / 4 口 EPON OLT）** + 10G intelligent access switch（8GE+4×10G SFP）+ L2 受管 8/16/24/28 口 + **ENTDPS208P Reverse PoE EPON ONU MDU（FTTB 楼道）**
- **结论**：Longline = **双品牌运营商**（LNG = 主 switch 线 longline.com.tr / Entegron = PoE+FTTx 线 entegronnetwork.com）；与 Angora 重叠面从"工业+企业 L2/L3"扩大至 **PoE 31 款 + FTTx OLT/ONU + 10G 接入 + Reverse PoE MDU**；威胁维持"**高**"（行 20 已同步更新）
- **监控增量**：entegronnetwork.com 周检（57 SKU 变动 + FTTx 线扩张）；用户备注中 E-wind/GXCOM 在售 = 其零售组合补充信号（未采信为客户证据）

## 十三、第 23 轮更新：全量复核 + 13 天新窗口（2026-10-21）

> 环境注：沙箱重置至基点（按 TASK-STATUS §八 恢复）+ **fetch_page 代理恢复**（rehbersanayi/hepsiburada/angoranetworks/fiberix 可直抓；ewindnet/pnetworks.com.tr 间歇失败 → web_search 摘要补足）。原始档案 = `99-raw/r23-recheck-mining-2026-10-21.md`。

### 13.1 EKAP 新窗口（rehbersanayi IT 归档 60 条，2026-10-09→10-19）
- 关键词扫描（Angora/PnetWorks/PAVO/Ewind/Longline/Mikrotik/switch/anahtar）= **0 命中**；与上轮窗口间存在 **10-01→10-08 盲区**（`?page=N` 参数确认仍被忽略 = JS 分页）
- **110 在册公司 6 起新中标**（İKN 逐条可验真，均已录入 CSV/XLSX 对应行）：
  - **Pantech（行 70）**：服务器供应 **132.5M TL / 仅 1 投标**，İKN 2026/1708449（10-19）→ 本轮最大单
  - **Fonet（行 63）**：SBYS+YBYS 医疗信息系统（Batman）**137.7M TL / 2 投标**，İKN 2026/1214002（10-15）
  - **Artı ve Artı（行 64）**：牙医医院服务器+存储+**网络设备**（Bursa）**9M TL / 仅 1 投标**，İKN 2026/1479835（10-12）
  - **NETCAD（行 73）**：CAD/GIS 两单 5.2M+5.3M TL / 1+1 投标，İKN 2026/1702069+1667628（10-16/15）
  - **Itech（行 74）**：E-Tır 集成 3.2M TL / 1 投标，İKN 2026/1798180（10-16）
  - **Gruptechs（行 76）**：MS 许可 1M TL / 3 投标，İKN 2026/1712577（10-13）
- 新窗口大额 SI 留档（未入 110）：Proday Bilişim（Ankara 两连中 15.3M+4.1M）、Cyberwise（11.9M）、Trust（6.3M）、CSIT（存储 9.8M）、Enfo（2.7M）等
- **市场统计（06-30→10-19）**：全行业 30,740 项 / 1,219.1 亿 TL / **38% ≤2 投标成交**；IT 625 项 / 16.2 亿 TL → 关系型市场结论再加强
- Trabzon Büyükşehir İKN 2026/1272126（PNetworks 全栈对口单）：结果落在盲区窗口（08-05 开标），**维持未验证**，下轮若页 2 可抓再核

### 13.2 ⭐ Ewind（深圳）2026 新品（ewindnet.com 官方新闻，经搜索摘要）
- **2026-04-29：EW-S3936GM Gigabit Managed = Microchip（Vitesse）芯片**（官网自述 "proven Microchip (Vitesse) chipset solution"）→ **芯片世代更新实锤**（39xx 线此前档案未记录）
- **2026-04-21：Industrial Cloud-Managed 系列**：hybrid PoE + 12/24V 被动 PoE + **802.3bt 90W** + DIN 轨 + 宽压 + 长距 → 工业云管理线扩张
- atommarket 目录 7 款在售：S2910GM-AP 4,475 / S1810GU-AP 1,005 / S1827CF-AP 3,471 TL 等；**S2924GM-AP（24GE PoE+ 4Combo 400W，既有锚点型号）仍在售** → 行 15 已录入

### 13.3 PNetworks 零售复核（2026-10-21）
- n11 锚点 **13 天不变**：CMS48 PoE+ 156,612 / Pn48 150,812 TL
- ⭐ **新增在售 PN8GE2CG（L2 管理 8 口 2 SFP/Combo PoE）= 61,419-63,707 TL** → 8 口 PoE 零售首次公开挂牌
- ⚠️ **渠道价差**：Trendyol 同 CMS48 PoE+ = **78,306.95 TL（约 n11 之半）**；akakce 多卖家 127K-204K → 多电商并行 + 价格不统一（价格战早期特征，我方定价直接参照）
- 2026 官方新闻 0 条（仅 2021-2024 旧档）→ 行 1 已录入

### 13.4 Longline hepsiburada 店铺复核（2026-10-21）
- 店铺 = **116 个产品**（r18 时点 ≈10 个 switch 模型）→ 零售铺货 10 倍级扩张；多卖家（Elektromarka/VENOT/miniöde/Emka/ÖZKARMAN/Core 等）
- ⭐ **新上架 LNG-M3XF4GE24：24 口 Gigabit L3 管理工业 PoE+ + 4×10G SFP+ = 137,900 TL**（r18 档案无此型号）→ 工业 L3 线上探企业级价格带
- 既有锚点：5 口 750 TL 不变；新光模块锚点：SFP-10G-SR 4,788 / GLC-LH-SM-LL 1,088 / QSFP-40G-LR4 12,600 TL → 行 20 已录入

### 13.5 Keenetic Türkiye 零售落地（2026-10-21）
- 2026-05-14 官宣（blog.keenetic.com.tr + Technopat/TechnoLogic/bthaber）→ **6 月分阶段上市已执行**
- 现价：**KN-4610-01-EU 5 口 PoE+ 60W = 1,599-1,849 TL**（Amazon 19 评 4.6★）/ **KN-4710-01-EU 9 口 PoE+ 120W = 2,909-3,349 TL**；akakce 5 口款 **30 个卖家**（1,599-3,398）
- 仅 unmanaged，**managed/工业线未触及** → 行 9 已录入；「12 个月观察」维持（是否上 managed = 关键信号）

### 13.6 Angora 本体复核（2026-10-21）
- 官网新闻栏 **停更于 2023-12-05**（产品方案公告，细节按常设规则不展开）→ 已 32 个月；2026 年新品/渠道/高管公开信息 = **0 条**（全量搜索仅回 2021-2024 旧新闻）
- VERGE 家族页复核：8/24/32/48 固定 GE + 2-4×10G SFP+，PoE+ ≤30W/口；DC/TOR 款 48×1G/10G/25G + **6×100G QSFP28 / 3.6Tbps**（与 T 档案一致）；工业 8 口 -40/+80°C 48V DC
- LinkedIn 2,110 followers（静态）；RocketReach 10 人；ZoomInfo 收入 <$5M
- **结论**：公开面继续沉寂，「渠道窄、低可见度」既有判断维持；官网停更 = 弱负面信号（营销资源投向线下直销/渠道）

### 13.7 待核项清理（2 解决 + 1 部分解决）
- ⭐ **Opax（111 行 20，r19 唯一客户侧待核）= 解决**：opax.com 法律条款页 = 「Opax Mühendislik Kamera Alarm ve Güvenlik Sistemleri ... Pazarlama Limited Şirketi」，地址 **Yeni Mah. Diriliş Blv. No:3, Opax Plaza, 50100 Merkez/NEVŞEHİR**，+90 850 259 12 12；**B2C 直销 + B2B 代理双轨**（官网发布代理商协议全文）；OPAX-08120W 实价 $35（1,623.30 TL）；**opax.pl = 另一波兰域，与土耳其主体无任何书面关联**
- ⭐ **Fiberix（r20 #66 排除项复核）= 确认排除**：fiberix.com.tr = **面向个人的光纤 ISP**（无限套餐 519-619 TL / 20-100 Mbps、自有基础设施、账单/速度测试/WhatsApp 客服）→ 非 switch 贸易实体；「广州现有伙伴」说法现网站无佐证
- **Duzgun Toptan ↔ Toptansarf（111 行 43）= 部分解决**：toptansarf.com / .com.tr 在运营 = 「TOPTANSARF BİLGİSAYAR VE GÜVENLİK SİSTEMLERİ」（Hürriyet Mah. Sedef Sk. No:5/A **Bahçelievler/İstanbul**；0212 580 25 25 / +90 541 660 10 66；「10 YILDIR BAYİLERİN ÇÖZÜM ORTAĞI」B2B 批发 1000+ SKU，目录含 Ruijie Reyee RG-RAP2200F PoE AP）；**teksarf.com 当前 HTTP 500（站点宕机）**；Duzgun（gmail 联系）同一主体 = 高概率，待 WhatsApp 实联确认
- NetGaste（疑似软文）/ ONSİS $28.2M（datanyze）/ Longline 成立年（2000 双源互证）：本轮无新证据，维持既有结论

### 13.8 数据边界（第 23 轮）
- rehbersanayi `?page=N` = JS 分页（参数被忽略）→ 盲区 10-01→10-08 无法覆盖；EKAP 官方站仍需 JS
- ewindnet.com / pnetworks.com.tr fetch 间歇失败（OSS 代理错）→ 数据 = web_search 摘要（价格项逐条双源核对）
- hepsiburada Longline 店铺抓前 2 chunks（switch + 光模块段完整，配件段截断）
- teknolojipazar（r19 排除）与 Duzgun（r20 收录）确认为两个不同主体，无混淆


## 十四、第 24 轮更新：Ewind 官网全量爬取入库（2026-10-21）

> 完整档案 = `06-competitors/112-ewind-website-mirror-2026-10-21.md`（公司面 + 站点结构 + 六大产品线 90+ SKU 规格表 + 2026 时间线 + 竞争情报解读 + 数据边界）。

### 14.1 抓取方式与边界
- ewindnet.com 直连 fetch **3 次全失败**（OSS InvalidAccessKeyId，本域名持续不可达）→ 改用 **`site:ewindnet.com` 索引爬取 workflow**（6 轮定向检索：PoE/unmanaged/industrial/2.5G-10G/光猫/ODM + 公司面，索引快照含完整规格表；pageAge = Google 抓取时间 2024-03~2026-07-22）
- 官网 = B2B 询价，0 价格（土耳其零售锚点 = atommarket 7 款，行 15 r23）；类目 SKU 总数部分可得（10G Managed PoE = 17 / Unmanaged 100M-1000M = 15）

### 14.2 公司面要点（此前档案未覆盖的增量）
- **总投资 $50.67M / 厂房 5000+ ㎡ / 500+ 员工 / 车间 3000+ ㎡ / 20 台 SMT + 4 条组装线**（OEM 页自述）；National High-tech Enterprise；RU 站口径"2017 年起"
- 联系 = +86 755-2100 6440（24h）/ info@ewindnet.com；多语言 **en/ru/zh-cn/es/no**（北欧站）
- 出口 100+ 国；展会 = **CPSE 2025**（深圳 1A16）；标杆案例 = **四川省公安厅**（政府级，2025-08）+ Wansheng Academy（2026-05）
- OEM/ODM 明牌：软硬件定制 / IP66/68 受管工业 PoE / FOB/CIF/EXW/FCA / **交付 4-6 周（常规 4 周）**

### 14.3 ⭐ 产品线增量（对 110 行 15 既有口径的扩展）
- **Cloud/AI PoE 新线（2025-26）**：ES2010CF-AP（4-24 口 100M 云 PoE 65-300W）/ ES3006CG-AP（4 口 65W）/ ES3028CG-AP（24 口 400W）/ 2026-05-27 与 07-22 两款 **Cloud-Managed AI PoE** 新页 / EPIS3910-8GE 工业云管理（DIP 12/24V 被动 PoE + 60W 口）；平台 = **EwindCloud**（ONVIF 发现 + 云拓扑图 + 单端口重启 + OTA）
- **2.5G/10G 扩品**：S6805F/6806/6809/6818/6826（5/4/8/16/24 口 2.5G ladder，160Gbps 顶配）+ **10G Managed PoE 类目 17 SKU**（含 S53928QM = 24×10G+4×100G L3）+ W-S2910SM-DP（**W- 前缀新系列**，8GE PoE+2×2.5G 轻管理，2026-06-25）
- **核心线**：S3936GM(-AP) = 8×GE+24×GE SFP+4×1/2.5/10G，598Gbps，**Microchip (Vitesse) 芯片**（2026-04-29 官方）；L3+ 线 S5954GM-AP = OSPF v2/VRRP 动态路由
- **OEM 定制实锤（EW-S1810CF-AP）**：拨码 **E = AI Extend 300m（单口 10Mbps 长距）/ V = 口隔离 & VLAN / D = AI-PoE 自愈（PoE Watchdog 相机掉线自动重启）** → 与 Longline（Extend 250m + Watchdog）= 同一卖点集
- 工业线 15+ 款（IP40/66/68，-40~85°C，双电，5 年）：含 PIS5728GM-AP-BT(VTS) **28 口 800W L3 BT** / PIS6812M-8GE-BT（2×2.5G SFP）/ PIS5712M-8GE（128Gbps）
- 光猫 9 款（含 2U 16 槽机箱 EF16-D220 / 10G 光猫 / PoE 光猫）+ 注入器/分离器 16 款（含 BT 60W/90W 类目、Type-C 分离器线）

### 14.4 竞争含义（对我方）
1. 全产品线正面对撞 + 土耳其双轨（atommarket 品牌零售 + HITIT 白牌，既有口径确认）
2. **300m 长距 + Watchdog = 全市场公共卖点**（Ewind/Longline/我方）→ 我方差异化 = Marvell 芯片代差 + 现货交期（对方 4-6 周）+ 830 RMB 价格地板
3. Ewind 自身 = 多芯片 ODM（Vitesse 线 vs Angora 的 Broadcom/SONiC 线）→ spec 对表可选任一线
4. 中国本土证据（四川省公安厅 + CPSE）= 国内竞争参照
5. 监控增量：EwindCloud 功能 / S68 系进 atommarket / W- 系列扩展 / WiFi 类目 / 10G PoE 余 5 SKU


## 十五、第 25 轮更新：Ewind 宣传面/全渠道爬取入库（2026-10-21）

> 完整档案 = `06-competitors/113-ewind-promo-full-presence-2026-10-21.md`（土耳其相关 + Alibaba 店铺价格 + 缺口补齐 + 官网类目计数 + WiFi 13 款 + 社媒矩阵 + 展会全录 + 公司细节 + 情报解读）。

### 15.1 方法
- 直连仍全 OSS 故障 → site: 索引 workflow 扩展 10 轮（ru 站/WiFi/B2B/Alibaba/缺口/社媒/FB/LinkedIn/展会/多语言）；覆盖 www + 12 语言子站（en/ru/zh/es/no/nl/ko/el/it/pt/fr/de）+ alibaba.com + linkedin + zoominfo + securex/essen 展会官网 + camsecurity.com.ua 分销页

### 15.2 ⭐ 土耳其相关
1. **官方案例「EWIND Successful Case in Malatya, Türkiye」**（12 语言站全同步，正文未入索引 → 监控）
2. **1Net Telekom ve İletişim**（BTK 持牌国家级电信运营商，Istanbul，20+ 年）总经理 **Uğur Konuk 在 LinkedIn 推广 Ewind 24 口 AI PoE** → 疑似土耳其渠道
3. 中国海关口径（Ewind blog 引用）：土耳其 = 中国 PoE 出口前十大市场

### 15.3 ⭐ Alibaba 宣传店铺（价格锚首建）
- 认证/排名：Verified Manufacturer + 工厂检验 + "#3 most popular in Network Switches" + 4.5-4.7/5 + ≤2-3h 响应 + 复购 11-14%；**270+ SKU**；Brand = **EWIND/OEM**；主要市场 = 美/伊/英/沙/菲/意/加/利
- 价格阶梯：**$21.55**（8 口 100M PoE）→ $23.5-26 → $29.96 → $33.85（4 口 65W 云）→ $39.15（bt）→ $75 → $75.4-80（PIS1712-8FE）→ **$111-115**（S1820CG-AP 20 口 300W）→ 24 口被动 PoE 250m+Watchdog 主推
- 我方对照：830 RMB（≈$115）地板 = 对标其 20 口档；$21.55 ≈ 155 RMB = 其低端锚

### 15.4 补齐 + 新增
- 缺口补：IS3814M（14 口受管工业）/ PSE101G-DC-60/90（BT 注入器）/ S1820CG-AP（= 20 口，300W）/ S1508CF / S1906FG-DP / S1906CFG-DP / S1806CF-AP（EVD 拨码）/ PIS3814M-8GE（240W）/ PIS3606M-4GE(-NB) / PIS3806M-4GE-BT / PIS3610M-8GE-BT / 2936GM-8GF-AP（400W）/ DP120W-52 / PI120W-48/240W-48/480W-48（工业电源）/ 95W BT 线
- 官网类目计数：Ethernet Switch 63 / PoE Injector 25 / Accessory 64 / IP66-68 IND 2 / Bypass 1 / 跳线 8 = 27 分页
- **WiFi 13 款**：CPE×4（CPE601/602/610/616）/ 路由 EW321/1200/3000/**1800（BCM6755）**/3600（WiFi7）/290 / AP×6（**WiFi7 9G 三频 = Qualcomm IPQ5322** / AX3000 / **EW-API210 IP65 户外 2.5G 48V PoE**〔2026-06-26〕）
- 社媒：FB 主页 + **EU-US 专页**（Maggie Lin）+ 总页（印尼 K-Town 案例）；LinkedIn（Arya Li：S5736GM #Vitess / COMPUTEX 2026 / **OSPF-BGP-VXLAN 核心叙事**）；ZoomInfo（**Jarvis Xie MD / Kathy Chiang / Arya Le**，51-200 人）
- 展会 10+ 场全录（2013 南非 → 2026 台北 COMPUTEX K1421；每年 20+ 场）；公司细节：5 条电话线 / 3 邮箱 / 办公室 2 址 + 工厂 2 址（松白 + 宝安）

### 15.5 竞争含义
1. 土耳其四轨渗透确认：atommarket 零售 + HITIT 白牌 + 1Net 疑似渠道 + Malatya 工程案例
2. 价格锚首建 → 我方报价对照表基础（830 RMB ≈ 其 20 口档 $111-115）
3. 24 口被动 PoE 250m = 其标准卖点（我方 300m 领先 50m）
4. 12 语言本地化但无土耳其专页/专售 → 可攻点
5. 查 Ewind 任何型号先查 Alibaba 店铺（270+ SKU 全集）


## 十六、第 26 轮更新：Ewind 爬取最终闭合（2026-10-21）

> 详情 = `06-competitors/113-ewind-promo-full-presence-2026-10-21.md` §11。

- 直连 ewindnet.com 第 4 次测试仍 OSS InvalidAccessKeyId → 索引快照 = 唯一通道（结论不变）
- 10G Managed PoE 类目（17 SKU）≈ 全量闭合：新增 **S53952QM**（48×10G+4×100G，1760Gbps）/ **S57948QM**（48×2.5/5GE+4×100G，1280Gbps，MAC 112K = 5GE 接入新线）/ S2828GM-AP / **S5728GM-AP(-AT)**（L3 完整规格，400/600W）/ S2854GM-AP（800W 216Gbps）/ ⭐ **S5954GM-AP(RTL) = Realtek 芯片版本**（→ 商用 L3 芯片源 = Microchip (Vitesse) + Realtek 双方案）/ S53928QM 完整规格
- Unmanaged 类目 15 款全量闭合（S1505 系 1 年质保 / S1605 系 2 年 / CGU 金属壳 4 型号 + 版本化 Datasheet V11.19.2025-V19.11.2025）
- 工业新增：**PIS5736GM-8GF-AP-BT(VTS)** 36 口 800W L3（24 GE + 8 GF + 4×10G，af/at/bt）
- **最终完整性结论（对用户问题的回答）**：信息层面 ≈95%+ 已爬完；5 项硬边界 = ① Malatya 案例正文 ② Alibaba 270+ SKU 逐个 ③ FB/LinkedIn 正文 ④ 官网 PDF/图片（需直连恢复）⑤ 动态内容（价格/新功能 = 监控项）

## 十七、第 33 轮更新：Kyland（东土科技）新入 + Netaş 语料增量（2026-10-21）

> 背景 = 用户 r33 指令「所有出现的公司名/网站/公司讨论/合作商合作事宜都挖出来入库」。全量 verbatim 见 `99-raw/r33-partner-company-mining-2026-10-21.md`；伙伴体系全图见 `09-orders/126-angora-partner-bidding-map-2026-10-21.md`。

1. **新增 行 89 = Kyland（北京东土科技股份有限公司，创业板 300353）**：
   - 来源 = 2025-04-09 铁路项目：终端客户 kitlist 原单 = Kyland 品牌（需 OT 协议，「except OTT」）→ 我方硬件软件均不对口未入（L3903-3920）；2025-04-25 Levent：「we now find a reliable channel for Kyland products / this channel also supplier original Moxa products / **Kyland and Moxa sometimes come up in railways projects**. I will check with partner」（L4010-4019）
   - 外网取证（2026-10-21）：创业板上市；EPA 标准（IEC61158）起草者 + IEC62439 拥有者 + 65+ 专利；350+ 员工（R&D 115）；认证 KEMA（电力中国首家）/UL508/DNV/IRIS（铁路）/铁路电务认证/GJB
   - 产品线：KIEN（工业）/**Aquam（铁路 EN50155/50121/45545，IP65，M12，Bypass 继电器）**/SICOM（变电站）/KD5886（128G/152G）/**KD3004（自主 4 口千兆 PHY 芯片）**
   - 应用版图 = 京津高铁信号、武广高铁供电、青藏铁路、杭州湾大桥、北京奥运配网、美国/哥伦比亚/西班牙项目 → 全球铁路市场玩家
   - 对我方 = 铁路/工业细分正面竞争（同为中国品牌）；投标动作 = 先核 kitlist 是否 Kyland/Moxa/Hirschmann，再按 OT 协议/端口密度缺口定位
2. **Netaş（行 2）增量**：2026-03-09 语料 —— ① **Netaş 从我方买过 3 台样品（项目已死）**（Simon verbatim：「they bought 3 samples from us but sad thing is, the project is dead」）② Levent：「No worries about the NETAS. They are looking for a **Moxa or Hirschmann replacement**」= 工业设备替换机会（L7821-7830/7848）
3. **关联增量（登记于 126 号档案，不入本表）**：Elips Elektronik（⚠️ Angora 竞标+资本伙伴，非交换机品牌，故不入 110）/ UDE（我方 RJ45 供应商，供应链不入 110）/ Rima Elektronik（我方客户清单，111 行 13 已更新）

## 十八、第 34 轮更新：生态公司全站爬取入库（2026-10-21）

> 用户指令=「语料所有公司网站全部爬取入库 + 合作关系/结构多角度深挖 + 尤其 Larch Networks」。主档案=`06-competitors/127-angora-ecosystem-companies-crawl-2026-10-21.md`；verbatim=`99-raw/r34-ecosystem-crawl-2026-10-21.md`；Larch 深度=41 号 §10。

1. **新增 行 90-98（9 行，三件套已同步）**：
   - **行 90 D-Link**：2026-09-11 发布 **DIS-110G 工业交换机组合**=正面进入工业线（撞我方工业线+EGM 工业标场景）；语料 26 命中（原 grep=1 系大小写误低，-i 复核修正）；$135 伙伴价锚既有
   - **行 91 Dahua**：数通产品类（交换机+光模块）在册；⭐**已赢标**（L9275-77）+捆绑策略（L8805 用 switch 压 camera 价）；CIIF 2026 上海
   - **行 92 Moxa**：RKS-G4030-PL（30 口模块 PoE++720W）/EcoVadis 金 2026；铁路共现（L4015/4019）+**Netaş 替换目标（L7848）=直接机会**
   - **行 93 Hirschmann (Belden)**：Belden 旗下（5G-ACIA/EtherCAT/SPE/TIA 成员）；Netaş 替换目标（L7848）；hirschmann.com 不可达（Belden 根页代偿）
   - **行 94 H3C**：定位基准（L10381「position like Maipu, H3C」）；Gartner 虚拟化 MQ Visionary；S12500X-AF
   - **行 95 Maipu 迈普**：运营商级全线（GPON/防火墙/光模块/HCI）；⭐partner 对标竞标对手（L2191/2201）；2026 中东展会（LEAP 沙特）在土辐射
   - **行 96 TronX**：⭐**姊妹品牌定性闭环**（L4290/4314/4471 同厂 ODM 双品牌+logo 源文件）；TT 项目线=Elips 资本/TronX 品牌（126 号）
   - **行 97 cryptoink**：88 台死单后 OEM 线（L10362）；站不可达×3=休眠（状态入库）
   - **行 98 Larch Networks**：⭐最高优先深挖（41 号 §10）；同 Marvell 98DX 平台（语料「AC5/AC3」=其平台命名）；⭐2025-11-02 加入 SONiC Foundation；OCP 2026 B31=TeraLynx10+Hardened SONiC+ConnectX-7+Dorado Cruz；新 BD 联系人=Irina Murzina
2. **不入表（定性后归他档）**：Taylan=人（Angora CTO）/ Karen=人（NEM Engineering）/ Elips=竞标伙伴（126 号，实体名 r34 坐实=ELİPS ELEKTRONİK SAN. VE TİC. LTD. ŞTİ，1990-10-03）/ Sagatele=我方 ODM 工厂（127 号 §4）/ UDE=我方 RJ45 供应商（TPEX:3689，L2698）/ NEM Engineering=SFP 供应商（nemengine.com）/ Connexite=英国客户（Amazon Business，L5813，非土仅存档）/ Rima=111 行 13（r33 结案）/ Centec/Marvell=芯片层（127 号 §1-§3）/ PNetworks=行 1 既有（AA 2021 发布会增量记 127 号）/ Keenetic=行 9 既有（2026-05 卖 switch 增量记 127 号）
3. **关系结构总图（各角度）**=127 号 §1：芯片层（Marvell/CENTEC/Realtek/NVIDIA X2）→工厂层（Sagatele 我方 / Larch 白盒+软件 / Maipu / H3C）→品牌层（Angora⋈TronX 姊妹 / PNetworks 唯一 yerli / Elips 资本）→客户层（TT/Netaş/Rima/Connexite）→供应链（UDE RJ45 / NEM SFP / cryptoink 死线）
4. **对我方三句话**：① 我方产品线=Sagatele（深圳）OEM+Marvell Prestera/CENTEC 芯片（语料 L2368「All based on Saga products」100% 证据），公开目录=其官网（谈判口径注意）② Larch=同芯片上游（平台成熟度话术来源），2026 重心 AI 以太网远离我方主战场，TT 大客户方案层会出现 ③ Netaş 替换线（Moxa/Hirschmann）=最近期直接机会；D-Link DIS-110G=工业线新压力源

## 十九、第 35 轮更新：深挖八线入库（2026-10-21，只增）

### 19.1 行 1 PNetworks（=Pavo Group 品牌，站恢复可达）
产品线升级=AI/ML + Cloud DC + Operator + Optics；CEO=Bilal Yıldız；**2026-07-30 土耳其主权基金 TWIF CFO&COO Dr. Mahmut Kayacık 会 Pavo CEO**（TWIF=Elips 客户→Elips 与 PNetworks 双线接触主权基金）；2026-08-27 Republikorp（印尼 Norman Joesoef）土-印尼防务；IG/LI=pnetworkstr、X=@Pnetworks_；pavo-group.com=伙伴入口。
### 19.2 行 9 Keenetic（keenetic.com.tr/en 产品矩阵）
KN-1013 Hero BE3600+10G SFP+ / KN-4210 TITAN SE BE7200 / KN-5210 Roamer 5G / KN-4110/4010/2013/3611/2113/1812/3910/1012/3811 / **⭐Stellar 6 KAP-650=IP65 PoE+ -40~+65℃ 户外 AP（线内唯一 rugged）** / KAP 530；KeeneticOS 云 demo=keenetic.demo.keenetic.pro；switch 线未变（unmanaged 零售，§18 锚点维持）。
### 19.3 行 90 D-Link（DIS-110G 规格落地）
DIS-110G-05/-06P/-10/-10P 全**非网管**工业 GbE：IP40 无风扇，-40~+75℃，6kV 全铜口，250m@10M 长距，PoE+ 30W（预算 240W 与 120W），**PD Alive 自动重启**，DIP Fast Ring，双 DC，802.3az → 定位=监控/楼宇/标牌低端入口（2026-09-11 Taipei press）；与 Sagatele STI-21616GP（16 口户外 PoE+ 非网管 6KV）同带正撞。
### 19.4 行 98 Larch（41 §10.8-10.11 同源）
Ironman 工业模块线 5 型号（50/72/86/110/126G，TSN/HSR/256b MACsec/级联 1K，datasheet 2026-06=新品）；Hardened SONiC 工业可选 G.8032 ERPS+PTP 1588+ITU-T G.8273；**⭐SKD/CKD 本地化生产官方计划**（Step1 建业务→Step2 SKD 含 PCBA→Step3 CKD PCB+SMT+全部元件）=Larch 官方「yerli 化」路径；生态=Xsight Labs CoE（X-Series AI switch+E-Series 800G SDN DPU）+SIDERA（UAE 本地化品牌，与 Larch 共建）+SERA（100/400/800G DC，COMPUTEX 2026）+Miyagi（远程管理 NOS）；未具名「major global brand」ToR SONiC 盒式 green DC 评估中（productizing SONiC 文）；Network World 2026-10-21 点名 OLS 代表厂商。
### 19.5 本轮结论
① PNetworks=主权基金背书+集团化转型（威胁上调一档，「唯一 yerli」叙事资源更强）；② D-Link 工业入口=非网管低端，与我方 managed 工业线错位（价格锚意义>直接竞对）；③ Larch SKD/CKD=我方 yerli 路径第二选项（Sagatele 深圳 ODM 之外）；④ Connexite Ltd=Angora 创始团队英国实体（123 号 r35 补，非外部竞对）。

## 二十、第 36 轮增量：既有行备注（2026-10-21，只增）

- **Netaş（行 2）**：2024 年报（2025-03-11 发布）=与 ZTE 合作 **800GE ethernet 测试**（单载波 800G 无再生 2,000 km 传输，2026-02 完成，世界纪录叙事）+ SAHA EXPO 2024（50 周年）+ Orhanlı 生产基地（donanım 生产）+ taktik saha/gemi haberleşme çözümleri → 高速网络需求侧铁证；与既有「Levent 2026-03-09 找 Moxa/Hirschmann 替代」机会并列。
- **Longline（行 20）**：营销扩张实锤=NetGaste 2025-10-14「Endüstriyel Switch Seçimine İlişkin Kapsamlı Bir Kılavuz」软广（Longline 段）+ Teknoblog 2026-02-05「2026 指南」软广（Longline Switch Ailesi 段）→ r19「疑似 Longline 软广」坐实在投；对我方打法影响=软广饱和市场，我方维持成本+捆绑策略不变。
- 本轮 110 无新增行；新潜客 4 行入 **111 管线（行 52-55）**（upTech/WINET/TGD/ULAK）。

## 二十一、第 37 轮增量：双品牌母公司坐实（2026-10-25，只增）

来源：用户 main 上传 `AI客户评估_TR 10.06.xlsx`（50 家双 AI 评估）+ `Turkey Client List.xlsx`（299 家）+ `2025土耳其ISAF客户.xlsx`（展会现场名单）。
- **行 1 PNetworks（=Pavo Group）**：⭐集团矩阵坐实——TCL #5 pavotek.com.tr=**Pavo Group 电子/嵌入式子公司**（pavotek.com.tr 导航全链 pavo-group.com；Avionics/通信网络控制/电源/IoT/智能能源/测试；TWIF 2026-07-30 CFO 会见+Republikorp 2026-08-27 同批新闻流）→ **Pavo 矩阵=网络 PNetworks（本行）+电子 PavoTek（111 行 59 战略留档，非客户）**；「唯一 yerli」叙事再加固一档。
- **行 20 Longline**：⭐**Entegron=LONGLINE 自有中国 OEM 品牌**（用户 master #44 双评估 30A/45A，Claude 母公司 LONGLINE Technology Ltd 2000 起 Bayrampaşa；TCL #60）：Entegron 线在售 Ethernet 11/**PoE 31**/EPON ONU 9/GPON ONU 6（L2 8/16/24/28 口+10G 8G+4SFP）；兴趣=PON switch/PoE/商业 PoE（有 E-wind）；YouTube「Entegron」Cahit Terzioğlu 疑似 owner 关联 → 行 20 双入口打法（LONGLINE 渠道+Entegron OEM）见 112 号 Tier1。
- 本轮 110 无新增行；111 管线本轮 +90 行（24 用户名单新客 56-79 + ISAF 展会 66 行 80-145），总 145 行。
