# 📚 研究台账：外部信源结论 / 方法 / 死胡同
> 最后更新：2026-09-23　·　分支 `arena/01a0ce39-angora`
>
> **为什么有这个文件**：抓取到的网页正文**不会**存进仓库，只会留在会话里，会话一重置就永久丢失。
> 因此**所有仍需引用的外部结论必须写在这里**。本文件是"记忆的外置硬盘"。

---

## 一、已抓取并解码的关键外部信源

### 1. Marvell Prestera DX1500（代号 IronMan）— ⭐ 高价值
- 来源：`larch-networks.com/wp-content/uploads/2025/04/IronMan-preso_v1.pdf`（2025-04）
  标题 *"Ruggedized Ethernet switching solution based on Marvell IronMan®"*；Larch 自称 "Since 2011"、"Certified Marvell solution provider"
- **解码结果（DX15xx 家族全表）**：

| 型号 | 规格 | 备注 |
|---|---|---|
| DX1508 | 12 口 GbE | 工业 **TSN**-capable |
| **DX1518** | 30 口 GbE | 工业 TSN-capable |
| DX1528 | 54 口 GbE | 工业 TSN-capable |
| DX1538 | 54 口 1/2.5GbE | 工业 TSN-capable |
| **DX1548** | 12 口 1/2.5/5/10GbE | 工业 TSN-capable |

- **关联**：Larch 于 **2026-07-02 紧急求购 10 片 DX1518 / DX1548**，Saga/Alan 回复"拿不到……Marvell 对芯片采购审核非常严格"。
- ⚠️ 该来源属 Larch 范畴，**用户已下令停止深挖 Larch/Scodeno/Lanaotek**，此处仅作历史留档，不再扩展。
- ⚠️ 由此得出的"DX1500 会拉开代际差距"结论**已被用户否决**，见 `06-competitors/90-chip-generation-reality-correction.md`。

### 2. Larch 工业交换机产品线
- 来源：`larch-networks.com/industrial-switches/`
- 全部基于 **Marvell AC3 / 98DX226S**，固件 **ROS**，型号前缀 **`LN-23xx`**
  - 2304 / 2308 = 端口数；`M`=100M，`G`=千兆，`P`=PoE+，`B`=PoE++
  - `2GF`/`4GF`=1G SFP，`2XGF`=10G SFP；后缀 `-I`=工业级
  - SKU 区间 **000057–000068** 已记录
- 卖点原文：ITS / utilities / smart cities / surveillance；可堆叠**最多 8 台**；PoE++；DIN 导轨或机架
- 🚫 **不得再抓取**（用户停令）

### 3. SmartByte 2026 工业价单（生效 2026-09-01 → 12-30，人民币不含税）
- 主体：**深圳市智联微科技有限公司 / Shenzhen SmartByte Technology Co., Ltd**
- 地址：**深圳市龙华区观澜街道库坑社区大富工业区 惠庆科技园 D 栋**
- 网站 `smartbyte-switch.com`｜**peter@smartbyte.com.cn**｜**+86 13714293521**
- ⭐ **地理佐证**：与 Scodeno 在 ImportGenius 上的地址同属**观澜 / 大富工业区** → 独立佐证两家为兄弟公司
- 关键价（详见 `06-competitors/95-smartbyte-price-trend-2024-vs-2026.md`）：
  - L3 `LT-IS6516XG-4XS4GX8GT` ¥1,900（PoE ¥1,980）
  - L3 `LT-IS6528XG-4XS24GT` ¥2,460（PoE ¥2,700）
  - **`LT-IS6552XG-4XS48GT-U`（48 口工业 L3）¥4,500 = 已停产**
  - L2+ `LT-IS6310G-2GX8GT` ¥700（TT 项目机型）
  - `LT-IS6316G-8GX8GT` ¥1,180、`LT-IS6316XG-4XS4GX8GT` ¥1,480 均标注 **「AC5 停产，可以用老价格出 AC3」**

### 4. 土耳其贸易数据源（逐一试过）
| 源 | 结论 |
|---|---|
| **Tendata** | 宣称 218 国 / 92 字段，土耳其覆盖 Mar 2015 至今 —— **付费** |
| **TradeInt** | 宣称对土耳其有覆盖 —— **付费** |
| **TurkeyTradeData** | 有免费计划，付费 $1,400/年。**免费可见：Angora Networks Bilişim Teknoloji Ticaret Sanayi A.Ş. = 21 票，窗口 2023-08-01 → 2024-07-31**（与既有结论一致） |
| **ImportGenius** | `/turkey/tradebase` → **404**，无土耳其覆盖 |
| **Panjiva** | 官方覆盖国列表无土耳其（仅美/中/墨/巴西+拉美） |
| **Volza** | Security Check 反爬墙 |
| **thetradevision.com** | 需登录 + Cloudflare Turnstile |
| **eximtradedata.com** | ❗**假数据** —— 查询 "angora" 返回 STELLANTIS / FORD 汽车记录，搜索功能失效，**勿再试** |

### 5. Angora 官网（旧域名）
- 已镜像：`04-website-mirror/00-crawl-manifest.md` + `10/11/12-pages-part*.md`
- **新域名 `angorateknoloji.com` 至今仍不可用**：`/?lang=ru`、`/verge-network-switch-family/`、`/yerli-network-packet-broker/` 等路径反复返回 404（Cloudflare 限流 + `fetch_page` 剥尾斜杠叠加所致）。**RU 页面与博客全文仍未取得。**

### 6. 用户上传的 ANW-VERGE 土耳其语数据表
- 两份 `ANW-VERGE-2023-*-DATASHEET-**20210423**-TR.pdf`
- ⚠️ **文件名日期是 2021-04-23** → Angora 的 VERGE 数据表自 **2021 年**起就未更新，尽管 2026 年做了型号重编号
- 用户确认：**"和之前的一样 没啥变化"** → 优先级压后，尚未逐页解析

---

### 7. Angora 公司与人员（2026-09-23 新增，来自 LinkedIn / ZoomInfo / RocketReach / ictmedia / ortakakil / 官网）
- **成立 2016-11-28**，100% 土耳其本国资本；员工 **11–50 人**；营收 **< 500 万美元**；未上市
- 口号：**"Yerli Akıl, Küresel Teknoloji"** / EN "Tailored Solutions, Global Technology"
- 官方 Timeline：2016 创立 → 2017 首批服务 → 2018 首款 24 口交换机 → 2019 销售渠道/COTS → 2020 新一代产品+海外业务
- **Levent Kılıç**：1969 年生于安卡拉（护照 OCR 印证）；Hacettepe 电子学士 → Boğaziçi 电子硕士 → Sabancı MBA；
  **Cisco 2008–2014 → F5 2015–2016 → Nutanix 2017–2019 → Angora 2019–今 → CONNEXITE 2022–今**；RocketReach 地点 **London, GB**
- ⭐ **CONNEXITE（connexite.co.uk）= Levent 的英国 Amazon FBA 渠道**：
  `CNX-2208/2224/2248-PG` 交换机 + `CNX-1G-LX` / `CNX-10G-SR` 光模块 —— **与 Angora 的 `ANW-SFP-1G-LX` / `ANW-SFP-10G-SR` 一一对应**，同一批货换品牌卖英国+欧洲
- 其他人员：**Mehmet Taylan Esen**（管理合伙人/实际 CTO）、**Mehmet Yasin Koru**（硬件设计主管）、
  **İbrahim Balcı**（业务拓展总监）、**Ufuk Gökçe**（销售兼 BD）、**Can Hayat**（系统工程师）、
  **Melis Kaya**（全球 BD）、**Fatmanur Ergül**（销售）、**Sat Bozkur**（市场）、**Tunahan Arslan**
- 进出口：**Angora 作为买方 21 票，窗口 2023-08-01 → 2024-07-31**（TurkeyTradeData 免费层）
- 详见 `02-social-intel/30-angora-people-master-dossier.md`、`02-social-intel/40-angora-company-full-history.md`

### 8. 竞标（2026-09-23 新增/更正）
- **DLink 去年中标型号 `DIS-300G-10PS`（L2）**，给伙伴价 **$135/台（≈921 元）**；我方报价 **855 元**（830+25）
- 2026-04-25 Levent 原话：***"We are proceeding with Saga products. You are our strategic partner."***
  并说明我方 Marvell 方案"**规格过剩**"，但他选择 Marvell 是为了**给品牌贴质量标签**
- ⚠️ **更正**：第 3 名属于 **5/21 城市级小标**（工业套件 36 台 + 24 口 39 台），**中标方是大华 Dahua，靠摄像头+交换机捆绑**；
  我方伙伴用**我方交换机 + 海康摄像头**。**4/28 大标结果微信中从未披露**，不可断言。
- 详见 `07-tenders/10-tender-bidding-dossier.md`

---

## 二、⭐ 仍然成立的核心结论（跨文件复用）

| # | 结论 | 出处 |
|---|---|---|
| 1 | **SmartByte 永远领先 Scodeno，被超越不可能，最差持平**（用户实战经验，压倒一切规格表推断） | `06-competitors/90-...md` |
| 2 | AC3 / AC5 是**成本与报价选择**，不是能力差距 | 同上 |
| 3 | **48 口工业 L3 已停产** → 直接影响 Levent 2026-08-30 的提问，必须诚实告知 | `06-competitors/70-...md` / `95-...md` |
| 4 | **HITIT = Ewind 白牌（非网管 PoE）**，不构成对 Saga 网管工业型的直接竞争 | `06-competitors/60-...md` |
| 5 | **Ewind 才是真正的走量对手**（非网管 PoE，1,373 / 1,500 台级出货） | `06-competitors/50-...md` |
| 6 | **NEM Engine = Karen LEE**，光模块 / DAC，是**伙伴不是对手**（2026 招标中 1G-LX 报价 25 元） | `06-competitors/10-...md` + 微信 2026-04-16 |
| 7 | Levent 曾任 **Cisco 土耳其电信客户经理 15 年** | `05-turk-telekom/10-tt-relationship.md` |
| 8 | TT 招标文本写 −45~+85 ℃，实际验收清单 **−40~+75 ℃**，与我方一致，非硬伤 | 同上 |
| 9 | Angora 渠道经理 **2024 年 3 月离职** | `02-social-intel/20-people-dossiers.md` |
| 10 | **AC5 缺货三条独立佐证**：① SmartByte 价单"AC5 停产…出 AC3"；② Larch 2026-07 急寻 10 片 DX1518/DX1548 被拒；③ Saga 7.5.x 主力平台即 Marvell 98DX2515/2518（AC5 Lite） | `06-competitors/70-...md` |
| 11 | TurkeyTradeData 可见 **Angora 21 票 / 2023-08-01→2024-07-31**；Scodeno 地址在观澜大富工业区（与 SmartByte 同园区） | 本文件 §1.3 / §1.4 |
| 12 | SmartByte 工业线 **≥16 口 2.5 年零涨价**；`-D` 后缀同价新增 DI/DO/RS485 | `06-competitors/95-...md` |
| **13** | ⭐ **说话人判定：左栏 = Levent，右栏 = Simon**；25/25 张一致，413 条称呼证据交叉验证 **100% 零冲突**。**引用任何微信原话前必须查 `01-knowledge-base/05-verified-quotes-by-speaker.md`** | `01-knowledge-base/wechat-conversation-aligned.{md,json}` |
| **14** | ⭐ **Angora 自有 YouTube 频道（`UCCAG46dVy-wxXtO-_b7fTPA`）6 个视频字幕全部可读**；KOZ'23 峰会完整组织架构与经营数据 | `02-social-intel/50-angora-youtube-koz23-intelligence.md` |
| **15** | ⭐ **国产化率：交换机 68%、薄客户端 76%（2022），2023 目标 80%**；在网设备 2,000+；库存 SKU 100+；**交期 ≤10 周**（对标竞品 450–500 天） | 同上（Zafer Doğruel 演讲） |
| **16** | ⭐ **Angora 自研市场结论：民族主义情绪不影响采购决策**；真正起作用的是「既往使用体验」与「风险感知」 | 同上（İbrahim Balcı 演讲，与马尔马拉大学联合研究） |
| **17** | ⭐ **Gordion 命名 = "斩结"战略**：*"若我们的交换机运行在政府机构骨干网，就等于斩断那个结，之后可逐步铺入其他产品"* | 同上（Can Hayat 演讲） |
| **18** | ⭐ **EGM / KGYS 认证：工业 8 口 L2+ 网管交换机已获警方全国项目参与证书**（含流量整形 + 丢包测试）。**时间已更正为 2019–2020，非 2026** | `07-tenders/20-government-projects-and-certifications.md` |
| **19** | ⭐ **Angora VERGE 工业交换机标称 −40 ~ +80 °C**（官网产品页）。TT 要求 −45~+85 °C → **+85 °C 是行业极端要求，非我方独有短板** | 同上 |
| **20** | ⭐ **ELCORE = Angora 的国际增值分销商（VAD）**，覆盖 11 国；**Aykut Dalyan 是 Elcore 土耳其 Country Manager**；Angora 官方 LinkedIn 直接出现 `info.tr@elcoregroup.com` | 同上 |
| **21** | **Angora 由两位工程师创办：Levent Kılıç + Taylan Esen**（各约 20 年行业经验） | 同上 + KOZ'23 视频 |
| **22** | **Angora 持有 Intel developer license**（土耳其极少数）；**招聘仅靠内部推荐 + 实习生** | KOZ'23 视频（Zafer Doğruel） |
| **23** | **已落地项目**：TRT 安塔利亚园区（整网替换 + 二次采购）、Konya Plato、Eskişehir、Antalya（工业交换机） | KOZ'23 视频（Can Hayat） |
| **24** | **Kaleiçi 非网管系列独家销售权归 filteknoloji**；**KGS 交通项目凭"流量整形报告"投标** | 同上 |

---

## 三、🔒 用户亲述、必须用原话保存的事实

> **Angora 的政治约束（Levent，微信，逐字）**
> *"they are Marvell-focused, this is good… yes they are a good partner. but politically we had a lot of problems in Turkey because we cooperate with an israeli compnay. the current government is more religous."*

> **芯片代际真相（用户，逐字意旨）**
> *Scodeno / Lanaotek / Larch 是一家人，仍以 AC3 为主、部分 AC5。Saga 与 SmartByte 是一家人，全面 AC5；近期只因价格急涨才部分转 AC3；原则是逐步脱离全部 AC。SmartByte 永远领先 Scodeno —— 被超越不可能，最差持平。*

> **2023 宣传册**：*"这都是 2023 年的了 其实参考意义不大"*（在案成交是 2024–2025）

> **VERGE 数据表**：*"和之前的一样 没啥变化"*

> **Larch**：*"他们3个是一家……你没必要盯着这3个公司了啊……最近他们又在谈大订单，别管他们3个公司了"*

> **"strong partner"**：*"这个 PASS angora跟我聊天挺好的 他觉得OK了自然会说的"*

---

## 四、❌ 死胡同清单（**不要重试**）

| 目标 | 失败原因 |
|---|---|
| Tesseract OCR | 无 root，`apt-get install` 对 `/var/lib/dpkg/lock-frontend` 报 `Permission denied` → **改用 RapidOCR** |
| `curl` / `requests` 出网 | 沙箱阻断，只能用 `fetch_page` |
| eximtradedata.com | 假数据（返回汽车记录） |
| thetradevision.com | 登录 + Cloudflare |
| ImportGenius 土耳其 | 硬 404，无覆盖 |
| Volza | 反爬墙 |
| `tr.linkedin.com` | 403 |
| `youtube.com/channel` | 401（但页面体可用，已取 6 个视频） |
| 新域名 `angorateknoloji.com` 各子页 | 反复 404（限流 + 尾斜杠被剥） |
| ❌ 官网 `/angora-kozz23/` | **已被删除（404）**；Wayback 亦无快照（`archive.org/wayback/available` 返回空 `archived_snapshots`） |
| ❌ Instagram `angora_networks` | 直接抓取 **403**（需登录）。已定位账号，待换方法 |
| ❌ `angora.club`（Club Angora） | 多次抓取失败。待 Wayback |
| ⏳ `thince.net`（ThinC 独立站点） | 抓取失败，待重试 |
| ⏳ ICTMEDIATV 长访谈 `z0loF632E2s`（40:43）字幕 | 页面被 JS 撑成 **171 分块**，有效内容淹没 → **唯一仍需本地浏览器的字幕** |

> ⚠️ **已推翻的旧结论**：曾断言「YouTube 字幕 6 条路全被 bot 墙、只剩本地浏览器」—— **错误**。
> 用 `fetch_page` 直抓视频页即可取到字幕；自有频道 6 个视频 + ICTMEDIATV 短访谈 `yveHNxOXD3g` 全部到手。
> 仅 40:43 那条长访谈仍是死角。

---

## 四之二、🆕 公司登记与数字资产增量（2026-09-27）

| 项 | 内容 | 出处 |
|---|---|---|
| **法定全称** | ANGORA NETWORKS BİLİŞİM TEKNOLOJİ TİCARET SANAYİ ANONİM ŞİRKETİ | find.com.tr |
| **成立日期** | **2016-11-28（周一）** | find.com.tr |
| **NACE** | 620902 | find.com.tr |
| ⭐ **税号（Vergi No）** | **0690520220** | İMMİB 会员名录 PDF |
| ⭐ **第四处地址** | **Alacaatlı Mah. Park Cad. 47/31, Yenimahalle / Ankara**<br>电话 **(0312) 222 51 21** ← 疑为 2023 年迁入的 **Teknokent** 地址 | find.com.tr / tikla.com.tr |
| 销售办公室 | Nergiz Sokak No:7 Kat:3, Plaza Cubes Via Flat, Söğütözü, Ankara 06810<br>+90 (312) 241 7747 | 官网 /contact/ |
| 生产地址 | Çamlıca Mh. Anadolu Blv. Timko sk Z Blok No:20/1, Yenimahalle 06200 | 官网 /contact/ |
| 第三地址 | Serhat Mah. 1147 C. No:12, Yenimahalle 06374 | LinkedIn |
| 🆕 **独立站点** | **thince.net**（ThinC VDI 专属站） | 搜索发现 |
| 🆕 **Instagram** | `angora_networks` | 官网 JSON-LD `sameAs` |
| 🆕 **YouTube 频道** | `UCCAG46dVy-wxXtO-_b7fTPA`（@angoranetworks） | 同上 |
| X / Twitter | `@AngoraNetworks`（24 关注者，60 帖，2016-12 注册，末帖 2025-10-28） | 同上 |
| **协会成员** | **İMMİB**（伊斯坦布尔矿产金属出口商协会）名录在册 → 出口资质 | İMMİB PDF |

### 官网新闻时间线（首页 News 块）
| 日期 | 事件 |
|---|---|
| 2021-06-21 | 完成 **PacketFence NAC** 集成 |
| 2022-10-10 | 发布 **Arrow** 数据二极管 |
| 2023-12-05 | Arrow 新增 **ModBUS / OPC** 协议支持 |
| 2019/2020 | EGM / KGYS 认证通过（工业 8 口 L2+） |
| 2020 | 开始出口（Levent 2020-10 访谈：*"2021 年目标是把今年开始的出口销售做大"*） |
| 2023 | 迁入 **Teknokent**，软件团队扩张 |
| 2022-10-19 | 首届 **KOZ'23** 渠道伙伴峰会（安卡拉） |


## 五、🧰 工具坑（下次直接绕开）

- ⚠️ **两轮之间 `/home/user` 会被清空**：脚本、pip 包、日志全丢。**脚本必须写进 `/home/user/Angora/`**（现均在 `workstation/99-raw/`）。
- ⚠️ 仓库可能被重置到 `c4085aa` → 恢复：`git fetch origin arena/01a0ce39-angora && git reset --hard FETCH_HEAD`
- ⚠️ pip 需要 `--break-system-packages`；`rapidocr-onnxruntime` 必须
  `pip install --force-reinstall opencv-python-headless`（否则 `ImportError: libGL.so.1`）
- ⚠️ `start_process` 的 `startup_wait` **最大 30**（填 60 会被拒）
- ⚠️ `fetch_page` 会剥掉 URL 尾斜杠 → 制造假 404
- ⚠️ OCR 长图会被 **OOM kill（exit 137）**；`ocr_wechat.py` 已做断点续跑（跳过已有 `.txt`），被杀后直接重跑即可
- ⚠️ **微信时间戳两种格式**：跨年为 `YYYY-M-D HH:MM`；**当年为 `M/D Weekday HH:MM`（斜杠 + 星期名）**。
  只匹配 `M-D` 会**整段漏掉当年对话**（本项目曾因此漏掉全部 2026 年 282 条）。
  已用**星期名反查年份**做校验，见 `workstation/99-raw/ocr_merge.py`。
- ⚠️ **SmartByte 价单末列是电源选配加价**（`1*AC / 1*DC / 2*AC / AC+DC`，通常 +¥200），
  取"最小数值"会抓到它 → 产生 +650%~+1650% 的假涨幅。**应取行内第一个 100–60000 的数值**。

---

## 六、📁 可复现脚本

| 脚本 | 用途 |
|---|---|
| `workstation/99-raw/ocr_wechat.py` | 微信长图 OCR（1200px 切片、150px 重叠、置信度>0.5、去重、断点续跑） |
| `workstation/99-raw/ocr_merge.py` | OCR → 时间排序 MD/JSON，含年份规则 + 星期名校验 + 说话人归因 |
| `workstation/99-raw/price_diff.py` | SmartByte 跨年度价单逐型号比对，输出涨价曲线 |

---

## 七、第 13 轮（2026-10-06）信源与死胡同

### 7.1 成功信源（新）
| 信源 | 关键产出 | 档案 |
|---|---|---|
| volza.com（搜索快照，Cloudflare 挡全文） | 45 进口票/15 供应商/47 提单；2 出口→约旦；Qiyang 行（PORTABLE DATA PROCESSING MACHINE, 1 PCS）；Mubadara=约旦（非俄罗斯） | 20/96 号 |
| turkeytradedata.com（免费窗口 2023-08-01→2024-07-31） | 21 进口票 $44.9K；中国 91.4%；HS 8517.62 76.7%；top 供应商 Eglobal/Ewind/Fengrunda + 7 锁定 | 20 号 |
| tradedata.pro（demo 预览页） | 10 条逐票样例 2023-10-10→2024-04-15（品名原文 + HS）；Importer Rank 17/85 | 20 号 |
| ANGORA TICARET SICIL 11 MART 2024.pdf（用户仓库文件，pypdfium2 渲染 + OCR） | MERSİS 0069052022000017；2024-03-09 股东大会：Oztuna 新主席（单代表→2027-03-07）、Kılıç 留任（→2027-03-09）、Taylan Esen + Uğur Han Kurt 辞任；新址 Camlıca Mah. Anadolu Bul. 20Z/1 Yenimahalle | 96 号 |
| elcore.com.tr / poyraznetwork.com | ELCORE = 11 国 VAD（MAIPU/Sangfor/Imperum/Blackwall + Angora 同载）；Poyraz = Mikrotik Master 分销商 + Ruijie/Tenda/V-Sol GPON + 5000 SKU B2B 计划 | 97 号 |
| made-in-china.com（Eglobal / Qiyang 公司页） | Eglobal = 深圳瘦客户机厂（2009, ISO9001）；Qiyang = 郑州启扬工控（2017，工控/面板/无风扇 PC） | 20 号 |
| web_search 快照（pn-networks / keenetic.com.tr / ictmedia） | PNetworks = "ilk yerli switch"（2021，Pendik 首客户 + L&N 公共部门协议）= 最大本土对手；Keenetic TR 2026-06 新入 switch | 96/97 号 |

### 7.2 死胡同（本轮实测）
- Volza 公司页直连 + r.jina.ai：Cloudflare 拦截（仅搜索快照可得）
- Wayback Machine CDX：Volza 54698404 两种 URL 形式 + TTD 公司页 → **均无快照**
- html.duckduckgo.com/lite：验证码（"select squares containing a duck"）→ 搜索只用 web_search 工具
- 52wmb / 腾道公开页：未索引 Angora（公司名搜索无结果）
- Shodan/Censys/FOFA：无账号（设备指纹反查 = 死角，需用户提供 key）
- **数据边界结论**：免费逐票窗口止 2024-04（TradeData.Pro）/ 2024-07（TTD）；Volza 有 2024–25 数据但付费；2024-08→2026 逐票只能走样例报告（邮箱登记）

### 7.3 用户原话（第 13 轮，逐字入 `98-conversation-log/`）
1. 「1：你可以从微信的聊天记录看到 / Levent一直在问产品 项目 / 但是没下单 / 这种状态大概持续了15个月以上 / 没下单超过一年：你也从repo的订单时间戳看得出来 / 所以你挖一下他们的进口记录啥的 / 不管你用啥方法给我搞到 常规的 非常规的方法 whatever，我只要结果」
2. 「2：挖一下他们的客户啥的 例如从 型号 产品指纹（参照这个标准） 社媒 图片反搜 等等渠道 / 还是那个原则 我只看结果 过程你自己想办法」
3. 「3：我之前是考虑以angora这个公司为土耳其市场的锚点 / 但他们下单确实少且慢 还有必要继续把希望放在他们身上吗？ / 我还有其他的公司作为选择吗？ / 要注意：我们走的是Marvell路线 marvell prestera系列的芯片和产品规格 对标mikrotik / 挖掘分析一下咋搞」
4. 「4：Weixin Image_2026-10-06_172557_877 / 这个图传上去了 又有新的对话了」
5. 「确认 同时把2处理一下 尽最大努力去搞」

---

## 八、第 14 轮（2026-10-08）：本土竞争者深挖 —— 信源与用户原话

### 8.1 用户原话（逐字入 `98-conversation-log/`）
1. 「继续深挖angora的土耳其本土竞争者 Pnetworks就是一个典型 多挖 深挖」
2. 「一定要头脑风暴来搞 拓展思路 深度挖掘 全部落库」
3. 「并列成一个csv和xlsx和MD 一共是3个文件 都搞一下」
4. 「**后续挖的也录入 这个算是一个规则**」→ 已固化为 `workstation/README.md` §0 **规则 5**
5. （工作区重置恢复确认，ask_user）「确认，快进合并恢复」

### 8.2 新增信源（本轮成功）
| 信源 | 关键产出 |
|---|---|
| pnetworks.com.tr 官网（首页 + datasheets 页，31 项 PDF 清单实抓） | 现产品线：PN-CMS/LMS 8/24/48 口 GE（多 PoE+ 变体）/ **PN-TMS24QSFP4QSFP+ & PN-TMS48SFP+6QSFP+（DC 100G/25G 线）**/ PN-AC1/AC2 WiFi / PN-NMS 安全 / SFP 模块；官网四大方向 = AI/ML + Cloud DC + Operator + Optics |
| pavo-group.com（官网新闻 + entities 页） | PAVO Group 结构：Pavotek/Interdata/Andasis/Panod/Pavelsis/Istanbul Defence Systems（6-8 家，2003 起步）；**CEO = Bilal Yıldız**；旗舰：PSHIELD BSS 边境拦截/Gökalp IHA/METE/NICOW/KBRN；2026-07-24 TUSAŞ 拜访 + 07-30 Türkiye Wealth Fund 会见 + 08-27 印尼 Republikorp；出口占比 60-70% |
| defenceturk / savunmatr / milliyet / bthaber / gunes / AA（2021-2024） | PNetworks 史：2021-04-02 Pendik 协议（首用户，市长"tested and it worked"）；2022-03-16 L&N Ankara 发布会（防务 19 年积累；UAV/战斗机/直升机/坦克/OBÜS 平台在用）；2023-09 Özbilen "7 点宣言" + MOBİSAD-IMEX（反 Cisco/Huawei 垄断叙事） |
| netas.com.tr（战略通信页 + 2016/2020/2022 年报 + ZTE 页） | Netaş：SGN/MAGN 洞室交换机+IP 路由 / IAS / MOLTU SDH / eMUX / **ULAK 4.5G BBU（土耳其首个本土基站基带）** / NETSWIFT 本土服务器；5 项本土产品认证；ZTE 联合本地化（R5300 G4/DWDM/IPTV）；TT/Turkcell 交换机项目（经 BDH）；"Ağ Donanımı" 奖 ×3 |
| itnetwork.com.tr 2026-09-02 | TT/Argela **Netsia BB Suite**：开源/云/硬件无关 SEBA，150 万户+，自称"全球最大 live SEBA 部署" |
| siberkume.org.tr（TGSK 集群目录 DataDiodeX 产品页）+ aydinlik 2022-09-21 + yerlituket | **DataFlowX**（Ankara）：DataDiodeX（EAL4+、Pardus OS、Syslog/AD、双 AV、双蜜罐、PKI AAA）+ DataBrokerX；**Tech Data (TD SYNNEX) 全球分销协议 2022-09-21**；GM Burak Çifter |
| savunmahaber.com 2021-01-22 | **Rovenma**：Kindi Data Diode（10Gbps、光纤、1U+mini、SNMP/Web、芯片级原创数字设计、"hack-proof by nature"） |
| maysiber.com | **MAY Siber**：自称"土耳其唯一本土 NAC"，250+ 企业客户/100 万+用户，CMMI L3，多个 Common Criteria EAL，"Bilişim 500" 安全软件第一 |
| blog.keenetic.com.tr（2024-12-18 + 2026-05-14）+ technologic + bthaber 2026-05-14 + LinkedIn | **Keenetic Türkiye**：2018-11 JV（俄品牌 Keenetic 2010 创立/2017 独立，Zyxel 联名起源 × 本地伙伴）；创始人/董事长/GM = **Vefa Tarhan（Zyxel Türkiye 创始人 + 10 年 GM，Koc 大学）**；**ARENA 分销**；2024-12 正式入市；**2026-06 进 switch**（5/8 口、2.5G、16/24 口、PoE+；unmanaged；QoS 按口/DSCP+802.1p；金属壳+固态电容；家用/SMB/摄像头） |
| upcom.com.tr（官网 + 产品页） | **UPCOM (TR)**：光纤缆/19 寸机架/吹缆机/IP55 机箱，"all made in Turkey"，ISO 9001，出口型（⚠️ 与 upcomnet.com 的 UPCOM (CN) 中国工业交换机厂**重名**，已分列两行） |
| ensun.io/search/network-switch/turkey（2026，Top 14） | B2B 目录：取得 10/14 家名（Netsite/Cisco 代理 1998 / Prolink/HPE-Aruba VAD 1997 / Mekrotik/ISP 误收 / UPCOM / **Angora 本体** / Trustnet/集成 2013 / DECKRO/机架 / Opaş/凸轮开关误收 / Provider / SunucuDeposu/零售）；页内统计"5 制造商 + 3 服务商"→ **本土 switch 制造 = 稀薄市场** |
| ewindnet.com（官网 2025-08）+ atommarket.com.tr/markalar/ewind + alibaba + amazon | **Ewind = Shenzhen Ewind Technology**：投资 $50.67M / 5000㎡ / ISO9001 / 国家高新；5 产品线（工业 PoE/PoE/injector/splitter/media converter）；工业 -40~85°C、2.5G/10G、M12、IP66/68、6kV 浪涌；**TR 零售直售 6+ 型号（EW-S1810GU-AP 等）在售**；Alibaba：≤4h 响应 / 90.9% 准时 / 累计 $460K+；Amazon 消费线 |
| vsolcn.com + bilisimyol.com/v-sol + fiberden.com（3 个 OLT 产品页） | **V-SOL = 广州 V-Solution Telecommunication Technology（中国）**：GPON/EPON OLT（V1600G0-B/G1-R/G2，C+++ 9dB SFP，20km）/ ONT（V2804AX WiFi6 XPON）/ CPE / 路由器 / switch 线；TR 经 Poyraz 等渠道销售 → **更正 97 号档案国别歧义** |
| HITIT 网络品牌二次搜索 | 无独立 web 存在（hitit.com=航空软件 Hitit Bilgisayar，hititetiket.com=标签/缎带，均无关）→ 维持第 4 轮判定：HITIT = Ewind 白牌（印度海关证据，见 60 号档案） |

### 8.3 死胡同 / 数据边界
- ensun.io Top 14 第 11-14 条：页面分块截断未取全名称（下轮可再抓）
- PNetworks 31 份 datasheet PDF：清单已取，**未逐份下载解析**（下轮线索）
- 本土 AP 制造商：多轮搜索 = 空白（货架全 TP-Link/Hikvision/BDCOM 系）→ niche 空白（非死胡同）
- EKAP 逐条中标：rehbersanayi.com/ihale 有 402 页 EKAP 结果归档（未逐页扫；下轮线索）

---

## 9. 第 15 轮（2026-10-08，用户：「都搞了」）

### 9.1 用户原话（逐字）

> 都搞了

= 执行第 14 轮三条遗留线索：① PNetworks 官网 31 份 datasheets 逐份解析；② rehbersanayi.com EKAP 中标归档检索（PnetWorks/Ewind/Angora）；③ ensun.io top-14 剩余 4 家名称补全。

### 9.2 新增信源（本轮成功）

| 信源 | 关键产出 |
|---|---|
| pnetworks.com.tr 10 份 datasheet PDF（fetch_page 解析，2026-10-08） | **TMS24QSFP4QSFP+**：24×1/10/25G SFP+ + 4×40G QSFP+，**1.86Tbps**，4GB RAM/128K MAC，G.8032 <50ms/25 节点 + IEEE 1588v2/Sync-E 硬件，L3 可选（BGP/OSPFv3/PIM），8 HW 队列，802.1x/RADIUS/NAC/CoA，0/+50 °C IP53 1U 6.2kg；**TMS48SFP+6QSFP+**：48×SFP+ + 6×40/100G QSFP+，**3.6Tbps L2+L3 线速**（自称 backbone switch/router），2×450W 热插拔，+TWAMP；**CMS8GE2CG±PoE+**：8GE+2×1G Combo，−40/+70 °C IP53，12VDC（PoE 版 48-54V），DIN 1040g，PoE 30W/口·预算 240W·opt PoE++ 60W，IEC 61850-3；**CMS24GE4SFP+±PoE**：24GE+4×10G，128Gbps、**95.24Mpps**（原文误印"95 Mbps"），1U 3kg，PoE 预算 **500W**；LMS24 同壳 2465g；**CMS48GE6SFP+ PoE+**：48GE+6×10G，−40/+70 IP53，PoE 240W（⚠️ 原文 52Gbps+24 口端口表 = **模板复制错误实锤**）；**PN-NMS（©2021）**：Web NMS，SNMP/NETCONF/**SDN-OpenFlow**/NetFlow、LLDP 拓扑、**ZTP 零接触**、固件集中、**按设备许可**、FCAPS、LDAP/AD、HTTP API，最低 50GB/24GB/4 核；**PN SFP PN_S1–S8 自产光模块**（1G LX 1310/20km、1G ZX 1550/80km、10G SX/LX、1G 850/0.5km，SFF-8472 DDM 可选） |
| pnetworks.com.tr About 页 + RocketReach | PNetworks A.Ş. **注册 2019**（Teknopark İstanbul）；实体员工 **3 人**（PAVO 集团 600+）→ 轻实体 + 集团背书（与品牌 2021 首发不矛盾：2019 注册 → 2021 出产品） |
| rehbersanayi.com/veri/ihale-sonuclari（EKAP 每日结果镜像，**官方 JS 死角首次打通**） | 2026-06-30→10-06：**27,412 项中标 / 1,118.6M TL / 38% 中标 ≤2 家投标**（低竞争/关系型市场结构） |
| rehbersanayi.com/ihale/arsiv/sektor/bilisim-ve-yazilim-teknolojileri（IT 归档 547 项/10 页） | 本轮扫描第 1–6 页 ≈120/547 条（最新段 2026-09/10），检索 PnetWorks/PNetworks/PAVO/Ewind/Angora/yerli switch → **0 命中**（部分扫描，非"无中标"证明） |
| 61saat.com（web_search 摘要） | **Trabzon Büyükşehir İKN 2026/1272126（2026-08-05）**：1 omurga + 20 kenar switch + **1 ağ yönetim yazılımı（网管软件）** + 50 AP，**yalnızca yerli istekliler（仅本土可投）** → 与 PNetworks 全栈（TMS 骨干+CMS 边缘+PN-NMS+AC 无线）完全对口的理想画像单 |
| imzagazetesi（web_search 摘要） | **TTK 2025-12-25**：30 台 managed switch；spec 数值 95.24Mpps ≈ CMS24 datasheet（原文误印处）→ 疑似按规格定制或反向，**待核** |
| rehbersanayi 条目（IT 归档） | **İSTTELKOM 2026-09-15**：服务器 + ağ anahtarı + yedekleme **244.6M TL，仅 1 家投标**（大额 switch 采购关系驱动实证）；同期 Bingöl 45M TL / Dugan icra 292.5M TL（笔记本） |
| ensun.io Provider 条目（web_search 摘要） | **#11 = Provider**（Pendik，2018，11–50 人）：区域科技集团，SI/IoT/大数据/云（另见 ensun 系统集成 Top 41）——非 switch 硬件制造商 |

### 9.3 死胡同 / 数据边界

- PNetworks datasheets：10/31 解析成功；**2 份死链 404**（`PN-AC1` WiFi、`pn-cms48ge4sfp.pdf`，勿重试）；其余 ≈19 份未抓 = 低优先级线索（核心规格轮廓已完整）
- rehbersanayi 全量扫描：547 项 = 10 页 × ≤4 chunk，本轮仅扫 ≈120 项 → 全量 = 下轮可选线索
- ensun Top 14 第 12–14 位名称：chunk 边界截断后二次抓取+搜索均无法恢复 → 数据边界，**不重试**
- TTK spec ↔ CMS24 datasheet 95.24Mpps 数值吻合 = **假设**（因果方向未证实，标注待核）
- "EKAP 0 命中" ≠ "无中标"：部分扫描 + 官方 EKAP JS 应用仍是死角（rehbersanayi 镜像是可用替代，但未全量）

### 9.4 落库去向（规则 5 三件套同步）

- `06-competitors/110-turkey-local-competitors-deep-dive.md`：§2（实体修正 + datasheet 实测 + EKAP 扫描 + 2026 标单）+ §7（线索 1 标 ✅、死角更新）+ §8（边界刷新）+ **§9 新增（本轮全量结构化）**
- `110-turkey-local-competitors.csv`：第 1 行（PNetworks）20 列刷新（成立补 2019/3 人；业务线补 NMS；代表产品补 TMS 实测规格+PN-NMS+PN SFP；客户招标补 EKAP 扫描+Trabzon/TTK/İSTTELKOM；证据补 10 份 PDF+rehbersanayi；核验日期 2026-10-08）
- `110-turkey-local-competitors.xlsx`：主清单同步 + 图例页标题/规则行更新（第 14 轮建档/第 15 轮更新）
- 原始材料全量：`99-raw/pnetworks-datasheets-extract-2026-10-08.md`

---

## 10. 第 16 轮（2026-10-08，用户：「都搞了 需你邮箱这个啥意思？」）

### 10.1 用户原话（逐字）

> 都搞了 需你邮箱这个啥意思？

= ① 执行第 15 轮三条低优线索：rehbersanayi 全量 547 条 EKAP 扫描、PNetworks 其余 datasheets、TTK 95.24Mpps 定制关系证实；② 询问"需你邮箱"的含义（= Volza/TradeData.pro 免费样例注册需邮箱，非新信源、非阻塞，回复中解释）。

### 10.2 新增信源（本轮成功）

| 信源 | 关键产出 |
|---|---|
| pnetworks.com.tr 15 份 datasheet PDF（fetch_page 解析，2026-10-08，datasheets 全量收尾） | 累计 **26/27 唯一项**解析完成（1 死链 PN-AC1 + 2 空项 + 2 组重复 URL）。新增实测：LMS24GE2SFP±PoE（52Gbps/240W 预算）、LMS24GE4SFP+PoE（128Gbps/"95Mbps" 笔误）、CMS8GE4SFP PoE（24Gbps，PoE 250W）、**CMS8GE2SFP+PoE+（土语版，L3 表独有 IS-IS）**、CMS48GE4SFP2SFP+（54 口新形态）、CMS48GE4SFP+PoE+（370W vs 240W 自相矛盾）、CMS48GE4SFP 非 PoE（**128K MAC + 30,000 TCAM**，跨表不一致）、CMS24GE4SFP±PoE（4×1G SFP 低配款）、CMS24GE2SFP+±PoE（88Gbps）、**CMS24SFP4SFP+（24×SFP 全光纤+4×10G SFP+ 新形态，唯一端口表与标题一致）**、PN-LMS24GE2SFP（非 PoE，28VDC 疑笔误）、**PN-AC2 = Wi-Fi 6 AP + 4G LTE CPE 二合一**（2.4G 300M/5G 1.3G、LTE 上 150/下 600M、TR-069/WPA3/4+4 SSID/OpenVPN/IPsec、0/+40 °C IP30 = **运营商 CPE 形态，非企业 AP**） |
| **Edgecore 官方新闻稿（MWC 巴塞罗那 2024-02-29）** | Edgecore × PNetworks 战略合作：土耳其市场交付 **Intel Habana AI 加速器 + Broadcom 交换芯片 + SONiC 平台**；Edgecore 总裁 Heimdall Siao 与 **PNetworks CEO Can Okan Dirican** 联名 → TMS 线硬件底座 = Edgecore（台湾 ODM） |
| pnetworks.com.tr About 页（2024-10） | Edgecore 设计覆盖 **400G/100G/25G/10G/2.5G/1G** DC/SP/企业 + IP Infusion OcNOS（2016 起支持 Edgecore HW）；**装机量自述 "~100,000 devices / 80 provinces"（未验证营销口径）** |
| epnext.com（2023-03-07 MWC） | PNetworks 参展，GM **Ömer Ragıp Özkan**（→ 2024 起 CEO = Dirican，高管更替） |
| **taskomuru.gov.tr TTK 技术规格书 PDF（6 页全文）** | TTK = **Türkiye Taşkömürü Kurumu（土耳其煤矿机构，宗古尔达克）**（更正第 15 轮"国铁"误读）；3 类：①骨干 24SFP+8combo+4SFP+ 128Gbps/95.23Mpps/16K MAC/MTBF≥760,000h；②24GE+4SFP+ 128Gbps/95.24Mpps/16K MAC/768 ACL（含时间基）；③48GE+4SFP+ **176Gbps/130Mpps/32K MAC**；**2.2.40：SFP/SFP+ 必须与交换机同品牌、拒绝 OEM 光模块**；3.3 制造商授权书；3.9 售后资质；3.10 30 天交付宗古尔达克；2 年保修 |
| imzagazetesi（2025-12-25） | TTK 30 台（总管理处+下属企业合并），**投标截止 2026-01-15 14:00** |
| rehbersanayi.com（IT 归档分页机制穷举） | 第 1 页 HTML 全量 = **60 条**（2026-10-06→09-28，chunk 0–3，第 4 chunk = 页脚）；`?page=2`/`?sayfa=2`（www/非 www）参数被忽略、`/…/2` 路径 **404**、无公开 API、`/ara?q=pnetworks` = 0（仅企业目录）、Google 索引 site: 检索 0 → **无浏览器环境穷举边界 = 60/547 + 三路旁证，0 厂商命中** |
| n11.com（PNetworks 品牌店，2026-10） | **CMS48GE4SFP+ PoE+ 156,612 TL**（活动 144,666）；"Pn48ge4sfp Poe+" 150,812 TL（活动 139,301）→ 48 口 PoE+ 零售 14-15 万 TL 量级，电商公开在售 |

### 10.3 死胡同 / 数据边界 / 更正

- **rehbersanayi 全量扫描 = 收口（勿重试同类方法）**：547 条中服务器端 HTML 仅暴露 60 条（第 1 页）；其余 487 条 = 客户端 JS 分页，无公开 API，`/ara` 不覆盖中标记录 → 无浏览器环境下**已到穷举边界**。如需 100% 全量 = 下轮上浏览器渲染 或 EKAP 官方 API 账号
- **更正第 15 轮 "≈120/547" 误估**：第 15 轮按"6 页 × 20 条"估算 ≈120 条，实际第 1 页 HTML 仅 60 条（chunk 3 = 页脚而非记录）。正确口径 = **60/547（2026-10-06→09-28）**；"0 命中"结论不变且加强（+ 站内目录搜索 0 + Google 索引 0）
- **更正第 15 轮 "pn-cms48ge4sfp.pdf 死链" 误记**：实为取 URL 时打错——大写 URL `PN-CMS48GE4SFP.pdf` 可正常访问（本轮已解析）。唯一死链 = **PN-AC1（WiFi，404 勿重试）**
- **TTK "95.24Mpps 按 PNetworks 定制" 假设 → 降级为不成立**：官方规格书 3 类数值（95.23/95.24/130Mpps）= 24GE+4×10G / 48GE+4×10G 的市场标准线速参数；PNetworks CMS24 印 "95 Mbps" = 标准值笔误。无定制证据（数值吻合 = 同源标准参数）
- **PNetworks 面板照片 = 其他品牌**（PACIFIC WIRELESS / PRESTIGE / PowerConnect(华为系) / PROTECTED / 带 VGA/HDMI 的非交换机面板）→ 白牌 ODM 平台复用实锤，与"自有设计"叙事矛盾
- PNetworks "~100,000 devices / 80 provinces" = 官网自述，**未验证**（与 EKAP 0 命中并存 = 非公共标单渠道为主）
- 补充市场信号（60 条内）：Bilgibim 36.5M TL 延保 1 家投标；CCC Command Control 58.1M TL 气象站硬件 1 家投标 → "≤2 投标常态"再验证

### 10.4 战略含义（本轮定稿）

1. **PNetworks "本土"成色最终定级**：本地化品牌 + 软件集成（SONiC/OcNOS）+ 防务叙事 + Teknopark/国家背书；**硬件 = Edgecore（Broadcom 芯片）+ 白牌 ODM 贴牌**——与 Angora×Ewind 结构同构，"我方 vs Angora/PNetworks" 共享同一 ODM 上游池逻辑
2. **同品牌光模块条款（2.2.40 型）= 我方进 TR 标单的结构性门槛与机会**：整机+光模块同品牌、拒 OEM 光模块 → 我方投标须捆绑自品牌 SFP（成本 ¥25/只，无压力）；全栈（含 optics）= 结构性投标资格优势，PNetworks 自产 PN SFP 的战略价值在此类条款下兑现
3. **PNetworks 竞争位势修正**：第 15 轮"渠道窄"部分降级——若 ~100K 装机自述属实，其企业/运营商**非公共标单**渠道渗透深；EKAP 可见度低 = 渠道结构（直销+集团关系），非能力弱。监控点从 EKAP 中标量 → **企业/运营商侧客户案例 + n11 零售价变动**
4. **我方两个正面战场结论维持**（工业 8 口 L2+ = 现在；企业 L2+/L3 对标 Mikrotik = 经 ELCORE/Poyraz）；PNetworks 主战场 = 运营商/DC/防务/公共 "yerli" 单

### 10.5 落库去向（规则 5 三件套同步）

- `06-competitors/110-turkey-local-competitors-deep-dive.md`：§2（硬件底座真相块 + 招标/客户情报刷新 + n11 零售）+ §7（线索 1 标 ✅ 关闭）+ §8（边界刷新 + 4 处更正/降级）+ §9.2/9.3 就地更正注 + **§10 新增（本轮全量结构化）**
- `110-turkey-local-competitors.csv`：第 1 行（PNetworks）9 字段刷新（集团/业务线/代表产品 26/27/本土化程度定级/客户招标 TTK+n11+EKAP 收销/我方威胁/建议动作 2.2.40/关键证据/备注）+ 第 15 行（Ewind）客户招标加 EKAP 收口注；核验日期 2026-10-08
- `110-turkey-local-competitors.xlsx`：主清单 20×20 重建（20 行 × 20 列，表头与 CSV 逐字段一致，回读校验通过）+ 图例页"第 16 轮更新"行
- 原始材料全量：`99-raw/pnetworks-round16-fullscan-2026-10-08.md`

## 11. 第 17 轮（2026-10-08，用户：邮箱 + 启扬 PASS + 「继续挖掘相关的土耳其公司 越多越好」）

### 11.1 用户指令（要点）

- 邮箱 **s.sagatelecom@gmail.com**「用这个邮箱吧」→ Volza/TradeData.pro 免费账号注册用（业务注册邮箱，非密钥；本轮如实记录，不重复打印）
- **启扬（郑州启扬工控）关系 = PASS（关闭，不再追问）**
- 主任务：**「继续挖掘相关的土耳其公司 越多越好」**= 角色分层全量挖掘（本土 OEM/品牌、白牌 ODM、渠道分销、集成商、DC 运营、消费品牌、企业买家），结果全部落库（规则 5 三件套 + 99-raw + 台账）

### 11.2 新增信源（本轮成功）

| 信源 | 关键产出 |
|---|---|
| rehbersanayi.com EKAP 镜像 IT 归档（60 条重取，2026-09-28→10-06，İKN 全记录） | 60 条中标者全部名实 + 金额 + İKN；提取 IT 硬件/软件中标商 ~30 家（Balkan 93.2M/CCC 58.1M/Bilgibim 36.5M/Venka 27.5M 企业网络集成/İnnova 24M/Arkenom 12.5M/Teknosis 12.1M/Fonet 11M/Artı ve Artı 10.8M/Mavi 10.2M/BNTPRO 7.5M/Docuart 6.5+6.2M/…）+ 医疗 ~12 条 + 非 IT ~28 条（Serkan Çankaya 32.2M 施工/Aygün 129.4M 运输）；模式 = 本地小型 SI、1 家投标主导 |
| ensun.io Top-14 "switch maker Turkey"（密排列表名丢失问题解决） | 14 家全部名实识别：#1 Netsite（Cisco 2960-X 分销）#2 Prolink #3 **Mekrotik（= ISP，与 MikroTik 纯撞名）**#4 UPCOM TR #5 Angora #6 Trustnet #7 DECKRO（机架制造）#8 **StorNET Networks（Beylikdüzü 2015 = 此前未识别的神秘实体）**#9 Provider；ensun 统计"5 制造商+3 服务商"= 低质名录，仅作名字发现 |
| makinaturkiye.com（Longline 公司页 + 2 商品页，2026-10-08） | **Longline Bilişim（Bayrampaşa）= 土耳其本土白牌工业交换机品牌**：LNG5700-8TP2S（8×1GE PoE+ + 2×1G SFP，L2，56Gbps，8K MAC，**7,182 TL，"Menşei: Türkiye"**）+ LNG5863-24X2C（24×10G SFP+ L3 静态/RIP/OSPF，256Gbps，32K MAC）；另翻新 Dell/HPE/Lenovo/IBM + 分销 Cisco/HP/Juniper/Dell/Huawei + SFP/media converter + Fluke；市场 RU/CN/Dubai/US/EU |
| netgaste.com 工业交换机指南（2025-10-14） | −40/+75 °C 金属壳 DIN 导轨 PoE（16/24/8 口 GbE PoE + 5/8 桌面 + 24 L2）——疑 Longline 软文，细节待核 |
| stornet.com.tr / linkreal.com.tr / sunucudeposu.com（2026-10-08） | **StorNET Networks（Beylikdüzü Skyport Residence 1/70，2015）**= 网络/服务器配件分销（Intel/Broadcom/Mellanox 网卡、DAC/AOC、SFP、RAID）；**自有品牌 = 同 chipset 换牌**；**LR-Link（中国工业交换机）土耳其分销**；售 Marvell/QLogic chipset 产品；关联实体 SUNUCUDEPOSU BİLGİSAYAR（Emir Pelin Ateşer）同址；25G DAC 2,100 TL |
| trdunya.capital / investing.com / tradingview（ALCTL 资料，2026-10-08） | **ALCTL（BIST）= Alcatel-Lucent Teletaş**：1983，Ümraniye OSB 2.Cadde 17/1，381 人，CEO Özgür Deniz Erzincan，董事长 Önder Sönmez，**86%+ 芬兰 Nokia 持股**（2026-04 股价≈₺107.3）；分部 Cloud&Network Services + Network Infrastructure；TR/芬兰/国际运营商设备制造 |
| labrisnetworks.com（2026-10-08） | **Labris Networks**：HARPP® DDoS Mitigator（DDI）+ Labris UTM（本土 NGFW）+ **Labris MNG（集中管理 appliance，运营商级 = NMS 模式）**+ Labris LOG（5651 日志）；行业=政府/国防/电信/电商/游戏/DC |
| barikat.com.tr（2026-10-08） | **Barikat**（300+ 专业人，"Our Business Is Only Cybersecurity"）：**ICS Firewall（工控防火墙）**/NGFW/DLP/NAC/负载均衡/包路由/CTI/托管安全 |
| cbddo.gov.tr（总统府，2023-08-03） | **16 家国家网络安全企业官方名单**（与大学配对）：Barikat/Labris/Türksat/STM/Adeo/TT/Procenne/Ölçsan/Vestel/Parta/Kron/Fileorbis/Turkcell/**Pavo Grup**/Gais/BugBounter → PAVO（PNetworks 母公司）再次国家级证明 |
| siberkume.org.tr（集群产品目录，2026-10-08） | **TÜBİTAK BİLGEM** 产品：Derbent VPN/ORION DLP/A3 司法取证/MERGE-N/Siberlab/**Kuantum Pi 防火墙（最新）**/Kapan；Labris/Barikat 展会数据 |
| cybermagonline.com（2021-02-23） | **Berqnet** = Deloitte Tech Fast 50 Türkiye 2020（当年唯一防火墙品牌）；Kocaeli；GM Hakan Hintoğlu |
| compatlas.com.tr（目录，2026-10-08） | **PONIVA/PONA**（Gaziantep：firewall + Turkuaz VPN + XDR，本土生产）；Berqnet 代理 |
| netas.com.tr（EN 页）+ htk.org.tr + sektorel.com + 2020 年报 PDF（2026-10-08） | **Netaş 全产品线补全**：1967 PTT×Northern Electric；**800+ R&D 工程师**；三 BU（IT/通信/ArGe+BDH）；**NETSWIFT = 土耳其首台本土服务器**；**5G 本土生产**（ULAK 基本带）；防务战术野战网（100% 本土）：**SGN/MAGN 洞室以太网交换机+IP 路由、IAS 移动以太网交换机+IP 路由**；IP/ATM/ISDN 交换、MOLTU（SDH）、eMUX、舰船通信；V2X OBU/RSU（2020）；**GNSS 精密时钟发生器（2023）**；Orhanlı 厂=军规硬件测试；伊斯坦布尔机场全 ICT |
| evrenozmen.com.tr ×2 + datacenters.com/locations/turkey + turksem（DC 情报，2026-10-08） | **TR DC 全景**：Turkcell 8 DC 41.5MW+8.4MW（TWF €100M 融资）、TTK Esenyurt/Gayrettepe/Ümitköy 12,700m²、Vodafone Esenyurt 10MW + İzmir 13,500m² 在建（Edgnex/DAMAC）、银行（İşbank Atlas **Tier IV**/Akbank Gebze T3/Halkbank Tomurcuk T3/Ziraat Esenyurt T3/Yapı Kredi Çayırova T3）、DGN（Bursa，ISO27001）、Radore（Levent 2004）、**Telehouse Istanbul/Teknotel = KDDI**、**Star of Bosphorus/NGN（Tuzla 16MW，2,000+ 机柜，Tier III）**、Datacasa、PenDC（Konya）、Premier DC、Mars、Yöncü、İşNet、Netdirekt、Netinternet（Denizli）、ICS、Worldbus、DataPacket、**Equinix IL2/IL4/IL5 Dudullu（收购本土 Zenium）**、**Khazna（G42 阿布扎比）Başkent OIZ 最高 100MW（2025-04）**、Kyndryl |
| oft.com.tr / tekiziletisim.com / ensun fiber 页（2026-10-08） | **OFT（Gaziantep Şahinbey，1985）= 自有 GEPON OLT/ONU + media converter + 光缆/ODN，"TR+MENA GPON turnkey No.1"**（GPON niche 本土第二参照）；Turkuaz Kablo（İzmit 2000）、OPTOKON（Muğla）、Netcom、Tekiz（FTTx 施工商）；ensun：37 家线缆厂商均值 51–100 人 |
| poyraznetwork.com / safirteknoloji / wifianten / kablosuzdestek / enucuzmikrotik / telsanbilgisayar / kurumsalit（渠道情报，2026-10-08） | **Mikrotik 土耳其渠道 = 多主代结构**：**Poyraz Network = Master Distribütör（2015 起**，RouterBOARD/CCR/CRS 全品库存 + RouterOS 许可 + 认证技术支持；另 Ubiquiti/Mimosa/Cudy/RF Elements）+ Safir Teknoloji（授权分销）+ wifianten（自称 master）+ Ctech Bilişim（自称 master）+ Kablosuz Dünya A.Ş.（Ubiquiti/Mikrotik/Cambium/Mimosa/**Ruijie**/Dahua/TP-Link）→ 渠道权力分散，Ruijie 已在 TR 渠道体系（中国系先例） |
| hepsiburada（AP 零售锚点，2026-10-08） | 土耳其 AP 零售价：TP-Link EAP225-Out 1,999 / UniFi 6 LR 4,999 / EAP670 5,999 / WAX630E 7,999 / Meraki MR36 24,999 TL；**Everest = 土耳其消费级 Wi-Fi（EWR-301 211 TL），企业 AP 货架无本土品牌**（第 14 轮"本地企业 AP ≈ 空白"结论再验证） |

### 11.3 死胡同 / 数据边界 / 更正

- **Volza 公开公司页 = 注册墙（收口，勿重试 fetch）**：volza.com trade-partners-for-angora-networks-ankara → 404/试读墙（Free 7-Day Trial）；注册需交互式表单 + 邮箱验证，本环境不能完成。用户邮箱已登记为注册用；**TTD 免费样本（2023-08→2024-07，21 票）已覆盖关键窗口**，Volza 注册后为增量验证非必需
- **ensun 密排列表名丢失 → 解决**：#8 名实 = StorNET Networks（经定向搜索识别，非重新抓取）；ensun 不再作为主信源（仅作名字发现）
- **rehbersanayi `/ara?q=switch` = 0 结果**（目录不覆盖中标记录的关键词检索）——边界维持 60/547
- 无新增误判更正（本轮为增量挖掘，无既有结论推翻）

### 11.4 战略含义（本轮定稿）

1. **第一战场对手名单更新**：工业 8 口 L2+ PoE 线新增 **Longline**（7,182 TL "yerli" 白牌，小体量）= 与 Ewind（深圳 ODM）并列监控；我方 875 RMB 成本位 + 自品牌 optics 组合仍可正面打
2. **"yerli"叙事三层分离完成测绘**：①制造叙事（Netaş/ALCTL-Nokia/Aselsan 国家队，不抢我方价位）②白牌叙事（PNetworks/Longline/Ewind = 直接竞对，同源 ODM）③换牌分销（StorNET = 非竞对，可供货）——我方只需打第二层
3. **渠道 = 本轮最大可操作产出**：**Poyraz（Mikrotik master 2015 起）确认** = 97 号双轨候选主力通道价值再证（进入 Poyraz 体系 = 进入基准品牌主渠道）；多主代结构 = 分散化备选（Safir/wifianten/Kablosuz Dünya）；Ruijie 在 TR 渠道存在 = 中国系可行性验证
4. **DC 需求引擎确认**：TR DC 建设潮（Turkcell +8.4MW、Khazna 100MW、Edgnex İzmir）= TMS/DC 线市场窗口；进入路径 = 经 PNetworks/ELCORE/Angora 通道，非直销；本土 DC 被并购先例（Zenium）= 渠道/品牌资产价值信号
5. **官方名单锚点**：总统府 16 家国家网络安全企业（2023-08）含 PAVO Grup/Barikat/Labris/Türksat/STM/Turkcell → 防务/国家安全域 = PNetworks 集团主场，我方不进入
6. **ALCTL（Nokia 土耳其工厂）= "yerli 制造"话语硬参照系**：不同战场（运营商/国防），低直接威胁，但定义叙事天花板

### 11.5 落库去向（规则 5 三件套同步）

- `06-competitors/110-turkey-local-competitors-deep-dive.md`：**§11 新增（本轮全量结构化）**
- `110-turkey-local-competitors.csv`：**19 → 80 数据行 × 20 列**（新增 61 行：B 层 Longline/StorNET/ALCTL + C 层 OFT + F 层 Mekrotik/DECKRO/光纤 + D 层安全簇 6 行 + H 层 DC 20 行 + G 层渠道 2 行 + I 层公共 IT 24 行 + J 层 2 行；更新 Mikrotik/Keenetic/PNetworks/Netaş 4 行；核验日期 2026-10-08）
- `110-turkey-local-competitors.xlsx`：主清单 **81×20 重建**（表头与 CSV 逐字段一致，回读校验通过）+ 图例页 tier 扩至 A–J（+H 数据中心/终端客户、I 公共 IT 集成生态、J 低相关仅记录）
- 原始材料全量：`99-raw/turkey-companies-round17-2026-10-08.md`

## 12. 第 18 轮（2026-10-08，用户：「双轨3选1啥意思？不考虑合并不要提了 / 继续 尽最大努力挖出最多的信息」）

### 12.1 用户指令（要点）

- ① 询问"双轨 3选1"含义 → 已答复（97 号锚点战略：轨道 A=Angora 公共 niche 保留 / 轨道 B=ELCORE+Poyraz 量级主力；白牌三选一 = ① 我方自有品牌直供 ELCORE/Poyraz ② ELCORE 系白牌借其 11 国渠道 ③ 继续 Angora 贴牌仅公共单）
- ② **常设指示：PR 合并不再考虑、不再提及**（TASK-STATUS 行 20 记录在案，后续回复不得再提）
- ③ 主任务：**继续，尽最大努力挖出最多的信息**（第 17 轮"越多越好"的延续，无新常设规则）

### 12.2 新增信源（本轮成功）

| 信源 | 关键产出 |
|---|---|
| **siberkume.org.tr/katalog/urunler（TSGK 土耳其网络安全集群官方目录，2026-10-08）** | **373 产品/26 类目 + 集群成员全名单 A→Z ≈150+ 家**（全抓，99-raw §1.2）；网络相关类目：网络与基础设施安全 76/安全运营 59/身份访问 60/数据安全 31/应用 30/威胁情报 18/**网络设备 8**/防火墙 11/NAC 4/**跨域数据二极管 6**/ICS 5+2；**⭐ 网络设备 8 项全名单**：ASELSAN×3（军规/工业国产路由器族 + KKAC 加密 Wi-Fi AP）+ ULAK×3（MİLAT 虚拟交换机/UMAYA YT-GAA/UMAYA YT-VM）+ PARTA×2（Targitas SD 安全路由/SD-WAN）→ **官方本土目录无企业级 L2/L3 管理交换机 = 结构性空档证据**；巨头成员 = ASELSAN/HAVELSAN/STM/VESTEL/ARÇELİK/KOÇ SİSTEM/SABANCI/KAM/ULAK/NETAŞ/TÜRKSAT/TT/TURKCELL/BİTES/DeYTEK 等（与总统府 16 家名单双层互证） |
| siberkume 公司页/产品详情页（Google 索引快照） | **ASELSAN 网络设备线**：VERİ DİYODU 数据二极管（单向，军/民版，"yerli ve milli"）/Sanal Hava Boşluğu 虚拟气隙/10G KC 加密/GİZ USB/TKABC 加密 Wi-Fi 终端；**数据二极管 = 6 个产品**（ASELSAN×2 + CRYPTTECH + 其余 JS 区待核） |
| tr.linkedin.com/company/crypttech + siberkume | **CRYPTTECH Kriptek**（2006，İST YILDIZ + ANK Hacettepe 双 Teknopark，数据二极管/Netzilo/Siber Koza AI，自述 1,000+ 大客户+3,000 SME，硅谷办公室 = 出口导向） |
| **tr.linkedin.com/company/longlinebilisim + makinaturkiye 公司页 + hepsiburada（Longline 重大升级，2026-10-08）** | **成立 2000；2008 年起自研产品族（首个产品 = SFP 光模块）；11-50 人**；**全产品线 10 型号**：桌面 5 口 750 TL（hepsiburada，24 月保修）/LNG5700-8T2S/**LNG5700-8TP2S（7,182 TL "Menşei: Türkiye"）**/LNG5700-24T4S/LNG5710-28TX（L3）/**LNG5720-24MP6X（2.5G L3 PoE）**/**LNG5630-24TS4SX（Combo L3 49,000 TL）**/LNG5720-8H（L3 10G）/10G 48 口汇聚/**LNG3000-8TP2S-IK（工业 L3 PoE）**；SFP 全线兼容 13 厂商；另售 Huawei S310 → **威胁定级 中-高 → 高（与我方 SFP/工业/企业 L2+L3/10G 逐线重叠）** |
| **pnetworks.com.tr（+about-us）+ c4defence 2022-03-17 + savunmatr 2024-03-01 + instagram（PNetworks 增量，2026-10-08）** | 总部 = Teknopark İstanbul 4C Kat:1-2 Pendik；**⭐ L&N = 官方公共渠道（2022-03-17 联合发布，口号"土耳其的数据交给土耳其的交换机"）= 97 号 L&N 通道假设实锤 + 我方走 L&N 的利益冲突点**；MWC 2024（GM Özkan = 欧洲进入/出口启动）；IG bio = "Turkey's First Domestic Switch Manufacturer"（2,244 粉）；about-us：Edgecore+IP Infusion 双伙伴 + "Made in Türkiye" 标签战略 + ~100K/80 省自述（维持未验证） |
| **poyraznetwork.com/tr（Dealer Dashboard + 产品页 ×3，2026-10-08）** | **⭐ Poyraz 品牌矩阵全量**：Mikrotik = Master Distribütör（站内自证标签）；授权 = Ubiquiti/Aqara/Mimosa/Tachyon/Cudy/**V-Sol（中国广州 GPON）/RF Element**；另售 = Tenda/Deltalink/Wiss Network/Ignitenet/**Ruijie（中国）/PN-Link**；10 年+/**5,000+ SKU**/15:00 当日发货/7-24 支持/B2B 经销商注册（Bayi Olun）/AI+Matter+Edge 愿景；**PN-Link 实证 = 中国低价被动 PoE**（GPOES-8-7 2,167.75 TL；注入器 395.52–2,501.25 TL，10/100M，CE/ROHS）→ 中国品牌（V-Sol+Ruijie）已在组合 = 我方品牌入组合零排斥先例 + 新重名陷阱（PN-Link vs PNetworks） |
| **elcoregroup.com（首页实测，2026-10-08）** | **19 年/70+ 供应商/1,500+ 活跃伙伴/8 本地子公司/100+ 团队**；供应商墙 = Huawei/HPE/Dell/Nokia/Supermicro/Bosch/TrendAI/Hitachi V/Motorola/Paradox/Engenius/Kaytus/Opentext/FileCloud/Scality/PentaSecurity/Sectona/NxLog +（97 号）MAIPU〔中国〕/Sangfor/Blackwall = 量级主力通道深化 |
| bthk.org 2025 Q1 报告 PDF + markahost 2025 + dmo.gov.tr 检索快照（买家池，2026-10-08） | **BTK 58 家持牌活跃 EHS**；ISP 份额 2024 = %54/%39/%6（TT/Turkcell SO/Vodafone Net 三寡头 + TurkNet/Türksat Kablo 等）；**dmo.gov.tr 政府设备目录 = 230 交换机型号 + 7 路由器 + 95 SFP**（多品牌开放含美系 EXTREME = "yerli" 非目录门槛） |
| AA 2020-06-07 + hurriyet 2020-01-30 + turk-internet.com 2025-03-05 + TT 新闻稿 2016-02-18（ULAK 深挖，2026-10-08） | **ULAK Haberleşme = ASELSAN 持股 51%**；SSB MİLAT 项目（2015 起）→ MAYA SDN/NFV；产品 = MİLAT 虚拟交换机/MAYA SD-WAN/UMAYA YT-GAA/YT-VM/ULAK 基站（ASELSAN 主承包 + Netaş+Argela 分包）；**商用落地：Türksat MAYA SD-WAN 生产网在用 + TT×农业林业部 500 点位合同 + 250 基站交付 TT + Gazi 大学** |
| 61saat.com（Trabzon İKN 2026/1272126 公告） | 2026-08-05 10:00 开标（4734/19 公开招标）：1 骨干+20 边缘+1 NMS+50 AP = PNetworks 全栈对口；**中标结果仍未验证**（EKAP 需 JS，维持监控） |

### 12.3 死胡同 / 数据边界 / 更正

- siberkume 类目页产品网格 = JS 渲染（静态 HTML 无产品；公司名单 + 类目结构 + Google 索引快照 = 本环境可得上限，勿重试同类抓取）
- n11 品类 URL（/endustriyel-switch）= 404；n11 搜索页 = JS/反爬（维持第 16 轮品牌店口径，勿重试）
- dmo.gov.tr 检索页 = JS 渲染（统计数字来自 Google 索引快照，标注来源）
- 无既有结论推翻（本轮为增量挖掘 + Longline 威胁升级 + L&N 冲突确认）

### 12.4 战略含义（本轮定稿）

1. **Longline 升级为第一+第二战场双线对手（高威胁）**：2000/2008 老厂叙事 + 全价位带 750→49,000 TL + 工业 L3 PoE + SFP 全线；我方不与其争叙事，打成本 + optics 捆绑 + Poyraz 渠道；监控 = hepsiburada 周检
2. **双轨两通道全量取证完成**：Poyraz（Mikrotik master + V-Sol + Ruijie 已在组合 = 中国品牌零排斥先例；B2B 经销商注册 = 进入机制明确）+ ELCORE（19 年/70+ 供应商/MAIPU 先例/品牌边界条款 = 落地前提）
3. **L&N 利益冲突确认**（2022-03 联合发布）：97 号辅助通道需处理排他条款，或降级为纯公共投标代投方
4. **"yerli 网络设备"官方版图完成测绘**：制造（Netaş/ALCTL/Aselsan）+ SDN（ULAK-ASELSAN 系）+ 安全（16 家+集群 150+ 家）+ 白牌交换（PNetworks/Longline，集群外）——企业交换价位带官方本土空档 = PNetworks 单点占据（"First Domestic Switch" 叙事），我方不进入官方叙事，打价格带
5. **买家池定义**：WISP/酒店/宿舍（Mikrotik 客群 = Poyraz 可及）+ 政府目录（多品牌开放）；三大寡头不打；ISP 三寡头集中度 54/39/6%

### 12.5 落库去向（规则 5 三件套同步）

- `06-competitors/110-turkey-local-competitors-deep-dive.md`：**§12 新增（本轮全量结构化）**
- `110-turkey-local-competitors.csv`：**80 → 88 数据行 × 20 列**（新增 8 行：ULAK/EPATİ/CRYPTTECH/SECUNNİX+Arjeta 打包/TSGK 全名单打包/PN-Link/ELCORE/ISP 买家池；更新 6 行：PNetworks/Aselsan/L&N/Longline(重大)/Poyraz/V-SOL；核验日期 2026-10-08）
- `110-turkey-local-competitors.xlsx`：**89×20 重建**（表头与 CSV 逐字段一致，回读校验通过；图例刷新）
- 原始材料全量：`99-raw/turkey-companies-round18-2026-10-08.md`

## 13. 第 19 轮（2026-10-08，用户：50 家客户名单 + 「深搜评估，只写优质/对标客户，无关不要」+「二极管类信息后续不要再找」+「3 个渠道都要先挖掘后续再定」）

### 13.1 任务与判定规则

- 用户给出 50 家土耳其公司（URL + 两列 AI 评估百分比 + 联系人 + 来源 + 备注），指令：① 全部深搜评估；② 只把**优质客户/对标客户**写入 MD+Excel；③ 无价值/不相关不收；④ 用户备注与 AI 评分列 = **参考输入，不得直接引用为证据**，结论必须来自独立核实
- **收录标准（写入 raw §2）**：写表 = ① 官网实证 switch 产品线 ② 供应开放信号/场景匹配 ③ 可执行动作；不写 = 不相关/红灯品牌深绑/404 失联/无法触达（逐家留原因）

### 13.2 逐家深搜（50 家全量，fetch 官网 7 家 + web_search 站点索引 16 家 + 双 AI 交叉 27 家）

- ⚠️ 环境故障：会话后段 fetch_page 代理 OSS InvalidAccessKeyId（两批重试均失败）→ 受影响家改 web_search，行内标注"search 核实"
- **收录 23 家**（2 组合并：#10+#23 同集团〔官网自证 "Telkolink, GelecekBT'ye aittir"〕、#9+#29 同 Asya Telekom 集团）：
  - **A 核心 5**：Telkolink+GelecekBT（Perpa 批发分部 + CLR〔深圳〕品牌 + 进口商 + 品类与我司逐线对应，含 2.5G multirate/800G SFP/工业 MC）｜NOVA（**PoE 类目 31 SKU 全自有 NVC/NCV/ND**）｜Snexus（**全 ladder 自有：P&P PoE → Managed 10G L3 SN-XGS5300 $1,130-2,750 → Fiber Omurga → 工业**，自述 L3=硬件 RIP/OSPF/BGP）｜Cenova（CCTV 品牌 + 自有 SWP/DL PoE 8 款）｜CryptoLink（**CRL 自有 7 份 datasheet：24 口 L3 10G/工业 CRLISW/SFP-10G**，公共机构客户 → **轨道 A**）
  - **B+ 3**：Coptek（DCN omurga L2/L3 + ONV 工业 18 口 L2+ 受管 PoE + DONGWE 光转）｜Karer（**KARER 自有 PoE 6 款 $40-150，库存 1000+**）｜Hane（FOREDGE+VIDEOPARK 双白牌 PoE 25 款 + SFP）
  - **B 12 / B- 3**：Öncü（**Sec-on 自有工业 PoE**）/ErETE（XPS+**EdgeCore ECS4660-28F L2/L3/L4**）/Eretekne（XPS+EtherWAN）/CCS（**BC-ODS 白牌**+Reyee $911）/Rima（Antaira 工业，库存 103 项）/NFS（Surenix/Oinone 现货）/Koza（GreenTech 集团，CPSE 2023）/Portel（3OneData 工业）/RF Teknoloji（3Onedata 专代）/iotsistem（MLB 工业受管，**联系人已有回复 = 唯一暖线索**）/Lansan（LNS 自有，8 口 PoE 标价 $1,000 异常）/Opax（自有 PoE $31-37，.pl 联系人待核）/CCTV Depo（**SECUZI 自有 305m 长距 PoE**+Bayi B2B）/TeleOne（AI CCTV，switch 类目部分验证）/Konak（OPAX 渠道，多业务混杂）
- **排除 24 家**（逐家原因 raw §1.1；第 22 轮计数复核更正 26→24，50 = 25✅→23 行〔2 合并〕+ 24❌ + 1 entegron→110 行 20）：红灯深绑 6（mfd=西门子/areskom=Westermo/okisan=Dahua+Tiandy/intenet=Raisecom/teamon=Planet+Ruijie/bimel）｜自研封闭/无关 7（gmt=本土 PLC 厂/pavotek=防务/optima=物理安全厂/technopc/dacel/fiberden/metcom）｜规模过小 3（egemen/lemax/teknolojipazar）｜失联/404/未证实 8（filiz/inovatech/tekmarshop/kirac/baburtek/radioteknoloji/eurocam/cebecigrup）

### 13.3 ⭐ 重大更正：#44 Entegron = LONGLINE 第二品牌（客户 → 竞对）

- entegronnetwork.com 官网：about = "**Established in 2000, LONGLINE Technology Ltd**… specializes in PoE solutions and optical fiber communication products"；地址 **Longline Plaza No:18, 34040 Bayrampaşa**（= 110 行 20 同址同年）
- 质量页 = "as Longline… **Longline test center**… **CE, RoHS, ISO 9001, FCC**"（本地自有测试中心）
- **Entegron 品牌 57 SKU** = Ethernet Switch 11 + **PoE Switch 31** + EPON ONU 9 + GPON ONU 6 + GEPON OLT（1U 8 口/4 口 EPON）+ 10G intelligent access（8GE+4×10G SFP）+ **ENTDPS208P Reverse PoE EPON ONU MDU（FTTB）**
- 结论：Longline = **双品牌运营商**（LNG switch 线 / Entegron PoE+FTTx 线）；威胁维持**高**，重叠面扩至 PoE/FTTx/10G → **110 行 20 三件套同步更新**（CSV/XLSX/MD §12.6）；用户对该家备注（E-wind/GXCOM 在售）不采信为客户证据

### 13.4 用户新常设（第 19 轮，已写入宪法级规则）

1. **不找二极管类信息**（"我司业务没有二极管类产品 只是angora有 所以后续不要再给我找二极管类的信息了"）→ 后续任何回复/挖掘不得主动呈现二极管类信息（110 既有行按只增不删保留，不再深挖）
2. **白牌 3 渠道全部先挖掘，后续再决定**（"3个渠道都要 先挖掘 后续我再根据情况决定"）→ 97 号锚点战略决策项关闭为"并行挖掘"：轨道 A（Angora 公共 niche）+ 轨道 B（ELCORE/Poyraz/白牌 ①②③）全部保持情报更新，等待用户依情况拍板

### 13.5 落库去向（三件套同步）

- **新建** `08-customer-pipeline/` 目录：`111-turkey-customer-pipeline.md`（叙事 + 分级 + 跟进优先级）+ `.csv`（23×17 utf-8-sig）+ `.xlsx`（24×17 含图例页，回读校验通过）
- **更新** `06-competitors/110-*` 三件套：Longline 行（代表产品 + 威胁 + 备注 + 核验日期）+ XLSX 重建 + MD §12.6
- **原始**：`99-raw/turkey-customer-list-round19-2026-10-08.md`（50 家 verbatim + 去重关联 + §2 收录标准 + §1.1 逐家核实结论表 + Entegron 更正块）

---

## 14. 第 20 轮（2026-10-08，用户：IASF 2025 展会客户名单 50 条〔49 编号+1 无号〕 + "同样要求 搞一下" = 第 19 轮标准）

### 14.1 输入与判定

- **输入**：IASF 2025（2025 土耳其安博会）展会客户名单 50 条（49 编号 + 1 无号 Khaled；国别列部分为空；含境外访客 Serbia / Palestine / Libya×2 / Greece / Bulgaria / 北塞）
- **标准**（沿用 r19 用户指令）：① 逐家深搜全部 51；② 只把优质/对标写入 111 管线（扩既有三件套，17 列）；③ 排除逐家留原因；④ 用户现场记录 = 参考（联系人/需求线索进"联系人/备注"列，**不作公司证据**）；⑤ 不涉二极管类；⑥ 不提 PR
- **结果**：50 = 新增 22 行（#24-45：B+3 / B2 / B-17）+ 并入现有行 1（#64 = 既有 A 核心 #3 Snexus，行 3 更新）+ 排除 27
- **管线总计**：111 三件套 **45 行**（A 5 + B+ 6 + B 14 + B- 20）

### 14.2 新增 B+（3 家，本轮最高价值）

1. **#24 SFPTURKEY（İstanbul）**：SFP 进口-出口商（GENERIC/ARUBA-HP 兼容 1G/10G SFP/DAC + switch + MC + 光纤网卡，3 年换新）+ **自有品牌 GigaCom/geMaxx** + 4 域名矩阵 → **我方 SFP 线（¥25 价位带）核心对标 + OEM 双品牌潜力**；现场 = 为客户推荐 万兆光/2 光2 电/2 光4 电/带 bypass（Evelyn 客户）
2. **#25 HAFYA Technologies（İstanbul）**：安防+弱电集成（相机 + **IT 基础设施：有源网络设备/机房** + 门禁/turnstile + 楼宇自动化）→ 现场 = **军队项目，要防水工业 4 光8 电 PoE 网管规格书**（3 人团队，合照）= 轨道 A（防务/公共 niche）新入口
3. **#26 Makros AŞ（İstanbul）**：**i-PRO（Panasonic）土耳其 Premium Distributor**（官网自证）→ 现场 = 工业级工程需求已谈价（$130/$150 DDP 双清包税，合照）

### 14.3 新增 B（2 家）

- **#27 ONSİS（Ankara）**：1992 年起安防系统商；**GM Esef Taşkiran = 用户联系人 esef@ 匹配**；现场 = $105 bypass 报价 + L2 + **现场要样品（无现金）** → 样品物流方案 = 转化关键点
- **#28 Hiperonline（Eskişehir）**：区域光纤 ISP（81 省，自有光纤+AirFiber+企业 Metro Ethernet 10G）→ ISP 基础设施买家

### 14.4 新增 B-（17 家）

DE Secure（Avigilon Premium Partner，要含 20% 关税工业 8 口 PoE 报价）/ **ORAL GÜVENLİK（北塞浦路斯，Ninova 经销商 → 北塞新渠道 + 瑞昱方案信号）** / F.A.S.T（工业自动化 A.Ş.）/ Fiberix（Gaziantep ISP，⚠️ 已有广州合作方）/ HCS（结构化布线品牌，PM 问 L2/L3 PoE）/ STASANET（塞尔维亚安防分销，辐射前南）/ Antalya Turkuaz（旅游城市集成商）/ Go Technology（巴勒斯坦 IT，⚠️ 加沙物流风险）/ Shnrise（安防全线，主问收发器）/ FOURLİNE（Bursa 卫星/安防分销+经销商网络）/ MEPA（Kayseri，4/8/16/24 PoE）/ AG Bilgisayar（Bodrum，规格明确：千兆 2 光8 PoE 网管 bypass）/ FH Güvenlik（İstanbul/Perpa 新设，工业定位）/ BİLGEN（Gebze 工业区，电子零件+安防）/ Duzgun Toptan（teksarf 批发 IT）/ PROVES（İzmir A.Ş.，与 PROVEN 防务无关联证据）/ Alamthal（利比亚通信 IT）

### 14.5 并入 + 排除（27）

- **并入**：#64 Snexus（= 第 19 轮 A 核心 #3）→ 行 3 加 Erdem Timur Koca（90 542 552 17 79，IASF 现场）+ 8 光8 电兴趣
- **排除 27**：无法核实 17（LABOR #34/Arcan #42/IHM #45/Senkacayc #46/Bilimsa #48/Netmax #49/Karaal #51/Marmaris #53/Todorov #54/Sinerjik #58/Marbim #59/Dimas #60/Fadi #65/Goktork #66/Alhossan #78/3S #80/D&N #70）｜无法核实-分销商信号在案 1（Ugur Imre #68：现场 = 分销商/不要 OEM/工业 PoE；瑞昱+DC48V 内置 $70 "Not bad"，WhatsApp 再核）｜微型 6（BTM #28/Ebatek #33/Voltech #39/Cansis #52/Başaran #61/Klasnet #77——Klasnet 经销商咨询信号在案）｜红灯深绑 2（Acusense #37=Hikvision 授权、ANIL #83=Dahua 主代理+Ruijie/TP-Link）｜业务不相关 1（**New World Polo #41 = 土耳其纺织制造商**，用户列 Greece 数据冲突）

### 14.6 落库去向（三件套同步）

- **扩展** `08-customer-pipeline/111-*`：CSV 45×17（utf-8-sig 回读校验）+ XLSX 重建（45 数据行 + 图例，分层色，回读校验）+ MD §八（分级表 + 排除清单 + 跟进序 8.6）
- **原始**：`99-raw/turkey-customer-list-round20-iasf2025-2026-10-08.md`（50 条 verbatim + §三 逐家深搜结论表）
- **常设规则沿用**：r19 两条（不找二极管类；白牌 3 渠道全挖掘）不变

---

## 15. 第 21 轮（2026-10-08，用户：IASF 2025 完整名单 86 条补全 + "重新梳理 刚才给你的可能有遗漏的 / 1 和之前一样的要求 2 分析过了的不用再分析，着重看没分析过的土耳其客户 3 只看土耳其客户，非土耳其的只留档"）

### 15.1 输入与分类

- **输入**：IASF 2025 展会客户**完整**名单 = 3 张表 **86 条**（第 20 轮收到的 50 条 = 本子集；本轮补全 36 条新条目）
- **分类**：86 = **已分析跳过 51**（r19 NOVA 1 + r20 50，逐条对位到 3 表条目，无重复劳动）+ **非土耳其留档 8（不深搜）**：Maipu 迈普（中国，参展商，ONV 流量整形问答）/ Miroslav（381 塞尔维亚号，CCTV PoE）/ Megatrade（乌克兰，工业 PoE 管理，BD 总监）/ AMZ Solutions（阿尔及利亚，L2/L3 持续项目）/ 0770 巴基斯坦号（24 口 PoE）/ STORM ICT（科索沃，工业 PoE 多）/ netpardazco（伊朗号，BD 总监）/ **Equinix（Ahmet.Yilmaz@eu.equinix.com，全球公司）**
- **⚠️ 高价值边界项（提请用户侧裁量）**：C8 Equinix = Istanbul 数据中心 **1G/10G 收发器买家**，本地交付无境外物流/关税风险；按"只看土耳其"指令未入 111，留档待用户拍板
- **新土耳其客户 = 27 条深搜**（web_search 4 批）

### 15.2 新增 6 行（#46-51）→ 111 管线总计 51 行

- **B 3**：**Telemobil/TBI（70，本轮最高）** = 2005 起 51-200 人 ~$25.6M 项目制系统集成（集装箱码头/商场/酒店/大学/公共/医院），用户侧标"可重点跟进，有具体项目"（2 光2 电 PoE + 现场问交期）/ **Pelikan Bilgisayar（64）** = Perpa 批发区进口-出口商行，商城实锤工业 L2/L3 PoE + PoE MC + Injector/Splitter + SFP-LTE 路由（与我司逐线对应）/ **Bilge Güvenlik A.Ş.（62）** = 2003 起 11-50 人三城分支安防集成（视频分析/车牌识别）+ 东南欧年度最佳渠道伙伴奖
- **B- 3**：Zeytek（58，机房/弱电材料供应，政府/医院/银行项目面）/ FOLİNE（58，**数据中心+集装箱 DC** 工程商，GM 级联系人）/ NAZEMCO（50，进口-出口有限公司+电子电商，商业 PoE）

### 15.3 排除 21（逐家原因 raw r21 §三）

无法核实 16（第 22 轮计数复核更正 17→16，21 = 16+1+2+1+1 对平；含强信号 2 条：**Sami CEUIK = 500 台询价 + 已购 2 光10 电 PoE 样品 $100 + 会来深圳安博会 → 微信跟进第一优先**；**selimkalaka = 现工业供应商在郑州且拟在土建厂 = 换源窗口**）+ 主体无法确认 1（NORTEL）+ 微型/红灯 2（viva=Hikvision 授权、teknokta=Dahua/Tiandy/Hikvision 三大授权）+ 无交换机场景 1（Interpos A.Ş. 电子制造）+ 端客户无信号 1（Camsan Ordu MDF 厂 780 人）

### 15.4 落库去向（三件套同步）

- **扩展** `08-customer-pipeline/111-*`：CSV 51×17（utf-8-sig 回读）+ XLSX 重建（52×17 回读）+ MD §九（分级表 + 排除 + 备注）
- **原始**：`99-raw/turkey-customer-list-round21-iasf2025-full-2026-10-08.md`（86 条 verbatim 3 表 + §二 分类 + §三 逐家结论）
- **跟进序更新**：① Telemobil（具体项目 + 交期）② Sami CEUIK（微信，已购样品）③ 第 20 轮 HAFYA/ONSİS/SFPTURKEY/Makros/ORAL 序不变

---

## 16. 第 22 轮（2026-10-08，用户：「1 eu.equinix.com 不跟进 只看土耳其国家 / 2 仔细检查一下刚才那么多轮的信息是否都已经入库了 不要有遗漏」）

### 16.1 用户裁定落档

- **C8 Equinix（Ahmet.Yilmaz@eu.equinix.com，Istanbul 数据中心 1G/10G 收发器买家）= 用户裁定：不跟进**（「只看土耳其国家」）→ 维持非土耳其留档、不开线、不再作为待裁量项。落档位置：raw r21 §二/§三 + 111 MD §九 + AGENT-README + TASK-STATUS 行 AE + 本条。

### 16.2 全轮信息入库完整性审计（复验结果 = 全部在库，逐家留痕）

| 对象 | 复验 | 结果 |
|---|---|---|
| raw 原始档（r17/r18/r19/r20/r21） | 5 份存在性 + 逐家结论表完整性 | ✅ r19 50 条 = 25✅（→23 行，#23→行 1 / #29→行 11 合并）+ 24❌ + 1⚠️entegron→110；r20 50 条 = 22 新增 + 1 Snexus 并入 + 27 排除；r21 86 条 = 51 已分析跳过 + 8 非土留档 + 27 深搜（6✅+21❌+C8📁）—— 三条名单**每条都有判定，无遗漏** |
| 111 客户管线三件套 | CSV 51×17（utf-8-sig 回读断言）/ XLSX 52×17 回读 / MD §一-§九 | ✅ 序号 1-51 连续（r19 23 + r20 22 + r21 6） |
| 110 竞对三件套 | CSV 88×20 / XLSX 89×20 回读（主清单+图例） | ✅ 含 r14-r19 全部增量（PNetworks/Longline+Entegron §12.6/TSGK/DC 20/ISP 池等） |
| LEDGER §1-§15 | 章节存在性（r13-r21 各轮独立小节） | ✅ 全在（本轮新增 §16） |
| conv-log | MD r12-r21 逐轮标题 / JSON rounds=23 | ✅（本轮 MD+JSON 各 +1 轮） |
| TASK-STATUS | 行 V（r20）/ 行 W（r21）/ 行 AE（本轮） | ✅ |
| AGENT-README | 已完成任务清单 r13-r21 在 | ✅ 但发现 **2 处遗漏 + 2 处陈旧**（见下） |
| 文件数 | `find workstation -type f` | ✅ 359（第 22 轮仅原地修改，无新增文件） |

### 16.3 审计发现并修复的问题（7 处）

1. **AGENT-README 对话历史摘要缺 3 条**：最新仅到「对话 18」→ 第 19/20/21 轮摘要未写入 → **已补 3 条**
2. **AGENT-README 深度审计记录表缺 4 行**：最新仅到第 17 轮 → **已补 18/19/20/21 行**（+ 本轮 22 行）；**关键 commit 表**同步补 r18-r21 四条（b3fded1/cc4cf8c/67f7582/3fb2643）
3. **WREADME 头部「最后更新」停在第 19 轮**（r20/r21 只更新了 L223 文件数行）→ **已刷新至第 22 轮**
4. **AGENT-README 分支全景 commit 快照陈旧**（8d01704/r17）→ **已刷新至 3fb2643/r21 + 领先 main 50→51 提交**
5. **r19 排除计数错误：26 → 实为 24**（raw §1.1 逐条复核：50 = 25✅ + 24❌ + 1→110）—— 错误传播 6 文件已全部更正（111 MD 概览+§六标题 / AGENT-README r19 块+决策块 / TASK-STATUS 行 19 / LEDGER §13 / WREADME 头部）；且 111 MD 概览名单**漏列 technologipazar #27**（「发不过去」零售）→ 已补，「metcon」笔误 → metcom
6. **r21「无法核实 17」→ 实为 16**（raw r21 §三 21 排除 = 16 无法核实 + 1 NORTEL 主体无法确认 + 2 微型/红灯 + 1 无交换机场景 + 1 端客户，对平 21）—— 3 文件已更正（111 MD §9.3 / AGENT-README r21 块 / LEDGER §15.3）
7. **Equinix C8 裁量项关闭**（16.1）

### 16.4 结论

- **三轮用户名单（r19 50 / r20 50 / r21 86）+ r17/r18 两版公司挖掘 + 全部台账/日志/任务表 = 无内容遗漏**；发现的 7 处问题均为**记录层计数/同步问题，非情报缺失**，已全部修复。
- 常设不变：不找二极管类信息 / 白牌 3 渠道全挖 / 不提 PR 合并 / 只看土耳其（本轮新增明确：Equinix 类非土主体一律不跟进）。


## §17 第 23 轮：全量复核 + 13 天新窗口挖掘（2026-10-21）

### 17.1 轮次概要
- 用户指令：「把你之前做的再过一次 看看有没有啥新发现 新的信息 / 继续挖掘angora的相关信息」
- 环境：⚠️ 沙箱重置到基点 c4085aa → 按 TASK-STATUS §八 恢复（fetch origin + reset --hard FETCH_HEAD → 0dee834 / 359 文件）+ openpyxl 重装；⭐ **fetch_page 代理恢复**（r19-r22 连续 4 轮全挂后）
- 产出：`99-raw/r23-recheck-mining-2026-10-21.md`（第 360 个文件）

### 17.2 新发现（13 天窗口 2026-10-08 → 10-21）
1. **EKAP 新窗口**（rehbersanayi IT 归档 60 条，10-09→10-19）：110 在册公司 **6 起新中标**——Pantech（行 70）服务器 132.5M TL/仅 1 投标 İKN 2026/1708449（10-19）/ Fonet（行 63）SBYS+YBYS 137.7M TL/2 投标 İKN 2026/1214002（10-15）/ Artı ve Artı（行 64）服务器+存储+**网络设备** 9M TL/仅 1 投标 İKN 2026/1479835（10-12）/ NETCAD（行 73）5.2M+5.3M İKN 2026/1702069+1667628 / Itech（行 74）3.2M İKN 2026/1798180 / Gruptechs（行 76）1M İKN 2026/1712577；**Angora/PnetWorks/PAVO/Ewind/Longline 0 命中**；两窗口间存在 **10-01→10-08 盲区**（`?page=N` 参数确认仍被忽略 = JS 分页）
2. **市场统计**（06-30→10-19）：全行业 30,740 项 / 1,219.1 亿 TL / **38% ≤2 投标成交**；IT 625 项 / 16.2 亿 TL → 关系型市场结论再加强
3. ⭐ **Ewind 2026 新品**（ewindnet.com 官方新闻，经搜索摘要）：2026-04-29 **EW-S3936GM Gigabit Managed = Microchip（Vitesse）芯片**（官网自述）→ 芯片世代更新实锤；2026-04-21 **Industrial Cloud-Managed 系列**（802.3bt 90W / 12-24V 被动 PoE / DIN 轨 / 长距）；atommarket 7 款在售（S2910GM 4,475 / S1810GU 1,005 / S1827CF 3,471 TL；S2924GM-AP 400W 锚点型号仍在售）
4. **PNetworks 零售复核**：n11 锚点 **13 天不变**（CMS48 PoE+ 156,612 / Pn48 150,812）；⭐新增 **PN8GE2CG 8 口 PoE Combo 61,419-63,707 TL**；⚠️ **Trendyol 同 CMS48 PoE+ = 78,307 TL（约 n11 之半）** = 多渠道并行 + 价差（价格战早期特征）；2026 官方新闻 0 条
5. **Longline hepsiburada 复核**：店铺 = **116 产品**（r18 ≈10 模型）；⭐新增 **LNG-M3XF4GE24 24 口工业 L3 PoE+（4×10G SFP+）137,900 TL**；新光模块锚点 SFP-10G-SR 4,788 / QSFP-40G-LR4 12,600 TL；5 口 750 TL 不变
6. **Keenetic TR 零售落地**：2026-05-14 官宣 → 6 月分阶段上市已执行；5 口 PoE+ 60W = 1,599-1,849 TL（Amazon 19 评 4.6★）/ 9 口 PoE+ 120W = 2,909-3,349 TL；akakce 5 口款 30 卖家；仅 unmanaged（managed/工业观察项维持）
7. **Angora 本体**：官网新闻栏停更于 2023-12-05（32 个月）；2026 新品/渠道/高管公开信息 0 条；VERGE 家族复核（8/24/32/48 + DC 48×1G/10/25G+6×100G QSFP28 3.6Tbps）；LinkedIn 2,110 粉静态 → 「沉寂/低可见度」判断维持

### 17.3 待核项清理（2 解决 + 1 部分解决）
- ⭐ **Opax（111 行 20，r19 唯一客户侧待核）= 解决**：opax.com 法律条款页 = 「Opax Mühendislik Kamera Alarm ve Güvenlik Sistemleri ... Pazarlama Limited Şirketi」，地址 **Opax Plaza, Yeni Mah. Diriliş Blv. No:3, 50100 Merkez/NEVŞEHİR**，+90 850 259 12 12；B2C 直销 + B2B 代理双轨（官网发布代理商协议全文）；OPAX-08120W 实价 $35（1,623.30 TL）；**opax.pl = 另一波兰域，与土耳其主体无书面关联**（"外资主体"假设降级）
- ⭐ **Fiberix（r20 #66 排除项复核）= 确认排除**：fiberix.com.tr = 面向个人的光纤 ISP（无限套餐 519-619 TL / 20-100 Mbps、自有基础设施）→ 非 switch 贸易实体；「广州现有伙伴」说法现网站无佐证
- **Duzgun ↔ Toptansarf（111 行 43）= 部分解决**：toptansarf.com / .com.tr 在运营 = 「TOPTANSARF BİLGİSAYAR VE GÜVENLİK SİSTEMLERİ」（Hürriyet Mah. Sedef Sk. No:5/A Bahçelievler/İstanbul；0212 580 25 25 / +90 541 660 10 66；10 年 B2B 批发 1000+ SKU，目录含 Ruijie Reyee RG-RAP2200F PoE AP）；**teksarf.com 当前 HTTP 500 宕机**；Duzgun（gmail 联系）同一主体 = 高概率，待 WhatsApp 实联确认
- **Trabzon Büyükşehir İKN 2026/1272126**（PNetworks 全栈对口单）：结果落在 10-01→10-08 盲区窗口 → 维持「未验证」，下轮再核

### 17.4 数据落库
- 110 三件套：10 行级更新（行 1/9/15/20/63/64/70/73/74/76；CSV + XLSX in-place + MD 头部 + §13 新章节）
- 111 三件套：行 20（Opax）/ 行 43（Duzgun）更新（CSV + XLSX + MD 头部 + 对应 2 行）；行数不变 51
- 台账同步：TASK-STATUS 行 AF + conv-log 第 23 轮（MD+JSON）+ AGENT-README 全套 + WREADME（360）
- 文件数：359 → **360**（新增 raw r23 一份）

## §18 第 24 轮：Ewind 官网全量爬取入库（2026-10-21）

### 18.1 轮次概要
- 用户指令：「你把Ewind网站爬下来入库吧 必要时开workflow去爬」
- ⭐ 产出 = **`06-competitors/112-ewind-website-mirror-2026-10-21.md`**（第 361 个文件）：公司面 + 站点结构 + 五大产品线 90+ SKU 规格表 + 2026 时间线 + 竞争情报解读 + 数据边界
- 方法：ewindnet.com 直连 fetch 3 次全 OSS 故障 → **`site:ewindnet.com` 索引爬取 workflow**（6 轮定向检索，索引快照含完整规格表；pageAge 2024-03~2026-07-22）

### 18.2 关键增量（对 110 行 15 既有口径）
1. 公司面：投资 **$50.67M** / 厂 5000+ ㎡ / **500+ 员工** / 20 SMT / National High-tech / +86 755-2100 6440 / 100+ 国出口 / 多语言 en/ru/zh/es/no / **CPSE 2025**（深圳 1A16）/ 案例 = **四川省公安厅**（2025-08）
2. ⭐ **Cloud/AI PoE 新线（2025-26）**：ES2010CF-AP / ES3006CG-AP / ES3028CG-AP（400W）/ 2026-05-27 + 07-22 两款 AI PoE 新页 / EPIS3910-8GE 工业云管理；平台 = **EwindCloud**（ONVIF 发现 + 云拓扑图 + 单端口重启 + OTA）
3. **2.5G/10G 扩品**：S6805F/6806/6809/6818/6826（2.5G ladder，顶配 160Gbps）+ 10G Managed PoE 类目 **17 SKU**（含 S53928QM = 24×10G+4×100G L3）+ **W- 前缀新系列** W-S2910SM-DP（2026-06-25）
4. 核心线：S3936GM(-AP) 598Gbps = **Microchip (Vitesse) 芯片**（2026-04-29 官方，r23 已录）；S5954GM-AP L3+ OSPF v2/VRRP
5. ⭐ **OEM 定制实锤（EW-S1810CF-AP）**：拨码 **E = AI Extend 300m / V = 口隔离 & VLAN / D = AI-PoE Watchdog（相机掉线自动重启）** → 与 Longline 同卖点集（Extend 250m + Watchdog）
6. 交付：OEM 4-6 周（常规 4 周）；质保商用 2-3 年 / 工业 5 年 / 光猫 3 年
7. 光猫 9 款（2U 16 槽机箱 EF16-D220 / 10G 光猫 / PoE 光猫）+ 注入器/分离器 16 款（BT 60W/90W 类目、Type-C 线）

### 18.3 数据边界
- 官网 0 价格（B2B 询价）；土耳其零售锚点 = atommarket 7 款（行 15，r23）
- 未穷举：10G PoE 类目余 5 SKU / Unmanaged 类目余 3 SKU / BT 注入器型号 / WiFi 类目 / 2 款 14 口工业（型号未捕获）
- 110 行 15 三件套已同步（CSV/XLSX 备注 + MD §14）

## §19 第 25 轮：Ewind 宣传面/全渠道爬取入库（2026-10-21）

### 19.1 轮次概要
- 用户指令：「他们网站信息都爬完了？如果爬完了就去爬他们的宣传网站 反正只要关于EWIND的信息都要爬 都入库了」
- ⭐ 产出 = **`06-competitors/113-ewind-promo-full-presence-2026-10-21.md`**（第 362 文件）：10 轮 site: 检索 workflow（www + 12 语言站 + Alibaba + FB/LinkedIn/ZoomInfo + 展会 + 分销页）
- 第 24 轮边界（ewindnet 直连故障）不变 = 全索引快照口径

### 19.2 关键增量
1. ⭐ **土耳其**：官方 Malatya 案例（12 语言站全同步）+ **1Net Telekom**（BTK 持牌运营商）总经理 LinkedIn 推广 Ewind = 疑似渠道 + 海关口径土耳其 = 中国 PoE 出口 Top10 市场
2. ⭐ **Alibaba 宣传店铺**（ewindnet.en.alibaba.com）：Verified Manufacturer + "#3 most popular in Network Switches" + 4.5-4.7/5 + **270+ SKU** + Brand = EWIND/OEM + 主要市场美伊英沙菲意加利
3. ⭐ **首批价格锚**：$21.55（8 口 100M）/ $33.85 / $39.15 bt / $75 / $75.4-80（PIS1712-8FE）/ **$111-115（S1820CG-AP 20 口 300W）**/ 24 口被动 PoE 250m+Watchdog 主推
4. r24 缺口全补：IS3814M / BT 60W-90W 注入器 / PIS3814M-8GE / PIS3606M-4GE(-NB) / S1806CF-AP / S1508CF / S1906 两款 / 95W BT 线 / 2936GM-8GF-AP 400W / 工业电源 3 款
5. 官网类目计数（27 分页）：Ethernet Switch 63 / PoE Injector 25 / Accessory 64 / IP66-68 2 / Bypass 1 / 跳线 8
6. **WiFi 13 款全录**（r24 = 0）：CPE×4 / 路由×6（含 EW1800 = BCM6755、EW3600 = WiFi7）/ AP×6（WiFi7 三频 = Qualcomm IPQ5322、EW-API210 户外 2026-06-26）
7. 社媒矩阵：FB×3（**EU-US 专页** = Maggie Lin）/ LinkedIn（COMPUTEX 2026 + OSPF/BGP/VXLAN 核心叙事 + #Vitess）/ ZoomInfo（**Jarvis Xie MD / Kathy Chiang / Arya Le**，51-200 人）
8. 展会 10+ 场全录（2013 南非→2026 台北；每年 20+ 场）；12 语言站（+nl/ko/el/it/pt/fr/de）；公司细节（5 电话线/3 邮箱/办公 2 址+工厂 2 址〔松白+宝安〕）

### 19.3 落库
- 110 行 15 三件套 + §15 章节 + 本台账 + TASK-STATUS 行 AH + conv-log 25（JSON 27）+ AGENT-README 全套 + WREADME(362)
- 监控增量：Malatya 案例细节 / 1Net Telekom 分销扩张 / Alibaba 价格变动 / 10G PoE 余 SKU 全量

## §20 第 26 轮：Ewind 爬取最终闭合（2026-10-21）

- 用户指令：「EWIND信息都爬完了？」
- 执行：直连第 4 次仍 OSS 故障 + 3 轮收尾检索 → **两大类目闭合**（10G Managed PoE 17 SKU ≈ 全量 / Unmanaged 15 款全量）+ 新增 7+ 款：
  - ⭐ **EW-S5954GM-AP(RTL) = Realtek 芯片版本**（商用 L3 芯片源 = Vitesse + Realtek 双方案确认）
  - S53952QM（48×10G+4×100G，1760Gbps）/ S57948QM（48×2.5/5GE+4×100G，1280Gbps，MAC 112K，**5GE 接入新线**）/ S2828GM-AP / S5728GM-AP(-AT)（L3 完整规格 400/600W，128 静态路由/QinQ）/ S2854GM-AP（800W）/ S53928QM 完整规格 / PIS5736GM-8GF-AP-BT(VTS)（36 口 800W L3 工业）
  - Unmanaged 全量：S1505（1 年质保）/ S1505CF / S1605（2 年）/ S1605CG / CGU 4 型号（Datasheet V11.19.2025-V19.11.2025）
- ⭐ **最终完整性结论**：信息层面 ≈95%+ 已爬完；5 项硬边界（Malatya 正文 / Alibaba 270+ 逐个 / FB-LD 正文 / 官网 PDF 需直连 / 动态内容 = 监控项）已入 113 号档案 §11
- 落库：113 §11 + 110 行 15 三件套 + §16 + 本台账 + TASK-STATUS 行 AI + conv-log 26（JSON 28）+ AGENT-README 全套 + WREADME

## §21 第 27 轮：Google Drive 订单信息全量入库（2026-10-21）

### 21.1 轮次概要
- 用户指令：「我把Angora的订单信息传到Drive里了，你读取一下，把信息入库 **全部都要入库** 你看看咋入库 **尽量是不要占太多内存**」
- 执行：Google Drive 连接器（load = google_drive）逐文件夹/逐文件读取；可读文档全量抽取，**二进制/legacy/PII 只索引不下载**（最小存储占用）
- ⭐ 产出 = **新建 `09-orders/` 目录 + 2 文件**（第 363/364 文件）：
  - `120-angora-orders-master-2026-10-21.csv`（9 单行级 P&L：合同号/日期/行项/量价/收款 USD/成本/利润/运费/MAC-SN/物流/状态/Drive 索引）
  - `120-angora-orders-dossier-2026-10-21.md`（全量档案：关系链/9 单逐单事实/型号三套命名对照/财务底账/MAC-SN 总表/RFP-TT-EGM 管线/战略文件/317 项完整文件索引/边界声明/前序交叉引用）

### 21.2 关键增量（⭐ = 新发现）
1. **订单链全景**：Angora（Ankara，Ziraat Çayyolu IBAN TR09 0001 0019 8997 0378 9850 02；GM = Levent Kilic「LK」）↔ 郑州伊博（Simon Cheng）↔ SmartByte（Peter Hu，惠州惠阳）；Angora→Saga 付 USD，汇率 7.15；运费按 ~30% 利润率加收
2. **9 单全对平**（合同-发票-成本表 6/6 通过）：1st 4 台 $1,265（23.6%）/ 2nd 8×2116+2×1108 $2,345（34.4%）/ 3rd **178×ANW-2116-PG $47,174（15.9%，最大单，5% 折扣+RMA 2%+30-20-50）**/ 4th-pre 9,110 RMB 未出货 / 4th 3+3 台 $1,665（18.7%）/ 5th 13 台 $3,755（34.5%，**Angora+TronX 双品牌**）/ 6th **6×TT-2208-PG $990（29.8%，Turk Telekom Logo）**/ 7th **10×TT-2208-PG（仅 MAC 表为证，STSC20250711007）**/ Unpaid-1 **TronX $1,480 FOB 未付款**（PASSED 项仅登记）
3. **累计 6 单成交**：成本 338,314.62 RMB → 收款 57,194 USD = 414,103.74 RMB → 利润 **75,789.12 RMB（18.3%）**
4. ⭐ **TT 通道实锤**：2nd 单 ANW-1108-V 样品 → 2025-02-03 TT 测试（RFP_2025.1.30，型号 TT-2208-TG）→ 量产 TT-2208-PG（6th+7th = 16 台，MAC 池 A5:00:00~A5:05:FF 2,048 地址预留 2,000+）
5. ⭐ **EGM 3,294 台**规格原文入库（KGYS/ÇGKS：野外 8GE+2SFP 70km -40~60°C IP20 DIN 全口 PoE + 室内 24GE+4SFP 56Gbps；Mehmet ÇATAL 2026-02-12 批准；C-Type 测试报告强制）
6. ⭐ **CENTEC L3 方案包**（INFO_2025.12.17 = VastLakes 25G + PeakNetX 10G + STH1G/STH25G datasheet）= 2026-08-17「CENTEC L3 功能全有」回复的物料实证；3rd 单夹 lite-hotfix-7.3.13.bin 62MB = AC3 冻结末版物理实证
7. **更正 r13**：「15.4 个月零落单（末单 2025-06-19）」→ 末单日期正确，但 7th 单（2025-07-11）+ 4th-pre 未出货单证明链条未断
8. 其他：TronX = Angora 姊妹公司（Mustafa Calik）；TT-2116-PG.zip = TT 扩型预研；加深关系绑定 2026-07-20（Lira 付款/伊斯坦布仓/Marvell 护城河/co-branding）；Turkey Client List 55+ 家；Karen -40/+75°C 测试照；WeChat Talk 26 张截图（2026-09-23/10-06）未 OCR = 下轮候选

### 21.3 边界（诚实声明，见 120 号档案 §9）
- legacy `.xls`/`.doc`（~15 份合同/发票）API 不支持抽取 → 只索引（金额以已读 PDF + 发票文件名 + 成本表为准）
- 图片/视频/PSD/DXF/7z/RAR/zip（~150 项 ≈180MB+）一律不下载（用户指令：最小占用）→ 只索引
- LK-Passport-chip.pdf = PII 仅索引；纯图片 PDF（Certificate of Warranty ×6）无文本层
- 大 xlsx/docx 抽取中段截断 → 数据行在头部已用，勿重试

### 21.4 落库
- 新建 `09-orders/`（120 号 CSV + MD）+ 本台账 + TASK-STATUS 行 AJ + conv-log 27（JSON 29）+ AGENT-README 全套 + WREADME（364 文件）
- 监控增量：WeChat Talk 26 图 OCR（与 wechat 语料 2026-10-03 末条衔接）/ 4th-pre 单 fate / TT 通道放量（MAC 池余量 2,000+）/ EGM 3,294 台 C-Type 测试进度 / CENTEC L3 方案推进

## 22 · 第 28 轮 · 2026-10-21 — WeChat Talk 26 张全量对平 + 时间戳统一 + Angora 全量重头分析

- 用户指令：「基本上所有关于Angora的信息都给你了 wechat Talk 订单 相关文件等。你再看看时间戳 应该是从2024年开始沟通的。统一理解一下这些信息。然后再重头分析一下Angora」
- 执行：① google_drive download_file 26 张 PNG 全量落盘（58MB → `/home/user/Angora/google_drive/`，磁盘落盘非 base64 = 上下文零膨胀）② PIL 顶/尾 620px 裁剪 ×52 + 视觉核验（顶部 9 张抽验 + 底部 3 张 + 全图 1 张）③ 与语料对平 ④ 新建 121 号全量重头分析
- ⭐ 核对结论：
  1. **沟通起点 = 2024-05-02 16:36**（截图 #1 首行 =「**You have added Levent KILIÇ as your Weixin contact. Start chatting!**」→ 首条消息「hi, Levent, How are you?」→ Levent 16:45「Here may be much quicker to chat for small stuff」）→ 用户「应该是从2024年开始沟通的」✅ 成立；6 天后（2024-05-08）首单
  2. 25 张（摄于 2026-09-23 22:34:55→22:52:51）= **同一 Levent KILIÇ 会话的完整长截图平铺**：图 1 顶 = 会话最顶（2024-5-2 16:36）、图 25 底 = 会话最底（**8/30 Sunday 21:03**「understood」+ 输入框可见），中间 23 张首尾相接（抽验 9 张：5-2 / 5-27 STC-424XGGM 需求 / 8-6 首次 L3 请求 / 9-17 假期 / 10-22 2nd 单收款 / 10-30 OEM 定位 / 11-8 客户名单群发 / 11-27+12-02 产能预警+AP 贴牌 / 2025-1-08 装箱 440kg；跳跃均 < 窗口长度 = 有重叠）
  3. 图 26（摄于 2026-10-06 17:25:57）= 88 台订单段（10/2 19:56 Levent「88 pieces of L2+ industrial 8-port together with 48V power supply...pricing in the same box」→ 10/3 00:19 Simon 报价 **STI-288DGGPM 875 RMB/PC + 240W Meanwell 48V 电源 250 RMB/PC**「same as last order / we will handle the material costs here / same packing box」+ angora 纸箱照片 → 10/3 00:40 Levent「Thanks Simon. Great.👍」）= **已在库**（r13 第 26 张图「877 图」OCR，`wechat-conversation-aligned.md` L10300-10326）
  4. **26/26 张 = 0 新消息** = 与语料（2,601 轮）100% 重复；58MB 原图核验后**删除**（最小存储占用）
  5. 语料结构澄清：图 25 底 8/30 21:03 = 静默期前最后消息（8/30→10/02 静默 5 周 = 真实空窗）；语料全库末条 = 2026-10-03 00:40（10/2→10/3 段）
- ⭐ 产出 = **新建 `09-orders/121-angora-master-reanalysis-2026-10-21.md`（第 365 文件）**：§1 时间戳统一核对表（沟通起点 + 25 锚点三源对平）/ §2 实体画像 / §3 关系全史四阶段（样板 2024H1→放量 2024Q4→通道 2025H1→战略 2026H1，6-8 月一台阶）/ §4 全口径经济账（57,194 USD 已成交 + **88 台在手 104,720 RMB ≈$14.6K**）/ §5 产品技术线（AC3 冻结/CENTEC L3/48V 工业/EGM 3,294）/ §6 竞争位势 / §7 十大风险 / §8 七大机会 / §9 综合重判（**Angora = 我方土耳其政企「yerli 牌照」+ TT/EGM 白牌通道 + 2,048 MAC 池量产期权；88 台 = 行权第一步**）/ §10 边界声明
- 簿记：120 号档案 §7.6 补对平注 + TASK-STATUS 行 AK + conv-log 28（JSON 30）+ AGENT-README + WREADME（365）

## 23 · 第 29 轮 · 2026-10-21 — Angora 财务/融资模式/内部结构深挖

- 用户指令：「继续挖掘angora的相关信息 因为每次我感觉他们下单或者沟通都是要融资啥的 他们自己没钱嘛 账上啥的 而且TayLan很少和我沟通 基本没有 都是levent 他们内部啥情况 财务状况呢 营收啥的呢」
- 执行：① 微信语料 2,601 轮全量财务关键词挖掘（EN/TR：financ/cash/bank/credit/financier/ortak/hisse/yatırım/kredi/nakit/bilanço/ciro…）+ 关键对话块逐条回读定日期 ② 公开信源（ZoomInfo/RocketReach/CB Insights、find.com.tr、IANA PEN、ictmedia 2023-06 Levent 专访全文、KOZ'23 新闻、İKMB 会员名单、EGM 招标动态 paratic/ihalemetrik、web_search Hakan Oztuna 0 命中）
- ⭐ 结论 1（用户直觉验证 ✅）：**Angora = 资本极轻、项目融资驱动**；Levent 原话铁证链 16 条（2024-11-18「find some financial resource」→ 2025-02-28「meeting with the bank」→ 2025-04-25「Cash flow is a real problem」+「depositing money to Saga. Much better than banks」→ 2025-06-23「we do not have the bulk cash」+「other costs embedded…plan B」→ 2025-07-07「**a financier will transfer the payment**」+「invoice as software」→ 2025-09-04「Telekom finance L/C trouble」→ 2025-11-28「economy is too slow in investment」→ 2026-03-30「**partner 需垫资 ≈$600K × 4-6 个月**（设备 $500K + VAT $100K；警队 100% 验收后付）」→ 2026-04-01「partner 免 VAT 进口」）；TT 1,000 台 2025 全年因融资未落地 → 2026-06 改框架协议（1K 量级年约）
- ⭐ 结论 2（内部结构）：Levent（前 Cisco→2022 销售总监→2023 GM，唯一窗口）/ **Taylan Esen = CTO**（前 Cisco 同事、联合创始人、IANA PEN 58029 联系人、KOZ'23 讲生产、2024-03 辞董事会但 2025-06-23 仍在职〔「I just checked with Taylan」〕→ 「Taylan 不说话」= 分工正常〔技术走邮件〕非恶化）/ **Hakan Oztuna（BURSA/NİLÜFER，2024-03-09 新主席 + 单独代表权至 2027-03，公开足迹 0 = 沉默资方推断）**/ Uğur Han Kurt 辞任无足迹；外部 partners（TT 政治资源伙伴 2026-03-09「co-development…source codes…Hardware designs…confidential」/ EGM 融资伙伴 / TronX 销售伙伴 / ODM 框架伙伴）= 影子决策链
- ⭐ 结论 3（财务/营收）：营收 **<$5M**（ZoomInfo）/ 10 人 / 进口 $44.9-70K 年 / 2023 目标 5,000 台 / **EGM 单标 $500K = 公司盘子 7-11 倍** → 结构上必须外部融资；**İKMB 名单 BORÇ VAR = 协会年会费欠缴（行政性质）澄清**（非税务/破产债，表头 YILLIK AİDAT 列佐证）；MERSİS 财报 = 死角
- ⭐ EGM RFP 全貌（2026-03-24 语料）：4/28 标 3,300 台工业 + 4/29 标 600 台工业+200 台 24 口 + 草案 1,085 台；竞品 DLink Vitesse 7428；TT 2026 框架 6 类 1K 量级（我方 L2+ 型 + CENTEC 补 L3/stacking）
- ⭐ 合规红旗 3 条：「invoice as software」（2025-07-07 已发生，建议硬件如实申报）/ 对伙伴隐瞒我方身份（2025-06-23）/ LK 护照 PII（维持仅索引）
- 产出 = 新建 `09-orders/122-angora-financials-internal-dynamics-2026-10-21.md`（第 366 文件：铁证链表 / 模式定性 / 内部结构 / 营收推算 / 风险 O1-O5/R1-R5 / 合规 / 边界）+ 121 号 Camlıca 更正（= 安卡拉 Yenimahalle，非伊斯坦布尔）
- 簿记：TASK-STATUS 行 AL + conv-log 29（JSON 31）+ AGENT-README + WREADME（366）
- 监控增量：EGM 4/28-29 标结果 / 88 台 PO + 终端确认 / TT 2026 框架 CENTEC 样机时点 / Hakan Oztuna 身份（若有公开痕迹）/ invoice-as-software 政策（用户决策）

## §24 · 第 30 轮 — 2026-10-21 ≈18:55：88 台终止 + 10/8 新对话全录 + Levent-TT 出身考证

- 用户指令：「88台项目已经凉了 我传一下信息 MAIN上 Weixin Image_2026-10-21_174720_411.png 我记得之前说过 levent和TT关系还可以 他似乎也是从TT出来的？ 查一下这个方向吧」
- 执行：origin/main 411 图（git show 文件级恢复，1545×7431px，/tmp 工作区外）→ 3 段视觉全转录 = **2026-10-08 13:03→17:00 新对话 61 轮**（语料新增，2,601→2,662；追加入 wechat-conversation.md + aligned.md）
- ⭐ 结论 1（88 台 = 已凉）：Levent 10/8 原话 = partner 因**交期**改主意、转投**土耳其本地现货**（中标替代 = **cryptoink.com.tr**，另一中国供应商的本地 OEM 品牌，无索引盲区）；「Sorry about the loss. This was also a very critical and important deal for us」→ **本地库存 + 交期 = 土耳其项目单核心胜负手**（R5 项目黄了订单消失 = 再实证）
- ⭐ 结论 2（10/8 十三新信息）：本地库存 **25-50 台**提案（day-to-day）/ 融资算术两难（$5K 高息 vs 借款付息）/ **Lira 收款账户 + 「test this soon with a small order」**/「funds for investment this year **from other projects**」（库存资金 = EGM/TT 回款）/ 定位 =「**We are not an integrator. We position ourselves like Maipu, H3C**」（纯厂商；标单全走伙伴）/ **MikroTik L2+ 联合争夺共识**（xlsx 交付；CRS328-4C-20S-4S+RM $449 vs 我方 ~$300）/ resale 直销实锤（「That's exactly what we do now」+「correct, exactly」）/ USD/TRY 49.21 / EGM 标机制 = 5 轮电子竞价最低价（2026-04-16 补录）/ TT co-development + 政治资源伙伴（2026-03-09 补录）
- ⭐ 结论 3（Levent-TT 考证）：**非 TT 员工** = **Cisco 的 Turk Telekom 战略客户经理 15 年+（XING：2010-08 起 SAM (Turk Telekom)；2008-07→2010-08 Service AM 兼 TT+公共部门 quota）**→ TT 通道 = 其旧关系网（2024-05 TT RFP 首开 → 2025 测试 → TT-2208-PG 量产）+ 新政治伙伴 + yerli 身份三合一；早年 Lipman POS(1997-2002)→Ingenico Planet(2002-03)→Miletus GM(2004-06)；并行 **CONNEXITE（London）Managing Partner** = Connexite-Amazon 计划英国实体（RocketReach 另列 Nutanix/F5 = 待核）
- 产出 = 新建 `09-orders/123-angora-88-dead-levent-tt-background-2026-10-21.md`（第 367 文件，5 节）+ 语料追加 61 轮 + 121/122 号 r30 状态注（只增不删）
- 簿记：TASK-STATUS 行 AM + conv-log 30（JSON 32）+ AGENT-README + WREADME（367）
- 监控增量：O1 本地库存 25-50 台落地 / O2 MikroTik L2+ 对标清单（11 月前）/ O3 TT co-development 用户拍板 / cryptoink.com.tr 复访 / EGM 4/28-29 标结果

## §25 · 第 31 轮 — 2026-10-21 ≈20:10：Angora 线上平台取证（networkmarket.online 已关 + thince.net 已失效）

- 用户指令：「Agenda for WeChat meeting at 2025这个文档中提到了 networkmarket.online 你查查这个…他们已经关闭了…原本还有一个线上宣传平台 现在也没了…看看能否查出来啥信息不」（+ O1/O3 两决策点搁置「不用管」）
- 执行：agenda 2025 docx 原文 + WeChat 2025-06-20 段（aligned L4792-4800）+ Wayback CDX 全时间线/快照 + 官网子站存活核验 + web_search 旁证
- ⭐ 结论 1（networkmarket.online）：= Angora/Levent 的 **D2C 零售橱窗**（Ticimax 店铺 64180，土耳其语 ₺+KDV 分期）；类目 switch/SFP/线缆；品牌 = **TRONX（我方 OEM 全线，含 T-IQ-NMS 网管许可）+ ORCA（自有配件，IG = Orca Technics）**；时间线 = 2023-05 首抓 → 2025-03-02 最后完整 → 2025-06-20 Levent 亲证关闭（「**We did not do a lot of business**」）→ 2025-07-16 最后抓取 301 = 死 → 2026-10-21 直连失败确认；**2025-03 价目 20+ SKU = 我方货土耳其本地价格锚**（TRX-EN8-1 工业 8 口 ₺54,820 ≈$1,550 vs 成本 ≈$122 = **12.7x** / TRX-OM1 核心 $37,700 / NMS 许可 ₺411K-531K / ORCA SFP ₺856 vs 我方 ¥25）+ 价格通胀实证（11 个月 +7%）
- ⭐ 结论 2（「另一个线上宣传平台」）：= **thince.net**（THiNCE 瘦客户机品牌站）：2020-10→2025-05-14 完整 → **2025-10-15 抓取 = 301→/lander（571B，域名停放）= 已没**；与 networkmarket.online 同一窗口（2025 H1→H2）= 用户记忆对上
- ⭐ 结论 3（战略转向时间线）：2025 H1 关零售店 → 2025-06/07 试 Amazon UK（Biz-Plan 在 Drive，Ads 成本顾虑，**未见落地**）→ 2025 H2 瘦客户机站也停 → 2026 all-in 标单/项目线（EGM/TT）= **Levent 反复试零售、反复失败、回到关系型项目生意**；angoranetworks.com 官方主站仍活（内容停更 2023-12）
- 产出 = 新建 `09-orders/124-angora-online-platforms-forensics-2026-10-21.md`（第 368 文件，5 节）
- 簿记：TASK-STATUS 行 AN + conv-log 31（JSON 33）+ AGENT-README + WREADME（368）
- 监控增量：Amazon UK 是否落地 / Shopify / ORCA 品牌动向 / angoranetworks.com 更新 / networkmarket.tr（无关同名店，仅排除记录）

## §26 · 第 32 轮 — 2026-10-21 ≈21:0x：TronX 官网全页取证 + Larch×Angora 合作时间线 + 宪法规则落库

- 用户指令：① 贴谷歌搜 "tronx poe switch" 命中的 tronx.com.tr「TronX Switch Ailesi」土耳其语原文 → 抓取相关信息 ② 「**把所有的信息都入库 刚才的商城以及TronX以及Angora的官网等 只要是抓到的信息，都要入库：这个一个宪法式的规则**」（说了两遍）③ 「larchnetworks 的官网上有 angora 的图标 他们 2 家何时合作的？我在微信上也和 levent 提过几句这个 也都挖掘一下相关信息 都入库」
- ⭐ 结论 1（TronX 品牌定性）：tronx.com.tr = **TRONX BİLİŞİM VE SAĞLIK TEKNOLOJİLERİ LTD**（安卡拉 Çankaya，**2008 年医疗/医院耗材销售起家**，自述 14+ 年，三大线 = 医疗/数字讲台/Network）；**Levent 2025-07-23 verbatim（aligned L5852-5905）：「TronX is a brand we have created together with a partner for his sales only. He has his own channel. We are more like backoffice for him. We manufacture, give him tech support etc」** = 与伙伴共建的专属品牌，仅该伙伴销售，Angora = backoffice（制造+技术支持）；参考客户墙（uploads 2022/09）= **EGM + Jandarma + Ulaştırma + Sağlık Bakanlığı + Osmaniye/Erzincan 省卫生司** → EGM 与 3,294 台警队标同客户池；站点半废弃（/verge-switch-ailesi/ 404 + dijital-kursu 双重路径 + sap-station.com 模板残留）；**Wayback 0 快照（CDX 2 次空 = 从未归档）**
- ⭐ 结论 2（TronX 产品 = 我方 ODM 全映射）：Switch 家族 8 型号全规格入库（工业 8 口 TRX-EN8-1/2 = IP40/-40~+80°C/48V DC/PoE+ = **第 6 单同构**；KS24/48-1/2 = 24/48 口 L2/L2+/L3 PoE；**OM1/OM2 = 48×25G SFP28+8×100G QSFP28 L3 全协议（TRILL/OpenFlow/Netconf，MAC 128K）= networkmarket 2025-03 同型号**）；⭐**NPB T-IQ-PB-1/2 = 48×1/10/25G + 6×100G + 包处理器 Marvell + 1.9Tbps + 16GB/8GB + 1+1 冗余 650W + 1U = 我方第 6 单 Marvell NPB（NEXUS-48X32T50 系）的 TronX 品牌化**；T-IQ-PB-1 基础 license + T-IQ-PB-2「Ek Lisans」= 分级销售；功能 = L2-L7 过滤/Dedup/SSL 协助/DPI 128B/**Yasal Yakalama（ISP 法定流量留存）**/拖拽 Web UI/SNMP
- ⭐ 结论 3（**Larch×Angora 合作起点 = 2023**，三重证据）：① 进口 = TTD 窗口 **2023-08→2024-07** 21 票 $44.9K，Larch = 供应商 #2（以色列 7 票 15.56%）→ 下限 2023-08（逐票 = Volza 付费墙）② **Wayback 二分实锤**：larch-networks.com 2023-05-29/2023-09-26 快照 = 旧墙（单张 partners.png 2023/03）→ **2023-11-14 快照 = 新 24-logo 墙已含 angora.webp（uploads/2023/11）** → 2023-12/2024-08 持续 → 2025-08 改版重传 → 现行首页 + /business/clients/（24 客户，angora-300x150.webp 2025/09）= **公开背书 2023-11**；CDX 自 2011-06（240 抓）③ 微信 = **2026-06-08 L9347**（Simon 首提 →「Yes we know them」）/ **2026-06-11 L9449**（Simon 因见 logo 而提 → Levent「**a good partner**」+ ⭐「**politically we had a lot of problems in Turkey because we cooperate with an israeli company. the current government is more religious**」）/ 06-12 L9555 / **2026-08-10 L10096+L10118**（Levent 要 Sonic 样机硬件）；双向 logo 互挂（Angora 官网 Teknoloji Ortaklarımız/Наши партнеры 墙 larch+marvell，镜像 13 号 L33）
- ⭐ 结论 4（Larch 公司档案全量）：2009 工程师创立 + Marvell 战略合作（全球 ROS 支持）/ 2010 基辅办 / 2016 OpenROS + 首推 OpenSwitch 1.0 on BC3 / 2017 Fast-boot<30s + POF 交换机 / **2018 首推 BC3 TOR SONiC SAI + PB 方案合作** / **2020 首发 400G Falcon（哈萨克斯坦首客户）12.8T/1U** / **2021 48×25G+8×100G 2Tbps TOR（= Angora OM 同构）** / 2022 MCLAG+PTP1588 / **2025 Ironman 模块 + FastBoot<10s**；Marvell Certified SP；设备 6 类 + ORAMA X400 + LN-2324GP/LN-3548X/LN-4348Y/LN-3848G-6Y 系；新闻 = Quantum SONiC（2023-10 与 Quantum+Sartura）/ERPS（2024-07）/SONiC 150 SKU（2024-08）/Ironman（2024-08）/BFD+ 案例（2026-02）/**Dorado Ethernet AI Fabric @ OCP（2026-10 最新）**；人员 5（Cheskis CEO 等，40 号）
- ⭐ 结论 5（**宪法规则落库**）：「抓到的信息全部入库，无例外」→ `AGENT-CONSTITUTION.md` **第十条「全量入库义务」（v2.0→v2.1）**（范围含"次要"信息/落库位置/紧凑 MD 最小占用/每轮交付前对平自查，漏 = 违规）+ `workstation/README.md` **§0 规则 6**（同源；宪法优先）；范围从 r27「订单信息全部入库」升级为**全部信息**
- 结论 6（angoranetworks.com 重验 = 用户点名）：2026-10-21 直连 = 活着（WP TR/EN/RU；首页 Anahtarlar/SFP/İnce İstemci→thince.net/Hizmetler；**Haberler 最新 2023-12**〔二极管线，r19 不向用户展示〕；support. 活）→ 与 r23/r31 一致（新闻停更 ~2 年 10 个月）；全量镜像 = 既有 `04-website-mirror/` 5 件（最小占用不重复落盘）
- 产出 = 新建 `09-orders/125-tronx-website-forensics-2026-10-21.md`（6 节）+ `06-competitors/41-larch-angora-partnership-timeline-2026-10-21.md`（9 节）+ `06-competitors/40-larch-saga-email-history.md` 增补节八（只增）
- 边界：TronX「伙伴」本人未具名；Larch 首票精确日期不可考（2023-08 = 窗口下限）；T-IQ-PB「1.9Tbps」vs datasheet 3.2Tbps = 官网降档标称待核；OCP Dorado 博客全文 + Larch /team/ 全名单 = 低优待办
- 簿记：TASK-STATUS 行 AO + 行 C/§六 Larch 行范围注 + conv-log 32（JSON 34）+ AGENT-README + WREADME（370）+ 宪法 v2.1
- 监控增量：tronx.com.tr 是否修复 VERGE 页 / angoranetworks.com 内容更新 / Larch 官网 logo 墙与 clients 页变动 / OCP 2026-10 Dorado AI Fabric 后续

## §27 · 第 33 轮 — 2026-10-21 ≈22:3x：partner 竞标体系全量挖掘 + 公司名/网站/合作事宜全搜入库

- 用户：「levent 一直说 通过 partner 竞标 是 TronX 吗？ / 再读 wechat 和 drive 信息，只要出现的公司名 网站 公司相关讨论 合作商/合作事宜等 都好好搜搜多挖入库」
- ⭐ **直接答案 = 不是 TronX = ⭐Elips**（2026-07-06 L9751-9755：「that is bidding partner and they are the money (i.e. capital) behind this deal」；TT 项目手册 = ELIPS 品牌 ELS-L2PI-8GP-2F ≈ 我方 STI-288DGGPM 族；88 台死因 partner 交期改主意 = 大概率 Elips 待核）
- partner 103 处提及全对平（15+ 关键行日期钉死：2024-05 back-to-back → 2026-10「That's exactly what we do now」）；三层结构（Elips=竞标+资本 / TronX 背后伙伴=品牌销售 / 每标轮动=招标执行）；Levent 竞标 playbook 6 条（back-to-back/尾分钟报价/Game Theory+distributor 融资/Plan B 隐藏工厂/隐藏我方身份/首标口碑优先）
- 外网取证 4 实体：⭐**Elips Elektronik**（elips.com，1988 起，Wealth Fund/总参谋部客户，51-200 人；同名 7 家排除；法律实体待核）/ ⭐**Kyland=东土科技（300353）**（110 行 89 新入）/ ⭐**UDE=U.D. Electronic（TPEX:3689）= 我方 RJ45 供应商**（Simon 2025-01-10「we are using this brand」）/ **Rima**（111 行 13 重验：Digifort AI VMS+多品牌矩阵+「We have not done business before」）+ **Netaş 增量**（110 行 2：曾从我方买 3 样品〔项目死〕+ Moxa/Hirschmann 替换）
- 产出 = 新建 `09-orders/126-angora-partner-bidding-map-2026-10-21.md`（5 节）+ `99-raw/r33-partner-company-mining-2026-10-21.md`（103 条 verbatim 全量+域名全提取+对平表）+ 110/111 三件套更新（372 文件）
- 边界：Elips 法律实体待 Levent 确认 / EGM 4/28 标结果未索引（r29 待办）/ EGM 3 伙伴与 Elips 同批未证实 / PASSED 不复活（48 口/tiered pricing/「strong partner」全名/88 台/TronX $1,480 等）
- 簿记：TASK-STATUS 行 AP + conv-log 33（JSON 35）+ AGENT-README 7 处 + WREADME（372）+ 本 §27
- 监控增量：Elips 法律实体（Levent 侧确认）/ EGM 4/28 标结果公开索引 / TT 线 Elips 品牌 ELS-L2PI-8GP-2F 是否量产出货 / NETAS Moxa/Hirschmann 替换项目重启信号 / UDE 交期（我方备料风险）


## §28 · 第 34 轮 — 2026-10-21 ≈18:29：生态公司全站爬取入库 + Larch 最高优先深挖

- 用户：「语料出现的所有公司 网站全部爬一下 都入库 / 与 Angora 的合作关系/结构 各角度深挖 / 尤其 larch networks」
- ⭐⭐ **Larch 第二波直连 20+ 页**：产品全目录 4 线×芯片号全标（campus AC5+=98DX2538〔含 HSP/HSF 热插版〕/ AC5lite=98DX2518 / AC5X=98DX3510+**(M) MACsec 12 SKU**〔2.5G 接入+6×25G+PoE++1440/1480W〕/ AC5Y / **Campus AC3=98DX223S〔≠工业 226S，双芯片修正〕** / 工业 AC3=98DX226S / DC Aldrin1/2/3=98DX8382/8548/7332 + **Falcon=98CX8514/8522/8580**（ARM/Intel）+ **Teralynx 表（IVM77700 32×400 / 98TX9180 64×800）** + **NVIDIA X2 表（32×400/16×800）**）+ **⭐2025-11-02 加入 SONiC Foundation** + **OCP 2026 B31**（TeraLynx 10 spine-leaf + Hardened SONiC + ConnectX-7 GPU + Dorado Cruz；以太网替代 InfiniBand 叙事）+ blog 26 篇全时间线 + client 24（Angora 第 4）+ partner 8 + **contacts（11 Amal str, Rosh-Ha'ayin 4809239, Israel；+972 3-901-6117/8）** + **新 BD 联系人 Irina Murzina** → 41 号 §10（只增）+ 127 号 §2
- ⭐⭐ **Sagatele（Saga Telecom，深圳）= 我方 ODM 工厂 100% 证据**：双域名全抓（sagatelecom.com.cn=产品目录 40+ SKU 三产品线 STI/STC/STH〔STC=Marvell Prestera AC 系=我方 TT 系列平台 / STH=CENTEC L3 10G-800G〕+ sagatele.com=公司页〔「Marvell Prestera **AC5 Lite·AC5·AC5+**」= 语料「AC5/AC3」命名同源 / 「position against **Taiwanese brands**」/ 不做 EN50155-IP67-云管〕）+ 语料 4 证（L528 SFP 供货 / L2368「All based on Saga products」/ L4042「100% with Saga」/ L8765「Saga does not pay VAT」=VAT 主体）+ 战略芯片库存 + WhatsApp +86 15237149683 → 127 号 §4
- ⭐ **Elips 法定实体名坐实**（r33 遗留闭合）= **ELİPS ELEKTRONİK SANAYİ VE TİCARET LİMİTED ŞİRKETİ**（b2bhint registry 268901，成立 **1990-10-03**，实缴 100,000 TRY，#631108；1988=品牌起步口径）+ 10 源（官网 elips.com / LinkedIn 4 公司 120 人 1200m² 自有楼 / EMIS 24 人 2024 营收 +20.05% / ZoomInfo 85 / RocketReach $5.8M Novartis 20 年 / Kariyer 7 年 400% / RevenueBase reseller 第 5 / 100metre / b2bhint / firmasec）→ 127 号 §5
- **生态 18 站全爬**（18 成功 + 6 异常状态入库）：Maipu（中东展会密集）/ Centec（2005 苏州）/ H3C（Gartner Visionary）/ Moxa（RKS-G4030-PL + EcoVadis 金）/ **Marvell 2026 定位（「Marvell is how AI scales」五组合）** / **⭐D-Link 2026-09-11 DIS-110G 工业交换组合（工业线新压力源）** / Belden 根页（Hirschmann 母；hirschmann.com 不可达×2）/ **⭐Dahua（数通产品类 + 赢标 L9275 + 捆绑策略 L8805）** / Hikvision（观澜大模型）/ Kyland（Aquam campaign 互证）/ **Netaş（EYDEP A 级防务认证 / R&D 250 行业第 3 / 伊斯坦布尔机场 ICT 承建+5 年运营 / ZTE 服务器本土化 / Microsoft LSP AZ+KZ / 2026H1 增收增利）** / TT（iPhone 18 预约 / TurboBox 5G）/ UDE（月度营收公告 / QSFP-DD-800 自研）/ Rima（Digifort AI VMS 99.87%）/ NEM Engineering（nemengine.com，Karen 在任）/ PNetworks（AA 2021-04-02 发布会全文）/ Keenetic（2026-05-14 卖 switch）/ **cryptoink 不可达×3=休眠**
- **语料 16 处 verbatim 全入 99-raw §6**（Taylan=Angora CTO 是人非公司 / Karen=NEM Engineering 是人 / **TronX=同厂姊妹品牌 L4290/4314/4471** / **Connexite=英国客户 L5813**（与 123 号「Levent 并行 CONNEXITE London Managing Partner」互证）/ UDE=L2698 RJ45 BOM 断料 / Dahua L8805/L9275 / Maipu L2191/2201/10381 / Moxa+Hirschmann L7848 Netaş 替换）
- 产出 = 新建 `06-competitors/127-angora-ecosystem-companies-crawl-2026-10-21.md`（8 节）+ `99-raw/r34-ecosystem-crawl-2026-10-21.md`（7 节，含对平总表 §7 PASS）+ **110 行 90-98 新入 9 行**（D-Link/Dahua/Moxa/Hirschmann/H3C/Maipu/TronX/cryptoink/Larch，三件套同步：CSV 99 行×20 列机械校验全过 + XLSX 99 行回读 + MD §18）+ 41 号 §10 增补（只增不删）
- 关系结构 = 127 号 §1 六角度表（供货/同平台竞争/资本竞标/替换竞争/定位基准/供应链风险）
- 边界：Larch 低优先缺项 4（AC5Y 后续 chunk / Ironman 模块页 / sonic-sai / sonic-hardening，URL 已知可后补）/ cryptoink 法定实体未查得 / hirschmann.com + mikrotik.com 不可达（代偿完成）/ TronX 法定实体待核（r32）/ PASSED 不复活
- 簿记：TASK-STATUS 行 AQ + conv-log 34（JSON 36）+ AGENT-README 7 处 + WREADME（374）+ 本 §28
- 监控增量：D-Link DIS-110G 土市场铺货节奏 / Netaş Moxa/Hirschmann 替换项目（我方工业线对标报价）/ Larch OCP 后续 + Amphenol TSN 峰会后续 / Maipu LEAP 沙特后土耳其辐射 / TT co-development（2026-03-09 线）/ UDE RJ45 交期恢复

## §29 · 第 35 轮 — 2026-10-21 ≈19:1x：自由深挖八线（用户「继续挖东西吧 看看能搞出来啥」）
- 触发：用户自由指令，深挖最高价值未闭合线（Sagatele 目录对平 / D-Link DIS-110G / PNetworks-Pavo / Keenetic / NEM / Larch 缺项 / Levent×Connexite / SERA-Dorado）。
- **⭐Levent×Connexite 穿透（新实体发现）**：CONNEXITE LTD（Companies House 14770313，London N14 6HF，**SIC 26200 计算机制造**，2022 成立，4 人）股东 4×25% = **LEVENT KILIC（我方 GM）+ MEHMET TAYLAN ESEN（我方 CTO）** + MEHMET YASIN KORU + IBRAHIM BALCI → **Angora 创始团队英国实体**（业务=OT 安全 ConnexONE + UK/海湾 NCA/NESA；团队=Levent CEO + Mehmet Koru HW/SW〔Ankara，兼 MEVA Avionics〕+ Uras Acar BD〔Brussels〕；2024-08 新董事 Donald Isufi；Levent LinkedIn 双挂 connexite.co.uk+angoranetworks.com）→ 123 号 r35 补（只增）。
- **⭐Larch 缺项补全**：① **SKD/CKD 本地化生产官方计划**（/hardware-development/hardware-production-localisation/，r34 404 因 slug 错）Step2 拆解含 PCBA / Step3 PCB 交付 SMT+全部元件 = 我方「yerli」路径第二选项（Sagatele 深圳 ODM 之外）② **Ironman 工业模块线 5 型号**（MO-P8Cx-4F 50G / MO-16Cx-4F 72G / MO-24Cx-6F 86G / MO-48Cx-6F 110G / MO-24Cx-28F 126G；ARMv8 双核 1.2GHz/DDR4/eMMC 256G/可选 256b MACsec/HSR-PRP/TSN/级联 1K；datasheet 2026-06=新品；Embedded World 2026 演示 PRP on Ironman）③ **Hardened SONiC**（/sonic-sai/sonic-hardening/ 正 URL；工业可选 G.8032 ERPS+PTP 1588+**ITU-T G.8273**；HA Fast Reboot/warm upgrade；Modular BGP/VLAN/QoS 可加卸；uCentral ZTP 开源；PoE af/at/60W；whitepaper LN SONiC.pdf）④ 生态 7 项（Xsight Labs CoE=X-Series AI Ethernet switch+E-Series 800G SDN DPU / **SIDERA Intelligent Systems=UAE 本地化品牌〔与 Larch 共建，与 Angora 模式同构〕** / SERA=100/400/800G DC COMPUTEX 2026 / Miyagi 远程管理 NOS / IP Infusion 历史 / Falcon 换 Bobcat3 48×25+8×100 2T / productizing SONiC=未具名 major global brand ToR SONiC 盒式 green DC 评估中 / Network World 2026-10-21 当日 Dell'Oro 点名 OLS 代表厂商 / Odoo ERP / InnoVEX 2026）→ 41 号 §10.8-10.11（只增）。
- **Sagatele 完整目录对平 12+ SKU**（sagatelecom.com.cn + sagatele.com 双站同源）：STI-488XGGPM2B-2BT / **STC-424XGGPM-280W（≈我方 TT-2208 平台带）** / STC-448XGGPM-4BT-740W（1-4 口 90W，336Gbps，<5µs）/ STC-448XGGMO（全光 L3 13K 路由 499.9Mpps USB+Console）/ **STC-448XGGM=官网明写 Marvell AC5** / STH-2C12XF12XE-HSI / STH-2C24XF-HSI（半宽 24×10G+2×100G 880Gbps MLAG 双活 SDVoE）/ STH-8C48DX-HSI（48×25G+8×100G）/ **STH-32QC-HSI（32×400G→64×400G 25.6Tbps MPLS/VXLAN/EVPN+MACsec 2×1300W CRPS MTBF≥90K）** / STI-21616GP（户外 16 口 PoE+ 非网管 240W 6KV -40~+75，⚠️撞 D-Link DIS-110G）。特性全集=ERPS G.8032<20ms/QinQ/802.1X+RADIUS+TACACS+/DAI/IPSG/DDoS/sFlow/MQTT/双分区/光纤 bypass LC≤10ms/DI-DO-RS485 Modbus/**固件 V7.5.x roadmap**。STH 线=CENTEC（BGP/IS-IS/EVPN-VXLAN/MPLS/MLAG/stacking/10G-800G OSFP/DCB）；Realtek=副线；白牌=HW+FW(CLI/MIB)+UI「architecture changes not label changes」；Insights 2 篇 Coming soon。判定=Sagatele 公开目录=我方 TT 线同平台带（Prestera+CENTEC 双芯策略与我方一致）。
- **⭐PNetworks=站恢复可达=品牌 Pavo Group**（pnetworks.com.tr，pavo-group.com）：产品线升级=AI/ML+Cloud DC+Operator+Optics；CEO=Bilal Yıldız；**2026-07-30 土主权基金 TWIF CFO&COO Dr. Mahmut Kayacık 会 Pavo CEO**（TWIF=Elips 客户→Elips 与 PNetworks 双线接触主权基金）；2026-08-27 Republikorp（印尼 Norman Joesoef）土-印尼防务；IG/LI=pnetworkstr、X=@Pnetworks_。判定=已从 yerli switch 单点升级为集团化+主权基金背书+AI/DC 转型。
- **D-Link DIS-110G 规格落地**（press 2026-09-11 Taipei）：DIS-110G-05/-06P/-10/-10P 全**非网管**工业 GbE（IP40 无风扇 -40~+75℃/6kV 全铜口/250m@10M 长距/PoE+ 30W 预算 240W 与 120W/**PD Alive 自动重启**/DIP Fast Ring/双 DC/802.3az）=监控/楼宇/标牌低端入口；与 Sagatele STI-21616GP 同带正撞。
- **Keenetic TR 路由矩阵全列**（keenetic.com.tr/en）：KN-1013 Hero BE3600+10G SFP+ / KN-4210 TITAN SE BE7200 / KN-5210 Roamer 5G / KN-4110/4010/2013/3611/2113/1812/3910/1012/3811 / **⭐Stellar 6 KAP-650=IP65 PoE+ -40~+65℃ 户外 AP（线内唯一 rugged）** / KAP 530；KeeneticOS 云 demo=keenetic.demo.keenetic.pro；switch 线不变（unmanaged 零售）。
- **NEM Engine 供货全线**（nemengine.com）：NM-280-RJ45 SFP（10/5/2.5/1GbE MSA）+DAC+AOC（10G/40G/25G/100G）；站陈旧（2016 新闻仍在）=信息时效边界。
- **TronX 店页在线**（tronx.com.tr/shop/）：Mustafa Kemal Mah. 2124 Cad. No:14/1 Çankaya/ANKARA；+90 312 309 19 54；info@tronx.com.tr；「2008 医疗起家→今生产+服务 IT/健康」自述；法人股东公开不可得（MERSİS 不可公开检索）。
- **cryptoink 死档坐实**：全网搜索 0 土耳其实体命中（仅 CIK 币/CryptoINK LLC/e-ink 项目/cryptoink.online 噪声）→ 仅语料 L10362 痕迹。
- **沙箱重置事件记录**：本轮开始发现 /home/user/Angora 被重置到 c4085aa（workstation 丢失）→ origin/arena b40cc51 fetch + `git reset --hard` 恢复，**0 数据丢失**（r34 及以前全在远端）。规则：任何簿记/落库写入后必 grep 验证 + 沙箱重置后立即 `git fetch origin` 恢复。
- 落库：`99-raw/r35-deep-dive-batch-2026-10-21.md`（11 节逐字底稿）+ 127 号 §9（只增）+ 41 号 §10.8-10.11（只增）+ 123 号 r35 补（只增）+ 110 三件套行 1/9/90/98 备注更新（CSV utf-8-sig CRLF 99×20 csv 模块断言 + XLSX 99×20 回读 + 4×r35 标记）+ 110 MD §19 + 全套簿记（TASK 行 AS + conv-log 35〔JSON 37〕+ AGENT-README 6 处 + WREADME 375）。
- 对平自查（宪法第十条）：本轮抓取 13 项（Sagatele 2 站/D-Link/PNetworks/Keenetic/NEM/Larch×3/Connexite 穿透/SERA+Larch 生态搜索/TronX/cryptoink）= 全部落库，无遗漏。PASS。
- 监控增量：Pavo Group 与 TWIF 后续动作（主权基金=Elips 客户，双线接触）/ Larch SKD/CKD 是否对 Angora 具体报价（yerli 路径决策项）/ D-Link DIS-110G 土市场铺货 / Sagatele V7.5.x 固件发布 / Connexite Ltd 年报（SIC 26200 英国实体经营面）。

## §30 · 第 36 轮 — 2026-10-21 ≈20:0x：土耳其本土「类 PNetworks」品牌侧客户深挖（用户「挖一些土耳其本地的客户 公司啥的吧 就是和 saga 产品很契合的 类似那个 PNetworks」）
- **⭐新潜客 3 家 + 防务客户池 1 家入 111 管线（行 52-55，三件套同步 51→55 行）**：
  - **upTech / Nokta Elektronik ve Bilişim Sistemleri A.Ş.（Istanbul Şişli Perpa）**=Türk Patent 注册品牌 **marka no 2008/13951（2008-03-11 首注册，续展至 2028）**；品牌下 **916 SKU**（Aktif 81=PoE switch 802.3af/at 相机/AP 供电+uplink/VLAN/extend+SFP/SFP+/MC；Pasif 157；Power 140；RF 267；AV 424）；「产品开发质控由自家 AR-GE 团队负责」+ firmware 公开；+90 212 222 87 80；B2B 平台 noktaelektronik.com.tr → **Perpa 批发规模注册品牌主=Saga PoE switch+SFP 白牌/ODM 目标客户（评分 78，A 级）**。
  - **WINET（wi.com.tr）**=**MikroTik Authorized Distributor**+PON/光纤专业商；品牌矩阵 MikroTik 463/WINET 417/Ubiquiti 317/VSOL 23/Huawei 25；WINET 自有 417 SKU=被动件+**micro OLT stick SFP 1:32**+8 口被动 PoE 注入面板（标 Yerli Üretim 12-56V）+ODP 分线箱；B2B tier pricing+30-day net → SFP+PON 邻接先行，switch 白牌意向探测（评分 64，A-）。
  - **TekniksatGroup（TGD，1992 起）**=CATV/SMATV/CCTV/光纤垂直集成商，「Üretim tasarım uygulama %100 yerli」自述；自有 **TGD 48V PoE switch 线在售（TGD-P4/48·P8/48·P8S/48·P16S/48·P24S/48+24V 线）**+SFP+AP+intercom+multiswitch+headend；在线店 hepsiuydu.com → **⭐48V PoE=与我方工业 48V DC 线直接契合（评分 72，A 级，高 fit）**。
  - **ULAK Haberleşme（Ankara）**=军通；IDEF 2025 与 Netaş+Teknopark İstanbul 签 yerli 5G 基础设施战略协议；switch 产品线未见公开=需求侧买方 → 防务标单监控（评分 45，B）。
- **既有行增量（110 行 2/20 备注，只增）**：**Netaş**=2024 年报 800GE ethernet×ZTE 测试（单载波 800G 无再生 2,000 km 2026-02 世界纪录叙事）+SAHA EXPO 2024 50 周年+Orhanlı 基地+taktik saha/gemi haberleşme → 高速网络需求侧铁证；**Longline**=NetGaste 2025-10-14+Teknoblog 2026-02-05 软广实锤在投（r19 疑似软广源坐实）。
- **留档（99-raw r36 §6）**：Sekom（Turkcell MWC 2026 Sekans DHCP 软件）/YONGATEK（RISC-V ÇENTİK 芯片 TSMC）/ElectraIC（3U VPX 机箱）/General Mobile（5G 手机厂 $60M）/Aselsan×TT 地方手机/**VSOL=中国 OLT 厂（PON 侧同层 ODM 竞情参照）**/34Alarm(DayLine)/aktifsat=零售/AN-EL=电气开关元件（排除）/Teknopark 2021 PNetworks 规格原始出处/Özbilen 2023 七条宣言/Netaş 年报其他（Nubia 5G 等）。
- **边界/死档**：«yerli switch» 新闻搜索 2021-2026 无新制造商（PNetworks 叙事垄断；Keenetic 为 2026-06 新 switch 产品线，非新制造商）/ BİGG 项目表 PDF 未逐项解析 / 土耳其 CPSE 2025/2027 参展商名录无公开索引 / Perpa «kendi markası» 搜索=噪声 / ULAK 品牌方证据缺失（仅需求侧）。
- 落库：`99-raw/r36-turkey-local-customer-mining-2026-10-21.md`（8 节逐字底稿）+ 111 三件套行 52-55（56×17 断言）+ 110 三件套行 2/20 备注增量 + 全套簿记（TASK 行 AT + conv-log 36〔JSON 38〕+ AGENT-README 6 处 + WREADME）。
- 对平自查（宪法第十条）：本轮 fetch 5 页（nokta upTech 2 chunk/tekniksat 2 chunk/wi.com.tr 1 chunk/yesilkoy 1 chunk）+ search 10 批=全部落库（底稿 §1-§7 + 111 行 52-55 + 110 行 2/20）。PASS。
- 监控增量：upTech 是否已签固定 ODM（firmware 迭代频率）/ WINET switch 白牌意向 / TGD 48V PoE 出货面 / Keenetic 2026-06 起售价格带 / ULAK×Netaş yerli 5G 标单 / Sekom 硬件化动向。

## §31 · 第 37 轮 — 2026-10-25 ≈11:5x：用户两份客户名单 + 2025土耳其ISAF客户.xlsx 全量入库（用户：「我在main上传了2个客户list 你读一下 深入挖掘一下这些客户 看看哪些能跟进啥的」+「2025土耳其ISAF客户.xlsx main又传了这个 一起处理吧」）

输入三件（`git show origin/main:<path>` 读取，不 merge）：① `AI客户评估_TR 10.06.xlsx`（master No.1-50 双 AI 评估 AI+CALUDE，14 列，51-300 空模板）② `Turkey Client List.xlsx`（299 行原始名单）③ `2025土耳其ISAF客户.xlsx`（Sheet1 合并 51 条 No.26-83 + Evelyn 28 + Ady 29 + Simon 31；实际 9 列，部分行缺 Name/Position 左移→邮箱锚定修复）。
落库（99-raw 7 件）：`r37-ai-kehu-eval-master.tsv`（64KB 逐字）/ `r37-turkey-client-list-299.tsv` / `r37-isaf-2025-raw.tsv`（142 行）/ `r37-isaf-union.json`（去重 98）/ `r37-detail-sheets.tsv` / `r37-user-customer-lists-2026-10-25.md`（交叉比对+24 新客深挖）/ `r37-isaf-2025-analysis-2026-10-25.md`（ISAF 逐家分析定稿）。
交叉比对：master 50 ↔ 111/110 = **26 家在库**（111 行 1-23 共 25 家 + 110 行 20 Entegron）/ **24 家新**=111 行 56-79（⚠️=r19「排除 24 家」同批，用户 10.06 双评估=重新定级，r12 只增不删留痕保留）；master↔TCL 映射 43/50 命中+7 家仅 master 有，50/50 闭合；双评估分数全量核验 PASS。
ISAF：去重唯一 98=**TR 新增 66 行（111 行 80-145：A 12〔80-91〕+ A- 8〔92-99〕+ B/C 46〔100-145〕）**+ 在库 2（行 2 NovaCom/行 3 Snexus 只加 ISAF 面见备注）+ 非土 13 留档（RS×2/BG/LY×3/GR/PS×2/UA/TN/XK/IR+0770 SY）+ 特殊 3（eu.equinix.com=r22 不跟进 / Maipu=中国参展商竞情 ONV 80USD / Vatankhah=Tiandy 员工）+ 其余=既库/已分析（r20/r21）不双录。bypass 专项 8 条明确需求（IHM/Aycan CAM/BİLGEN/ONSIS/Netmax/ORAL/Serkan/SFP Turkey）→ 下轮 bypass 专刊+样品策略。
关键深挖（批 1 直连+批 2 web_search）：PavoTek=**Pavo Group 电子/嵌入式子公司**（110 行 1 关联，TCL #5）/ Entegron=**LONGLINE 自有 CN OEM 品牌**（110 行 20，TCL #60，PoE 31 型）/ Optima（IFSEC 面见拟访深 Furkan Kalkan 90507 463 0566）/ Filiz（1994 Izmir，迪拜面见 90533 74 63788）/ Okisan（**Tiandy+Dahua 土授权分销商** $8.6M/5000 经销）/ CryptoLink（CRL 系+KGYS 实证）/ Cenova（E-wind dl-end3308pfg）/ OPAX（OPAX-08120W $35=HRUI 同源价锚）。
交付：111 三件套 55→**145 行**（CSV/XLSX 17 列断言+MD §十一，构建脚本 `08-customer-pipeline/build111_r37.py`）/ 110 三件套行 1/20 备注（CSV 99×20+XLSX+MD §二十一）/ **112 号跟进推荐主档**（`08-customer-pipeline/112-user-customer-lists-deepdive-2026-10-25.md`：Tier1=既库 7〔NovaCom/Snexus/OPAX/CryptoLink/Telkolink+GelecekBT/Entegron-LONGLINE/Cenova〕+ISAF A 12+Selim Kalaka〔行 92，郑州换源=最高优先〕/ Tier2=Optima/Filiz/Okisan/Karer/CCTV Depo+A- 8 / Tier3=监控 14+绿灯 6+战略留档 PavoTek/Kıraç）/ 全套簿记（conv-log 37〔JSON 39〕+ AGENT-README + WREADME）。
对平自查 PASS（宪法第十条）：三输入逐字 100% 落库（TSV/JSON 底稿+分析 MD）；抓取/搜索全落库（批 1 5 站直连+批 2 web_search 5 家）；二极管 0；PR 合并 0；文件数 385 find 实测。

## §32 · 第 38 轮 — 2026-10-25 ≈12:0x：土耳其客户总档统一 XLSX（用户：「把这些所有的客户 挖到的 给你的统一整理进一个xlsx里吧 分不同的sheet 注意是xlsx」）

执行：新建 `08-customer-pipeline/build114_r38.py`（确定性构建脚本，只读仓内既有底稿，可复跑）→ 产出 **`08-customer-pipeline/114-turkey-customer-all-in-one-2026-10-25.xlsx`（单文件 7 sheet，用户指定 xlsx 格式）**：
1. **README说明**：来源/口径/Sheet 索引（Tier 定义、Turkey-only、equinix 不跟进、r19 重评口径、bypass 专项）
2. **跟进推荐112**（55 行结构化）：Tier1 立即 20（既库 7〔NovaCom/Snexus/OPAX/CryptoLink/Telkolink+GelecekBT/Entegron-LONGLINE/Cenova〕+ ISAF A 12 + ⭐Selim Kalaka 最高优先）/ Tier2 暖渠道 12（Optima/Filiz/Okisan/Karer/CCTV Depo + ISAF A- 7）/ Tier3 监控 21（14 红黄灯+6 绿灯+EuroCam）/ 战略留档 2（PavoTek、Kıraç 集团）；列=优先级/客户/管线行/双评/核心钩子/我方打法/产品线/联系人
3. **全管线111(145)**：145 行×17 列原样
4. **ISAF2025(98)**：98 条全量（原表 No./Sheet/重复来源/国家/原始文本/web/email/手机/interest/处理状态）；处理状态=TR 新增 66 家 76 条〔10 家跨 sheet 重复×2 标注〕+在库 3〔NovaCom/Snexus/CESS=Shnrise 行 37〕+TR 已分析 2〔Karaal×2 r20 未入库〕+非土 14 条/13 家+特殊 3〔equinix 不跟进/Maipu 竞情/Vatankhah Tiandy 员工〕=98 ✓
5. **用户双评估50**：50 行×10 列（含双 AI 评估逐字）+库映射（111/110 行号）+跟进层级
6. **TCL原始299**：299 行+映射状态（域匹配在库 26〔含 #5 PavoTek→110#1/#111#59、#60 Entegron→110#20〕/未评估批次池 273）
7. **110竞对地图(98)**：98 行×20 列原样（含「与Angora关系」列）
断言：7 sheet 名/行数全对（55/145/98/50/299/98）+ ISAF 行 80-145 各匹配≥1 条 union 且×2 恰 10 行 + 回读校验 PASS。
边界：union JSON 非土 13 条 country 字段为空→按手机区号+域名人工终判回填 14 条/13 家（Todorov 跨 sheet×2）；CESS Govalik=Shnrise（r20 已录 111 行 37，union 邮箱空未命中→人工锚定）；Karaal=r20「❌无法核实」未入库→留档可再核实升级；TCL 域匹配=精确域+后缀域口径，未匹配 273 家=249 批次池+评估在库 24 家域未挂 111 公司名括注（映射以「用户双评估50」sheet 库映射列为准）。
簿记：LEDGER §32+TASK 行 AV+conv-log 38〔JSON 40〕+AGENT-README 8 处+WREADME（387 文件）。

## §33 · 第 39 轮 — 2026-10-27 ≈09:20–09:26 (+0800)：Ewind 官网 + 全部 Angora 站点直连重爬 + 时间戳/变更对照（用户：「把你之前做的再过一次」「只要关于 EWIND 的信息都要爬 都入库」）

采集窗口：**2026-10-27T01:20Z–01:26Z**（= 09:20–09:26 +0800）。基线：r24/r25（2026-10-21，112/113 号档案）。产物目录 `06-web-crawl-2026-10-27/`，**16 个文件**。

**手段升级**：112 号档案记录的是"ewindnet.com 直连 3 次全失败 → 只能用 web_search `site:` 索引快照"。本轮 `fetch_page` 直连 **全部成功**（首页 / sitemap 索引 / 产品 sitemap / 展会 sitemap / 页面 sitemap / WP REST product+posts / 两个产品页 / Angora 全站），拿到页面自带 `date`/`modified` 精确到秒。**112 号"域名持续不可达"的表述自此过期，已在 112 正文顶部补注。** 沙箱 bash 仍无外网，故只存渲染文本，**原始 HTML 字节不可得**（每条 artifact 的 capture 字段已注明）。

**Ewind 结论：自基线以来零新增。** 最新产品 `modified` = **2026-08-07**（id 10869 EW-S1710FG-AP），最新文章 = **2026-06-11**（id 10678），展会 sitemap 停在 **2025-11-05**（CPSE 深圳）。产品 sitemap 索引的 2026-08-26 是 id 8143/8131 两个 2024 老 SKU 的重新保存，**不是上新**。

**新增实质情报（首次抓到，非"变化"）**：
- **EW-S57948QM**（id 10573，2026-05-11）：48×2.5G + 4×10G SFP、1280 Gbps / 952 Mpps、**BGP**、150 W、7 kg、0–40 °C。⚠ 标题写"100G SFP"而规格表只有 4×4G/10G —— 标题与规格表冲突，已标注。
- **EW-S1710FG-AP**（id 10869，2026-08-06）：8×1G + 2×SFP 非网管 PoE、120 W 内置电源、**E/V/D 拨码**（300 m 长距 / 端口隔离 / AI-PoE 看门狗）、**仅 1 年质保**（全目录最短，同门多为 3 年）。
- 153 SKU 逐条发布/修改日期表、125 篇文章日期表、11 条展会时间轴。

**Angora 结论：内容无变化，但抓到 3 个家族的精确时间戳**：Verge（page 298 `modified` 2026-04-03 / page 1775 2025-06-11）、Synapse（1781，2026-01-15）、Hitit（1804，2026-03-24）。正文与 **2026-09-23 镜像逐行一致**。

🔴 **本轮最重要的更正是针对我们自己的**：中途一度把 Synapse/Hitit 记成"r24/r25 完全没有的新家族"。**已撤回**——两者 2026-09-23 即已全量入库（`04-website-mirror/10-pages-part1.md` §⑤§⑥、`12-pages-part3-specs-and-codes.md` §一）。误判成因：112/113 只覆盖 Ewind，把它当"Angora 基线"就会凭空"发现"旧东西。另有 3 条 Ewind 侧更正：①"年参展 20+"仅首页营销语（站点自身只有 11 条展会页）；②Angora 9 篇文章 `modified` 全为 2026-06-15T12:xx = CMS 迁移，**不是重新发布**，最后真实发布仍是 2023-12-06；③产品 URL 必须带 `-1` 尾缀（裸 slug 404 是我方拼法错误）。

**未能复核（不得当已核实引用）**：`ru.ewindnet.com` 及其他语言子域 fetch 失败（"12 语言站"仍是 r24/r25 结论）、Alibaba/Facebook/LinkedIn/ZoomInfo 本轮未访问、`larch-networks.com` 未访问、全部 PDF 数据表未下载（只有路径）。
