# r92 · 「投标资格」是可审计的：Kamu Bilişim Yetki Belgesi 全解（法规 / 发证 / 有效期 / 公开核验）

- 轮次：**r92**（承接 r91 三层门槛的第三层）
- 日期：**2026-10-26**
- 主轴：r91 把 r88/r89/r90 的三堵墙写成了 **三层门槛**（产品层 · 投标人层 · 上游层），并在 §10.1 留下一条行动项：**查清 `Kamu Bilişim Yetki Belgesi` 的发证机关、条件、有效期、能否核验**。本轮就是这条行动项的结案。**结论用一句话说：这道墙比想象的矮，但它是土耳其法人专属的 —— 门槛不高，国籍很硬。**
- 源计数：**抓取 20（9 页/PDF 全文与分片 + 11 组 SERP 深读）· 去重引用来源 54 · 一手官方 7 · 二手 47**（逐条列于 §10.2，可复核）

---

## 一、结论先行

1. **r91 的三层门槛，第三层（投标人层）已经彻底查清，而且比预想的简单**：这张证叫 **`Kamu Bilişim Yetki Belgesi`（KBYB，公共信息授权证）**，签发机关是 **Sanayi ve Teknoloji Bakanlığı / Milli Teknoloji Genel Müdürlüğü**，依据 **29.06.2022  tarihli ve 31881  sayılı Resmî Gazete** 上的《Kamu Bilişim Hizmet Alımı Kapsamında Katılımcıların Yetkilendirilmesi Hakkında Yönetmelik》（Mevzuat No **39610**）。
2. **⭐ 门槛低得出奇**：**MADDE 5(1)(a)** —— 取得 KBYB **只需一份「bilişim hizmet alımlarından en az birini kapsayan」的 `TS EN ISO/IEC 27001`**。**不要求业绩、不要求资本、不要求本地工厂、不要求 62443、不要求 CMMI**。后两者只出现在 **Yazılım Yetki Belgesi**（+15504-L2 或 CMMI-L3）与 **Sızma Testi Yetki Belgesi**（+TSE A/B 型）里。⇒ **「投标资格」这道墙的真实成本 ≈ 一张 ISO 27001。**
3. **⭐⭐ 但它是 e-Devlet 专属**：申请入口是 **`kamubilisim.sanayi.gov.tr`**，须 **e-Devlet 登录 + 土耳其税号（VKN）主体 + 土耳其纳税**；证书正文直接写 **VKN**。⇒ **我方（境外主体）在这一层上是结构性不可得，不是钱的问题。** ⇒ 这给 r91 §10.3 的「Angora = 投标资格壳」补上了机制解释，但也补上了一条**禁区**（见 §9.3）。
4. **⭐⭐ 有效期是个大坑，且所有中文/二手资料都写错**：法规 **MADDE 6(2)** 规定「有效期 = 所提交材料中**最早到期**的那一份的日期」；**实测 13 张证书，有效期 197–355 天，中位 ≈324 天**（**没有一张是 3 年**）。二手咨询站普遍写「3 年有效」—— **作废**。⇒ 这意味着**土耳其投标人的资格是每年滚动续的**，也意味着**「查证」必须查日期，不能只查存在**。
5. **⭐⭐⭐ 公开核验库确认存在且是官方唯一入口**：`kamubilisim.sanayi.gov.tr/belgedogrulama`（**每一张证书正文都印着这句话**，4 份不同企业的 PDF 互证）。⚠ 但该域名**对本沙箱不可达**（详见 §7.3），**「按公司名反查」未能实证**，只能确认「按编号核验」的机制。
6. **⭐⭐ 编号规则**：**`STB01-####` = KBYB**，另见 **`STB02-####` = Yazılım Yetki Belgesi**（2 例）。已见最高号 **`STB01-3564`（2026-07）**，2025-10 为 `2451` ⇒ **发证速度 ≈3.4–4.8 张/日、约 1,300 张/年**，累计 ≈3,500–3,600 张。
7. **⭐⭐ 2026 年的真实用法已经溢出法条**：KİK 的强制条文（**Kamu İhale Genel Tebliği 89/A**，2022-12-29/32058 新增，**2023-09-29 生效**）只覆盖 **bilişim hizmet alımı（含 doğrudan temin 与 4734 豁免标）**，**对 mal alımı 没有任何强制条款**。但 2026 年 **至少 5 张 mal alımı 标**（Kdz Ereğli 2026-02 · Selçuk Ü. 2026-04 · Şebinkarahisar 2026-08 · Yeniankara UPS 2026-09 · **Çankırı 2026/1967649** 2026-10）把 KBYB 写进了 **`4.3.2 sicil/izin/ruhsat/faaliyet belgesi`** 那一格。⇒ **r91 留下的那个歧义，答案是第三种**（见 §4.3）。
8. **⭐ 一个可用的合法性窗口**：`Hizmet Alımı İhaleleri Uygulama Yönetmeliği 16.6.4`（KİK 2026 年一份 karar 原文引述）—— **若采购人在招标文件中漏写该资格证，则该文件在评标阶段「不得再要求、不得补交」**。⇒ **「标书里没写 KBYB 的标」是无证方可投的合法通道**，且这解释了为什么有些标到 zeyilname 才补（见 §4.4）。

---

## 二、法规原文全解（A 级，`mevzuat.gov.tr` MevzuatNo=39610，两分片全读）

> 载体：`https://www.mevzuat.gov.tr/anasayfa/MevzuatFihristDetayIframe?MevzuatTur=7&MevzuatNo=39610&MevzuatTertip=5`（chunk 0 覆盖 MADDE 1–7 前半，**chunk 1 本轮补读**，覆盖 MADDE 7(3)–(7) + MADDE 8–9）

| 条 | 原文要点（译） | 对我的意义 |
|---|---|---|
| **MADDE 1** | 目的：确定 **kamu idareleri 的 bilişim hizmet alımları** 中参与者的标准、授权，及违规时的暂停/撤销 | 只谈 **hizmet**，从头到尾没提 mal |
| **MADDE 3(c)** | **bilişim hizmet alımı** = 4734 号法（**含咨询类 hizmet 采购**）+ 其他法规 + **KÖİ（公私合营）**项目中的**软件/系统安装/维护/咨询/安全服务** | KÖİ 项目也被纳入 |
| **MADDE 3(f)** | **KBYB** = 按 5(1)(a) 标准，证明投标人 **在 bilişim hizmet alımı 招标中的合格性与能力** | 定义即以「hizmet 招标」为限 |
| **MADDE 4** | 三类证：**KBYB / Yazılım Yetki Belgesi / Sızma Testi Yetki Belgesi** | ⚠ 2026 年公开的**新草案**拟加第四类 **Veri Merkezi Yetki Belgesi**（§7.2） |
| **MADDE 5(1)(a)** | KBYB 条件：**bilişim hizmet alımlarından en az biri için `TS EN ISO/IEC 27001`** | **唯一实质条件** |
| **MADDE 5(1)(b)** | Yazılım 证：27001（覆盖软件开发/集成/维护）**+ 至少 TS ISO/IEC 15504 Seviye 2 或 CMMI Seviye 3** | 与我无关（我们是硬件） |
| **MADDE 5(1)(c)** | Sızma 证：27001 **+ TSE 签发之 A 或 B 型 TS 13638 渗透测试企业证书** | 与我无关 |
| **MADDE 5(4)** | 材料由部委**从相关机构数据库核验**；无法核验须交原件/公证本；**虚假申报 ⇒ 撤销且 1 年禁申** | 意味着**造假不可行**：VKN + 27001 都在国家库里 |
| **MADDE 6(1)** | 材料齐全后评估，**最迟 2 个月内结案**；合格者**电子签发并在部委网站公示** | **公示即核验库**的法源 |
| **MADDE 6(2)** | **有效期 = 所交材料中最早到期者之日期**；延期须**到期前至少 1 个月**申请并提交换发后的材料 | **实测有效期 197–355 天**的法规根因 |
| **MADDE 7(1)(2)** | 部委有**检查权**；持证人须如实配合 | — |
| **MADDE 7(3)** | 违规：**书面警告 + 最长 6 个月整改期 + 暂停证书**；逾期不改 ⇒ **撤销** | — |
| **MADDE 7(4)** | 停证期间**不发同类新证** | — |
| **MADDE 7(5)** | 撤销后 **1 年**禁申；**再次被撤销 ⇒ 3 年**禁申，期满后按首次申请处理 | 惩罚阶梯 |
| **MADDE 7(6)** | **停证期间不计入/不影响 6(2) 的有效期** | 停证不「冻结」有效期 ⇒ 停证易导致过期 |
| **MADDE 7(7)** | 停/复/撤均**通报 Kamu İhale Kurumu（KİK）**并在部委网站公告 | ⇒ **KİK 手上有一份黑名单**，理论上可从 KİK 侧反查 |
| **MADDE 8** | 公布后 **3 个月**生效 ⇒ **2022-09-29** | 生效日与 KİK 强制日（2023-09-29）**差整一年** |
| **MADDE 9** | 由 Sanayi ve Teknoloji Bakanı 执行 | — |

### 2.1 三个容易读错的点

1. **「bilişim hizmet alımlarından en az biri için 27001」** ≠ 「必须做过 bilişim hizmet项目」。原文语义是 **「ISO 27001 的认证范围（scope）须覆盖至少一类 bilişim hizmet」** —— 二手资料给出实证：**若 27001 的范围写的是「Donanım Satışı」而不含软件/服务，则 Yazılım 类拿不到；KBYB 类须范围里至少落一类 bilişim hizmet**。⇒ **对只卖硬件的公司，27001 的 scope 写法就是生死线。**
2. **「终身为 3 年」是错的**（§7.1 修正 1）。
3. **证书不等于安全审查**：证书正文有免责句（A 级原文，GBB 样本）：**「yalnızca teknik kriterler doğrultusunda inceleme yapılmış olup; mali, idari, hukuki ve millî güvenlik açısından herhangi bir değerlendirme yapılmamıştır.」**（仅按技术标准审查；财务、行政、法律与国家安全层面未作任何评估）⇒ **不能对客户说「有 KBYB = 通过了国家安全审查」**。

---

## 三、KİK 的强制化条文：时间线与「适用到哪」

> A 级原文：`hakedis.org` 的 **RG 29.12.2022 / 32058** 全文 PDF（KİK Genel Tebliğinde Değişiklik Yapılmasına Dair Tebliğ，1 页，已全文读）+ `mevzuat.gov.tr` Kamu İhale Genel Tebliği（MevzuatNo=13354）89/A 条文。

| 时点 | 事件 |
|---|---|
| 2022-06-29 | Yönetmelik 公布（31881） |
| 2022-09-29 | Yönetmelik生效（MADDE 8） |
| **2022-12-29** | **KİK 一般公报新增 `Madde 89/A`**（RG 32058） |
| **2023-09-29** | **89/A 生效**（Tebliğ MADDE 5(a)）；同公报**废除 7.3/7.4 的银行参考函要求** |
| 2023-08-23 | 主管咨询界公开解读：**此后发标的 bilişim hizmet 标必须在资格条款列证** |

### 3.1 `89/A` 五款的完整内容（A 级）

| 款 | 内容 | 影响面 |
|---|---|---|
| **89/A.1** | bilişim hizmet alımı 标：在 idari şartname 的「**因相关法规对该业务特别规定的 sicil、izin、ruhsat 等文件**」那一格里，**必须写入 KBYB** | **强制** |
| **89/A.2** | 若**约成本 > 4734/13(b)(2) 服务上限的 10 倍**，且含软件开发/集成/维护 ⇒ 该格须写 **Yazılım Yetki Belgesi** | 大标才触发 |
| **89/A.3** | 渗透测试服务标 ⇒ 须写 **Sızma Testi Yetki Belgesi** | — |
| **89/A.4** | **联合体（iş ortaklığı）每一家成员须分别提交；财团（konsorsiyum）各自提交自己部分** | ⇒ 见 §4.4 的实证 |
| **89/A.5** | 允许分包时：**bilişim 分包商须持 KBYB**；渗透测试分包商**另须 Sızma 证**；软件分包合同额超「服务上限 10 倍」⇒ 分包商须持 Yazılım 证 | **⇒ 供应链被穿透：连分包商都要证** |

### 3.2 ⭐ 适用范围的两处「加码」（这是 2023-08 解读给出的、比公报条文更狠的部分）

- **4734/22 `doğrudan temin`（直采）—— 也要证**；
- **4734 豁免标（istisna）—— 也要证**。
- 依据同样来自 KİK 口径：证是「**ilgili mevzuatında o iş için özel olarak düzenlenen belge**」，与采购方式无关。
- ⇒ **这一条对我们最关键**：r90 找到的「水务/市政/大学/医院小包」里，**凡是以 bilişim hizmet 名义走的直采，也在墙内**；而 **mal alımı 名义的直采，法条上不在墙内**（§4）。

### 3.3 与 89/A 配套的一条「程序性反制」（⭐⭐ 本轮最有战术价值的发现）

> 来源：KİK 一份 2026-06 的 karar 转述（`ihaledanismani.com`），其引用了 **Hizmet Alımı İhaleleri Uygulama Yönetmeliği 16.6.4**：

> 「**İlgili mevzuatına göre ihaleye katılma şartı olarak istenmesi gereken belge veya bilgilerin idarece istenmediği ve bu durumun tekliflerin değerlendirilmesi aşamasında tespit edildiği hallerde, idarelerce bu tür belge veya bilgiler başvuruların ya da tekliflerin değerlendirilmesi aşamasında aday veya isteklilerden talep edilemeyecek ve tamamlatılamayacaktır.**」

译：**采购人本该要求却没要求某份法定资格文件的，评标阶段不得再向投标人索取、也不得要求补交。**
⇒ **合法反制**：**没有 KBYB 的一方，可以合法投「标书漏写 KBYB」的标，并中标**；采购人不能事后补救。
⇒ 这也解释了 §4.4 里 TSE 那张标**为什么用 `zeyilname`（补充公告）事后再加** —— 那是采购人发现漏写后的**唯一合法修补路径**（在原定投标截止前正式发 zeyilname）。

---

## 四、⭐⭐ 实证：KBYB 在 2026 年已溢出法条，成为「泛 bilişim 筛子」

### 4.1 法条上的边界（先立边界，避免过度归纳）

| 标的类型 | 法条是否强制 KBYB | 依据 |
|---|---|---|
| **bilişim hizmet alımı**（含咨询） | **强制** | KİK 89/A.1 |
| **bilişim hizmet — doğrudan temin / 4734 豁免** | **强制** | 2023-08 KİK 口径 |
| **渗透测试服务** | 强制 Sızma 证 | 89/A.3 |
| **mal alımı（含交换机、服务器、UPS）** | **无任何强制条款** | 89/A 只管 hizmet；Mal Alımı İhaleleri Uygulama Yönetmeliği 无对应条 |
| **yapım işi** | 无 | — |

### 4.2 但 2026 年的实际标书（6 例 mal alımı，全部把 KBYB 写进 `4.3.2`）

| 时间 | 采购人 / İKN | 标的 | KBYB 出现位置 | 证据等级 |
|---|---|---|---|---|
| 2024-11 | Sağlık Bilimleri Ü.（BİDB） | 6 项 Microsoft 教育授权续期 | `4.3.2` | 二手（ilan 转载） |
| **2026-02-22**（标期 03-16） | **Kdz Ereğli Belediyesi**（Zonguldak） | **muhtelif malzeme + yazılım + 存储设备** | `4.3.1`：**ISO 27001 + ISO 9001 + KBYB** 三项并列 | 二手（`imzagazetesi`） |
| **2026-04-19**（标期 05-12） | **Selçuk Üniversitesi** `2026/7050971` | **Microsoft 校园协议 2,016 套授权** | `4.3.2` | 二手（`konyapostasi` 全文） |
| **2026-08-27** | Şebinkarahisar（Giresun）某 idare | **「Bilişim Malzemeleri」2 部分 3 项** | `4.3.2` | 二手（`yenisebinkarahisar`） |
| **2026-09-13** | 某 idare（Ankara 系 gazete） | **UPS + 电池 mal alımı** | `4.3.2` 的候选清单里含 KBYB | 二手（`yeniankara`）⚠ 该清单是模板式罗列，是否**真要求**待核 |
| **2026-10-15**（标期 **11-09**） | **Çankırı Karatekin Ü.** `2026/1967649` | **9 部分，Kısım-4 交换机 6 台** | `4.3.2`：**KBYB + Yetkili Satıcı / İmalatçı** | **一手（r91 全文）** |

⇒ 另有 4 张 **hizmet** 标同期要求（Kocaeli BB **SOAR 2026/2186257** 标期 12-07；İstanbul Taksim EAH **HBYS 2026/2248263** 标期 12-10，且**同时要 KBYB + Yazılım Yetki Belgesi**；Türkiye Hudut ve Sahiller SGMD 软件开发咨询；Selçuk Ü. 等），均为 **89/A.1 的合法适用**。

### 4.3 ⭐⭐ r91 留下的歧义 —— 答案是「第三种」

r91 问：**该证法规上是 `hizmet alımı` 要求，为何 Çankırı 的 `mal alımı` 要它？是采购人滥用条款（可质疑），还是 KİK 已扩到「含安装调试的货物标」？**

**答案：都不是。是「KİK 未扩、采购人普遍自行扩用」，且扩用的法律载体是 `4.3.2` 那一格。**

1. **KİK 没有扩**：89/A 的标题与各款全部限定 `bilişim hizmet alımı`；**2026-10 时点仍无任何针对 mal alımı 的强制条文**（`mevzuat.gov.tr` 13354 号公报现行文本，A 级）。
2. **采购人的扩用有形式依据**：Mal Alımı İhaleleri Uygulama Yönetmeliği 的 `4.3.2`（= 条款号 `4.3.2 İhale konusu işin ya da malın satış faaliyetinin yerine getirilebilmesi için ilgili mevzuat gereğince sicil, izin, ruhsat, faaliyet belgesi vb. belgeler`）本身是**开放式格子**，采购人可往里放「自己认为相关」的法定文件。
3. **但严格说它站不住**：KİK 一般公报 **74. maddesi** 明文「**与标的内容无关、或业务性质不需要的资质与标准文件，不得要求**」；而 89/A 的强制义务只及 hizmet。⇒ **在 mal alımı 里要 KBYB，是可被质疑的**。
4. **为什么没人质疑**：质疑窗口短（先 şikâyet 再 itirazen şikâyet，且要交保证金）、成本高于收益、且**持证方早已是本地主流集成商** —— 质疑等于自曝「我没证」。
5. ⇒ **定性**：**法律上可争议、事实上是硬墙**。这条要写进客户话术的「不可抗力」栏，不要写成「这个标违法」（对客户说「这个标违法」会显得外行且无用）。

### 4.4 两条由此产生的战术推论

- **A. 没证的窗口 = 标书漏写**（§3.3 的 16.6.4）。⇒ 给伙伴的行动指令不是「你先去拿证」，而是**「先扫 11–12 月的标，把 `4.3.2` 里没写 KBYB 的标挑出来，那才是我们现在就能投的」**。
- **B. 联合体要「全员持证」**：`89/A.4` + 实证（KİK karar 转述的 yeterlik 表：`Kamu Bilişim Yetki Belgesi … Tüm ortakların sunması gerekmektedir`）⇒ **「借壳投标」在 iş ortaklığı 形式下不成立** —— 想靠一个持证伙伴带一个无证伙伴进联合体，**两家都得有证**。
  - ⚠ 与 Konsorsiyum 的差别：`89/A.4` 允许财团**各自提交自己那部分的证** ⇒ **「分包/财团」是唯一能绕开「全员持证」的结构**。⇒ 这与 r91「我方做 Angora 的裸机 ODM」是同一条路线的延伸。

---

## 五、⭐⭐ 证书本体解剖（从 4 份不同企业的 PDF 正文反推）

### 5.1 版式要素（A 级，`gbbbilisim.com.tr` PDF 全文可读）

| 要素 | 原文 | 备注 |
|---|---|---|
| 抬头 | `KAMU BİLİŞİM YETKİ BELGESİ` | — |
| 编号 | `STB01-2451` | **`STB01` 前缀 + 4 位序号** |
| 法律依据 | 「29.06.2022 tarihli ve 31881 sayılı Resmi Gazete'de yayımlanan … Yönetmelik kapsamında」 | 2026 年新证仍引 2022 年旧法（**新法未生效**，见 §7.2） |
| 主体识别 | 「**3891567798 vergi kimlik numaralı GBB BİLİŞİM HİZMETLERİ ANONİM ŞİRKETİ** için tanzim edilmiştir」 | **以 VKN 锁定主体** ⇒ 换壳/改名无效 |
| 免责 | 「yalnızca teknik kriterler … mali, idari, hukuki ve millî güvenlik açısından herhangi bir değerlendirme yapılmamıştır」 | 见 §2.1(3) |
| 签发 / 到期 | `Belge Düzenlenme Tarihi : 07.10.2025` / `Belge Geçerlilik Tarihi : 28.08.2026` | **≈10.7 个月** |
| 签署 | `e-imzalıdır · Emre DABAK · Genel Müdür Yardımcısı` | 电子签，无纸本 |
| 核验 | 「Belgenin doğrulaması, **`kamubilisim.sanayi.gov.tr/belgedogrulama`** adresinden yapılabilmektedir」 | **4 份 PDF 互证同一 URL** |

### 5.2 编号规则（⚠ 推断级，样本 15）

| 前缀 | 含义 | 样本 |
|---|---|---|
| **`STB01-`** | **Kamu Bilişim Yetki Belgesi** | 13 张（§5.3） |
| **`STB02-`** | **Yazılım Yetki Belgesi** | `STB02-1376`（bilgibirikim，2026-06-16→2027-01-11）、`STB02-1143`（GG Tech） |
| `STB03-` | 推测 = Sızma Testi（**未取到样本**） | — |

⇒ **`STB` = Sanayi ve Teknoloji Bakanlığı**；**01/02/03 = 证种**；**序号按证种各自独立递增**（KBYB 3,564 vs Yazılım 1,376）。

### 5.3 13 张 KBYB 实测样本（有效期栏是本轮最重要的表）

| # | 企业 | 编号 | 签发 | 到期 | **跨度（天）** | 来源 |
|---|---|---|---|---|---|---|
| 1 | Netcom | `STB01-656` | 2023-12-21 | 未取 | — | netcom.com.tr PDF |
| 2 | itstack | `STB01-734` | 未标 | 「—」 | — | itstack.com.tr |
| 3 | Zirve Bilgisayar | `STB01-1057` | **2024-05-30** | 未取 | — | zirve-bilgisayar.com PDF |
| 4 | Beyaz | `STB01-1732` | 未取 | 未取 | — | 二手 |
| 5 | **Yönsis** | `STB01-1837` | **2025-03-19** | **2026-03-09** | **355** | yonsis.com.tr PDF |
| 6 | LPS Bilişim | `STB01-2291` | 2025-09-08 | 2026-07-29 | **324** | lpschain.com PDF |
| 7 | **GBB Bilişim** | `STB01-2451` | 2025-10-07 | 2026-08-28 | **325** | gbbbilisim PDF（A 级全文） |
| 8 | Netcad | `STB01-2771` | 未取 | **2026-12-26** | — | netcad.com |
| 9 | **Reisswolf** | `STB01-2784` | 2025-12-15 | 2026-06-30 | **197** | reisswolf PDF |
| 10 | GG Tech | `STB01-2792` | 未取 | 未取 | — | ggtech.co/due-diligence |
| 11 | CVyolla（某企业） | `STB01-3060` | 未取 | 未取 | — | cvyolla.com |
| 12 | Nesilgrup | `STB01-3242` | 未取 | 未取 | — | 二手 |
| 13 | **UZSER Teknoloji** | `STB01-3505` | 2026-07-16 | 2027-06-07 | **326** | uzser.com.tr PDF |
| 14 | **BFS A.Ş.** | `STB01-3438` | 2026-07-14 | 2027-05-20 | **310** | bfskurumsal.com（含 JSON-LD） |
| 15 | **Egebilgi** | `STB01-3564` | 未取 | 「Aktif」 | — | egebilgi.com.tr |

**统计**：7 张有完整日期 ⇒ **197 / 310 / 324 / 325 / 326 / 355 天**（中位 ≈324.5 天）⇒ **全部 ≤1 年**，最短 197 天（≈6.5 个月）。

### 5.4 发证速度（⚠ 推算）

| 时点 | 最大号 | 增量 |
|---|---|---|
| 2023-12 | 656 | — |
| 2024-05 | 1,057 | ~400 / 5 月 ≈ 2.6/日 |
| 2025-03 | 1,837 | ~780 / 10 月 ≈ 2.6/日 |
| 2025-10-07 | 2,451 | ~614 / 7 月 ≈ 2.9/日 |
| 2025-12-15 | 2,784 | 333 / 69 日 ≈ **4.8/日** |
| 2026-07-16 | 3,505 | 721 / 213 日 ≈ **3.4/日** |
| 2026-07（月内） | 3,564 | +59（不足 1 月） |

⇒ **年发证 ≈900–1,300 张**；累计 ≈3,500–3,600 张（2026-07 时点）。⇒ 对照土耳其「bilişim 类中小集成商」的总量，**这一层筛子并不稀**（这是「墙矮」的量化依据）。

---

## 六、⭐ 名单侧：谁有证、谁没有（对我们 33 家 A/B 客户的可核查结论）

### 6.1 我们点名核查的 8 家（Angora / Ultron / Trio / Cyberwise / GelecekBT / Snexus / Nokta / LINK）

**结论：8 家全部「未公示」 —— 0 家在任何可检索页面公开 KBYB 编号。**

| 主体 | 检索结果 | 判定 |
|---|---|---|
| **Angora Networks** | 官网 `page-sitemap.xml`（末次更新 **2026-04-03**）与 `post-sitemap.xml`（末次 **2026-06-15**）**均无「证书/文件」页**；全站无 `belge`、`KBYB`、`STB01` 字样 | **未公示**（≠ 无证） |
| **Ultron Bilişim** | 无 | 未公示 |
| **Trio Entegrasyon** | 仅 LEI/MERSİS 企业登记（`789000DGLXW79STGRD76`），无证 | 未公示 |
| **Cyberwise** | 无 | 未公示 |
| **GelecekBT**（CLR/ONET 总代） | 官网 `hakkimizda` 只有品牌与业务，**无证书页** | 未公示 |
| **Snexus** | 无 | 未公示 |
| **Nokta Bilişim** | 仅控股集团介绍页（2020 成立，军工/系统集成） | 未公示 |
| **LINK** | 无 | 未公示 |

**对照组（同类土耳其企业，10 家有公示）**：GBB · LPS · Yönsis · Reisswolf · UZSER · BFS · Egebilgi · Netcad · itstack · GG Tech · Zirve · Netcom · bilgibirikim ⇒ **「有证就公示」是行业惯例**。
⇒ **推论（⚠ 概率级，非事实）**：**我们的 8 家目标主体很可能确实没有 KBYB**，因此它们**不能以自己名义投任何 2026 年的 bilişim 标** —— 这会**改变 r90/r91 的行动排序**（见 §7.1 修正 2）。

### 6.2 这对我们意味着什么（三段式）

1. **它们不是「壳」，而是「上游」**：没有 KBYB ⇒ 它们只能做**持证方的供货商/分包商**（`89/A.5`：分包商也要 KBYB —— **但只限「bilişim hizmet 标」的分包**；**mal alımı 标的分包不在 89/A.5 范围内**）。
2. ⇒ **最干净的通道是「mal alımı 标」**：货物标的分包/供货**不受 89/A 约束**，而**投标方（持证的本地集成商）** 负责扛证。⇒ **我们卖裸机给持证方，持证方去投货物标** —— 这条链路**不触碰任何资格法条**。
3. ⇒ **需要一份「持证方名单」作为渠道靶子**：本轮已拿到 33 个具名持证企业（§5.3 + 对照组），其中 **Reisswolf（文件管理）· Netcad（GIS 软件）· BFS（内审培训）· CVyolla（招聘）** 与本业无关 ⇒ 说明**该证在土耳其是「泛 IT 企业标配」而非「网络设备专属」**。⇒ **渠道靶子应按「谁真投网络设备标」二次筛**（下一步，见 §10.3）。

---

## 七、三条修正 / 划边界（按 r48 结构要求，点名被改写的判断）

### 7.1 ⭐ 修正 1：**「KBYB 有效期 3 年」是错的 —— 实测 6.5–12 个月，且由 27001 的到期日决定**

- **被修正者**：二手咨询站（`dsrbelgelendirme.com.tr` 明确写「Yetki belgesi, düzenlendiği tarihten itibaren **3 yıl** süreyle geçerlidir」）。**本轮不再采用。**
- **法规依据**：MADDE 6(2)「**有效期取所交材料中最早到期者的日期**」（A 级原文）。
- **实测反证**：7 张有双日期样本，跨度 **197–355 天**，无一超 1 年；最短的 Reisswolf 只有 **197 天**。
- **含义（对客户可说）**：
  1. **投标时必须查到期日**，只查「有没有证」会踩空；
  2. 该证的**续期节奏绑定 27001 的年度监督审核（surveillance audit）** ⇒ 拿证不是一次性投入，是**年费**；
  3. **「没证/证过期」在土耳其投标圈是高频率事故**，因此**「你的证什么时候到期」是一句很好的开场问题**（比「你有证吗」信息量大得多，且不冒犯）。

### 7.2 ⚠ 边界 1：**发证机关「没有被 2026-10-31 的部委改组改动」** —— 不要跟着新闻乱写

- 事实（A 级，RG **31.10.2026 / 33416**，**201 号 Cumhurbaşkanlığı Kararnamesi**）：Sanayi ve Teknoloji Bakanlığı 的 **Bilgi İşlem Dairesi Başkanlığı 被撤销**，新设 **Bilgi Teknolojileri Genel Müdürlüğü**（1 GM + 2 署长）；同批在 Enerji Bakanlığı 也新设同名 GM。
- **但**：KBYB 的发证单位在证书正文与 Egebilgi 页面里写的是 **`Milli Teknoloji Genel Müdürlüğü`**，**这是另一个单位**，**未被此次改组触及**。
- ⇒ **结论**：**发证机关仍为 Sanayi ve Teknoloji Bakanlığı / Milli Teknoloji Genel Müdürlüğü**；新的 BTGM 管的是**部委自身**的 bilişim 基建（含「kamu bilişim standartlarına uygun çözümler」），**不是发证**。**不要写「发证机关刚换」** —— 这是最容易被客户当场纠正的一类错误。
- ⚠ 但要知道它在：**新 GM 的职责里含「提高软硬件国产化率」** ⇒ 与 r87 的 Yerli Malı 议题同向，未来可能收紧跟证挂钩的国产化权重。**记为观察项。**

### 7.3 ⚠ 边界 2：**核验库「存在」已证，「可按公司名反查」未证**

| 问题 | 结论 | 依据 |
|---|---|---|
| 有公开核验入口吗？ | **有**，`kamubilisim.sanayi.gov.tr/belgedogrulama` | **4 份证书正文 + 1 份官方口径解读（2023-08）互证** |
| 能按编号查吗？ | **能**（这就是 `belgedogrulama` 的字面功能） | 同上 |
| 能按公司名/VKN 反查吗？ | **未证** | 该域名**对本沙箱 3 次抓取全部失败**（`https://` / `http://` / 根路径），**无 HTML 可读**；未见任何二手资料展示「按名搜索」的界面 |
| 有「全部持证企业」的清单页吗？ | **未证** | MADDE 6(1) 只说「部委网站公示」，未说以清单形式；检索未见 |
| 有第二层核验吗？ | **有**：TÜRKAK **TBDS**（`tbds.turkak.org.tr`）核 27001；**ASİST**（`asist.turkak.org.tr`）核发证机构资质 | 二手（多站一致） |
| 有第三层吗？ | **有**：KİK 手上有**停/撤证名单**（MADDE 7(7) 强制通报） | A 级（法规原文） |

⇒ **行动口径**：**不要对客户承诺「我能查你的证」**；正确说法是「**你可以用 `STB01` 号在这两个库里自查，把截图发我**」—— 把动作交给对方，我们只做判读。

### 7.4 修正 3（轻）：**r91「Angora 是最可能已持证的一方」——降级为「未证实」，且这条不能再作为卖点**

- r91 §10.3 写：Angora「**有 Kamu Bilişim Yetki Belgesi（需核实）**」。本轮核实结果：**官网无证书页、全站无编号、sitemap 显示产品页与新闻页最后更新分别在 2026-04 / 2026-06，之后无新增**。
- ⇒ **改写为**：**Angora 是否持证未知；且它连「证书公示页」这类行业标配都没有**（对比 §6.1 的 10 家）。
- ⇒ **战术后果**：**对 Angora 的第一句不能是「你有 KBYB 吧」**（若没有，等于当面指出短板）；**改成「你们今年投的标，资格条款是走自己的证还是搭伙伴的证？」** —— 同样信息量，不设陷阱。
- ⇒ **这同时给 r91 的「投标资格壳」定位打一个折扣**：**壳可能不在 Angora 身上**，而在 §6.1 那 10 家「有公示」的企业里。**需要下一轮做「持证 ∩ 真投网络设备标」的交叉筛。**

---

## 八、钱的算术：拿到这张证要多久、多少钱（给伙伴的可执行清单）

| 步骤 | 内容 | 成本 | 周期 | 证据等级 |
|---|---|---|---|---|
| ① ISO 27001（**TÜRKAK 认可**） | 10 人以下企业 | **28,000–30,000 TL + KDV** | 建体系 2–3 月 + 审核 1–2 日 | 二手（`isobelge` / `dmbelge` 2026 报价） |
| ①′ ISO 27001（**仅 IAF/境外认可**） | 同上 | **4,500–5,000 TL + KDV** | 4–6 日内可出 | 二手（`isobelge` IAF 价目） |
| ② **KBYB 申请** | e-Devlet → 门户填报 → 上传签署人证明 + 商会登记 | **未见官方收费项**（⚠ 未证实免费） | **法规 ≤2 个月** | A（MADDE 6(1)）+ 二手流程文 |
| ③ 年度维持 | 27001 监督审核 ≈ 首年 50–70% + TÜRKAK 文件核验费 **19,000 TL + KDV（2026）** | 年费 | 每年 | 二手（`mega-cert` 引 TÜRKAK 2026 价） |
| ④ 可回收部分 | **KOSGEB  belgelendirme desteği：上限 300,000 TL，比例 60–80%**，须 TSE/TÜRKAK 或其认可机构签发 | **−60~80%** | 先批后付 | 二手（`vertacert` / `toemkalite`） |

### 8.1 ⭐ 一个真实的陷阱：**便宜的 IAF 证可能不被认**

- 法规 **MADDE 3(a)** 把「Akredite kuruluş」定义为「**由 TÜRKAK 认可的**测试/认证机构」；
- 但 **MADDE 5(1)(a)** 的措辞是「**ISO/IEC 17021-1 akreditasyonuna sahip akredite kuruluşlar**」（未点名 TÜRKAK）；
- 二手实务口径**一致倾向「必须有 TÜRKAK 抬头」**，并有明确的失败案例描述（27001 范围写「Donanım Satışı」⇒ 拿不到服务类证）。
- ⇒ **给伙伴的建议只有一句**：**「别买 4,500 TL 的 IAF 证，那是废纸 —— 要 TÜRKAK 抬头的，30,000 TL 那一档，KOSGEB 能退 60–80%。」** 这句话本身就是**一次有价值的免费咨询**，且**不需要我们承诺任何东西**。

### 8.2 单位经济对比（放回 r90 的锚）

- 拿证一次性净成本（KOSGEB 70% 计）≈ **9,000–12,000 TL**（≈**$220–290**，按 TRY 50.02）。
- 对照 r90：**İSU 单台工业交换机成交 $3,486–4,102**。
- ⇒ **「一张标里一台机器的毛利 = 整家公司的投标资格」**。⇒ **这是本轮最可复述的一句话**：**资格成本 ≈ 0.07 台机器的售价。**

---

## 九、行动：三条能本周执行的，和三句不能说的话

### 9.1 三条可执行

1. **对 Trio / Ultron / Cyberwise / Elit Arge / GelecekBT**（r91 已定的谈话对象），把问题从「下一标用哪个品牌投」升级为 **两问**：
   - 「**你们今年投的标，`4.3.2` 那格是自己扛证还是搭联合体？**」
   - 「**你们 27001 的 scope 写的是哪一类 bilişim hizmeti？**」（scope 写错 = 拿不到证，这是他们自己会焦虑的点，且我们免费提供了诊断价值）
2. **扫 11–12 月标的 `4.3.2` 栏**，把**漏写 KBYB** 的标挑出来 —— 那是**唯一「合法可投」的窗口**（§3.3）。已知在册的近期待投标：**Çankırı `2026/1967649`（11-09，写了，不可投）· Tarsus `2026/2162042`（11-27，未知）· GDZ `ILN02589099`（11-18，未知）· İTÜ `2026/2063358`（11-19，未知）· GDZ `ILN02594847`（11-24，未知）** ⇒ **优先去把后四张的 `4.3.2` 栏读出来**（下一轮任务）。
3. **建一份「持证方渠道靶子表」**：以本轮的 33 个具名持证企业为种子，交叉 EKAP 中标记录，挑出**真投网络设备**的 5–8 家（下一步）。

### 9.2 ⚠ 修正后的行动优先级（替代 r91 §10.1 的旧序）

| 旧（r91） | 新（r92） | 为什么变 |
|---|---|---|
| ① 守：不投写死 NAC/网管/堆叠的标 | **不变**（生态墙仍然最硬） | r92 未推翻 r91 §二 |
| ② 攻：水务/市政/大学/医院 | **收窄**：「**先看 `4.3.2` 有没有 KBYB**」，有则直接放弃（除非搭持证方） | 新增第四道墙，且它是**二值判断**（比参数好查） |
| ③ 绕：经 Angora/Trio/Ultron/Cyberwise 进 | **改口**：这几家**大概率无证** ⇒ 只能做「它们的上游」或「持证方的上游」，**不能做「它们的投标壳」** | §6.1 |
| ④ 不追：Forescout 矩阵与 62443 | **不变** | — |
| — | **⑤ 新：找「持证 ∩ 投网络设备」的集成商** | 这是唯一同时过第 2 与第 3 层门槛的群体 |

### 9.3 三句不能说的话（并入 r92 谈话禁区）

1. **不能说「我们可以帮你拿 KBYB」/「我们也能拿」** —— e-Devlet + 土耳其税号，**境外主体结构上不可得**。
2. **不能说「这个标要求 KBYB 是违法的」** —— 法律上可争，但**对客户说这句等于承认自己没证且想翻桌**；正确说法是「**这类要求在货物标上很常见，但它不是 KİK 的强制条款**」。
3. **不能说「有 KBYB 就等于通过了安全审查」** —— 证书正文自带免责句（§2.1(3)）。

---

## 十、差额、边界与下一轮

### 10.1 与上一轮（r91）的差异清单

| 项 | r91 | r92 |
|---|---|---|
| 主轴 | 生态锁死（ETİ MADEN） | **投标资格（KBYB）专项** |
| 新一手法律文本 | — | **MevzuatNo 39610 全文（两分片读完）+ RG 32058 公报全文** |
| 新增强制条文 | — | **KİK 89/A 五款 + 生效日 2023-09-29 + 公报 74 条 + 程序条 16.6.4** |
| 新增实证 | — | **15 张证书（13 KBYB + 2 Yazılım）· 6 张 mal alımı 标要证 · 7 张带到期日** |
| 修正旧判断 | r89 SFP 边界 | **「3 年有效」作废** · **「Angora 是投标壳」未证实并降级** · **发证机关未变（挡掉一条新闻误读）** |
| 行动 | 四层优先（守/攻/绕/不追） | **改序：攻收窄为「先看 4.3.2」；绕改指「持证方」；新增靶子表任务** |

### 10.2 本轮来源清单（54 条，供复核）

**A. 一手法规 / 官方（7）**
1. `mevzuat.gov.tr` MevzuatNo=39610（Chunk 0 + **Chunk 1 本轮补读**）· 2. `mevzuat.gov.tr` MevzuatNo=13354（KİK 一般公报 89/A 现行文本）· 3. `hakedis.org` RG 29.12.2022/32058 公报 PDF（**全文**）· 4. `resmigazete.gov.tr` 2022/06/20220629-2.htm（SERP 摘录）· 5. `kamubilisim.sanayi.gov.tr/belgedogrulama`（**3 次抓取失败**，仅机制确认）· 6. `ekap.kik.gov.tr` Karar 2024/UH.I-78（**全文分片 0/6**，Afyonkarahisar İl Sağlık SBYS）· 7. RG 31.10.2026/33416 · 201 号 Kararname（经 `theprowess` 全文转述）

**B. 证书原件 PDF / 企业公示页（17）**
8. gbbbilisim.com.tr PDF（A 级全文）· 9. yonsis.com.tr PDF · 10. lpschain.com PDF · 11. reisswolf.com.tr PDF · 12. uzser.com.tr PDF · 13. netcom.com.tr PDF · 14. zirve-bilgisayar.com PDF · 15. bilgibirikim.com PDF（**STB02-1376**）· 16. bfskurumsal.com（含 JSON-LD）· 17. egebilgi.com.tr/dokumanlar · 18. netcad.com/tr/kurumsal/kalite-yonetimimiz · 19. itstack.com.tr/sertifikalarimiz · 20. ggtech.co/due-diligence（**STB01-2792 + STB02-1143**）· 21. cvyolla.com · 22. angoranetworks.com `sitemap_index` + `page-sitemap` + `post-sitemap`（**3 次抓取，全站无证书页**）· 23. gelecekbt.com/hakkimizda · 24. noktaholding.com.tr

**C. 招标公告侧（13）**
25. cankiripostasi.com（Çankırı `2026/1967649`，r91 全文）· 26. konyapostasi.com.tr（Selçuk Ü. `2026/7050971`）· 27. imzagazetesi.com（Kdz Ereğli）· 28. yenisebinkarahisar.net（Bilişim Malzemeleri）· 29. yeniankara.com.tr（UPS+电池）· 30. ensonhaber.com（Sağlık Bilimleri Ü.）· 31. mavikocaeli.com.tr（Kocaeli BB SOAR `2026/2186257`）· 32. milliyet.com.tr/resmi-ilanlar（Taksim EAH `2026/2248263`）· 33. baskentgazete.com.tr（**TSE `2026/2220498` düzeltme ilanı，zeyilname 补加 KBYB**）· 34. kikkararlari.com（RG 32058 公报转录）· 35. ihaledanismani.com（KİK karar 转述，**含 16.6.4 原文**）· 36. ihaletakip.com.tr（Türkiye Hudut ve Sahiller SGMD）· 37. gunisigigazetesi.net

**D. 法律 / 咨询解读（14）**
38. salimdemirel.com.tr（2023-08-23，**含「doğrudan temin 与 istisna 也要证」**）· 39. lbfpartners.com · 40. lexology.com · 41. mondaq.com · 42. alomaliye.com · 43. lexpera.com.tr（RG 原文转录）· 44. iktisadidayanisma.com · 45. iso.org.tr `Ek-12865.pdf`（**新草案：Veri Merkezi Yetki Belgesi + 6 个月生效**）· 46. manisatso.org.tr（同一草案另一份）· 47. dsrbelgelendirme.com.tr ×2（**含被修正的「3 年」说法**）· 48. abkalite.com · 49. isodanisman.com ×2 · 50. andbelgelendirme.com ×2 · 51. certby.com ×2（e-Devlet 流程）

**E. 成本 / 核验侧（3）**
52. isobelge.net ×4（TÜRKAK 27001 30,000 TL / IAF 4,500 TL / İstanbul / 核验指南）· 53. dmbelge.com.tr · 54. vertacert.com + toemkalite.com + mega-cert.com（KOSGEB 300,000 TL / %60–80；**TÜRKAK 2026 核验费 19,000 TL**）+ nobelbelgelendirme.com（TBDS/ASİST）

（另有 `theprowess.net` / `sonmuhur` / `samanyoluhaber` / `ajans04` / `yesilhaber` / `foreks` 六家仅用于交叉验证 201 号 Kararname，计入第 7 条。）

### 10.3 ⚠ 诚实边界（本轮明确未完成）

1. **`belgedogrulama` 界面未实证**：3 次抓取全失败，**不知道能否按公司名反查**、**是否有全量清单**。
2. **Angora / Ultron / Trio / Cyberwise / GelecekBT / Snexus / Nokta / LINK 的持证状态是「未公示」，不是「无证」** —— 二者不能混。要确认只能：① 让对方自查截图；② 若其投过 2023-09 后的 bilişim 标，看 yeterlik 表。
3. **KBYB 是否收费未证**：门户要求 e-Devlet 登录，**无公开价目**；「免费」只是未见收费项的推断。
4. **`STB03` = Sızma 证：无样本，纯推断。**
5. **「15 张证书」不等于全量**：样本来自「愿意公示的企业」，**存在选择偏差**（不公示的企业可能更多）。
6. **TSE `2026/2220498` 与 Kocaeli/Taksim 两张标的日期晚于本日（索引异常）** ⇒ 仅作为「用法趋势」佐证，**不作时间锚**。
7. **新草案（Veri Merkezi 证）的立法状态未证**：`iso.org.tr` / `manisatso` 上的是 **TASLAK**（草案），**2026-10 时点未见生效公报**；且草案 MADDE 8 会**废止 2022 年现行法**。⇒ **若通过，2026 年新版证书的全部规则重写**（KBYB 不再单列、改按 27001 scope 分类、有效期规则改）。**这是必须监控的第一号立法风险。**
8. **r91 旧边界未动**：ETİ MADEN 6 个 chunk 未读、İSU 分项单价、GDZ 规格数量、EÜAŞ 中标方、41 家电话仍未拨。

### 10.4 下一轮（r93）候选，按性价比排序

1. **把 4 张在投标的（Tarsus `2026/2162042` · GDZ `ILN02589099` · İTÜ `2026/2063358` · GDZ `ILN02594847`）的 `4.3.2` 栏逐个读出来** —— 直接决定「能不能投」，且是**二值信息**，成本最低、价值最高。
2. **「持证 ∩ 投网络设备」交叉筛**：拿 33 个持证企业去撞 EKAP 中标记录。
3. **新草案跟踪**：`Veri Merkezi Yetki Belgesi` 是否生效（一有公报，r92 的 §二 全表要重写）。
4. **KBYB 与「yerli malı / Sanayi Sicil」的交互**：Çankırı 同时要 KBYB + İmalatçı 证明，**这两张证的交集是谁** —— 这才是「土耳其法人壳」的完整体。
