# 第 23 轮原始档案：全量复核 + 新挖掘（2026-10-21，10-08 后 13 天窗口）

> 任务来源：用户第 23 轮指令「把你之前做的再过一次 看看有没有啥新发现 新的信息 / 继续挖掘angora的相关信息」
> 环境变化：⚠️ **沙箱重置**（workspace 回到基点 c4085aa、openpyxl 丢失）→ 按 TASK-STATUS §八 恢复流程 `git fetch origin arena/01a0ce39-angora && git reset --hard FETCH_HEAD`（HEAD=0dee834，359 文件 ✓）+ `pip install --break-system-packages openpyxl`（3.1.5）。
> ⭐ **fetch_page 代理恢复**（r19-r22 连续 4 轮 OSS InvalidAccessKeyId 全挂 → 本轮 rehbersanayi/hepsiburada/angoranetworks/fiberix/teksarf 直接可抓；ewindnet.com 与 pnetworks.com.tr 仍间歇失败 → 用 web_search 摘要补足）。

---

## §1 EKAP 新窗口扫描（rehbersanayi IT 行业归档，2026-10-21 抓取）

- 抓取对象：`rehbersanayi.com/ihale/arsiv/sektor/bilisim-ve-yazilim-teknolojileri` 第 1 页 60 条 = **2026-10-09 → 10-19**（与上轮窗口 09-28→10-06 之间存在 **10-01→10-08 盲区**，JS 分页未恢复，`?page=2` 参数确认仍被忽略）。
- **关键词扫描（Angora / PnetWorks / PAVO / Ewind / Longline / Mikrotik / switch / anahtar）：60 条 0 命中** → 新窗口内无 Angora/PNetworks 系中标。
- **110 在册公司新中标 6 起**（İKN 均可在 rehbersanayi 逐条验真）：

| # | 公司（110 行号） | 中标内容 | 金额 | 投标数 | İKN | 公告日 |
|---|---|---|---|---|---|---|
| 1 | **Pantech Teknoloji**（70） | Sunucu Temini（服务器供应） | **132.5M TL** | **1** | 2026/1708449 | 10-19 |
| 2 | **Fonet Bilgi Teknolojileri**（63） | SBYS-HBYS + YBYS 医疗信息系统（Batman） | **137.7M TL** | 2 | 2026/1214002 | 10-15 |
| 3 | **Artı ve Artı**（64） | 牙医医院服务器+存储+**网络设备**（Bursa Emek 150 床位） | **9M TL** | **1** | 2026/1479835 | 10-12 |
| 4 | **NETCAD Yazılım**（73） | CAD/GIS 软件更新 + 新模块（两单） | 5.2M+5.3M TL | 1+1 | 2026/1702069+2026/1667628 | 10-16/15 |
| 5 | **Itech Bilgi Teknoloji**（74） | E-Tır 系统集成与软件开发（Ankara） | 3.2M TL | 1 | 2026/1798180 | 10-16 |
| 6 | **Gruptechs**（76） | Microsoft 1 年软件许可（Kastamonu） | 1M TL | 3 | 2026/1712577 | 10-13 |

- 新窗口其他大额 SI（未入 110，仅留档观察）：Proday Bilişim（Ankara，网络安保维护 15.3M + 350 台平板 4.1M 两连中）、Fonet 之外的医疗 SI（Sisoft/ATM Sağlık）、Cyberwise（攻击模拟 11.9M）、Trust（沙箱 6.3M）、Enfo（文档扫描 2.7M）、Wıdetech（6 部分软件许可 3.1M）、Alfa Trend（Palo Alto 许可 3.2M）、İfoks（防火墙 3.4M）、CSIT Bilişim（存储 9.8M）、Karel Elektronik（PBX 3.1M）。
- **Trabzon Büyükşehir İKN 2026/1272126（PNetworks 全栈对口单）结果仍不可见**：开标 08-05，结果应落在 10-01→10-08 盲区窗口内；web_search 仅回索引到招标公告（61saat.com 07-11）。维持「结果未验证」，下轮若 rehbersanayi 页 2 可抓取再核。
- **市场统计（rehbersanayi 数据页，2026-06-30→10-19）**：全行业 30,740 项已决标 / 1,219.1 亿 TL / **38% 以 ≤2 份投标成交**；IT 行业 625 项 / 16.2 亿 TL；电气电子 1,036 项 / 15.8 亿 TL → 关系型市场结论（低竞争）继续加强。

## §2 Angora 本体复核（官网 + 新闻面，2026-10-21）

- **官网 angoranetworks.com（tr/en）新闻栏停更**：最新条目 = 2023-12-05（产品方案公告，细节按常设规则不展开）→ 2022-10 Packet Broker → 2021-09 PacketFence NAC。产品页 = Anahtarlar / SFP / İnce İstemci（thince.net）。**10 月无任何新品/新闻**。
- web_search 全量：仅 2021-2024 旧新闻（MWC 2023/2024、EGM 测试、KOZ 渠道峰会、Levent Kılıç 2023 访谈：OEM 能力自述「项目够大可以 OEM 生产」、teknoent 搬迁）。**2026 年 0 条新公开信息**。
- VERGE 家族页（复核）：8/24/32/48 固定 GE + 2-4×10G SFP+，PoE+ ≤30W/口；DC/TOR 款 = 48×1G/10G/25G + **6×100G QSFP28、3.6Tbps**（与既有 T 档案一致）；工业 8 口款 -40/+80°C 48V DC。
- LinkedIn：2,110 followers（静态）；RocketReach：10 人（7 可见）、2016 成立；ZoomInfo：收入 <$5M。
- **结论**：Angora 公开面继续沉寂（与「渠道窄、低可见度」既有判断一致）；官网停更 32 个月 = 弱信号（营销投入不足 or 内容集中在直销/渠道线下）。

## §3 PNetworks 动态复核（2026-10-21）

- 官方新闻：0 条 2026（仅 2021 Pendik 协议 / 2022 L&N / 2023-24 MWC / 2024-10 TTiMoT 旧档）。
- **n11 零售价（2026-10-21，与 10-08 锚点对比）**：CMS48GE4SFP+ PoE+ = **156,612 TL**（活动 144,666）／48GE PoE+ 款 = **150,812 TL**（活动 139,301）→ **锚点 13 天不变**。
- ⭐ **新增在售：PN8GE2CG（L2 管理 8 口 2 SFP/Combo PoE）= 61,419-63,707 TL**（SÜPER 标）→ 8 口 PoE 零售首次公开挂牌。
- ⚠️ **渠道价差**：Trendyol 同型 Pt_7 Pn-cms48ge4sfp+ PoE+ = **78,306.95 TL**（约为 n11 官方 1/2）；akakçe 聚合 127,189-204,732 TL 多卖家 → PNetworks 多电商并行、渠道间价格不统一（价格战早期特征，与我方定价策略直接相关）。

## §4 Ewind（深圳）2026 新品（ewindnet.com 官方新闻，经 web_search 摘要）

- ⭐ **2026-04-29：EW-S3936GM Gigabit Managed Switch** = **Microchip（Vitesse）芯片方案**（官网自述 "proven Microchip (Vitesse) chipset solution"）→ **芯片世代更新实锤**（既有档案未记录 39xx 线）。
- ⭐ **2026-04-21：Industrial Cloud-Managed 系列**：hybrid PoE + 12/24V 被动 PoE + **802.3bt 90W** + DIN 轨 + 宽压 + 长距 → 工业云管理线扩张。
- atommarket 目录（10-21 搜索摘要）：7 款在售 = S1806CF-AP（4FE PoE+ 65W）/ S1810GU-AP（1,004.57 TL）/ S1827CF-AP（24FE 3,470.81 TL）/ S1920CG-AP（16GE 300W）/ S2910GM-AP（8GE PoE+ 4,475.38 TL）/ **S2924GM-AP（24GE PoE+ 4Combo 400W，既有锚点型号仍在售）** / S2916GM-AP（16GE 250W）。

## §5 Keenetic Türkiye 零售落地（2026-10-21）

- 2026-05-14/15 官宣（blog.keenetic.com.tr + Technopat/TechnoLogic/bthaber）：6 月起分阶段上市 switch（5/8 口经典、2.5G、16/24 口、PoE+）；CEO Vefa Tarhan。
- **零售实况（10 月）**：KN-4610-01-EU 5 口 PoE+ 60W = **1,599-1,849 TL**（Amazon 19 评 4.6★／Trendyol 1,699）；KN-4710-01-EU 9 口 PoE+ 120W = **2,909.92-3,349 TL**（n11 SÜPER 标）；akakçe 5 口款 **30 个卖家报价**（1,599-3,398）→ 铺货快、价格带压到 1.6-3.3K TL，与我方 8 口 PoE 成本优势带正面重叠；**仅 unmanaged，无 managed/工业线**（观察项维持 12 个月）。

## §6 Longline hepsiburada 店铺复核（2026-10-21）

- **店铺规模：116 个产品**（r18 时点 ≈10 switch 模型 + SFP 族）→ 零售铺货扩张 10 倍级；品类 = Switch/网络配件/连接器/网卡/线缆/RAM/SSD/手机/服务器硬件（多卖家：Elektromarka/VENOT/miniöde/Emka/ÖZKARMAN/Core 等）。
- ⭐ **新上架 LNG-M3XF4GE24：24 口 Gigabit L3 管理工业 PoE+ 交换机 + 4×10G SFP+ uplink = 137,900 TL**（r18 档案无此型号）→ 工业 L3 线上探企业级价格带（≈4.8 万 TL/5630 锚点之上的新档）。
- 既有锚点复核：5 口 Gigabit = **750 TL 不变**。
- 光模块价（新锚点）：SFP-10G-SR-LL = 4,787.99 TL；GLC-LH-SM-LL（1G 单模）= 1,087.83 TL；GLC-BX-D/U Bidi = 1,028-1,115 TL；**QSFP-40G-LR4 = 12,600 TL**；LNG-8110G-SS MC = 688.70 TL。

## §7 待核项清理（复核解决 2 项 + 部分解决 1 项）

1. ⭐ **Opax（111 行 20，r19 唯一客户侧待核）= 已解决**：opax.com 官网法律条款页 = 主体「**Opax Mühendislik Kamera Alarm ve Güvenlik Sistemleri ... Pazarlama Limited Şirketi**」，注册/办公地址 = **Yeni Mah. Diriliş Bulvarı No:3, Opax Plaza, 50100 Merkez / NEVŞEHİR**，电话 +90 850 259 12 12 / 044 9890；**B2C 直销 + B2B 代理商（bayi）双轨**（官网发布《代理商与 B2B 会员协议》全文）；产品页实价 OPAX-08120W = $35（1,623.30 TL）/OPAX-0890W 等；**opax.pl = 另一波兰域，与土耳其主体无任何书面关联** → 「外资主体」假设降级为「无关域名的历史联系」，跟进对象 = 土耳其 NWS 主体。
2. ⭐ **Fiberix（r20 #66 排除项复核）= 确认排除**：fiberix.com.tr = **面向个人的光纤 ISP**（无限流量套餐 519-619 TL / 20-100 Mbps、"自有基础设施"、账单/速度测试/WhatsApp 客服）→ 非 switch 贸易实体，「广州现有伙伴」说法现网站无任何佐证 → 排除维持。
3. **Duzgun Toptan ↔ Toptansarf（111 行 43）= 部分解决**：toptansarf.com / .com.tr **在运营** = 主体「TOPTANSARF BİLGİSAYAR VE GÜVENLİK SİSTEMLERİ」，Hürriyet Mah. Sedef Sok. No:5/A **Bahçelievler/İstanbul**，0212 580 25 25 / +90 541 660 10 66，「10 YILDIR BAYİLERİN ÇÖZÜM ORTAĞI」B2B 批发 1000+ SKU（目录含 **Ruijie Reyee RG-RAP2200F PoE AP**、IMOU 路由、Wissmann 接收机等）；**teksarf.com 当前 HTTP 500（站点宕机）**；Duzgun（gmail 联系）与 Toptansarf 同一主体 = 高概率但需 WhatsApp 实联确认 → 待核降级为「待实联」，不阻塞跟进。
4. NetGaste（疑似软文）、ONSİS $28.2M（datanyze）、Longline 成立年（LinkedIn 2000 vs entegron "Established in 2000, LONGLINE Technology Ltd" 已互证）——维持既有结论，本轮无新证据。

## §8 其他复核（负面结果留痕）

- rehbersanayi `?page=N` 分页参数确认仍被忽略（JS 渲染）→ 盲区 10-01→10-08 无法覆盖；EKAP 官方站仍需 JS。
- pnetworks.com.tr 官网首页 fetch 间歇失败（代理 OSS 错）→ 以 n11/Trendyol/akakce 第三方渠道数据为准（已足够）。
- Angora 渠道面（bayi/satış ortağı 2026 新闻）：0 命中。
- 111/110 既有数字交叉复核：本轮 110 行 63-76 中标数字均为 r17 窗口旧值（10-08 抓取），本轮 6 起新增为**追加**而非矛盾（旧 İKN 记录保持不变）。

## §9 本轮信源清单

1. rehbersanayi.com（IT 归档 60 条 10-09→10-19 + 数据页统计，2026-10-21 fetch）
2. angoranetworks.com tr/en（首页新闻 + VERGE 家族页，fetch）
3. hepsiburada.com/longline（116 产品目录，fetch 2 chunks）
4. n11.com Pnetworks 品牌聚合页 + trendingol/akakce PNetworks 单品（web_search 摘要）
5. ewindnet.com/news/product-news（2026-04-21/29 两条，web_search 摘要）+ atommarket.com.tr Ewind 目录（摘要）
6. opax.com（产品页 + 法律条款 + 代理协议页，web_search 摘要）
7. toptansarf.com / toptansarf.com.tr / infobel 条目（web_search 摘要；teksarf.com 直连 = HTTP 500）
8. fiberix.com.tr（fetch 首页）
9. blog.keenetic.com.tr / technopat / technologic / bthaber（2026-05-14/15，web_search 摘要）+ trendyol/n11/akakce/amazon/inchhesap Keenetic 零售（摘要）
10. ictmedia / defensehere / mediatrend / c4defence / platinonline / tele1（Angora/PNetworks 旧新闻面复核，摘要）
