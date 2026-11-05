# TR Customers · 土耳其客户总表（一客户一 MD）

**这个文件夹是什么**：把仓库里**已有的土耳其客户底稿**，拆成**一家一个 Markdown 文件**，方便逐家看、逐家发、逐家跟。

- 客户数：**146** —— **A 档 33 · B 档 77 · C 档 36**
- 组织方式：**A / B / C 三个子文件夹**（`A/` `B/` `C/`，按 `111` 的 `层级` 列首字母归档），本 README 放在根部
- 文件数：**146** 个客户 MD + 本 README
- 数据源（唯一权威）：`ingest/angora-1__arena-01a0ce39__5acb613/01-text-verbatim/workstation/08-customer-pipeline/111-turkey-customer-pipeline.csv`（**145 行 × 17 列**）
- 额外 1 家：**Entegron / LONGLINE**（`A/146-entegron-longline.md`）—— 它只在 `06-competitors/110` 第 20 行与原始名单 #44，**不在 111 管线里**，按客户侧评级归入 `A/`。

---

## 一、怎么读（四件事）

1. **每个文件固定七段**：身份卡 → 我方核实的交换机产品线 → 当前供应链 → 联系人（逐字）→ 证据与核实等级 → 建议动作 → 备注。
2. **21 家有「附：完整研究档案」**（文件里带 📚 标记）：把 `08-followup-dossiers-2026-11-01/` 里的**八段档案 + r42 核验补录 + r43 商业深挖全文逐字并入**，所以这 21 个文件是**自包含**的，不用来回跳。
3. **按档分目录**：`A/` 优先跟进、`B/` 常规维护、`C/` 备选池（标准见第三节）。**想只打重点，就只看 `A/` 这一个文件夹。**
4. **没有合并任何记录**：111 里同一家公司在两批名单里各出现一次（如 `Makros A.Ş.` = #26 与 #81、`Telemobil` = #46 与 #80、`HAFYA` = #25 与 #82），**各自独立成文件**，文件顶部用 ⚠ 标出「疑与 #NNN 同一家」，**要不要合并由人判断**（共 21 组，见第八节）。

## 二、诚实边界（必读）

| 事项 | 实情 |
|---|---|
| 覆盖范围 | **111 的 145 行全覆盖**。你给的两批原始名单（`Turkey Client List.xlsx` 299 行 + `2025土耳其ISAF客户.xlsx` 98 家）**已经折进这 145 行**（见 `112-user-customer-lists-deepdive-2026-10-25.md`），所以这里不是「299+98=397 家」，而是**去重后的 145 家管线**。 |
| 深度差异 | **21 家有深度档案**（八段 + 核验 + 深挖）；其余 124 家只有管线表的字段（公司/城市/品牌/供应链/联系人/证据/建议动作）。**不要把 124 家当成「已调研」，它们只是「有档案」。** |
| 联系人来源 | 「联系人」**全部来自用户侧**（展会/微信/名单），`证据来源` 列才是我方独立抓取的内容。**对外沟通前先分清这两类。** |
| 报价 | 表里所有报价都是**历史口径**，含 DDP/关税的一律要重算。 |
| 第三方数据 | 规模/营收等若来自 Datanyze / ZoomInfo / RocketReach / Volza，均为**第三方推算**，非财报（详见各家深度档案）。 |

## 三、分档标准（A / B / C 是怎么来的）

**不是我这轮重新打的印象分**——直接沿用 `111` 管线表 `层级` 列的**首字母**，该列本身是「双 AI 初筛 + 我方人工核实 + 综合评分」的产物（详见 `112-user-customer-lists-deepdive-2026-10-25.md`）。

| 档 | 子标签举例 | 家数 | 含义 |
|---|---|---|---|
| **A** | `A 核心` / `A-` / `A 订单级` / `A 军项目` / `A 战略` / `A 暖线` / `A 大型分销` | 33 | 已有接触 + 有明确需求或产品空档；**本周就该动手**。 |
| **B** | `B+` / `B` / `B-` / `B 暖线` / `B bypass` / `B 防务客户池` | 77 | 有真实业务，但缺一环（价格、DDP、规模、决策链）；**季度节奏维护**。 |
| **C** | `C` / `C+` / `C 战略留档` / `C 不跟进` / `C 低` | 36 | 只到邮箱/电话，或明确不跟进；**只做群发触达与备选**。 |

> ⚠ 两处需要人判断的地方：① `C 战略留档`（如 PavoTek）与 `C 不跟进`（如 MFD/Bimel 类）**同放在 `C/`**，但性质完全不同，看文件里的「备注」；② 同一家公司在两批名单里可能被分到**不同档**（如 #26 是 B+、#81 是 A），本文件夹**不做合并**，两份各归各档，请自行裁决以哪份为准。

## 四、索引 · A 档 · 优先跟进（33 家）

> 核心客户 / 有明确产品空档或订单信号。**先打这一层。**

| # | 客户 | 城市 | 层级 | 评分 | 深度档案 | 文件 |
|---|---|---|---|---|---|---|
| 1 | Telkolink + GelecekBT（同集团） | İstanbul/Şişli（分部 = Perpa… | A 核心 | 88 | 有 | [A/001-telkolink-gelecekbt.md](A/001-telkolink-gelecekbt.md) |
| 2 | NOVA Group（Novacom） | Ankara | A 核心 | 86 | 有 | [A/002-nova-group-novacom.md](A/002-nova-group-novacom.md) |
| 3 | Snexus Networks | İstanbul | A 核心 | 85 | 有 | [A/003-snexus-networks.md](A/003-snexus-networks.md) |
| 4 | Cenova Bilişim Teknolojileri | İstanbul | A 核心 | 82 | 有 | [A/004-cenova-bilisim-teknolojileri.md](A/004-cenova-bilisim-teknolojileri.md) |
| 5 | CryptoLink Elektronik Güvenlik Sistemleri | Ankara/Çankaya | A 核心（公共 niche） | 80 | 有 | [A/005-cryptolink-elektronik-guvenlik-sistemleri.md](A/005-cryptolink-elektronik-guvenlik-sistemleri.md) |
| 52 | upTech / Nokta Elektronik ve Bilişim Siste… | Istanbul Şişli Perpa | A 自有品牌switch主（r36 新入） | 78 | — | [A/052-uptech-nokta-elektronik-ve-bilisim-sistemleri-a.md](A/052-uptech-nokta-elektronik-ve-bilisim-sistemleri-a.md) |
| 53 | WINET（wi.com.tr） | TR（站点未披露城市） | A- 品牌+分销（r36 新入） | 64 | — | [A/053-winet-wi-com-tr.md](A/053-winet-wi-com-tr.md) |
| 54 | TekniksatGroup（TGD） | Istanbul（1992 创立） | A 自有品牌switch主（r36 新入） | 72 | — | [A/054-tekniksatgroup-tgd.md](A/054-tekniksatgroup-tgd.md) |
| 56 | Optima / Optima Mühendislik Ltd. Şti. | Ankara Sincan（Başkent OSB… | A- 暖线（r37 新入） | 68 | 有 | [A/056-optima-optima-muhendislik-ltd-sti.md](A/056-optima-optima-muhendislik-ltd-sti.md) |
| 58 | Okisan Güvenlik Teknolojileri A.Ş. | İstanbul Şişli Okmeydanı（O… | A- 大型分销（r37 新入） | 70 | 有 | [A/058-okisan-guvenlik-teknolojileri-a-s.md](A/058-okisan-guvenlik-teknolojileri-a-s.md) |
| 72 | LeMax Güvenlik | （İstanbul） | A- 自有品牌（r37 新入） | 55 | — | [A/072-lemax-guvenlik.md](A/072-lemax-guvenlik.md) |
| 75 | TechnoPC | İstanbul Ataşehir | A-（r37 新入） | 55 | — | [A/075-technopc.md](A/075-technopc.md) |
| 80 | Telemobil（tbi.com.tr） | İstanbul | A 具体项目（ISAF25 新入） | 72 | 有 | [A/080-telemobil-tbi-com-tr.md](A/080-telemobil-tbi-com-tr.md) |
| 81 | Makros A.Ş. | İstanbul | A 工程（ISAF25 新入） | 70 | 有 | [A/081-makros-a-s.md](A/081-makros-a-s.md) |
| 82 | HAFYA | İstanbul | A 军项目（ISAF25 新入） | 70 | 有 | [A/082-hafya.md](A/082-hafya.md) |
| 83 | SFP Turkey（sfpturkey.com.tr） | İstanbul | A 既有客户（ISAF25 新入） | 68 | — | [A/083-sfp-turkey-sfpturkey-com-tr.md](A/083-sfp-turkey-sfpturkey-com-tr.md) |
| 84 | ONSIS ELEKTRONIK | （0232 区） | A 要样品（ISAF25 新入） | 68 | 有 | [A/084-onsis-elektronik.md](A/084-onsis-elektronik.md) |
| 85 | Netmax（Ugur Simsek） | İstanbul | A-（ISAF25 新入） | 66 | — | [A/085-netmax-ugur-simsek.md](A/085-netmax-ugur-simsek.md) |
| 86 | bilimsateknoloji（Muharrem KILIC） | （İstanbul） | A-（ISAF25 新入） | 66 | 有 | [A/086-bilimsateknoloji-muharrem-kilic.md](A/086-bilimsateknoloji-muharrem-kilic.md) |
| 87 | UGUR IMRE | （İstanbul） | A- 分销（ISAF25 新入） | 66 | — | [A/087-ugur-imre.md](A/087-ugur-imre.md) |
| 88 | ORAL GUVENLIK（oralcompanies.com） | （0392 区） | A- 价敏（ISAF25 新入） | 62 | — | [A/088-oral-guvenlik-oralcompanies-com.md](A/088-oral-guvenlik-oralcompanies-com.md) |
| 89 | DE secure（desecuretechnology.com） | İstanbul | A-（ISAF25 新入） | 62 | — | [A/089-de-secure-desecuretechnology-com.md](A/089-de-secure-desecuretechnology-com.md) |
| 90 | cansisteknoloji（Ahmet CAN） | （0332 区） | A-（ISAF25 新入） | 62 | — | [A/090-cansisteknoloji-ahmet-can.md](A/090-cansisteknoloji-ahmet-can.md) |
| 91 | Sami CEUIK | （微信） | A 订单级（ISAF25 新入） | 70 | 有 | [A/091-sami-ceuik.md](A/091-sami-ceuik.md) |
| 92 | Selim Kalaka（供应商侧线） | （微信，外国人中文很好） | A 战略（ISAF25 新入） | 68 | 有 | [A/092-selim-kalaka.md](A/092-selim-kalaka.md) |
| 93 | HCS（hescs.com） | （0352 Bilecik 区） | A-（ISAF25 新入） | 62 | — | [A/093-hcs-hescs-com.md](A/093-hcs-hescs-com.md) |
| 94 | KLASNET | （0501 区） | A- 分销意向（ISAF25 新入） | 62 | — | [A/094-klasnet.md](A/094-klasnet.md) |
| 95 | F.A.S.T（fasttr.com） | （0216 区） | A-（ISAF25 新入） | 60 | — | [A/095-f-a-s-t-fasttr-com.md](A/095-f-a-s-t-fasttr-com.md) |
| 96 | voltechelektronik | （0216 区） | A-（ISAF25 新入） | 58 | — | [A/096-voltechelektronik.md](A/096-voltechelektronik.md) |
| 97 | LABOR Mühendislik（Ramazan DAS） | （Ankara 0412 区） | A-（ISAF25 新入） | 58 | — | [A/097-labor-muhendislik-ramazan-das.md](A/097-labor-muhendislik-ramazan-das.md) |
| 98 | MEPA Elektronik | （İstanbul） | A-（ISAF25 新入） | 58 | — | [A/098-mepa-elektronik.md](A/098-mepa-elektronik.md) |
| 99 | viva bilgisayar（ismet Yavuz 老板） | Hatay | A-（ISAF25 新入） | 55 | — | [A/099-viva-bilgisayar-ismet-yavuz.md](A/099-viva-bilgisayar-ismet-yavuz.md) |
| 146 | Entegron ／ LONGLINE（双品牌） | İstanbul / Bayrampaşa | A-（客户侧） | 30A/45A | 有 | [A/146-entegron-longline.md](A/146-entegron-longline.md) |

## 五、索引 · B 档 · 常规跟进（77 家）

> 有真实业务但无强信号，或有单一短板（价格/DDP/规模小）。**按季度节奏维护，不投定制资源。**

| # | 客户 | 城市 | 层级 | 评分 | 深度档案 | 文件 |
|---|---|---|---|---|---|---|
| 6 | Coptek | İstanbul/Balmumcu | B+ | 78 | — | [B/006-coptek.md](B/006-coptek.md) |
| 7 | Karer Güvenlik | İstanbul/Pendik | B+ | 76 | 有 | [B/007-karer-guvenlik.md](B/007-karer-guvenlik.md) |
| 8 | Hane Elektronik | İstanbul/Küçükçekmece | B+ | 74 | 有 | [B/008-hane-elektronik.md](B/008-hane-elektronik.md) |
| 9 | Öncü Güvenlik Sistemleri A.Ş. | İstanbul/Beykoz | B | 72 | 有 | [B/009-oncu-guvenlik-sistemleri-a-s.md](B/009-oncu-guvenlik-sistemleri-a-s.md) |
| 10 | ErETE | —（B2B 平台） | B | 71 | — | [B/010-erete.md](B/010-erete.md) |
| 11 | Eretekne（+ Isee，同 Asya Telekom 集团） | —（B2B 平台） | B | 70 | — | [B/011-eretekne-isee-asya-telekom.md](B/011-eretekne-isee-asya-telekom.md) |
| 12 | CCS Güvenlik | —（B2B 电商） | B | 69 | — | [B/012-ccs-guvenlik.md](B/012-ccs-guvenlik.md) |
| 13 | Rima Elektronik | Ankara | B | 68 | — | [B/013-rima-elektronik.md](B/013-rima-elektronik.md) |
| 14 | NFS Teknoloji | İstanbul | B | 67 | — | [B/014-nfs-teknoloji.md](B/014-nfs-teknoloji.md) |
| 15 | Koza Güvenlik Elektronik Sistemleri（GreenT… | İstanbul/Okmeydanı（Koza Pl… | B | 66 | — | [B/015-koza-guvenlik-elektronik-sistemleri-greentech.md](B/015-koza-guvenlik-elektronik-sistemleri-greentech.md) |
| 16 | Portel（industrialnetworkcenter.com） | İstanbul/Kartal | B | 65 | — | [B/016-portel-industrialnetworkcenter-com.md](B/016-portel-industrialnetworkcenter-com.md) |
| 17 | RF Teknoloji | — | B | 64 | — | [B/017-rf-teknoloji.md](B/017-rf-teknoloji.md) |
| 18 | iotsistem | İstanbul | B | 63 | — | [B/018-iotsistem.md](B/018-iotsistem.md) |
| 19 | Lansan | Ankara | B | 62 | — | [B/019-lansan.md](B/019-lansan.md) |
| 20 | Opax Mühendislik（opax.com） | Nevşehir Merkez（Opax Plaza… | B | 61 | 有 | [B/020-opax-muhendislik-opax-com.md](B/020-opax-muhendislik-opax-com.md) |
| 21 | CCTV Depo Güvenlik Teknolojileri AŞ | İstanbul/Şişli-Perpa | B | 60 | 有 | [B/021-cctv-depo-guvenlik-teknolojileri-as.md](B/021-cctv-depo-guvenlik-teknolojileri-as.md) |
| 22 | TeleOne | — | B- | 58 | — | [B/022-teleone.md](B/022-teleone.md) |
| 23 | Konak Güvenlik | İstanbul | B- | 55 | — | [B/023-konak-guvenlik.md](B/023-konak-guvenlik.md) |
| 24 | SFPTURKEY Elektronik İth. İhr. Ticaret Ltd… | İstanbul | B+ | 77 | — | [B/024-sfpturkey-elektronik-ith-ihr-ticaret-ltd-sti.md](B/024-sfpturkey-elektronik-ith-ihr-ticaret-ltd-sti.md) |
| 25 | HAFYA Technologies | İstanbul | B+ | 75 | — | [B/025-hafya-technologies.md](B/025-hafya-technologies.md) |
| 26 | Makros AŞ（Makro Sistem） | İstanbul | B+ | 73 | — | [B/026-makros-as-makro-sistem.md](B/026-makros-as-makro-sistem.md) |
| 27 | ONSİS Elektrik Elektronik Güvenlik Sisteml… | Ankara/Çankaya | B | 68 | — | [B/027-onsis-elektrik-elektronik-guvenlik-sistemleri-in.md](B/027-onsis-elektrik-elektronik-guvenlik-sistemleri-in.md) |
| 28 | Hiperonline | Eskişehir（总部，81 省覆盖） | B | 66 | — | [B/028-hiperonline.md](B/028-hiperonline.md) |
| 29 | DE Secure（Desecure Technology） | İstanbul | B- | 62 | — | [B/029-de-secure-desecure-technology.md](B/029-de-secure-desecure-technology.md) |
| 30 | ORAL GÜVENLİK Sistemleri（Oral Companies 集团… | Lefkoşa/北塞浦路斯（K.K.T.C.） | B- | 62 | — | [B/030-oral-guvenlik-sistemleri-oral-companies.md](B/030-oral-guvenlik-sistemleri-oral-companies.md) |
| 31 | F.A.S.T（Fabrika Aygıtları Sistem Teknoloji… | İstanbul/Ataşehir | B- | 60 | — | [B/031-f-a-s-t-fabrika-aygitlari-sistem-teknolojisi-a-s.md](B/031-f-a-s-t-fabrika-aygitlari-sistem-teknolojisi-a-s.md) |
| 32 | Fiberix | Gaziantep | B- | 60 | — | [B/032-fiberix.md](B/032-fiberix.md) |
| 33 | HCS（hescs.com） | Türkiye（布线全国体系） | B- | 58 | — | [B/033-hcs-hescs-com.md](B/033-hcs-hescs-com.md) |
| 34 | STASANET d.o.o. | Belgrade + Novi Sad（塞尔维亚） | B- | 57 | — | [B/034-stasanet-d-o-o.md](B/034-stasanet-d-o-o.md) |
| 35 | Antalya Turkuaz Bilişim Teknolojileri | Antalya/Muratpaşa | B- | 56 | — | [B/035-antalya-turkuaz-bilisim-teknolojileri.md](B/035-antalya-turkuaz-bilisim-teknolojileri.md) |
| 36 | Go Technology | Gaza（巴勒斯坦） | B- | 55 | — | [B/036-go-technology.md](B/036-go-technology.md) |
| 37 | Shnrise Güvenlik Sistemleri | İstanbul | B- | 55 | — | [B/037-shnrise-guvenlik-sistemleri.md](B/037-shnrise-guvenlik-sistemleri.md) |
| 38 | FOURLİNE | Bursa | B- | 54 | — | [B/038-fourline.md](B/038-fourline.md) |
| 39 | MEPA Elektronik | Kayseri | B- | 53 | — | [B/039-mepa-elektronik.md](B/039-mepa-elektronik.md) |
| 40 | AG Bilgisayar | Bodrum/Muğla | B- | 53 | — | [B/040-ag-bilgisayar.md](B/040-ag-bilgisayar.md) |
| 41 | FH Güvenlik Sistemleri ve Bilişim San. Tic… | İstanbul（Perpa-3 区位） | B- | 52 | — | [B/041-fh-guvenlik-sistemleri-ve-bilisim-san-tic-ltd-st.md](B/041-fh-guvenlik-sistemleri-ve-bilisim-san-tic-ltd-st.md) |
| 42 | BİLGEN ELEKTRONİK（GÜVENLİK SİSTEMLERİ... L… | Gebze/Kocaeli（工业区） | B- | 52 | — | [B/042-bilgen-elektronik-guvenlik-sistemleri-ltd-sti.md](B/042-bilgen-elektronik-guvenlik-sistemleri-ltd-sti.md) |
| 43 | Duzgun Toptan Ticaret（teksarf.com） | İstanbul/Bahçelievler（Topt… | B- | 51 | — | [B/043-duzgun-toptan-ticaret-teksarf-com.md](B/043-duzgun-toptan-ticaret-teksarf-com.md) |
| 44 | PROVES（Proves Bilgi Teknolojileri San. Tic… | İzmir/Bayraklı（Verapol Pla… | B- | 50 | — | [B/044-proves-proves-bilgi-teknolojileri-san-tic-a-s.md](B/044-proves-proves-bilgi-teknolojileri-san-tic-a-s.md) |
| 45 | Alamthal（الامثل للاتصالات و تقنية المعلوما… | Tripoli（Libya） | B- | 49 | — | [B/045-alamthal.md](B/045-alamthal.md) |
| 46 | TBI - Telemobil（tbi.com.tr） | İstanbul/Üsküdar | B | 70 | — | [B/046-tbi-telemobil-tbi-com-tr.md](B/046-tbi-telemobil-tbi-com-tr.md) |
| 47 | PELIKAN BILG. İTH. İHR.（Pelikan Bilgisayar… | İstanbul/Şişli（Perpa Ticar… | B | 64 | — | [B/047-pelikan-bilg-ith-ihr-pelikan-bilgisayar.md](B/047-pelikan-bilg-ith-ihr-pelikan-bilgisayar.md) |
| 48 | Bilge Güvenlik ve Teknoloji A.Ş. | İstanbul（+ Ankara/İzmir 分支… | B | 62 | — | [B/048-bilge-guvenlik-ve-teknoloji-a-s.md](B/048-bilge-guvenlik-ve-teknoloji-a-s.md) |
| 49 | Zeytek Bilişim ve Teknoloji Ürünleri Ltd.… | İstanbul/Sancaktepe | B- | 58 | — | [B/049-zeytek-bilisim-ve-teknoloji-urunleri-ltd-sti.md](B/049-zeytek-bilisim-ve-teknoloji-urunleri-ltd-sti.md) |
| 50 | FOLİNE BİLİŞİM TEKNOLOJİLERİ SAN. TİC. LTD… | İstanbul/Kağıthane | B- | 58 | — | [B/050-foline-bilisim-teknolojileri-san-tic-ltd-sti.md](B/050-foline-bilisim-teknolojileri-san-tic-ltd-sti.md) |
| 51 | NAZEM CO İTH. İHR. SAN. TİC. LTD. ŞTİ.（NAZ… | Türkiye | B- | 50 | — | [B/051-nazem-co-ith-ihr-san-tic-ltd-sti-nazemco.md](B/051-nazem-co-ith-ihr-san-tic-ltd-sti-nazemco.md) |
| 55 | ULAK Haberleşme | Ankara | B 防务客户池（r36 新入） | 45 | — | [B/055-ulak-haberlesme.md](B/055-ulak-haberlesme.md) |
| 57 | Filiz Güvenlik Sistemleri Proje İnş. San.… | İzmir Konak（Mersinli 2817… | B 暖线（r37 新入） | 58 | 有 | [B/057-filiz-guvenlik-sistemleri-proje-ins-san-tic-ltd.md](B/057-filiz-guvenlik-sistemleri-proje-ins-san-tic-ltd.md) |
| 60 | GMT Control（GMTCNT） | （İstanbul） | B（r37 新入） | 40 | — | [B/060-gmt-control-gmtcnt.md](B/060-gmt-control-gmtcnt.md) |
| 62 | Cebeci Grup | （İstanbul） | B（r37 新入） | 45 | — | [B/062-cebeci-grup.md](B/062-cebeci-grup.md) |
| 63 | Areskom | İstanbul Üsküdar | B-（r37 新入） | 35 | — | [B/063-areskom.md](B/063-areskom.md) |
| 64 | İntenet | （İstanbul） | B-（r37 新入） | 35 | — | [B/064-intenet.md](B/064-intenet.md) |
| 65 | Teamon | Ankara | B-（r37 新入） | 30 | — | [B/065-teamon.md](B/065-teamon.md) |
| 66 | İnovatech | İstanbul | B-（r37 新入） | 25 | — | [B/066-inovatech.md](B/066-inovatech.md) |
| 67 | Metcom | Ankara+İstanbul Ümraniye | B-（r37 新入） | 35 | — | [B/067-metcom.md](B/067-metcom.md) |
| 68 | Egemenelektronik | （İstanbul） | B-（r37 新入） | 30 | — | [B/068-egemenelektronik.md](B/068-egemenelektronik.md) |
| 69 | TeknolojiPazar | İzmir Konak | B（r37 新入） | 45 | — | [B/069-teknolojipazar.md](B/069-teknolojipazar.md) |
| 70 | TekmarShop（TEKMAR） | İstanbul Ümraniye | B-（r37 新入） | 25 | — | [B/070-tekmarshop-tekmar.md](B/070-tekmarshop-tekmar.md) |
| 71 | BaburTech | Ankara | B-（r37 新入） | 25 | — | [B/071-baburtech.md](B/071-baburtech.md) |
| 73 | Kiracı Bilişim=ZKR（Kıraç 集团） | （İstanbul） | B（r37 新入） | 35 | — | [B/073-kiraci-bilisim-zkr-kirac.md](B/073-kiraci-bilisim-zkr-kirac.md) |
| 79 | EuroCam Güvenlik | （İstanbul） | B- 待评估（r37 新入） | 30 | — | [B/079-eurocam-guvenlik.md](B/079-eurocam-guvenlik.md) |
| 100 | PROVES（proves.com.tr） | （0232 区） | B（ISAF25 新入） | 50 | — | [B/100-proves-proves-com-tr.md](B/100-proves-proves-com-tr.md) |
| 101 | NECDET SENKACAYC | （İstanbul） | B（ISAF25 新入） | 48 | — | [B/101-necdet-senkacayc.md](B/101-necdet-senkacayc.md) |
| 102 | fiberix（fiberix.com.tr） | İstanbul | B-（ISAF25 新入） | 45 | — | [B/102-fiberix-fiberix-com-tr.md](B/102-fiberix-fiberix-com-tr.md) |
| 103 | acusenseteknoloji（Umit Celik） | （0216 区） | B-（ISAF25 新入） | 45 | — | [B/103-acusenseteknoloji-umit-celik.md](B/103-acusenseteknoloji-umit-celik.md) |
| 104 | Duzgun Toptan Ticaret（teksarf.com） | （İstanbul） | B-（ISAF25 新入） | 42 | — | [B/104-duzgun-toptan-ticaret-teksarf-com.md](B/104-duzgun-toptan-ticaret-teksarf-com.md) |
| 105 | IHM Technology | （0216 区） | B bypass（ISAF25 新入） | 50 | — | [B/105-ihm-technology.md](B/105-ihm-technology.md) |
| 106 | sinerjik（Ufuk GOKALP） | İstanbul | B-（ISAF25 新入） | 40 | — | [B/106-sinerjik-ufuk-gokalp.md](B/106-sinerjik-ufuk-gokalp.md) |
| 107 | Ecevit（marbim.com.tr） | （0242 区） | B（ISAF25 新入） | 42 | — | [B/107-ecevit-marbim-com-tr.md](B/107-ecevit-marbim-com-tr.md) |
| 114 | ag-bilgisayar（Aycan CAM） | （0252 区） | B+ bypass（ISAF25 新入） | 52 | — | [B/114-ag-bilgisayar-aycan-cam.md](B/114-ag-bilgisayar-aycan-cam.md) |
| 116 | fhguvenlik（Hasti F. GOLLER） | （0535 区） | B-（ISAF25 新入） | 35 | — | [B/116-fhguvenlik-hasti-f-goller.md](B/116-fhguvenlik-hasti-f-goller.md) |
| 117 | BİLGEN ELEKTRONİK | （İstanbul） | B bypass（ISAF25 新入） | 45 | — | [B/117-bilgen-elektronik.md](B/117-bilgen-elektronik.md) |
| 123 | Sedat（微信） | （İstanbul） | B-（ISAF25 新入） | 45 | — | [B/123-sedat.md](B/123-sedat.md) |
| 124 | Interland Network & Security | （İstanbul） | B-（ISAF25 新入） | 42 | — | [B/124-interland-network-security.md](B/124-interland-network-security.md) |
| 126 | NAZEMCO（Osama） | （İstanbul） | B-（ISAF25 新入） | 40 | — | [B/126-nazemco-osama.md](B/126-nazemco-osama.md) |
| 128 | Fatih A（微信） | （İstanbul） | B+（ISAF25 新入） | 48 | — | [B/128-fatih-a.md](B/128-fatih-a.md) |
| 130 | 90543 780 22 23（合影客） | （Ankara） | B-（ISAF25 新入） | 35 | — | [B/130-90543-780-22-23.md](B/130-90543-780-22-23.md) |

## 六、索引 · C 档 · 备选池（36 家）

> 信息少 / 只到邮箱电话 / 战略留档 / 明确不跟进。**只做群发触达与备选，不单独投入人力。**

| # | 客户 | 城市 | 层级 | 评分 | 深度档案 | 文件 |
|---|---|---|---|---|---|---|
| 59 | PavoTek（pavotek.com.tr） | （Pavo Group 见 110 行 1） | C 战略留档（r37 新入） | 10 | — | [C/059-pavotek-pavotek-com-tr.md](C/059-pavotek-pavotek-com-tr.md) |
| 61 | MFD（mfd.com.tr） | İstanbul | C 不跟进（r37 新入） | 5 | — | [C/061-mfd-mfd-com-tr.md](C/061-mfd-mfd-com-tr.md) |
| 74 | RadioTeknoloji | （İstanbul） | C（r37 新入） | 15 | — | [C/074-radioteknoloji.md](C/074-radioteknoloji.md) |
| 76 | Bimel | Ankara（总部+4 分支） | C 低（r37 新入） | 20 | — | [C/076-bimel.md](C/076-bimel.md) |
| 77 | Dacel Solutions | İstanbul Esenler | C（r37 新入） | 15 | — | [C/077-dacel-solutions.md](C/077-dacel-solutions.md) |
| 78 | Fiberden | İstanbul | C（r37 新入） | 15 | — | [C/078-fiberden.md](C/078-fiberden.md) |
| 108 | DIMAS TEKNOLOJI VE GUVENLIK | （0530 区） | C（ISAF25 新入） | 30 | — | [C/108-dimas-teknoloji-ve-guvenlik.md](C/108-dimas-teknoloji-ve-guvenlik.md) |
| 109 | basaranelektronik（Emrah Basaran 老板） | （0266 区） | C（ISAF25 新入） | 30 | — | [C/109-basaranelektronik-emrah-basaran.md](C/109-basaranelektronik-emrah-basaran.md) |
| 110 | Fadi | （İstanbul） | C（ISAF25 新入） | 28 | — | [C/110-fadi.md](C/110-fadi.md) |
| 111 | Ali Goktork | （Ankara） | C（ISAF25 新入） | 28 | — | [C/111-ali-goktork.md](C/111-ali-goktork.md) |
| 112 | D&N ELEKTRIK MUHENDISLIK | （0541 区） | C（ISAF25 新入） | 25 | — | [C/112-d-n-elektrik-muhendislik.md](C/112-d-n-elektrik-muhendislik.md) |
| 113 | fourline.com.tr | （0224 区） | C（ISAF25 新入） | 25 | — | [C/113-fourline-com-tr.md](C/113-fourline-com-tr.md) |
| 115 | 3s.com.tr（SAVAS TULGAR） | （0533 区） | C+（ISAF25 新入） | 30 | — | [C/115-3s-com-tr-savas-tulgar.md](C/115-3s-com-tr-savas-tulgar.md) |
| 118 | ANIL（aniltelekom.com） | İstanbul | C（ISAF25 新入） | 25 | — | [C/118-anil-aniltelekom-com.md](C/118-anil-aniltelekom-com.md) |
| 119 | BTM ELECTRONIC | （0532 区） | C（ISAF25 新入） | 25 | — | [C/119-btm-electronic.md](C/119-btm-electronic.md) |
| 120 | ebatek（BALKIS S.Coskun CEO） | İstanbul | C（ISAF25 新入） | 25 | — | [C/120-ebatek-balkis-s-coskun-ceo.md](C/120-ebatek-balkis-s-coskun-ceo.md) |
| 121 | turkuaz（antalyaturkuaz.com） | Antalya | C（ISAF25 新入） | 25 | — | [C/121-turkuaz-antalyaturkuaz-com.md](C/121-turkuaz-antalyaturkuaz-com.md) |
| 122 | GÜNGÖR ELEKTRONİK | （İstanbul） | C（ISAF25 新入） | 22 | — | [C/122-gungor-elektronik.md](C/122-gungor-elektronik.md) |
| 125 | Smali（微信） | （İstanbul） | C（ISAF25 新入） | 22 | — | [C/125-smali.md](C/125-smali.md) |
| 127 | Serkan（Alisa 客户） | （İstanbul） | C（ISAF25 新入） | 25 | — | [C/127-serkan-alisa.md](C/127-serkan-alisa.md) |
| 129 | Celali Ayazoglu | （İstanbul） | C（ISAF25 新入） | 22 | — | [C/129-celali-ayazoglu.md](C/129-celali-ayazoglu.md) |
| 131 | wechat:TeT529 | （İstanbul） | C（ISAF25 新入） | 20 | — | [C/131-wechat-tet529.md](C/131-wechat-tet529.md) |
| 132 | Ertan Kral | （İstanbul） | C（ISAF25 新入） | 25 | — | [C/132-ertan-kral.md](C/132-ertan-kral.md) |
| 133 | Enes Talha Karaaslan（微信） | （İstanbul） | C（ISAF25 新入） | 28 | — | [C/133-enes-talha-karaaslan.md](C/133-enes-talha-karaaslan.md) |
| 134 | Gokhan（微信） | （İstanbul） | C（ISAF25 新入） | 25 | — | [C/134-gokhan.md](C/134-gokhan.md) |
| 135 | NORTEL İletişim（norteliletisim.com） | （0242 区） | C（ISAF25 新入） | 25 | — | [C/135-nortel-iletisim-norteliletisim-com.md](C/135-nortel-iletisim-norteliletisim-com.md) |
| 136 | Zeytek（zeytek.com.tr） | İstanbul | C（ISAF25 新入） | 25 | — | [C/136-zeytek-zeytek-com-tr.md](C/136-zeytek-zeytek-com-tr.md) |
| 137 | Bilge SECURITY SYSTEMS | （İstanbul） | C+（ISAF25 新入） | 30 | — | [C/137-bilge-security-systems.md](C/137-bilge-security-systems.md) |
| 138 | pelikanbilgisayar（Ahmet Karci） | （0541 区） | C（ISAF25 新入） | 22 | — | [C/138-pelikanbilgisayar-ahmet-karci.md](C/138-pelikanbilgisayar-ahmet-karci.md) |
| 139 | Interpos（inter-pos.com） | İstanbul | C（ISAF25 新入） | 22 | — | [C/139-interpos-inter-pos-com.md](C/139-interpos-inter-pos-com.md) |
| 140 | camsanordu（0553 区） | （Tekirdağ 区） | C（ISAF25 新入） | 22 | — | [C/140-camsanordu-0553.md](C/140-camsanordu-0553.md) |
| 141 | teknoktadestek.com | İstanbul | C（ISAF25 新入） | 22 | — | [C/141-teknoktadestek-com.md](C/141-teknoktadestek-com.md) |
| 142 | FOLINE（foline.com.tr） | İstanbul | C（ISAF25 新入） | 25 | — | [C/142-foline-foline-com-tr.md](C/142-foline-foline-com-tr.md) |
| 143 | Holil | （İstanbul） | C+（ISAF25 新入） | 28 | — | [C/143-holil.md](C/143-holil.md) |
| 144 | Marmaris Bilişim | Marmaris | C（ISAF25 新入） | 22 | — | [C/144-marmaris-bilisim.md](C/144-marmaris-bilisim.md) |
| 145 | hiperonline.com | Eskişehir | C（ISAF25 新入） | 25 | — | [C/145-hiperonline-com.md](C/145-hiperonline-com.md) |

## 七、从哪儿开始（建议顺序）

1. **A 级 + 有深度档案的 6 家**：#4 Cenova、#9 Öncü、#7 Karer、#56 Optima、#80 Telemobil、#58 Okisan —— 有产品空档、有联系人、有打法。
2. **订单级/窗口级 3 家**：#91 Sami（500 台）、#92 Selim（换源窗口）、#84 ONSIS（回头要样品）—— **只能靠人推进，爬虫无效**。
3. **B/C 级 124 家**：先扫 `建议动作` 列，只挑「有具体项目/有自有品牌」的动，其余作为备选池。

## 八、重复对（21 组，两批名单各录一次）

> 这里**只做提示，不做合并**。给客户发信前请先确认是同一条线还是两家不同公司。

| # | 公司 | ↔ | # | 公司 |
|---|---|---|---|---|
| 24 | SFPTURKEY Elektronik İth. İhr. Ticaret Ltd. Şt… | ↔ | 83 | SFP Turkey（sfpturkey.com.tr） |
| 26 | Makros AŞ（Makro Sistem） | ↔ | 81 | Makros A.Ş. |
| 28 | Hiperonline | ↔ | 145 | hiperonline.com |
| 29 | DE Secure（Desecure Technology） | ↔ | 89 | DE secure（desecuretechnology.com） |
| 30 | ORAL GÜVENLİK Sistemleri（Oral Companies 集团） | ↔ | 88 | ORAL GUVENLIK（oralcompanies.com） |
| 31 | F.A.S.T（Fabrika Aygıtları Sistem Teknolojisi A… | ↔ | 95 | F.A.S.T（fasttr.com） |
| 32 | Fiberix | ↔ | 102 | fiberix（fiberix.com.tr） |
| 33 | HCS（hescs.com） | ↔ | 93 | HCS（hescs.com） |
| 35 | Antalya Turkuaz Bilişim Teknolojileri | ↔ | 121 | turkuaz（antalyaturkuaz.com） |
| 38 | FOURLİNE | ↔ | 113 | fourline.com.tr |
| 39 | MEPA Elektronik | ↔ | 98 | MEPA Elektronik |
| 40 | AG Bilgisayar | ↔ | 114 | ag-bilgisayar（Aycan CAM） |
| 41 | FH Güvenlik Sistemleri ve Bilişim San. Tic. Lt… | ↔ | 116 | fhguvenlik（Hasti F. GOLLER） |
| 42 | BİLGEN ELEKTRONİK（GÜVENLİK SİSTEMLERİ... LTD.… | ↔ | 117 | BİLGEN ELEKTRONİK |
| 43 | Duzgun Toptan Ticaret（teksarf.com） | ↔ | 104 | Duzgun Toptan Ticaret（teksarf.com） |
| 44 | PROVES（Proves Bilgi Teknolojileri San. Tic. A.… | ↔ | 100 | PROVES（proves.com.tr） |
| 46 | TBI - Telemobil（tbi.com.tr） | ↔ | 80 | Telemobil（tbi.com.tr） |
| 47 | PELIKAN BILG. İTH. İHR.（Pelikan Bilgisayar） | ↔ | 138 | pelikanbilgisayar（Ahmet Karci） |
| 49 | Zeytek Bilişim ve Teknoloji Ürünleri Ltd. Şti. | ↔ | 136 | Zeytek（zeytek.com.tr） |
| 50 | FOLİNE BİLİŞİM TEKNOLOJİLERİ SAN. TİC. LTD. ŞT… | ↔ | 142 | FOLINE（foline.com.tr） |
| 51 | NAZEM CO İTH. İHR. SAN. TİC. LTD. ŞTİ.（NAZEMCO… | ↔ | 126 | NAZEMCO（Osama） |

## 九、相关目录

- 深度档案原件：`ingest/angora-1__arena-01a0ce39__5acb613/08-followup-dossiers-2026-11-01/`（21 份，**仍是 r41–r43 的原始出处**）
- 结构化管线（唯一权威）：`…/08-customer-pipeline/111-turkey-customer-pipeline.csv`
- 竞对地图（98 家）：`…/06-competitors/110-turkey-local-competitors.csv`
- 生成脚本：`…/08-customer-pipeline/build_tr_customers_r44.py`
