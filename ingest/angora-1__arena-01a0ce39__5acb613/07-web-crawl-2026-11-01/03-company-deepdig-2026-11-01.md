# r43 · 土耳其 21 家客户「商业深挖」抓取台账（2026-11-01）

**这一轮是什么**：用户要求「各个角度深挖：**年报 / 领英 / KP / 人事变动 / 参展 / 论坛 / GitHub 等，只要商业角度都搞一下**」，并把结果写进 MD。

- **抓取时间**：全部为 **2026-11-01（Asia/Shanghai）**，单次会话内完成。
- **抓取方式**：bash 无外网 → 全部经 `fetch_page` / `web_search`；**原始 HTML 未落盘，本文件为唯一存证**。
- **写入位置**：`08-followup-dossiers-2026-11-01/` 下 **21 份 MD 各追加一节 `## 商业深挖 2026-11-01`**（原有八段 + r42 的核验补录全部保留）。
- **覆盖**：**21 / 21**。其中 **15 家挖到了新的商业事实**，**6 家公开面为零**（如实标注，不编造）。

---

## 一、角度 × 结果总表

| 角度 | 有效命中 | 说明 |
|---|---|---|
| **领英企业页**（人数/成立/关注者/行业分类） | **11 家** | Longline 3,979 / Okisan 5,318 / Telemobil 1,402 / Optima 2,987 / Han 746 / CCTV Depo 239 … |
| **KP（关键人姓名+职务+任职年限）** | **10 家** | 最能改变打法的是 Longline 的 **Safa Özer（Purchase Manager）**、Okisan 的 **Okan Özkara**、Karer 的 **Nurbaki Karataş（CEO/owner）** |
| **年报 / 财报** | **0 家（直接年报）** | 土耳其私营有限公司**不公开年报**；只能拿到第三方估算（Datanyze/RocketReach/ZoomInfo），**已全部标注"第三方推算，非财报"** |
| **营收第三方估算** | **3 家** | Longline ≈$10.7M（Datanyze）/≈$15M（RocketReach）；Telemobil ≈$25.6M；Okisan $8.6M（旧档） |
| **海关提单（Volza 类）** | **2 家** | ⭐ **Öncü：128 批、2 家供应商、供应商 `SEC ON CO LTD`**；**Longline/Entegron：土耳其进口方从 `ENTEGRON TECHNOLOGY FZE` 进货** |
| **参展 / 展会足迹** | **5 家** | ⭐ **Optima：连续 20 年 Intersec 迪拜 + Messe Frankfurt 奖 + Intertraffic Amsterdam 2026 首秀**；Okisan：ISAF 2026；Han：ISAF 2018/2019/2019 Ankara |
| **人事变动 / 招聘信号** | **2 家** | Longline 2022 招 Kurumsal Saha Sorumlusu；CCTV Depo 领英发过销售/市场招聘 |
| **GitHub / 开源** | **0 家** | 21 家全部无开源活动（白牌固件，无开源策略）—— **这是"确认无"，不是"没查"** |
| **论坛 / 技术社区** | **0 家** | 同上 |
| **行业协会会员** | **2 家** | ⭐ **Karer：PESİAD 会员**（1,000 m²、2006 成立、0216 397 33 88）；Okisan：SAHA İstanbul（旧档） |
| **政府/招标平台（EKAP）** | **未接入** | 本轮未做，列为下轮方法 |
| **品牌/域名资产** | **6 家** | Longline 五站（longlinestore/longlinesfp/longlifesfp/longlinenetwork/endustriyeltestcihazlari）、Han（milesight.com.tr + IG）、GelecekBT 四站、Novacom 双域 |

---

## 二、逐家结果

| # | 客户 | 挖到的核心新事实 | 等级 |
|---|---|---|---|
| 01 | Telkolink/GelecekBT | ⭐⭐ **CLR Networks 总部在深圳宝安（+86 755 33127842）**，其 **EMEA 联系人 = Yusuf Ölçer（Skype yusufolcer）= GelecekBT 总经理**；主体 **Gelecek Yönetim Merkezi … İth. İhr. Ltd. Şti.**；2004-10-13 成立；代理 **3onedata / TG-NET / Fibridge / Repotec / IMC / CLR / ONET**；两个 Perpa 门牌（Telkolink A K:5 No:295-297；GelecekBT A K:13 No:1990） | 强 |
| 02 | NOVA/Novacom | 品牌 **Novacom（NVC-）**，三域（nova-grup.com / novacom.com.tr / 第三方 pekgross.com）；⭐ **24V 楼宇对讲 PoE** 两款 `NVC-INTSF0420FB2L`（4+2）/`NVC-INTSF0820FB2L`（8+2）；PoE 延长器 `NVC-EBT14GW-A`/`NVC-AT13F-A`；测试仪 `NVC-MFOV58`(SKU 10594)/`MFV56`/`LT300S` | 强 |
| 03 | Snexus | 成立 **2020**、11–50 人、İstanbul **Çekmeköy**；⭐ **新加坡据点 Sim Lim Square（Rochor Canal Rd 02-67）**；具名分销商 **HEMMAH GROUP**；⚠ 名称污染（巴基斯坦外包公司、美国存储软件同名） | 强 |
| 04 | Cenova | 法定名 **CENOVA BİLİŞİM TEKNOLOJİLERİ İTH. İHR. VE TİC. LTD. ŞTİ.**；**2002 成立**；客户=市政/大学/军/医院/工厂；给经销商账期；人员 Abdurrahman Erkarslan、Necla Güler(会计) | 中 |
| 05 | CryptoLink | 站点自证六大业务（边境/网络/网安/LPR/在线培训/**信号干扰**）；法定名 **A.Ş. 与 Ltd. Şti. 自相矛盾**；是 `itmteknoloji.com.tr` 的解决方案伙伴；⚠ 与 CryptoLink Inc(US)、Cryptex 同名 | 中 |
| 06 | Longline/Entegron | ⭐ **Entegron Technology FZE = 阿联酋自贸区实体**（土耳其提单显示它作为出口方供货，含 SFP 模块）；Longline 五站点矩阵；**Romania/China/Dubai/USA** 合作、TR+RO 双仓、ATR/TAREKS/GTIP；800+ 伙伴；**采购经理 Safa Özer**、董事 Ercan Çiçekci；全系**仅 1 年保修** | 强 |
| 07 | Sami CEUIK | 公开面 0；⚠ **`CEUIK` 疑为 `ÇEVİK` 的录入变体** → 需名片校正；维持订单级优先级 | 空 |
| 08 | Selim Kalaka | 六个角度全空；固化结论：**窗口信息只存在于展会对话，外部无法证实也无法推翻** | 空 |
| 09 | Okisan | **48–49 人 / 5,318 关注 / 行业分类=进出口 / 1993(领英) vs 1986(官网) vs 2004(A.Ş.) 三日期**；⭐ **Okan Özkara（Business Development Director，2010–）**、**Kerem Öztürk（Ankara 区域经理，2001–，24 年）**、Ekrem Özkara(CEO) | 强 |
| 10 | Optima | ⭐⭐ **9,000 m² 厂（2014 补助购地、2015 夏建成）、NACE 28.99.90、ISO 9001:2008、出口 >90% 到 50+ 国**；`areaServed` 16 国；**连续 20 年 Intersec 迪拜 + Messe Frankfurt 奖**、**Intertraffic Amsterdam 2026 首秀**、OKSİAD 2025；新实体线索 **Ulgen**（待核关系） | 强 |
| 11 | Karer | **PESİAD 会员**；法定名 **Karer Güvenlik Sistemleri Sanayi ve Ticaret Ltd. Şti.**；**2006 成立 / 1,000 m²**；新座机 **0216 397 33 88**；Nurbaki Karataş（CEO/owner，Akdeniz Üniv.）、Ebru Tekin（会计 2021–）、Neslihan Entrk（销售） | 强 |
| 12 | Telemobil | 法定名 **Telemobil Bilgi İletişim Hizmetleri San. ve Tic. A.Ş.**；**90 年代为 A.B GRUP 的 IT 部门 → 2005 独立 A.Ş.**；Üsküdar Küçükçamlıca；**97–120 人**；第三方估营收 **≈$25.6M**；业务=IT 集成+**电气承包**+楼宇自动化/弱电；客户 教育/医疗/建筑/数据中心；KP Murat Gül、Mehmet Emre Güney | 强 |
| 13 | ONSIS | 公开面 0（仅知 0232=İzmir） | 空 |
| 14 | Makros | ⚠ **名字撞车**：`makrosinsaat.com`（建筑）、`macromuhendislik.com`（弱电工程，2013）、Makro İnşaat 均非本案；**r41 的"Makros A.Ş."在公开网络无对应实体** → 先核主体 | 空 |
| 15 | HAFYA | 公开面 0（军项目集成商本就低调）→ 直接 WhatsApp 给 Emre Makili + 防水规格书 | 空 |
| 16 | CCTV Depo | ⭐ **CEO Can Gurcan 领英自述"中国，尤其深圳，我非常熟悉"**；成立 2004、51–200 人、**HQ Bahçelievler（非 Şişli-Perpa，更正）**；SECUZI 品牌；Mehmet Furkan Beklin；WHOIS 2004-07-21 持有人 Can Gürcan；领英仅 239 关注 | 强 |
| 17 | Filiz Güvenlik | ⭐ **护城河=内政部许可的 7/24 报警监控中心**（订阅制）；官网有 **"Çözüm Ortaklığı"（合作伙伴）表单** = 现成正式入口；**A.Ş. vs Ltd. Şti. 冲突**；Mavili Yangın 授权服务；社媒 FB/YT/领英(个人页形式) | 中 |
| 18 | Han Elektronik | ⭐ **18+ 品牌矩阵**（Milesight 土唯一授权+2023 最有价值伙伴奖、FOREDGE、VIDEOPARK、SPY 全系、GRUNDIG、PANASONIC、AXXON、AVER*、SHELLY、ALIENFENCE、**Rujie/Reyee**）；⭐ **官网菜单里直接有 "OEM" 分类**；2000 成立、51–200 人；444 1 426；运营 milesight.com.tr | 强 |
| 19 | Öncü Güvenlik | ⭐⭐ **集团六实体**（ISSD / Neotech / Oncu Security / Sec-on / Secube）；Öncü **2002** 成立、Sec-on **2012(公司列表) vs 2016(时间线)**；代理 **HIKVISION/COFEM/DAVANTIS**；**Volza 提单：128 批 / 2 家供应商 / China / HSN 8525·8521·8531 / 供应商 `SEC ON CO LTD` + Tamron Europe / 录像机 150 UNT** | 强 |
| 20 | OPAX | 法定名**逐字核实**（Opax Mühendislik … İthalat İhracat Dış Ticaret Pazarlama Ltd. Şti.）；**Gmail 之外新增 `sezer@opax.com`**（Google Play 开发者）；App **OPAX Pro**（com.opax.opaxalarmpro）；Damian Brozda **仍无法定论** | 中 |
| 21 | bilimsat/KILIÇ | 公开面 0；⚠ **纠正 r41**："Gmail = 个人经营"不成立，只能当"IT 成熟度低" | 空 |

---

## 三、两个可复用的方法论（这是本轮真正的资产）

### 3.1 海关提单反查（B/L 数据）——本轮最大突破

**做法**：用主体**法定全名**（不是品牌名）在公开提单库（Volza / ImportGenius / Panjiva / TradeAtlas）检索，可得到：

- **供应商名称**（→ 客户现在到底从谁进货）
- **批次数量**（→ 采购频次与规模量级）
- **HS 编码**（→ 品类结构）
- **单票数量**（→ 单次订多少台）

**本轮实证**：Öncü 的 `SEC ON CO LTD` + 128 批；Longline/Entegron 侧的 `ENTEGRON TECHNOLOGY FZE`。

**注意三条边界**：
1. **只覆盖有报关记录的部分**，不等于全量采购；
2. **时间范围需逐条确认**（免费页面通常只给"历史数据"）；
3. **话术风险**：**绝不能在邮件里说"我们知道你们的供应商是谁"**——等于告诉对方你在查底。要用「你们现在是整机进口，对吧？」这种**让他自己确认**的方式。

### 3.2 行业协会会员名录 —— 中小企业的"官方履历"

**做法**：土耳其行业协会名录（**PESİAD** 安防、**SAHA İstanbul** 国防、**TÜBİSAD** 信息）常登记：**法定全名、成立年、面积、电话、联系人**，比官网更硬。

**本轮实证**：通过 **PESİAD** 一次性拿到 Karer 的法定名 + 2006 成立 + **1,000 m²** + 新座机 0216 397 33 88。

**推论**：Han Elektronik、Öncü、CCTV Depo 大概率也在 PESİAD 名录内（**下轮优先查**）。

### 3.3 市场盘子（用于报价与预期管理）

Volza 品类口径（2026-10 页面）：
- **土耳其从中国进口「Ethernet Switch」：4,061 批次 / 509 家买家**；
- **土耳其「Ethernet Switch」总进口：2,940 批次**；
- 全球从中国进口的「Access Switch」中，**土耳其占 13%（599 批次）**，排第 3。

→ **含义**：土耳其是一个**年批次量数千、买家数百**的成熟市场，**不是空白市场**。所以我方的胜负手在**"替换存量供应商"**，不在"开荒"。

---

## 四、没做到的部分（诚实清单）

1. **年报/财报：0 家**。土耳其私营 Ltd./A.Ş. 不公开年报；所有"营收"数字均为第三方推算，已在档案内逐条标注。
2. **GitHub/论坛：0 家**。这是**确认无**（白牌固件生态），不是遗漏。
3. **政府招标（EKAP）未接入**：`ekap.kik.gov.tr` 未在本轮测试。若接入，可直接拿到 CryptoLink / HAFYA / Telemobil / Sami 的**中标项目与金额**（下轮方法候选）。
4. **6 家公开面为零**（07/08/13/14/15/21）——其中 14 Makros 是**名字撞车导致无法定位**，其余是**对象类型决定**（个人 / 军项目 / 无营销）。
5. **`optimasecurityonline.com` 仍 500**（r42 已记），美国同名公司无法深挖，也不需要。
6. **未做的角度**：员工离职率（无公开数据源）、专利/商标（TÜRKPATENT 需交互查询）、股权结构（需 Ticaret Sicil Gazetesi 付费查询）。

---

## 五、下轮建议（按性价比排序）

1. **PESİAD / SAHA İstanbul 名录批量反查**（Han、Öncü、CCTV Depo、Filiz、CryptoLink）—— 一次拿全法定名+电话+联系人。
2. **EKAP 招标记录**（CryptoLink / HAFYA / Telemobil / Sami / Okisan）—— 直接给项目与金额。
3. **公开提单库按法定全名反查**（Cenova / Karer / Novacom / Han / Longline）—— 拿供应商与批次。
4. **Ticaret Sicil Gazetesi**（付费）—— 股权与注册资本，用于判断信用与谈判层级。
5. **各公司官网的 `/kurumsal`（关于我们）与 `/bayilik`（经销申请）页**—— 土耳其站几乎都有，且常含成立年与团队照片。
