> **r96 补充与修正**：已找到公报的两张内嵌 JP2，但转码后仍不可读，**不是完整 PDF 页的可视核验**；Hakan 主体未确认的结论不变。MAC 登记、六单成本、4th-pre 与 6th 的金额/物流记录经新复核，以 [r96 总报告](165-angora-order-mac-document-reconciliation-2026-10-26.md)和[逐字段映射](../09-orders/120-angora-orders-master-2026-10-21.mapping-r96.md)为准。会话给出的日期与沙箱时钟不一致，实际采集日待核；用户没有另设历史截止日，实时页面不能伪装成过去快照。

# r95 · Angora 深挖与纠错：工商公报跨栏、既有供应链、英国关联公司的股权及财务

- **日期口径（r96 修正）**：会话给出的当前日期为 2026-10-26（UTC），不是用户另设的业务截止日；运行 `date -u` 显示 2026-11-19，实际采集日需独立核实。不能把实时网页当作 10-26 当天的历史快照；凡能独立确认的旧公告、旧财报和合同以文书日期标注，其余仅记为「本轮页面所见」。
- **范围**：承接 r94 的「成立以来商业信息」，回读仓库内订单、公报 OCR 和历史研究，再用第三方贸易页面、2022 峰会原声及英国官方申报交叉核验。**本轮不联系任何人、不索取账号、不新增采购或发送邮件。**
- **来源落盘**：11 个 URL 的完整可见文本抽取，逐 URL 分文件存于 `09-source-evidence-r95-2026-10-26/`；清单逐项列 URL、路径、字节数和哈希。**文本抽取不是 PDF 原件**；墙后和未取文本不能当作已读取。以前留存的来源不重新合并。
- **保密**：本档混有用户提供的商业会话与订单，应当作为内部工作底稿；不向 Angora 或第三方转发。未转抄护照、自然人身份证、私人住址或银行账号。

## 一、先修正上轮：我方不是「准备成为第 16 家」

**r94「我们要成为 Angora 第 16 家供应商」作废。** 仓库原有的 [`STSC20240508007.pdf` 文本抽取](../01-knowledge-base/pdfs/1st-order-sample-3-10g-24-48-stsc20240508007-pdf.md) 列出 **2024-05-08 的 proforma invoice**：买方 Angora Networks、卖方 Zhengzhou Saga Telecom，4 台样机、含运费总额 $1,265。它本身是形式发票，不单独证明实际付款或交付。原始商业通信归档 `../01-knowledge-base/gmail-threads/layer_3_managed_switch.md` 第 37–39 封，2024-05-21 双方已谈清关及首笔收款；`../09-orders/120-angora-orders-dossier-2026-10-21.md` 第 2–3 节记录首单付款和发货及后续订单。对用户，正确定位是 **已有交易关系，争取可持续复购和合规的第二供货来源**，不是陌生人开拓。

具体核对状态：

| 项 | 可用事实 | 不得推成 |
|---|---|---|
| 2024-05 样品 | 有双方、型号、数量及价格的形式发票；存档邮件当日讨论清关；订单归档另记付款/发货 | 不能把形式发票本身当付款水单 |
| 2025-01 大单 | `120` 订单底账记 `STSC20250117007`、178 台（含 2 台备机）及后续发货；属我方内部历史单据 | 不把本单推成 Angora 全部市场销量 |
| 2025-07 TT 型号 | `120` 将 10 台 MAC/SN 分配列为记录，合同/发票未上传 | **MAC/SN 分配不等于已付款或交付** |
| 2026-10 的 88 台 | `wechat-conversation-aligned.md` 2026-10-08 与 `../09-orders/123-angora-88-dead-levent-tt-background-2026-10-21.md`：Levent 称伙伴因交期改用土耳其现货 | **不能继续写为在手订单或首批已成单** |

Volza 的 15 家是其数据库特定覆盖范围内的数字，**不是完整的全球供应商清单，也不能据此给我方编号**。r94 还把 45 票概括成「白牌硬件底座」「每天在进口」：应改成**第三方索引记录有进口迹象；其具体货品、供应商身份及活跃期须逐票核对**。

## 二、2024 土耳其工商公告：文件已存在，但跨栏不能乱认人

**修正 r94「Ticaret Sicil 没查到」**：仓库有用户提供的 `ANGORA TICARET SICIL 11 MART 2024 .pdf`，清单记原件 **39,879 bytes**，本地只有无文本层的[提取记录](../../../02-extracted/ANGORA%20TICARET%20SICIL%2011%20MART%202024%20.pdf.extracted.md)和[原有 OCR](../01-knowledge-base/pdfs/angora-ticaret-sicil-2024-03-11-ocr.md)；本轮没有读取到原始扫描图。2024-05-21 Levent 给 Simon 的存档邮件称附上的贸易登记公报用于回答银行的股东信息需求，**不等于该页一定包含完整股东名单**。

OCR 页头为 **11 MART 2024 / SAYI 11040 / SAYFA 930**。在同一页 OCR 中可读到 Angora 全称、安卡拉登记处、**MERSİS `0069052022000017`**、**Sicil/Dosya `401714`**、`Çamlıca … 20Z/1, Yenimahalle/Ankara`；该 MERSİS 的数字与已归档 VKN `0690520220` 相符，且官网联系页的生产地址同地区。**这是可核实的文书线索，不是经本轮目视核验的公报原件。**

### 2.1 必须纠错：Hakan Öztuna 不能再记为 Angora 董事长或资方

OCR 把多栏按照横向行顺序交错输出。其相邻文句同时出现 **Bursa 登记处 / `ITECH MÜHENDİSLİK … A.Ş.` / Bursa 28 公证 / Hakan Öztuna / 2027-03-07** 和 **Ankara 登记处 / Angora / Ankara 58 公证 / Levent Kılıç / 2027-03-09**。按文本的交错位置，**Hakan 的内容更像是旁栏 Bursa ITECH 的公告，而不是 Angora**；但没有原图坐标时，连此跨栏归属也应由扫描件复核，不能凭 OCR 行序作法律定论。

因此，`../06-competitors/96-angora-customer-fingerprints.md`、`../09-orders/121-angora-master-reanalysis-2026-10-21.md`、`../09-orders/122-angora-financials-internal-dynamics-2026-10-21.md` 中「**Hakan 是 Angora 董事长/单独代表/沉默资方、新资本进会**」**撤回，主体待确认**。不能由董事变更推断股权变动、融资人或资金来源。OCR 中 Levent、Mehmet Taylan Esen 与 Uğur Han Kurt 的职务表述看似属于 Angora 栏，但也须核对原图和完整公告；**董事职务终止 ≠ 不再任职 ≠ 不再持股**。

### 2.2 股东和资本到底知道多少？

- **Angora（土耳其 A.Ş.）**：股东名册、持股比例、注册资本及实缴额，本轮仍**未在可核实的 Angora 原文中确认**。公司称 100% 本土资本是 2023 年采访自述，**不是最新工商股东清单**。
- **英国 Connexite Ltd**：下面有清楚的英国申报，但这是**另一个法律主体**；四名同名自然人关联线索不能倒灌成 Angora 的股权表、营收、现金或债务。
- **解锁条件**：目视核对用户原 PDF 的版面；如需最新股权/资本，取得 Ankara 注册号 `401714` 的当前 **Ticaret Sicil / MERSİS** 公司摘录或让 Levent 提供最新 shareholders/capital statement。不要要求身份证号码。

## 三、英国 Connexite：不是「猜」，是英国登记申报；但不是 Angora 股权

[Companies House 官网](https://find-and-update.company-information.service.gov.uk/company/14770313) 显示 **CONNEXITE LTD**（英格兰及威尔士，company no. **14770313**）2023-03-30 设立。登记机关明确提醒其**不核实申报资料的真实性**。其姓名与 Angora 2022 渠道峰会团队匹配；`../09-orders/120-angora-orders-dossier-2026-10-21.md` 亦有 Connexite 商业计划线索。**同人关联强，不等于已证 Angora 持有 Connexite 或反之。**

### 3.1 分时点的股权，不可混成一张「当前表」

| 截止时点 | 官方原始申报 | 正确理解 |
|---|---|---|
| 2023-03-30 设立 | [NEWINC 设立文件](https://find-and-update.company-information.service.gov.uk/company/14770313/filing-history/MzM3NDUxMDIxOWFkaXF6a2N4/document?format=pdf&download=0)：100 股 ordinary，面值合计 £100，申报未缴 0；Mehmet Taylan Esen、Mehmet Yasin Koru、Levent Kilic、Ibrahim Balci 各 24 股，Cemal Arda Tekkesin 4 股 | **初始英国公司股份**；£100 为申报股本面值，不是 Angora 的注册资本或账户现金 |
| 2023-12-27 | [CS01](https://find-and-update.company-information.service.gov.uk/company/14770313/filing-history/MzQwNTY1NDQzMmFkaXF6a2N4/document?format=pdf&download=0)：上面前四人**各 25 股**；Tekkesin 在 2023-12-12 转出 4 股，期末 0 股 | **英国 Connexite 当期股东各 25%**，不得写成土耳其 Angora 股权 |
| 2024-12-27 / 2025-12-27 | 官方后续 CS01 标明 no updates；均未另附新的逐人持股表 | 可保留最新具名股东清单的申报时间，**不是对任意时点股权的实时担保** |
| PSC 自成立至本轮所见 | [设立文件](https://find-and-update.company-information.service.gov.uk/company/14770313/filing-history/MzM3NDUxMDIxOWFkaXF6a2N4/document?format=pdf&download=0)和 [PSC 页面](https://find-and-update.company-information.service.gov.uk/company/14770313/persons-with-significant-control) 登记 Taylan 对 Connexite **75% 或以上表决权**及任免多数董事权；PSC04 2026-04-10 变更个人资料，未在该表证明投票权形成方式 | **表决权 ≠ 持股比例**。同一设立文件又显示其 24/100 ordinary 股且写 full voting rights，存在需要解释的表面张力；可能有间接或协议控制，也可能申报需核实，**本轮不知道原因，不能自行定论** |

董事列表本轮所见 Taylan 为现任董事，另一位董事 Donald Isufi 的终止日 **2025-02-19**；详见[官方 officers](https://find-and-update.company-information.service.gov.uk/company/14770313/officers)和 filing history。网页的「active」是本轮访问显示，**不可回填为 2026-10-26 的实时历史状态**。

### 3.2 英国微型公司账目：有财报，但不披露营收或现金

[2025-03-31 micro-entity accounts](https://find-and-update.company-information.service.gov.uk/company/14770313/filing-history/MzQ5MzU5OTYwNWFkaXF6a2N4/document?format=pdf&download=0)，2025-12-11 批准、Taylan 签署，**免审计**；对照 [2024-03-31](https://find-and-update.company-information.service.gov.uk/company/14770313/filing-history/MzQyNzc4MTAzM2FkaXF6a2N4/document?format=pdf&download=0)：

| 指标 | 截至 2024-03-31 | 截至 2025-03-31 | 边界 |
|---|---:|---:|---|
| 流动资产 | £100 | £100 | **不等于现金**；账目没有现金细分 |
| 一年内到期债权人款项 | £389 | £749 | 负债科目，不证明银行欠款或违约 |
| 净资产 / 净负债 | **−£289** | **−£649** | 仅 Connexite 个体，非 Angora 合并报表 |
| 平均员工数 | 1 | 1 | 两期申报值，不是 Angora 员工数 |

**未披露营业收入、利润表、客户、银行余额、关联往来或现金流。**不能由负净资产直接判定失信、破产、停业、或 Angora「没钱」；2026-03-31 及以后的财报未在本轮拿到。2025 报表已经列出 2024 对比，但为遵守逐源独立原则仍保留两份独立抽取，不合并。

## 四、供应链：找回旧结论，但把「已证明」和「像」分开

### 4.1 已有供应方线索，均带窗口

**Ewind（本轮页面观察；会话当前日期 2026-10-26，运行环境时钟显示 2026-11-19，实际采集日待核）**：搜索索引展示的 [Volza 公司摘要](https://www.volza.com/company-profile/angora-networks-informatics-technology-trade-industry-joint-stock-company-54698404/) 列 **Ewind Technology Co Ltd**；[TurkeyTradeData 公开公司页](https://www.turkeytradedata.com/company/angora-networks-bilisim/4da8548afd70d79878456c8e21724f57) 在 **2023-08-01—2024-07-31** 的供应商预览列 **Ewind Technology**、Eglobal Technology Company Limited、Shenzhen Fengrunda Technology Company Limited。**不是 r95 首次发现**：仓库 `../03-import-data/20-angora-import-records-2026-10.md` 第四节和 `../06-competitors/50-gordion-and-ewind-trade-data.md` 已记。两家商业聚合商可能基于重叠的海关数据，**不能当两个互不相干的逐票一手证据**。

以上只能支持「这两个第三方页面把名称列为供应商线索」。**具体供应批次、产品、成交价格、持续性及 Ewind 缩写与哪一个完整注册实体完全对应均未见**。另一个 Volza 索引的 Ewind 页面只显示印度一个买家，和 Angora 页面中的关联口径不同：可能存在不同覆盖范围、别名/实体合并或其他错误；不能消除冲突。**Ewind 是用户定义的竞对；不把它称为我方、也不声称其在 2026 仍给该客户供货。**

### 4.2 修正「HITIT = Ewind 白牌已实证」

旧 `../06-competitors/60-hitit-ewind-proof-and-peers.md` 将相同的 8FE+2FE/96W、8FE+2GE/120W、8GE+2GE/120W 规格表与印度第三方进口样例配对；其中 16 口 **200W 对 300W** 甚至不同，4 口电源配件也不能直接等同成一台交换机。**端口与预算相同是兼容形态，不是序列号、BOM 或逐票型号对应。** 即使两家贸易聚合页都列 Ewind，**也不能证明每台 HITIT 或任意具体型号的 OEM 身份，更不能说 Ewind 为最大供应商**。优先级降为「待核型号映射」，不再作为对客户的既定事实。

验证顺序：① 对既有经许可的铭牌/外箱/订购规格，核型号和生产批次；② 请求客户自愿提供匹配的 **BOM/ODM 授权或出货资料**；③ 用独立单据核买卖双方及时间。**不得要求客户泄露其他供应商机密，也不接触此前用户叫停深挖/主动联系的 Larch、Scodeno、Lanaotek。**

### 4.3 第三方贸易数据的质量测试

TurkeyTradeData 公开页写该窗口 **21 进口、$44.9K；1 出口、$5K，目的地 Jordan**；商品样例包括 2024-07-30 1 台 Ethernet switch、$304；2024-05-22 50 件 network-device modules、$882。**这些是商用数据商所示样例，不是本轮取得的海关原单或报价。** 不能把 21 票说成全部来自中国：该页概览明确列 China、Israel、Germany，且国家表金额占比分别为 91.4%、8.3%、0.3%。50 件的 $882/50 ≈ $17.64 是**该条申报总额的算术均值**，不是 SFP 价格、成本或报价；模块品名并未证明是 SFP。

对照非关联的 [European Tobacco 页面](https://www.turkeytradedata.com/company/european-tobacco-sigara/ab3466316c227e3c7d3cc21fea203ab6)：两页头部都显示同一组 **+18.5%、+12.3%、+8.7%、+24.2%**，且各自图表有与头部不一致的 12M 合计。**这证明展示层至少有模板化/口径风险，不证明所有明细是假的。** 同比增长率及「实时全面」营销语全部弃用；$44.9K 等仅可列为未审计、未逐票验证的第三方样本。不能用其估算 Angora 营收、进口总量或市场份额。

Volza 摘要称 45 入 / 2 出与来源国，中国 37、以色列 7、德国 1；旧 `03-import-data/20` 又记录具体出口样本可能均为约旦。**来源国、目的国与数字均暂按各自页面口径并列，未看完整提单，不能作全球精确数量或下结论 Russia/Jordan 必然一票各一。** 两网站统计期不同，45 vs 21 不能相加或视作自动冲突。

## 五、产品与网站：补读未读手册 + 明确哪些是宣传

### 5.1 Gordion：从 2022 宣传到真实售卖，中间仍缺证据

[`download/1053`](https://www.angoranetworks.com/download/1053/) 的表格列 **32×400G / 12.8 Tbps**；这足以推翻 r93 将「公司能力只到 10G」当作其**官方产品资料上限**，但文档广告数字 ≠ 成交、生产、库存或 2026 实际可交货。正文 12.5 与表中 12.8 自相矛盾；应原样并列，报价只按最新有型号的签字资料。

**r94「新发现 Gordion」也是错的**：仓库 `../06-competitors/50-gordion-and-ewind-trade-data.md` 2026-09-23 就已收过相同手册。本轮新增核对：Angora 自有 [KOZ'23 产品组合视频](https://www.youtube.com/watch?v=I5kDVMWC79I) 于 **2022-12-06 上传**，讲话提到 32 口 400G（自动字幕需听原音确认）；它是**历史产品宣讲的独立形式**，不是客户验收或 2026 售卖证明。另一个 [VERGE 官方页面](https://www.angoranetworks.com/verge-network-switch-serisi/) 在 Gordion 栏列 48×1/10/25G + 6×100G、写 **3.6 Tbps**；旧 DC 英文规格页又在正文写 3.6、表写 3.2。**不同页面/型号/双工口径不明，不能选一个充作认证规格。**

行动：向现有对口人员**按具体 SKU**询价、交期、受支持 OS、售后及一个经客户允许公开的案例；如果答不出，只记「历史目录存在，商业状态未证」，不能反过来说「实务上仍只到 10G」。不把 400G 直接当我方供货缺口。

### 5.2 Iris 长距机会：不是「第三次确认只到 10 km」

同源 `download/1039` 家族宣传册明列 **1G/2.5G SX/LX/EX/ZX；10G SR/LR/ER/ZR**，还写 25/40/100/400G 类别；该小册未给 EX/ZX/ER/ZR 的 Angora SKU、具体公里数、价格及交期。[Iris 旧型号表](https://www.angoranetworks.com/26/urunler/iris-sfp/)只逐项列出 SX、LX、SR、LR，最长标注 10 km。**两者不是相同层次**：五个已列 SKU 的最高距离为 10 km，不等于品牌或市场上不存在更长距离型号。**撤回 r94「Angora 只到 10 km，40/70/80 km 是已确认空白」**；保留长距产品为**可询的二供/交期机会**。

Angora 的 [100G 文档](https://www.angoranetworks.com/26/files/Angora-Datasheet-SFP100G-20210330.pdf) 在 `ANW-QSFP28-100G` 描述中直接出现 **“This module incorporates Gigalight Technologies proven circuit and VCSEL technology”**，但这仅证明文档使用该品牌技术措辞，**可能是参考资料沿用；不能证明该 SKU 的真实 BOM、授权关系或每一批实际供应商**。同一文档的 100G SR4 正文写 **MTP/MPO**，通用表却写 **LC**，且 `1M` 行写 6 ft；按具体批次核连接器、距离及料号。另有标名 100G 的官方链接实际返回 1G/10G 文档；链接名称不能替代打开文件后的内容。0–70 ℃也不能自动满足工业温度。

### 5.3 VERGE / ANMS / ThinCE：补读三份，型号边界不夸大

- **VERGE** [`1015`](https://www.angoranetworks.com/download/1015/) 文字列 2100（L2/1G SFP）、2200（L2+/10G SFP+）、3100（L3/10G SFP+），宣称最多 8 台堆叠；它是家族总览，**不能外推所有具体型号、固件均支持堆叠或该认证**。
- **ANMS** [`1035`](https://www.angoranetworks.com/download/1035/) 描述设备视图、状态、网络地图、报告，也称管理非 Angora 品牌；2022 演讲描述的是**管理自家设备、监控其他品牌**。混合品牌的下发配置、API 范围、授权数量和受支持版本**应逐机验证**。
- **ThinCE** [`1027`](https://www.angoranetworks.com/download/1027/) 列 ARM `ANW-THC-1000`/`2000` 和 Intel `3000`，文档写 Debian/Citrix、LTE/5G 及集中管理；**“5G”是产品资料字段，不是频段、认证或实际在售证明**。
- **Karınca** [`1031`](https://www.angoranetworks.com/download/1031/) 的 BASE 是 **8×1/10/25G、100 Gbps throughput**，另有 `ADD-XP` 端口与 `ADD-YGB` 吞吐许可；另一 [Karınca 网页](https://www.angoranetworks.com/26/urunler/karinca-network-packet-broker/) 头部称最高 1 Tbps、正文称 >3 Tbps、技术表称 1.9 Tbps。可能有不同型号/软硬件及单/双向口径，**原文没解释，故不可把任一数字当全系列实测能力**。

### 5.4 `ANW-5713-24S8T6X` 对 TTK：不能再写「全过」

r93 的 `162 §七` 先写 2.1 **「✅ 全过」**，同一行又标 **MAC 16K 未在官网标注**，还把官网的 `8T+24S` 当作满足招标所写 **8 个 combo**。后者只证明网页列了 8T 与 24S，**并未说明它们是否共享为 combo，或能同时使用**。2.2 的 IPv4/IPv6 静态路由数量和 16 kbps 粒度、2.3 的 32K MAC 也未在该表证明；授权、售后、供货和实际设备均须逐项查证。故**撤回 r93「Synapse 三档全过 / 只剩交期和售后」**，改为「若干官网数值达到阈值，其他关键项待核；不能据此认定合格或不合格」。

对官网标称的 128 Gbps 作一个**前提明确的压力检查**：若 `24×1G SFP + 8×1G RJ45 + 6×10G` 全为独立可同时使用，端口双向速率之和为 `(24+8+6×10)×2 = 184 Gbps`；即使 8 个电口与 8 个光口共享，仍是 `(24+6×10)×2 = 168 Gbps`。在厂家 **128 Gbps 与上述双向端口和采用相同定义**的前提下，均不能据此宣称全部端口同时满速无阻塞。TTK 若只使用 24 个千兆逻辑口及 4 个 10G 上行，理论和为 128 Gbps；但 combo 对应、端口限制、芯片/软件实际转发和容量统计口径仍未知。**这不是实测，也不是判废标**；应请求厂家针对具体型号、硬件版本、combo 关系、并发端口配置、64 字节包测条件及整标条款给书面答案。网页的 106 Mpps 未写测试口径，不据它直接推断互相矛盾。

### 5.5 维护和质保是可谈项目，不是无条件承诺

Angora [服务页](https://www.angoranetworks.com/26/hizmetler/)列 best-effort 15 天、次日或 4 小时更换，以及软件 5×8/7×24 年维护选项。均为厂商营销服务选项；**覆盖地区、适用型号、库存、价格、合同 SLA、2026 履约能力未知**。客户谈判可先核「需要多长交期 / 备机在哪 / 谁负责 RMA」，避免替其承诺全国四小时。

## 六、渠道与时间线重做：不能用几个名字推出全国空白

1. **KOZ'23 发生于 2022，非 r94 的 2023-10-19。** [ICT Media 2022-10-18 预告](https://ictmedia.com.tr/haber/angora-networks-kanal-ortaklari-zirvede-bulusuyor)说 19 Ekim 且讨论 2023 策略；[Angora 频道 KOZ 视频](https://www.youtube.com/watch?v=jrdoTa5owZk)上传于 **2022-12-03**，不能是 2023-10 活动的录像。结合材料，**2022-10-19 为高可信日期**，保留预告与录像的证据层次。此前 `../02-social-intel/50-angora-youtube-koz23-intelligence.md` 已记录，r94 忽略了它。
2. 预告提 Elcore 主讲「ANGORA & ELCORE 合作与分销力量」；可证明**当年拟展示分销合作**，不证明唯一总代、排他、截至本轮仍在代或具体成交。Elcore [本轮首页](https://elcore.com.tr/)展示的供应商区未看到 Angora；**未列出 ≠ 已终止**，且页面展示未必穷尽。不能要求其披露客户或项目。
3. r94 的「1+4+1=6、与 81 省对不上，所以渠道密度极低」不成立。**已找到几个名字是样本下界，不是全国渠道总体或市场密度**；`../06-competitors/60-hitit-ewind-proof-and-peers.md` 很早已记 Advensis 的历史 Angora 产品页面，2022 官方影片和既有资料还提 Fi/Kaleiçi 的历史安排。没有逐省/逐年完整名单，既不能确认 81 省，也不能证伪其覆盖。`angora.club` 直接抓取失败，仅搜索摘要可见，不当完整伙伴名录。
4. Zafer Doğruel 的旧 KOZ 职务是**历史职务**。公开职历索引显示其 Angora 渠道经理为 2021–2024、2025 起在 Andasis，来源为 [RocketReach 索引](https://rocketreach.co/zafer-dogruel-email_205015321)，不能断言本日状态。**撤回 r94「现在首问 Zafer 办报备」；先通过已联系的 Levent 确认当前对口人。**
5. `ut-in-laoreet-sapien-eu-amet` 页显示 2017-02-03，同时复用含 `20201124` 的图片路径，官网沿革又称 2018 第一款产品；这无法证明 2017 订单是服务、贸易还是设备，也无法证明首次出口日期。**撤回 r94「2017 年出口肯定是服务/贸易，不是设备」**。
6. r94 所引媒体稿标注 2026-10-30，晚于会话给出的当前日期 2026-10-26；保留其线索，但**不得作为截至会话日已发生的决赛/获奖事实或趋势**，须以独立来源核对其时点。运行环境时钟的不同显示不能单独证明已发生。

## 七、给现有合作关系的下一步（不骚扰、不发信）

| 优先级 | 可由 Levent 确认的问题 | 所需结果 | 不应说 |
|---|---|---|---|
| P0 | 现有合作按型号、批次、固件/授权和 RMA 联系人怎样维持？ | 同一已有客户的准确接口与记录 | 「我们是第 16 家新供应商」 |
| P0 | 小批现货或备机可按 25/50 台等情景测算吗？地点、预付款、存货归属、汇率、滞销与售后谁承担？ | 条件报价表，**非承诺授信** | 88 台还会成交；替其承诺融资 |
| P1 | Iris ER/ZR/ZX 的**现售型号**、距离/预算/兼容测试、交期、MOQ？ | 该 SKU 的买卖或二供条件 | 「你们没有 40/70/80 km」 |
| P1 | 400G Gordion 哪个 SKU 可以报价，固件/质保/案例是否可公开？ | 可证实的商业状态 | 「产品一定已停产」或「已经大量交付」 |
| P1 | 哪个型号需要工业宽温 PoE++？功率预算、版本和认证要求？ | BOM/样机与技术验收 | 把目录没列出等同于绝对没有 |
| P2 | 哪位是当前渠道/报备负责人；所需授权、项目保护规则是否有修订？ | 最新书面条款 | 旧日职务当现任；追问其不愿透露的 strong partner |
| P2 | 有无可分享的 Angora 当前登记摘录（股东/资本/签字权限）？ | 最近正式文件 | 用 Connexite 持股/负净资产替代土耳其公司财务 |

**合规底线**：不承诺我方能帮客户拿 KBYB；不说某标要求 KBYB 必然违法；不说有 KBYB 等于通过安全审查。硬件及服务按真实交易内容申报，不建议虚开发票。未获得客户同意之前不引用或传播内部对话、其他供应商身份及合同细节。

## 八、修正清单（有旧值、有新值、有出处）

| 修正对象 | 旧判断 | r95 取代/划边界 |
|---|---|---|
| **r94 / `163`** | 我方是第 16 家新供应商 | **作废**：2024 起已有我方形式发票和商业往来；第三方列表非穷尽 |
| **r94 / `163`** | 公报没有找到 | **作废**：仓库有 2024-03-11 OCR 与用户所传 PDF 的索引；股权金额仍未核实 |
| **旧 `96` / `121` / `122`** | Hakan 是 Angora 新董事长、沉默资方 | **撤回，主体未确认**：多栏混排，Bursa ITECH 邻栏高度疑似；严禁人物归属与资本推断 |
| **r94 / `163`** | 2017 首次出口且肯定是服务 | **撤回**：日期及具体货物未解；2018 时间轴和旧帖互有张力 |
| **r94 / `163`** | KOZ'23 在 2023-10-19 | **修正为 2022-10-19 高可信**：2022-10-18 预告与 2022-12 视频互证 |
| **r93/r94** | 4 家或 6 家=总渠道，81 省失实、东部无渠道 | **作废**：名单样本不完整，实际数量/覆盖均未知 |
| **r93 / `162`** | Synapse 已全过 TTK 三档，只剩交期和售后 | **撤回全过**：`5713` 的 8T 是否 combo、MAC 表及部分路由等未证明；不同端口并发与 128G 口径需书面核验 |
| **r94** | Elcore 唯一总代且当期持续 | **撤回唯一/当前关系**；只有历史分销合作线索 |
| **r94** | 只到 10km，长距是确定缺口 | **作废**：官方手册写 EX/ZX/ER/ZR 类别；SKU/距离/现售待询 |
| **旧 `60` / 贸易档** | HITIT 全系 = Ewind，Ewind 是最大供应商 | **降为线索**：通用规格相同 + 聚合商供应商列表不足以锁定具体 OEM 或排名 |
| **r94** | Gordion、Advensis 和 Elcore 是首次发现 | **更正**：分别在 `06-competitors/50`、`60`、`02-social-intel/50` 已有；本轮是复核与回收，非首次发现 |
| **r94** | 10/30 报道=10/26 时已入围且未获奖 | **撤回截至当日的事实判断**；未来日期不能作为过去发生的证据 |

## 九、证据等级、源数与空白

- **A｜正式申报/公司自述（不是成交保证）**：Companies House NEWINC、2023/2024/2025 CS01、2024/2025 micro accounts、PSC 与 officers；Angora KOZ 录像元数据及台词、产品手册、Iris/VERGE/服务页面。英国财报属于公司递交，**免审计、注册处不核实**。原件二进制本轮未下载；11 个保存项均为逐 URL 的**文本抽取**。
- **A-｜用户提供的内部一手商业材料的本地抽取**：2024 形式发票、2024 邮件和 2026 对话；原始扫描版公报未在本轮取得，仅 OCR，有跨栏和视觉待核风险。`120`/`123` 为已入库分析，不自动升格为全部原始凭证。
- **B/C｜第三方**：ICT Media 的历史预告；Volza 搜索索引、TurkeyTradeData 的页面与对照页、RocketReach 职历、Advensis 搜索索引。数据商彼此可能共享原始数据；标为参考，不视作两张原始海关单。
- **源数降级与可复核口径**：本轮**保存 11 份独立来源的完整可见文本抽取**（英国官方 3、Angora 官网 7、第三方贸易页 1）；另引用未单独落盘的官方 NEWINC/PSC、网页和 2022 视频，以及仓库既有原始抽取/研究。与 r94 的「44 个去重引用」不是同一统计口径，不能用百分比比较质量；本轮主动缩到能逐项对账的重点来源，低于宽泛全景抓取数。付费锁定、未读取的后台数据、失败请求不算已获全文。
- **当前不可确认**：Angora 最新股权/资本和最近财务报表；公报原图跨栏人物；Connexite 股权与 PSC 表决权表面不一致的原因；两家公司的法定股权关系；Gordion 400G 现货/真实项目；Ewind 对 Angora 的具体型号与近年批次；IRIS 长距 SKU/性能/价格；Elcore 当前授权/排他/覆盖；KOZ 2024–26 是否续办；YMB/Sanayi Sicil 有效证书；任一客户 logo 的合同金额。未拨电话、未发信、未操作第三方账户。

**与 r94 的差异**：r94 把已有资料当新发现、忽略我方交易及公报、把渠道和进口索引过度推断；r95 回到一手/旧档案逐条校验，并新补英国官方主体的股权时序与两年微型账目。所有修正保留旧文以供追溯，同时在原载体和映射索引显式提示，不能静默覆盖。

## r103 增补：IRIS 模块规格与证据边界

厂商可见文本中存在 10G SR 参数行、100G 接口、25G AOC 表项及线缆单位疑点；没有原始 PDF 与实物，不能认定产品故障。多 URL 的归一化文字复用不是独立原始证据。见 [r103 报告](172-angora-optics-port-evidence-r103-2026-10-26.md)。


---

## r108 限定／修正 r95：KOZ 日期证据层

前文把 `2022-10-19` 作为实际活动“高可信”过于确定：2022-10-18 媒体稿是对 19 Ekim 的**事前预告**，Angora 另一条 KOZ'23 市场演讲视频的 `2022-12-06` 上传字段不独立证明现场日期。计划日期、视频上传、实际召开和议程履约应分开；未取得能够单独确认活动当天的资料。仍保留 r95 对 r94 将这则预告直接写成 `2023-10-19` 的撤回，也不排除另有同名活动。详见 [r108 报告](177-angora-koz-survey-channel-evidence-r108-2026-10-26.md)。
