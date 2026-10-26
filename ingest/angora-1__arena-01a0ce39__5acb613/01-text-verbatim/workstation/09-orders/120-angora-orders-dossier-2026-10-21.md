# 120 · Angora 订单链全量档案（Google Drive 订单文件夹 → 本地知识库）

- 日期：2026-10-21（第 27 轮）
- 来源：Google Drive 根文件夹（36 项 = 23 文件 + 13 文件夹；子层共 **317 项 = 283 文件 + 34 文件夹**，实测清单见 §8）
- 读取方式：`google_drive__read_file_text` 逐文件抽取（PDF/DOCX/XLSX/TEXT 可读）；**legacy `.xls`/`.doc` 仅索引**（API 不支持抽取，且禁止下载 base64 = 内存爆炸，用户指令「尽量不占内存」）；图片/视频/PSD/DXF/CAD/7z/RAR/zip 一律只索引不下载
- 主数据文件：`120-angora-orders-master-2026-10-21.csv`（9 单行级 P&L + 行项 + 物流 + MAC/SN + Drive 索引）
- ⭐ 本档案 = Angora 订单链**唯一完整底账**；此前 r13 进口记录（Volza 45 票 / TTD 21 票 $44.9K）= 海关视角，本档案 = 合同/发票视角，两者互补

---

## 1. 关系链与关键人

```
土耳其侧                              中国侧
Angora Networks Bilişim A.Ş.  ←→  郑州伊博通讯器材有限公司（Saga / 我司）
├── Ankara · Ziraat Çayyolu 支行 IBAN TR09 0001 0019 8997 0378 9850 02
│                                  Simon Cheng 15237149683（商务）
├── Levent Kilic（LK = Angora GM，谈判署名；护照 PII 仅索引）
├── TronX Bilişim ve Sağlık Tekn. Ltd. Şti.（姊妹公司；Mustafa Calik
│   mustafa.calik@tronx.com.tr +90-531-450-4445）
├── Turk Telekom（TT 贴牌通道：TT-2208-PG/TT-2208-TG）
└── EGM 土耳其警察局（3,294 台项目，KGYS/ÇGKS）
                          ↓ 采购
                深圳凌特华盛（SmartByte；Peter Hu 13714293521；惠州惠阳产业大道）
```

- 币种：Angora→Saga 付 **USD**（水单 Ziraat 银行）；Saga→SmartByte 付 **RMB**（STSC 合同；郑州伊博开票「未税 RMB」，发票额 == 合同额 = 对平锚）
- 汇率口径（成本统计.xlsx 自含）：1 USD = 7.15 RMB
- 货代链：深圳百运网（韦德晶 19114693006 早期 / 陈佩珍 15323556923 2025 起），FedEx 发土耳其（WE 开头运单号）
- 定价规则（运费一览表.xlsx）：向客户按 **~30% 利润率**在货代成本上加收运费（18.54 RMB/kg ≈ $2.6/kg）

## 2. 订单总览（9 单）

| # | STSC 号 | 日期 | 客户 | 内容（量） | 成本 RMB | 收款 USD | 利润 RMB | 利润率 | 状态 |
|---|---|---|---|---|---|---|---|---|---|
| 1st | STSC20240508007 | 2024-05-09 | Angora | 4 台样品（2×8口工业 + 24口L3 + 48口L3） | 6,991.42 | 1,265 | 2,158.96 | 23.6% | ✅ 已付已出 |
| 2nd | STSC20241021007/1028/1105 | 2024-10~11 | Angora | 8×ANW-2116-PG + 2×ANW-1108-V + PVC + GUI 费 | 10,967.61 | 2,345 | 5,753.90 | 34.4% | ✅ 已付已出 |
| 3rd | STSC20250117007 | 2025-01-17 | Angora | **178×ANW-2116-PG**（176+2 备）+ 电源×2 | 288,123.96 | 47,174 | 54,296.26 | 15.9% | ✅ 已付已出（最大单） |
| 4th-pre | STSC20250228007 | 2025-02-28 | Angora | 行项在 legacy .xls（未抽取） | 9,110（发票） | 0 | — | — | ⏸ 未出货 |
| 4th | STSC20250507007 | 2025-05-07 | Angora | 3×ANW-2224-PX + 3×ANW-2248-PX 样品 | 9,705.99 | 1,665 | 2,227.08 | 18.7% | ✅ 已付已出 |
| 5th | STSC20250526007 | 2025-05-28 | Angora+TronX 双品牌 | 10×2224-PX + 3×2248-PX | 17,577.19 | 3,755 | 9,250.80 | 34.5% | ✅ 已付已出 |
| 6th | STSC20250619007 | 2025-06-23 | **TT 贴牌** | 6×TT-2208-PG 工业（TT Logo） | 4,948.45 | 990 | 2,102.12 | 29.8% | ✅ 已付已出 |
| 7th | STSC20250711007 | 2025-07-11 | TT 贴牌 | 10×TT-2208-PG（仅 MAC/SN 表为证） | 未上传 | 未上传 | — | — | 📋 MAC/SN 已分配 |
| Unpaid-1 | STSC20241129007 | 2024-11-29 | **TronX** | 24口$180+48口$335+2×工业8口$125+7类SFP×5+2×WiFi6 AP，FOB **$1,480** | 合同 12.6MB 未抽取 | 0 | — | — | ❌ 未付款（PASSED 项，仅登记） |

**累计（6 单已成交）**：成本 **338,314.62 RMB** ← 收款 **57,194 USD = 414,103.74 RMB** → 总利润 **75,789.12 RMB**（加权 **18.3%**）
**未了结**：4th-pre 9,110 RMB 未出货单 + TronX $1,480 未付款单
**运费利润**（6 单合计）：200+445+4000+350+700+125 = **5,820 USD 加收** vs 实际货代成本 29,720.62 RMB（= 4,156 USD）→ 运费毛利 ≈ 1,664 USD

## 3. 逐单详细事实

### 3.1 1st（STSC20240508007，2024-05）
- 合同（采购合同.pdf 177KB 可读）：3 行（LT-S8210GP-2GX8GT ×2 @500 / LT-S8528XGP-4XS24GT ×1 @1900 / LT-S8552XGP-4XS48GT ×1 @3100），交货期 3 周，付款 = 发货前付清（USD T/T），交货地 = 工厂
- 行项备注：8 口工业 PoE **af/at 欧规电源线 Angora Logo**；24 口 L3（4×2.5G SFP + 24×1G）；48 口 L3（4×2.5G SFP + 48×1G）
- 客户定制：SN 格式、Angora logo（WEB 界面 + 设备外观）、1 年质保
- 收款：Angora 2024-05-08 Ziraat 水单（IBAN TR09 0001 0019 8997 0378 9850 02）；Saga 同日付 SmartByte（货款支付记录.jpg）
- 出货：FedEx WE02405009117；出货子夹 = ANW-3108-PG / ANW-3124-PX / ANW-3148-PX（3 个照片子夹 + Certificate of Warranty.psd 5.2MB + 8口/24口照片）
- 型号口径备注：合同 SmartByte 型号 ↔ 客户型号 ANW-2208-PG / ANW-3424-PX / ANW-3448-PG ↔ 出货夹命名 ANW-3108/3124/3148（同品三套命名，历史遗留）
- 伊博发票：P20240510-01（未税 6000 RMB，.doc legacy 仅索引 1.56MB）

### 3.2 2nd（STSC20241021007 + 1028007 + 1105007，2024-10/11）
- 两个伊博发票已签章 PDF（可读）：
  - **P20241026-01**：5×LT-S8328GP-4GX16GT-S @750 + 2×LT-IS6310G-2GX8GT @622 + PVC 面贴×100 @6.3 + 管理界面修改×1000 → 毛 6,624 / 净 5,624 RMB（文件名取净值）
  - **P20241106-01**：3×LT-S8328GP-4GX16GT-S @750 = 2,250 RMB（对应 STSC20241105007）
- 合同 3 份 legacy .xls（1.63MB/258KB/1.46MB）仅索引；STSC20241021007.xls 5.77MB / STSC20241105007.xls 707KB
- 成本表：8×750 + 2×622 + 630 + 1000 + 运费 2,093.61 = 10,967.61 RMB；收款 1545+200+600 = 2,345 USD
- 出货：货代 深圳宝安福源大道 141 号大塘田工业区 8-9 栋（中科/百运网 韦德晶）；WE02411006486 2024-11-06；运费 445 USD（18.54 RMB/kg）
- 2024-11-28 谈判纪要（Angora-Replies_2024.10.23.docx 1.26MB + 夹内文档，3rd 单前置谈判）：5% 折扣、新外壳 $10/台（放弃）、PVC 100pcs $2.30、console 线 $1 分摊、$200 软件费抵扣、30-20-50 付款、UPS $7K 放弃
- 夹内含：STC-448DGGPM.cdr + STC-424DGGPM-280W.cdr（**TronX 标签图稿** = 姊妹公司同平台）、ANW-1108-V/ANW-2116-PG User Manual（PDF+pub）、label 图、GUI after change.png
- **⭐ TT 渊源**：本单 2×ANW-1108-V（LT-IS6310G-2GX8GT）= 后于 2025-02-03 送 TT 测试的样品（RFP_2025.1.30 中型号记为 TT-2208-TG）→ 量产 TT-2208-PG（6th/7th 单）

### 3.3 3rd（STSC20250117007，2025-01-17）——最大单
- 合同 PDF 279KB 可读：SmartByte 型号 **LT-IS6318GP-2GX16GT**（2×1/2.5G SFP + 16×1G PoE 工业 L2+）×178 @1,490 = 265,220 RMB + 鹰盾电源 ×2 @239 = 478
- 谈判成果（Reply on 174 pieces...docx 24KB 可读）：5% 折扣、RMA 2%（→ 实发 176+2 备）、30-20-50 付款、生产 4 周、UPS $7K 太贵→改海运/陆运评估后仍走 FedEx UPS
- 伊博发票：P20250303-01 未税 265,220 RMB（.doc legacy）
- 收款：货款支付记录 6 张 + Payment Receipt.pdf（2025-01-16 → 03-07）
- 出货：WE02503002566 2025-03-02；包装 32+2 箱 ≈700kg；Commercial Invoice_R1.xls 5.9MB + Shipment Label 5MB + 视频 4 段（195-6,889KB）
- SN 25012116XXX03（001-176）；MAC 池 98:06:37:**A1:00:00~A4:FF:FF**（4,096 地址段）
- 定制电源 **ANW-PWR-48-240**（橙色、Angora Logo、去 Made in China 标识）
- 夹内：lite-hotfix-7.3.13.bin **62MB**（Marvell AC3 末版固件 = 与 2026-08-17 回复「AC3 冻结在 7.3.13」互证）、Reply on RFP 2024.12.10.docx（Marvell 自研软件/SFTP/串口 = TT 差异化回复）、Info to be provided-Angora.docx（SN/MAC/电源规格确认）
- 子夹：Sample Confirmation（包装确认 9 图含 29.7MB 包装箱图）/ 采购_Smartbyte（176 台报价 + LT-IS6318GP User Manual）/ 采购_Yingjiao（**盈教/鹰盾 2 台测试样品** 出货照片）/ TT-2116-PG.zip（**TT 贴牌 2116 资产** = TT 线扩型预研）

### 3.4 4th-pre（STSC20250228007，2025-02-28）——未出货单
- 位于 4th order/**Unshipped** 子夹（12 项）：采购合同_STSC20250228007.xls（468KB）+ 4 份 R 版（488KB）+ **伊博 P20250304-01 未税 9,110 RMB**（.doc legacy）+ PL + 装箱单 + User Manual（608KB，同 2nd 单模板）+ 需求_2025.2.28.png + PVC.png + 出货照片夹
- 行项在 legacy .xls 内未抽取；金额以发票文件名 9,110 RMB 为口径
- 状态：**未出货**（截至 Drive 快照）；后续 fate 待用户确认

### 3.5 4th（STSC20250507007，2025-05-07）——样品批
- 3×STC-424XGGPM @920 + 3×STC-448XGGPM @1810 = 8,190 RMB；伊博 P20250508-01 未税 8,190 ✓对平
- 出货：货代深圳百运网（陈佩珍）；WE02505007424 2025-05-12；运费 350 USD vs 1,515.99 RMB
- MAC 98:06:37:**A5:00:00~05**；SN 25052224**A**01-03 / 25052248**A**01-03
- 夹内：ANW-2224-PX / ANW-2248-PX 产品照片+GUI 截图子夹；采购合同 PDF 可读
- 产品：ANW-2224-PX = 24×1G PoE + 4SFP（1/2.5/10G）**L2+ AC5 防爆型 280W**；ANW-2248-PX = 48×1G PoE + 4SFP L2+ 440W（**= SAGA 街价 $340/$530 型号 STC-424/448XGGPM**，见 05-turk-telekom SAGA L3 报告）

### 3.6 5th（STSC20250526007，2025-05-28）——Angora+TronX 双品牌
- 10×STC-424XGGPM @920 + 3×STC-448XGGPM @1810 = 14,630 RMB；伊博 P20250530-01 未税 14,630 ✓对平；**发货前付清**
- 出货：WE02506006381 2025-06-01；运费 700 USD vs 2,829.55 RMB（实际）
- MAC 98:06:37:A5:00:06~12；SN 25052224**B**01-10 / 25052248**B**01-03
- **TronX 双品牌资产全在这**：TRX-AS-24TP4X.zip / TRX-AS-48TP4X.zip（logo 包）、TronX User Manual_reference only.pdf、TRX web gui / log-in 截图、TronX Commercial User Manual.pub（3.68MB）、label confirmation.docx、Black/White TRONX.psd（根夹）
- 采购合同 PDF 279KB 可读（Angora 抬头，双品牌出货）

### 3.7 6th（STSC20250619007，2025-06-23）——TT 贴牌通道
- **6×TT-2208-PG @712** = 4,272 RMB（LT-IS6310GP-2GX8GT 工业 2 光 8 电 L2+，PoE 240W，3 年质保，DC44-57V 输入，无电源无串口，**Turk Telekom Logo**）；伊博 P20250624-01 未税 4,272 ✓
- 出货：WE02506020141 2025-06-13；国内运费 30 + 国际 646.45 RMB
- MAC 98:06:37:A5:00:13~18；SN 25052208**C**01-06
- 夹内：STI-288DGGPM 图纸（dxf 18.7MB / ai 1.06MB / pdf 322KB）= 工业 8 口机箱图；User Manual 445KB + pub 6.7MB
- **通道意义**：Angora 以集成商身份把 SAGA 工业交换机贴 TT 标卖给 TT = 白牌进入运营商体系的活样本（与 PNetworks-Edgecore 同构，见 110 行 1）

### 3.8 7th（STSC20250711007，2025-07-11）——TT 延续单
- 仅 **mac_address&serial_number.xlsx**（28KB）为证：10×TT-2208-PG，MAC 98:06:37:A5:00:19~22，SN 25052208**D**01-10
- 合同/发票未在 Drive 上传；金额未披露 → 按 TT 通道持续放量处理（6+10 = 16 台已登记）

### 3.9 Unpaid-1（STSC20241129007，2024-11-29）——TronX 一次性单（PASSED 项）
- 客户：**TronX Bilişim ve Sağlık Teknolojileri Ltd. Şti.**（Angora 姊妹公司；Mustafa Calik）
- 报价（FOB，USD）：STC-424DGGPM-280W ×1 $180 / STC-448XGGPM ×1 $335 / STI-288DGGPM ×2 @125 / SFP 7 类 ×5 只（1G-SX $25 / 1G-LX $25 / 10G-SR $40 / 10G-LR $50 / 25G-SR $100 / 40G-SR $165 / 100G-SR $210）/ WiFi6 AP TRX-AP-612T ×2 @50 → **合计 $1,480**
- SmartByte SFP 成本对照（报价表内文）：26 / 26 / 39 / 51 / 99 / 172 / 218.5 RMB
- 内文备注：「该公司为土耳其客户的另外一个公司」「一次性单子，质量和价格 OK 就行」「光模块未说工商业级别，高速只做商业级」
- 文件：STSC20241129007.xls **12.6MB** + Quotation.xls + Tronx Saga Siparis Listesi-3.xlsx（77.9KB）+ Tronx...Smartbyte报价.xlsx（11.4KB，可读）
- **状态：未付款（文件夹名「未付款1」= 铁证）→ PASSED 项：仅数据登记，不催款、不再分析**

## 4. 型号对照总表（三套命名 → 一套底）

| SAGA 内部（采购合同） | Angora 客户型号 | TT / TronX 贴牌型号 | SmartByte 平台 | 端口形态 |
|---|---|---|---|---|
| STI-288DGGPM（drawing） | — | TRX-IS-8TP2G | LT-IS6310G-2GX8GT 系 | 8×1G+2SFP 工业 L2+ |
| LT-S8210GP-2GX8GT | ANW-2208-PG（出货夹 ANW-3108-PG） | — | LT-S8210GP-2GX8GT | 8×1G PoE+2SFP 工业 |
| LT-S8528XGP-4XS24GT | ANW-3424-PX（夹 ANW-3124-PX） | — | LT-S8528XGP-4XS24GT | 24×1G+4SFP L3 |
| LT-S8552XGP-4XS48GT | ANW-3448-PG（夹 ANW-3148-PX） | — | LT-S8552XGP-4XS48GT | 48×1G+4SFP L3 |
| LT-IS6310G-2GX8GT | ANW-1108-V | TT-2208-TG（测试名） | LT-IS6310G-2GX8GT | 8×1G+2SFP 工业（TT 测试样机） |
| LT-S8328GP-4GX16GT-S | ANW-2116-PG | （TT-2116-PG.zip 预研） | LT-S8328GP-4GX16GT-S | 16×1G PoE+4SFP 1U L2+ |
| LT-IS6318GP-2GX16GT | ANW-2116-PG（3rd 单 178 台） | — | LT-IS6318GP-2GX16GT | 16×1G PoE+2×2.5G 工业 L2+ |
| STC-424XGGPM | ANW-2224-PX | TRX-AS-24TP4X | STC-424XGGPM | 24×1G PoE+4SFP L2+ AC5 防爆 280W |
| STC-448XGGPM | ANW-2248-PX | TRX-AS-48TP4X | STC-448XGGPM | 48×1G PoE+4SFP L2+ 440W |
| LT-IS6310GP-2GX8GT | — | **TT-2208-PG**（6th/7th 单 16 台） | LT-IS6310GP-2GX8GT | 8×1G+2SFP 工业 PoE 240W 3 年质保 DC44-57V |
| 配件 | ANW-PWR-48-240 电源 / PVC 面贴 / GUI 定制 | Black/White TRONX.psd | 鹰盾电源 | — |

## 5. 财务底账（成本统计.xlsx 全 6 单，已对平）

| 单 | 成本 RMB | 收款 USD | 收款 RMB(7.15) | 利润 RMB | 利润率 | 运费加收 USD |
|---|---|---|---|---|---|---|
| 1st | 6,991.42 | 1,265 | 9,150.38 | 2,158.96 | 23.6% | 200 |
| 2nd | 10,967.61 | 2,345 | 16,721.51 | 5,753.90 | 34.4% | 445 |
| 3rd | 288,123.96 | 47,174 | 342,420.22 | 54,296.26 | 15.9% | 4,000 |
| 4th | 9,705.99 | 1,665 | 11,933.07 | 2,227.08 | 18.7% | 350 |
| 5th | 17,577.19 | 3,755 | 26,827.99 | 9,250.80 | 34.5% | 700 |
| 6th | 4,948.45 | 990 | 7,050.57 | 2,102.12 | 29.8% | 125 |
| **合计** | **338,314.62** | **57,194** | **414,103.74** | **75,789.12** | **18.3%** | **5,820** |

- 成本 = 货物 + 国内运费 + 国际货代成本（实际）；3rd 单利润率最低 = 178 台大单 5% 折扣 + UPS 空运溢价
- 发票对平锚：伊博开票额 == STSC 合同额（6/6 单验证）
- 待了结：4th-pre 9,110 RMB（未出货）+ TronX $1,480（未付款）

## 6. MAC / SN 登记总表（mac_address&serial_number.xlsx，28KB）

| 段 | 型号 | 数量 | MAC | SN | 对应单 |
|---|---|---|---|---|---|
| 001-002 | ANW-2208-PG | 2 | （早期未列段） | 20240509001/002 | 1st |
| 001-176 | ANW-2116-PG | 176 | 98:06:37:A1:00:00~A4:FF:FF | 25012116XXX03 | 3rd |
| A 系列 | ANW-2224-PX / ANW-2248-PX | 3+3 | 98:06:37:A5:00:00~05 | 25052224A01-03 / 25052248A01-03 | 4th |
| B 系列 | 同上 | 10+3 | 98:06:37:A5:00:06~12 | 25052224B01-10 / 25052248B01-03 | 5th |
| C 系列 | TT-2208-PG | 6 | 98:06:37:A5:00:13~18 | 25052208C01-06 | 6th |
| D 系列 | TT-2208-PG | 10 | 98:06:37:A5:00:19~22 | 25052208D01-10 | 7th |

- OUI 98:06:37（SAGA）；**预留 MAC 池 A5:00:00~A5:05:FF = 2,048 地址**（TT 通道余量 2,000+）

## 7. 管线与战略文件（非订单夹，同 Drive 根）

### 7.1 RFP 文件夹（16 项）——TT 通道起源
- 时间线：RFP_2024.5.9 → 2024.5.27（**Turkcell 运营商 RFP 合规表**：non = OpenFlow/Y.1731/TWAMP/RTR；partial = PON SFP/-20~70°C/无热插拔/4093 VLAN/无 VRF-BFD-NAT/无 PIM/无 Netconf-YANG；Angora 自有 ZTP）→ 2024.6.15（TT-RFP-EN.pdf + 两次沟通 mp4 32MB/85MB）→ 2024.7.2（ÇTIPI ETHERNET ANAHTAR KGYS.pdf = TT 技术规格）→ 2024.7.11 SFTP reply → 2024.7.12 R&D 周期成本 → 2024.12.11 RFP → **RFP_2025.1.30（TT 测试起源：送 ANW-1108-V 样品，2025-02-03 测试，型号 TT-2208-TG）** → 2025.2.5 SFTP check list + Turk_Telekom_Test_Items.xlsx → **Saga Software Function List 7.3.0**（Marvell AlleyCat3 vs 5 = 「AC5 方案」；MAC 16k / ERPS 20ms / 静态路由 256/768 / ACL 240/480 / sFlow）
- 量产落地 = 6th 单 TT-2208-PG ×6 → 7th ×10

### 7.2 警察局项目文件夹（EGM，8 项）
- **⭐ 3,294 台**（KGYS.txt）：Mehmet ÇATAL 2026-02-12 批准
- 规格（ÇGKS.txt 3.3.1 室内 44 条 + 3.3.2 野外 23 条）：野外 = 8GE+2SFP、70km、-40~+60°C、IP20、无风扇、DIN 安装、全口 PoE；室内 = 24GE+4SFP、56Gbps
- **EGM C-Type 测试报告 SUCCESSFUL 为强制项**；对样：DLink DIS300G compliance 表
- 翻译 PDF ×3（KGYS §3.3 / ÇGKS 3.3 Network Switches / EGM 3.3+3.4 EN）
- 与 r25 已归档 wechat-2026-business-digest（警察局招标盘）互证

### 7.3 SAGA L3 报告 + 官方回复（2026-07-31 / 2026-08-17，1.08MB docx + 153KB pdf）
- LK（Levent Kilic，Angora GM）发起：TT 2026 tender 需 **stacking/USB/OOB/dual-PSU + OSPF/BGP/VRF**；市场价 24 口 L3 $1,000-1,100 / 48 口 $1,500-2,500 vs **SAGA 街价 $340/$530（STC-424/448XGGPM）**
- Simon 回复（已归档 01-knowledge-base/2026-08-17-l3-strategy-official-reply.md）：**AC3 冻结（末版 lite-hotfix-7.3.13）、L3 "let it be"、⭐ CENTEC L3 功能全有 → 「Saga 锁定 Marvell L2+ + CENTEC L3」双芯片战略**；RAM/PCB 涨价压现金流
- ⭐ 3rd 单夹内 lite-hotfix-7.3.13.bin = 回复中「末版冻结」的物理实证

### 7.4 加深关系绑定.docx（2026-07-20，94KB 可读）
- Lira 本地付款 / 多语言 GUI / 伊斯坦布 office+仓 / **Marvell 无同行全线护城河** / VMI / co-branding「Saga Telecom & Angora Networks」/ 短中长期三步绑定

### 7.5 其他根夹文件
- **Turkey Client List.xlsx**（25KB 可读）：55+ 土耳其 prospects（含 Opax / Entegron = Longline 第 2 品牌 / Longline 本身）；备注「本地公司多有中资供应商」
- **Quotation_48 port switch 150pcs.xls** + **Quotation_5电口 工业MC.xls**（legacy 仅索引）
- **TRY.xls**（5.56MB legacy 仅索引）；**PVCs.xlsx**（229KB）
- **Connexite-Amazon-Biz-Plan-DRAFT.pdf**（393KB 可读，Amazon 业务计划草稿）
- **ANGORA TICARET SICIL 11 MART 2024.pdf**（39.9KB = 2024-03-11 商业登记，与 96 号档案 2024-03-09 股东大会互证）
- **Proposal.docx**（410KB 可读）；**Agenda/Key Points for WeChat meeting 2024.10.31 + 2025**（docx）
- PCB板带LOGO.png / ANGRA LOGO2.ai / trontx.png / Black/White TRONX.psd = 品牌资产
- ⚠️ **LK-Passport-chip.pdf（635KB）= 护照 PII：仅索引，不抽取不引用**

### 7.6 IoT Board（4 项）/ Karen 工业模块测试结果（4 项）/ WeChat Talk（26 项）
- IoT Board：PCB.jpg + IoT Prototype.jpg + **SC0012-000.pdf**（2.14MB 可读 = IoT 模块规格）+ PC0012_Saga.7z（9.3MB 仅索引）
- Karen（李 = NEM Engine 关联人）：-40°C / +75°C / 测试端口 1、2 照片（工业温度测试记录）
- WeChat Talk：**26 张 Weixin 截图（2026-09-23 ×25 + 2026-10-06 ×1）**—— ✅ **r28 已全量视觉对平**：25 张 = Levent KILIÇ 会话完整长截图平铺（图 1 顶 = 会话最顶 **2024-05-02 16:36**「You have added Levent KILIÇ as your Weixin contact」；图 25 底 = 会话最底 **8/30 21:03**「understood」）= 语料 2,601 轮全区间视觉副本；图 26（10-06）= 88 台订单段（10/2 19:56→10/3 00:40，**已在库** = r13「877 图」OCR，aligned L10300-10326）；**26/26 张 = 0 新消息**；58MB 原图核验后删除（最小占用）—— 详见 `121-angora-master-reanalysis-2026-10-21.md` §1

### 7.7 INFO_2025.12.17（12 项 + STH-8C48DX 子夹）——CENTEC L3 方案包
- ⭐ **VastLakes（25G）+ PeakNetX（10G）平台 Performance pptx ×2**（CENTEC 芯方案评估材料）
- **STH1G / STH25G Series Switches Datasheet pptx ×2** + STH-8C48DX 子夹（CENTEC STH 产品线）
- **ANW-DC-RFP-EN.pdf**（数据中心 RFP 模板）+ CENTEC web gui.jpg
- CLI Manual.docx 2.7MB / User Manual.docx 12.4MB / Web Manual.docx（CENTEC 平台文档，大文件抽取截断，头尾已用）
- **INFO.rar 51.4MB 仅索引不下载**
- 意义：2025-12 已备好 CENTEC 材料 → 2026-08-17 回复「CENTEC L3 功能全有」= 方案已落地

## 8. 完整文件索引（317 项，按文件夹；状态：📖=已读全文 / 📋=仅索引（二进制/legacy/大文件）/ 🔒=PII）

### 根夹（23 文件 + 13 文件夹）
| 文件 | 大小 | ID | 状态 |
|---|---|---|---|
| Reply on SAGA Enterprise L3 Recommendation Report.docx | 1.08MB | 1AL8bt2gt-j3x_t5Ok63p2mn8rcm1dx6w | 📖 |
| SAGA Enterprise L3 Recommendation Report.pdf | 153KB | 1UNUYhtACxZPQ1xGnMGG7EmzrhWoNNZN8 | 📖 |
| Turkey Client List.xlsx | 25KB | 1D7ZlLL_zr7XVpZUXAVeX0L_qOHDGNUIK | 📖 |
| 成本统计.xlsx | 16KB | 1g7TJ4dSUApljoF8TObv9uz75FrbTZr5F | 📖 |
| 运费一览表.xlsx | 10KB | 1_Z8ykzUUTvsVV_ZW0Aw7KvLPqiZLwd2f | 📖 |
| mac_address&serial_number.xlsx | 28KB | 1o--dzqS6SVrKDwv3yepCIl2cyH_GrCP6 | 📖 |
| 加深关系绑定.docx | 94KB | 13AogQWLopYRYuNSahotaDFxAm17dkyw7 | 📖 |
| Connexite-Amazon-Biz-Plan-DRAFT.pdf | 393KB | 1F9e0d9cr3SWZqJfCZaf9bPYIDb54vXAa | 📖 |
| ANGRA TICARET SICIL 11 MART 2024.pdf | 40KB | 1lWs7LCoy5jKGbVAQghZOXWFX9oPJ8RnH | 📖 |
| Proposal.docx | 410KB | 1j-RTecTU0iDnJ57YXR1TG-1w-MXXVDkE | 📖 |
| Agenda for WeChat meeting at 2024.10.31.docx | 419KB | 13V2LsW-pucmc8F9O3HWhqQbV4w8SNomZ | 📋 |
| Key Points in WeChat meeting at 2024.10.31.docx | 51KB | 1qd8IdYFNxkS8Vm3xn39LAfyWNIkwNTLw | 📖 |
| Agenda for WeChat meeting at 2025.docx | 226KB | 19nLkDZ5vZKeLmIeAX8AZjnwwDB7HI-V- | 📋 |
| TRY.xls | 5.56MB | 1j6pPhNVDdLDRPXfjHCbtIHyaMGKbb9iY | 📋 legacy |
| Quotation_48 port switch 150pcs.xls | 173KB | 13iN_5AoCKJKasNlNG-D2piQnKsPLSJoV | 📋 legacy |
| Quotation_5电口 工业MC.xls | 172KB | 159Rp1N3Ey-0TlSGFtCALXYwxzPogmJ9T | 📋 legacy |
| PVCs.xlsx | 229KB | 1As2x_3NHkYUOmn5ZWJGuNVuAdLjBp_UR | 📋 |
| PCB板带LOGO.png | 790KB | 1eYIdG6WaGBeP3R3WXphujArPfkOD4cw5 | 📋 |
| trontx.png | 116KB | 1hHlUNpiLzEfvKjRIPwIahxoQHiDyjo3t | 📋 |
| ANGRA LOGO2.ai | 1.13MB | 1XIieUXtc43DS3Al1ewy7d4eVUNCahMBS | 📋 |
| Black TRONX.psd | 89KB | 1TypmtKfUYrSd0O-HAigpGmi8pzcPD4Ak | 📋 |
| White TRONX.psd | 167KB | 15VrSSDx02xtB4e9zV4B8ADizxjyeXAQe | 📋 |
| LK-Passport-chip.pdf | 635KB | 1VIBdgXuC63CDYP9nrt0HID2uK99xAKLA | 🔒 PII |
| 文件夹 ×13：1st~6th order / RFP / IoT Board / INFO_2025.12.17 / Karen工业模块测试结果 / WeChat Talk / 未付款1 / 警察局项目 | — | 1Ipewa…/1DWyCZ…/1H_Mb6…/1X84CG…/1euKws…/1-N-Qd…/196m4Z…/1L1Lkm…/1mmBio…/16dnjD…/1xN0oG…/1mI0H3…/1BeELd… | — |

### 1st order 夹（13 项：出货 9 + 文件 12）
WE02405009117 FedEx 运单标签.pdf(46KB,1knD1ub3Dwy2IE7kuC2xw5X57xuWzhk_B) / PL P-24051001.xls(274KB,1r-5WeZE…) / 货款支付记录.jpg(60KB,1nnBsT58…) / 伊博 P20240510-01 未税6000RMB.doc(1.56MB,1YvUPrMy…,legacy) / CI.xls(177KB,12dQ8qeF…) / 采购合同.xlsx(144KB,1LzVjleb…) / 采购合同.pdf(177KB,1lpxEECC…,📖) / 银行报文.jpg(444KB,1uVwW5qO…) / 水单 5.8.pdf(92KB,1y_O6_WT…,📖) / STSC20240508007.pdf(131KB,140VYGZH…,📖) / logo.png(69KB,1QKQ_kHL…) / Quotation.xls(171KB,1udlhT2h…,legacy) / 出货夹(1dkPPKnj…)：ANW-3148-PX、ANW-3124-PX、ANW-3108-PG 照片子夹 ×3 + Certificate of Warranty.psd(5.17MB) + 普通快递发票.xlsx(12KB) + after/before log-in.png + 8口.jpg(5.6MB) + 24口.jpg(4.7MB)

### 2nd order 夹（30 项）
采购合同_STSC20241021007.xls(1.63MB,legacy) / 采购合同_STSC20241105007.xls(1.46MB,legacy) / STSC20241021007.xls(5.77MB) / STSC20241028007.xls(259KB) / STSC20241105007.xls(707KB) / 伊博 P20241026-01 净5624 已签章.pdf(📖,1IpYo6lL…) / 伊博 P20241106-01 未税2250 已签章.pdf(📖,16ewK4HA…) / Certificate of Warranty.pdf(803KB,纯图无文本层) / .psd(5MB) / PL.xls(148KB) / CI.xls(6.08MB) / 装箱单PL.xls(274KB) / awb.png / 货款支付记录 1/2/3.png / shipping mark.png / ANW-1108-V label.png / ANW-2116-PG label.png / ANW-1108-V User Manual.pdf(📖)+.pub(6.7MB) / ANW-2116-PG User Manual.pdf(📖)+.pub(3.7MB) / PVC.png / label format.jpg(2.28MB) / GUI after change.png / Angora-Replies_2024.10.23.docx(1.26MB,📖) / STC-448DGGPM.cdr / STC-424DGGPM-280W.cdr（TronX 图稿）/ 出货夹(1W2dk8N6…)：ANW-1108-V、ANW-2116-PG 照片子夹 ×2 + WE02411006486 入库标签.PDF + 深圳联邦UPS报关资料.xls + 普通快递发票.xlsx

### 3rd order 夹（19 项）
STSC20250117007.xls(5.91MB) / 伊博 P20250303-01 未税265220RMB.doc(legacy) / Packing List.xls / Payment Receipt.pdf(📖) / 货款支付记录 1-6.png / Reply on RFP 2024.12.10.docx(📖) / Reply on 174 pieces of ANW-2116-PG-ANW.docx(📖) / Info to be provided-Angora.docx(3MB,📖) / lite-hotfix-7.3.13.bin(62MB) / 子夹 ×5：Sample Confirmation(9 图) / 采购_Smartbyte(报价+LT-IS6318GP User Manual📖) / Shipment Info(WE02503002566 + CI_R1 5.9MB + 标签 5MB + 视频×4 + 照片×4 + 发票) / TT-2116-PG.zip(158KB) / 采购_Yingjiao 2 样品(出货 3 照片)

### 4th order 夹（17 项）
采购合同_STSC20250507007.xls(559KB) / STSC20250507007.xls+R1(488KB×2) / 伊博 P20250508-01 未税8190RMB.doc(legacy) / PL+装箱单+买单报关.xls / 普通快递发票.xlsx / WE02505007424 入库标签.PDF / User Manual(📖608KB) / 货款支付记录 1/2.png / awb.png / Certificate of Warranty.psd(5.39MB) / 子夹 ×3：ANW-2224-PX(8 图) / ANW-2248-PX(6 图) / **Unshipped(12 项 = 4th-pre 单 STSC20250228007 全套 + 出货照片夹)**

### 5th order 夹（12 项）
采购合同_STSC20250526007.pdf(📖279KB)+.xls(537KB) / STSC20250526007.xls+R1(490KB×2) / 伊博 P20250530-01 未税14630RMB.doc(legacy) / Packing List.xls / User Manual(📖608KB) / TronX Commercial User Manual.pub(3.68MB) / label confirmation.docx(📖) / 货款支付记录.png / Certificate of Warranty.psd(5.3MB) / Shipment Info 夹(14 项)：WE02506006381 入库标签 + CI.xls(489KB) + PL + 报关 + 发票 + awb + **TRX-AS-24TP4X.zip/48TP4X.zip + TronX User Manual_reference only.pdf + TRX web gui/log-in.png** + ANW-2224-PX/ANW-2248-PX 照片子夹 ×2

### 6th order 夹（13 项）
采购合同_STSC20250619007.pdf(📖331KB)+.xls(1.1MB) / STSC20250619007.xls+R1(5.55MB×2) / 伊博 P20250624-01 未税4272RMB.doc(legacy) / User Manual(📖445KB)+.pub(6.72MB) / **STI-288DGGPM drawing.dxf(18.7MB)/.ai(1.06MB)/.pdf(322KB)** / 货款支付记录.png / Certificate of Warranty.psd(5.08MB) / Shipment Info 夹(15 项)：WE02506020141 入库标签 + CI.xls(5.55MB) + PL + 报关 + 发票 + awb + 照片 1-9

### 未付款 1（4 项）
STSC20241129007.xls(12.66MB,legacy) / Quotation.xls(176KB,legacy) / Tronx Saga Siparis Listesi-3.xlsx(78KB,📖) / Tronx Saga Siparis Listesi Smartbyte报价.xlsx(11KB,📖)

### RFP（16 项）
2024.5.27_RFP.xlsx(📖87KB) / RFP_2024.5.9/5.27/6.15/7.2/12.11/2025.1.30.docx(📖) / 2024.6.15_TT-RFP-EN.pdf(📖) / 2024.7.2_ÇTIPI ETHERNET ANAHTAR KGYS.pdf(📖) / Sftp reply_2024.7.11.docx(📖) / R&D period&cost_2024.7.12.docx(📖) / 第一次+第二次沟通_RFP_2024.6.15.mp4(85MB+32MB,📋) / RFP_SFTP check List_2025.2.5.docx(📖) / Turk_Telekom_Test_Items.xlsx(📖) / Saga Software Function List-release 7.3.0.xlsx(📖)

### 警察局项目（8 项）
EGM.txt(📖5.2KB) / KGYS.txt(📖2.9KB) / ÇGKS.txt(📖5.5KB) / KGYS_Section33_Translation_EN.pdf(📖) / CGKS_Section_3.3_Network_Switches_EN.pdf(📖) / EGM_Sections_3.3_3.4_EN.pdf(📖) / Turkey_Police_RFP_Compliance_Template.xlsx(📖) / CGKS_Field_Switch_DLink_DIS300G_Compliance.xlsx(📖)

### IoT Board（4 项）/ Karen（4 项）
PCB.jpg / IoT Prototype.jpg / SC0012-000.pdf(📖2.14MB) / PC0012_Saga.7z(9.3MB,📋) ｜ testing port 1/2.jpg / -40 degree.jpg / +75 degree.jpg（温度测试照）

### WeChat Talk（26 项）
Weixin 截图 ×26（2026-09-23 22:34~22:52 ×25 + 2026-10-06 17:25 ×1）—— 图片未 OCR（下轮候选，与 01-knowledge-base wechat 语料 2026-10-03 末条衔接）

### INFO_2025.12.17（12 项 + STH-8C48DX 子夹）
Performance of VastLakes Platform_EN.pptx / Performance of PeakNetX Platform_EN.pptx / STH1G Series Datasheet_EN.pptx / STH25G Series Datasheet_EN.pptx / Saga Software Function List_EN.pptx / ANW-DC-RFP-EN.pdf / CLI Manual.docx(2.7MB) / User Manual.docx(12.4MB) / Web Manual.docx / CENTEC web gui.jpg / **INFO.rar(51.4MB,📋 不下载)** / STH-8C48DX 子夹（CENTEC STH 产品线）

## 9. 边界与限制（诚实声明）

1. **legacy `.xls`/`.doc`（~15 份合同/发票）API 无法抽取** → 行项级数据以已读 PDF 合同 + 发票文件名金额 + 成本统计表为准；合同-发票-成本表三方对平 6/6 通过
2. **图片/视频/PSD/DXF/ai/7z/RAR/zip（~150 项，≈180MB+）一律不下载**（用户指令：最小存储占用）→ 只索引；WeChat Talk 26 图 + Karen 4 图未 OCR
3. **LK-Passport-chip.pdf = PII**：仅索引不抽取
4. 大 xlsx/docx 抽取截断（中段省略）：数据行在头部，已用；纯图片 PDF（Certificate of Warranty ×6 单）无文本层
5. 9 个照片子夹（1st/出货×3、2nd/出货×2、4th/Unshipped/出货照片、5th/SI×2、INFO/STH-8C48DX）内容 = 产品/包装照片，未展开计数
6. 7th 单合同/发票未在 Drive 上传；4th-pre 单状态以 Drive 快照为准（未出货）
7. TronX $1,480 = 未付款 PASSED 项：仅登记不催款（r13 已定）

## 10. 与前序档案交叉引用

- `05-turk-telekom/10-tt-relationship.md` + `01-knowledge-base/2026-08-17-l3-strategy-official-reply.md` = TT 通道 + L3 战略（本档案 6th/7th 单 = 其物理落地）
- `07-tenders/10-tender-bidding-dossier.md` + `01-knowledge-base/wechat-2026-business-digest.md` = EGM 3,294 台（本档案 7.2 节 = 规格原文）
- `03-import-data/20-angora-import-records-2026-10.md`（r13）= 海关视角 45 票；本档案 = 合同视角 9 单；「15.4 个月零落单（末单 2025-06-19）」**更正为：末单 = 6th 单 2025-06-19 正确，但 7th 单 2025-07-11（MAC 表）+ 4th-pre 未出货单表明链条未断**
- `06-competitors/110-turkey-local-competitors.csv` 行 1（PNetworks）：TT 贴牌通道 vs PNetworks-Edgecore 白牌同构对照
- `06-competitors/97-turkey-anchor-strategy-marvell-route.md`：Marvell 护城河论述（本档案 7.4 节 = 用户方 2026-07-20 内部文档原文）
- `06-competitors/95-smartbyte-price-trend-2024-vs-2026.md`：SmartByte 价单（本档案 = 实际成交价的 9 个锚点）
