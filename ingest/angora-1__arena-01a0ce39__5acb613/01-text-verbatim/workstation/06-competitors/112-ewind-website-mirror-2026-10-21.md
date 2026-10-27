# Ewind 官网全量爬取档案（2026-10-21，第 24 轮）

> **[r39 补注 · 2026-10-27 · 只增不删]** 正文"本域名持续不可达"的陈述**已过期**：第 39 轮 `fetch_page` 直连 ewindnet.com **全部成功**（首页 / sitemap 索引 / 产品·页面·展会 sitemap / WP REST `product`+`posts` / 两个产品页）。本轮结果见 `ingest/angora-1__arena-01a0ce39__5acb613/06-web-crawl-2026-10-27/`（16 文件）：**站点自 2026-10-21 基线以来零新增**（最新产品 `modified` 2026-08-07、最新文章 2026-06-11、展会 sitemap 停 2025-11-05）；首次拿到 EW-S57948QM 与 EW-S1710FG-AP 的完整规格表、153 个 SKU 与 125 篇文章的逐条日期。另更正：产品 URL 必须带 `-1` 尾缀，裸 slug 404 是我方拼法错误。


> 任务来源：用户第 24 轮指令「你把Ewind网站爬下来入库吧 必要时开workflow去爬」
> **抓取方法（workflow）**：ewindnet.com 直连 fetch 3 次全失败（OSS InvalidAccessKeyId 代理路由故障，本域名持续不可达）→ 改用 **web_search `site:ewindnet.com` 索引爬取 workflow**：6 轮定向检索（产品 PoE/unmanaged/industrial/2.5G-10G/media converter/ODM + 新闻/公司面），每轮返回带**完整规格表**的索引快照（pageAge = Google 抓取时间）。另含 r23 已抓的官方新闻页 snippet。
> **数据边界（如实）**：① 官网 = B2B 询价模式，**不列价格**（价格锚点见 atommarket 土耳其零售，r23 已录 110 行 15）② 部分型号仅得摘要规格（未达整页规格表）③ 类目 SKU 总数：10G Managed PoE 类目 = 17 款（索引页"Showing 1–12 of 17"）、100M/1000M Unmanaged 类目 = 15 款（"1–12 of 15"），其余类目总数未穷举 ④ WiFi 类目在导航中存在但本轮未展开（0 产品快照）。
> **对应实体**：Shenzhen Ewind Technology Co., Ltd（深圳）= 110 行 15 = Angora 头号供应商 + 我方直接竞对（同源 ODM 池）。

---

## 一、公司面（官网首页/OEM 页/RU 站/新闻页）

| 项 | 内容 | 来源 |
|---|---|---|
| 主体 | **Shenzhen Ewind Technology Co., Ltd**（深圳市伊威德科技） | 首页 |
| 定位 | "dedicated in communication Security field for over 7+ years"；**National High-tech Enterprise**（国家高新技术企业）；集 R&D/制造/营销/服务一体 | 首页 |
| 投入 | **总投资 5,067 万美元（50.67M USD）**；**厂房 5,000+ ㎡** | 首页 |
| 产能 | **500+ 员工**；**车间 3,000+ ㎡**；**20 台 SMT**；4 条常规组装线 + 2 条备用 | OEM/ODM 页 |
| 历史口径 | RU 站："**自 2017 年起**中国智能网络通信行业领先制造商"；另有"5+ 年 OEM 经验"旧文案 | ru.ewindnet.com / blog |
| 联系 | **+86 755-2100 6440**（24h 热线）；info@ewindnet.com | 站脚 |
| 多语言 | **en / ru / zh-cn / es / no**（挪威语站 = 北欧市场投入） | 各子域 |
| 出口 | "exporting to **more than 100 countries**"（欧洲/北美/东南亚点名） | 新闻页 |
| 展会 | **CPSE 2025**（深圳，10-28~31，Hall 1 1A16 展位）；CPSE 2023（r19 已录 Koza=GreenTech 同场口径无关） | 新闻 2025-09-16 |
| 标杆客户案例 | **四川省公安厅**（政府级公安网，2025-08-13 官宣）；Wansheng Academy 住宅安防网（2026-05-20 项目案例） | 新闻页 |
| 定制能力 | 软硬件定制 / **OEM/ODM** / FOB/CIF/EXW/FCA / IP66/68 受管工业 PoE 定制 | OEM 页 |
| 交付期 | OEM/ODM 订单：Pink Equine 4-6 周，**其余产品 4 周** | 产品页脚注 |
| 质保口径 | 商用 2-3 年（10G 线 3 年）/ 工业 5 年 / 光模块 3 年 | 各产品页 |

## 二、站点结构（导航树，首页快照 2025-08-13 + OEM 页）

```
Home
├── Product
│   ├── Commercal PoE Switch〔拼写原样〕
│   │   ├── 100M POE Switch          ├── 1000M POE Switch
│   │   ├── 2.5G/10G Managed PoE Switch（含 10G Managed PoE = 17 SKU 类目）
│   │   └── Cloud PoE Switch / Hi-PoE Switch（2025-26 新类目）
│   ├── Industrial PoE Switch（100m/1000m 工业 PoE；IP66/68 Managed IND PoE）
│   ├── Ethernet Switch
│   │   ├── Desktop Switch / 1000M Fiber Switch
│   │   ├── Managed Ethernet Switch（L2+）
│   │   ├── Industrial Ethernet Switch（1000M 工业）
│   │   └── 2.5G/10G Ethernet Switch
│   ├── PoE Injector（DC / 100M / 1000M / BT 60W / BT 90W）
│   ├── Accessory
│   │   ├── Media Converter（100M / 1000M）+ PoE Splitter（100M/1000M，含分页）
│   │   └── POE Media Converter
│   └── WiFi（新类目，本轮未展开）
├── Solutions：Smart Grid / Rail transit（+ 新闻面：Smart Security / 工业自动化 / 企业网）
├── OEM/ODM
├── News（Product news / Project Case / blog）
├── Company-culture / History-Achievements
└── 语言：en / ru / zh-cn / es / no
```

## 三、产品目录（按线，型号 + 核心规格）

### A. 商用受管（L2+/L3，Enterprise/Campus/核心）
| 型号 | 规格（索引快照） |
|---|---|
| **EW-S3936GM** | ⭐ 36 口 L2+ 汇聚/核心：**8×GE RJ45 + 24×GE SFP + 4×1/2.5/10G SFP+**；**598Gbps / 107.14Mpps / MAC 32K / 缓冲 32M / 整机 <15W**；3 年质保；**芯片 = Microchip（Vitesse）**（2026-04-29 官方产品新闻；Web GUI/CLI/SNMP；802.1Q/QoS/LACP/镜像/IGMP/STP-RSTP-MSTP/ACL L2-L4）；Datasheet V1.4 |
| **EW-S3936GM-AP** | 上行 PoE 版：**8×1000M RJ45 PoE + 24×GE SFP + 4×10G SFP+**（10G Managed PoE 类目） |
| **EW-S5736GM-AP** | 36 口 L3 PoE：8×GE PoE + 24×GE SFP + 4×10G SFP+ |
| EW-S2928GM | 28 口 L2+：24×GE + 4×1G/2.5G/10G SFP+；RS232 console |
| EW-S2926GM-AP | 26 口 L2 受管 PoE：24×GE PoE + 4×1000M combo SFP + 2×SFP；3 年 |
| EW-S2948GM-AP | 52 口 L2 PoE：48×GE PoE + 4×10G SFP+ |
| EW-S2854GM / -AP | 54 口 L2+：48×GE(+PoE) + 6×10G SFP+；**128Gbps / MAC 32K**；3 年 |
| EW-S5748GM-AP | 52 口 L3 PoE：48×GE PoE + 4×10G SFP+ |
| EW-S5954GM-AP | 54 口 **L3+** PoE：48×GE PoE + 6×1/2.5/10G SFP+；**动态路由 RIP v1/v2 / OSPF v2 / VRRP**、IPv4/v6、PoE 口功率电流实时显示；1U 内置电源；3 年 |
| **EW-S53928QM** | **24×10G SFP+ 4×100G 口 L3 受管光纤交换机**（DC/汇聚档） |
| EW-S3910GM-AP | 10 口 L2+ PoE：8×GE PoE + 2×1G/2.5G/10G SFP+ |
| EW-S1950CG-AP | 48 口 GE PoE + 2×GE SFP（对比表出现） |
| EW-S1927CG-AP | 24 口 GE PoE：24×GE + 2×GE RJ45 + 1×GE SFP |

### B. 2.5G/10G 线（2025-26 扩张中）
| 型号 | 规格 |
|---|---|
| EW-S6805F | 5×2.5G RJ45 + 1×10G SFP+；60Gbps / MAC 4K；6KV 浪涌 / 8KV ESD；12V1A |
| EW-S6806 | 4×2.5G + 2×10G SFP+；60Gbps / 4K |
| EW-S6809 | 8×2.5G + 1×10G SFP+；60Gbps / 4K |
| EW-S6818 | 16×2.5G + 2×10G SFP+；**120Gbps / MAC 16K** |
| EW-S6826 | **24×2.5G + 2×10G SFP+**；**160Gbps / 16K MAC**；12V4A |
| W-S2910SM-DP | ⭐（2026-06-25 新页）**8×GE PoE + 2×1/2.5G SFP 轻管理**（W- 前缀新系列） |
| （类目）10G Managed PoE Switch | 17 SKU（含 S53928QM / S3936GM-AP / S5954GM-AP 等） |

### C. 商用非受管（CCTV/宿舍/办公）
EW-S1505（5×100M）/ EW-S1508（8×100M）/ EW-S1605（5×GE）/ EW-S1608（8×GE）/ **EW-S1608CGU（8×GE 金属 18Gbps <6W）/ EW-S1616CGU（16×GE 32Gbps）/ EW-S1624CGU（24×GE 金属 48Gbps，缓冲 4M，35.7Mpps，MAC 8K，<18W 内置电源）** / EW-S1650CG（48×GE + 2×GE SFP）/ EW-S1910G-DP（10 口：8×10/100M PoE + 2×GE RJ45；af/at）/ 20 口 400W 非受管 PoE（16×GE PoE + 2×GE + 2×SFP）/ 24 口非受管 PoE（24×GE + 2×GE + 2×SFP，内置 AC，1U 机架带耳，2 年，2026-04-27 更新）

### D. ⭐ Cloud/AI PoE 线（2025-26 新线，重点监控）
| 型号/条目 | 规格 |
|---|---|
| EW-ES2010CF-AP | 10 口 100M 云 PoE（4/8/16/24 口版本，65-300W）；**ONVIF 设备发现 + 云端 PD 拓扑图**；af/at 30W/口 |
| EW-ES3006CG-AP | 4 口 GE 云智能 PoE 65W（1×GE RJ45 + 1×GE SFP） |
| EW-ES3028CG-AP | **24 口 GE 云智能 PoE 400W**（2×GE RJ45 + 2×GE SFP）；3 年 |
| 24×FE PoE+2×GE+2×GF **Cloud-Managed AI PoE** | ⭐ 2026-07-22 新页（AI PoE） |
| 8×GE PoE+1×GE+1×GF **Cloud-Managed AI PoE** | ⭐ 2026-05-27 新页（AI PoE） |
| EW-EPIS3910-8GE | 云管理**工业** PoE：1-2 口 DIP 选 12V/24V 被动 PoE，3-6 口 48V 30W，7-8 口 48V **60W**；**EwindCloud APP/网页远程管理、单端口重启** |
| 平台 | **EwindCloud**：远程告警/故障检测/端口重启/OTA 升级/复位预留 |

### E. 工业线（IP40/IP66/68，DIN 轨，-40~85°C，DC12-48/48-57V 冗余双电，5 年质保）
| 型号 | 规格 |
|---|---|
| EW-IS1802 / EW-IS1804 | 2 口 / 4 口（2×GE+2×SFP）非受管工业 |
| EW-PIS1802-1GE | 1 口户外 PoE SFP（1×GE PoE + 1×SFP；48-57V；IP40） |
| EW-PIS1805-4GE | 4 口 PoE + SFP（4×GE PoE + 1×SFP；10Gbps 交换） |
| EW-PIS1810-8GE / EW-PIS1812-8GE | 8 口 PoE + 2×SFP（-8GE 纯电口上联 / -8GE 含 2×RJ45+2×SFP；**拨码 = 端口优先级**；2026-01-30 更新） |
| 10 口非受管工业 PoE | 8×GE + 2×GE RJ45 + 2×SFP（12V booster） |
| 5 口 10/100M 工业 PoE SC 光（户外，2024-08-22） | — |
| EW-PIS3610M-8GE | 10 口 L2+ 受管：8×GE PoE + 2×SFP；20Gbps / 8K MAC |
| EW-PIS3620M-16GE | 20 口 L2+ 受管：16×GE PoE + 4×SFP；**40Gbps / 16K MAC**（2026-04-16 更新） |
| EW-PIS3810M-8GE-BT | 8 口受管 **af/at/bt**：8×GE PoE + 2×SFP（95W 口径页） |
| EW-PIS5712M-8GE | 12 口：8×GE PoE + **4×10G SFP+**；128Gbps / 16K MAC；6 位端子 |
| EW-PIS6812M-8GE-BT | ⭐ 12 口：**8×GE PoE af/at/bt + 2×GE + 2×1000M SFP + 2×2.5G SFP**（2026-01-30） |
| EW-PIS5728GM-AP(VTS) | 28 口 L3：24×GE PoE + 4×10G SFP+；**400W；AC+DC 双电** |
| EW-PIS5728GM-AP-BT(VTS) | ⭐ 28 口 L3 **800W**：24×GE PoE af/at/bt + 4×1/2.5/10G SFP+ |
| 14 口受管工业 PoE+ 4 上联 SFP 802.3BT（2024-09-05） | — |
| 14 口全千兆受管工业（2024-09-05） | — |

### F. OEM/ODM 定制（我方直接对标项）
- **EW-S1810CF-AP（10 口 100M 定制 PoE）**：8×10/100M PoE + 2×10/100M；7-8 口 BT 60W/口；**拨码功能 = E（AI Extend 300m 单端口限速 10Mbps 长距 + 其余口 100m 内 100M）/ V（1-8 口隔离 & VLAN）/ D（AI-PoE 网络自愈 = PoE Watchdog，相机掉线自动重启，减少售后）**
- 交付：4-6 周（Pink Equine 款）/ 4 周（其余）
- 能力：IP66/68 受管工业 PoE 定制 / 软硬件定制 / 多语言包装

### G. 光模块/媒体转换器
| 型号 | 规格 |
|---|---|
| EW-610MM-2 / EW-610SM-20 | 10/100M 双纤 MM 2km / SM 20km |
| EW-610MM-2A/B / EW-610SM-20A/B | 100M 单纤 MM 2km / SM 20km |
| EW-810GM-2 | 10/100/1000M 双纤 2km |
| EW-810GS-20 / EW-810GS-20A&B | 1000M 单/双纤 SM 20km；**EF16-D220（16 槽）/ EF14-D220（14 槽）2U 机架机箱** |
| EW-810GS-3A/B | 1000M 单纤 3km |
| EW-P910-SFP | 1 口 1000M **PoE** 光猫（af/at 30W，36W 电源，3 年） |
| EW-10GSFP-SR | 10G 光猫（1×RJ45 10G/5G/2.5G/1G/100M + 1×SFP+；fabric 20Gbps） |

### H. PoE 注入器/分离器
- Injector：EW-PSE101G-AC（1000M AC af）/ -AF / **-AT（30W）** / **-60（60W bt，中跨 4/5,7/8 默认，末端 1/2,3/6 可定制）** / EW-PSE101F-AC（100M AC 24W 48V）/ EW-PSE101F-DC-AT（100M DC 12-32V）/ EW-PSE202G-DC-AF（1000M 双口 DC 44-57V）/ EW-PSE312CG（12 口 DC af）/ EW-PSE316CG（16 口 DC af）；类目另有 **BT 60W / BT 90W** 注入器
- Splitter：EW-PD111G-AF（1000M，15.4W，5V/12V 双出）/ EW-PD111F-AF（10/100M 15.4W）/ EW-PD111F-AT（10/100M 25.5W，兼容 1236 & 4578 供电）/ EW-PD101F-AF（100M 线 13W）/ EW-PD101F-AT-12（12V 2A 25.5W）/ EW-PD101F-AF-5S（5V 2.4A 12W "better chip"）/ EW-PD101F-TYPEC-5（**Type-C 转 RJ45** 线）

## 四、2026 新闻/产品页时间线（活跃度证据）

| 日期 | 事件 |
|---|---|
| 2026-01-30 | PIS1812-8GE / PIS6812M-8GE-BT 产品页更新 |
| 2026-04-16 | ES2010CF-AP / PIS3620M-16GE 页更新 |
| 2026-04-21 | **Industrial Cloud-Managed 系列**官宣（hybrid PoE / 12-24V 被动 / 802.3bt 90W / DIN / 宽压 / 长距） |
| 2026-04-27 | 24 口非受管 PoE 1U 页更新 |
| 2026-04-29 | ⭐ **EW-S3936GM 产品新闻 = Microchip (Vitesse) 芯片方案**（L2/L3 双能力，企业级） |
| 2026-05-20 | 项目案例：Wansheng Academy 住宅安防网 |
| 2026-05-22 | blog：Core Switch 解析（营销内容） |
| 2026-05-27 | ⭐ 8×GE Cloud-Managed **AI PoE** 新页 |
| 2026-06-11 | 品牌合作页（OEM/ODM + 100 国出口） |
| 2026-06-25 | ⭐ W-S2910SM-DP（8GE+2×2.5G 轻管理）新页 |
| 2026-07-22 | ⭐ 24×FE Cloud-Managed **AI PoE** 新页 |

→ 官网**持续活跃更新**（每月级节奏），2026 主线 = **Cloud/AI PoE 平台化 + 2.5G/10G 扩品 + Vitesse 芯片核心线**。

## 五、竞争情报解读（对我方 SmartByte/Marvell 线）

1. **全产品线正面对撞**：Ewind 5+1 线（工业 PoE/商用 PoE/非受管/2.5G-10G/光猫/注入分离 + WiFi）覆盖 Angora 全部场景 + 我方全部产品线；土耳其侧 = **atommarket 品牌零售（r23 七款锚点）+ HITIT 白牌（r4 海关证据）双轨**。
2. ⭐ **2026 两大动向**：① Cloud/AI PoE 平台化（EwindCloud APP + ONVIF 拓扑图 + 单端口重启 + 相机自愈 = 直接打"安防运维痛点"叙事，**与 Longline 的 PoE Watchdog/250m 长距为同一卖点集**）② 2.5G/10G 全 ladder 扩品（S68 系 5/4/8/16/24 口 + 10G Managed PoE 17 SKU + S53928QM 24×10G+4×100G L3）。
3. **300m 长距 + PoE Watchdog = 全市场公共营销点**（Ewind E/V/D 拨码 / Longline Extend 250m / 我方 2.5G 长距 PoE）→ 我方差异化不能只靠"长距"，要靠**芯片代差（Marvell Prestera L3）+ 交期（对方 4-6 周 vs 我方现货）+ 价格（830 RMB 地板）**。
4. **芯片源多元**：S3936GM = **Microchip (Vitesse)**（与 Angora 的 Edgecore/Broadcom+SONiC 不同源）→ Ewind 自身 = 多芯片方案 ODM（我方可对标其 Vitesse 线的 L3 功能集做 spec 对表）。
5. **中国本土市场证据**：四川省公安厅案例 + CPSE 展位 → Ewind 在中国国内安全/公安网有落地（对我方 = 潜在国内竞争参照，非土耳其战场）。
6. **对我方 OEM 渠道的威胁**：其 OEM 页明牌 4-6 周交付 + 500 员工 + 20 SMT + 100 国出口 → 土耳其白牌客户（111 管线 KARER/Cenova/OPAX 等）若比价，Ewind 是**与我方同一供应商池的直接对手**；我方优势 = 深圳本地交付 + 价格地板 + Marvell 叙事。
7. **监控增量（下轮）**：① EwindCloud 平台功能变化 ② S68 系 2.5G 线是否进 atommarket 土耳其零售 ③ W- 前缀新系列（W-S2910SM-DP）扩展 ④ WiFi 类目内容 ⑤ 10G Managed PoE 17 SKU 全量（本轮 12 可见）。

## 六、数据边界与缺口（如实）

- ewindnet.com 直连 = 3 次 fetch 全 OSS 代理故障（2026-10-21）；本档案 = **site: 索引快照 workflow**（6 轮检索 + r23 新闻页 snippet），pageAge 为 Google 抓取时间（2024-03 ~ 2026-07-22）
- 价格：官网 0 价格（B2B 询价）；土耳其零售锚点 = atommarket 7 款（r23，110 行 15）
- 未穷举：10G Managed PoE 类目余 5 SKU / 100M/1000M Unmanaged 类目余 3 SKU / PoE Injector BT 60W/90W 具体型号 / WiFi 类目 / SFP 光模块（非光猫）单品页
- 14 口受管工业（2024-09-05）/ 14 口 PoE+ 4 上联 BT 两款型号未捕获（仅标题级）
- 20-port 400W 非受管 PoE 型号未捕获（标题"16 20 port full gigabit poe switch with sfp uplink"，2025-03-18 页）
