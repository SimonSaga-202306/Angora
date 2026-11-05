# TR Customers · 土耳其客户总表（一客户一 MD）

**这个文件夹是什么**：把仓库里**已有的土耳其客户底稿**，拆成**一家一个 Markdown 文件**，方便逐家看、逐家发、逐家跟。

- 文件数：**147**（客户 **146** 家 + 本 README）
- 数据源（唯一权威）：`ingest/angora-1__arena-01a0ce39__5acb613/01-text-verbatim/workstation/08-customer-pipeline/111-turkey-customer-pipeline.csv`（**145 行 × 17 列**）
- 额外 1 家：**Entegron / LONGLINE**（`146-…`）—— 它只在 `06-competitors/110` 第 20 行与原始名单 #44，**不在 111 管线里**。

---

## 一、怎么读（三件事）

1. **每个文件固定七段**：身份卡 → 我方核实的交换机产品线 → 当前供应链 → 联系人（逐字）→ 证据与核实等级 → 建议动作 → 备注。
2. **21 家有「附：完整研究档案」**（文件里带 📚 标记）：把 `08-followup-dossiers-2026-11-01/` 里的**八段档案 + r42 核验补录 + r43 商业深挖全文逐字并入**，所以这 21 个文件是**自包含**的，不用来回跳。
3. **没有合并任何记录**：111 里同一家公司在两批名单里各出现一次（如 `Makros A.Ş.` = #26 与 #81、`Telemobil` = #46 与 #80、`HAFYA` = #25 与 #82），**各自独立成文件**，文件顶部用 ⚠ 标出「疑与 #NNN 同一家」，**要不要合并由人判断**（共 21 组，见第五节）。

## 二、诚实边界（必读）

| 事项 | 实情 |
|---|---|
| 覆盖范围 | **111 的 145 行全覆盖**。你给的两批原始名单（`Turkey Client List.xlsx` 299 行 + `2025土耳其ISAF客户.xlsx` 98 家）**已经折进这 145 行**（见 `112-user-customer-lists-deepdive-2026-10-25.md`），所以这里不是「299+98=397 家」，而是**去重后的 145 家管线**。 |
| 深度差异 | **21 家有深度档案**（八段 + 核验 + 深挖）；其余 124 家只有管线表的字段（公司/城市/品牌/供应链/联系人/证据/建议动作）。**不要把 124 家当成「已调研」，它们只是「有档案」。** |
| 联系人来源 | 「联系人」**全部来自用户侧**（展会/微信/名单），`证据来源` 列才是我方独立抓取的内容。**对外沟通前先分清这两类。** |
| 报价 | 表里所有报价都是**历史口径**，含 DDP/关税的一律要重算。 |
| 第三方数据 | 规模/营收等若来自 Datanyze / ZoomInfo / RocketReach / Volza，均为**第三方推算**，非财报（详见各家深度档案）。 |

## 三、索引（按 111 序号）

| # | 客户 | 城市 | 层级 | 评分 | 深度档案 | 文件 |
|---|---|---|---|---|---|---|
| 1 | Telkolink + GelecekBT（同集团） | İstanbul/Şişli（分部 = Perpa… | A 核心 | 88 | 有 | [001-telkolink-gelecekbt.md](001-telkolink-gelecekbt.md) |
| 2 | NOVA Group（Novacom） | Ankara | A 核心 | 86 | 有 | [002-nova-group-novacom.md](002-nova-group-novacom.md) |
| 3 | Snexus Networks | İstanbul | A 核心 | 85 | 有 | [003-snexus-networks.md](003-snexus-networks.md) |
| 4 | Cenova Bilişim Teknolojileri | İstanbul | A 核心 | 82 | 有 | [004-cenova-bilisim-teknolojileri.md](004-cenova-bilisim-teknolojileri.md) |
| 5 | CryptoLink Elektronik Güvenlik Sistemleri | Ankara/Çankaya | A 核心（公共 niche） | 80 | 有 | [005-cryptolink-elektronik-guvenlik-sistemleri.md](005-cryptolink-elektronik-guvenlik-sistemleri.md) |
| 6 | Coptek | İstanbul/Balmumcu | B+ | 78 | — | [006-coptek.md](006-coptek.md) |
| 7 | Karer Güvenlik | İstanbul/Pendik | B+ | 76 | 有 | [007-karer-guvenlik.md](007-karer-guvenlik.md) |
| 8 | Hane Elektronik | İstanbul/Küçükçekmece | B+ | 74 | 有 | [008-hane-elektronik.md](008-hane-elektronik.md) |
| 9 | Öncü Güvenlik Sistemleri A.Ş. | İstanbul/Beykoz | B | 72 | 有 | [009-oncu-guvenlik-sistemleri-a-s.md](009-oncu-guvenlik-sistemleri-a-s.md) |
| 10 | ErETE | —（B2B 平台） | B | 71 | — | [010-erete.md](010-erete.md) |
| 11 | Eretekne（+ Isee，同 Asya Telekom 集团） | —（B2B 平台） | B | 70 | — | [011-eretekne-isee-asya-telekom.md](011-eretekne-isee-asya-telekom.md) |
| 12 | CCS Güvenlik | —（B2B 电商） | B | 69 | — | [012-ccs-guvenlik.md](012-ccs-guvenlik.md) |
| 13 | Rima Elektronik | Ankara | B | 68 | — | [013-rima-elektronik.md](013-rima-elektronik.md) |
| 14 | NFS Teknoloji | İstanbul | B | 67 | — | [014-nfs-teknoloji.md](014-nfs-teknoloji.md) |
| 15 | Koza Güvenlik Elektronik Sistemleri（GreenT… | İstanbul/Okmeydanı（Koza Pl… | B | 66 | — | [015-koza-guvenlik-elektronik-sistemleri-greentech.md](015-koza-guvenlik-elektronik-sistemleri-greentech.md) |
| 16 | Portel（industrialnetworkcenter.com） | İstanbul/Kartal | B | 65 | — | [016-portel-industrialnetworkcenter-com.md](016-portel-industrialnetworkcenter-com.md) |
| 17 | RF Teknoloji | — | B | 64 | — | [017-rf-teknoloji.md](017-rf-teknoloji.md) |
| 18 | iotsistem | İstanbul | B | 63 | — | [018-iotsistem.md](018-iotsistem.md) |
| 19 | Lansan | Ankara | B | 62 | — | [019-lansan.md](019-lansan.md) |
| 20 | Opax Mühendislik（opax.com） | Nevşehir Merkez（Opax Plaza… | B | 61 | 有 | [020-opax-muhendislik-opax-com.md](020-opax-muhendislik-opax-com.md) |
| 21 | CCTV Depo Güvenlik Teknolojileri AŞ | İstanbul/Şişli-Perpa | B | 60 | 有 | [021-cctv-depo-guvenlik-teknolojileri-as.md](021-cctv-depo-guvenlik-teknolojileri-as.md) |
| 22 | TeleOne | — | B- | 58 | — | [022-teleone.md](022-teleone.md) |
| 23 | Konak Güvenlik | İstanbul | B- | 55 | — | [023-konak-guvenlik.md](023-konak-guvenlik.md) |
| 24 | SFPTURKEY Elektronik İth. İhr. Ticaret Ltd… | İstanbul | B+ | 77 | — | [024-sfpturkey-elektronik-ith-ihr-ticaret-ltd-sti.md](024-sfpturkey-elektronik-ith-ihr-ticaret-ltd-sti.md) |
| 25 | HAFYA Technologies | İstanbul | B+ | 75 | — | [025-hafya-technologies.md](025-hafya-technologies.md) |
| 26 | Makros AŞ（Makro Sistem） | İstanbul | B+ | 73 | — | [026-makros-as-makro-sistem.md](026-makros-as-makro-sistem.md) |
| 27 | ONSİS Elektrik Elektronik Güvenlik Sisteml… | Ankara/Çankaya | B | 68 | — | [027-onsis-elektrik-elektronik-guvenlik-sistemleri-in.md](027-onsis-elektrik-elektronik-guvenlik-sistemleri-in.md) |
| 28 | Hiperonline | Eskişehir（总部，81 省覆盖） | B | 66 | — | [028-hiperonline.md](028-hiperonline.md) |
| 29 | DE Secure（Desecure Technology） | İstanbul | B- | 62 | — | [029-de-secure-desecure-technology.md](029-de-secure-desecure-technology.md) |
| 30 | ORAL GÜVENLİK Sistemleri（Oral Companies 集团… | Lefkoşa/北塞浦路斯（K.K.T.C.） | B- | 62 | — | [030-oral-guvenlik-sistemleri-oral-companies.md](030-oral-guvenlik-sistemleri-oral-companies.md) |
| 31 | F.A.S.T（Fabrika Aygıtları Sistem Teknoloji… | İstanbul/Ataşehir | B- | 60 | — | [031-f-a-s-t-fabrika-aygitlari-sistem-teknolojisi-a-s.md](031-f-a-s-t-fabrika-aygitlari-sistem-teknolojisi-a-s.md) |
| 32 | Fiberix | Gaziantep | B- | 60 | — | [032-fiberix.md](032-fiberix.md) |
| 33 | HCS（hescs.com） | Türkiye（布线全国体系） | B- | 58 | — | [033-hcs-hescs-com.md](033-hcs-hescs-com.md) |
| 34 | STASANET d.o.o. | Belgrade + Novi Sad（塞尔维亚） | B- | 57 | — | [034-stasanet-d-o-o.md](034-stasanet-d-o-o.md) |
| 35 | Antalya Turkuaz Bilişim Teknolojileri | Antalya/Muratpaşa | B- | 56 | — | [035-antalya-turkuaz-bilisim-teknolojileri.md](035-antalya-turkuaz-bilisim-teknolojileri.md) |
| 36 | Go Technology | Gaza（巴勒斯坦） | B- | 55 | — | [036-go-technology.md](036-go-technology.md) |
| 37 | Shnrise Güvenlik Sistemleri | İstanbul | B- | 55 | — | [037-shnrise-guvenlik-sistemleri.md](037-shnrise-guvenlik-sistemleri.md) |
| 38 | FOURLİNE | Bursa | B- | 54 | — | [038-fourline.md](038-fourline.md) |
| 39 | MEPA Elektronik | Kayseri | B- | 53 | — | [039-mepa-elektronik.md](039-mepa-elektronik.md) |
| 40 | AG Bilgisayar | Bodrum/Muğla | B- | 53 | — | [040-ag-bilgisayar.md](040-ag-bilgisayar.md) |
| 41 | FH Güvenlik Sistemleri ve Bilişim San. Tic… | İstanbul（Perpa-3 区位） | B- | 52 | — | [041-fh-guvenlik-sistemleri-ve-bilisim-san-tic-ltd-st.md](041-fh-guvenlik-sistemleri-ve-bilisim-san-tic-ltd-st.md) |
| 42 | BİLGEN ELEKTRONİK（GÜVENLİK SİSTEMLERİ... L… | Gebze/Kocaeli（工业区） | B- | 52 | — | [042-bilgen-elektronik-guvenlik-sistemleri-ltd-sti.md](042-bilgen-elektronik-guvenlik-sistemleri-ltd-sti.md) |
| 43 | Duzgun Toptan Ticaret（teksarf.com） | İstanbul/Bahçelievler（Topt… | B- | 51 | — | [043-duzgun-toptan-ticaret-teksarf-com.md](043-duzgun-toptan-ticaret-teksarf-com.md) |
| 44 | PROVES（Proves Bilgi Teknolojileri San. Tic… | İzmir/Bayraklı（Verapol Pla… | B- | 50 | — | [044-proves-proves-bilgi-teknolojileri-san-tic-a-s.md](044-proves-proves-bilgi-teknolojileri-san-tic-a-s.md) |
| 45 | Alamthal（الامثل للاتصالات و تقنية المعلوما… | Tripoli（Libya） | B- | 49 | — | [045-alamthal.md](045-alamthal.md) |
| 46 | TBI - Telemobil（tbi.com.tr） | İstanbul/Üsküdar | B | 70 | — | [046-tbi-telemobil-tbi-com-tr.md](046-tbi-telemobil-tbi-com-tr.md) |
| 47 | PELIKAN BILG. İTH. İHR.（Pelikan Bilgisayar… | İstanbul/Şişli（Perpa Ticar… | B | 64 | — | [047-pelikan-bilg-ith-ihr-pelikan-bilgisayar.md](047-pelikan-bilg-ith-ihr-pelikan-bilgisayar.md) |
| 48 | Bilge Güvenlik ve Teknoloji A.Ş. | İstanbul（+ Ankara/İzmir 分支… | B | 62 | — | [048-bilge-guvenlik-ve-teknoloji-a-s.md](048-bilge-guvenlik-ve-teknoloji-a-s.md) |
| 49 | Zeytek Bilişim ve Teknoloji Ürünleri Ltd.… | İstanbul/Sancaktepe | B- | 58 | — | [049-zeytek-bilisim-ve-teknoloji-urunleri-ltd-sti.md](049-zeytek-bilisim-ve-teknoloji-urunleri-ltd-sti.md) |
| 50 | FOLİNE BİLİŞİM TEKNOLOJİLERİ SAN. TİC. LTD… | İstanbul/Kağıthane | B- | 58 | — | [050-foline-bilisim-teknolojileri-san-tic-ltd-sti.md](050-foline-bilisim-teknolojileri-san-tic-ltd-sti.md) |
| 51 | NAZEM CO İTH. İHR. SAN. TİC. LTD. ŞTİ.（NAZ… | Türkiye | B- | 50 | — | [051-nazem-co-ith-ihr-san-tic-ltd-sti-nazemco.md](051-nazem-co-ith-ihr-san-tic-ltd-sti-nazemco.md) |
| 52 | upTech / Nokta Elektronik ve Bilişim Siste… | Istanbul Şişli Perpa | A 自有品牌switch主（r36 新入） | 78 | — | [052-uptech-nokta-elektronik-ve-bilisim-sistemleri-a.md](052-uptech-nokta-elektronik-ve-bilisim-sistemleri-a.md) |
| 53 | WINET（wi.com.tr） | TR（站点未披露城市） | A- 品牌+分销（r36 新入） | 64 | — | [053-winet-wi-com-tr.md](053-winet-wi-com-tr.md) |
| 54 | TekniksatGroup（TGD） | Istanbul（1992 创立） | A 自有品牌switch主（r36 新入） | 72 | — | [054-tekniksatgroup-tgd.md](054-tekniksatgroup-tgd.md) |
| 55 | ULAK Haberleşme | Ankara | B 防务客户池（r36 新入） | 45 | — | [055-ulak-haberlesme.md](055-ulak-haberlesme.md) |
| 56 | Optima / Optima Mühendislik Ltd. Şti. | Ankara Sincan（Başkent OSB… | A- 暖线（r37 新入） | 68 | 有 | [056-optima-optima-muhendislik-ltd-sti.md](056-optima-optima-muhendislik-ltd-sti.md) |
| 57 | Filiz Güvenlik Sistemleri Proje İnş. San.… | İzmir Konak（Mersinli 2817… | B 暖线（r37 新入） | 58 | 有 | [057-filiz-guvenlik-sistemleri-proje-ins-san-tic-ltd.md](057-filiz-guvenlik-sistemleri-proje-ins-san-tic-ltd.md) |
| 58 | Okisan Güvenlik Teknolojileri A.Ş. | İstanbul Şişli Okmeydanı（O… | A- 大型分销（r37 新入） | 70 | 有 | [058-okisan-guvenlik-teknolojileri-a-s.md](058-okisan-guvenlik-teknolojileri-a-s.md) |
| 59 | PavoTek（pavotek.com.tr） | （Pavo Group 见 110 行 1） | C 战略留档（r37 新入） | 10 | — | [059-pavotek-pavotek-com-tr.md](059-pavotek-pavotek-com-tr.md) |
| 60 | GMT Control（GMTCNT） | （İstanbul） | B（r37 新入） | 40 | — | [060-gmt-control-gmtcnt.md](060-gmt-control-gmtcnt.md) |
| 61 | MFD（mfd.com.tr） | İstanbul | C 不跟进（r37 新入） | 5 | — | [061-mfd-mfd-com-tr.md](061-mfd-mfd-com-tr.md) |
| 62 | Cebeci Grup | （İstanbul） | B（r37 新入） | 45 | — | [062-cebeci-grup.md](062-cebeci-grup.md) |
| 63 | Areskom | İstanbul Üsküdar | B-（r37 新入） | 35 | — | [063-areskom.md](063-areskom.md) |
| 64 | İntenet | （İstanbul） | B-（r37 新入） | 35 | — | [064-intenet.md](064-intenet.md) |
| 65 | Teamon | Ankara | B-（r37 新入） | 30 | — | [065-teamon.md](065-teamon.md) |
| 66 | İnovatech | İstanbul | B-（r37 新入） | 25 | — | [066-inovatech.md](066-inovatech.md) |
| 67 | Metcom | Ankara+İstanbul Ümraniye | B-（r37 新入） | 35 | — | [067-metcom.md](067-metcom.md) |
| 68 | Egemenelektronik | （İstanbul） | B-（r37 新入） | 30 | — | [068-egemenelektronik.md](068-egemenelektronik.md) |
| 69 | TeknolojiPazar | İzmir Konak | B（r37 新入） | 45 | — | [069-teknolojipazar.md](069-teknolojipazar.md) |
| 70 | TekmarShop（TEKMAR） | İstanbul Ümraniye | B-（r37 新入） | 25 | — | [070-tekmarshop-tekmar.md](070-tekmarshop-tekmar.md) |
| 71 | BaburTech | Ankara | B-（r37 新入） | 25 | — | [071-baburtech.md](071-baburtech.md) |
| 72 | LeMax Güvenlik | （İstanbul） | A- 自有品牌（r37 新入） | 55 | — | [072-lemax-guvenlik.md](072-lemax-guvenlik.md) |
| 73 | Kiracı Bilişim=ZKR（Kıraç 集团） | （İstanbul） | B（r37 新入） | 35 | — | [073-kiraci-bilisim-zkr-kirac.md](073-kiraci-bilisim-zkr-kirac.md) |
| 74 | RadioTeknoloji | （İstanbul） | C（r37 新入） | 15 | — | [074-radioteknoloji.md](074-radioteknoloji.md) |
| 75 | TechnoPC | İstanbul Ataşehir | A-（r37 新入） | 55 | — | [075-technopc.md](075-technopc.md) |
| 76 | Bimel | Ankara（总部+4 分支） | C 低（r37 新入） | 20 | — | [076-bimel.md](076-bimel.md) |
| 77 | Dacel Solutions | İstanbul Esenler | C（r37 新入） | 15 | — | [077-dacel-solutions.md](077-dacel-solutions.md) |
| 78 | Fiberden | İstanbul | C（r37 新入） | 15 | — | [078-fiberden.md](078-fiberden.md) |
| 79 | EuroCam Güvenlik | （İstanbul） | B- 待评估（r37 新入） | 30 | — | [079-eurocam-guvenlik.md](079-eurocam-guvenlik.md) |
| 80 | Telemobil（tbi.com.tr） | İstanbul | A 具体项目（ISAF25 新入） | 72 | 有 | [080-telemobil-tbi-com-tr.md](080-telemobil-tbi-com-tr.md) |
| 81 | Makros A.Ş. | İstanbul | A 工程（ISAF25 新入） | 70 | 有 | [081-makros-a-s.md](081-makros-a-s.md) |
| 82 | HAFYA | İstanbul | A 军项目（ISAF25 新入） | 70 | 有 | [082-hafya.md](082-hafya.md) |
| 83 | SFP Turkey（sfpturkey.com.tr） | İstanbul | A 既有客户（ISAF25 新入） | 68 | — | [083-sfp-turkey-sfpturkey-com-tr.md](083-sfp-turkey-sfpturkey-com-tr.md) |
| 84 | ONSIS ELEKTRONIK | （0232 区） | A 要样品（ISAF25 新入） | 68 | 有 | [084-onsis-elektronik.md](084-onsis-elektronik.md) |
| 85 | Netmax（Ugur Simsek） | İstanbul | A-（ISAF25 新入） | 66 | — | [085-netmax-ugur-simsek.md](085-netmax-ugur-simsek.md) |
| 86 | bilimsateknoloji（Muharrem KILIC） | （İstanbul） | A-（ISAF25 新入） | 66 | 有 | [086-bilimsateknoloji-muharrem-kilic.md](086-bilimsateknoloji-muharrem-kilic.md) |
| 87 | UGUR IMRE | （İstanbul） | A- 分销（ISAF25 新入） | 66 | — | [087-ugur-imre.md](087-ugur-imre.md) |
| 88 | ORAL GUVENLIK（oralcompanies.com） | （0392 区） | A- 价敏（ISAF25 新入） | 62 | — | [088-oral-guvenlik-oralcompanies-com.md](088-oral-guvenlik-oralcompanies-com.md) |
| 89 | DE secure（desecuretechnology.com） | İstanbul | A-（ISAF25 新入） | 62 | — | [089-de-secure-desecuretechnology-com.md](089-de-secure-desecuretechnology-com.md) |
| 90 | cansisteknoloji（Ahmet CAN） | （0332 区） | A-（ISAF25 新入） | 62 | — | [090-cansisteknoloji-ahmet-can.md](090-cansisteknoloji-ahmet-can.md) |
| 91 | Sami CEUIK | （微信） | A 订单级（ISAF25 新入） | 70 | 有 | [091-sami-ceuik.md](091-sami-ceuik.md) |
| 92 | Selim Kalaka（供应商侧线） | （微信，外国人中文很好） | A 战略（ISAF25 新入） | 68 | 有 | [092-selim-kalaka.md](092-selim-kalaka.md) |
| 93 | HCS（hescs.com） | （0352 Bilecik 区） | A-（ISAF25 新入） | 62 | — | [093-hcs-hescs-com.md](093-hcs-hescs-com.md) |
| 94 | KLASNET | （0501 区） | A- 分销意向（ISAF25 新入） | 62 | — | [094-klasnet.md](094-klasnet.md) |
| 95 | F.A.S.T（fasttr.com） | （0216 区） | A-（ISAF25 新入） | 60 | — | [095-f-a-s-t-fasttr-com.md](095-f-a-s-t-fasttr-com.md) |
| 96 | voltechelektronik | （0216 区） | A-（ISAF25 新入） | 58 | — | [096-voltechelektronik.md](096-voltechelektronik.md) |
| 97 | LABOR Mühendislik（Ramazan DAS） | （Ankara 0412 区） | A-（ISAF25 新入） | 58 | — | [097-labor-muhendislik-ramazan-das.md](097-labor-muhendislik-ramazan-das.md) |
| 98 | MEPA Elektronik | （İstanbul） | A-（ISAF25 新入） | 58 | — | [098-mepa-elektronik.md](098-mepa-elektronik.md) |
| 99 | viva bilgisayar（ismet Yavuz 老板） | Hatay | A-（ISAF25 新入） | 55 | — | [099-viva-bilgisayar-ismet-yavuz.md](099-viva-bilgisayar-ismet-yavuz.md) |
| 100 | PROVES（proves.com.tr） | （0232 区） | B（ISAF25 新入） | 50 | — | [100-proves-proves-com-tr.md](100-proves-proves-com-tr.md) |
| 101 | NECDET SENKACAYC | （İstanbul） | B（ISAF25 新入） | 48 | — | [101-necdet-senkacayc.md](101-necdet-senkacayc.md) |
| 102 | fiberix（fiberix.com.tr） | İstanbul | B-（ISAF25 新入） | 45 | — | [102-fiberix-fiberix-com-tr.md](102-fiberix-fiberix-com-tr.md) |
| 103 | acusenseteknoloji（Umit Celik） | （0216 区） | B-（ISAF25 新入） | 45 | — | [103-acusenseteknoloji-umit-celik.md](103-acusenseteknoloji-umit-celik.md) |
| 104 | Duzgun Toptan Ticaret（teksarf.com） | （İstanbul） | B-（ISAF25 新入） | 42 | — | [104-duzgun-toptan-ticaret-teksarf-com.md](104-duzgun-toptan-ticaret-teksarf-com.md) |
| 105 | IHM Technology | （0216 区） | B bypass（ISAF25 新入） | 50 | — | [105-ihm-technology.md](105-ihm-technology.md) |
| 106 | sinerjik（Ufuk GOKALP） | İstanbul | B-（ISAF25 新入） | 40 | — | [106-sinerjik-ufuk-gokalp.md](106-sinerjik-ufuk-gokalp.md) |
| 107 | Ecevit（marbim.com.tr） | （0242 区） | B（ISAF25 新入） | 42 | — | [107-ecevit-marbim-com-tr.md](107-ecevit-marbim-com-tr.md) |
| 108 | DIMAS TEKNOLOJI VE GUVENLIK | （0530 区） | C（ISAF25 新入） | 30 | — | [108-dimas-teknoloji-ve-guvenlik.md](108-dimas-teknoloji-ve-guvenlik.md) |
| 109 | basaranelektronik（Emrah Basaran 老板） | （0266 区） | C（ISAF25 新入） | 30 | — | [109-basaranelektronik-emrah-basaran.md](109-basaranelektronik-emrah-basaran.md) |
| 110 | Fadi | （İstanbul） | C（ISAF25 新入） | 28 | — | [110-fadi.md](110-fadi.md) |
| 111 | Ali Goktork | （Ankara） | C（ISAF25 新入） | 28 | — | [111-ali-goktork.md](111-ali-goktork.md) |
| 112 | D&N ELEKTRIK MUHENDISLIK | （0541 区） | C（ISAF25 新入） | 25 | — | [112-d-n-elektrik-muhendislik.md](112-d-n-elektrik-muhendislik.md) |
| 113 | fourline.com.tr | （0224 区） | C（ISAF25 新入） | 25 | — | [113-fourline-com-tr.md](113-fourline-com-tr.md) |
| 114 | ag-bilgisayar（Aycan CAM） | （0252 区） | B+ bypass（ISAF25 新入） | 52 | — | [114-ag-bilgisayar-aycan-cam.md](114-ag-bilgisayar-aycan-cam.md) |
| 115 | 3s.com.tr（SAVAS TULGAR） | （0533 区） | C+（ISAF25 新入） | 30 | — | [115-3s-com-tr-savas-tulgar.md](115-3s-com-tr-savas-tulgar.md) |
| 116 | fhguvenlik（Hasti F. GOLLER） | （0535 区） | B-（ISAF25 新入） | 35 | — | [116-fhguvenlik-hasti-f-goller.md](116-fhguvenlik-hasti-f-goller.md) |
| 117 | BİLGEN ELEKTRONİK | （İstanbul） | B bypass（ISAF25 新入） | 45 | — | [117-bilgen-elektronik.md](117-bilgen-elektronik.md) |
| 118 | ANIL（aniltelekom.com） | İstanbul | C（ISAF25 新入） | 25 | — | [118-anil-aniltelekom-com.md](118-anil-aniltelekom-com.md) |
| 119 | BTM ELECTRONIC | （0532 区） | C（ISAF25 新入） | 25 | — | [119-btm-electronic.md](119-btm-electronic.md) |
| 120 | ebatek（BALKIS S.Coskun CEO） | İstanbul | C（ISAF25 新入） | 25 | — | [120-ebatek-balkis-s-coskun-ceo.md](120-ebatek-balkis-s-coskun-ceo.md) |
| 121 | turkuaz（antalyaturkuaz.com） | Antalya | C（ISAF25 新入） | 25 | — | [121-turkuaz-antalyaturkuaz-com.md](121-turkuaz-antalyaturkuaz-com.md) |
| 122 | GÜNGÖR ELEKTRONİK | （İstanbul） | C（ISAF25 新入） | 22 | — | [122-gungor-elektronik.md](122-gungor-elektronik.md) |
| 123 | Sedat（微信） | （İstanbul） | B-（ISAF25 新入） | 45 | — | [123-sedat.md](123-sedat.md) |
| 124 | Interland Network & Security | （İstanbul） | B-（ISAF25 新入） | 42 | — | [124-interland-network-security.md](124-interland-network-security.md) |
| 125 | Smali（微信） | （İstanbul） | C（ISAF25 新入） | 22 | — | [125-smali.md](125-smali.md) |
| 126 | NAZEMCO（Osama） | （İstanbul） | B-（ISAF25 新入） | 40 | — | [126-nazemco-osama.md](126-nazemco-osama.md) |
| 127 | Serkan（Alisa 客户） | （İstanbul） | C（ISAF25 新入） | 25 | — | [127-serkan-alisa.md](127-serkan-alisa.md) |
| 128 | Fatih A（微信） | （İstanbul） | B+（ISAF25 新入） | 48 | — | [128-fatih-a.md](128-fatih-a.md) |
| 129 | Celali Ayazoglu | （İstanbul） | C（ISAF25 新入） | 22 | — | [129-celali-ayazoglu.md](129-celali-ayazoglu.md) |
| 130 | 90543 780 22 23（合影客） | （Ankara） | B-（ISAF25 新入） | 35 | — | [130-90543-780-22-23.md](130-90543-780-22-23.md) |
| 131 | wechat:TeT529 | （İstanbul） | C（ISAF25 新入） | 20 | — | [131-wechat-tet529.md](131-wechat-tet529.md) |
| 132 | Ertan Kral | （İstanbul） | C（ISAF25 新入） | 25 | — | [132-ertan-kral.md](132-ertan-kral.md) |
| 133 | Enes Talha Karaaslan（微信） | （İstanbul） | C（ISAF25 新入） | 28 | — | [133-enes-talha-karaaslan.md](133-enes-talha-karaaslan.md) |
| 134 | Gokhan（微信） | （İstanbul） | C（ISAF25 新入） | 25 | — | [134-gokhan.md](134-gokhan.md) |
| 135 | NORTEL İletişim（norteliletisim.com） | （0242 区） | C（ISAF25 新入） | 25 | — | [135-nortel-iletisim-norteliletisim-com.md](135-nortel-iletisim-norteliletisim-com.md) |
| 136 | Zeytek（zeytek.com.tr） | İstanbul | C（ISAF25 新入） | 25 | — | [136-zeytek-zeytek-com-tr.md](136-zeytek-zeytek-com-tr.md) |
| 137 | Bilge SECURITY SYSTEMS | （İstanbul） | C+（ISAF25 新入） | 30 | — | [137-bilge-security-systems.md](137-bilge-security-systems.md) |
| 138 | pelikanbilgisayar（Ahmet Karci） | （0541 区） | C（ISAF25 新入） | 22 | — | [138-pelikanbilgisayar-ahmet-karci.md](138-pelikanbilgisayar-ahmet-karci.md) |
| 139 | Interpos（inter-pos.com） | İstanbul | C（ISAF25 新入） | 22 | — | [139-interpos-inter-pos-com.md](139-interpos-inter-pos-com.md) |
| 140 | camsanordu（0553 区） | （Tekirdağ 区） | C（ISAF25 新入） | 22 | — | [140-camsanordu-0553.md](140-camsanordu-0553.md) |
| 141 | teknoktadestek.com | İstanbul | C（ISAF25 新入） | 22 | — | [141-teknoktadestek-com.md](141-teknoktadestek-com.md) |
| 142 | FOLINE（foline.com.tr） | İstanbul | C（ISAF25 新入） | 25 | — | [142-foline-foline-com-tr.md](142-foline-foline-com-tr.md) |
| 143 | Holil | （İstanbul） | C+（ISAF25 新入） | 28 | — | [143-holil.md](143-holil.md) |
| 144 | Marmaris Bilişim | Marmaris | C（ISAF25 新入） | 22 | — | [144-marmaris-bilisim.md](144-marmaris-bilisim.md) |
| 145 | hiperonline.com | Eskişehir | C（ISAF25 新入） | 25 | — | [145-hiperonline-com.md](145-hiperonline-com.md) |
| 146 | Entegron ／ LONGLINE（双品牌） | İstanbul / Bayrampaşa | A-（客户侧） | 30A/45A | 有 | [146-entegron-longline.md](146-entegron-longline.md) |

## 四、从哪儿开始（建议顺序）

1. **A 级 + 有深度档案的 6 家**：#4 Cenova、#9 Öncü、#7 Karer、#56 Optima、#80 Telemobil、#58 Okisan —— 有产品空档、有联系人、有打法。
2. **订单级/窗口级 3 家**：#91 Sami（500 台）、#92 Selim（换源窗口）、#84 ONSIS（回头要样品）—— **只能靠人推进，爬虫无效**。
3. **B/C 级 124 家**：先扫 `建议动作` 列，只挑「有具体项目/有自有品牌」的动，其余作为备选池。

## 五、重复对（21 组，两批名单各录一次）

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

## 六、相关目录

- 深度档案原件：`ingest/angora-1__arena-01a0ce39__5acb613/08-followup-dossiers-2026-11-01/`（21 份，**仍是 r41–r43 的原始出处**）
- 结构化管线（唯一权威）：`…/08-customer-pipeline/111-turkey-customer-pipeline.csv`
- 竞对地图（98 家）：`…/06-competitors/110-turkey-local-competitors.csv`
- 生成脚本：`…/08-customer-pipeline/build_tr_customers_r44.py`
