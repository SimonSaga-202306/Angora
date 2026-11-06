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

## §34 · 第 40 轮 — 2026-11-01 ≈13:29–13:45 (+0800)：Ewind 官网 + 宣传面（Alibaba）+ 6 份 PDF 复爬 / Angora 宣传册首次入库

采集窗口 **2026-11-01T05:29–05:45Z**。基线 = **r39（2026-10-27）**。产物 `07-web-crawl-2026-11-01/`，**17 个文件**。

**Ewind 官网：连续第 2 轮零新增。** 产品 `modified` 最大值仍是 2026-08-26（id 8143，2024 老品重存）；最近真实上新 2026-08-06（距 87 天）、最近文章 2026-06-11（143 天）、最近展会页 2025-11-05（361 天）。页面 sitemap 补完：**40 条 URL**（r39 只取到 chunk0 的 18 条），新增 12 个行业垂直页（全部 2024-07-30~08-02 一次性铺量、之后未改）+ 3 个 SEO 落地页 + 售后/质保页。

**宣传面三件新情报**：
1. ⭐⭐ **19 个非英语子站全部下线**——实测 `es.` / `tr.ewindnet.com` 均返回 "GTranslate Error 402: Subscription Inactive"。语言切换器实测 **19 个**语言（不是 r24/r25 记的 12 个），全是 GTranslate 机翻子域而非独立本地化站。**土耳其语站已不存在**，与官网内容停滞共同指向"低成本维持"状态。
2. ⭐ **Alibaba 店铺首次直连成功**（r25 只能靠索引快照）：4.5/5 店铺分、准时发货 99.0%、响应 ≤3 h、**在线营收 US$240,000+**、**员工 33 人**、平台 7 年、主要市场东南亚/东欧/中东。与官网"200 人 / 5,000 m²"形成可量化落差（旧快照厂房 2,200 m²）。价格带：$6.30–7.20 延长器 → $21.50–23.50 EW-S1806CF-AP → $97.5–258 工业网管。
3. SEO 落地页暴露 8 个我们档案里没有的型号（EW-S1712CG-AP、EW-S2924SM-AP、EW-S2910SM-DP、EW-ES3028/3020/3010CGSH-AP、EW-ES3006FGSH-AP），并显示 2026-06 新开 **Lite Management Switch** 类目。

**PDF 数据表首次读到正文，推翻 r39 的 4 个数值**（EW-S1710FG-AP：温度 0–50→**−20~+55 °C**、MAC 8K→**2K**、拨码 V/D 仅 **1–4 口** 非 1–8、补 **IP30 + 4 kV + CCC/CE-LVD/FCC**）；**EW-S57948QM 的"100G"冲突确认为 Ewind 官方文档内部矛盾**（标题/介绍写 4×100G vs 规格表 4×10G），并新增"3 年质保"与"轻量 L3"（IPv6 仅 5 条命令、SNMP 仅 v1/v2、无 RMON/TACACS+/堆叠/ISSU）。质保口径三处打架（1 年 / 3 年 / 官网 3–5 年）。

**Angora：官网零改动**（24 页面 + 10 文章的 `date`/`modified` 与 r39 逐条一致），但 **4 份宣传册首次入库**，抓到 5 条实质信息：① Hitit 宣传册 PDF 标题元数据是 **`Kaleiçi_Datasheet_Taslak`（草稿）**，草稿直出官网；② Hitit 是**非网管**且**自带 PoE 看门狗**→ Ewind 的 watchdog 不再独家；③ 长距对位改写为"**Hitit 250 m 不降速 vs Ewind 300 m 需降到 10 Mbps**"；④ Verge 工业册出现**并存编码 `ANW-2023-E8GT`**（48.1 Mpps/56 Gbps/RAM 512 MB/4096 VLAN/512 ACL/G.8032）；⑤ Synapse 订货表把 **24T4X/48T4X/48T6X 三型描述全写成 "8-Port"** → 可作谈判点。新增能力：堆叠 16 台、ISSU、SNMPv3、RMON、TACACS+、WRED、1024 ACL、USGv6 + IPv6 Gold Logo、sFlow/telemetry、4 个 SFP 配套 SKU。

**边界**：`ru.` 连续 3 轮 fetch 失败；其余 17 个语言子域未逐个实测（结论写"实测 2 个，同源推断"）；Alibaba 单品页 302 到图片搜索，价格仅列表卡片；Alibaba 270 SKU 未全抓；FB/LinkedIn/ZoomInfo/YouTube 未访问；证书页无文本；售后/质保页只取 chunk0；Angora 425/428 只取 0–2 分块；全部 PDF 仍无原始二进制落盘。

## §35 · 第 41 轮 — 2026-11-01：土耳其客户「可深入跟进」单客户档案（用户：「哪些可以深入跟进？给我在branch里单独创建一个文件夹…每个客户分别一个 MD」）

新目录 **`08-followup-dossiers-2026-11-01/`**（22 个文件 = 1 个 README + **21 个单客户 MD**，合计 1,302 行）。

**筛选**：从 `111`（145 行）+ 你的 299 行名单 + ISAF 98 家里，按五条标准（有已发生接触 / 有可替换的在用供应链 / 有自有品牌+OEM 诉求 / 有订单级或项目级信号 / 规模足够）选出 21 家，并按**可执行性加权**排序（有现存接触 > 分数高但没接触过）。

**Tier S（本周就动）**：01 Telkolink+GelecekBT（88）· 02 NOVA（86）· 03 Snexus（85）· 04 Cenova（82，官网在卖 E-wind）· 05 CryptoLink（80）· 06 Entegron/LONGLINE（30A/45A）· 07 Sami CEUIK（**500 台订单级**）· 08 Selim Kalaka（**郑州系供应商要去土耳其建厂 → 他正在换源**）。
**Tier A**：09 Okisan（5,000+ 经销）· 10 Optima（**最暖：IFSEC 见过+计划来深圳**）· 11 Karer（老板直联+1,000 库存）· 12 Telemobil（问了交期）· 13 ONSIS（**回头要样品**）· 14 Makros（卡在 DDP）· 15 HAFYA（军项目+防水）· 16 CCTV Depo（2025 新品牌 SECUZI）· 17 Filiz（自有 7/24 报警中心）· 18 Hane（Milesight 土唯一授权）· 19 Öncü（Sec-on 工业）· 20 OPAX（价格锚 $35/120W）· 21 bilimsat（「最近在找」）。

**每个 MD 固定八段**：一句话结论 / 身份卡 / 证据链（带日期+出处+核实等级）/ 为什么现在跟 / 我方打法 / 联系人逐字 / 风险与注意 / 下一步动作+待核问题。

**边界（重要）**：本目录是**案头整编，本轮零新增外部抓取**。所有事实来自 `111`/`112`/`110`/`99-raw/r37-*`，每条标了来源行号；`用户侧事实`（如「CEO 到访过」「外观一般」）与`已独立核实`分开标注；所有报价均为历史口径（含 DDP/关税者需重算）。被剔除的：MFD（西门子红灯）/ Bimel（Cisco 红灯）/ PNetworks·Longline（竞对，转监控）/ PavoTek·Kiracı（战略留档）。


## §36 · 第 42 轮 — 2026-11-01 ≈15:10–15:40 (+0800)：土耳其客户档案**外部核验**（对 5 家做独立抓取，推翻 1 条 / 结案 1 条 / 封顶 1 条）

用户原话：「OK」。即批准 r41 提议的 3 家（04 Cenova / 08 Selim Kalaka / 10 Optima）做真实外部核验；本轮顺手把已抓到的 09 Okisan、11 Karer 一并写入。

**抓取台账（新文件）**：`07-web-crawl-2026-11-01/02-turkey-dossier-verification-2026-11-01.md`（**25 条 URL 逐条存证**，含逐字原文摘录，原始 HTML/PDF 字节未落盘）。

**① 04 Cenova —— 推翻 r41 结论（最重要）**
r41 写「官网在卖 E-wind，dl-end3308pfg 实页」。本轮逐页复核：全站 8 个品牌板块（**Cenova / Dayzip / Wisetech / Dayline / Bawcon / GVD / Tiandy**）**无 E-wind 字样**；`DL-END3308PFG` 是**自有品牌 Dayline** 的工业 PoE 交换机 —— PDF 首页印 `dayline / Industrial Switch`，且 PDF 内嵌标题为 **`Microsoft Word - DL-END3308PFG.docx`**（中文 ODM 的 Word 模板直接改写；`DL-3524PGF` 同样内嵌 `Microsoft Word - 8pfgport.docx`）。PoE 交换机分类 `urunler/network-urunler/poe-switchler` 声称 **16 款**、实渲染 **15 款**，全线自有品牌（DZ-* / DL-* / SWP-*），4 口→27 口。**结论方向不变（仍 Tier S 82 分），打法改向**：从「换掉 E-wind」→「抢 ODM 订单」，主打它没有的 **2.5G 上联 / 802.3bt** 档。
- 附 2 处**它自己的矛盾**（可作专业性筹码，不当武器）：同一型号网页写 `Garanti 2 Yıl`、PDF 写 `Garanti 3 yıl`；Uplink 端口表述网页与 PDF 不一致。
- 附**二级零售价锚点**：`dijiteknoloji.com` 单开 `DL-END3308PFG` 商品页标 **₺23,945.29**，图片直引 cenova `img/upl/` → Dayline 交换机已铺到二级零售，**有真实出货**。
- **死路**：`/sitemap.xml` → 404；站内搜索 `?q=` 路由坏（返回空产品模板）。正确入口 `urunler/<大类>/<子类>`。

**② 10 Optima —— 沙特悬念结案**
`optima.tc` 已 **302 → `optima-engineering.com`**（邮箱域仍 `@optima.tc`）。`/en/contact` 逐字给出**四据点**：Ankara 工厂（Başkent OSB 19.Cadde No:62, Malıköy 06909 Sincan，**+90 312 815 15 00**，fax +90 312 815 12 98）、İstanbul Perpa（+90 212 210 70 00）、**沙特利雅得厂（Al Fowzan Rimash Industrial Zone, Istanbul Street, 2851 Al Mishal Dist., 14328-6950 Riyadh）**、**Optima UAE（Sharjah SAIF Zone, T5-074, 250 m², +971 50 563 5922）**。→ r41「沙特同名第三方待核」**结案：是它自己的厂**。画像升级为 **TR+SA+UAE 三地制造商 = 三套重复采购**。产品范围补 **SCADA 应用 / 车型识别 / 路侧停车 / 交通方案**；首页新闻含 **Intersec Dubai 2026**（中东是主动战场）。
- ⚠ **名称撞车已隔离**：`optimasecurityonline.com` 卖 `OP-SW881 / OP-SW1601I / OP-SW1600G / POE-SW800G / BV-SW2402` 等白牌 PoE，但它是 **Optima Security Systems（Dallas, TX 75229, 2527 Royal Ln Ste 135, +1 972-481-1010）**，与土耳其 Optima **无关**；该站对抓取 **HTTP 500**。**不得把 `OP-SW` 型号当土耳其 Optima 的证据。**

**③ 08 Selim Kalaka —— 验证被结构性封顶（阴性结论本身是结论）**
`"Selim Kalaka" güvenlik` 及企业站/店铺/LinkedIn 检索 → **0 条相关**（命中全是词源学与无关电商）。→ **无公开企业主体**。处理原则写入 dossier：**不补公司名、不补城市**；把「待核」改写成**微信内必问 6 题**（公司全称/城市/角色、现郑州供应商全称与起始年、年量与主力口数、「去土耳其建厂」是官宣还是口头、最痛的是交期还是价格还是认证、土耳其清关认证谁覆盖），答完**逐字回填**。方法论沉淀：人名+目标国语言行业词检索一次，命中 0 条**即结案**，并在档案里显式写「无公开网络面」，防止下一位重做。

**④ 09 Okisan —— 身份复核 + 新增 5 家二级分销**
站点标题自证 `Okisan Güvenlik | Tiandy - Dahua Türkiye Yetkili Distribütörü`；首页 4 大方案（CCTV / Mobil / Akıllı Ev / Yangın），**无自有交换机产品线** → PoE 属「配单件」，与「现用丰润达（用户侧）」相容。最新新闻 **ISAF 2026-İstanbul**（2026-10 图）→ 它刚参展，**展会上堵人优于冷发邮件**。`dagiticilarimiz/` 给出 Tiandy **5 个区域二级分销**（Uğur Güvenlik Ankara 0312 481 90 50 / Ata Global 0532 523 3246 / Tria Antalya 0242 244 00 08 / MST Van 0432 502 00 65 / 3D Bilgisayar Diyarbakır 0850 988 03 03，含邮箱）。**明确写入：这 5 家是 Tiandy 的下游，不是 Okisan 的客户，默认不直接打**（绕过主谈=废掉主谈），只作区域覆盖图与备选。

**⑤ 11 Karer —— 拿到公开 USD 价锚点**
`karerguvenlik.com` 是活的 AKINSOFT 电商，**USD + TL 双标价 + 实时库存**。`KR-ND1P802LFG`（`8*10/100 PoE + 2 Gigabit Uplink，150 W`）= **US$160.00（8.014,40 TL）+KDV**，库存「Son 1 ADET」。同族另有 `KR-ND1PD1621HG`（16 口 + 2×GbE + 1×SFP，250 W）、`KR-ND1PD2412L`（24 口 + 2 SFP）、`PSE-0820G`（"Diğer" 品牌，6 件）。**型号更正**：r41 写的 `KR-S1710GU-AP` 本轮站内**未见**，现行族为 `KR-ND*` → 发信前必须确认，别拿旧型号开场。**结构发现**：它同时卖 **IP/AHD 相机主板、NVR 板、镜头、IRCUT、灯板、空壳、维修工具** → **板级 + 整机级双料商**，懂「模组价 / 整机价 / NRE」三件套，**不能只报整机**。可枚举性：`/sitemap.ashx` → `custom.xml` + **`products_1.xml`**（全站商品 URL，时间戳 2026-11-01）→ 下轮可做完整价格带。

**产物与改动**：新增 1 文件（抓取台账）；改写 5 份 dossier（各追加 `## 核验补录 2026-11-01`，原文八段保留以便对照）；`08-followup-dossiers-2026-11-01/README.md` 新增「**六、2026-11-01 外部核验轮**」状态表并更正 04 行。

**边界（不得越过）**：
- **未核验 16 家**（01/02/03/05/06/07/12/13/14/15/16/17/18/19/20/21）本轮 0 次抓取，**等级不变，不得标为「已验证」**。
- 「Okisan 现用丰润达」仍为**用户侧事实**，未独立核实。
- Optima 年用量、三地是否同一 BOM：均无数据。
- Karer 的 OEM 工厂名：站点不披露，仍未拿到。
- Cenova「16 款 vs 15 款」差 1、`DL-3416PF`/`DL-3524PGF`/`DL-END3308PFG` 是否已从 PoE 分类下架：待核。
- 全部为 `fetch_page` 文本提取，**无原始 HTML/PDF 字节落盘**；`optimasecurityonline.com` 只读到搜索引擎快照。

## §37 · 第 43 轮 — 2026-11-01 ≈16:20–17:35 (+0800)：土耳其 21 家客户「商业深挖」（年报/领英/KP/人事/展会/论坛/GitHub）

用户原话：「你深挖一下这些公司吧 把内容写进MD 深挖：各个角度 年报 领英 KP 人事变动 他们参加的展会 论坛 github 等等 只要是商业角度的都搞一下」。

**做法**：对 `08-followup-dossiers-2026-11-01/` 的 **21 份客户 MD 全部追加 `## 商业深挖 2026-11-01`**（r41 八段 + r42 核验补录原样保留，只增不删）。新增抓取台账 `07-web-crawl-2026-11-01/03-company-deepdig-2026-11-01.md`。

**覆盖 21/21，15 家挖到新事实、6 家公开面为零。**

**① 最重磅：01 Telkolink/GelecekBT —— 它自己就是深圳品牌方**
CLR Networks 官网 contact 页逐字：**总部 `5/F, Hua sheng sheng hui Building, Jian'an first Road, Baoan District, Shenzhen, China, 518101`，`+86 (0) 755 33127842`**；**EMEA 联系人 `yusuf@clrnetworks.com`、Skype `yusufolcer`、web `gelecekbt.com`** —— 与 **GelecekBT 总经理 Yusuf Ölçer** 同一人。→ 这家人**已经跑通「深圳贴牌 + 土耳其独家分销」全链路，且贴牌方在深圳**。打法由「帮你做 OEM」改为「**做 CLR 的第二供应源**」，并提示**它亦是我方潜在竞争者，勿一次性交出 BOM**。另补齐：网站归属主体 **Gelecek Yönetim Merkezi Eğt. Dan. ve Teknoloji Hiz. İth. İhr. San. Tic. Ltd. Şti.**、**2004-10-13 成立**、两个 Perpa 门牌（Telkolink **A K:5 No:295-297**；GelecekBT **A K:13 No:1990**）、代理条线含 **3onedata / TG-NET / Fibridge / Repotec / IMC / CLR / ONET / Allied Telesis / HP / Cisco**（即：交换机品类它已压 4 条中国线）。

**② 10 Optima —— 公开商业信息最完整的一家**
**2014** 获经济部区域激励补助购 **Başkent OSB 9,000 m²** 工业用地、**2015 年夏**建成投产；**NACE 28.99.90**；**ISO 9001:2008**；⭐ **出口 >90% 产量、50 多个国家**；结构化 `areaServed` 16 国（含沙特/UAE/卡塔尔/埃及/阿曼/约旦/阿塞拜疆/乌克兰/阿尔及利亚/**蒙古**/摩洛哥/利比亚/俄罗斯/西班牙/法国）；领英 **2,987 关注**，原话「**As Optima and Ulgen, we have been exhibiting consistently and consecutively at Dubai Intersec for 20 years**… rewarded by **Messe Frankfurt**」；**Intersec Dubai 2026（1/12–14）**、**Intertraffic Amsterdam 2026 首秀**、OKSİAD 2025；下一场 **Intersec Global 2027（1/12–14）**。新增待核实体 **Ulgen**。

**③ 19 Öncü —— 本轮唯一"海关提单级"证据**
集团站 `oncu-group.com` 六实体：**ISSD / Neotech Technology A.Ş. / Oncu Security（代理 HIKVISION·COFEM·DAVANTIS·SEC-ON）/ Sec-on Co. Ltd. / Secube**；Öncü **2002** 成立，Sec-on **2012（公司列表）vs 2016（时间线）自相矛盾**。**Volza 提单：128 批 / 2 家供应商 / 主源 China / HSN 8525·8521·8531 / 供应商 `SEC ON CO LTD`（中国）+ `Tamron Europe GmbH` / 单票「video recorder」150 UNT**。→ **它的"自有品牌"是向 `Sec On Co Ltd` 买的整机**，**供应链高度集中（仅 2 家）**= 我方破口。话术红线：**绝不能说"我们知道你的供应商是谁"**。

**④ 06 Longline/Entegron —— 合同主体可能不在土耳其**
`Entegron Technology FZE`（**阿联酋自贸区实体**）在土耳其提单里作为**出口方/供应商**出现（如 Fons Information Technology Ltd 进口 `1 GE SFP SLOT + 1 10/100/1000M MODULE`）。Longline 五站矩阵（longlinestore / longlinesfp / **longlifesfp**（双 SFP 品牌）/ longlinenetwork / endustriyeltestcihazlari）、**Romania+China+Dubai+USA+欧洲**合作、**TR+RO 双仓当日发货**、**ATR/TAREKS/GTIP** 报关能力、**800+ 伙伴**；办公 **Longline Plaza Bayrampaşa**； LinkedIn **3,979 / 28 人**，第三方营收 **$10.7M（Datanyze）/ $15M（RocketReach）**；⭐ **KP：Safa Özer（Purchase Manager）、Ercan Çiçekci（董事）**；⚠ **全系仅 1 年保修**（我方 3 年即可量化取胜）。

**⑤ 16 CCTV Depo —— CEO 公开自述"深圳我熟"**
领英个人简介原文：*"2000 Yılından beri Güvenlik Sektöründeyim. **Çin, özellikle Shenzhen'i çok iyi biliyorum**"*。更正 r41 两处：**HQ = Bahçelievler**（非 Şişli-Perpa）、**Can Gurcan 企业页标 CEO / ZoomInfo 标 CTO**（两处冲突）。成立 2004、51–200 人、领英仅 239 关注、WHOIS 2004-07-21 持有人 Can Gürcan、品牌 SECUZI（Mehmet Furkan Beklin）。

**⑥ 18 Han Elektronik —— 有独立 OEM 事业部的品牌运营商**
官网 MARKALAR 全列：**MILESIGHT（土唯一授权，2023 最有价值伙伴奖）/ FOREDGE（网络与云，有分销证书）/ VIDEOPARK / SPY·SPY AHD·SPY IP·SPY MOBİLE·SPY ALARM / GRUNDIG / PANASONIC / AXXON / AVERDIGI·AVERFIRE·AVERGUARD·AVERCLOUD / SHELLY / ALIENFENCE / UNIWIZ / NEVIO / HOOP CAM / TNA / Rujie(Reyee)**，且**菜单里直接有 "OEM - SPY MOBİLE" 分类**；**Han Elektronik A.Ş.**、2000 成立、51–200 人、`444 1 426`、fax 0212 220 82 79、Küçükçekmece Basın Ekspres Yolu；运营 `milesight.com.tr` 与 IG `@milesight_tr`。⚠ **决策人姓名仍为空白（最大缺口）**。

**⑦ 其余 14 家的新增要点**
- **02 NOVA/Novacom**：品牌 **Novacom（NVC-）**，三域（nova-grup.com / novacom.com.tr / 第三方 **pekgross.com** 转售）；⭐ **24V 楼宇对讲（diafon）PoE** 两款 `NVC-INTSF0420FB2L`(4+2)/`NVC-INTSF0820FB2L`(8+2)，**规格表极简**=我方升级空间；另有 PoE 延长器、CCTV 测试仪（SKU 10594/10884/10885）。
- **03 Snexus**：**2020 成立**、11–50 人、Çekmeköy；⭐ **新加坡据点 Sim Lim Square（Rochor Canal Rd 02-67）**；具名分销商 **HEMMAH GROUP**；⚠ 名称污染（巴基斯坦外包公司 / 美国存储软件同名）。
- **04 Cenova**：法定名 **CENOVA BİLİŞİM TEKNOLOJİLERİ İTH. İHR. VE TİC. LTD. ŞTİ.**、**2002 成立**、自述"主要与远东和欧洲知名公司合作"；客户=**市政/大学/军/医院/工厂**、给经销商账期；人员 Abdurrahman Erkarslan、Necla Güler（会计）。
- **05 CryptoLink**：站点自证六业务（边境/网络/网安/LPR/在线培训/**信号干扰**）；⚠ **法定名 A.Ş. 与 Ltd. Şti. 站点自相矛盾**；是 `itmteknoloji.com.tr` **解决方案伙伴**；⚠ 与 **CryptoLink Inc(US)**、**Cryptex(Ankara)** 同名 → 勿混。
- **09 Okisan**：**48–49 人 / 5,318 关注 / 行业分类=İthalat ve İhracat（进出口）/ Ortaklık**；⚠ **成立年三个数字**：官网 1986、领英 1993、2004 转 A.Ş.（对外统一用 1986+2004）；⭐ **Okan Özkara（Business Development Director，2010–，同姓=家族）**、**Kerem Öztürk（Ankara Bölge Müdürü，2001–，24 年）**、Ekrem Özkara(CEO)、Gökhan Özkara(外贸)。
- **11 Karer**：⭐ **PESİAD 会员**；法定名 **Karer Güvenlik Sistemleri Sanayi ve Ticaret Ltd. Şti.**、**2006 成立**、**1,000 m² kapalı alan**、新座机 **0216 397 33 88**；Nurbaki Karataş（CEO/owner，Akdeniz Üniv.）、Ebru Tekin（会计 2021–）、Neslihan Entrk（销售）→「1,000 m² + 板级生意」= **具备本地组装条件，推"模组+技术转移"**。
- **12 Telemobil**：法定名 **Telemobil Bilgi İletişim Hizmetleri San. ve Tic. A.Ş.**、**90 年代为 A.B GRUP 的 IT 部门 → 2005 独立 A.Ş.**、Üsküdar Küçükçamlıca、**97（LinkedIn）/120（ZoomInfo）人**、第三方估营收 **≈$25.6M**；业务 = **IT 系统集成 + 电气承包（Elektrik Taahhüt）+ 楼宇自动化/弱电**；客户 教育/医疗/建筑/**数据中心**；KP Murat Gül（Proje Grup Direktör Yrd.）、Mehmet Emre Güney、Aydın Akkoyun。→ **投标支持 > 降价**。
- **17 Filiz Güvenlik**：⭐ 护城河 = **须经内政部许可的 7/24 报警监控中心（merkezi alarm istasyonu）**，订阅制；官网有 **`Çözüm Ortaklığı`（合作伙伴）表单** = 现成正式入口；⚠ **Ltd. Şti. vs A.Ş. 冲突**；Mavili Yangın İzmir 授权服务；FB/YouTube/领英（**个人页形式**的企业号）。
- **20 OPAX**：法定名**逐字核实**（…**İthalat İhracat Dış Ticaret Pazarlama Limited Şirketi**）；地址 No:3/1 Opax Plaza；**`satis@opax.com` + 新增 `sezer@opax.com`**（Google Play 开发者信息）；自有 App **OPAX Pro**（`com.opax.opaxalarmpro`）→ 有云/移动端能力；**$35/120W 是引流款**，机会在 802.3bt/24 口/宽温；`Damian Brozda(.pl)` **仍无法定论**。
- **07 Sami CEUIK**：公开面 0；⚠ **`CEUIK` 疑为 `ÇEVİK` 的录入变体** → 需名片校正；维持"订单级"优先级（500 台 > 公开资料丰富度）。
- **08 Selim Kalaka**：六角度全空；固化结论 = **窗口信息只存在于展会对话，外部无法证实也无法推翻 → 外部检索到此为止**。
- **13 ONSIS / 15 HAFYA / 21 bilimsat**：公开面 0（ONSIS 仅知区号 0232=İzmir；HAFYA 军项目本色；bilimsat ⚠ **"Gmail=个人经营"判断不成立**）。
- **14 Makros**：⚠ **名字撞车**（`makrosinsaat.com` 建筑 / `macromuhendislik.com` 弱电工程 2013 / Makro İnşaat）→ **r41 的"Makros A.Ş."在公开网络无对应实体，先核主体再谈生意**。

**⑧ 两个可复用方法论（写进台账，后续直接用）**
1. **海关提单反查**：用**法定全名**在 Volza/ImportGenius/Panjiva 查 → 供应商名 + 批次数 + HS 编码 + 单票数量。边界：只覆盖报关部分；**话术上绝不能说"我们知道你的供应商是谁"**。
2. **行业协会会员名录**：**PESİAD（安防）/ SAHA İstanbul（国防）/ TÜBİSAD** 常登记法定名+成立年+面积+电话 → 本轮靠 PESİAD 一次拿全 Karer 硬信息。
- 另附市场规模（Volza 品类口径）：**土耳其自中国进口 Ethernet Switch 4,061 批次 / 509 家买家**；全球「Access Switch」进口中土耳其占 **13%（599 批）排第 3**。→ 土耳其是**成熟替换市场**，胜负手在换存量供应商，不在开荒。

**边界（必须保留的诚实口径）**
- **年报/财报：0 家**。土耳其私营 Ltd./A.Ş. 不公开年报，档案内营收**全部为第三方推算**（Datanyze/RocketReach/ZoomInfo），已逐条标注"非财报"。
- **GitHub/论坛：0 家**，且是**"确认无"**（白牌固件生态），非遗漏。
- **政府招标（EKAP）未接入、TÜRKPATENT 商标未查、Ticaret Sicil Gazetesi 股权未查**（付费/交互查询）→ 列为下轮。
- 全部为 `fetch_page` / `web_search` 的**文本提取**，无原始 HTML 落盘；第三方数据库（Lusha/ZoomInfo/RocketReach/Datanyze/Volza）数据**存在滞后与推算误差**，引用时保留"第三方"限定。

## §38 · 第 44 轮 — 2026-11-01 ≈18:10–18:55 (+0800)：新建仓库根目录 `TR Customers/`（一客户一 MD，146 份）

用户原话：「仓库里是有一批土耳其看户吧 弄成MD给我吧 单独建立一个文件夹 就叫TR Customers 里边每个客户分别一个MD 里边是客户的信息 调研等」。

**做法**：不新抓任何外部数据，**纯结构化重整**：把权威管线 `111-turkey-customer-pipeline.csv`（**145 行 × 17 列**）**一行一个 MD**，外加 1 份 `111` 里没有的客户（Entegron／LONGLINE），共 **146 个客户 MD + 1 个 README = 147 个文件，10,901 行，792 KB**。生成脚本 `08-customer-pipeline/build_tr_customers_r44.py`（可复现，重跑即重建）。

**每个客户 MD 固定七段**：① 身份卡（公司/层级/总部·城市/场景/自有品牌/名单来源/源表位）② 我方核实的交换机产品线 ③ 当前供应链（核实口径）④ 联系人（`代码块` 逐字，防改格式）⑤ 证据与核实等级（证据来源 + 核验日期 + 双 AI 初筛 + 我方评估，并注明「联系人=用户侧，证据=我方独立抓取」）⑥ 建议动作 ⑦ 备注。

**21 家「自包含」**：凡在 `08-followup-dossiers-2026-11-01/` 有深度档案的（01 Telkolink/02 NOVA/03 Snexus/04 Cenova/05 CryptoLink/07 Karer/08 Hane/09 Öncü/10 Optima/11 …），把档案**全文逐字并入**文末「附：完整研究档案（逐字并入，未删改）」，含 r41 八段 + r42 核验补录 + r43 商业深挖。→ **不用在文件夹之间来回跳**；同时原档案文件**一个字节都没动**（只读引用）。

**序号映射（111 序号 → 档案）**：1→01、2→02、3→03、4→04、5→05、7→11、8→18、9→19、20→20、21→16、56→10、57→17、58→09、80→12、81→14、82→15、84→13、86→21、91→07、92→08。

**★ 遵守「不合并」**：`111` 里同一家公司在两批名单各录一次的有 **21 组**（Makros #26/#81、Telemobil #46/#80、HAFYA #25/#82、SFPTURKEY #24/#83、Hiperonline #28/#145、DE Secure #29/#89、ORAL #30/#88、F.A.S.T #31/#95、Fiberix #32/#102、HCS #33/#93、Antalya Turkuaz #35/#121、Fourline #38/#113、MEPA #39/#98、AG Bilgisayar #40/#114、FH Güvenlik #41/#116、Bilgen #42/#117、Düzgün Toptan #43/#104、Proves #44/#100、Pelikan #47/#138、Zeytek #49/#136、Foline #50/#142、Nazemco #51/#126 —— 按短名/整串包含算法自动识别）。**一律各自独立成文件**，文件顶部 ⚠ 标注「疑与 #NNN 同一家」，README 第五节列出全部 21 组对照表，**合不合并留给人判断**。

**诚实边界（写进 README 第二节）**：
- **覆盖 = 111 的 145 行全覆盖**；用户的两批原始名单（299 行 xlsx + ISAF 98）**已折进这 145 行**（见 `112`），所以不是 397 家，而是**去重后 145 家**。
- **深度差异**：21 家有深度档案；**其余 124 家只有管线字段**，README 明确写「**不要把 124 家当成已调研，它们只是有档案**」。
- 联系人全部来自用户侧；报价均为历史口径；第三方（Datanyze/ZoomInfo/RocketReach/Volza）数字为推算非财报。
- `146 Entegron／LONGLINE` 标注「**不在 111 管线里**」，来源 `06-competitors/110` 第 20 行 + 原始名单 #44，并提示它**同时是我方竞对**。

**README 内容**：文件清单与权威源、怎么读（三件事）、诚实边界表、**146 行全索引表**（#/客户/城市/层级/评分/是否有深度档案/文件链接）、建议阅读顺序（A 级 6 家 → 订单级·窗口级 3 家 → B/C 124 家扫「建议动作」列）、**21 组重复对对照表**、相关目录、生成脚本路径。

**仓库根 `README.md`** 的「入口」列表最上方加了 `TR Customers/` 指针。

## §39 · 第 45 轮 — 2026-11-01 ≈19:20–19:45 (+0800)：`TR Customers/` 按 A/B/C 三档分目录

用户原话：「我记得是有一些不错的 一些普通的吧 分为ABC3类吧 就是在这个文件夹下分别建ABC文件夹 往里塞MD」。

**做法**：不新增内容、不重打印象分——**分档直接沿用 `111` 管线 `层级` 列的首字母**（该列本身 = 双 AI 初筛 + 我方人工核实 + 综合评分，详见 `112`）。改 `build_tr_customers_r44.py` 输出目录，重跑即重建。

**结构**（`TR Customers/`）：
- `A/` **33 份** —— 优先跟进（`A 核心` / `A-` / `A 订单级` / `A 军项目` / `A 战略` / `A 暖线` / `A 大型分销`）
- `B/` **77 份** —— 常规维护（`B+` / `B` / `B-` / `B 暖线` / `B bypass` / `B 防务客户池`）
- `C/` **36 份** —— 备选池（`C` / `C+` / `C 战略留档` / `C 不跟进` / `C 低`）
- 根部 1 个 `README.md`（索引已按三档拆成三张表，链接改为 `A/xxx.md` 形式）
- 合计 **146 份客户 MD + README = 147 文件 / 10,932 行**

**三处细节**：
1. 深度档案（21 份）分布：**A 15 份 / B 6 份 / C 0 份** → 说明"有深度档案"与"档位"高度相关，但 **B 里那 6 家（Karer #7、Hane #8、Öncü #9、Filiz #57、Makros #26 …）反而可能是"被低估"的候选**，值得单独看一眼。
2. `C/` 里混着两种完全不同的东西：**`C 战略留档`（PavoTek #59、Kiracı #73）与 `C 不跟进`（MFD #61、Bimel #76）**——已在 README 第三节明确标注「性质不同，看备注」。
3. **跨批次分档不一致已标出**：同一家公司在两批名单里可能落进不同档（`Makros` #26 = `B+` 落 `B/`，但 #81 = `A 工程` 落 `A/`），**两份各归各档、不合并**，README 第三节写明「请自行裁决以哪份为准」。

**脚本可复现**：重跑会先清掉根目录旧版平铺 MD（v1 遗留），再按档重建 → 本次清理 146 个旧文件。**再次强调：`08-followup-dossiers-2026-11-01/` 原件零改动。**

## §40 · 第 46 轮 — 2026-11-01 ≈19:50–21:10 (+0800)：B 档 77 家逐家深挖

用户原话：「A类OK B类继续深挖 C类就是不跟进的了 没那么多精力 你看看ABC需要再重新处理一下吗」+「搞完深挖B类客户 A类似乎已经挖完了」。

**决策（先回答"要不要重新处理 ABC"）**：**不再重新分档**。
- **A 33 家不重挖** —— 它已是文档最厚的一档（15/33 有完整研究档案），再挖的边际收益最低。
- **C 36 家零投入** —— 用户明确"没那么多精力"；`C 战略留档` 与 `C 不跟进` 的区分**在实操中取消**（README 里的标注保留，但不再分配时间）。
- **全部预算给 B 的 77 家** —— 这也回答了用户的第一层疑问：B 不是"次等客户"，是**没被认真看过的一档**。

**产出**
- `TR Customers/B/*.md` **77/77** 每家文末追加 `## 附：B 档深挖（r46 · 2026-11-01）`，结构固定五节：**一句话 → 主体与坐标（表）→ 它在卖什么／与我方的切入点 → 打法（含首封主题模板）→ 证据等级与空白**。
- 横向总表 **`08-customer-pipeline/115-turkey-b-tier-deepdig-2026-11-01.md`**：77 家分五类（**已在卖交换机 11 / 相邻品类 17 / 工程商集成商 22 / 结构错配 10 / 重复登记**），另含"需人工拍板三件事"、"方法与证据纪律"、"下一步"。
- `TR Customers/README.md` 新增**第九节「B 档深挖（r46）」**（原第九节顺延为第十节）。
- 目录规模：**10,932 行 → 13,182 行（+2,250 行）**；文件数不变（146 客户 MD + README）。

**⭐ 三条改变打法的发现**

1. **B 档被严重低估：11 家已经在卖交换机，其中 6 家有自有/白牌型号。**
   - `6 Coptek`（**Koptek Bilgisayar**）产品目录 = Omurga/DC/PoE/L3/L2/工业/SFP，型号 **`S4600-28X-SI`**（24GE+4×10G）——**通篇只有规格没有品牌名 = 白牌**。
   - `14 NFS`（NFS Teknoloji）**Surenix `SRX-*` 全梯子**：`SRX-GS24PP+` / `SRX-10GS24PX-L3`（24GE+4×10G L3）/ `SRX-IGS·IMS` 工业线 / `ONSW-IMS8PP`。
   - `62 Cebeci`（Cebeci Teleteks）在售 **`S5700-24G-4FR` / `S5700-24G-4TFR`**（L3 网管，24GE+4×10G），页面同样无品牌名。
   - `18 iotsistem` 自有 **`MLB-E4xxx`** 工业线（5/10/14/**28 口**，E4204-28-G-F 机架式 + DC 备份）。
   - `79 Eurocam` **代理 Ruijie（锐捷）** + 自有 Eurocam/Europer/Eurolink 三品牌 + **500+ 经销商**。
   - `10 ErETE` **XPS 工业交换机，标注 EGM onaylı（警察总局认证）** + XPCABLE 布线（Cat6 终身系统保证）+ 台湾/伊斯坦布尔双据点。
   - 另有 `15 Koza`（PoE 分类 + **自设进口部**）、`19 Lansan`（A.Ş. 2019-12-04，自称配线架制造商）、`33 HCS`（A.Ş. 2000-11-22，布线批发无有源）、`35 Antalya Turkuaz`（TP-Link/Omada/VIGI + Dahua + Teknim）、`49 Zeytek`（MOBESE 柜 + Network 品类，总经理履历含 **Legrand/Asrack**）。
   → **这 11 家的谈法不是"教育客户"，是"型号对位 + 二供/贴牌"**。

2. **10 家是"结构错配"，不是"资料不足"——建议降档（本轮只提建议，未改 `111`）。**
   - `34 Stasanet` = **Stasanet d.o.o.（塞尔维亚贝尔格莱德）**，Jablotron 官方进口商 → 根本不是土耳其公司。
   - `28 Hiperonline` = **ISP**；`32/102 Fiberix` = **ISP**，且有 **ASN 185.207.56.0/22**（BGP 一锤定音）。
   - `43/104 Düzgün Toptan / teksarf` = **纺织辅料 B2B**，与弱电无关。
   - `71 Baburtech` = **笔电原厂备件 + 5,000 m² 主板级维修**，无网络品类。
   - `55 ULAK Haberleşme` = **国家级设备商**（SSB 参股 + Aselsan 主承包，国产 4.5G 基站、Netaş 2025-07 战略合作）→ **是情报源不是客户**。
   - 改市场标签：`30 ORAL` = **KKTC 北塞**（1982 Oral Companies，董事 Metin Oral，在用 Height Vision + Arma Kontrol）；`45 Alamthal` = **利比亚市场**（`alamthal.ly` + 伊斯坦布尔 İncirtepe 采购办，CTO Nayl Alielah / GM Khalid Kraizim）。

3. **新挖到的高价值"补位"关系（不是替代，是缺口）。**
   - `60 GMT Control (GMTCNT)` —— 土耳其**第一家国产 PLC 制造商**（2014，Beykoz，51–200 人），有 PLC/HMI/变频/伺服但**没有以太网交换机** → **PLC 柜内 DIN 导rail 交换机**是纯补位。
   - `50 Foline` —— 数据中心/集装箱 DC/结构化布线（Siemens/CommScope 伙伴），**写 şartname 的角色** → 目标是**进它的招标规格**，不是卖货。
   - `67 Metcom A.Ş.` —— 自研 **MTC-500 高速公路车牌识别**，杆上设备 → **户外 PoE（IP66/6kV/−40~75°C）进 BOM**。
   - `73 Kiracı Bilişim / ZKR` —— 医院 IP 护理呼叫（700+ 套，Ankara Çankaya）→ **一个 500 床医院 ≈ 1,000 个 PoE 口**，要**长距 + 无风扇**。
   - `29 Desecure` —— **1,400+ 人 / 9 据点**，自研 **MIA 移动监控车 / MID 移动监控杆 / MAS 移动报警台** → **DC 宽压工业 PoE**，参展是能源展（Solar Storage İstanbul、TÜREK）不是安防展。
   - `63 Areskom` —— Westermo/Moxa/Belden/Tektelic 级工业通信分销 → **只切"边缘/分支"，绝不碰核心环网**。
   - `48 Bilge Güvenlik`（Axis/Milestone/Hikvision + Honeywell）、`13 Rima`（**Digifort VMS 土耳其**）、`12 CCS`（2016-03-28 注册，自述伊兹密尔最大，2018 进伊斯坦布尔）。

**这 77 家里必须点名的三条"省钱建议"**
- `27 ONSİS` **不要再做调研** —— ISAF 2025 最后一天回展台要样品（没带现金）＝行为信号全场最强，**直接进样品 + 阶梯报价**。而公开网络面为零（两轮检索确认）。
- `45 Alamthal` / `126 Nazemco` / `51 Nazemco` —— 都是**"伊斯坦布尔采购 + 转口"**模式，谈 **FOB İstanbul**，不谈土耳其本地账期。
- `46/100/102/116/117` 是重复登记档 → **只联系一次**（两家销售同时发信在土耳其买家眼里非常掉分）。

**方法（本轮新增，可复用）**
1. **查型号，不查公司名** —— 四个最大突破（Coptek/NFS/Cebeci/iotsistem）全部来自官网的**具体型号页**；`S4600`/`S5700` 属"深圳通用型号族"，**"只有规格没有品牌名"本身就是白牌证据**。
2. **ASN/BGP 判 ISP vs 分销商** —— Fiberix 的 `185.207.56.0/22` 直接定性；比看官网文案可靠。
3. **企业登记站取注册日/公司类型** —— CCS `2016-03-28`、İnovatech `2014-08-21`、Lansan `2019-12-04`（**A.Ş. 多股东**）、HCS `2000-11-22`（A.Ş.）、Egemen `2013-07-25`。
4. **顶级域/公司后缀判市场** —— `.ly`（利比亚）、`d.o.o.`（塞尔维亚）；这一条直接纠正了三家的国别。
5. **"品类页有分类但无产品/无品牌" = 缺口信号**（Koza 的 PoE、Zeytek 的 Network、HCS 的有源）。

**诚实边界**
- 77 家中：**约 12 家关键事实有 ≥2 个独立来源**（Coptek/Cebeci/iotsistem 的型号页虽只有官网一个来源，但型号本身可交叉对位中国厂规格）；**约 25 家仅官网单一来源**；**约 10 家公开面为零**（`101/103/105/106/123/128/130/36/40/114`）→ 一律写「**主体未确认 + 一次通话建档**」，**不给假信息**。
- **所有营收/人数均为第三方估算**（ZoomInfo/EMIS/Tracxn/RocketReach/ContactOut），已在每家档案里标 ⚠。
- **本轮未改任何 `层级` 字段**；升 A/降 C/改市场**全部只是建议**，`111` 仍是唯一权威。

**脚本与可复现**
- 新增 `b_deepdig_data_1.py`（#6–30）/ `b_deepdig_data_2.py`（#31–130）/ 一次性注入器 `build_b_deepdig_r46.py`。
- **`build_tr_customers_r44.py` 已内置"B 深挖数据注入"**（读取上面两个数据模块，仅对 `letter=='B'` 且有序号的档追加）→ **重跑脚本不会丢掉 r46 内容**，也不会污染 A/C。
- `08-followup-dossiers-2026-11-01/` **原件零改动**（本轮只读）。

## §41 · 第 47 轮 — 2026-11-01 ≈21:15–22:30 (+0800)：A 档补齐 + B/A 型号对位表

用户原话：「继续挖 那照你的思路来搞 反正就是把AB挖的越深越好 不要管C」。

**范围决定**：只做 **A + B**，**C 36 家继续零投入**。A 档上一轮（r46）按用户「A 类似乎已经挖完了」的判断跳过了——本轮补上：**A/ 里此前只有 `111` 管线字段、没有完整档案的 17 家，全部逐家深挖**。

### 一、A 档补齐（17 家）

`A/` 33 家的结构现在是：**15 家原有完整研究档案（r41–r43）+ 1 家 Entegron 专档 + 17 家 r47 新深挖 = 33/33 全部有深度内容。**

17 家 = `052 053 054 072 075 083 085 087 089 090 093 094 095 096 097 098 099`，其中 5 家是 r44/r45 的跨批次重复档（`083`=#24 SFP Turkey、`089`=#29 DE Secure、`093`=#33 HCS、`095`=#31 F.A.S.T.、`098`=#39 MEPA）——按"不合并"原则**各自保留文件、内容指向首次深挖的那一份**。

**⭐ 三个高价值发现（本轮最大收获）**

1. **`052 Uptech / Nokta Elektronik` —— A 档最优先的 OEM 目标。**
   - **upTech 是 Nokta Elektronik ve Bilişim Sistemleri A.Ş. 的自有品牌**：土耳其专利商标局注册号 **2008/13951**，**2008-03-11 首次注册，续展至 2028**。
   - **916 个 SKU**，覆盖**以太网交换机与 PoE 交换机**、SFP/SFP+、媒体转换器、跳线、连接器、HDMI 转换器、测线仪；**保修与技术支持由 Nokta 自己承担**。
   - 同时是 **Dahua、Ruijie Networks、Edge-Core、Planet、ORing、Amphenol、Gewiss、Goldtool、Noyafa、ATC** 的分销商。
   - 登记信息：**MERSİS 0631-0730-5210-0020**、**Tic. Sicil No 555138-0**、Perpa、**0212 222 87 80**、`nokta@noktaelektronik.net`、**25 年+**。
   - 市场：土耳其 + **中东、突厥语共和国、巴尔干**。
   - → **它代理 Edge-Core（开放网络厂牌）、能贴牌、能转口、有 916 SKU 的自有品牌** = 三条通道同时成立。**这是全项目里最优先的一封邮件。**

2. **`053 Winet` —— 全项目唯一可引用的土耳其零售价锚点。**
   - `wi.com.tr` 把价格印在页面上；型号前缀直接用 **`OEM-`**（**`OEM-8-PORT-GB-POE`**），即它自己就承认是贴牌线。
   - **`OEM-8-PORT-GB-POE`（WINET 8 口千兆 PoE，7×PoE 24/48 V + 1 上行）= 2,916.76 ₺ + KDV（未税）**。
   - 该型号**只有 24/48 V 手动、无 af/at 自动协商、无 bt、无长距** → 我方 `EW-S1710FG-AP`（af/at）与 `EW-S1810CF-AP`（af/at/bt 60 W + 300 m + PoE Watchdog）是**三档升级**。
   - 同页另有 `WINET-ANT-LTE-12DB` **1,956.56 ₺（含税）**、`WINET-TSFR-1` 技术支持包 **3,467.28 ₺ + KDV**。

3. **`075 Technopc` —— 最大 OEM 机会。**
   - **1998 创业 / 2006 自建厂**，**27,500 m² 制造基地 + 研发设计中心**，**250+ 人**。
   - **全土耳其第一张「国产货证书（Yerli Malı Belgesi）」的电脑制造商** + GreenPC 认证。
   - **SAHA İstanbul（国防航空集群）+ Ostim Savunma（安卡拉国防集群）双会员**；客户 = **政府、国防组织、关键基础设施、企业数字化**。
   - 产品：台式机、笔记本、**工业电脑**、服务器、**数据存储**、**AI 基础设施**、定制硬件平台。
   - → **工控机/服务器/存储的「柜内交换 + ToR」是它天然的缺口**（我方 `EW-PIS*` 工业线 + `EW-S53928QM` 24×10G+4×100G + `EW-S5954GM-AP` L3+）。
   - ⚠ **谈法纪律**：它的核心叙事是"国产化"，**不要拿"中国工厂"当卖点**，要落在**本地交付 / 本地保修 / 贴 technopc 牌**上。

**其余 14 家的要点**（详见各档案）：`054 TekniksatGroup`（1992，制造实体 **RFT Teknoloji A.Ş.**，自有 **Teknoline**，官网有 **NETWORK ÜRÜNLERİ** 分类，444 40 91）；`072 Lemax`（2009，零售套装商，出口阿塞拜疆/KKTC/格鲁吉亚，**建议降 C**）；`090 Cansıs Teknoloji`（Konya Çumra，老板 **Ahmet Can**，**Armiya Teknoloji 的 Çumra bayisi**，**ASKON Konya 会员**登记号 4474226 → 真正该打的是 **Armiya**）；`094 Klasnet`（Bursa Nilüfer，**2021 起业**，团队 14 年，**站点被注入垃圾内容** → 只能电话）；`096 Voltech`（⚠ **两个不同主体**：Silivri 小店 vs 迪拜 **VOLTECH L.L.C** + Perpa B Blok）；`097 Labor Mühendislik`（**Diyarbakır**，弱证据）；`099 Viva Bilgisayar`（**Hatay**，**İsmet Yavuz**，**Hikvision Hatay Silver Partner**，**震后重建市场**；另有同名伊斯坦布尔 Şişli 电脑批发商 0212 216 90 11）；`085/087` 与 `083/089/093/095/098` 见上。

### 二、`116-b-a-model-mapping-2026-11-01.md`（新品）

把 **11 家 B + 8 家 A** 的**在售型号逐条对位到我方型号**：

- **缺口矩阵（谈判空间只有这 6 行）**：`2.5G 电口` / `802.3bt 60–90 W` / `250–300 m 长距 PoE` / `云管理·AI PoE` / `工业宽温+DC 宽压` / `40–100G 上联`。
  → **11 家客户的产品线全部停在「GE + 10G 上联」**；这 6 行是我方唯一的结构性差异，**同规格比价只在第 1 行用**。
- **逐家对位表**：Coptek（`S4600-28X-SI` → `EW-S2928GM`）、NFS（`SRX-4GS24PP+` / `SRX-10GS24PX-L3` → `EW-S2926GM-AP` / `EW-S5748GM-AP`）、Cebeci（`S5700-24G-4FR` / `-4TFR` → `EW-S2928GM`）、iotsistem（`MLB-E410x/E420x` → `EW-PIS3610M/PIS5728GM-AP`）、ErETE（`XPS-I7120-*` / `XPS-I8120-16` → `EW-PIS1810/5712M-8GE`）、Eurocam（Ruijie 经济层）、Koza、Lansan（SKD 本地组装）、HCS、Antalya Turkuaz（⚠ 不打 Omada）、Zeytek（MOBESE 柜内）、Nokta（upTech 全线）、Winet（OEM-8 三档升级）、Tekniksat（Teknoline 牌）、Technopc（工控机+ToR）、Viva（震后重建）、Cansıs（→ Armiya）。
- **纪律写进文档**：`EtherWAN` 是 ErETE 的长期代理 → **永不贬低**，只谈经济层；`Ruijie/Omada` 有云生态 → **不正面打云战**；`SRX-GS24PMX` 模块化机型**我方没有 → 照实写缺**。

### 三、两处修正（对 r46 的自我更正）

1. **`#62 Cebeci` 的品牌归属判错了一半**：r46 说 `S5700` 是"白牌贴 Cebeci 的牌"；r47 抓首页后确认它的**真实品牌宇宙是电信测试与 FTTx**（代理 **Argus、Cifocs、CMG、Greenlee-Tempo、InterCoax、Micos、Trend Networks**），工业交换机与光转换器挂的是 **`Cifocs`** 品牌（分类首图 = **`Cifocs CFC-4G2SFP-IPS`**）。
   → **`S5700` 是电商挂品（大概率代发/白牌），不是它的自有线；真正该谈 OEM 的是 `Cifocs` 线。** 顺带补齐：**Halil Rıfat Paşa Mah. Yüzer Havuz Sok. No:8 D:24, Okmeydanı / İstanbul 34384**、**0212 320 08 88 / 320 08 85**、`iletisim@cebecigrup.com`。

2. **`#10 ErETE` 应从 B 改判 A**：抓到 `erete.com.tr` 完整分类后，发现它**不只卖 XPS**——有独立的 **`OPEN NETWORKING`** 与 **`NOS（Network Operating System）`** 分类，代理 **IP Infusion**（开放网络 NOS）与 **EtherWAN**（台湾加固工业交换机）、**LANDE**（布线）；
   自有 **XPS** 全型号：`XPS-I7120-6/-10/-14/-16/-24`（非 PoE）、**`XPS-I7120-6P/-10P/-14P/-16P`（PoE）**、**`XPS-I8120-16`（12×GE + 4×10G SFP+，L2+）**、`XPS-I8120-24F`（12×GE + 8×SFP）；
   EtherWAN 线：`EX89000 / EX87000 / EX77000 / EX83000 / EX61000A / EX70900 / EX72000 / ECS4660-28F` + 加固 PoE `ER59000 / ER58000` + `EX75000 / EX76000 / EX78000 / EX78602 / EX74000 / EX46100 / EX48000`。
   → **它是 B 档里唯一具备「白盒 + 第三方 NOS」能力的客户**，与 Angora 的产品域正面重叠。**建议升 A，并列入第一批要打的 3 家。**

### 四、产出与规模

- `TR Customers/A/*.md`：**17 家**新增「附：A 档深挖（r47 · 2026-11-01）」。
- `TR Customers/B/*.md`：77 家的 r46 小节**原样保留**（脚本重跑后自动重建，内容不丢）。
- 新建 `08-customer-pipeline/116-b-a-model-mapping-2026-11-01.md`；`115` 追加 §九 修正。
- `TR Customers/README.md` 第九节改标题为「A/B 档深挖（r46–r47）」，补 r47 三条发现与 `116` 指针。
- 目录 **13,182 → 13,679 行（+497）**；文件数不变（146 客户 MD + README）。

### 五、方法与诚实边界

**本轮新方法**
1. **协会/集群名录是挖"国产化玩家"的捷径** —— Technopc 的 `27,500 m² / 250 人 / Yerli Malı Belgesi / SAHA+Ostim 双会员` 全部来自 **SAHA İstanbul 与 Ostim Savunma 的企业页**，官网只说"领先"。
2. **商标注册号能证明"自有品牌"** —— upTech 的 **2008/13951** 一锤定音（官网自述 + 商标库双证），比"看起来像自有"可靠得多。
3. **"客户把价格印在网站"是稀缺资源** —— 一旦遇到（Winet），**立刻记进档案**，它是未来所有定价谈判的参照。
4. **`OEM-` 前缀 / 分类首图**这类"结构性痕迹"比文案更有信息量（Winet 的 `OEM-`、Cebeci 的 `Cifocs` 首图）。

**诚实边界**
- `085 Netmax`、`087 Uğur İmre`、`097 Labor Mühendislik`：**主体未确认**，只写"一次通话建档"。
- `096 Voltech`：**实为两个不同主体**（Silvri 小店 vs 迪拜 L.L.C + Perpa），111 对应哪家**未确认** → 本档阻塞。
- `072 Lemax`：零售套装商，客单价极低 → **建议降 C**（与 r46 对 Baburtech/Düzgün 的处理逻辑一致：品类不对，不是资料不足）。
- **对位表右列的我方规格来自仓库 `112` 目录快照（r24 索引，2026-10）**，**不是 2026-11 最新价表** → **报价前必须内部复核价与 MOQ**（已写进 `116` §四）。
- 客户侧 **6 家只有"分类"没有"型号"**（Coptek 的 L3/PoE 分类、Koza、Lansan、HCS、Antalya Turkuaz 部分品牌、Zeytek）→ 对位只到**档位级**，未到型号级。

---

## §42 · 第 48 轮 — 2026-11-01 ≈22:40–23:50 (+0800)：四家客户**产品清单取证**（型号级）+ 一处**证伪自我修正**

用户：「继续」。承接 r47 ROI 清单，**只做 A+B，C 零投入**。这轮不进新客户，**进客户官网把分类点到底，拿型号**。

### 一、⭐ 最重要：`116` 的 bt 行被自己证伪（已改）

r47 的缺口矩阵写「**802.3bt：只有 ErETE / NFS**」。r48 逐型号抓 upTech 后发现：

- **`SW1082-GGSUP`** 8×GE PoE，**1–4 口 802.3bt**，300 W
- **`SW20244-GGCUP`** 24×GE PoE，**1–4 口 bt**，500 W
- **`SW2082-GGSUP`** 8×GE PoE，**1–4 口 bt**，300 W

→ **bt 不是"0 命中"**。已把 `116` §一 第 2 行改写为「**bt 已有，但仅 1–4 口、总功率 300–500 W**」，并把话术从「我们有你没有」改成「**全口 bt / 单口 60 W / 总 800 W**」。
**2.5G / 250–300 m 长距 / 云管理 / 40–100G 上联四行仍然是真 0 命中**（upTech 全线 + ErETE XPS 全线已确认）。

### 二、`117-customer-catalog-forensics-2026-11-01.md`（新品）

四家 = 四种客户类型，全部给到**型号级**：

| 客户 | 类型 | 本轮拿到 |
|---|---|---|
| **`A/052` upTech** | 自有品牌贴牌商 | **14 款交换机全表**（非管理 PoE 5 / L2+ 7 / L3 2）+ **命名规则** + **916 SKU 分类结构** + B2B 平台 `noktaelektronik.com.tr` |
| **`A/053` Winet** | **WISP 渠道**（定性修正） | **30 个品牌 SKU 计数** + **全站 USD 标价 / 满 $10,000 免运费 / 当日自提** + **8 个美元价** |
| **`B/010` ErETE** | **开放网络分销商**（定性修正） | **OPEN NETWORKING 7 款全为 Edgecore**（含 `Wedge100BF-32X` Tofino、`ASXvOLT16` XGS-PON OLT）+ **NOS = OcNOS 6.6（IP Infusion）** + 骨干 5/8 为 Edgecore ECS |
| **`B/062` Cebeci** | 电信测试 + 自有转换器牌 | **Cifocs 13 款**（转换器 6 / 工业 `CFC-4G2SFP-IPS` / 光纤电话 6）+ **内部码 `OPT-###` / `RSC-###`** |

### 三、两个定性修正（都推翻 r47）

1. **Winet 不是"自有品牌网络设备商"** —— Brands 页原文：**Mikrotik 473 · WINET 426 · Ubiquiti 319 · Ruijie 40 · Mimosa 29 · WiPOINT 24 · VSOL 23 · GMT 23 · Mean Well 20 · RF Elements 18 · NetElastic 18 · S-Link 17 · TP-Link 16 · DeltaLink 9 · DMA-SOFT 6 · Everest 6 · Paessler 4 · RedLine 3 · Extralink 3 · Xiaomi 3 · Tenda 3 · Compex 2 · Juniper 1 · Pisces 1**。
   → **它是 WISP / FTTx 渠道**，自有 WINET 只是 house brand。**要卖的从"24 口机架式"改成"塔上那台 DC 供电、能远程重启的 PoE"** → 我方 **`EW-EPIS3910-8GE`**（1–2 口 DIP 选 **12V/24V 被动 PoE**，正对 Mikrotik 生态）。
   **新价格锚点**：`RG-ES08G-L`（8 口千兆非管理）**USD 19.50**、`RG-POE-AT30` **$21.00** → 与自家 `OEM-8-PORT-GB-POE`（2,916.76 ₺+KDV）并列，**PoE 溢价区间被量化**。
2. **ErETE 是 Edgecore 分销商** —— 7 款 ONIE 设备全为 Edgecore，NOS 只有 **OcNOS 6.6** 一个 SKU（⇒ IP Infusion 是其唯一 NOS 线）。
   → ⚠ **与 Angora 自身 Edgecore 线可能正面撞车** → 已在 `117` §五 立为**内部待拍板问题**：**确认前不要给 ErETE 发任何含 Edgecore 字样的邮件**；接触方式取决于 Angora 是「Edgecore 渠道」还是「自有/ODM 白盒」。

### 四、`Cifocs` 推定（仍不作定论）

Cifocs 13 款全部用**自家编号体系**（`CFC-*` + 内部码 `OPT-###`/`RSC-###`），而它代理的 Argus / Micos / Greenlee-Tempo / Trend / InterCoax **全部用原厂型号**（`MIS-900`、`801K`、`NC-500`、`TM-700`、`Argus 153/260`）
→ **推定 Cifocs 为 Cebeci 自有/独家贴牌牌**（与 upTech 的 `SW-` 体系同构）。
⚠ **商标注册人仍未在公开面确认** → 首封必问「**Cifocs sizin tescilli markanız mı?**」，**任何客户可见文本不得写"自有商标"**。

### 五、产出与规模

- 新增 `08-customer-pipeline/117-customer-catalog-forensics-2026-11-01.md`。
- 新增 `08-customer-pipeline/r48_appendix_data.py`，**`build_tr_customers_r44.py` 已接入**（r48 小节追加在 A/B 深挖之后，生成 4 份：`A/052`、`A/053`、`B/010`、`B/062`）。
- `116` §一 修正 bt 行 + 增 r48 修正块 + 头部指向 `117`。
- 根 `README.md` 增 `117` 链接。
- 目录 **13,679 → 13,877 行（+198）**；文件数不变（146 客户 MD + README）。

### 六、方法与诚实边界

**新方法**：① **命名规则反推产品线**（`SW` + 1/2/3 + 端口 + 代号）一次覆盖 14 款；② **品牌页的 SKU 计数是渠道结构指纹**（Mikrotik 473 vs WINET 426 一眼定性）；③ **内部产品码 vs 原厂型号的对照**是判别自有牌的最强公开证据。
**诚实边界**：ErETE 的 Edgecore 授权层级、OcNOS 授权方式、Cifocs 商标注册人、upTech 现工厂、Winet 法定名与员工数 —— **全部仍空白**，已在各档「证据等级」逐条列出。

---

## §43 · 第 49 轮 — 2026-11-01 ≈23:55–01:20 (+0800)：**上一轮三个未决问题全部收口**（ErETE 供应链 / upTech 工业线 / Cifocs 证据）

用户：「继续」。**0 新客户**，只打上一轮自己列出的 ROI 前三项 + 一个内部溯源。

### 一、⭐⭐ ErETE 阻塞项解除（本轮最重要）

**两条证据同时到手**：
1. **仓库内既有**：`06-competitors/110` §十 已写明 **PNetworks 硬件底座 = Edgecore（Broadcom）+ SONiC + OcNOS**（Edgecore 官方新闻稿 MWC 2024-02-29），且 **PNetworks 是 Angora 的本土竞对**；§13 写明 **Angora 线 = Ewind（深圳 ODM）+ Marvell AC3/AC5**。
   → **Angora 不是 Edgecore 渠道；土耳其的 Edgecore 白牌玩家是 PNetworks。**
2. **外部决定性**：**`ipinfusion.com/partners/` 的 Resellers 名单原文含 `Erete — EMEA, Turkey`** → **ErETE 是 IP Infusion 官方授权 Reseller**。

**⭐ 但因此推翻 r48 的建议**：`OcNOS Systems` 的合格硬件**只有 Edgecore（PRO）与 UfiSpace（FAST）**，**我方 Marvell 箱子不在清单里** →
**不能**说"我们的交换机跑 OcNOS，比 Edgecore 便宜"。定稿话术改为：**「XPS 品牌的接入/园区线，与 OcNOS 数据中心线互补」**，只打接入段。

**⭐ 新发现**：ErETE 真正在打的自有牌是 **`XPS-1220` 线 5 款 GE 接入 PoE**（`-10P` 8 口 / `-18P` 16 口 / `-26P` 22 口 / `-26PH` 高功率 / `-52P` 48 口），**全线 GE + 1G SFP 上联，无 2.5G、无 bt、无 10G、无云** → **这才是我方能正面对打的一段**。
另：**`Kenar Switchler` 分类是空的**（导航有入口、0 产品）；**L3 分类 6 款全部 Edgecore**。
→ 定性：**「西边 Edgecore 打 DC/骨干/L3、东边 XPS 打接入/工业」的双轨机器；我方只在东边有意义。**

### 二、⚠ upTech 工业线补正（r48 的"无工业宽温"是错的）

`noktaelektronik.com.tr/urunler/endustriyel-ethernet-3` = **50 个产品**，upTech **`ISW` 系列至少 6 款**：`ISW2420-GGS/GGSP`、`ISW2820-GGS/GGSPV`、`ISW1820-FGSP`（**非管理还是百兆**）、`ISW21240-GGS`。
**工业段差距**：upTech **全部 GE + 1G SFP，无 2.5G / 无 10G / 无 bt**。
**⚠ 两处话术禁区**：同分类里 **ORing `RGPS-R9244GP+-P` = 24×PoE+ 带 4×10G**（"工业没 10G 上联"不能说）、**Dahua `PFS4207-4GT-DP` = 4 口 bt 单口 90 W**（"单口功率最高"不能说）。

### 三、WINET 结构复核

WINET **426 SKU 的主体是无源光**：Breakout **53** / Patchcord Duplex SM **37** / **PoE 注入器 22** / 电源 16 / LoRa 14 / SFP+ 10G 11 …
→ **它是 FTTx 现场物料商，不是交换机品牌**（r48 的"少量交换机"改为"**近乎孤例**"）。
→ 最锋利一句：它自己卖 **22 个注入器**（`RG-POE-AT30` **$21**）→ 用 **`EW-EPIS3910-8GE`** 打「1 台顶 4 个注入器 + 4 条线 + 4 个电源 + 可远程重启」。

### 四、Cifocs 权重下调

`cebecigrup.com/markalar/` 品牌墙 **13 个品牌**（argus · BitStream · cifocs · cmg · greenlee · intercoax · Kingfisher · Maisvch · micos · PatchSee · tempo · trend-networks · vesala）→ **Cifocs 与 12 个外国品牌并列、无 "our brand" 标注** ⇒ **证据权重从"偏自有"下调为五五**，**仍作推定**，客户可见文本**禁写"自有商标"**。TÜRKPATENT 检索仍需人工（图形验证码）。

### 五、产出与规模

- 新增 `08-customer-pipeline/118-erete-supply-chain-and-uptech-industrial-2026-11-01.md`。
- 新增 `08-customer-pipeline/r49_appendix_data.py`，`build_tr_customers_r44.py` **已接入** → `A/052` `A/053` `B/010` `B/062` 各增 **「附：r49 复查收口」**。
- `116` **工业宽温行已修正** + 头部指向 `118`。
- 根 `README.md` 增 `118` 链接。
- 目录 **13,877 → 13,971 行（+94）**；文件数不变（146 客户 MD + README）。

### 六、方法与诚实边界

**新方法**：① **先在自己仓库里找答案**（Edgecore 归属由 `110` 一号文件解决，零抓取）；② **厂商 Partner 页（Reseller 名单）是"授权关系"的权威证据**，比客户官网自述可靠；③ **OcNOS 合格硬件清单 = 我方能不能卖的分界线** —— 这类"资格清单"必须在报价前查，否则一查就露。
**诚实边界**：工业分类 50 个产品只读了第 1 页 20 个；ErETE 分类 68/71/95–99 未读；WINET 折叠子类未读完；**Cifocs 商标仍是唯一未解阻塞项**；IP Infusion 授权是否**独家**官网未写。

---

## §44 · 第 50 轮 — 2026-11-01 ≈01:30–02:40 (+0800)：ErETE 全站点算完成 + **两条自证伪** + WINET 枚举边界

用户：「继续」。**0 新客户**。本轮的价值不在"又挖到新东西"，而在**把前两轮的过度结论按证据收回**。

### 一、ErETE 产品树逐分类点算完毕（12 类）

| 分类 | 数 | 品牌 |
|---|---|---|
| 骨干 33 | 8 | Edgecore ECS 5 + 自有 `XPS-1320-36F` 1 |
| **边缘 34** | **0** | **空分类** |
| 网管 L2 68 | **12** | **全 Edgecore**（ECS4210/4110/4510/4120） |
| 网管 L3 69 | **6** | **全 Edgecore**（ECS4610/4620） |
| WebSmart 70 | **9** | Edgecore ECS2100 + 自有 **`XPS-1110-18/26`（仅百兆）** |
| **PoE 71** | **16** | ⚠ **全 Edgecore**（`ECS2100-10P` 125W / `ECS2100-28PP` 400W / `ECS4210-12P·28P` / `ECS4110-52P` / `ECS4620-28P·52P`） |
| L2+ PoE 94 | **5** | **全自有 XPS-1220** |
| L2+ 网管 98 | **11** | **全自有 XPS**（1220×3 + **1320×8**） |
| ONIE 102 | 7 | 全 Edgecore |
| NOS 107 | 1 | `OcNOS 6.6` |

**比例 Edgecore : XPS ≈ 46 : 19 ≈ 2.4 : 1。**

### 二、⚠ 自我证伪两条

1. **「XPS 全线无 10G 上联」——错。** `XPS-1320-28P` = **24×GE PoE + 4×10G SFP+**；`XPS-1320-52P` = **48×GE PoE + 4×10G SFP+**；`XPS-1320-36P/36PH` = 24 PoE + **8×SFP**；非 PoE 版 `XPS-1320-28/36/52` 同样 4×10G。
   → **只能说三件事：无 2.5G · 无 802.3bt · 无云管理。**
2. **「东边 XPS 打接入、西边 Edgecore 打 DC」——太干净。** **PoE 主力 16 款全部 Edgecore**，XPS 只在 94（5 款）与 98 中带 PoE 的 5 款出现。
   → **正确表述：Edgecore 是主轴（含 PoE 与接入），XPS 是"补位的自有线"**；我方定位从"替代 XPS"再收窄为 **"给 XPS 补 2.5G 与 bt 两档，且接受贴 XPS 牌"**。

### 三、upTech 工业线全 50 款读完：**upTech 只有 8 款**

`ISW2420-GGS/GGSP`、`ISW2820-GGS/GGSPV`、**`ISW2840-GGSP`（8 PoE + 4 SFP）**、`ISW21240-GGS`、`ISW1820-FGSP`、**`ISW1811-FGSP`**。
工业分类品牌分布：**ORing ≈ 20 · Planet ≈ 12 · upTech 8 · Dahua 6 · Harting 2 · Edge-Core 2**。
→ ⭐ **工业主供是 ORing，upTech 这条是"刚铺的补位线"（多款标 `Yeni`）** → **动不了 ORing，但最容易换掉 upTech 这条新线**，这是本季最佳切入点。
⚠ 同分类 **Dahua `LR2118-16ET-240` ePoE 单线 800 m**、**`PFS4207-4GT-DP` bt 单口 90 W** ⇒ "长距"与"单口高功率"在该渠道已被占位。

### 四、WINET 枚举硬边界

三条实测全封：**分类页商品列表 JS 渲染返回 `No results found`**；**`sitemap.xml` 只有 20 个栏目页、无任何商品 URL**；**facet 被无关品类污染（PoE 分类里混进 Wi-Fi AP 字段）不可当计数**。
→ **撤回 r49 的「WINET 交换机近乎孤例」**（无证据）；改为 **"公开面不可枚举 = 硬边界"**，首封直接向客户要产品目录。

### 五、全局修正：「云管理」不再是差异化

Winet 卖 Ruijie（Reyee 云）、Nokta 卖 Dahua（DoLynk）/Planet/ORing、`wi.com.tr` facet 已出现 UniFi Cloud / Cloud Mobil Yönetim
→ **云管理在土耳其渠道已是"配置项"**，`116` 该行已改弱；我方差异化回到 **2.5G / 全口 bt / 300 m 长距 / 12–24 V 被动 PoE** 四条硬规格。

### 六、产出与规模

- 新增 `08-customer-pipeline/119-erete-full-catalog-and-uptech-industrial-full-2026-11-01.md`。
- 新增 `r50_appendix_data.py`，`build_tr_customers_r44.py` 已接入 → `A/052` `A/053` `B/010` 各增 **「附：r50 全量点算与结论回收」**。
- `116` **云管理行改弱 + 40/100G 行补注**。
- 根 `README.md` 增 `119` 链接。
- 目录 **13,971 → 14,062 行（+91）**；文件数不变（146 客户 MD + README）。

### 七、方法与诚实边界

**新方法**：① **分类页的产品数 + 品牌名 = 一句话就能算出的"主轴/补位"结构**；② **facet 不等于 SKU 计数**（会被跨品类污染），**商品列表 JS 渲染时 facet 反而是唯一线索但不可用于计数**；③ **sitemap 无商品 URL 是很多 Next.js 电商的通病**，遇到就直接放弃枚举、改为"向客户要目录"。
**诚实边界**：ErETE 分类 **95 / 96 / 97 / 99 未取**（99 fetch 失败）；WINET 自有交换机数量**仍未知**；`XPS` 的"PH 高功率档"具体瓦数**未取**（页面只写端口数）。

---

## §74 · 第 80 轮 — 2026-11-06 ≈08:30–11:00 (+0800)：**「÷2.95」被证伪为通用规则（PLANET 反例 0.81×）→ 定价拆双轨** / **新 K 码 İNFOGEN `K5884`（PLANET 挂单方）** / **电力段三条新线索（İNFOGEN · Simgenet · İSAC）与 IEC 61850-3 代理地图** / **Nokta 工商身份补完（推翻 2000 年成立）**

用户第 33 次「继续」（每轮 ≥10 工作分钟）。本轮做的是**给自己上一轮的规则找反例** —— 找到了，规则必须拆轨。

### 一、🛑 修正 r79：`÷2.95` 只是「白牌挂牌虚高」的特例
反例：**PLANET `IGS-801T`（8 口工业千兆非 PoE，−40~75 ℃，IP30，16 Gbps，4K MAC）**
- **DMO 净价 6,955.49 ₺ / 含税 8,346.59 ₺ ≈ $139 / $167**；
- **美国 MSRP $172**（planetechusa / neteon）· **Newegg $179** ⇒ **DMO = MSRP 的 0.81 倍**。
**⇒ 新规则（三句）**：① 有公开 MSRP / 全球零售可比的品牌（PLANET / Moxa / Cisco / HPE）**DMO ≈ 0.8–1.0× MSRP**，直接引用；② 只有「官网自挂一张价、无第三方可比」的白牌（RUBISEC）**才 ÷2.3–3.0**；③ **探针 = 去 Newegg / planetechusa / DigiKey 搜同型号**，搜得到走①，搜不到走②。
**⇒ 实际影响**：**Moxa / Planet / Cisco 的历史价格锚不需要重算**，省掉一整轮返工。

### 二、⭐⭐ 新 K 码 `K5884` = **İNFOGEN DANIŞMANLIK VE BİLİŞİM A.Ş.**
挂 **PLANET `IGS-801T`**（产品码 131798），**合同 2026-03-10 → 2028-03-10（刚续两年）**，电话 **0216 706 1845**；另有 `K3193` / `K4329`（D-Link，r76）。
⇒ **它同时是 D-Link 与 PLANET 的 DMO 挂单方** ⇒ **「中低端进口网络设备」在政府渠道的实际操盘手**，客户表里没有的一类角色。
⇒ **PLANET 的 8 口工业 PoE 不在 DMO** ⇒ **这一格在 İNFOGEN 这里也是空的** ⇒ **打法：不替代 PLANET，补它缺的那一格。**

### 三、⭐⭐⭐ 电力段三条新线索（与现有 146 家客户零重叠）
- **SİMGENET MÜHENDİSLİK ENERJİ SAN. VE TİC. LTD. ŞTİ.**（**2020-04-05**，Kartal/İstanbul，**Orhantepe Mah. Girne Sk. No:25A**，迁 **Tomurcuk Sok. 4B**，**+90 555 600 45 06**，`info@simgenet.net`）：**3onedata 土耳其代理**（`MES5400` 30 口模块化 L3 **IEC 61850-3** HSR/PRP 1588v2 · `MES5300-28GS` · `MES5300-24GT4GS` · `MES5200` · `MES6400PHR-8GT4XS` · `ICS5400TSN`）+ **自研 SMGOS 平台** + **Simgenet Teleprotection Unit V2**；业务 = **TEİAŞ OPGW · PAX · PLC 载波 · TPU · RTU · 本地 SCADA · IP/MPLS · SDH/PDH**；ISO 9001 / CE / TSE。
- **İSAC**（`isac.com.tr`，**0850 60 60 180**，`bilgi@isac.com.tr`）：**Advantech 工业以太网交换机授权伙伴**（`EKI-2000/5000/7000/9000`，`EKI-2525P`、`EKI-2728`），自我定位「工业传感器 + 自动化供应商」。
- **İNFOGEN**（见上）。

### 四、⭐⭐ 电力段（IEC 61850-3）代理地图：这一格已被 6 家分完
**Moxa → GSL Mühendislik**（IEC 61850-3 / EN 50155 / NEMA TS2 / IEC 62443）· **Kyland → GSL**（IEC 61850-3 / EN 50155）· **EtherWan → ErETE**（`EX47000` / `EX47080-00B`，IEC 61850 / IEEE 1613，−40~75 ℃）· **3onedata → Simgenet**（IEC 61850-3 / HSR/PRP / 1588v2）· **JetNet(Korenix) → Beijer Electronics Türkiye**（IEC 61850-3 / DNV / eMark / ITxPT / EN 50155）· **Advantech → İSAC**（CE/FCC/UL，工业级非变电站）· **RUBISEC → Birkil**（⚠ 未见 IEC 61850-3 声明）。
**⇒ 我方进这一段的唯一路线：做「第二源」而不是「第三品牌」** —— 找**已有电力客户但品牌单一**的 Simgenet / ErETE / İSAC，给一个**同规格、能并行投标**的备份。

### 五、⭐⭐ DMO「工业 8 口」两轴定稿
非 PoE：**PLANET `IGS-801T` $139（İNFOGEN K5884）** → PoE：**DAHUA `PFSC28GT1-120D` $380** → **RUBISEC `RS-IS-300-12GP` $584（暂时无货）** → **`RS-IS-200-10GP` $668–770** → **`RS-IS-300-12GPX` $1,221（−40~80 ℃，240 W）** → ALCATEL `OS6465T-P12` $1,306–1,328 → **CISCO `IE-3300-8P2S-E` $2,315**。
⇒ **我方 $500–700 的三条支撑**：Dahua $380 = **非受管 + 120 W + −30 ℃**；RUBISEC $584–770 = **无货 / 非宽温 / 资料不全**；Cisco = 天花板 ⇒ **「受管 + 240 W + 整机 −40~75 ℃ + 有货」= 唯一解。**

### 六、⭐ Nokta 工商身份补完（推翻 r79 的「2000 年成立」）
**VKN `6310730521`（Şişli）· MERSİS `0631-0730-5210-0020` · 商业登记 `555138-0` · 注册成立 `2005-05-26`（原名 LTD，后转 A.Ş.）· 实缴资本 `30,000,000 ₺`（≈$600k）· NACE #465202 · ETBİS 2024-05-02 · `upTech` 是它注册的商标 · Perpa A Blok K:2 No:1 / 信函 B Blok K:8 No:906 · 0212 222 87 80 · `nokta@noktaelektronik.net`。**
⇒ **实缴 3,000 万 ₺ = A 级里「中等偏上」的重资产分销商**；⇒ **「2000 → 2005」差 5 年 ⇒ 对方讲 25 年时打折听，但不点破**；⇒ **`upTech` 有商标 ⇒ 不换牌，换里面的板子**。**分级 78 → 81。**

### 七、产出
新增 `08-customer-pipeline/149-pricing-rule-split-and-power-segment-leads-2026-11-06.md`；新增 `r80_appendix_data.py`（键 `'52' '62'`）；builder 接入 `R80` + `R80_MARK` + emit 块；根 `README.md` 增 `149`；本 ledger 增 §74；`AGENT-README` 增行 80；`00-TASK-STATUS.md` 增 CL 行 + 待办 61。

### 八、方法与诚实边界
**新方法**：① **规则必须找反例** —— 上一轮立的 ÷2.95，本轮被 PLANET 的 0.81× 推翻为「白牌特例」；② **MSRP 探针法**：用海外零售站判断一个品牌有没有真实价格锚；③ **「代理地图」优先于「客户名单」** —— 电力段 6 家代理一次列清，比逐家搜客户高效。
**诚实边界**：İNFOGEN 的工商身份未知（只有电话 + K 码）· Simgenet 员工数/营收/VKN 未取（2020 年成立、手机号做总机 ⇒ 疑 ≤10 人，**未证实**）· İSAC 法定全称/地址/VKN 未取 · **Karer / CryptoLink / Novacom 的 VKN 本轮检索失败（b2bhint 与 eticaret 均无命中）** · PLANET 的 8 口工业 PoE 是否在 DMO · **RUBISEC 是否有 IEC 61850-3 声明** · **所有电话未试拨**（新增 İNFOGEN 0216 706 1845 · Simgenet +90 555 600 45 06 · İSAC 0850 60 60 180）。

---

## §73 · 第 79 轮 — 2026-11-06 ≈06:10–08:30 (+0800)：**「挂牌 ÷2.95 = 成交」被 DMO 实价验证（误差 0.3%）** / **工业货架上有空位（$584 有价无货）** / **Snexus 真正主体是 Hemmah（VKN+MERSİS）** / **Cebeci 名字撞车排雷**

用户第 32 次「继续」（每轮 ≥10 工作分钟）。本轮任务是**检验上一轮自己立的两条规则**，同时把客户的「工商级身份」补到能开发票的密度。

### 一、⭐⭐⭐ 「挂牌价 ÷2.95 = 成交价」被实价验证
r78 按 RUBISEC 挂牌 `RS-IS-300-12GPX` **$3,600** 预测成交 ≈ **$1,225**；本轮 DMO 详情页：**61,075.68 ₺ ≈ $1,221（含税 73,290.82）** ⇒ **误差 −0.3%**。
| 型号 | 挂牌 | 预测 | **实价** | 倍率 |
|---|---|---|---|---|
| `RS-IS-300-12GPX`（8×PoE + 2 GbE + 4×10G，−40~80 ℃，240 W） | $3,600 | ≈$1,225 | **$1,221** | **2.95×** |
| `RS-IS-200-10GP`（8×PoE + 2 SFP） | $1,800 | ≈$610 | **$668–770**（聚合） | 2.34–2.70× |
| `RS-IS-300-12GP`（8×PoE + 2 + 4×1G SFP） | $1,950 | ≈$660 | **$584**（**无货**） | 2.61× |
⇒ **工业段溢价结构**：商用 8 口 `RS-ES-200-10PS` **$257** → 工业 **$584（2.3×）** → 工业 + 10G + 宽温 **$1,221（再 2.1×）**。

### 二、⭐⭐ 工业货架上有空位：`RS-IS-300-12GP` 详情页写 **「暂时无法供货」**
`Ürün geçici olarak temin edilememektedir` ⇒ **DMO 的「8 口工业 PoE」现状 = Dahua $380 · RUBISEC $584（无货）/ $668–770 · Cisco IE-3300 $2,315** ⇒ **$500–700 这一格是「有货 + 有认证」的空位**。

### 三、⭐⭐⭐ Snexus 的真正主体 = **HEMMAH GROUP BİLİŞİM VE MİMARLIK TİCARET LTD. ŞTİ.**
**MERSİS `0461092236500001` · VKN `4610922365`** · **Turgut Özal Blv. No:2 A6 No:145, Çekmeköy/İstanbul** · `info@hemmahgroup.com` · 11–50 人。
`snexus.com.tr` 域名注册人 = Hemmah；销售合同抬头 = Hemmah；**经销商页只列 Hemmah 一家** ⇒ **品牌方 = 唯一分销商**；且**自己在 Trendyol / Allesgo 开店**。
⇒ **决策链最短 + 库存压力在自己身上 + 工业格全空** ⇒ **分级 85 → 87（A 级第一梯）**。

### 四、⚠ 名字撞车排雷：Cebeci 是两个主体
| | **我们要的（B/062）** | **不是** |
|---|---|---|
| 全称 | **CEBECİ TELETEKS SANAYİ TİCARET LTD. ŞTİ.** | **CEBECİ GRUP İNŞ. TUR. TİC. A.Ş.** |
| VKN | **2040018047** | — |
| 地址 | **Halil Rıfat Paşa Mah. Yüzer Havuz Sok. No:8 K:3 D:24 Okmeydanı/Şişli** | Alanya/Antalya（Şekerhane Mah.） |
| 行业 | **电信测试仪表 + ONV 工业交换机** | **建筑 / 房地产** |
| 规模 | 小型 | **66 人 · $50.5M · 1982** |
⇒ **域名 `cebecigrup.com` 归「电信测试」这一家**（页面是 Greenlee 711K / Argus 166 / Tempo TM-500 / NC-500）。**纪律：提 Cebeci 必须带 VKN `2040018047` 或「Yüzer Havuz Sok.」。**
⇒ **它在卖 ONV（深圳）** ⇒ **我方直接竞品的下游**。

### 五、⭐⭐ FOREDGE 的 DMO 实价收口
`IS108GPS-2F` 在 **FS Grup（K4702）详情页 = 52,264.98 ₺ ≈ $1,045**（聚合页 44,928.91 / 57,262.43 / 57,784.04）。
**FS Grup 的 FOREDGE 交换机共 12 个 SKU，价位 5,807–121,951 ₺（≈$116–2,438）** ⇒ **「一站式报单」逻辑（每价位放一台），不是专业工业逻辑** —— **这是我方在 8 口工业能赢的结构性原因。**

### 六、⭐ 六家客户身份补齐
**Nokta**（**2000 · 75–99 人** · Perpa **A Blok K:2 No:1** · 0212 222 87 80 / 0850 333 02 08 · **伊斯坦布尔自有生产设施 + AR-GE** · 出口中东/巴尔干/突厥）· **Karer**（**2006** · Pendik Atasever Cd No:44 · **1,000 ㎡** · **CEO Nurbaki Karataş** · DESİ 34/16 服务商）· **CryptoLink**（Çankaya Bükreş Cd No:19/1 · **0312 557 64 00** · 边境安全/网安/车牌识别/信号干扰 ⇒ **最纯的政府项目商**）· **Novacom**（**Nova Grup Mühendislik，2002，安卡拉，NOVACOM 注册商标** ⇒ **弱电/卫星电视出身，网络判断力弱，但 SKU 更新意愿最强**）。

### 七、分级变动
Snexus **85→87** · Nokta **78→80** · CryptoLink **80→81** · Karer **76→77** · Cebeci **45→47** · **Novacom 86→84 ↓**（弱电出身，网络非主场）。

### 八、产出
新增 `08-customer-pipeline/148-customer-vkn-and-industrial-shelf-gaps-2026-11-06.md`；新增 `r79_appendix_data.py`（键 `'2' '3' '5' '7' '52' '62'`）；builder 接入 `R79` + `R79_MARK` + emit 块；根 `README.md` 增 `148`；本 ledger 增 §73；`AGENT-README` 增行 79；`00-TASK-STATUS.md` 增 CK 行 + 待办 60。

### 九、方法与诚实边界
**新方法**：① **预测—验证闭环**：上一轮用规则算出的数，这一轮必须拿实价回验（本轮 1 中 1，误差 0.3%）；② **「暂时无法供货」是标书里最锋利的刀** —— 有价无货 = 目录位空着；③ **同名不同主体必须先排雷再建档**（Cebeci 就是样本）。
**诚实边界**：`RS-IS-200-10GP` 详情页价未取 · **Nokta / Karer / CryptoLink / Novacom 的 VKN/MERSİS 仍缺** · Nokta 的生产设施地址未取 · Hemmah 老板姓名未知 · FS Grup 的 12 个 SKU 只取到 3 个价 · **所有电话未试拨**（新增 Nokta 0212 222 87 80 · Karer 0216 397 33 88 · CryptoLink 0312 557 64 00 · Cebeci 0212 320 08 88）。

---

## §72 · 第 78 轮 — 2026-11-06 ≈03:40–06:10 (+0800)：**RUBISEC = 黑山注册 + 爱沙尼亚总部 + 香港物流 + 中国代工** / **挂牌价 ÷2.96 = 成交价** / **Birkil Savunma 建档（5 年公司拿到两年期 DMO 合同）** / **四家客户身份卡可打电话**

用户第 31 次「继续」（每轮 ≥10 工作分钟）。本轮把 r77 留的四个缺口一次结掉：**RUBISEC 主体 · Birkil · Dayzip 工厂 · TG-NET 实体**。

### 一、⭐⭐⭐ RUBISEC 的真实身份：一个「离岸品牌」的标准模板
官方 About 时间线：**2016 黑山成立 → 2018 迪拜研发办 → 2020 总部迁爱沙尼亚 → 2023 香港物流中心**。
DMO 产品页 `Menşei` = **Karadağ（黑山）**；页脚地址 **Budva, XVI Ulica, Lokal br. 7**；客服 **+372 5838 16 45（爱沙尼亚）**；官方 datasheet 自称 `independently developed by Rubisec`。
⇒ **模型 = 品牌壳（黑山）+ 总部（爱沙尼亚）+ 研发（迪拜）+ 物流（香港）+ 代工（中国）**。
⇒ **对客户的含义**：**「土耳其本土制造」没有制度红利** —— DMO 只认「原产地 + 供应商 + 合同 + 价格」，一个黑山品牌能进目录，本土牌的价值只在「集成商信任 + 服务响应」。

### 二、⭐⭐⭐ 挂牌价 vs 成交价 = **2.96 倍**（本轮最重要的定价纪律）
`rubisec.com/price-list/` 公开 **43 项 `Partner Project Price`**（USD）：
**`RS-ES-200-28PS` 挂牌 $1,200 → DMO 20,331.42 ₺ ≈ $406（2.96×）** · `RS-ES-300-28GPX` $2,100 → 38,973.49 ₺ ≈ $779（2.69×） · `RS-ES-300-52GPX` $2,550 → 42,899.79 ₺ ≈ $858（2.97×） · `RS-ES-350-54GPX` $6,660 → 117,708.23 ₺ ≈ $2,354（2.83×） · `RS-ES-200-10PS` $600 → 12,840.90 ₺ ≈ $257（2.33×）。
**⇒ 纪律：任何「官网 price list / partner price」一律 ÷2.3–3.0 还原成交价**，再用 DMO 详情页校准（Moxa / FOREDGE / Planet 同理）。
**⇒ 工业线还原**：`RS-IS-100-10GP` $550 → **≈$235** · `RS-IS-200-10GP` $1,800 → **≈$610** · `RS-IS-300-12GPX`（8×PoE + 2 RJ45 + 4×10G，−40~80 ℃，240 W）$3,600 → **≈$1,225**。**我方 8 口工业 PoE $125.72 在所有这些数的一半以下。**

### 三、⭐⭐⭐ Birkil Savunma 建档 —— 用 5 年资历拿到两年期 DMO 网络合同
**BİRKİL SAVUNMA TEKNOLOJİLERİ A.Ş.**：**2021-01-21** 成立、**单一股东 A.Ş.**、NACE **620101**、**`K4525` + `K6355` 两个码都是它**、合同 **2026-09-02 → 2028-09-02**、交期 30/35/40/45 天、电话 **0312 284 8477**、`info@birkil.com`。
总部 **Kızılırmak Mah. Ufuk Üniversitesi Cd. Next Level Loft No:4 K:15 D:44 Çankaya/Ankara**；研发办 **Gazi Üniversitesi Gölbaşı Yerleşkesi C Blok No:10/50-C/112**。
代理 **Allied Telesis · Milestone · Ruckus · Axis · BCD · Canon · Skyfilter · Rubisec · FF Group · Maipu**；主营 **弹药/防弹/反无人机/雷达**。
⇒ **结论句**：**如果一家 5 年历史的安卡拉防务小公司都能进 DMO 卖交换机，我们的客户没有理由进不去 —— 缺口只有一个：能过目录价的成本结构。**
✅ **技术债结清**：r44 起挂的「RUBISEC `K4525`/`K6355` 合同期」已取得。

### 四、⚠ 再修正：`32,102.24 ₺` 是 DAHUA，不是 FOREDGE
**DAHUA `DH-PFSD224ET2-360D`**（**24×10/100 Base-T PoE 百兆** + 2 GbE combo + 2 SFP，8.8 Gbps，**360 W**，−10~55 ℃，产品码 **55492**），**AKTİF GRUP（K4969）与 RİVO 两家同价 32,102.24 ₺**。
⇒ r77 把该价记在 FOREDGE `AI2010GX` 名下是错的；**FOREDGE 在 DMO 的唯一已核实价 = `AI8024` 21,401.50 ₺**。
⇒ 新判读：① **政府花 $642 买「24 口百兆 PoE」** ⇒ 客户比的是「端口数 + 瓦数 + 250 m 远距离」，**不是千兆**；② **同型号两家同价 ⇒ DMO 价格由上游控**，**「换个分销商便宜 5%」不存在**。

### 五、⭐⭐ 四家客户身份卡（可打电话）
- **Cenova**：**Perpa B Blok Kat 7-8-9 No:902**（**占三层**）· **0212 221 13 40 / 222 71 66** · `rifat@cenova.com.tr` · **11–50 人** · LinkedIn 注册 **2004**（官宣 2002）· 地址码 **1599466776**。
  **🛑 推翻 r77「`Dayzip` 疑深圳 ODM 牌」**：**`Dayzip` 是 Cenova 自有品牌**（App Store 开发者 **Rifat BAYDEMİR**，版权 **© CENOVA BİLİŞİM**，`dayzip@cenova.com.tr`；第三方站确认 **CMS 由 Cenova 自研**）⇒ **Cenova 已跑通「自有牌 + ODM 硬件 + 自研 CMS」，缺的是工业段与 DMO 码。**
- **GSL**：**GSL MÜHENDİSLİK SANAYİ VE TİCARET A.Ş.**，**1988 安卡拉**，İlkbahar Mah. 612. Cad. No:9，**25–49 人**（ContactOut 29 / Tracxn 42），**安卡拉 + 伊斯坦布尔两办公室**，**Moxa 2003 起 22 年** + Robustel/Digi/Kyland/Pro Optix/RuggON/Transcend/**Tipro**，Key Principal **Ümit Özdemir**，GM Yrd. **Nevzat Özdemir**。
  ⇒ **它的护城河是技术服务不是价格 ⇒ 不会为 10% 换供应商；切口是它的边缘品类（Tipro/RuggON/Transcend）。**
- **Öncü**：**2002**，**51–200 人**，**1,500+ bayi**，**Beykoz 总部（Fatih Sultan Mehmet Cd. Yayabeyi Sk. No:8）+ Pendik Teknopark 二址**，0216 537 01 23 / 693 23 33 / 504 06 26。
- **Han**：**2000**，**51–200 人**，**营收 ≈$20M**，Bağcılar/Ümraniye 1904 Sk No:15/A，**总经理 Hakan Kasap / 采购经理 Fadime Maden ⭐**，DIA ERP + B2B 电商。

### 六、⭐ TG-NET 实体坐实
**Shenzhen TG-NET Botone Technology Co., Ltd.**，**2011**，总部南山中山园路 1001 号 E3 栋 4 楼，工厂 **龙华大浪华荣第二工业区 1,500 ㎡**，**200+ 人 / 60+ 研发 / 6 条线 / 日产 5,000 / ISO9001:2008**，深圳+上海双研发中心。
⇒ **与我方同量级 ⇒ CLR 换供应商的技术风险极低**；**⚠ 未验证**：CLR 是进口贴牌还是 TG-NET 代工（`CLR-*` 与 `P3010M-8POE` 同列 K291 目录，倾向前者）。

### 七、产出
- 新增 `08-customer-pipeline/147-rubisec-offshore-brand-and-identity-cards-2026-11-06.md`。
- 新增 `r78_appendix_data.py`（键 `'1' '4' '8' '9' '62'`），builder 接入 `R78` + `R78_MARK` + emit 块。
- 根 `README.md` 增 `147`；本 ledger 增 §72；`AGENT-README` 增行 78；`00-TASK-STATUS.md` 增 CJ 行 + 待办 59。

### 八、方法与诚实边界
**新方法**：① **`Menşei`（原产地）字段 + 客服电话区号 + About 时间线 = 三分钟判定一个「品牌」的真实国籍**；② **官网 price list ÷2.3–3.0 = 成交价**，再用 DMO 详情页校正；③ **「同型号多家同价」是 DMO 的定价机制特征**，不是巧合。
**诚实边界**：Birkil 真实 VKN（`find.com.tr` 税号是占位符 `1234567890`，**不可引用**）· **RUBISEC 的代工厂名未知** · RUBISEC `RS-IS-*` 工业线的 DMO 成交价未取 · Cenova/Öncü VKN 未取 · **Han 的 VKN、工厂地址、FOREDGE 代工厂名均未证** · GSL 营收未取 · **所有电话未试拨**（新增 Birkil 0312 284 8477 · Cenova 0212 221 13 40 · Öncü 0216 693 23 33 · RUBISEC +372 5838 16 45）。

---

## §71 · 第 77 轮 — 2026-11-06 ≈01:30–03:40 (+0800)：**DMO 聚合页会串价（方法修正）** / **FOREDGE 的 DMO 主体是 FS Grup K4702（合同有效到 2026-10-21）** / **RUBISEC 完整价格阶梯** / **GSL 311 实为 231 台交换机**

用户第 30 次「继续」（并要求每轮 ≥10 工作分钟）。本轮不铺新面，**先把 r76 的价格表打回详情页重核** —— 结果发现方法本身有洞。

### 一、🛑 方法修正：DMO 聚合页会「串价」（r76 表降级）
- `RUBISEC RS-ES-300-28GPX` 同型号三处价：**38,973.49 ₺（详情页）/ 31,784.73 ₺ / 334,604.66 ₺**（**8.6 倍差**）。
- `FOREDGE AI8024` 三处价：**21,401.50 ₺（详情页 119852-K4702）/ 25,681.80 ₺ / 58,072.20 ₺**。
- **`PLANET GS-4210-24P4C` 与 `FOREDGE AI8024` 被挂上同一个 25,681.80 ₺** ⇒ 串行错价实锤。
⇒ **新规则**：① 只引用 `/Katalog/Urun/Detay/...`（带 `产品码-K供应商码` + 供应商全称 + 合同起止）；② 聚合页（`/Arama`、`/EMagaza`）只找型号不取价；③ 同型号 3 倍以上价差 ⇒ 先怀疑串价再怀疑僵尸码。
⇒ **r76 的 `IS108GPS-2F / IS104GPS-2F / S5700-*` 区间价全部降级为「待详情页核实」，不得对外引用。**

### 二、⭐⭐⭐ FOREDGE 的 DMO 主体 = **FS GRUP BİLİŞİM LTD. ŞTİ.（K4702）**，合同 **2024-10-21 → 2026-10-21（有效）**
- 详情页 `Tedavikçi` 字段 = **FS GRUP**，不是 Han；**一个 K 码覆盖 FOREDGE + MILESIGHT + AXXON 共 44 个产品**；联系 **0555 685 6157**，总机 **0312 473 32 00**，Faks 473 32 01，Cevizlidere 1243. Sk. No:6/4 Öveçler/Çankaya/Ankara。
- 已核实单价：**`AI8024` 21,401.50 ₺（产品码 119852）**；`AI2010GX` 29,036.10–32,102.24 ₺（聚合，待核实）。
- **MILESIGHT 还有两个码：OMSİS TEKNOLOJİ `K4141`（2023-08-25→2025-08-25 已到期）与 `K2831`。**
⇒ **判读**：Han 是工厂/品牌端，**FS Grup 是目录端且无工厂** ⇒ **替换上游成本 ≈ 0** ⇒ 最易撬开的一道门；**合同 2026-10 到期，目录申报窗口就在眼前**。

### 三、⭐⭐ RUBISEC 完整价格阶梯（经销 USD / 零售 TL / DMO TL）
`RS-ES-100-10GP` **$279** · `RS-ES-100-28GP` **$559** · `RS-ES-200-28GS` **$829** · **`RS-ES-300-28GPX`（24×GbE PoE+ + 4×1/10G SFP+）$969 / 零售 42,000 ₺≈$840 / DMO 38,973.49 ₺≈$779** · `RS-ES-300-52GPX` **$1,179**（零售 29,900 ₺ ⚠ 低于 28 口，疑错价）· `RS-ES-400-28GSX` **$1,380** · `RS-ES-400-28GTSX` $12,000 ⚠ · `RS-ES-350-28GPX` $3,700 · `RS-ES-350-54GPX` $6,600。
⇒ **渠道 = Birkil Savunma（`birkilsavunma.com`，用 USD 报价的军工/安防渠道）** —— 新线索。
⇒ **一台 24 口千兆 PoE+ 受管在土耳其能站住 $779–969**，我方同类 FOB 量级 $120–150。

### 四、⭐⭐ DMO 工业 8 口「详情页可信价」全段：$167 → $2,315
**PLANET `IGS-801T`（非 PoE）8,346.59 ₺≈$167** → **DAHUA `DH-PFSC28GT1-120D`（8×GbE PoE + 2 SFP，非受管，−30~65 ℃，120 W）18,993.83 ₺≈$380（含税 22,792.60，KDV 20%）** / 另一店 **AKTİF GRUP `K4969` 22,586.84 ₺** → **DAHUA `DH-PFSD216ET2-240D`（16 口 240 W 受管）15,215.40–23,274.13 ₺≈$304–465** → **ALCATEL `OS6465T-P12-EU` 65,342–66,451 ₺** → **CISCO `IE-3300-8P2S-E`（4S BİLİŞİM `K4427`）115,787.25 ₺≈$2,315**。
⇒ **r76 的「$898–1,155」作废**；**DMO 工业 8 口的真实带 = $380（Dahua 白牌）→ $2,315（Cisco）**，FOREDGE 的 $898–1,155 是「国牌 + 240 W + 服务」的位置。

### 五、⭐ GSL 311 的真实构成：**受管 119 + 非受管 112 + 其余约 80**
第 3 页抽样过半是 **SFP 模块**（`SFP-1G40ALC-T`、`1G20BLC`、`1G10ALC`、`1FELLC-T` 80 km）与 **`RK-4U` 机架件、`ADP-SCm-STf-*` 光接头**。
⇒ **GSL 真正在卖的交换机 = 231 款**，「311」不能当竞争规模；**但 SFP + 配件是它的黏客层，我方 SFP 价格对就能插进去。**

### 六、⭐ Angora Networks 不在 DMO（`VERGE` / 公司名 零命中）
⇒ 走直销 + 集成商 + 项目标，不进政府目录 ⇒ **「你不进 DMO，是因为你没有一条能撑住目录价的产线」**；也可反向提案「帮你把 8 口段做成能报 DMO 的成本结构」。⚠ 也可能以关联主体在册，未穷举。

### 七、⭐ 渠道商名录累积 14 家 K 码
**K291** Telkolink(CLR) · **K2757** ASIR · **K2831/K4141** OMSİS · **K2887** TeleOne(僵尸) · **K3193/K4329** İNFOGEN(D-Link) · **K3922** ALE 渠道 · **K4051/K5041** VOLGA(IDIS) · **K4385** RİVO(GWSECU) · **K4427** 4S BİLİŞİM(Cisco) · **K4702** FS GRUP · **K4716** NETCOM(Huawei) · **K4969** AKTİF GRUP(DAHUA) · **K6285** PİNET(i-PRO)
⇒ **每一行都是「有 K 码、没工厂」的潜在客户。**

### 八、⭐ Cenova 的三个交换机牌 / OEM 上游排表
`Cenova CN-` + **`Dayzip DZ-`**（`DZ-PS204D/PS208G/PS308G/GS108/GS116/POE103S/POE105S/GPS424`）+ **`DL-`**（`DL-3308P/DL-3316PF`）；**`Dayzip` 无工厂痕迹 ⇒ 疑深圳厂 ODM 牌，是 A 级客户的入场券（r78 首要）。**
OEM 11 家里**只有 2 家上游可点名**：**Telkolink → TG-NET**（强）· **Han/FOREDGE → 深圳未定名工厂**（中）；其余 9 家空白。

### 九、产出
- 新增 `08-customer-pipeline/146-dmo-price-bleed-and-rubisec-ladder-2026-11-06.md`。
- 新增 `r77_appendix_data.py`（键 `'1' '8' '9' '22' '62'`），builder 已接入 `R77` + `R77_MARK` + emit 块。
- 根 `README.md` 增 `146` 链接；本 ledger 增 §71；`AGENT-README` 增行 77；`00-TASK-STATUS.md` 增 CI 行 + 待办 58。

### 十、方法与诚实边界
**新方法**：① **DMO 定价必须三层校验**（详情页 → 同型号跨供应商 → 同型号跨时间）；② **`Tedarikçi` 字段才是「谁在卖」，品牌名不是** —— 这一步把 r76 的「Han 在 DMO」改成「Han 的牌由 FS Grup 挂」；③ **一个 K 码覆盖多品牌 ⇒ 纯目录商**，这是最容易替换上游的一类客户。
**诚实边界**：r76 的 FOREDGE 区间价未回详情页 · Han 自己是否有 K 码未查 · **RUBISEC 的 K4525/K6355 合同期仍未取得（技术债自 r44）** · `Dayzip` 真实工厂未知 · TG-NET 实体未知 · Asya/ISEE 的 5 家供应商未取 · GSL 剩余约 80 个「其余」未分类 · **所有电话未试拨**（新增 AKTİF GRUP 0312 284 64 14 / RİVO 0533 658 73 12 / FS Grup 0555 685 61 57）。

---

## §70 · 第 76 轮 — 2026-11-06 ≈21:30–01:30 (+0800)：**DMO 反查方法成立（供应商 K 码 → 型号 → 单价 → 合同）** / **8 口工业千兆 PoE 在 DMO 卖 $898–1,155（FOREDGE）** / **土耳其本土交换机厂 Angora Networks** / **XPS = 台北 XPcable Group（推翻 ONV 贴牌说）** / **BDCOM 是 Öncü 独家**

用户第 29 次「继续」。本轮换招：不再一家一家搜，而是用 **DMO 公开目录**做价格与渠道反查。

### 一、⭐⭐⭐ DMO 反查方法（本轮方法论突破）
**DMO 产品页 URL = `/Katalog/Urun/Detay/{供应商ID}_{产品ID}`，正文含 `产品码-K供应商码`、单价（+Vergiler）、含税价、合同起止、供应商全称。** ⇒ 只要知道 K 码，就能翻出「这家在政府渠道卖什么、卖多少钱、合同有没有过期」。
**本轮拿到 4 个 K 码**：**TeleOne = K2887** · **Telkolink/GelecekBT = K291** · **FS Grup Bilişim = K4702** · **Han Elektronik 的 FOREDGE 走多家供应商（含 K4702）**。

### 二、⭐⭐⭐ TeleOne 的 K2887 是僵尸码
合同 **2021-09-09 → 2023-09-09**（已过期两年），页面状态「temin edilememektedir（无法供货）」。产品：**`BRICKCOM PS-7242IL-AT` 24 口 10/100 PoE+ Web Smart 交换机 14,645.16 ₺（≈$293）** · `NR-8232-RM-D` 32 路 NVR **39,501.00 ₺**（含税 46,611.18，KDV 18%）· `OB-H200NP-WDRPRO-H265` 枪机 **10,534.01 ₺**（含税 12,430.13）· `VD-300NP-VIA` 半球 · `LANDE LN-SBO-IP5509U6060-LG` 室外机柜 **5,088.39 ₺**。\$⇒ **修正 r75**：「2014 起进 DMO、自述前三」给人「现在仍在册」的印象 —— **实际最后一个可见合同 2023-09-09 已到期，它是历史玩家。**
⇒ **判读**：它**确实卖过交换机**（BRICKCOM，台湾，型号老：10/100 + Web Smart）⇒ **DMO 目录里没有一台「千兆 + 802.3at + 工业」的 TeleOne 货，这一格是空的。** 第一句就问：「你的 DMO 合同 2023 年 9 月就到期了，新一期准备放什么型号？」

### 三、⭐⭐⭐ Telkolink / GelecekBT 的 K291 是活目录
**目录文件标题即 `DMO ÜRÜN KATALOĞU -K291`**，DMO 批准 **2018-08-03，文号 55238**。进目录的 **CLR 自有型号**：`CLR-SW-811P` · `CLR-SWG-822P` · `CLR-SWG-1621P` · `CLR-SWF-2422P` · `CLR-IES-G42P`（4×GbE+2 SFP 工业非受管 PoE）· `CLR-IES-G82P`（8×GbE PoE+2 SFP 工业非受管）· `CLR-IES-G802P`（8 PoE+2 SFP **受管**）· `CLR-IES-G824P`（14 口受管）· **`CLR-IES-T884P`（DIN 导轨 24 口 10G L2+ 骨干 PoE）** · `CLR-SWG-28`（8 SFP + 2 GbE 骨干）· `CLR-SWT-4244`（光纤骨干 L2+）· `CLR-FXS/FXO` 电话光端机 · `CLR-VTR` 视频光端机 · `CLR-MCT-SFP+` 10G 转换器 · `CLR-PSE-100` PoE 注入器。
**⭐ 底牌**：同一份目录里并列出现 **`TG-NET`** 的 PoE 交换机（`P3010M-8POE` 150 W、`P3018M-16POE` 300 W、`P1000` 系列、`S5500` L3 骨干）⇒ **TG-NET（中国 ODM）= CLR 的上游。** 另有一本 **`IEC61850 Ethernet switch`** 目录 ⇒ 它已能做电力标。
⇒ **话术**：「TG-NET 那条线，我给你换一代：千兆 PoE + 802.3bt + 环网 G.8032，规格直接进你 K291 的下一版。」

### 四、⭐⭐⭐ 价格伞硬数：8 口工业千兆 PoE 在 DMO 卖 $898–1,155
**FOREDGE（Han 自有品牌）在 DMO 有 10 个型号**（产品码段 119852–119881，多家供应商挂价，同型号价差最高 **28.6%**，`AI8024` 甚至 **126%**）：`IS108GPS-2F`（工业 8×GbE + 2 SFP，240 W）**44,928.91–57,784.04 ₺ ≈ $898–1,155** · `IS104GPS-2F`（4 口，120 W）**34,944.71–44,943.14 ₺** · `S5700-24GP-4TFR`（24×GbE PoE 360 W + 4×10G）62,401–80,256 ₺ · `S5700-48GP-4TFR` 84,866–109,148 ₺ · `S5700-24F-8G-4TF` 104,834–134,829 ₺ · `AI2010GX` 29,036–32,102 ₺ · `AI8024` 25,682–58,072 ₺ · `AI1016GC` 43,554–48,153 ₺ · `AI1024GC` 58,072–64,204 ₺ · `PS2024GR` 70,625 ₺。
**地板价参照**：**PLANET `IGS-801T`（8 口工业非 PoE）8,346.59 ₺ ≈ $167** · D-LINK `DGS-3000-52X` 35,179.47 ₺（KDV 20%）· HPE `JG932A`（5130 24G）19,993.19 ₺（KDV 18%）· HUAWEI `S5735-L48T4XE-A-V2` 65,946.95 ₺（NETCOM K4716）。
⇒ **DMO 的「工业 8 口」价格带 $167 → $1,155，我们在中间，空间极大。28.6% 的价差不是成本差，是渠道差。**

### 五、⭐⭐ 新渠道样本：FS Grup Bilişim（K4702）
**2017** 成立 · **Cevizlidere Mah. 1243. Sok. No:6/4, Öveçler / Çankaya / Ankara** · **0312 473 32 00**（Faks 473 32 01）· `fsgrup.com.tr`。DMO 目录 **44 个产品**：**FOREDGE 全部交换机**（`119853-K4702`…`119881-K4702`）+ **MILESIGHT** 摄像机/VMS + **AXXON** 视频软件。⇒ **不碰工厂、只碰目录，是 Han 的下游。要找的不是它，是它上游的工厂。**

### 六、⭐⭐⭐ 土耳其有自己的交换机厂：Angora Networks
**ANGORA NETWORKS BİLİŞİM TEKNOLOJİ TİCARET SANAYİ ANONİM ŞİRKETİ**，**2016-11-28** 成立（NACE 620902）。销售 **Nergiz Sok. No:7 K:3 Via Flat / Plaza Cubes, Söğütözü / Ankara 06560**；**制造 Çamlıca Mah. Anadolu Blv. Timko Sk. Z Blok No:20/1, Yenimahalle / Ankara 06200**；注册 Alacaatlı Mah. Park Cad. 47/31 Yenimahalle。**+90 312 241 77 47**，`sales@angoranetworks.com`，**10–50 人**。口号 **「Yerli Akıl, Küresel Teknoloji」**。产品：**VERGE 交换机家族**（8/24/32/48×GbE + 4×10G 光纤骨干，受管）· SFP 模块 · 瘦客户机 · **数据二极管「Arrow」（支持 ModBUS / OPC）** · WiFi/VoIP · **PacketFence NAC 集成**。官网自述「Turkey's network equipment manufacturer」「a disruptive Turkish manufacturer」。
⇒ **三种可能都成立**：① 对手（「本土制造商」是 DMO 供应商 A/B/C/D 评级里的加分项）；② **OEM 客户**（10–50 人不可能自建 SMT 线，VERGE 大概率台/陆 ODM 贴牌）；③ 合作者（数据二极管方案需配套工业交换）。第一句：「VERGE 现在在哪家工厂做？8 口工业那一段我给你补上，贴 VERGE 的牌。」

### 七、⭐⭐ 两条身份订正
**🛑 `XPS Active Systems` = XPcable Group（台北）**，推翻 r73 的「= ONV 贴牌」。证据：产品 PDF 页脚 **`XPcable Group · 11F, 51 HENGYANG ROAD, 100 TAIPEI, TAIWAN, R.O.C. · info@xpcable.com`**；XPCABLE（布线）与 XPS（交换机）同一集团，ErETE 同时代理。型号：`XPS-1220-18`（16×GbE+2 SFP，30 W）· `XPS-1220-28P`（24 PoE+4 SFP，**400 W**）· `XPS-1220-10P` · `XPS-I7100-4/6/10` · `XPS-I7120-6P/10P/14/14P`（8 PoE，**240 W**，**G.8032 ERPS**）/24/24P · `XPS-I8120-24F/24PF`（+4×10G）。**交期 4–6 周**；ErETE 有 **~200 家「Yetkili Sistem Kurucu」**。
**⭐ BDCOM 在土耳其是「独家」**：`bdcom.com.tr` 原文「**Öncü Güvenlik, BDCOM'un Türkiye'deki exclusive distribütörüdür**」，站内 22 个 switch 型号（`S2900-8T4X` 等）⇒ **$399 是独家代理价，不是市场价；对着它的零售价打，差价远大于我方成本优势。**

### 八、⭐ 靶型与路线
**Sec-on `SC-E208-4FH` 完整规格**：**8×GbE PoE + 4×GbE SFP · L2+ 受管 · 240 W · −40~+75 ℃（电源除外）**；第二渠道 **ASR Teknoloji / ASR Güvenlik Teknolojileri A.Ş.**。⇒ **这就是我们的靶型**；差异点 = **它「电源除外」，我方整机 −40~75 ℃。**
**路线补站**：**İzmir 路线 B 加 BİMEL（İzmir 分部 0232 489 0755；İstanbul 0212 347 7540）**；**新路线 C · 安卡拉一天：Angora Networks（Söğütözü 销售 + Yenimahalle 工厂）+ GSL（İlkbahar Mah. 612. Cd. No:9）+ FS Grup（Cevizlidere 1243. Sk. No:6/4）**，三站互距 15 分钟。

### 九、⭐ OEM 客户池正式成表（11 家）
**Angora Networks（VERGE）· Asya Telekom/ISEE · HAN（FOREDGE/VIDEOPARK/SPY/AVer/M-Sight）· Telkolink（CLR，上游 TG-NET）· Nokta（upTech）· Öncü（Sec-on）· Lansan（LNS-）· Karer（KR-*）· Snexus（SN-）· Cenova（SWP/DL）· Novacom（NVC-）**。
⇒ **11 家里 10 家「有牌没厂」，只有 Angora 声称有厂（且只有 10–50 人）。**

### 十、GSL 目录进度 56/311
家族结构已明：**Moxa** `EDS-205/208/208A/308/316/2005-ELP/2008-ELP/P206A-4PoE` + `EOM-104` 模块；**Kyland** `Opal5/5L/5-E`、`Opal8/8L/8-E-2S6T`、`SICOM3000A-8T/16T/2SFP8T/2GX8GE/2GX8T`、`SICOM3000A-LITE-2S6T-SC40/ST40`、`SICOM3000S-4GX8P`（IEEE1588）、`SICOM3307S-3G7P`、`KIEN1009-3M6T-SC05`、`KIEN7009-2S6T-SDSC40`；**SFP** `SFP-1GSXLC/1GLXLC-T/1GLSXLC/1FESLC-T/1FEMLC-T`。⇒ **Kyland 的 Opal 系列（5/8 口非受管）是它最便宜、也最易被打穿的一层。**

**诚实边界**：**GSL 只剩 255/311 未抓** · FOREDGE 完整供应商名单未取 · **TeleOne 是否已续签新 K 码未知** · **Angora 的工厂是组装还是贴牌、DMO K 码未知** · CLR↔TG-NET 贴牌关系未证 · K2887 合同金额与年销量未取 · **所有电话仍未试拨**。

## §69 · 第 75 轮 — 2026-11-06 ≈17:00–21:30 (+0800)：**两条品牌标签修正（Ekosinerji = 中压柜厂 / Tipro = 斯洛文尼亚）** / **GSL = Moxa 阵营旗手（1988，2003 起 Moxa，311 SKU）** / **白牌层 9 家自有品牌（Asya/ISEE · Han · Lansan …）** / **Perpa B K:8 一层 8 家** / **İzmir 一天路线**

用户第 28 次「继续」，并要求拉长每轮工时 ⇒ 本轮改为「先拉线再补点」：先找**谁在贴牌**，再回头修标签。

### 一、🛑 两条修正（会直接影响话术对象）
**`Ekosinerji` 不是工业交换机品牌**：法定 **EKOS Teknoloji ve Elektrik A.Ş.**（原 Ekosinerji Elektrik San. ve Tic. A.Ş.，BİST **EKOS**），EKOS GROUP 五家公司（含 **Tuzla 自由区** EKOSinerji Dış Tic. 与突尼斯/加拿大公司）。**2000** 成立，集团自述 80 年代初以电气材料批发 + EPC 起家。地址：**Balıkesir OSB 17-19**（总部/工厂）· **Gebze İstasyon Mah. Güney Yanyol Cd. No:78** · **İstinye Ressam Hikmet Onat Sk. No:9**；**0262 656 47 67**。**101–250 人**，营收 **$7.6–7.8M**（多源不一）。董事长 **Tarık Akbaş**，GM **Memduh Birbilen**，供应链总监 **Mehmet Eryılmaz**。产品 = **中压空气绝缘/气体绝缘柜、RMU、重合器、分段器、负荷开关、真空断路器、水泥箱变（半地下式土耳其首家）、保护控制继电器、RTU、变电站自动化、NTP-PTP 时间服务器（EKOSync 1588）、GE 配电产品**；自述「**土耳其 GIS 第一家也是最大一家**」，出口 70%。⇒ **它是变电站集成商 = ODM 客户（要 IEC 61850-3 交换机 + PTP），不是竞品。** GSL 的 Moxa 项目里就写着「Moxa PT-7528 + **EKOS Electric EKOSync 1588**」。
**`Tipro` 不是土耳其品牌**：**Tipro d.o.o.（斯洛文尼亚/卢布尔雅那）**，模块化工业键盘 + 触摸终端（BeFREE 20/22、FREE/FREE+ 模块、工业键盘、听筒、对讲模块），用于轨交/空管 dispatch/安防/医疗/工厂自动化/零售/酒店/停车场。**土耳其代理 = GSL，2018 起。不做以太网交换机。** 误导来源 = `toptanbilgisayar.net/kategori/endustriyel-ethernet` 把「货架上出现的名字」当「生产商」。

### 二、⭐⭐⭐ 新对手：GSL Mühendislik
**GSL Mühendislik Sanayi ve Ticaret A.Ş.**，**1988 年 5 月安卡拉**成立（38 年）。**İlkbahar Mah. 612. Cadde No:9, Çankaya/Ankara 06550**；**0312 473 3540**（Faks 3544），`info@gsl.com.tr`。安卡拉 + 伊斯坦布尔办公室，**25–49 人**。代理 **Moxa（2003 起，21 年+）· Kyland · Robustel · Digi · Tipro（2018 起）· Pro Optix · RuggON · Transcend · TXOne**，历史含 EKOS。线上店 `store.gsl.com.tr`：工业以太网 **311 SKU / 受管 119**，品牌计数 **MOXA 363 · Kyland 27 · Meanwell 8 · Pro Optix 7**。**自己做 FAT**（Kyland 交换机在安卡拉办公室完成 FAT）、办认证工业网络培训、TSE+ISO 认证技术服务。
⇒ **价格伞**：Moxa `EDS-208-M-SC`（10/100 8 口 + 1 光口）**RS Türkiye 13,988.58 TL 未税（≈$280）**；`EDS-208A-T`（−40~75 ℃）美国挂牌 **$278.58**；`EDS-208A-MM-ST` RS Türkiye **26,091 TL 未税（≈$521）** ⇒ **土耳其「8 口工业非受管」心理价位 $280–520**。
⇒ **唯一切口**：「Moxa 的标你继续报 Moxa；报不下来的标，用我的线兜底 —— 不冲突、不抢代理权。」

### 三、⭐⭐⭐ 白牌层（OEM 池）—— 比代理层更肥
**Asya Telekomünikasyon ve Net Güvenlik Sistemleri San. Tic. Ltd. Şti.**（新）**1995-12-27**，İTO 注册；总部 **Mehmet Akif Mah. Öztekin Cad. No:18 Asya Plaza Ümraniye 34774**；**批发点 Perpa B Blok Kat 7-8-9 No:908（KIRMIZI HAT，入口 K:7）**；Bostancı 分点 (0216) 573 23 43；**0850 433 27 92**；11–50 人；决策人 **Baysal Günel · Serkan Ur · Harun Baştürk**。**自有品牌 ISEE**（官网：「ISEE marka NVR/DVR cihazları firmamızın ürünüdür」）。**贸易实据：132 批进口 / 5 家供应商**（HS 8529.90.92 / 8522.90.00）。ISEE 交换机仅 3 型：`ISS-2006P`（4 口 PoE 78 W + 2 上行，250 m 主动 PoE）、`ISS-1026P`（24 口 400 W + 2×GbE）、`ISS-1040`（28×1G SFP + 4×10G + 12×GbE）。在售还含 Hikvision/Haikon·Dahua·Neutron·Bulwark·Vguard·Karel·Bosch·Honeywell·Samsung。⇒ **全表最像 OEM 客户的一家**。
**HAN ELEKTRONİK Bilgisayar ve Güvenlik Sistemleri A.Ş.**（订正：档案原写「Hane」）：**2000**，51–200 人，**Mehmet Akif Mah. Bahariye Cad. (Basın Ekspres Yolu) 1904 Sok. No:15/A Küçükçekmece**，**444 1 426**，`info@hanelektronik.com`。自由区同名主体 **HANE ELEKTRONİK SAN. VE TİC. LTD. ŞTİ.**（İst. End. ve Tic. Serbest Bölgesi, Aydınlı SB Mah. Atatürk Cd. No:15 Tuzla）。**自有商标 5 组**：Han 商标注册证 · **FOREDGE 分销证** · **VIDEOPARK** · **SPY/AHD/IP/Mobile/Alarm/Network Solution** · **AVerFire/AVerGuard/AVerSound** · **M-Sight**（金属探测门/X 光）；ISO 9001 · ISO 10002 · TS-12540。独家：**MILESIGHT 土耳其唯一授权 + 其土耳其办事处**（2018 最高增值+最快成长、**2023 最有价值伙伴**）· **UNIWIZ 唯一** · Panasonic 可寻址消防 · AXXON/Hoop Cam · Honeywell · TNA · AlienFence · **Shelly** · GRUNDIG · Nevio · Monitoreal。**中国线：Ruijie + Reyee**。⇒ **已有两层中国供应链（OEM 白牌 + 品牌代理）⇒ 要的是「换掉现在那个深圳工厂」。**
**LANSAN TEKNOLOJİ A.Ş.**：**2019-12-04**；**Perpa B Blok No:1/1 İç Kapı No:989**（另址 Work Plaza Başakşehir）；0212 955 02 30 / 0312 955 02 00；自有 **LNS-** 全线。**官网标价：LNS-1310P 8 口 PoE $1,000 / LNS-1324P 24 口 $1,427 / LNS-1306-P 6 口 $242 / LNS-1308 8 口 SFP 骨干 $1,755**。⚠ `find.com.tr` 的 MERSİS `1234567890123456` 与 E-tebligat `12345-67890-12345` 是占位假号，不可引用。

### 四、⭐⭐ 邻类三家（各一句）
**ErETE**：法定 **ERETE BİLGİ SİS. DIŞ TİC. VE SAN. LTD. ŞTİ.**，2001-12 成立，创始人 **Pınar Kabil · Murat Soyak · Timur Yıldız**；**19 Mayıs Mah. Güven Sok. No:4/2 Şişli**；**0212 212 81 03**；`erete@erete.com.tr`，GM **Murat Soyak**。**据点 = 伊斯坦布尔 + 台湾**。代理 **EDGE-CORE（Accton）+ ETHERWAN + VOSCOM + XPCABLE（EGM 认证）+ XPS Active System**；B2B 平台 **`eretekne.com`**（= 它自己的店，非独立公司）；**「Erete Network Okulu」** 每月培训出证（土耳其首创）；美国多州交通信号 + 土耳其 MOBESE 用 EtherWan hardened。⇒ **台系价格，纯价格标打不动；切口 =「EtherWan 同防护等级低一档」或「XPS 那条线我给你做 OEM」。** ⚠ `XPS` 身份仍未定（自有 vs ONV 贴牌）。
**RF Teknoloji Makine ve Otomasyon San. Tic. Ltd. Şti.**：2012；**Tevfik Bey Mah. Şehit Adem Tamrak Sok. No:2/5 Sefaköy/Küçükçekmece**；**0212 210 95 65**；CalAmp 土耳其代表 + 3OneData 工业线 13 SKU；RF 数据电台/4G/CNC 控制单元/Smart Grid 网关。⇒ **卖「无线回传 + 杆上 PoE 交换一体箱」。**
**iotsistem ≠ iosistem**：`iotsistem.com` = IoT Sistem（自有 **MLB-E4xxx** 工业受管/非受管、USR IoT 土耳其官方分销 Bosgem）；`iosistem.com.tr` = **IOSistem Endüstriyel Teknolojiler**（**Ataşehir İnönü Mh. Kayışdağı Cd. No:128 Kandiş İş Mrk. K:1**，**0216 577 66 82**，2023，2 人，CTO **Emre Anayurtlu**，做 SCADA/TEİAŞ RTU/EDAŞ RTU/轨交 SDH-PDH/PAX/数据中心能耗）。**两家绝不能合并。**

### 五、⭐⭐ Perpa B Blok K:8 名册（一层 8 家，4 家是客户）
**B 836** CCTV Depo · **B 902-904** Cenova · **B 906-907** Nokta · **B 908（K:7-8-9）** Asya Telekom/ISEE ⭐ · **B 989** Lansan ⭐ · **B 1105** Perpa Otomasyon/Sanpa Elektronik（1988，测试测量，0212 912 36 86） · **B 1246** Perpa Kameram · **B 1276** ALM Elektronik（switch/AP/PBX/摄像头/消防，0212 210 02 03）。
⇒ 电梯上 **A K:5 No:295（GelecekBT/Telkolink）+ No:419（Güvenlik Toptancım）→ A K:8 No:841（Nokta 二号店）+ No:808-810/940（Koza）**。**半天 8 家，4 家有档案。**

### 六、⭐⭐ İzmir 一天路线
**① Folkart Towers（CCS 总部/展厅，Adalet Mh. Manas Blv. No:39 K:2511 Bayraklı）→ ② Halkapınar 1442 Sk. Tesisat İş Merkezi No:1/L（CCS 法定 İşyeri Adresi + 仓库）→ ③ 1443 Sk. No:3/A 旧址 + GIDA ÇARŞISI（1201–1443 sokak 整片电气/电子批发）→ ④ Mithatpaşa Cd. No:146 Zafet Apt. K:1 D:2-3（TeleOne 800 m²）**；四站互距 1.5–5 km。可选 ⑤ **Manisa Yunusemre 75. Yıl Mah. 5391. Sok. No:41**（CCS 点，0533 272 31 91）。

### 七、两条工商级修正
**CCS**：法定 İşyeri Adresi **Halkapınar 1442 Sk. Tesisat İş Merkezi No:1 L Konak 35170**（VKN 变更：旧 1443 Sk. No:3 A → 新）。规模第三源：zoominfo **283 人 / $10–25M**（同站另处 250–499 / $15.6M），rocketreach 3 人 ⇒ 区间「中型，≥50 人可信」。**「İzmir'in en büyük dağıtıcısı」是自我宣称。**
**TeleOne**：法定 **TELEONE BİLGİ VE İLETİŞİM HİZMETLERİ SAN. VE TİC. LTD. ŞTİ.**，**VKN 8370410675**，**Yeşiltepe Mh. M.Paşa Cd. No:146 Konak**。**法人成立 2003-10-06（1999 是品牌史）**，税务开始 2009-01-22。**代理 = Brickcom · Nuuo · Digital Watchdog**（r74 空白已补）。**2014 起进 DMO，自述 DMO 本领域最大前三家供应商。** TSE-HYB 2008 起 · ISO+OHSAS 2008 起 · Bilişim 500 两次 · 2016 全球最佳突破 Brickcom 分销商。NACE 由「安防服务」改为「**计算机编程**」⇒ 重心转向软件。**0850 221 95 95 / (0232) 425 50 53。**

### 八、顺手修正两条
**Öncü 有 BDCOM**：官网在售 `IES200-V25-4S2T8P`（8 口受管 PoE 工业）、`IES200-V25-4S10T`（10 口受管）、`IES2000-TW8S8P`，另有自有 **Sec-on `SC-E208-4FH`** ⇒ **BDCOM 在土耳其已有正式代理，$399 锚价是「本地可比」不是海外参考。报价对 Öncü 的 BDCOM，不对 Moxa。**
**`upTech` = Nokta 自有品牌**（官网 JSON-LD `brand: upTech, manufacturer: Nokta Elektronik`）⇒ 推翻「upTech 是中系品牌」。**Nokta 在售 13 品牌含 Edge-Core · Planet · Oring · Ruijie** ⇒ 不能打「你缺工业」，只能打「**upTech 的工厂换我**」。

**诚实边界**：**Asya Telekom 的 5 家供应商未取到**（需付费贸易数据）· **`XPS Active System` 身份未定** · **EKOS 的 IEC 61850-3 交换机来源未取到** · **`Lansan` 真 VKN/MERSİS 未取到**（公开页是假号）· **FOREDGE 代工厂未定** · **Ekosinerji→EKOS 更名日期未取到** · **İzmir Gıda Çarşısı 未逐家建档** · **所有电话仍未试拨** · **DMO K 码仍未反查（TeleOne 最值得查）**。

## §68 · 第 74 轮 — 2026-11-06 ≈13:30–17:00 (+0800)：**Koptek = DCN(2010) + Dongwe(2010) + ONV(2020) 三条中国线** / **Portel = CTC Union 车载·轨交（E-Mark / EN50155 / ITxPT）** / **伊兹密尔第二极：CCS(VKN 2030341121) + TeleOne**

用户第 27 次「继续」，执行 r73 定的两项第一优先。

### 一、🛑 `Koptek` 不缺交换机 —— 它已经代理三家中国品牌
**DCN / Digital China Network（DC Yunke，2000 年从联想集团分出）**：**2010 年起代理**；骨干 **15 Tbps / 512×1G/10G / MPLS / 4–16 槽**、数据中心、L2/L3、无线控制器、AP、防火墙；全系 **DCNOS** + 硬件 IPv6 Ready；**L3/PoE 型号 5 年保修**。在售：`S4600-28P-P-SI`（24×GE+4×SFP，370 W PoE，4 kV 防雷，无风扇）· `S5750E-52X-P-SI(R2)`（48×GE PoE+ 740 W，L3+，4×10G）· `CS6200-28X-P-EI`（24 PoE 340 W）· `CS6200-52X-P-EI`（48 PoE 740 W + 2×20G 堆叠）· **`IS2100D(R2)` 工业（IP40，−40~+85 ℃）**。
**Dongwe**：2010 年起，光纤转换器 + SFP（500 m–120 km）。**ONV Technologies（中国）**：2020 年起，工业与室内交换机 `POE33064PF`/`POE33108PF`/`ONV-H2108PL`/`ONV-H3016PF`/`POE33020-28-52PFM`/`POE36028PFM`/`POE56028PFM`。
**公司历史订正**：**1988 年入行、1997 年起做网络分销** ⇒ **老手，砍价能力强。**
⇒ **话术改**：不讲「我也有交换机」，讲「**你已有 DCN/ONV/Dongwe，第四条线要不要一个价格更硬的**」。⇒ **技术切口：DCN 的 PoE 型号多为外置电源，我方一体机可直接对标。**

### 二、⭐ `Portel` 的战场是「车载 / 公交 / 轨交」，不是安防
代理 **CTC Union（台湾 1993）**：`IVS-G802T-8PH24`（8×GbE PoE+ 30 W/口、120 W、**24/48 VDC 双路冗余**、**E-Mark E13**、−40~75 ℃、IP30 无风扇）· `IVS-802GT-8PH24`（8 FE PoE + 2 GbE）· `ITP-G802TM-8PH24` / `ITP-802GT-8PH24`（**EN50155 + M12**，抗冲击震动）· `ITP-800A-8PH24` · `ICR-GW404`/`ICR-W401`（4G/WiFi 车载路由）。标准覆盖 **E-Mark / EN50155 / ITxPT / IEC 61850-3 / EN45545-2**。
另一条业务：**半导体 / 电子元器件供应，香港设据点** ⇒ 解释了三币种 IBAN 与「只做工业网络、不碰摄像头」。
⇒ **不要拿普通工业 8 口去谈**：要么「认证齐全 + 低于 CTC Union」，要么直接做它的**元器件供货**。

### 三、⭐ 伊兹密尔第二极
**CCS Güvenlik Sistemleri İç ve Dış Tic. Ltd. Şti.**：**Vergi No 2030341121** · **成立 2016-03-28** · 活动代码 **464308** · 总部 **Folkart Towers No:39 İç Kapı 2511 Bayraklı/İzmir** · 仓库 **Halkapınar 1442 Sk. Tesisat İş Merkezi 1/L Konak** · **(0232) 459 55 70** · `hello@ccsguvenlik.com.tr` · **2018 Q2 开 İstanbul 分店** · 代理 **Hikvision / HiLook / ZKTeco / ERSE / OPUS / AlteBox** · 产品面含 **X 光机 / 闸机 / UPS / 网络与基础设施**。
⇒ **「网络与基础设施」这一格没有交换机厂 = 第三个空货架**（与 Cenova、NFS 同型）；客户现成选项只有 Hikvision 交换机 ⇒ 我方 = 「Hikvision 之外的第二个选择」。
⚠ **规模两源严重冲突**：zoominfo 250–499 人 / $15.6M vs rocketreach 3 人 ⇒ 只可信「中型以上」。
**TeleOne**（1999，Konak Mithatpaşa Cd. No:146，**800 m² 总部 + Ankara 区域经理部**，<25 人，<$5M）：Video İzleme / Analiz / Networking / 指挥控制中心 / 远程监控的「360° 总方案」，覆盖公共机构；自述「多家品牌土耳其分销商」但**品牌名单未公开** ⇒ 卖点应为「能进标书的规格 + 本地服务」。

### 四、土工业交换机生态（对标清单）
国际/台系：**CTC Union · Moxa · Kyland · Planet · Edge-Core · Oring · Robustel · Digi · Advantech · Siemens · Weidmüller · Phoenix Contact · Harting**；中系：**DCN · ONV · Ruijie · upTech · RUBISEC**；**土本地：Ekosinerji · Tipro（+ RUBISEC 深度本地化）**。
⇒ **「中国货没人要」不成立；「没好渠道」才是真问题。**

### 五、三类客户三句话（定稿）
**缺品类**（Cenova · NFS · CCS · Okisan · Koza）→「你的品牌表里没有一家交换机厂 —— 这一格我给你。」
**已有中国线缺第四条**（Koptek · Nokta · CCTV Depo）→「你已有 DCN/ONV/Dongwe/Ruijie，第四条线要不要一个价格更硬的？」
**垂直场景**（Portel 车载轨交 · Rima 项目集成 · TeleOne 政府总包）→「我不跟你比通用型号，我按你的标准做：E-Mark / EN50155 / 标书规格。」

**诚实边界**：Koptek / Portel / TeleOne / CCS 的**税号与 MERSİS 多数未取到**（仅 CCS 有 VKN）· **CCS 员工数两源冲突** · **TeleOne 品牌名单未公开** · **Portel 除 CTC Union 外的代理未穷举** · **Ekosinerji / Tipro 未建档** · 本轮仍未试拨任何电话。

## §67 · 第 73 轮 — 2026-11-06 ≈09:50–13:20 (+0800)：**10 张 B 级身份卡** / **Perpa K:8 一层楼 = 4 家客户** / **13 人门店也有自有 PoE 全系（Karer KR-*）** / **两类空货架**

用户第 26 次「继续」，延续 r72「只挖客户、不算我方价格」。

### 一、⭐ Perpa 客户地图（落到楼层+房号，本轮更新）
A K:2 Nokta（总部 No:1）· **A K:5 GelecekBT No:295** · **A K:5 Güvenlik Toptancım No:419（新发现，0212 220 41 88）** · **A K:8 Koza Güvenlik No:808-810-940** · A K:8 Nokta 第二门市 No:841 · **B K:8 CCTV Depo（CepDepo）No:836** · **B K:8 Cenova D:902-903-904** · **B K:8 Nokta 销售/技术 No:906-907**。
⇒ **A 座 2/5/8 层 + B 座 8 层 = 6 家客户（含 3 家 A 级），一趟电梯走完。** Pertpa B K:8 一层楼挤了 4 家客户。

### 二、⭐⭐ 最有用的新事实：13 人的门店也有自有 PoE 全系
**Karer Güvenlik**（Pendik，**2006 立、13 人、营收约 $948K、1,000 m² 仓库**）· **MERSİS 0524126788900001 · Vergi 5241267889** · 0216 397 33 88 · CEO/所有人 **Nurbaki KARATAŞ** · 代理 **Dahua / HiLook(by Hikvision) / Seagate / WD / Desi Alarm**。
自有 **`KR-*` PoE 全系**：`KR-04F2BE`（4+2 100M PoE）· `KR-08F2BE`（8+2 100M PoE）· `KR-16F2G1G`（16+2 千兆 PoE）· 24 口千兆 PoE。
⇒ **白牌不需要规模，只需要一个愿意接小单的工厂** ⇒ **我方 ODM 客户池比 A 级清单长得多。** ⚠ 该司公开投诉集中于「电话打不通、找不到对接人」⇒ **必须锁定具体人。**

### 三、两类「空货架」，话术完全不同
**A. 安防分销缺「品类」**：`Cenova`（7 品牌零交换机）· `NFS Teknoloji`（代理 **Hanwha Techwin / Pelco / Oinone / Surenix / TDSI / Identiv** 六家，**零交换机**）· `Okisan` · `Karer`（有自有 KR 但缺高配）⇒ 语言 = **「你缺这一格」**。
**B. 纯网络缺「便宜供应源」**：`Koptek`（法定名，旧档误写 Coptek；Balmumcu-Beşiktaş，0212 275 79 53；产品线 = 骨干 / Data Center / PoE / L3 / L2 / 工业 / 无线+AP 控制器 / 光纤 / SFP / 转换器，**完全不碰摄像头**）· `Portel Teknoloji A.Ş.`（Kartal，0216 464 44 50，`industrialnetworkcenter.com`，**只做工业网络**，官网公示六个 IBAN 可收 **TL/USD/EUR**）⇒ 语言 = **「同样东西我给你更低」**。

### 四、其余 B 级卡（工商级）
**CCTV Depo（CCTVDEPO Güvenlik Teknolojileri A.Ş.）**：**MERSİS 0203034849100015 · Vergi Yenibosna 4420033641 · Ticaret Sicil 70431-5 · KEP cctvdepo@hs01.kep.tr** · 主仓 Remzi Özkaya Cad. No:18 Yenibosna/Bahçelievler · Perpa 点 B K:8 No:836 · 0850 303 03 17 · **2004（自称土耳其第一家 B2B 安防平台）** · **官网直列 8 位业务员手机**（Asuman Özüdoğru 0505 018 34 32 / Mehmet Sağlam 0553 090 98 31 / Mert Yıldız 0553 966 98 32 / Volkan Alçevik 0553 089 57 33 / Şahin Elektrik 0535 973 65 19 / Sait Osanmaz 0535 973 65 21 / Tolga Topraklı 0533 271 60 12 / Seda Nur Yılmaz 0533 272 60 12）· 自述「进口 + **自有生产**」⇒ 谈成本与 SKU 数，不谈品牌故事。
**Öncü Güvenlik Sistemleri A.Ş.**：**Vergi 6560323830（Beykoz VD）· Ticaret Sicil 480061-0** · Kavacık Mah. Yayabeyi Sk. No:8 Kat:Zemin-1-2-3 Beykoz · **+90 216 537 01 23** · `info@oncuguvenlik.com.tr` · **2002 · 51–200 人 · 1,500+ 经销商 · 有 AR-GE · 做 EDS 电子监控** ⇒ 可同时谈贴牌与项目指定。
**Koza Güvenlik**：Perpa **A K:8 No:808-810-940** · 0212 220 06 04 · Faks 0212 220 11 03 · **2005** · 自述「**kendi tescilli markaları yanında aldığı distribütörlük**」（自有注册商标 + 代理）· 自有线 **Greentech** · 技术 **Deniz Aydın** ⇒ 直接谈「Greentech 的交换机线」。
**Rima Elektronik**：**1. İnönü Cad. No:18 Kat:1 Beşyol/Florya Küçükçekmece** · 0212 424 16 16 · Faks 0212 553 36 21 · GSM 0533 364 56 81 · `bilgi@rimaelektronik.com` · 成立 2000（名录称 2014 ⚠ 冲突）· **项目集成 + 年度维保**，不是分销商 ⇒ 只谈项目报价与品牌指定。
**Hane Elektronik**：**本轮三次检索未命中官网，如实记为空**（仅 `info@hanelektronik.com`）。

**诚实边界**：**`Portel` 与 `Koptek` 的代理品牌未取到（下一轮第一优先）** · `Karer KR-*` 的产地与工厂未查明 · Koza/NFS/Rima/Portel/Koptek/Hane 税号未取到 · Rima 成立年份两源冲突 · CCTV Depo 员工数三源不一致（25–49/51–200/100–200）· **所有电话邮箱未试拨未发信**。

## §66 · 第 72 轮 — 2026-11-06 ≈06:20–09:40 (+0800)：**用户转向「挖客户、不看我方价格」** / 6 家 A 级客户身份档案 / **Perpa 一栋楼 = 客户中心** / **CryptoLink `CRLISW-8P` 已拿政府 BAŞARILI 报告**

用户第 25 次指令，明确改方向：「**继续挖掘 挖这些客户的信息为主 不需要过度关注 Saga 的价格**」。本轮**不计算任何我方倍率**，只做客户工商情报。

### 一、⭐⭐ 本轮最重要：`CryptoLink` 的自有工业交换机 `CRLISW-8P` 已取得土耳其通信司「BAŞARILI（合格）」报告
KGYS C 型以太网交换机技术文件原文：「Türkiye'de hali hazırda **EXTREME NETWORK, ALLIED TELESIS, CRYPTOLINK, D-LINK** gibi çeşitli markalar **Haberleşme Daire Başkanlığı'ndan BAŞARILI raporu almış**」，并注「**Cryptolink, Extreme network, Dlink switch'ler için benzer yazılımı kullanmaktadır**」。
⇒ **土本地品牌可以拿到政府工业交换机型式认可** —— 我方 ODM 合作的**认证路径已被走通一次**；且它与 Extreme/D-Link 软件相似 ⇒ **同芯片同参考设计贴牌，认可文件可复用** ⇒ 切入语 = 「**用你的认可 + 我们的成本**」。
CryptoLink：Çankaya Mah. Bükreş Cad. No:19/1 Çankaya/Ankara · 0312 557 64 00 · `info@cryptolink.com.tr` · 业务=边境安全/网络安全/网络方案/车牌识别/信号干扰（政府项目商）。

### 二、⭐ Perpa Ticaret Merkezi = 客户中心（首次落到楼层号）
**GelecekBT** Perpa **A Blok K:5 No:295**（0212 320 4030，`bayi@gelecekbt.com`，2004，CLR Networks 土耳其**唯一**授权分销，5–10 人）· **Nokta Elektronik** Perpa **A Blok K:2 No:1**（总部）+ **B Blok K:8 No:906-907**（销售/技术）+ A Blok K8 No:841 · **Cenova** **Elektrokent B Blok K:8 D:902-903-904**（与 Nokta 同层相邻）· **Okisan** Okisan Plaza Okmeydanı（步行范围）。⇒ **一次 İstanbul 行程覆盖 4 家 A 级客户。**

### 三、Cenova：Tiandy 土耳其总代，7 个品牌里没有交换机
法人 **CENOVA BİLİŞİM TEKNOLOJİLERİ İTH. İHR. ve TİC. LTD. ŞTİ.**（**2002**）· 地址 = Perpa Elektrokent B Blok K8 D902-903-904 · `cenova.com.tr` / `info@cenova.com.tr`。
身份：**`Tianjin Tiandy Digital Technology` 土耳其授权总代** + **`GVD / Genius Vision Digital`（台湾 Taipei，2007）土耳其总代兼战略项目伙伴**。
品牌 7 个：**Cenova · Dayzip · Wisetech · Dayline · Bawcon · GVD · Tiandy** —— **全是摄像头/报警/录像，没有一个交换机** ⇒ **23 年老分销商货架上唯一的结构性缺口。**
销售部 3 人（分机+邮箱）：**Rıfat BAYDEMİR（116，总经理）`rifat@cenova.com.tr`** · **Kuntay KIZILAY（115）`kuntaykizlay@cenova.com.tr`** · **Ahmet CANCA（117）`ahmetcanca@cenova.com.tr`**。
自述：「**Uzakdoğu'da sahip olduğu üretim kanalları**」⇒ 本来就在中国做 OEM，**谈判不需翻译**。

### 四、Nokta Elektronik：数据最全的一家（含 MERSİS / 税号 / KEP）
**Nokta Elektronik ve Bilişim Sistemleri A.Ş.** · **MERSİS 0631-0730-5210-0020** · **Ticaret Sicil 555138-0** · **Vergi Şişli / 6310730521** · **KEP noktaelektronikvebilisim@hs03.kep.tr** · 电话 0212 222 87 80 / 0850 333 02 08 · `nokta@noktaelektronik.net`。
规模 **75–99 人**、营收约 **$7.5M**、**39% 员工在职 11 年以上**。自有品牌 **upTech**：土耳其专利局 **2008/13951**（2008-03-11 首注册，**续展至 2028**），**916 个 SKU**。
代理：**Dahua（官方 Distribution Partner id 203）· Oring · Amphenol · Planet · Gewiss · Edge-Core · Goldtool · ATC · Ruijie · Inno Instrument · Noyafa**。
决策层：**Harun Yazar（Vice Chairman）· Ersan Çağlar（COO/CDO）· `Casey CHEN`（Import Manager ← 进口决策人，中文名）· Mehmet Tığlı / Nefise Tugay（Sales Managers）· Kadir Babur（Marketing）**。
⇒ **它同时代理 5 个交换机品牌 ⇒ 不缺供应商，缺「能贴 upTech 标且更便宜」的那一家**；`Casey Chen` 说明**中国采购通道已存在**。

### 五、Novacom / Okisan / GelecekBT / HAFYA
**Nova Grup Mühendislik Ticaret Ltd. Şti.**（**2002**）· Öveçler Mah. 1332 Cad. No:8/1-3-5-7 Çankaya/Ankara · **0312 311 02 00** · `info@novacom.com.tr` · 网点 **Ankara + İstanbul + İzmir + Şanlıurfa + London** · 自述「ithalat firması」。产品线含 **24V Intercom PoE 交换机**（`NVC-INTSF0420FB2L`/`0820FB2L`）、**PoE Extender 1×4 Full Giga 户外**（`NVC-EBT14GW-A`）、PoE Splitter、5 口千兆、卫星 SMATV、NVR ⇒ **24V 门禁 PoE 是我方没有的品类，可「先互补后替代」**。
**Okisan Güvenlik Teknolojileri San. ve Tic. A.Ş.** · **1988-01-18 注册** · Okisan Plaza, Mahmut Şevket Paşa Mah. Odesa Bulvarı Ersan Sok. No:24 Okmeydanı/Şişli · **444 1 309** · `info@okisan.com` · 分公司 **Ankara Dikmen（Çetin Emeç Bul. Sokullu Cad. No:15/A）+ İzmir** · **44–51 人 / $8.6M / 5,000+ 经销商** · **Dahua + Tiandy 双授权** · 决策层 **Ekrem ÖZKARA（创始人/CEO）· `Okan ÖZKARA`（Business Development Director，旧档误写 Gokhan Ozkara）· Burhan ACAR（Technical Presales）** ⇒ **无 DMO 记录 = 纯渠道玩家**，销售语言改为「你 5,000 家店里卖谁的交换机？」
**GelecekBT 订正**：地址 **Perpa A-Blok K:5 No:295**（旧档 K13）、电话 **0212 320 4030**、邮箱 `bayi@gelecekbt.com`、**2004 成立**、**CLR Networks 土耳其唯一授权分销**、5–10 人（Telkolink 8 人）；人名新增 **Ebru Akdemir（Kurumsal Satış）· Sait Yıldız（Yönetici）· Bilge Birol（Satış）**。⇒ **5–10 人做 7 个站 + 全品类 = 高度依赖外部供应 ⇒ 响应速度与 MOQ 比价格更能打动它。**
**HAFYA**：Şişli，0212 221 16 72，`hafya.com.tr`，**系统集成商非分销商**（无品牌表/无团队页/无工商信息）⇒ **改做项目报价，不做代理谈判**。

### 六、结构性判断（本轮新增）
`Tianjin Tiandy` = **Cenova（总代）+ Okisan（授权分销）**；`Dahua` = **Okisan（授权分销）+ Nokta（Distribution Partner）** ⇒ **土安防分销的两大货源都是中国摄像头厂，而它们的交换机生意都让给了别人** ⇒ **交换机是这条渠道里唯一空着的货架。**
销售语言：「你们卖 Tiandy/Dahua 的摄像头，交换机靠 Dahua/Planet/Ruijie 补。**摄像头那两个牌子自己不做交换机生意 —— 这块货架上没有主人。**」

**诚实边界**：Cenova 与 Novacom 的税号/MERSİS 未取到 · CryptoLink 实控人与采购人未取到、`CRLISW-8P` 规格与产地未取到 · Okisan 的 DMO 关系仅「未找到」不排除存在 · HAFYA 只有表层 · 员工数三源不一致（44/49/51）· **所有电话邮箱均为公开页原文，未验证有效性，发信前需人工试拨**。

## §65 · 第 71 轮 — 2026-11-06 ≈03:00–06:10 (+0800)：**24 口市价地板 $278（IP-COM `G3326P-24-410W`）/ $240（`G5328P-24-410W`，470 W L3）** · **渠道活地板 $403（RUBISEC `RS-ES-200-28PS`）** · **RUBISEC = 黑山 2016 品牌，合同 K4525 至 2026-09-03** · **IP-COM 土独家代理 = NASA/Nasabil（2018-04 起）** · 2.5G 锚 $460/$1,700

用户第 24 次「继续」。清待办 51 的 ①②④。

### 一、🛑 24 口地板再降两格（第三次下修）
**市价最低**：`IP-COM G3326P-24-410W`（24×GE PoE+ **370 W** + 2 SFP，云管理）hepsiburada **13,895.15 ₺ = $278**；更低：`G5328P-24-410W`（24 PoE **470 W**，**L3**）almaluk **12,000.91 ₺ = $240**（⚠ kibristeknoloji 报 339 USD ≈17,000 ₺，**1.4 倍矛盾，待复核**）。
**渠道活地板**：`RUBISEC RS-ES-200-28PS`（24×GE PoE+ + 4 SFP，56 Gbps）DMO `122939-K6355` **20,147.89 ₺ = $403**（BİRKİL）⇒ **推翻 r69/r70 的 $513。**
⇒ **我方 $140 = 1.7–2.0×（市价）/ 2.9×（渠道）** ⇒ **r68 的 2.9 这个数字第三次出现，但这次三条不同来源都指向 2–3×，可以定稿。** ⚠ **`G5328P` 的 $240（24 口 + 470 W + L3）低于我方任何预期售价 ⇒ 24 口成本底线 FOB $120–150，我方 $140 只是持平，不是优势。**

### 二、⭐ RUBISEC 全档案解密
官网原文：「**Rubisec was founded in Montenegro in 2016**」「produces … **under its own brand**」⇒ **不是土品牌。**
DMO 通道 **BİRKİL SAVUNMA**（店 879103），两套 K 系列：**`K4525` 合同 3.07.2024–3.09.2026（有效）** / `K6355`（期未读）。
全线：`RS-IS-100-10GP` 8 口 PoE **$211** · `RS-ES-100-10GP` $234 · **`RS-ES-200-28PS` 24 口 PoE+ $403** · `RS-ES-250-10PS` 8 口 PoE+ 140 W $568 · `RS-IS-200-10GP` $702–760 · `RS-IS-300-12GP` $770–834 · **`RS-ES-300-52GPX` 48 PoE+ 600 W $858** · `RS-IS-300-12GPX` 8 PoE + 4×1/10G，**-40~+80 ℃ / IP40 DIN / 32K MAC** $1,221–1,404 · `RS-ES-500-54XQS` 48×1/10G + 2×40G + 4×40/100G 双 PSU（价未取）· **`RS-ES-750-32XQS` 核心 $18,806** · `RS-WCL-500` AP。
⇒ **战略判断**：**2016 年成立、无本土工厂的品牌，靠 K 码在 DMO 把 24 口 PoE+ 卖 $403、8 口工业卖 $1,221** ⇒ **这是我方 ODM 路径的可行性证明：路径/位置/价格带都存在，缺的是「谁去做那个品牌」。** ⚠ 官网「own production」≠ 自有工厂，**极可能中国 ODM 贴牌，供应商未查明（本轮最值钱缺口）。**

### 三、IP-COM：土耳其独家代理 = NASA Information Technologies（Nasabil），2018-04 起
IP-COM 本体：2007 成立，中国，3,500+ 员工，5 万 m² 工厂，日产 19 万台。
零售全线：`G1008` $25 · `G1024D` 24 口非 PoE **$66** · `G1016D` $19 · `G1110P-8-150W` 8 口 PoE 150 W **119 USD** · `G3310P-8-150W` $89 · `G1120P-16-250W` $133 · `F1126P-24-410W` 24×100M PoE 370 W $320 · **`G3326P-24-410W` $278** · **`G5328P-24-410W` $240** · `G3328F` $110 · `G5328F` $219–736 · `G5324-16F` $307。
⇒ **修正 r69「DMO 比零售贵」不是普遍规律**：**IP-COM `G1024D` DMO $26 vs 零售 $66（DMO 便宜 2.5×）**；`G1110P-8-150W` DMO $53–68 vs 零售 $119（便宜 1.7–2.2×）。⇒ **规则改为：有活 K 码的型号 DMO 可能更便宜；僵尸 K 码则贵得离谱。逐型号判断。**

### 四、2.5G 价格锚（服务待办 ⑤）
`TP-Link TL-SG3210XHP-M2`（**8×2.5G PoE+ 240 W + 2×10G SFP+**）Amazon.com.tr **23,000 ₺ = $460**（欧洲 €419–594）· `ZyXEL XMG1930-30`（24×2.5G L3）**€1,440 ≈ $1,700** · `CLR-MRS-8109N/8218N/8226N/8330N` **全部面议**。
⇒ **8 口 2.5G PoE+ 做到 ≈$150 即「TP-Link 三分之一价」；CLR-MRS 不报价 = 永远处在「不知道贵不贵」的劣势，可主动利用。**

**诚实边界**：`K6355` 合同期未读到（**决定 $403 是否活价**）· RUBISEC 的 ODM 供应商未查明 · `G5328P-24-410W` $240 与 339 USD 矛盾待复核 · 2.5G 土耳其本地只有 TP-Link 一家、无交叉验证 · 我方 8 口千兆 FOB 仍缺（r70 遗留）· `RS-ES-500-54XQS` 价格未取。

## §64 · 第 70 轮 — 2026-11-06 ≈23:20–02:40 (+0800)：**`JL255A` $209 是死价** / **24 口市价地板 $302（Reyee）· $412（ZyXEL）** / **8 口是血海：ARNA $15、BESTA $32–42、IP-COM DMO $53–68** / **RUBISEC 8 口 $211–1,404** / MİRSAN 2.5G 五款

用户第 23 次「继续」。清算 r69 遗留 + 排 8 口全带 + ZYXEL 枚举 + MİRSAN 定档。

### 一、🛑 `JL255A` $209 = 死价（r69 悬念关闭）
土零售同款：`itstore` **1,750 USD+KDV = 71,939.07 ₺ 含税 = $1,438** · `kurumsalit` **104,558.46 ₺ = $2,090** · `switchstore` **5,230 USD+KDV = 240,132.31 ₺ = $4,800**。⇒ **$209 比土零售最低低 6.9 倍 ⇒ 旧 K 码冻结残留。不得引用；r69 的 3.7–3.8× 成立。**
⇒ **僵尸价三形态齐**：① 合同到期（EXTREME/NEXTDATA 2025-09-28）② EOL 清库（2930F EOL 2026-08-11）③ **旧 K 码被索引器冻结残留**。⇒ **新增全局规则：DMO 价与土零售最低价差 >3 倍即判僵尸价，不得引用**（比查合同期快，零售价公开可查）。

### 二、⭐ 24 口：市价地板 = **$302（Reyee `RG-NBS3100-24GT4SFP-P`）** / **$412–514（ZyXEL `GS1920-24HP v2`，24 PoE+ 375 W，4 Dual SFP，2 年保，土零售 8 家在售）**
⇒ **我方 $140 = 2.2×（市价最低）/ 2.9–3.7×（市价品牌）**；**渠道口径 3.7–4.4×（DMO 活 $513–616）** ⇒ **两个口径以后严禁混用。**
⇒ **ZyXEL 牌价 vs 成交差 2.7 倍**：`zyxelmarket` 挂 965.12 USD+KDV = 56,144 ₺（$1,122），土零售成交 20,621–25,686 ₺（$412–514），最高报价 38,466 ₺。

### 三、🛑🛑 8 口段是血海 —— 我方没有优势
**DMO 净价**：`IP-COM G1008`（8×GE 非 PoE）1,278.20 = **$26** · `IP-COM G1110P-8-150W`（8×GE PoE 130 W + 2 SFP）**2,644.56–3,393.85 = $53–68**（`114634-K3983`，供应商 **NETWORK KURUMSAL**，店 1205）· `RUBISEC RS-IS-100-10GP` 10,532.94 = **$211** · `DAHUA DH-PFSC28GT1-120D` **15,037.43–18,993.83 = $301–380**（`55483`，AKTİF GRUP = RİVO 同价 18,993.83）· `DH-PFSD216ET2-240D` 23,274.13 = $465 · `PLANET GSW-2620HP` 15,088.06 = $302 · `MERAKI MS130-8X` $831 · `ALLIED AT-X530L-52GPX` $5,134 · `MAIPU NSS5830-56XQFP` $8,189 · **`RUBISEC RS-ES-750-32XQS` 940,681.03 = $18,806**。
**土零售含税**：**`ARNA-6108`（8×100M PoE）772.56 = $15** · `AL-8PORT` 1,956 = $39 · **`BESTA BST-820`（8+2 100M PoE 120 W）1,603.89–2,078.14 = $32–42** · `BST820G` 2,298.30 = $46 · `D-Link DES-1008P` $60–72 · `ZyXEL GS1008-HP` 3,607.93 = $72 · `TP-LINK TL-SG1008MP` 3,595.84 = $72（110.88 USD）· `Tenda TEF1110P` $119 · **`Hikvision DS-3E0109P-E/M(B)` 7,896.24 = $158** · `KD0820` $240。
⇒ **我方 8 口 100M FOB $24–26：对 ARNA $15 反而贵 1.6×、对 BESTA $32–42 持平、对 IP-COM 千兆 $53–68 才 2.1–2.6×** ⇒ **r66「8 口 100M 是唯一真优势（$24–26 vs $60）」被取代** —— 那个 $60 是零售品牌价，土本地 CCTV 品牌已把 8 口 PoE 打到 $15–41。⇒ **8 口卖点改为「同价给千兆/给管理」，不是「便宜」。**

### 四、⭐⭐ 8 口段的金矿：土品牌 `RUBISEC`
供应商 **BİRKİL SAVUNMA TEKNOLOJİLERİ**（K6355）。8 口 PoE 全线：`RS-IS-100-10GP` **$211** · `RS-ES-100-10GP` $234 · `RS-ES-250-10PS`（8 口 PoE+ 140 W）**$568** · `RS-IS-200-10GP` **$702–760** · `RS-IS-300-12GP` $770–834 · `RS-IS-300-12GPX`（8 PoE + 4×1/10G）**$1,404** · 核心 `RS-ES-750-32XQS` **$18,806**。
⇒ **同一个国家的 8 口段 $15 ↔ $1,404 = 91 倍** ⇒ **打 ARNA 是死路，打 RUBISEC 是活路** ⇒ **ODM/OEM 给土品牌的真实天花板不是 $60，是 $211 起。** ⚠ RUBISEC 自研 or 贴牌未确认（若贴牌，其 ODM 供应商即直接对手 + 潜在客户，**下一轮必查**）。

### 五、MİRSAN / `CLR-MRS` 2.5G 五款（⚠ 主体未确认）
`CLR-MRS-8106N`（5×2.5G+1×10G）· `8109N`（8×2.5G+1×10G）· `8218N`（16×2.5G+2×10G，Web managed）· `8226N`（24×2.5G+2×10G，Web managed）· **`8330N`（L3，30 口，6×10G）**；渠道 `gelecekbt.com`，**全部价格面议**。⇒ **2.5G 段已有土渠道 5 款在售、零公开价 ⇒ 我方 2.5G 定价窗口就在现在：谁先给价谁定义这一格**；报价单直接标「对标 `CLR-MRS-8226N`」，把对手钉在「面议」。

**诚实边界**：**我方 8 口千兆 PoE 的 FOB 未知（最急内部缺口，无法对 IP-COM $53–68 定价）** · RUBISEC 自研/贴牌未确认 · IP-COM 公司背景与土总代未查 · MİRSAN 零价格、`CLR` 主体未确认 · 24 口市价只有 2 家（Reyee/ZyXEL），中位数待第三四家 · `AT-X530L-52GPX`/`NSS5830-56XQFP` 口数配置未读，仅作「DMO 有天价」佐证。

## §63 · 第 69 轮 — 2026-11-06 ≈19:30–23:10 (+0800)：**$412 是僵尸合同（NEXTDATA，2023-09-28→2025-09-28）** / **DMO 比零售贵 1.7–2.1×（同品牌同规格实证）** / **8 口 MS130-8X $831 = 我方 32–35×** / ARUBA `JL255A` 出现 $209（⚠待复核）

用户第 22 次「继续」。本轮专攻 r68 唯一未闭合的致命空白：$412 地板价的来源。

### 一、🛑 地板价是僵尸：`EXTREME 210-24P-GE2` = NEXTDATA `K4200`，合同 28.09.2023–28.09.2025（已过期 13 个月）
净价 20,057.27 ₺ = **$401**（含税 24,068.72 = $481），保修 60 月，供应商电话 0312 284 70 60。同型号 `K4594`（**İFOKS**）28,321.94 ₺ = **$566**；同页另有 25,624.78 / 25,826.82 / 26,957.71。⇒ **同型号 5 个价位、1.41 倍跨度，全部来自 K 码**（第 5 次实证）。
⇒ **活着的 24 口 PoE+ 地板 = RUIJIE `RG-S2915-24GT4MS-P-L` $513（RESET，K4230，36 月）/ DAHUA $516（合同至 2027-05-07）** ⇒ **我方 $140 = 3.7–3.8×（对活地板 / 中位 $529）**，r68 的 2.9× 下限作废。

### 二、🛑🛑 方法论核心：DMO 价比零售贵 1.7–2.1 倍（同集团、同 24 口 PoE+ 370 W 规格）
**RUIJIE/RESET 在 DMO：25,667.05 ₺ 净价 / 30,800.46 含税 = $616。**
**Reyee `RG-NBS3100-24GT4SFP-P-V2` 土零售：15,100 ₺ 含税 = $302**（smartlink；nedratek 18,151.09；akakçe 最低 16,950；havale 14,798 = $296）。
⇒ **DMO 贵 1.7×（对 15,100）/ 2.1×（对 havale 14,798）。** ⇒ **「DMO 价 = 客户心理价位」这个 r60–r68 的全局隐含前提首次被实证否定**；DMO 价是**渠道位置溢价**，不是市场价格。⇒ 这也同时解释了 Cebeci 零售 FOREDGE 工业 4 口 $156–212 vs DMO $742–1,155（同一机制，不是品牌黑心），以及 SFP 的 $442–1,010 vs $9–25。
⚠ **同质边界**：S2915（36 月保）≠ NBS3100（24 月保），同一集团两条产品线，规格对齐但保修与软件体系不同 ⇒ 分母不完全同质，对外引用须先自陈。

### 三、⭐⭐ 8 口段最大发现：`CISCO MERAKI MS130-8X`（8 口）= $831
41,567.52 ₺ 净价 = **$831**（含税 $997），而同页 `MS130-24`（24 口）= 41,816.31 ₺ = $836 ⇒ **8 口与 24 口差 0.6%** ⇒ **口数在 DMO 不是定价变量，型号层级才是**。
⇒ **我方 8 口 FOB $24–26 = 32–35×**，**69 轮来最大单点价差**，远超此前 8×/9× ⇒ **r66/r68「8 口段只有平价到 3.5×」被取代**：8 口不是没优势，是从没有人量过。**用法**：客户预算上限由 $831 定义 ⇒ 我方 $24 交付、报 $60–80，客户在预算内、我们 2.5–3.3×。

### 四、⚠ ARUBA `JL255A` 出现 $209 —— 唯一可能推翻本轮全部结论的数字
`JL255A`（2930F 24G PoE+ **370 W** + 4×10G SFP+ uplink，L3）DMO 页面矩阵出现 **10,435.13 ₺ = $209** / 11,200.94 = $224，但同型号另有 21,244.38 = $425 / 26,458.65 = $529 ⇒ **2.5 倍跨度 = 多个 K 码。** `2930F` 已 EOL（2026-08-11），**EOL 清库是僵尸价的第二个来源**。⇒ **K 码/供应商/合同期未取到，未复核前不得引用**；若 $209 成立，我方对它是 **1.5–1.6×**。

### 五、ARUBA 价格结构（145 条中的第一批）
`JL256A`（48G PoE+ 4 SFP+）26,458.65 净价 / 31,221.21 含税（税 18%，`32094-K2757`）**由 4 家同价供应：ASIR DİGİTAL / CORETEK / MEGA BİLGİSAYAR / PLATO BİLGİSAYAR** ⇒ **ARUBA 是「同价多点」，比价时不会内部分裂，弱点是价格本身高**（与 DAHUA 单点、RUIJIE 单点不同）。`R8N85A-5Y` CX6000 48G PoE+ 370 W = 58,913.76 = $1,178（ASIR，`117113-K4877`）。`JL254A` 48G 非 PoE = 12,565.64 = $251。
⚠ **脏数据**：`R8N88A-5Y` 显示 1,113,641.08 ₺（$22,264），同页 `R8N85A-5Y` 仅 58,913.76 ⇒ 明显目录错误，**记录但绝不引用**；任何单点数字必须有第二来源。

### 六、其余新增 DMO 价格（净价）
MERAKI `MS130-24` $836 · ALCATEL `OS6360-P24` 45,550.03 = $911（K5003）· HUAWEI `S5735-L24P4XE-TA-V2` 66,271.99 = $1,325（「Only for Overseas」）· MICROSENS `MS453535P` 15,800.83 = $316（配置未读到）· RUIJIE `RG-S2915-24GT4MS-L`（非 PoE）13,824.01 = $276。零售：Zyxel `GS2210-24HP` 63,990.56 = $1,279 / `XGS1930-28HP` 49,625–77,168 = $992–1,543。

### 七、MİRSAN 线索（⚠ 主体未确认）
土电商 `gelecekbt.com` 在售 **`CLR-MRS-8218N`（16 口 2.5G + 2×10G SFP+）/ `CLR-MRS-8226N`（24 口 2.5G + 2×10G SFP+）**，管理型，**价格面议**。`MRS` 前缀疑同 MİRSAN（DMO 51–53 条）⇒ 若成立，**2.5G 段已有土产品牌铺货但无公开报价** ⇒ **有产品无价格 = 谁先给价谁定义市场**，直接服务待办 ⑤。**⚠ 主体未确认，不得引用。**

**诚实边界**：`JL255A` $209 的 K 码/供应商/合同期全缺（**本轮唯一可能推翻全部结论的数字**）· `210-24P-GE2` `K4594`（İFOKS，$566）合同期未读到 · MICROSENS 端口配置未读 · `JL073A` 未取价 · MİRSAN 零价格 · 8 口 PoE+ 全带未排、中位数无从计算 · DMO 站内直抓仍不可用，全部数据来自索引快照 ⇒ 同页多价位可能是索引混排。

## §62 · 第 68 轮 — 2026-11-06 ≈15:00–19:20 (+0800)：**24 口地板 $412（EXTREME）** / **DAHUA $516** / **SFP 价差 $442–1,010** / 净价口径

用户第 21 次「AB继续挖 挖完为止」。按 r67 计划做分品牌枚举第一批：EXTREME / DAHUA / HIKVISION / CISCO / D-LINK。

### 一、🛑 24 口 PoE 地板价 = **$412**（EXTREME `210-24P-GE2`，净价，60 月保修）
**EXTREME `210-24P-GE2`** 20,599.22 ₺ 净价 = **$412** · **DAHUA `DH-PFSD224ET2-360D`**（24×10/100 PoE 360 W 管理）25,792.52 ₺ = **$516**（合同 2025-05-07→2027-05-07）· HIKVISION `AI-SW26S` $922–1,136 · CISCO `C9200L-24P-4X-A` $2,018 · `C9300L-24P-4X` $2,193。
⇒ **我方 24 口 FOB $140 = 2.9×（对地板）/ 3.7×（对 DAHUA）** ⇒ **r67 的 4.0–5.3×、r61 的 4.6–8.1× 全部下调，对外只报「约 3 倍」。**
⇒ **同一品牌内部差 7.3 倍**：EXTREME 210 $412 ↔ EXTREME 5320 $3,001 ⇒ **「品牌决定价格」在 DMO 连同一品牌都不成立，只有型号/K 码决定。**

### 二、🛑 方法论级修正：净价 vs 含税价
DMO 明细页同时给「`+ Vergiler` 净价」与「`(Vergiler Dahil)` 含税价」，差 **20%**（老条目 18%）。**r61–r67 比对未统一口径，最坏高估 20%。** ⇒ 从本轮起**所有 DMO 价强制标注口径**。

### 三、⭐⭐ SFP 模块是比交换机更干净的价差
`HIKVISION AI-SFP10/1270`（10G SR）**$442–568** · `AI-SFP10/1330`（10G LR）**$871–1,010** · `AI-SFP25/1310`（1G SX）$266–328 · `AI-SFP25/1550`（1G LX）$492–606；对照 PLANET 1G SFP **$9–25**、KYLAND 工业 SFP 40 km **$66**、FOREDGE `SF312A` **$128**。
⇒ **「随交换机送 4 个 10G 模块」= DMO 目录价值 $1,700–2,300，我方成本极低** ⇒ **不降价也能加分的唯一手段**，对 Cebeci 类监控渠道尤其有效。

### 四、⭐ 8 口工业真实坐标
**DAHUA `DH-PFSC28GT1-120D`（工业 8 口 PoE 120 W，净价 15,037.43 ₺）= $301** ⇒ 我方 $158.66 = **1.9×**；PLANET $162–556 ⇒ 平价–3.5×；MOXA $1,292 ⇒ 8.1×（**特例**）。
⇒ **工业段诚实区间 1.9–3.5×**，「工业 8 倍」彻底退场。

### 五、⭐ 新增 5 家供应商
**NEXTDATA**（**0312 284 70 60**，HIKVISION 全线 + EXTREME，**合同 2026-03-24 → 2028-03-24 = 唯一还有 16 个月**）· **İFOKS BİLİŞİM SAVUNMA**（EXTREME 主力：X435/X440/5320/210）· **AKTİF GRUP SAVUNMA GÜVENLİK**（DAHUA，7.05.2025→2027-05-07，与 Cebeci 同为安防工程）· **ALTURA BİLİŞİM** · **E KAMPÜS EĞİTİM**。
⇒ **NEXTDATA 不缺续签、缺新品类** ⇒ 话术从「替换」改为「加第二条线」；**AKTİF GRUP = Cebeci 的 DMO 同行** ⇒ 「它在 DMO 用 DAHUA 卡住 $516，你要么比它便宜，要么比它有货」。

**诚实边界**：`EXTREME 210-24P-GE2` 的供应商/合同期未取到（**全类目最低价，来源待锁**）· İFOKS/AKTİF GRUP 合同期未取到 · 净价/含税混用对历史倍率的影响无法精确回溯，只能声明「最多高估 20%」· HIKVISION 四组 K 码（K4544/K4200/K5938/K4702）与供应商对应只确认部分。

## §61 · 第 67 轮 — 2026-11-06 ≈10:00–14:30 (+0800)：**类目 354–511 条结案** / **26 品牌普查** / **FOREDGE 全 12 条** / 「DMO 价」不成立

用户第 20 次「AB继续挖 挖完为止」。**0 新客户**；本轮把「类目多大」结案，并交出品牌级全量普查。

### 一、⭐ 类目规模结案：**354–511 条**（不是上万）
各视图「Toplam」实测：**esatis 末页 p=42 → 511（42 页）** · `dmo.gov.tr/Arama` 首页 **368** · NETCOM 视图 **354** · `s=switch` **336** · `s=extreme switch` **295**。
⇒ **与 DMO 官方 34,000/39,000+ 自洽** ⇒ **`p=774` 参数失效，第三次确认**；**交换机类目可在 ~42 页内枚举完**。
⚠ **`fetch_page` 抓不了 DMO**（返回「Ürün Bulunamadı」，需 JS/会话）⇒ 枚举只能靠搜索引擎缓存，**条目级全量仍差一步**。

### 二、⭐⭐ 品牌普查（26 个品牌，R6「Kabinet Ve Network Cihazları」视图）
**CISCO 226 · ARUBA 145 · EXTREME 78 · MİRSAN 51–53 · RUİJİE 42（+RUIJIE 2）· ZYXEL 41 · ALCATEL 30 · HUAWEI 29 · ALLIED 23–28 · RUCKUS 22–26 · HPE 21 · HIKVISION 16–18 · PLANET 15–16 · DAHUA 12–15 · JUNIPER 14 · FOREDGE 12 · D-LINK 11–17 · RUBISEC 11–25 · EDGECORE 10 · PEPLINK 9 · KYLAND 7 · TRONX 7 · DELL 6 · DELL EMC 6 · BESTRACK 6 · EATON 6 · FORMRACK 4 · F5 4 · MOXA 4 · HPE ARUBA 4 · ÜÇ-ER 4 · MILESIGHT 3 · LINE 2 · DRAYTEK 2 · VIVOTEK 2 · MICROSENS 2 · MELANOX 1 · AGER 1 · IPECS 1 · TR7 1**。
⇒ **① Cisco = 全类目 44–64%，且多为过期合同**；**② 中国/台系合计约 172 条 = 34–49%** ⇒ **「产地」不是障碍，K 码才是**；**③ RUIJIE 有 44 条在架**（`RG-S6150-24VS8CQ-X` $3,959、`RG-WS6816` $5,812–7,288）。

### 三、⭐⭐⭐「DMO 价格」这个说法不成立 —— 同型号价差 1.1×–9×，全来自 K 码
**PLANET `PL-IGS-TS82CM`：$162 / $403 / $457 / $556（3.4×）** · **FOREDGE `IS104GPS-2F`：$742 / $1,155（1.6×）** · **Alcatel `OS6560-P24X4`：$1,060–$9,542（9×）** · MOXA `EDS-G512E`：$1,190–$1,978（1.66×）。
⇒ **标准问句改为「这个型号你有几个 K 码，最低那个多少」**。⇒ 我们不需要打赢市场，**只需打赢客户手里那一个 K 码**。

### 四、⭐⭐ FOREDGE 全 12 条（K 码 119852–119884）
`AI8024` 24×100M PoE 250 W **$513** · `AI1024GC` $1,284 · `PS2024GR` $1,098 · **`S5700-24GP-4TFR` $1,605** · **`S5700-48GP-4TFR` $2,182** · `S5700-24F-8G-4TF` $2,696 · **`IS108GPS-2F`（工业 8×GE PoE 240 W + 2 SFP+）$1,155** · `IS104GPS-2F`（工业 4 口）$742 · `SF312A-LC-10KM` $128。
⇒ **与 r61 冲突两处**：`S5700-24GP-4TFR` r61 记 **$1,337**、本轮见 **$1,605**（1.20×）；`IS104/IS108` 相邻串号 ⇒ **同型号多档，非数据错**。
⇒ **对 Cebeci 的杀伤**：它卖的工业 8 口 DMO **$1,155**，而 PLANET 同规格 **$162–556** ⇒ **它自己就贵 2–7 倍**；我方 FOB $158.66 ⇒ **对 FOREDGE 11.5×（仅对 FOREDGE，不可说成对市场）**。

### 五、⭐⭐ PLANET 全系列 —— 24 口 PoE 的真锚是 $565–744
`SGS-6310-24P4X`（24 PoE + 4×10G）**$744** · `GS-4210-24PL4C`（24 PoE+ 4 SFP）**$565** · `GS-6322-24P4X` $1,733 · `SGS-6310-24T4X`（非 PoE）$359 · **`GS-4210-8P2S`（8 口 PoE+ 管理）$201** · `IGS-10020HPT` $680 · `IGS-5225-16T4S` $898–1,001 · `IGS-6325-20T4C4X` $1,001 · `IGS-6325-20S4C4X` $1,181。
⇒ **24 口管理型我方 FOB $140 ⇒ 4.0–5.3×**（比之前 4.6–8.1× 更保守可信）⇒ **对外一律报 4–5×**，4.6–8.1× 只在客户指名 Cisco/Zyxel 时用。
⇒ **8 口双口径**：对贸易商（EZCOOL $30.25）贵 44–55%；**对 DMO 目录（$201）是 4.3–4.6×**。**两个都对，必须声明口径。**

**诚实边界**：`fetch_page` 抓不到 DMO ⇒ 枚举依赖搜索缓存，**条目级全量未完成** · `IS104/IS108` 价格归属待复核 · `AI2010GX` 44,943.14 ₺ 与 `IGS-5225-16T4S` 同价疑串行 · `PL-IGS-TS82CM` 8,108 ₺ 档供应商未确认 · 品牌计数随视图漂移。

## §60 · 第 66 轮 — 2026-11-06 凌晨 ≈04:00–06:30 (+0800)：**核实 `PL-IGS-TS82CM` → 是 PoE+，r65 判断反了** / DMO 官方规模口径

用户第 19 次「AB继续挖 挖完为止」。**0 新客户**；本轮把 r65 的最高优先级空白核实掉了，**结论反转**。

### 一、🛑🛑 我错了：`PLANET PL-IGS-TS82CM` 是 **PoE+** 机，不是「无 PoE」
**PLANET 官方**：`Industrial 8-Port Gigabit 802.3at PoE+ Switch` · 8×GE **PoE+ 单口 36 W** · **240 W 预算** · 2×SFP · **20 Gbps** · **IP30** · **−40~75 °C** · DC 48–56 V · 255 W max。
**BİMEL（土耳其总代）**：`802.3at/af PoE+ Injector`（30.8 W/口，240 W），分类挂「Yönetilebilir Endüstriyel Tip **PoE** Ethernet Switch」。
**错因**：DMO 商品页根本没有 PoE 字段 ⇒ 我据「无字段」推断「无功能」。**⇒ 方法教训：DMO 缺字段 ≠ 产品缺功能；PoE/bt/宽温/管理型必须回厂商或总代确认。**

### 二、⇒ 连带作废的结论（四条）
① r65「8 倍来自 PoE」→ **错**，PoE 满街都是；② r65/r64「同价带 PoE」→ **错**；③ r62「工业 8 口 8.1×」→ 只对 MOXA 成立（品牌溢价）；④ r63「工业段是厚利段」→ **错**。
**⇒ 我方 FOB $158.66 vs DMO $162 = 平价位**；**土耳其零售 5,293.83 / 5,599.54 / 5,605.24 ₺ = $106–112 ⇒ 我方比零售贵 1.4–1.5×**。

### 三、⭐ 我方定档（唯一权威版，替代此前所有版本）
| 档位 | 锚 | 我方 FOB | 位置 |
|---|---|---|---|
| 8 口 **100M 非管理 PoE** | Hikvision 零售 **$60** | **$24–26** | ✅ 便宜 2.3–2.5× **唯一真优势** |
| 8 口千兆 PoE | EZCOOL B2B $30.25 | $43.50–47 | ❌ 贵 44–55% |
| 8 口千兆工业 PoE+ | **PLANET DMO $162 / 零售 $106–112** | **$158.66（bt）** | ⚠ **平价**（对 DMO）/ 贵 1.4–1.5×（对零售） |
| 8 口工业 PoE+（MOXA） | $1,292 | $158.66 | ✅ 8.1×（品牌溢价） |
| 24 口千兆 PoE 管理 | DMO 主力 $650–1,130 | $140 | ✅ 4.6–8.1×（僵尸价） |
| 24 口 2.5G PoE + 10G | Zyxel $1,706–2,083 | ≤$800 | ✅ 2.1–2.6×（GXCOM $118 压顶） |

**内部动作**：**若工业 8 口要对 $162 打出 25% 空间，FOB 需 ≤ $120 ⇒ 需降本 24%（约 $39）**；否则只能讲规格（bt/300 m Watchdog/5 年）。

### 四、⭐ DMO 官方规模（权威数，一劳永逸）
`dmo.gov.tr/Home/Icerik/86`（2026-07-24）：**「约 34,000 项目录与库存产品，合计超过 39,000 种产品」** ⇒ 交换机类目**数百条**合理，**`p=774` 确系参数失效**（r65 判断成立）。**⇒ 类目可在 30–40 页内枚举完。**

### 五、六家经销商话术统一改口（一页表）
**Cebeci**：工业 8 口只作补充，主推 **100M（$60 卖价我 $25）** · **ROKHSİS**：PLANET $162 平价位、规格更高 → 做 Cisco 降级替代 · **4S**：缺的是 **100M 非管理入门线** · **DÖRT US**：`4US` 品牌补 **100M 入门 + 8 口工业 bt** 两条 · **EKSPA**：Technopc 加 **100M 非管理 PoE**（最不易失败）· **RESET**：开场仍用 8,108 ₺，落点改「**同价 + bt + 5 年**」。

**诚实边界**：8,108 ₺ 那档的 DMO 供应商名未取到（BİMEL 是分销商身份推断）· MOXA 功率预算未比对 · **我方 `EW-PIS3810M-8GE-BT` 的 PoE 预算本轮未核对**（若低于 240 W，「同价更高功率」需改口）· DMO/零售 1.4–1.5× 样本仍不足。

## §59 · 第 65 轮 — 2026-11-05 夜 ≈00:10–03:40 (+0800)：**8 倍来自 PoE 不来自「工业」** / **撤回「类目上万条」** / RESET 具名联系人

用户第 18 次「AB继续挖 挖完为止」。**0 新客户**；本轮三件事全是「把漂亮的数字拆开」。

### 一、🛑 拆掉「工业 8 口 8.1×」：真正的价差来源是 PoE
**PLANET `PL-IGS-TS82CM`（工业 8 口 L3 管理型，20 Gbps，非 PoE）= 8,108.23 ₺ = $162**（另有 20,136.98 / 22,838.38 ₺ 两档）；**MOXA `EDS-P510A-8PoE`（PoE+）= $1,292**。
⇒ **我方 `EW-PIS3810M-8GE-BT` FOB $158.66 ≈ DMO 非 PoE 价 $162** ⇒ **不能说「工业机便宜 8 倍」**，只能说「**同样的钱，DMO 给你不带 PoE 的，我们给 802.3bt**」。
⇒ **工业段真实价带 `PLANET IGS` 全家**：`IGS-5225-4UP1T2S` $565–712 · `IGS-10020HPT` $680 · `IGS-5225-8P2S2X` $847 · `IGS-5225-16T4S` $898 · `IGS-6325-20T4C4X` $827–1,001 ⇒ **中位倍率 2.6–4.3×，不是 8×**。

### 二、🛑 撤回「DMO 交换机类目至少上万条」
同一类目在不同页自报 **222 / 253 / 339 / 369 / 418 / 435 / 480** 条，**随 `p` 单调上升且互相矛盾** ⇒ `p=774` 返回结果是**参数被忽略/钳制**，不是「有上万条」。
⇒ **类目在数百条量级（约 300–500），30–40 页可枚举完** ⇒ **不需要抽样，可以做穷尽** —— 这正好符合用户「挖完为止」的原意。

### 三、🛑 `OS6560-P24X4`：7–8 档、最高 9 倍（r62 的「1.47×」低估）
$1,060（53,019.91 ₺，K1840 REFLEKS，2020-11-25→2023-02-25 已停售）/ $1,950 / $2,414 / $2,777 / $2,824 / $2,856（K77414 DÖRT US）/ $3,091 / **$9,542（477,281.22 ₺，⚠ 待复核）**。
⇒ **$9,542 是其余七档的 3–9 倍，且 P24X4 贵过 P48X4（$2,856）3.3 倍，高度可疑** ⇒ **r62 §三「24 口 10G 7.5–8.0×」暂停引用**。
⇒ 但**话术反而更强**：「**同一台 Alcatel 在 DMO 里能有七个价，从 5 万到 15 万里拉**」= 「K 码才是真价格」的最强证明。

### 四、⭐⭐ RESET 完整档案 + 具名联系人
店铺 **170027**（类目内 47 条）· **+90 212 955 00 95** / fax 96 · `info@reset.com.tr` · **Vizyon Park Ofis Blokları 4. Blok Kat 29 Ekim Cad. No:3/304, Yenibosna/İstanbul 34197**（第二址 Parima Plaza Cevizlibağ）· **2016 成立 · 10–50 人** · 自述「**Sistem Entegratörü**」「**marka bağımsız**」。
**具名**：⭐ **`Kerem Kendirci` — Sales Manager, Public & Corporate**（第一联系人，KPI 就是公共部门=DMO）· `Ismail Kavak` — Founder & CTO · `Mehmet Karadut` — Sales Manager ICT · `Mustafa Tümay` — Network System Engineer。
品牌：CISCO 228 · ARUBA 54 · MİRSAN 53 · HUAWEI 37 · HPE 17 · D-LINK 17 · DRAYTEK 6 · EATON 6 · CANOVATE 9 · LONGLINE 9 · BESTRACK 6 · PLANET 6 · MOXA 4 · MICROSENS 2 · MILESIGHT 3 · MELLANON 1 · ALFA TREND 6。
⇒ **冷呼脚本已成文**（自称 marka bağımsız + 用他自己目录里的 `PL-IGS-TS82CM` 8,108 ₺ 开场 + 报 $160 FOB）。⚠ 姓名来自 ZoomInfo（B 级），邮箱打码，**电话里若否认立即改口**。⚠ **Crunchbase 把总部写成 Ankara 是错的**（电话 0212）。

### 五、⭐ DÖRT US 品牌补充（修正 r64）
**HPE `Q6M27A SN2410M` 25GbE = 522,177.79 ₺ = $10,439**（另一档 574,091.65）· HPE `JL828A 5140` · `R9L61A 5140` · **ALCATEL `OS6560-P48X4` = $2,856** · **ZYXEL `XS3800-28` = 211,815.65 ₺ = $4,235** · **D-LINK `DGS-1210-10/ME`** · **KYLAND `IGSFP-S-LH-LC-1310-40-DDM`（SFP 40 km）= $66**。
⇒ **DÖRT US 不是 Zyxel 独家**，是多品牌（Zyxel/HPE/Alcatel/D-Link/KYLAND/Supermicro）+ 自有品牌 ⇒ **但不削弱「自有品牌缺交换机」的结论，反而加强**（一个做 5 个网络品牌的店，自有品牌里没交换机）。
⇒ **修正**：r64 说「KYLAND 7 条 = 工业交换机」要收窄为「**KYLAND 7 条，含至少 1 条工业 SFP 模块，其余 6 条未逐条确认**」。

**诚实边界**：`PL-IGS-TS82CM` 的 PoE 属性是 DMO 字段推断（页内无 PoE 字段，未见 PLANET datasheet）· $9,542 那档无法复现 · RESET 合同期三次未取到 · RESET 姓名来自第三方库 · DÖRT US KYLAND 其余 6 条未确认。

## §58 · 第 64 轮 — 2026-11-05 ≈20:10–23:50 (+0800)：**推翻 r61 最低锚（FX2120 是 10G 汇聚）** / **DÖRT US = ODM 第一顺位** / 僵尸合同规则化

用户第 17 次「AB继续挖 挖完为止」。**0 新客户**。

### 一、🛑 推翻 r61：Draytek `FX2120` 不是 24 口 PoE
DMO 页字段 `Port: 12` / `SFP+ (10G) x 12` / `240 Gbps`；DrayTek UG V1.3 `L2+ Managed Switch`；CE `12 portami 10Gbps SFP`。**DMO 价 24,621.85 ₺ = $492（NETCOM）**。
⇒ **24 口 PoE 最低锚从 $413 → $437**（Zyxel `XGS2210-28HP`，DÖRT US 店 25,746.46 ₺ = $515 与另一档 $437 并存 ⇒ 又是「同型号不同 K 码」的例证）。**价格带 $413–1,337 收窄为 $437–1,337，对我方有利。**

### 二、🛑 修正 r63：「4S = CISCO + HP 双头」不成立
4S 交换机类目还有 **ZYXEL 14 条**：`XGS4600-52F` 189,398.87 ₺ = $3,785、`RGS200-12P` … ⇒ 应写「**Cisco 为主、HP 为辅、Zyxel 补位**」。**⇒ 4S 不排斥台系品牌，这是打电话最该用的一句。**

### 三、⭐⭐⭐ DÖRT US（店铺 120026，112 条）= ODM 第一顺位，不是 EKSPA
品牌：**ZYXEL 43 · SUPERMICRO 40 · PANTUM 13 · KYLAND 7（工业交换机）· ÜÇ-ER 4 · COMODO 2 · POINTMAN 1 · 自有 `4US BİLİŞİM` 2**。电话 **0850 666 03 12**。`XGS2210-28` 21,495.41 ₺ = $430 / `XGS2210-28HP` 25,746.46 ₺ = $515 / `WAC6103D-I` 6,364.57 ₺ = $127；自有品牌含 `Tıbbi Akıllı İlaç Arabası AHTİ M-16` **164,771.19 ₺ = $3,294**。
⇒ **三条理由**：① 已在做自有品牌（不需解释贴牌）② 已在卖工业交换机（不需解释工业 PoE 卖给谁，且它知道 KYLAND 采购价）③ **自有品牌里没有交换机**（缺口正好是我们那格）。
⇒ **排序改为：ROKHSİS → 4S → DÖRT US → EKSPA**。

### 四、⭐⭐ 「僵尸条目」的制度依据
DMO 合同条款（`dmo.gov.tr/Home/Icerik/180` 2018 修订 + EK-3 第 20 条）：供应商到期前提出新合同申请、申请日仍在原合同范围内者，**原合同可按「每次 1 个月、最多 3 次」延期**。
⇒ ① 过期价能查到是**制度性**的 ⇒ 只能压价不能指望查不到；② 「过期仍在架」= **正在申请续签** ⇒ 最佳电话时机；③ **过期超 3 个月的实际已不可下单**（DUGAN 7 月 / İNFOGEN 9 月 / 4S-Cisco 6 月）⇒ 可对客户说「那个价你买不到」。
⇒ **报价规则**：**报「僵尸价 − 20%」，不报「当前价 − 5%」**；续签中的卖「新 K 码」，已死的卖「替换」。

### 五、⭐ 新锚（本轮）
DUGAN 店 1346：`GS1350-26HP` $466 · `XGS2220-30` $805 · `XGS2220-54` $1,289 · `XS3800-28` **$5,044** · `XMG1930-30HP` **$1,706**（合同 25.03.2024–25.03.2026 已过期）。
DÖRT US：`XGS2210-28` $430 · `XGS2210-28HP` $515 · `WAC6103D-I` $127。4S：`XGS4600-52F` $3,785 · `C9300L-24T-4X-E` $542 · `C9500-24X-E` $3,628。
**零售侧（安防渠道）**：Hikvision `DS-3E0109P-E/M(B)` 8×100M 60 W = **$60** · `DS-3E0326P-E/M(B)` 24×100M 230 W = **$119–123** · `DS-3E0526P-E/M` 24×GE PoE = **$204** · 杂牌 8+2GE = **$27** · 24+2GE = **$277**。
⇒ **我方 8 口 100M FOB $24–26 vs 零售 $60 = 2.3–2.5×（这个档是真的）**；千兆档无优势（r61 已证）。

### 六、⚠ TECHNOPC 自营合同也断了
`TECHNOPC TEKNOLOJİ SAN. VE TİC. A.Ş.`（0216 329 39 99）自营条目 `ProPC AIO DNT24-Q585`：**30.11.2023–30.11.2025 ⇒ 已过期 11 个月**。⇒ 「Technopc 零交换机 + 自己合同断档」= **它比我们更急**，EKSPA 提案紧迫度上调。

**诚实边界**：DÖRT US / RESET 合同期未取到 · `4US` 自有品牌 2 条只确认 1 条 · 4us 的 DMO 目录 PDF 已 404（5 个 K 码仅索引级）· 「过期 3 个月不可下单」是我的推论，DMO 未明文。

## §57 · 第 63 轮 — 2026-11-05 ≈15:00–19:40 (+0800)：**DMO 同 K 码价格锁定** / **Cisco 货架在垮** / ROKHSİS 通话脚本

用户第 16 次「AB继续挖 挖完为止」。**0 新客户**；本轮把 r62 的名单变成可执行动作，并挖到一个比名单更值钱的结构。

### 一、🛑 推翻「便宜 5% 就能抢 DMO 位」—— **DMO 对同 K 码价格锁定**
`CISCO C9200-48P`：**ROKHSİS 与 4S 同为 118.420,84 ₺**（含税 142.105,01 ₺ = $2,841）；`C9400-LC-24XS=`：**ROBİT 与 EKSPA 同为 102.726,72 ₺**。
⇒ **同一 K 码全供应商同价，只能在服务/交付上竞争。** ⇒ 抢位只能靠**新品牌/新 K 码**，不能靠折扣。
⇒ **同时修正 r62 §二的归因**：r62 把「同型号 3–5 档」写成「供应商让价差」，**实为不同 K 码/合同期**。结论（先问第几档）不变，**归因改**。

### 二、⭐⭐⭐ DMO 的 Cisco 货架正在垮 —— 品牌位在空出来
| 供应商 | Cisco 合同期 | 状态（2026-11-05）|
|---|---|---|
| EKSPA | 20.09.2019–20.09.2021 | 过期 5 年 |
| NETKUR | 3.09.2021–3.09.2023 | 过期 3 年 |
| BİLGİBİM | 27.09.2021–27.04.2024 | 过期 2.5 年 |
| **4S** | **3.05.2024–3.05.2026** | **过期 6 个月** |
| **ROKHSİS** | **7.11.2024–7.11.2026** | **2 天后到期** |
| NETCOM（Huawei）| 30.10.2024–30.10.2026 | 过期 6 天 |

⇒ **DMO 目录里存在大批「僵尸条目」：合同已过期但商品页仍在、价格仍可查。** 客户看到的是过期合同价。
⇒ **我方报价只要落在僵尸价带之下，就会被当成「明显划算」。** 这是本轮最大的未开采矿（r64 候选 #5）。
⇒ **第二通电话应打给 4S（空 6 个月），不是 EKSPA。**

### 三、⭐⭐ ROKHSİS = 一个 Cisco 专柜，51 条里 49 条 Cisco
店铺 **1141170**：**51 条**，**CISCO 49 + COBIDU 2**，区间 **2,840–1,564,467 ₺**；Cisco 合同 **7.11.2024–7.11.2026**；`Tedarikçi İletişim 0312 2586459`；官网营业 **PZT–CMT 09:00–18:00**；解决方案线含 **Fiziksel Güvenlik** + **İletişim Ağları**（⇒ 工业 PoE 不用另开话题）。
⇒ **通话脚本已写**（`132` §二）：30 秒开场（报店铺号 + 51/49 + 到期日）· 三段式（价格锁定事实对撞 → 我方 DMO 位置 → 只留一个动作）· 三句异议应对 · 最佳窗口 **11/5–11/6 15:00–17:00 (+0800)**。
⇒ **禁忌**：不要说「便宜 90%」；不要说「你们合同没了」（只说「到期日我看到是 7 号」）。

### 四、⭐⭐ EKSPA = Technopc 的 DMO 通道（店铺 1353）
EKSPA 店铺 **1353** 只挂 **TECHNOPC 3 条**（`ProPC H410` 9,559.71 ₺ = $191）。r58 已证 **Technopc 交换机为零** ⇒ **给 Technopc 贴牌交换机 + 沿用 EKSPA 现有合同扩 K 码 = 一条现成进 DMO 的路**。
⇒ 话术升级：「不换供应商、不重进目录，**我给你加一个品类**」。

### 五、⭐ 新锚价（关键两条）
**PLANET `GS-5220-8P2T2S`（8×GE PoE + 2 GE + 2 SFP，管理型）= 12,203.31 ₺ = $244**（供应商 İNFOGEN，合同 12.02.2024–12.02.2026 已过期）⇒ **普通 8 口管理型的真锚是 $244，我方 FOB $158.66 = 1.54×，不是 8 倍**。
**ALLIED `AT-IE340-12GP`（工业 12 口）= 122,884.32 ₺ = $2,457** ⇒ 我方工业 16 口 FOB $333.67 = **7.4×**。
其余：`C9200-24T` $953 · `C9200L-48T-4G` $1,347 · `C9200L-48P-4G-A` $3,114 · `AT-X530L-52GTX` $4,153 · `-52GPX` $4,679 · `AT-X530-52GPXm` $5,440 · `AT-X220-52GT` $2,106 · `C9200-NM-4X` $675。

### 六、⭐ 经销商名册 17 → 26 家
新增：**RESET**（唯一多品牌大店：CISCO 228 / ARUBA 54 / MİRSAN 53 / HUAWEI 37 / D-LINK 17 / HPE 17 / DRAYTEK 6 / MOXA 4 / PLANET 6 / MICROSENS 2 …）· **İNFOGEN**（PLANET）· **NETKUR** 0312 419 87 03（CISCO）· **BİLGİBİM** 店铺 1406、0312 472 33 73、CISCO 52 条 · **PLATO** 0312 418 36 76（HPE）· **ASIR DİGİTAL** 0212 212 20 97（HPE）· **EDUSANO**（ARISTA）· **DİJİTAL DÜNYA** 0272 214 72 72（IP-COM）· **BEYAZ** 店铺 1111169（FORTINET 15）。
⇒ **6 家有直拨电话可冷呼**；**RESET 是唯一不会因「单品牌独家」拒新品牌的**。

**诚实边界**：ROKHSİS 合同「到期」还是「续签中」**未知**（DMO 不显示续签状态）· 六家仍无采购负责人姓名 · **Allied Telesis 供应商名两轮未果**（`Doğan Birlik` 是纺织公司，无关，勿写）· `4S` 成立年两源冲突（1996 创立 / 2004 注册，并列）· `p=774` 疑点未消除。

## §56 · 第 62 轮 — 2026-11-01 ≈07:50–11:20 (+0800)：**DMO 工业段 $1,292 / 同型号 5 档价差 47%** / 安卡拉 6 家经销商完整档案

用户第 15 次「AB继续挖 挖完为止」。**0 新客户**；本轮补 r61 缺的两块：工业高端段 + 经销商联络。

### 一、⭐⭐⭐ 同型号在 DMO 里有 3–5 档报价，最高差 47%
**Alcatel `OS6860N-P48M`（L3，36×1/2.5G，95 W bt PoE）**：**$5,061 / $6,466 / $6,645 / $7,031 / $7,449**（253,166.57 – 372,561.67 ₺）⇒ **1.47×**。
**MOXA `EDS-G512E-8PoE-4GSFP-T`**：$1,190 / $1,373 / $1,840 / $1,978 ⇒ **1.66×**。**Allied Telesis `AT-X530L-28GPX`**：$2,457 / $3,217 / $3,471 ⇒ 1.41×。**Huawei `S5735-L48LP4XE-A-V2`**：$2,530 / $2,731 / $2,807。**PLANET `IGS-6325-20S4C4X`**：$898 / $1,181。
⇒ **标准问句改成「这个 K 码你按第几档拿？」** —— 一句就能筛出谁是真操盘方。

### 二、⭐⭐ 工业与高端段价格全表（本轮新取）
**MOXA `EDS-P510A-8PoE-2GTXSFP-T`（工业 8 PoE+ + 2 combo，−40~75 °C）= $1,292** · PLANET `IGS-6325-20T4C4X` **$1,001** / `IGS-6325-20S4C4X` $898–1,181 · Zyxel `RGS200-12P` $1,323 · Cisco `IE-3300-8U2X-E` **$2,814** · FOREDGE `IS104GPS-2F` $742 · **Huawei `S5735-L48LP4XE-A-V2`（48 GE + 4×10G，PoE 380 W）$2,530–2,807** · Huawei `S5735-L48T4S-A-V2` $1,040 · Allied Telesis `AT-X530L-28GTX` $2,340–2,567 / `-28GPX` $2,457–3,471 / `-52GPX` $4,153–5,049 / `AT-X530-52GPXm` **$5,440** · Alcatel `OS6860N-P48M` $5,061–7,449 / `-P48Z` $5,694–5,937 / `OS6860E-U28` $3,151 / `OS6560-P24X4` **$9,542** · Zyxel `CX4800-56F` $28,157。
⇒ **倍率（DMO / 我方 FOB）**：工业 8 口 bt **8.1×**（$158.66 vs MOXA $1,292）· 工业 8 口低端 **8.2–11.1×** · 工业 16 口 **3.0×** · 48 口 PoE+ **5.6–6.0×**（$425–450 vs Huawei $2,530）· 24 口 PoE+ 10G **7.5–8.0×**。
⇒ ⚠ **修正 r59 的适用范围**：r59「高端 1.14–1.65×，不要打价格战」**只对零售渠道成立**；对 DMO 客户同批型号是 **3.0–11.1×**。**结论不推翻，但必须分渠道说。**

### 三、⭐⭐ 安卡拉 6 家 DMO 经销商完整档案（r61 只有电话）
**ROKHSİS** — Via Flat İş Merkezi, Beştepe Mah. Nergiz Sok. K:3 No:87 Söğütözü/Çankaya/Ankara；**+90 312 258 64 59**；**info@rokhsis.com.tr**；域名 2017-07-10；**WHOIS 注册人为「ODTÜ GELİŞTİRME VAKFI BİLGİ TEKNOLOJİLERİ」⇒ ODTÜ 发展基金会旗下**；自述「%100 yerli sermaye」「marka bağımsız」；Cisco 合同 **2026-11-07 到期（2 天后）**。
**EKSPA** — Turan Güneş Bul. 576. Sk. No:30, Aşağı Dikmen/Çankaya/Ankara 06450；**+90 312 463 88 88** / 呼叫中心 **444 10 42**；**info@eks-pa.com.tr** / info@eb.com.tr；`eks-pa.com.tr`；**Ankara+İstanbul 100+ 人、1000+ 客户**；**7 大区 21 省 7×24 授权服务**（HP/HPE/Microsoft/Oracle/Cisco/Trend Micro）⇒ **补我方本地 RMA 短板的最佳伙伴**。
**4S BİLİŞİM TEKNOLOJİLERİ A.Ş.** — Çetin Emeç Bul. 1314. Cad. No:40/B, Öveçler/Çankaya/Ankara；**0312 472 90 00** / fax 05；`4s.com.tr`；**2004-05-04 成立**；**DMO 在册 231 个条目** ⇒ **目录体量最大**。
**DATANETSOFT** — Sağlık Mah. Ataç 1 Sk. No:7/6 Çankaya/Ankara；**0850 502 59 69**；info@datanetsoft.com.tr；**21 个条目全是 Zyxel**（价区间 5,295–1,408,405 ₺）⇒ Zyxel 独家通道。
**RİVO TEKNOLOJİ A.Ş.** — HQ Ceyhun Atuf Kansu Cad. Ata Plaza No:100/B Balgat/Çankaya/Ankara；**444 8 620** / +90 312 481 19 14；info@rivo.com.tr；**2013 成立、51–200 人、营收估 $10–50 M**；**27 个条目全是 Dahua**。
**NETCOM** — **0312 473 73 24**；**38 个条目 = Huawei 34 + Draytek 4**；Huawei 合同 2024-10-30 → **2026-10-30**；`S5735-L48T4S-A-V2` 只要 **$1,040** ⇒ Huawei 预算段通道。

### 四、⚠ 主体未确认：4S ≠ Dört Us
`4S BİLİŞİM TEKNOLOJİLERİ A.Ş.`（4s.com.tr，**2004-05-04**，0312 472 90 00，Ankara Öveçler，DMO 231 条）与 `DÖRT US BİLİŞİM SAN. VE TİC. A.Ş.`（4us.com.tr，**2008**，**0549 299 0967**，iletisim@4us.com.tr，İstanbul Başakşehir + Zonguldak 支店）**名称几乎相同但为两家不同公司** ⇒ **按「一定不能合并」原则各自记录**。

### 五、DMO 类目体量修正
`dmo.tr/Katalog/Arama?...&p=774` 仍返回交换机类目结果 ⇒ **该目录条目数至少上万**，r61「上千」的判断**低估一个量级**。

**诚实边界**：6 家只有 info@ 邮箱与电话，**采购负责人未取得**；ROKHSİS 股权来自 WHOIS 转载站，**需人工复核**；EKSPA 总经理姓名来自博客转载（低可信）；`AT-X530*` 与 Alcatel 的价格**未见供应商名**；4S 与 NETCOM 官网未找到。

## §55 · 第 61 轮 — 2026-11-01 ≈04:30–07:40 (+0800)：**DMO 24 口价格带 $413–1,337** + **17 家经销商** + **EZCOOL B2B 价推翻 r58**

用户第 14 次「AB继续挖 挖完为止」。**0 新客户**；本轮是**口径重构轮** —— 第一次把 DMO 合同价与零售价分开成两张带。

### 一、⭐⭐⭐ DMO 24 口 PoE 价格带 = **$413 – $1,337，主力 $650–1,130**
Draytek `FX2120` **$413** · Zyxel `XGS2210-28HP` **$437** · D-Link `DGS-3000-28X` **$473** · Cisco `C9300L-24T-4X-E` **$459–542** · Ruijie `RG-S2915-24GT4MS-P-L` **$513** · Dahua `DH-PFSD224ET2-360D` **$636–770** · Zyxel `XGS2220-30` **$665** · Zyxel `XGS2220-30HP`（400 W/L3）**$774** · Aruba `JL255A 2930F` **$862** · Aruba `JL725A 6200F 370 W` **$1,128** · **FOREDGE `S5700-24GP-4TFR` $1,337**。
⇒ 我方 FOB **$70（非管理 300 W）/ $140（管理型）** ⇒ **报 $250–400 进目录仍是全场最低**。
⇒ **价格带按品牌排不按配置排**：同为 24 GE PoE + 4×10G，Zyxel $437 / Ruijie $513 / Aruba $1,128 / FOREDGE $1,337 —— **差 3 倍**。
⇒ **2.5G PoE 在 DMO 是奢侈品**：Zyxel `XMG1930-30HP`（24×2.5G PoE + 4×10G PoE、700 W）**$1,882–2,083** vs FOREDGE 零售 `PS3024XGPSH` $447.9–560.2 ⇒ 我方 `EW-S57930TM-AP` 报 **$800 以下即全场唯一**。
⇒ **同型号双价差**扩到新三例：Dahua **$770 vs $636**、Zyxel `XMG1930` **$1,882 vs $2,083**、Cisco `C9300L-24T-4X-E` **$542 vs $459**。

### 二、⭐⭐⭐ FOREDGE 渠道加价链首次量化
`IS104GPS-2F`：零售 **$156–212** → DMO **$742** ⇒ **3.5–4.8×**；24 口档：零售 $363.6–408.8 → DMO **$1,337** ⇒ **3.3–3.7×**。**DMO / 我方 FOB = 8.2–19.1×。**
⇒ **解释了一个老问题**：FOREDGE 敢要 MOQ 500、6–8 周交期，因为**它的钱在 DMO 目录里，不在货架上**。
⇒ 对经销商的新话术：不讲「零售 $231 我 $70」（3.3×），讲 **「FOREDGE 在 DMO 这一档卖 $1,337，你在 DMO 里没有位置——我让你有」**。

### 三、🛑 推翻 r58 的 8 口判断（EZCOOL B2B 价）
**EZCOOL 主体** = **MS Teknoloji Tic. Ltd. Şti.**，税号 **6230371894**，İstanbul Kartal / Esentepe Mh. Kelebek Sk. No:2/24 Kat:4 ⇒ **贸易商非工厂**。
**B2B 价（`bdk.com.tr` 原文）**：`EZ-04PSE` **$15.95** · `EZ-08PSE` **$19.64** · `EZ-08PSF` **$25.85** · **`EZ-08PSF-FG`（8GE+2GE/120 W）$30.25** · `EZ-08PSF-SFP` **$30.80** · `EZ-04PSF-FG` **$65.00**。
⇒ 我方 8 口千兆 PoE **$43.50–47.00** ⇒ **贵 44–55%** ⇒ **r58 说的「我方 $24–26 有 3.1–3.3×」是拿 100M 款价当千兆款用（错）**，且「$80 天花板」是零售价不是 B2B（也错）。
⇒ 🛑 **「我们 8 口更便宜」这句话不能说，是假的**；8 口只讲「+48% 价格换管理/云/Watchdog」。**EZCOOL 没有工厂 ⇒ 它是 ODM 客户，不是对手**（与 Technopc 同模型）。

### 四、⭐⭐ DMO 在册经销商 17 家（本轮新增 13 家，全带电话）
**安卡拉 0312 系 5 家**：`EKSPA` **0312 463 88 88**（Cisco）· `4S / DÖRT US BİLİŞİM` **0312 472 90 00**（Cisco）· `ROKHSİS` **0312 258 64 59**（Cisco，**合同 2026-11-07 到期，距今 2 天**）· `REFLEKS` **0312 220 04 44**（Alcatel，到 2027-05-28）· FS Grup。
**单品牌独家系**：`DATANETSOFT` **0545 314 98 82**（Zyxel **21 SKU 全独家**）· `DUGAN`（Zyxel 第二供）· `RİVO TEKNOLOJİ`（**Dahua 27 SKU**）· `BİLGİBİM`/`ROBİT`（Cisco）· `BEYAZ`/`NETCOM`（Fortinet）· `ARTIKANAL`/`MEGA`（Aruba）。
⇒ **r56 待办①「找 FS Grup 同类」的答案就是 EKSPA 与 4S**（安卡拉 Cisco 双雄，体量最大、最可能加一条白牌线做预算段）。
⇒ **DMO 结构 = 一家吃一个品牌** ⇒ 换线空间只在「无独家品牌」或「独家品牌不够强」的那家。

### 五、⭐ 方法论修正：零售价与 DMO 价必须分成两张带
**零售 24 口 PoE**：$121（Zyxel GS1100-24）– $896（Dahua PFS4428-24GT-370），主力 **$231–480** ⇒ 我方 FOB **1.7–6.9×**。
**DMO 24 口 PoE**：$413 – $1,337，主力 **$650–1,130** ⇒ 我方 FOB **4.6–19.1×**。
⇒ **同一台机器在 DMO 里比零售贵 2–3 倍是常态**。以后**所有倍率必须分别对零售客户与投标客户做**，不许再混用一个数。

**诚实边界**：DMO 仅按交换机类目取样（页码已见 p≥105，未数完总条目）；`HUAWEI S5735-L48LP4XE-A-V2`/`PLANET IGS-6325`/`ALCATEL OS6860N-P48M`/`ALLIED TELESIS AT-X530L-28GTX` 只见型号未见价；13 家新经销商只有电话没有采购负责人；`guvenlikavm` 的 TL 与 USD 价隐含汇率 48.5，不可与 50.02 混用。

## §54 · 第 60 轮 — 2026-11-01 ≈01:50–04:20 (+0800)：**我方 2.5G 全线 7+1 款拿齐** + Tria 主体 + 修正指针双向落地

用户第 13 次「AB继续挖 挖完为止」。**0 新客户**；本轮结清两笔欠账，并把 r59 的修正写进被推翻的原文旁边。

### 一、⭐⭐ 我方 2.5G 全线（`ewindnet.com` 规格页原文，**型号齐、价格缺**）
非管理线：`EW-S6805F`（5×2.5G + 1×10G，60 Gbps/4K）· `EW-S6806`（4+2）· `EW-S6809`（8+1）· `EW-S6818`（16+2，120 Gbps/16K）· `EW-S6826`（24+2，160 Gbps/16K），全部 **12V 外置电源、端口防雷 6KV / ESD 8KV**。
管理线：**`EW-S2910SM-DP`**（8×GE PoE + 2×2.5G SFP，Lite 管理，26 Gbps/8K，8 口 af/at 30 W，**外置电源**，**3 年保修**）· **`EW-S57930TM-AP`**（**24×2.5GE PoE + 6×10G SFP+，L3，1–24 口 af/at/bt，1–8 口 bt**）· 工业 **`EW-PIS6810M-8GE`**（8×GE PoE + 2×1G/2.5G SFP，**192 Gbps**，DC48–57V 双冗余，IP40，**5 年保修**）。
⇒ **FOREDGE 9 款 vs 我方 7+1 款**：双方 2.5G 都不缺 ⇒ **2.5G 是入场券不是差异化牌**。真正的差异在 **`EW-S57930TM-AP` 多 2 个 10G 口 + bt**（对比 `PS3024XGPSH` 24×2.5G+4×10G 无 bt，$447.9–560.2）。
⇒ 🛑 **价格仍缺**：`S6805F`/`S6806`/`S6809`/`S6818`/`S6826`/`S2910SM-DP`/`S57930TM-AP`/`PIS6810M-8GE` 阿里均未挂价，**只有官网规格页** ⇒ **这不再是搜索问题，只能走内部报价单**。唯一可用价：4 口 2.5G PoE **$40 / MOQ 10**（索引级）。
⇒ ⚠ **型号陷阱**：`EW-S2910SM-DP` 是**外置电源**，投标写「300 W 内置」会写错型号。

### 二、⭐ `Tria Güvenlik` 主体（r58 欠账）
**TRİA GÜVENLİK SİSTEMLERİ SAN. TİC. LTD. ŞTİ.**，**安塔利亚 Muratpaşa / Kızılsaray Mah. Yener Ulusoy Bul. 86 Sk. Ali ve Oğuz Apt. No:4/C**，**0242 244 00 08**，`info@triaguvenlik.com`（经销申请 `bilgi@`）。原文 **`Sadece Bayilik Sistemi İle Satış`**（只做经销，需税号 + 合同 + 人工审批）。自有 **`DZ-`** 前缀（`DZ-2018SPD-A5` PTZ、`DZ-PS316G`/`DZ-GPOE408`/`DZ-PS208G` 交换机）。上游 = **Tiandy 分销商** + **Cenova（宇视）安塔利亚区域经理部**。
⇒ **它是「要白牌货源」的一方，不是终客户**；建议编号 **#147 / A-**，但**是否纳入管线由用户决定**（未纳入前不写客户档案，不合并进 #35 Antalya Turkuaz）。

### 三、修正指针双向落地（r48 规则）
`125` 末尾加「⚠ r59/r60 修正」框：MOQ/交期武器**不受影响**，但「倍率 2–4×」只对非管理 24 口 / 百兆 / 低端工业成立。`126` §三顶部加「本表已被 r59 部分推翻」框，逐行标 ⬆3.31× / ⬇1.65× / 🛑10G 1.24–1.32× / 🛑工业 bt 1.14× / 🆕48 口 1.25–1.35×。

### 四、竞争补点
同规格对手 **GXCOM（广州）**：`10G/2.5G 工业 L2 管理 PoE 8×GE + 4×2.5G + 2×10G，双 DC 12–54V` = **$118 / $115 / $108**（2–99 / 100–499 / ≥500），**store rating 4.8/5、Network Switches 类目 #1 best seller、3 天发货、免运费** ⇒ **比我方同档（$158–330）便宜且发货更快**，这是本轮唯一让我方难看的数据，必须记住。

**诚实边界**：2.5G 全线 FOB 缺失（官网只有规格）；Tria 员工数/营收/税号未取到；`DZ-` 是否全自有未证实；GXCOM 价为**竞品**报价非我方。

## §53 · 第 59 轮 — 2026-11-01 ≈23:00–01:40 (+0800)：**型号级 FOB 到手，r57 的高倍率结论被推翻** + 5 年保修

用户第 12 次「AB继续挖 挖完为止」。**0 新客户**；本轮是**自我纠错轮** —— 拿到型号级 FOB 后 r57 的倍率表塌了一半。

### 一、🛑 两条推翻（按 r48 规则点名）
| 被推翻 | 原结论 | 现结论 |
|---|---|---|
| **r57 §三** | 24×GE PoE +4×10G 倍率 **3.86–4.30×** | **1.24–1.32×**（我方 `$309–329` vs FOREDGE `PS3028GT` $408.8） |
| **r57 §三** | 工业 8×GE PoE 倍率 **3.70–3.94×** | **1.14×**（bt 款 `EW-PIS3810M-8GE-BT` $158.66 vs `IS1010GPS` $181.2）／ **2.01–2.70×**（低端款 $67–90） |
| **r57 §三** | 24×GE PoE 倍率 **2.18–2.44×**（按 $95–106 估） | **3.31×**（`EW-S1828CG-AP` **$70**，24×PoE+2RJ45+2SFP **300 W**）／ **1.65×**（管理型 `EW-S1926CG-AP-AT` **$140**） |

⇒ **倍率从 1.14× 到 3.31×，方向与直觉相反：越低端越有价格空间，越高端的我方越不便宜。** r57 的错因是**把非管理 24 口的价格套到了 10G / bt 工业型号上**。

### 二、⭐⭐ 我方型号级 FOB 全表（2026-11-01 阿里快照）
`EW-S1810CF-AP` 8×100M PoE **$22.55/22.15/21.55**（2–99/100–499/≥500，样品 $23）· `EW-S1806CF-AP` 4×100M PoE $21.50–23.50 · `EW-S1827CF-AP` **16×100M PoE + 3×GE 上联 $99–112.50** · **`EW-S1828CG-AP` 24×PoE +2 RJ45 +2 SFP 300 W = $70** · `EW-S1926CG-AP-AT` 24×GE PoE 300 m Watchdog **$140.11–141.33** · `EW-S2948GM-AP` **48×GE PoE +4×10G 400 W = $425/438/450**（另一链接 $526.55–554.55）· `EW-PIS3810M-8GE-BT` **$158.66–160.88** · **`EW-PIS3810M-8GE-BP` $381.52 / $305.39 / $285.09**（1–499/500–999/≥1000）· `EW-PIS3824M-16GE` **$333.67–335.73** · 8×GE PoE+2 SFP 管理 **$43.50–45.90** · 8 口工业 GE PoE+2 光 $67 / $90 · 24 口 PoE「New Design」$55.80–65.20 · `EW-S5748GM` L3 48×GE+4×10/25G 非 PoE（无公开价）。
⇒ **阶梯折让极小**：`EW-S1810CF-AP` 100→500 台只降 **3%**；`EW-S2948GM-AP` 1→100 台降 **5.6%** ⇒ **「量大再谈」不是筹码**；唯一真阶梯是 **Bypass `EW-PIS3810M-8GE-BP` 1–499→500+ 降 20%**，适合 500 台框架协议。
⇒ **定制 LOGO/包装 MOQ 500**（原文）· **海运 $0.84/kg 起、50 kg 起、17–24 天** · 8 口工业机单台毛重 **3.000 kg** ⇒ 约 $2.5/台。

### 三、⭐⭐ 新武器：**5 年保修**
`EW-PIS3824M-16GE` datasheet 原文 **`ultra-long 5 years warranty`**（IP40 / 双电源冗余 / 无风扇 / MTBF 35 年 / 16×GE PoE + 8×GE SFP）。而 **DMO 主流是 24 个月**（FOREDGE、MOXA、Ruijie `S5310`·`S6150` 全 24 月，仅 `RG-S2915-*` 36 月）⇒ **工业段投标直接写 5 年，压过所有在册对手。**

### 四、三条销售纪律（取代 r57「16 口不主推」）
1. **主推非管理 24 口 300 W**（$70 → 客户 $150–180，3.3×）；2. **管理型/2.5G/10G 只讲 MOQ 1 台 + 5–7 天出样 + 5 年保修，不讲价**（价差仅 1.2–1.7×，讲了会被 Aruba `JL683A` $291 与 FOREDGE $408.8 反噬）；3. **工业段改口径**：不说「便宜 3–4 倍」，说「同价给你 bt + 5 年保修 + 300 m + 单口重启」。

### 五、Technopc ODM 收窄（r58 结论修正）
ODM 只在 **≤$150 档**成立：**24 口 300 W $70 → ODM $112–126**（Aruba $291 / FOREDGE $231.6）、**8 口 GE PoE $43.5–45.9 → $70–83**、**16×100M+3GE $99–112.5 → $159–203**（FOREDGE 无同档）。**明确不报**：bt 工业（$158.66×1.6 = $254 > `IS1010GPS` $181.2）、24+4×10G（$494–592 > $408.8）、48 口 PoE（$680–810 > $561.6）。

**诚实边界**：中「索引级」未逐页打开（`EW-S1828CG-AP` $70、`EW-S1926CG-AP-AT` $140、24+4×10G $309–329 等）；`EW-PIS6810M-8GE` 与我方 **8/16 口 2.5G PoE** 的确切价仍缺；阿里价随登录地/活动波动（同店同日已见 $240,000 与 $200K–500K 两种营收口径）⇒ **对外引用须标「2026-11-01 快照」**。

## §52 · 第 58 轮 — 2026-11-01 ≈19:40–22:50 (+0800)：**Technopc 零交换机 = ODM 缺口** + RESET/DAPA 联络档案 + 土耳其自有品牌低价带

用户第 11 次「AB继续挖 挖完为止」。**0 新客户**；本轮把 r57 名单**变成可联络的实体**，并解开 r53 的 Technopc「空目录」。

### 一、⭐⭐⭐ Technopc：网络品类只有 5 款 x86 盒子，**零个交换机 SKU**
`technopc.com.tr/network-urunleri/` 原文只有 **`FW801` / `FW622` / `FW57`（x86 防火墙）+ `NSW 4500` / `NTSN 6500F`（x86 SD-WAN）**；营销文案写满「gigabit ve 10G switch / PoE / L2-L3 / bulut yönetim」，但筛选结果 `Seçilen filtrelere uygun ürün bulunamadı`，`/urun-kategori/network-urunleri/switch/` = **404**，全部产品只有「Bize Ulaşın」无价格。
⇒ **r53「空目录」原因改写**：不是没上架，而是**交换机是纯宣传品类、没货源**。而管线 #75 原文写「Switch/AP/Firewall = 近期扩张配套品类；**工业 PoE 采购 E-wind**」⇒ **一个正在找交换机货源、且已在我方采购的土耳其本土品牌**。
⇒ **动作：不卖成品，谈 ODM**（我方 FOB × 1.6–1.8），仍低于 FOREDGE `PS3028GT` $408.8 与 Aruba `JL683A` $291。⚠ 前置欠账：我方 24 口+4×10G / 8 口 2.5G / 48 口 PoE 的 FOB 连续两轮未取得，**没有这三个数就发不出提案**。

### 二、⭐⭐ RESET 与 DAPA 联络档案（r57 名单落地）
**RESET BİLGİ TEKNOLOJİLERİ SAN. ve TİC. A.Ş.** — 伊斯坦布尔 Bahçelievler / Yenibosna **İstanbul Vizyon Park 4. Plaza Kat:3 No:304**；**+90 212 955 00 95**（fax 96）；**info@reset.com.tr**；**11–50 人 / 营收 <$5M**；认证 **ISO 9001 · 27001 · 20000-1**；品牌墙 **Dell · Huawei · Fortinet · Palo Alto · Cisco · Microsoft · IBM · VMware · Veeam · Ruijie**；客群原文 `Kamu kurumları, üniversiteler ve özel sektör`；创始人&CTO İsmail Kavak（第三方）。DMO 目录码 **`K4230`（S2915/S5310）+ `K5882`（S6150）**。
**DAPA TEKNOLOJİ SAN. ve TİC. A.Ş.** — 伊斯坦布尔 Bakırköy **Yeşilköy EGS Business Park No:12/1**；**+90 212 982 83 37**；**info@dapatek.com**；分支 **Adana（0322 408 01 01）+ Bolu Teknopark**；DAPA Bilişim **25 年以上**；主要负责人 **Aytaç Türkkolu**（D&B）；集团含 **Hitachi 空调授权分销** / 能源 / 化学 / 零售。DMO 里与 RESET **同价 88,232.39 ₺** 投 `RG-S5310-48GT4XS-P-E`。
⇒ **两家都是系统集成商不是纯分销**，靠集成能力而非价格竞争 ⇒ **最容易接受「多一条自有品牌线」**。DAPA **集团化 + 三地 + 25 年 + 仓储物流**，比 FS Grup（2017、单点、12 SKU）更适合做国代。

### 三、⭐⭐ 24 口 PoE 的天花板已经固定：一线品牌 **Aruba `JL683A` ION 1930-24G = 14,570 TL = $291**
⇒ 24 口 PoE 真实竞争带 = **FOREDGE $231.6 – Aruba $291**（Ruijie-Reyee `RG-ES124G-L` 非 PoE 24 口 $205）⇒ **报价 >$200 需要重新谈，<$150 客户几乎必然成交**。「比 Aruba 便宜」已无叙事价值。
⇒ 🛑 **8 口 GE PoE 被土耳其自有品牌打穿**：**EZCOOL `EZ-08PSF-FG`（8GE+2GE，PoE 120 W）= $80**、`EZ-08PSE`（8FE+2FE，120 W）**$55**、`EZ-04PSF-FG`（4GE+2GE 65 W）；Tria Güvenlik 自有 `DZ-PS316G`（16 口 240 W）/ `DZ-GPOE408` / `ODS-16P2U1S-200`。⇒ **8 口不敲门**（这一档拼本地库存与土语包装，不拼价）。
⇒ **`DZ-` / `ODS-` / EZCOOL = 土耳其白牌运营者**（与 Ewind→FOREDGE 同构）⇒ 本身即潜在 ODM 客户，下轮查主体。

### 四、⭐ 阿里店铺 MOQ 分布抽样（第 1–3 页 ≈52 个商品）
**1 piece 占约 3/4**（交换机/AP/注入器/分离器）；**1 pair**（户外 CPE 网桥 $44–74）；**10 pieces**（8 口百兆桌面 $5.20–7.20、WiFi5 路由 $30–35）；**99 pieces**（WiFi6 1800M 路由 $28.50–34.20）；**100 pieces**（IP66 单口延长器 $6.30–7.20）。
⇒ **「MOQ 1 台」只对交换机/AP 主线成立**，低货值品与 WiFi6 路由有门槛 ⇒ 对客户承诺时必须限定品类。店铺品类远宽于交换机（AP / 户外 CPE 桥 / 注入器 / 分离器 / 延长器 / 光模块）⇒ 对集成商可整包报价。

### 五、⭐ DMO 保修期字段（投标新发现）
`Garanti Süresi`：FOREDGE 两款 **24 月**、MOXA **24 月**、Ruijie `RG-S5310`/`RG-S6150` **24 月**，但 **`RG-S2915-10GT2MS-P-L` 与 `RG-S2915-24GT4MS-P-L` 是 36 月** ⇒ **3 年保修已是公共采购差异化点**，我方投标按 36 个月准备。

**诚实边界**：RESET/DAPA 只有 info@ 邮箱与第三方推测人物，**采购负责人姓名未取得**；Technopc 网络品类负责人未取得；EZCOOL / Tria 主体未查；DMO 仅取样未全类目翻页；我方三个关键 FOB 仍缺。

## §51 · 第 57 轮 — 2026-11-01 ≈16:10–19:30 (+0800)：**FOREDGE 25 个型号零售价全表 + DMO 合同价地图 + 4 家 DMO 注册经销商具名**

用户第 10 次「AB继续挖 挖完为止」。**0 新客户**；本轮是**价格情报轮**，把 r56 的「2–4× 倍率」从一句话变成一张按端口分档的表。

### 一、⭐⭐⭐ 24 口是利润区，16 口是绞肉机（倍率按档位分裂）

| 档位 | 我方 FOB | FOREDGE 零售 | 倍率 |
|---|---|---|---|
| 24×GE PoE +2 上联 | $95–106 | `PS3024GS` **$231.6** | **2.18–2.44×** |
| 24×GE PoE +4 SFP | $95–106 | `PS3024GR` **$363.6–374.2** | **3.43–3.94×** ⭐ |
| 24×GE PoE +4×10G | 待报价 | `PS3028GT` **$408.8** | **3.86–4.30×** ⭐⭐ |
| **16×GE PoE** | **$114–129** | `PS3016GS` **$187.5–214.4** | **1.45–1.88×** 🛑 |
| 工业 8×GE PoE +2 SFP | **$46–49** | `IS1010GPS` **$181.2** | **3.70–3.94×** ⭐⭐（且 FOREDGE 无 bt） |
| 工业 4×GE PoE +2 SFP | $46–49 | `IS104GPS-2F` **$156.0–212.0** | **3.18–4.61×** |

⇒ **销售纪律新增第 6 条：16 口 GE PoE 不要主推**（倍率不到 2×，是全系最薄）；主推 24 口带光口 / 24×2.5G / 工业 bt。

### 二、⭐⭐⭐ DMO 合同价：我方 FOB 的 4.8–14.1 倍
`S5700-24GP-4TFR`（FOREDGE，24 GE PoE + 4×10G / 360 W）= **$1,337 净价 / $1,604 含税**（FS GRUP）；`RG-S2915-24GT4MS-P-L`（Ruijie，24 GE PoE + 4×2.5G SFP / 370 W）= **$513.1 净价 / $615.8 含税**（RESET BİLGİ）。
⇒ **同配置 FOREDGE 比 Ruijie 贵 2.6 倍** ⇒ FOREDGE 在 DMO 是**高价挂单**，靠「目录稀疏、无同价对手」维持。
⇒ 我方 24 口 GE PoE FOB $95–106 ⇒ **报 $300–400 进目录仍低于所有在册对手**。**DMO 是准入战场，不是价格战场。**
⇒ **DMO 同型号双目录价差**：`RG-S5300-48GT4XS-E` $1,451 vs $1,096；`RG-CS83-24GT4XS-PD` $1,370 vs $1,081 ⇒ 谈判先问「按哪个 K 码目录」。
⇒ ⚠ **MOXA `EDS-G512E-8PoE-4GSFP-T` DMO 净价 $1,190，只有全球市价（DigiKey $3,088 / icomtech $2,885）的 38–45%** ⇒ 工业段公共采购是**真全球底价**，别用「比 MOXA 便宜」打标，要用「MOXA 没有的」（bt / 云 / 单口重启）。
⇒ **合同到期窗口**：MOXA 该条目 `12.02.2024 – 12.02.2026`（İNFOGEN）；Ruijie `RG-S5310-48GT4XS-P-E` 已于 **2025-11-01 过期**；`RG-S6150-24VS8CQ-X` 为 2026-03-09–2028-03-09 ⇒ **进目录要卡续签窗口**。

### 三、⭐⭐ r56 待办 ① 有名字了：4 家 DMO 注册网络设备供应商
`FS GRUP BİLİŞİM`（安卡拉，FOREDGE）· **`İNFOGEN DANIŞMANLIK VE BİLİŞİM A.Ş.`**（伊斯坦布尔，0216 7061845，MOXA）· **`RESET BİLGİ TEKNOLOJİLERİ SANAYİ ve TİCARET A.Ş.`**（Ruijie 主供）· **`DAPA TEKNOLOJİ SANAYİ VE TİCARET A.Ş.`**（Ruijie 同价第二供）。
⇒ **RESET 与 DAPA 是纯经销商、不绑制造，是首选**；FS Grup 已绑 FOREDGE（利益冲突，但只 12 条目录，产能没打满）。

### 四、⭐ FOREDGE 零售价全表 25 个型号（TL 挂牌 ÷ 50.02）
`PS3010GS` $110 · `PS3016GS` $187.5–214.4 · `PS3024GS` $231.6 · `PS3024GR` $363.6 · `PS3028GT` $408.8 · `PS5052GT` $561.6 · `PS2024GC` $235.5 · `NS6016GC` $72.6 · **`NS6024GC` $68.4（24 口比 16 口便宜！）** · `PS3008XGPSH` $348.3 · `PS3016XGPSH` $510.5 · `PS3024XGPSH` $447.9–560.2 · `IS104GPS-2F` $156–212 · `IS1010GPS` $181.2 · `IS1016GPS-4F` $402.6 · `IS1024GPS-8F-4TF` $805.2 · `S5700-24G-4FR` $274.6 · `S5700-24G-4TFR` $321.0 · `S5700-48G-4TFR` $377.2–464.5 · `S5700-24G-24F-4TF` $890.6–986.0 · `NS5032GXT` $625.8 · `S6700-24TF-2QF` $2,586.8 · `S6700-48TF-8QF` $8,832 · `S6700-32QF` $10,794.7 · AP/AC $72.5–180.6。
⇒ **同型号跨卖家价差 2%–36%**（`IS104GPS-2F` $156 vs $212；`PS3024XGPSH` $560 vs $448）⇒ **FOREDGE 无严格转售价管控**，可据此对经销商说「你到手价不会比隔壁高」。
⇒ `PS3024XGPSH` 规格自相矛盾（toptan「24 口 2.5G」vs parnet「16×2.5G + 8 GE」）⇒ 谈判素材，非攻击。
⇒ `surviku.com` 上架 **80 个 FOREDGE SKU 全部 0,00 TL 无价** ⇒ 「广铺货、不挂价」的分销打法。

### 五、Ewind 阿里店铺指标再次自相矛盾（第三次）
storefront 页：**4.5/5 · 211 评价 · 100% 按时 · ≤2h · US$240,000+ · 33 人 · 主市场 = 东南亚/东欧/中东**；商品详情页：**4.5/5 · 升为「Network Switches 类目第 3 名」· 复购 7% · 主市场 = 美国/伊拉克/英国/沙特/菲律宾**。
⇒ r56 记的「4.6/5 · 90.9% · US$460,000」与今天两处都不一样 ⇒ **阿里指标会随店铺/时点变化，对外一律不引用具体百分比**，只用「ISO 9001 + 2 条产线 + 中型工厂」。
⇒ 商品列表共 **54 页**（≈1,000+ 挂单），本轮只读第 1–2 页 36 个商品；MOQ 分布 **1 台为主，少量 10 / 100 台**（`EWIND OEM 8 口百兆` 10 台、`IP66 单口延长器` 100 台）。

**诚实边界**：toptanbilgisayar 品牌页实时返回 0 件（JS），该列取搜索索引快照；DMO 仅取样 switch 关键词，未全类目翻页；我方 48 口 PoE / 24 口+4×10G / 8×2.5G PoE 的 FOB 仍未取得，表内留空未估算；TÜRKPATENT 仍 CAPTCHA。

## §50 · 第 56 轮 — 2026-11-01 ≈13:20–16:00 (+0800)：**MOQ 1 台 / 5 天 = 我方唯一硬武器**（有数字了）+ Koza 关格 + FS Grup 身份

用户第 9 次「AB继续挖 挖完为止 每次多挖一些 把工作时间拉长」。**0 新客户**；**新开一份 Ewind 渠道档案**。

### 一、⭐⭐⭐ 第 55 轮遗留的「MOQ / 交期」不用问内部了 —— 阿里店铺就写着

| 项 | Ewind（阿里店铺原文） | FOREDGE（官网原文） |
|---|---|---|
| **MOQ** | **「Min. Order: 1 piece」**（多条链接逐字）；部分型号 10 pcs | **「MOQ 500 adetten başlar」** |
| **交期** | **1–20 台 = 5 天；21–50 = 5 天；51–100 = 7 天**（另一链接 1–50 = 7 天 / 51–500 = 10 天 / 501–1000 = 15 天） | **6–8 周（42–56 天）** |
| 打样 | **rapid sampling 3–7 days** | 未承诺 |

⇒ **MOQ 500× 优势、交期 6–10× 优势** = 首封信第一句。**诚实边界**：这是阿里零售挂单口径，对经销商应按 **100–200 台试单**承诺；客户若要 500 台以上且能等 8 周，则只剩价格。

### 二、⭐⭐ 公开 FOB 报价 + 渠道加价倍率（本轮最实用的尺子）
**24 口 GE PoE（2 GE 上联 + 1 SFP，af/at，300 W 内置电源）= $95–106**；16 口全千兆 PoE + 2 RJ45 + 2 SFP = **$114–129**；24 口 GE PoE（AF/AT 智能识别）= $112–124；工业 4/8/16/24 口 = **$46–49**；100M 8 口 = **$24–26**。
⇒ 对比 r54 土耳其零售（Besta $208–223 / ALFA $194 / `F2420GBL-A` $424）⇒ **渠道零售/FOB 倍率 = 2.0×–4.0×**。
⇒ **尺子**：客户目标价低于 FOB×2 = 压价；高于 ×4 = 我方有提价空间。

### 三、⚠ Ewind 店铺自述**六处互相矛盾**（引用必须标来源）
成立年份 **2017 vs 2019**；阿里年限 **7 YRS vs 1 YRS**；员工 **11–50 vs 33 vs 官网 200**；厂房 **3,000 ㎡ vs 10,000–30,000 ㎡**；产线 **2 条**；年产值 **「Below US$1 Million」vs 年营收 US$5–10 M**。
⇒ **两个店铺（`ewindnet.en` / `ewind.en`）= 两套资料**。**对外只讲**：中型工厂、2 条产线、年营收 500 万–1000 万美元级、ISO 9001、**按时交付 90.9%**（第三方口径）。
⇒ **绝不讲**「200 人 / 5000 ㎡ / 年产值低于 100 万美元」。
⇒ **工厂资质对比诚实结论**：FOREDGE **180,000 sqft / 3 条 SMT / 200 万台/年** 纸面强于我方 ⇒ **不比规模、不比认证数量，比 MOQ、交期、打样、RMA**。

### 四、⭐⭐ Koza 关格（三轮未取到，用站内 OpenCart 搜索拿到）
`?route=product/search&search=poe+switch` → **5 个型号，全部 TRENDnet**：`TN-P08G`（8×100M PoE + 2 GE，**120 W**）· `TN-P08FG` · **`TN-P16M`**（16×100M PoE + 2 GE，**360 W**）· `TN-P16MG` · **`TN-P24MG`**（**24×100M PoE** + 2 GE + 2 SFP）。
⇒ **无自有品牌、全线百兆、全线非管理、无 bt/2.5G/云** ⇒ 一刀 **`EW-S1927CG-AP`**；**首封只讲 GE + 300 m + Watchdog，不讲 2.5G**。

### 五、⭐ `FS Grup Bilişim` 身份（对 r55「300 渠道」降温）
**2017 年成立、安卡拉 Öveçler（Cevizlidere Mah. 1243. Sokak No:6/4）、IT 经销商**；DMO 目录里 **FOREDGE 仅 12 个条目**（+ MILESIGHT 1）。
⇒ **不是分公司，是一个能进 DMO 的安卡拉伙伴，不是全国性组织。** ⇒ **我方路径 = 找 FS Grup 的同类**，而非幻想铺 300 家。

### 六、BDCOM 工业补点
DMO 无独立 BDCOM 条目，但土耳其渠道完备（**Öncü Güvenlik** = BDCOM 分销：`IES2000-TU12S4T` 12×GE SFP + 4 GE TX / 256 Gbps / PTP / IP40；`IES2000-TU8S8T` 8 GE + 8 SFP / −40~85 °C）；**BDCOM 原厂阿里报价 `IES2000-TW8S8P`（L3，8 PoE + 8 SFP）≥5 台 $399**。
⇒ **工业段 FOB 锚 = $399**；我方 `EW-PIS3810M-8GE-BT` / `EW-EPIS3910-8GE` 报价应按此，而 **60 W bt + 云 + 单口重启** 仍是工业段的牌。

**诚实边界**：阿里价与 MOQ 均为**索引快照口径**，未逐条抓 270+ SKU；两个店铺主体是否同一家未知；FS Grup 与 FOREDGE 的代理性质未知；TÜRKPATENT 仍 CAPTCHA。

## §49 · 第 55 轮 — 2026-11-01 ≈10:40–13:10 (+0800)：**FOREDGE 全产品线打开 → r54 战略结论被彻底推翻** + DMO 价格地图

用户第 8 次「AB继续挖 挖完为止 每次多挖一些 把工作时间拉长」。**0 新客户**。

### 一、🛑 r54 的「三条差异化安全」被推翻 —— FOREDGE 什么都有

| r54 原判断 | r55 实测（`foredgetech.com/tr` 原文） |
|---|---|
| 无 2.5G | ❌ **9 款**：⭐ **`S6700-48GXP-4TF-2QF`（48×2.5G + 4×10G + 2×100G，PoE 1200 W，RunOS + Apollo Cloud）**、`PS3024XGPSH`、`PS3016XGPSH`、`PS3008XGPSH`、`NS3024XGSH`、`NS3016XGSH`、`NS3008XGSH`、`AI1009XG`、`AI1009XGP` |
| 无 802.3bt | ❌ 全线 **90 W/口**；`AI6016M`/`AI8016M`/`AI806G` 标 **60 W BT 口** |
| 无云 | ❌ **`Apollo Cloud`** 自有云平台（官网筛选器一栏） |
| （未评估） | ❌ **数据中心 6 款**：`S6700-24TF-2QF`（880 Gbps）、`S6700-32QF`（6.4 T）、`S6700-48TF-8QF-H`、`S6700-48YF-8QF-H`（25G）、`S6700-32CQ`（25.6 T）、**`S6700-64CQ`（64×400G / 51.2 Tbps / 38 Bpps）**，NOS = **SONiC 或自有 RunOS** |
| （未评估） | ❌ **它自己也做 OEM/ODM**：**180,000 sqft / 3 条 SMT / 年 200 万台 / MOQ 500 / 交期 6–8 周 / 2021 年起 12 个贴牌项目 / 每客户独立模具** |
| （未评估） | ❌ **土耳其本地案例**：官网 solutions 原文 **「Ankara'nın şehir çapındaki gözetim ve halka açık Wi-Fi altyapısını besleyen endüstriyel PoE switching」** = **安卡拉城市级监控 + 公共 Wi-Fi 已被它供过货** |

**企业/工业线共 72 个型号**（官网 `72 model bulundu`），筛选项含 **2.5G / 802.3bt Yüksek Güç / Apollo Cloud**。资质：**ISO 9001 / 14001 / 45001 · CE · FCC · RoHS · CQC**；自述 120+ 国家、累计 1 亿台、深圳研发。

### 二、⭐⭐ DMO 公共采购价格地图（`dmo.gov.tr` 实测）
交换与路由分类 **339 条**，区间 **458 ₺ – 2,033,781 ₺**。
| 品牌型号 | 规格 | DMO 价 |
|---|---|---|
| FOREDGE `S5700-24GP-4TFR` | 24 GE PoE + 4×10G / 360 W | **80,255.62 ₺ ≈ $1,604 含税** |
| FOREDGE `S5700-48GP-4TFR` | 48 GE PoE + 4×10G | **103,828.67 ₺ ≈ $2,076** |
| RUIJIE `RG-CS83-24GT4XS-PD` | 24 GE + 4×10G | **93,496.25 ₺ ≈ $1,869 未税** |
| RUIJIE `RG-S6150-24VS8CQ-X` | **24×10G/25G + 8×40/100G** | **198,026.22 ₺ ≈ $3,959 未税** |
| RUIJIE `RG-WS6816` | 无线控制器 | 290,728 ₺ |
| CISCO `IE-2000-16T67P-G-E` | 16 口工业 PoE，**产地中国** | **76,903.70 ₺ ≈ $1,537 含税** |
| 在册其它 | HPE Aruba CW5120v3 8G PoE · BDCOM `IES2000/IES200` · MOXA `EDS-G512E-8PoE-4GSFP-T` · RUCKUS · TR7 · ÜÇ-ER · RUBISEC | — |

⇒ **公共采购 24 口 GE PoE + 4×10G 的成交带 = $1,600–1,870 含税**；**24×10G/25G + 8×100G = $3,959**（我方 `EW-S53928QM` 有明显空间）；**CISCO 16 口工业 PoE 仅 $1,537 且产地中国** ⇒ 工业段洋品牌溢价只有 2–3 倍。

### 三、CCTV 渠道补点（ALFA / Karer / F2420GBL-A）
ALFA `AL-24PORT` 24 口 GE PoE **9,700 ₺ ≈ $194**；`AL-24-2PORT` **13,841.50 ₺ ≈ $277**；`F2420GBL-A` 24 GE PoE **21,213.65 ₺ ≈ $424**（同页其他 24 口机的 2 倍 ⇒ **渠道价 ≠ 成本价**）；无品牌 24 口 GE PoE **9,319.81 ₺ ≈ $186**。

### 四、r53 遗留收口：CryptoLink 最后两份 PDF
`CRL-MC02` = 100M 媒体转换器（1×100M RJ45 + 1×100M 光纤，ST/SC/FC，多模 2 km / 单模 20–120 km，<5 W，11×7×2.5 cm / 0.18 kg，−20~50 °C，MTBF 100k）。
`CRL-SFP-10G-LC` = 10G SFP+ 1310 nm，单模 20 km / 多模 2 km，1 W，0~70 °C —— ⚠ **正文却写「speed rate up to 155Mbps」**，与型号 **10G 自相矛盾** ⇒ 换牌沿用 OEM 模板未校对（与 r53 的 `CrystalWAN` 页眉同源）。**招标附件里可直接质疑**。

**诚实边界**：FOREDGE 剩余 30 型号未读；除 DMO 两个型号外无成交价；**FS Grup 是分公司还是代理未知**；我方 MOQ/打样周期**尚未向内部确认**（这已是唯一可打的牌）；Koza 型号仍空白；TÜRKPATENT 仍 CAPTCHA。

## §48 · 第 54 轮 — 2026-11-01 ≈08:00–10:30 (+0800)：**B 档 11 家做到型号级** + **价格锚点全部重建** + 新竞对 **FOREDGE**

用户第 7 次「AB继续挖 挖完为止 每次多挖一些 把工作时间拉长」。**0 新客户**，**9 份 B 档档案加 r54 附录**，**新增竞对专档 `06-competitors/128`**。

### 一、⭐⭐ B 档「已在卖交换机」11 家：型号级结果

| # | 公司 | 真实品牌 | 关键型号 / 最高档 |
|---|---|---|---|
| 6 | **Coptek** | ⚠ **DCN（神州数码）+ ONV 双代理**（官网自曝「DCN Private MIB」「DCN firmasına ait MRPP」） | ⭐ **`S4600-12X-P-SI` = 24×2.5G + 4×10G + 2×40G QSFP+，530 W**；`S5750X` 6×10G + **750 W**；`CS6200X` **1000 W**；ONV `POE33052PFM` 48 口 **600 W** |
| 18 | **iotsistem** | ⚠ **MLiS**（`MLB-` 前缀，澳洲媒体公告为证） | `MLB-E4204-28-F` **24×100M** + 4 SFP；⭐ `MLB-E4212-8-G-P-F` 6 PoE **60 W/口**；`MLB-E4104-5-P-F` −40~75 °C |
| 62 | **Cebeci** | ⚠ **FOREDGE**（中国，DMO 合同） | `S5700-48GP-4TFR` 48 PoE + 4×10G，176 Gbps |
| 79 | **Eurocam** | ✅ 自有 EUROCAM / EUROLINK | `EC-SWG24-POE` 24GE PoE + 2 SFP **400 W**；**已在宣传「0-250 M」** |
| 19 | **Lansan** | ✅ 自有 LANSAN `LNS-` | 21 SKU，`LNS-1324P` 24 口 PoE **$1,427** 挂牌 |
| 49 | **Zeytek** | ✅ 自有 **`ZT-`**（本轮新发现） | `ZT-SP1026HP` 24×GE PoE **450 W**（非管理）；`ZT-816-P24` 唯一 L2 但百兆 |
| 15 | **Koza** | ⚠ 确认有「PoE Switchler」类目 | **型号未取到（空白）** |
| 33 | **HCS** | — | 复核仍**无有源** |
| 35 | **Antalya Turkuaz** | 代理 TP-Link/Omada/VIGI | 本轮未取新证据（如实标注） |

**三处自我修正**：① r47「B 档只到 GE + af/at 30 W」**不成立**（Coptek 2.5G+40G/750–1000 W、iotsistem 60 W/口、Zeytek 450 W、Eurocam 400 W）；② r47「iotsistem 缺 bt」**不准确**（已有 60 W/口 8 口级工业机）；③ r49/r50「300 m 是差异点」**已被打平**（Eurocam「0-250 M」、Besta「305 Metre」）。

### 二、⭐⭐ 价格锚点重建（USD/TRY = **50.02**，2026-11-04）
- **汇率修正**：Dayline 17,949 ₺ = **≈ US$359**，旧记 **$423 作废**（`116`/`120` 已改）。
- **新发现 CCTV 渠道低价带**（此前无此层）：Besta `BST2422G` 24×100M PoE + 2 SFP，**305 m**，**11,104.81 ₺ ≈ $222**；Multitek `SWITCH24-POE` **240 USD + KDV**；Besta 24 口 GE PoE **10,380–11,158 ₺ ≈ $208–223**；Besta 8 口 120 W **2,009 ₺ ≈ $40**。
- **新 DMO 公共采购锚点**：`FOREDGE S5700-24GP-4TFR`（24 PoE + 4×10G / 360 W / 128 Gbps）**80,255.62 ₺ 含税 ≈ $1,604**；`S5700-48GP-4TFR`（48 PoE + 4×10G / 176 Gbps / 130.9 Mpps）**103,828.67 ₺ ≈ $2,076**；非 PoE `S5700-24G-4TFR` **299.28 USD+KDV**。
- **第四公开 USD 价源**：Lansan `LNS-1324P` **$1,427**、`LNS-1310P` **$1,000**、`LNS-1308` **$1,755**、10G 网卡 $1,016–$3,303。
- ⇒ **四档报价纪律**：**A CCTV 杂牌 $200–290（不打）· B 中国白牌/DMO $1,300–1,600 含税 · C 品牌渠道 $359–900 · D 高价小品牌 $1,427 挂牌**。**对 A 档客户不报 B 档价，对 D 档客户不报 C 档价。**

### 三、⚠ 新竞对专档：`06-competitors/128-foredge-white-label-competitor-2026-11-01.md`
FOREDGE = 中国品牌 + `foredgetech.com/tr` 土耳其语站 + **300+ 本地渠道** + **DMO 框架合同（2024-10-21→2026-10-21，供应商 FS Grup Bilişim，Menşei Çin）** + **BROADCOM** 芯片。
**它没有：2.5G / 802.3bt / 云** ⇒ **我方三条命必须第一封信就出现**，否则被当成「又一家 FOREDGE」。
**反向机会**：它的 300 渠道里「卖 2.5G 项目的人没货可卖」= **我方最快的分销候选**。

**诚实边界**：Koza 型号级未取；FOREDGE 全型号表未取、FS Grup 是代理还是分公司未知；`S4600-12X-P-SI` 成交价未知；Cebeci↔Foredge 合作层级未知；Lansan 24 口机是否 GE 未知。

## §47 · 第 53 轮 — 2026-11-01 ≈06:20–07:40 (+0800)：**规格实锤** —— CLR 2.5G 就是 bt 机（推翻 r52）+ CryptoLink 换牌实证 + Technopc 目录是空的

用户第 6 次「AB继续挖 挖完为止」。**0 新客户**。

### 一、🛑 修正 r52：`CLR-MRS-8330P` = 24×2.5G PoE，**1–4 口 802.3bt 90 W**，**总 400 W**

r52 写「没有一款 2.5G SKU 标 802.3bt」「`-8330P` 功率未知」「2.5G PoE 只有 100 W」——**三条全错**。
产品页技术表原文：`Ethernet: 24* 100/1000/2500 Mbps PoE Ports (Ports 1-4 support IEEE802.3bt(90W))`、`PoE Total Power maximum 400W`、电源 `DC 54V 7.69A + 12V 5A`。
全表：**240 Gbps / 178.56 Mpps / DDR 512 MB / Flash 32 MB / MAC 32K / Jumbo 10K / VLAN 1–4094 / 802.3az / 440×281×44 mm / N.W 4.37 kg / CE FCC RoHS**；**PoE 使用率指示灯**（<90% 灭 / 90–95% 闪 / >95% 亮）。
⭐ **两个可打的短板**：**工作温度仅 −10~50 °C**（商用机箱）；**L3 只到 IPv4 静态路由 + ARP，无 OSPF / 无 VRRP**（而同定位的 `CRL-SW-L3-2404-10G` 反而有 OSPF+VRRP）。
→ **真实缝隙改写为「24 口全 bt + 800 W」**（它 24 口只 4 口 bt、400 W、均摊 ≈16.7 W/口），对位 `EW-PIS5728GM-AP-BT`；再加「要 OSPF/VRRP 它没有」。
→ `CLR-MRS-8312P` 口径核实：**8 口 2.5G PoE，25 W/口上限、总 250 W**。

### 二、⚠ 必须承认：它有两档比我方齐（回传产品部）

| 档位 | CLR 型号 | 我方 |
|---|---|---|
| **10G 电口接入** | ⭐ **`CLR-SWT-7514C` = 12×10G RJ45 + 2×SFP+ 全 10G 网管** | **无对位** |
| **工业 10G SFP+ 骨干** | ⭐ **`CLR-IES-T120N` = 12×1G/10G SFP+，240 Gbps / 178.56 Mpps，双核 1 GHz，4 Gbit DRAM，32K MAC，DC12–48 V 防反接，−40~+85 °C，25 W，导轨 166×150×75** | 工业最高 8 口 GE |

r53 新增 CLR 型号：`CLR-SWT-7514C`（12×10G RJ45）、`CLR-SWT-7520F`（8 RJ45 + 12 SFP+）、`CLR-SWT-7312F`（12×SFP+ L3）、`CLR-SWT-4804N`（48 GE + 4×10G）、`CLR-SWG-1724`（24 GE 非网管）、`CLR-IES-T120N`。**累计 17 类 40+ 型号。**

### 三、⭐⭐ CryptoLink：PDF 里还留着原厂牌子 **`CrystalWAN Network Solutions`**

`DatasheetofCRLISW-14.pdf` **封面页眉 = `CrystalWAN Network Solutions`**，内页型号 **`CRLISW-414`**；`CRLISW-08.pdf` 内页型号 **`CRLISW-8P`**。**一份 PDF 三个名字** ⇒ 只改封面的换牌。
- `CRLISW-8P`：**8×GE PoE + 2×GE SFP + Console**，af/at，**总 240 W**，24 Gbps，8K MAC，**ERPS + PD Alive**，双路 **DC48–55 V**，**−40~85 °C**，**IP40**，防雷 6/4 kV，MTBF 100k。
- `CRLISW-414`：**8×GE PoE + 4×GE SFP**，af/at，**总 120 W**，**16K MAC**，MTBF **800k**。
→ **工业段 100% 停在 af/at 30 W** ⇒ 对「边界安全 / 车牌识别」的 bt 60 W 需求，我方 `EW-PIS3810M-8GE-BT` / `EW-EPIS3910-8GE` 是干净一刀。

### 四、⭐⭐ Technopc（`A/075`）：**想卖交换机，但目录是空的**

`technopc.com.tr/network-urunleri/` 营销承诺 **「gigabit ve 10G destekli switch … Layer 2/3 … bulut tabanlı yönetim」**，实际只有 **5 个产品、全是防火墙与 SD-WAN**（`FW801` / `FW622` / `FW57` / `NSW 4500` / `NTSN 6500F`），页面底部原文 **「Seçilen filtrelere uygun ürün bulunamadı.」**，`/switch/` = **404**。
⇒ **全名单唯一「已是我方客户 + 公开要做交换机 + 目录为空」的 A 档**：评级 **55 → 70**，打法从"开发新客户"改为**"扩品类"**（`EW-S1927CG-AP` → `EW-S2926GM-AP` → `EW-S5748GM-AP` → `EW-S6826` 做 `Technopc` 牌首屏 + `EwindCloud` 对应它写的 bulut）。它强项是 x86（Atom/Celeron/Intel），**交换机纯外购、无自研冲突**，比 Telkolink 好谈。

**诚实边界**：`CLR-MC02` / `CRL-SFP-10G-LC` / `CRL-SFP-125 LC` 三份 PDF 未读；`CLR-MRS-8226N/8218N` 交换容量未知；`CLR-MRS-8109P` 的 100 W 是否含 bt 口未知；Technopc 是否已有未上架交换机 SKU 未知。

## §46 · 第 52 轮 — 2026-11-01 ≈04:30–06:10 (+0800)：**「自有品牌」大清算** —— 三家 A 档其实是代理商 + **四项自我证伪**

用户第 5 次「AB继续挖 挖完为止」。**0 新客户**，把 `A/001` `A/005` `A/054` 三家做到型号级，并**推翻自己 r51 的横切结论**。

### 一、⭐⭐ 最大增量：`A/001` Telkolink/GelecekBT **不是待开发的缺口，是我方最强的对手**

`gelecekbt.com/anahtarlar?limit=100` 全目录 facet 原文：**Ethernet Switch 122 · POE Switch 126 · 工业 73 · 工业 PoE 60 · 工业骨干 10 · 骨干光纤 57 · 10G 104 · Multirate(1G/2.5G/10G) 15 · SFP 112 · POE AI 22 · PD PoE 7** ⇒ **交换机 ≈291 SKU**，**25 个品牌**，其中 **`CLR Networks` 193 个**。

**品牌真相**：自家幻灯片「**CLR Networks Türkiye dağıtıcısı GelecekBT'dir**」+ guvenlikonline 企业页「CLR Networks、ONET、Telkolink、Netkablo gibi markaların Türkiye dağıtıcısıdır」⇒ **CLR = 深圳品牌，它是土耳其分销商**，不是自有商标。

**🛑 四项自我证伪（直接推翻 `116` 四行）**：
| 原判断 | 实测 |
|---|---|
| 2.5G 11 家 0 家 | ❌ `CLR-MRS-8106N/8106P/8109N/8109P/8218N/8226N/8312N/P/8330N/P` 整条线，最高 **24×2.5G PoE + 6×10G SFP L3**；另有 **`CLR-DCS-2110N/P` = 24×2.5G + 100G 上联 L3** |
| bt 只有 1–4 口 | ❌ facet `Tip3 60W` **3** · `Tip4 90W` **1** · `802.3bt` **6**；`CLR-SWF-9006BT` **96 W** |
| 云管理 0 家 | ❌ facet `Cloud` **15** · `Yapay Zeka` **12**；`CLR-SWT-5736F/3754F` 标 **L3 Cloud** |
| 40/100G 0 家 | ❌ 100G 上联 **6** · 100G 交换机 **9** · 400G **1**；`CLR-DCS-6332F/6432F` = **32×40/100G QSFP28** |

→ **它真正还缺的只有四条**：① 2.5G PoE 功率（`-8109P` 仅 **100 W**、`-8330P` 无标注）；② 工业 bt（73 款里 90 W 单口只 1 个）；③ `POE Extend` 18 / `POE Watchdog` 14（291 SKU 里）；④ SFP 112 SKU 是它的现金牛（我方齐套供）。
→ **打法改写**：从「补位」改为「**同档位更低 ODM 成本 + 可贴 CLR 牌 + 2.5G×bt 组合**」；**一半客户一半竞对，不交完整 BOM**。

### 二、⭐⭐ `A/005` CryptoLink：`CRL` 也不是自有品牌

7 份 PDF **页脚全部**印 **`CryptoLINK.  Authorized Dealer | Cryptolink Elektronik Güvenlik Sistemleri San ve Tic. Ltd. Şti`**，`CRL-SW-2402` 页眉出现 **`Cryptol.net`** 字样 ⇒ **CRL 属第三方，它是授权经销商**。
- ⭐ `CRL-SW-L3-2404-10G`：**24×GE PoE + 8 Combo + 4×10G SFP+**，**BCM**，**128 Gbps / 96 Mpps**，MAC 12K，**总 360 W**，**af/at 仅 30 W**，**静态+RIP+OSPF+VRRP**，−20~50 °C；变体 `-8C`（24×SFP 全光）/ `-8C-POE`。
- `CRL-SW-2402`：24×PoE + 2×SFP，52 Gbps，**总 300 W**，防雷 6 kV/4 kV/ESD 15 kV。
- 它客户 = **边界安全 / 车牌识别 / 政府项目** ⇒ 谈**工业宽温 + 冗余电源 + 防雷**，不谈云。

### 三、⭐ `A/054` TekniksatGroup(TGD)：**24 V 被动 PoE 的一对一对位**

TGD 全表：`TGD-P4/24`、`TGD-P8S/24`（**24 V 被动**，1,2+/3,6−）、`TGD-P4/48`、`P8/48`、`P16S/48`、`P24S/48`、`P424/824/848`、`[SWITCH]` 5 口非网管。
**关键上下文**：同目录并列 `TGD-7IP24/7IP48`（7 吋 IP 对讲主机）、`TGD-4K24`、`TGD-GU10 S1` ⇒ **这些交换机是给 24 V 对讲配套**，全线**非网管、无云、无远程重启**；自述 **「Üretim tasarım uygulama %100 yerli」**。
→ ⭐ 一刀：**`EW-EPIS3910-8GE`**（1–2 口 DIP 选 **12/24 V 被动** + 48 V 30/60 W + 云 + **单口远程重启**）一台覆盖它三台机；卖点「**对讲主机死机不用上门**」。

### 四、⚠ 由此得出**通用判据**（已写入 `121` §四）

| 现象 | 身份 | 谈法 |
|---|---|---|
| 有自家型号命名（`NVC-/SWP-/LNG/TGD-/CRL-`） | 未必自有 | **必须查商标** |
| 页脚 **"Authorized Dealer"** / 官网写 **"…Türkiye dağıtıcısı"** | **代理** | 谈二供/替换上游，不谈 OEM |
| 有 **TÜRKPATENT 注册号**（upTech **2008/13951**） | **真自有** | OEM 贴牌成立 |

已核：`upTech` 真自有 · `CLR` 代理 · `CRL` 代理 · `Cifocs/Dayline/TGD/NVC/SWP/LNG` **商标未查**。

**诚实边界**：`CLR-MRS-8330P` 功率未知；CLR 是否独家未知；CLR 的深圳工厂名未知（**是否与我方同厂未知**）；`CRLISW-08/14P` 未读；TGD 交换机自产/外协未知。

## §45 · 第 51 轮 — 2026-11-01 ≈03:00–04:20 (+0800)：A 档**自有品牌交换机线**型号级对位 + **第二个价格锚点**

用户：「AB继续挖 挖完为止」。**0 新客户**，**4 家 A 档自有品牌线一次做到型号级**。

### 一、⭐⭐ 最大增量：Snexus **公开美元价目表**

`A/003 Snexus` 把美元零售价直接印在官网分类页（`Excluding GST/HST`）——
**这是全项目第二个公开价源，也是第一个「自有品牌 + L3 + 10G」的美元价**：

| 型号 | 规格 | 价 |
|---|---|---|
| `SN-GS2300-10F / 10FP` | 8 口 GE（非 PoE / PoE），L2 | **$320 / $400** |
| `SN-GS2300-28F / 28FP` | 24 口 GE（非 PoE / **PoE**），L2 | **$660 / $900** |
| `SN-XGS5300-28F / **28FP**` | 24×GE（+PoE）**+4×10G**，**L3** | $1,130 / **$2,050** |
| `SN-XGS5300-52F / 52FP` | 48×GE（+PoE）+4×10G，L3 | $2,050 / **$2,750** |

**加上已有的 Winet 2,916.76 ₺ 与 Cenova/Dayline 17,949 ₺ ≈ US$423**，现在**24 口千兆 PoE 的市场区间被完整框定**：
**US$423（非网管零售）～ US$900（L2 网管零售）**。
→ **报价纪律：非网管（`EW-S1927CG-AP`）打 $423 档、网管（`EW-S2926GM-AP`）打 $900 档，混报一次丢一档。**

### 二、四家型号级全表（结论：与 B 档完全一致）

| 客户 | 型号数 | 旗舰型号 | 命门 |
|---|---|---|---|
| **`A/002` Novacom** | **13** | `NVC-HIF2422GBL-C`（**24×100M** PoE + 2×GE + 2 Combo，400 W，AI Watchdog） | **24 口还是百兆** |
| **`A/003` Snexus** | **7 段线** | `SN-XGS5300`（L3 24/48 + 4×10G） | 无 2.5G / 无 bt / 非网管只 1 款 |
| **`A/004` Cenova（Dayline）** | **12** | `SWP-POE31024PFB`（24×GE PoE 440 W，宣传 **20–120 km**） | **24 口主力仍是百兆**、无 bt |
| **`A/146` Longline（LNG）** | **20+** | `LNGIGF26GT-24POE-M`（"28 口"口径，400 W，**L2**） | 工业全线 **30 W/口封顶** |

**统一水位**：**四家 0 款 2.5G、0 款 802.3bt、0 款云管理**；24 口有相当比例还是百兆。
→ **这是土耳其渠道的整体技术水位，不是某一家的问题** —— 也让"2.5G + 全口 bt"这条主线**在 A 档同样成立**。

### 三、两个战术级发现

1. **Longline 的「20 口 / 28 口」是营销口径**（把 uplink 与 SFP 算进端口数）：`LNGIGF18GT-16POE` 实为 16 PoE + 2 uplink + 2 SFP。
   → **跟它比规格必须同口径报总端口数**：`EW-PIS3620M-16GE`（16 PoE + 4 SFP = 20 口）↔ 它 20 口；`EW-PIS5728GM-AP`（28 口）↔ 它 28 口。
2. **Cenova 的「20–120 km」说明它的客户是园区/城域光纤项目** → 我方应做**交换机 + 长距 SFP 捆绑报价**，用整包价打它"只卖机头"。

### 四、产出与规模

- 新增 `08-customer-pipeline/120-a-tier-own-brand-switch-lines-2026-11-01.md`。
- 新增 `r51_appendix_data.py`，`build_tr_customers_r44.py` 已接入（**并首次支持 146 Longline 这条独立分支**）→ `A/002` `A/003` `A/004` `A/146` 各增 **「附：r51 自有品牌线型号级对位」**。
- `116` 新增 **§二 Snexus 价格锚点**（含四档市场区间表）。
- 根 `README.md` 增 `120` 链接。
- 目录 **14,062 → 14,404 行（+342）**；文件数不变（146 客户 MD + README）。

### 五、方法与诚实边界

**新方法**：① **经销商/比价站是"自有品牌型号"的第二信源**（Cenova 的 `SWP-POE33028PF-AT` 零售价来自 34alarm，官网没有价）；② **Wix/商城类官网把价格印在分类页** → `Snexus` 一次拿到 8 个美元价；③ **端口数口径必须先对齐再比规格**（Longline 的 20/28 口）。
**诚实边界**：Snexus/Cenova 的价均为**零售含税口径的外币标价**，**不是 FOB**；`HIF0820FBL-C` 等中间型号的 PoE 预算、`330XX` 系 PoE 预算、`LNG3000-8TP4S-IK` 是否带 10G —— **仍空白**，已逐家标注；**Dayline 与 Cifocs 的商标注册人仍未查**（同一次 TÜRKPATENT 查询可一起解决）。

