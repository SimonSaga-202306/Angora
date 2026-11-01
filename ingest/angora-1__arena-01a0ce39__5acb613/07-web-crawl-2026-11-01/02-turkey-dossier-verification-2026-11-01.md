# r42 · 土耳其客户档案外部核验 · 抓取记录（2026-11-01）

**这一轮是什么**：对 `08-followup-dossiers-2026-11-01/` 里的客户档案做**公开网络独立核验**，目标是「哪些结论站得住、哪些站不住」。

- **抓取时间**：全部为 **2026-11-01（Asia/Shanghai）**，北京时间当日白天单次会话内完成。
- **抓取方式**：本环境 bash **无外网出口**，全部 HTTP 经 `fetch_page` 工具完成 → **本文件是唯一存证**（原始 HTML/PDF 字节未落盘）。
- **写入位置**：5 份 dossier 各自末尾的 `## 核验补录 2026-11-01`；本文件是**抓取侧台账**（按 URL 归档），两者互不替代。
- **核验对象**：04 Cenova、08 Selim Kalaka、09 Okisan、10 Optima、11 Karer（其余 16 家**本轮未核验**，等级不变）。

---

## 一、抓取台账（逐条，按发生顺序）

| # | URL | 结果 | 提取到的关键内容 |
|---|---|---|---|
| 1 | `https://www.cenova.com.tr/` (chunk 0) | OK | 品牌板块 Dayzip/Wisetech/Dayline（相机为主），CN-* SKU，Teknolojilerimiz 文章停在 2023 |
| 2 | `https://www.cenova.com.tr/arama?q=ewind` | **空**（路由坏） | 返回产品详情空模板，无搜索结果 |
| 3 | `https://www.cenova.com.tr/sitemap.xml` | **404** | `404 - File or directory not found`（ASP.NET，无 sitemap） |
| 4 | `https://www.cenova.com.tr/` (chunk 1) | OK | 「Markalarımız」全列：**tiandy / cenova / gvd / wisetech / bawcon / dayzip / dayline**；社媒 IG/FB/YT/X |
| 5 | `https://www.cenova.com.tr/marka/cenova` | OK | Cenova 品牌 **69 产品**（Dashcam / AHD / WiFi / 4G 相机 + 适配器） |
| 6 | `https://www.cenova.com.tr/marka/dayline` | OK | Dayline 品牌 **67 产品**，**含「PoE Switchler」分类**（SWP-POE31024PL 24 口在列） |
| 7 | `https://www.cenova.com.tr/dl-end3308pfg` | OK | 12 口千兆工业交换机；网页表：8×G RJ45 + 2×G RJ45/2×1000 SFP、**120 W**、24 Gbps、16K MAC、4 M buffer、−40…85 °C、165×145×52 mm、1.3 kg、**Garanti 2 Yıl** |
| 8 | `https://www.cenova.com.tr/img/upl/132998657118177444-dl-end3308pfg.pdf` | OK | **PDF 首页印 `dayline` + `Industrial Switch`**；内嵌标题 **`Microsoft Word - DL-END3308PFG.docx`**；DC12–57 V 双路冗余 5-pin；IP40；6 kV；CCC/CE/FCC/RoHS；**Garanti 3 yıl**（与网页 2 年矛盾） |
| 9 | `https://www.cenova.com.tr/swp-poe31024pl` | OK | 24×10/100 PoE + 2×1G RJ45、250 W、14.8 Gbps、16K MAC、MTBF 100,000 h、智能模式 10M/250 m、−20…55 °C、2 年 |
| 10 | `https://www.cenova.com.tr/dl-3524pgf` | OK | 24×100M PoE + 2×GE + 1×GF SFP、**300 W**、54 Gbps、8K MAC、330×220×44 mm；规格含 **E(300 m)/V(VLAN)/D(PoE Watchdog)** 拨码三段式（中文 ODM 原文） |
| 11 | `https://www.cenova.com.tr/img/upl/133104703868053410-dl-3524pgf.pdf` | OK | 内嵌标题 **`Microsoft Word - 8pfgport.docx`**；Garanti **3 yıl**；IEC61000-4-2/4-5 |
| 12 | `https://www.cenova.com.tr/poe-switchler` | **空模板** | 被当作产品详情路由，无内容 |
| 13 | `https://www.cenova.com.tr/urunler/network-urunler/poe-switchler` | OK ★ | **「16 Ürün bulundu」，实渲染 15 个 SKU**（全自有品牌 DZ-*/DL-*/SWP-） |
| 14 | `https://www.cenova.com.tr/urunler/network-urunler` | OK | Network 大类 **67 产品**（相机/NVR 为主） |
| 15 | `https://karerguvenlik.com/` | OK | AKINSOFT 电商；品牌 DAHUA/HILOOK/HIKVISION/DESİ/SEAGATE/WD/AKINSOFT；自有 KARER；**USD + TL 双标价**、实时库存 |
| 16 | `https://karerguvenlik.com/ag-urunleri` | **404** | 「Ulaşmaya çalıştığınız sayfa bulunamadı」——英文习惯路径不存在 |
| 17 | `https://karerguvenlik.com/ag-urunleri/poe-switchler` | **404** | 同上 |
| 18 | `https://karerguvenlik.com/sitemap.ashx` | OK ★ | 指向 `custom.xml` + **`products_1.xml`**，时间戳全为 2026-11-01 |
| 19 | `https://karerguvenlik.com/products_1.xml` (chunk 0/3) | OK | 全站商品 URL 列表，含 `switchler/poeli-switchler/8-port/prd-kr-nd1p802lfg-…` |
| 20 | `https://karerguvenlik.com/switchler/poeli-switchler/8-port/prd-kr-nd1p802lfg-82-port-gigabit-101001000-poe-swich` | OK ★ | `8*10/100 PoE + 2 Gigabit Uplink、150 W`；**$160.00（8.014,40 TL）+KDV**；库存 **Son 1 ADET**；品牌 KARER |
| 21 | `https://www.okisan.com/` | OK | 标题自带 **「Tiandy - Dahua Türkiye Yetkili Distribütörü」**；4 大方案；最新新闻 **ISAF 2026-İstanbul** |
| 22 | `https://www.okisan.com/dagiticilarimiz/` | OK ★ | Tiandy **5 个区域二级分销**含地址/电话/邮箱（见下） |
| 23 | `https://www.optima.tc/` | **302** | → `https://www.optima-engineering.com/en`（域名已不承载官网） |
| 24 | `https://www.optima-engineering.com/en` | OK | 产品全列：road blocker / bollard / tyre killer / gates / armoured guard house / turnstile / LPR / vehicle recognition / parking / on-street parking / traffic / **SCADA** / fence / security doors；新闻含 **Intersec Dubai 2026** |
| 25 | `https://www.optima-engineering.com/en/contact` | OK ★ | 四据点地址电话（Ankara/İstanbul/Riyadh/Sharjah），邮箱统一 `optima@optima.tc` |

---

## 二、关键存证原文（逐字，便于后续引用不再回抓）

### 2.1 Cenova · PoE 交换机分类页（#13）

`PoE Switchler` / `16 Ürün bulundu`，渲染顺序：

`DZ-PS204D`(4口PoE智能管理) · `DZ-GPS105S`(4口千兆) · `DZ-GS108`(8口千兆管理) · `DZ-PS316G`(16口PoE) · `DL-3424PF`(27口千兆上联PoE光纤) · `DZ-GPS424`(24口PoE) · `DZ-GPS316`(16口千兆PoE) · `DZ-GPOE408`(8口千兆PoE) · `DZ-PS308G`(8口PoE) · `DZ-GPS204`(4口千兆) · `DZ-GPS204R`(4口千兆) · `DZ-PS208G`(8口PoE) · `DL-3508PFG-M`(12口全千兆管理) · `SWP-POE31024PL`(24口PoE) · `DZ-GPS208F`(8口千兆PoE)

→ **15 个渲染 vs 声称 16 个**，差 1，记为待核。

### 2.2 Cenova · `DL-END3308PFG` PDF 头部（#8）

```
12 Port G)gab)t Upl)nk Sw)tch
8*1000M + 2*1000M SFP + 2*1000 RJ45 Endüstr>yel Ethernet Sw>tch
DL-END3308PFG
• 8*1000M RJ45 + 2*1000M SFP + 2*1000M RJ45 port,
dayline
Industrial Switch
```

- PDF 内嵌标题：`Microsoft Word - DL-END3308PFG.docx`
- 端口/保修在网页与 PDF 间**不一致**（网页 2 年、PDF 3 年；Uplink 表述不同）。

### 2.3 Karer · 8 口 PoE 交换机商品页（#20）

```
KR-ND1P802LFG 8+2 PORT GİGABİT 10/100/1000 POE SWİCH
Stok Kodu: KR-ND1P802LFG   Stok Miktarı: Son 1 ADET   Markası: KARER
Web Özel Fiyatı $160,00 (8.014,40 TL) +KDV   KDV: %20
>8*10/100 PoE Ports
>2 Gigabit Uplink Port
>150 W
```

同页「Tavsiye Edilen Ürünler」→ `PSE-0820G`（品牌显示 "Diğer"，库存 6）。
`products_1.xml` 中另见 `prd-kr-nd1pd1621hg-16-port10100-poe-2-portgigabit-uplink-1-portsfp-switch-250w`、`prd-kr-nd1pd2412l-24-port-1port-uplink-2-sfb`。

### 2.4 Okisan · 站点标题与二级分销（#21/#22）

站点标题原文：`Okisan Güvenlik | Tiandy - Dahua Türkiye Yetkili Distribütörü`

| 区域 | 名称 | 地址 | 电话 | 邮箱 |
|---|---|---|---|---|
| İç Anadolu | Uğur Güvenlik | Ata Mah. Kabil Cad. No:100/B Öveçler Çankaya/ANKARA | 0 (312) 481 90 50 | info@ugurguvenlikankara.com |
| İç Anadolu | Ata Global Elektronik | Huzur Mah. 1066.Cad. No:33/A, Çankaya/Ankara | 0 532 523 3246 | hasanemreyurekli@gmail.com |
| Akdeniz | Tria Güvenlik | Kızılsaray Mah. Yener Ulusoy Bulvarı 86 sok. No:4/C Antalya | 0 (242) 244 00 08 | info@triaguvenlik.com |
| Doğu Anadolu | Mst Group Güvenlik | Serhat Mah. 19001. sok. No:8B İpekyolu/Van | 0 (432) 502 00 65 | mst@mstguvenlik.com.tr |
| Güneydoğu Anadolu | 3D Bilgisayar | Selahattin Eyyubi Mh. Urfa Bulvarı No:11/B, 21080 Bağlar/Diyarbakır | 0 (850) 988 03 03 | 3d@3dbilgisayar.com |

> ⚠ 这 5 家是 **Tiandy 的**二级分销，不是 Okisan 的客户。**默认不直接打**（绕过主谈=废掉主谈）。

### 2.5 Optima · 四据点（#25）

| 据点 | 地址 | 电话/传真 |
|---|---|---|
| Ankara 工厂 | Başkent OSB 19.Cadde No:62, Malıköy 06909 Sincan/Ankara | +90 312 815 15 00 / fax +90 312 815 12 98 |
| İstanbul 销售 | Perpa A Blok K:8 No:701, Okmeydanı | +90 212 210 70 00 |
| Saudi Arabia 工厂 | Al Fowzan Rimash Industrial Zone, Istanbul Street, 2851 Al Mishal Dist., 14328-6950 Riyadh | — |
| Optima UAE | 250 m² warehouse T5-074, SAIF Zone, Sharjah | +971 50 563 5922 |

---

## 三、⚠ 名称撞车：`optimasecurityonline.com`

- 检索 `Optima` + `PoE switch` 会命中该站，卖 `OP-SW881 / OP-SW1601I / OP-SW1601E / OP-SW1600G / POE-SW800G / OP-POE-I100GH / BV-SW2402` 等白牌 PoE。
- **它是 Optima Security Systems（Dallas, TX 75229, 2527 Royal Ln Ste 135, +1 972-481-1010）**，与土耳其 Optima Engineering **无关**。
- 该站对抓取返回 **HTTP 500**（首页与分类页均 500），只能读到搜索引擎快照。
- **结论：不得把它的 `OP-SW` 型号当作土耳其 Optima 的证据。**

---

## 四、本轮结论分级（诚实口径）

| 客户 | 可主张的等级 | 不可主张的 |
|---|---|---|
| 04 Cenova | ①自有品牌矩阵 8 个 ②PoE 16 款 ③DL-END3308PFG 规格与保修矛盾 ④无 sitemap/搜索坏 ⑤二级零售价 ₺23,945.29 | 「它在卖 E-wind」（**已被推翻**）、它的 ODM 工厂名 |
| 08 Selim Kalaka | 「公开网络面无记录」这一**阴性结论**本身可主张 | 任何公司名/城市/规模（**均无来源**） |
| 09 Okisan | ①Tiandy+Dahua 授权 ②无自有交换机线 ③ISAF 2026 参展 ④5 家二级分销联系方式 | 「现用丰润达」仍是**用户侧事实**（我方未独立核实） |
| 10 Optima | ①四据点（含利雅得自有厂、Sharjah 仓库）②两处电话 ③产品范围含 SCADA/LPR/交通 ④域名迁移 | 年用量、三地是否同一 BOM、`OP-SW` 型号（属美国另一家） |
| 11 Karer | ①公开 USD 价 $160（8.014,40 TL）②KR-ND* 型号族 ③板级商品线 ④商品 URL 可枚举 | `KR-S1710GU-AP` 仍在售（**本轮未见于站点**）、其 OEM 工厂名 |

**未核验 16 家**：01/02/03/05/06/07/12/13/14/15/16/17/18/19/20/21 —— 本轮 0 次抓取，档案等级不变，**不得标为「已验证」**。

---

## 五、下轮别再试（本轮确认的死路）

1. `cenova.com.tr/sitemap.xml` → 404
2. `cenova.com.tr/arama?q=…` → 路由坏，无结果
3. `cenova.com.tr/poe-switchler`、`/urunler/network-urunler` 的英文平级路径 → 会被当产品页；**正确入口 `urunler/<大类>/<子类>`**
4. `optimasecurityonline.com` → HTTP 500
5. `optima.tc` → 302，别再当官网站点
6. `karerguvenlik.com/ag-urunleri*` → 404，用 `sitemap.ashx` 反查
7. `"Selim Kalaka" güvenlik` 检索 → 0 相关，**结案，不必换搜索引擎重试**
