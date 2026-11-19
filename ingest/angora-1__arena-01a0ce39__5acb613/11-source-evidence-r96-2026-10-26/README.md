# r96 · 来源与产物全量清单（逐源，不合并）

**计数范围**：本轮单独保存 **15 个不同 URL 的工具可见文本产物**（每 URL 一文件，其中 12 份为网页/PDF 可见文本人工转录、1 份为 LinkedIn 工具结构化结果、2 份分别复用已保存规范化文本并按章节比对）；另有 **3 个固定 GitHub commit 的原样镜像文件**（2 份 CSV + 1 份更新时间元数据）、**1 份搜索片段**（另一个 URL，不是全文）及 **5 张从两幅既有 JP2 派生的图像**。因此为 **19 个不同 URL / 19 个对应源产物**，外加 5 张派生图，共 **24 个产物**；本 README 自身不计。URL 不等于互相独立的信息源，同一网站不同页面也可能共用底层数据。

**日期与读取**：会话给出的当前日期为 **2026-10-26 UTC**，并非用户另行指定的历史截止日；执行时沙箱 `date -u` 显示 **2026-11-19 UTC**，两者不一致，实际采集日不能单靠环境时钟独立确定。文章日期、历史交易窗口和镜像 commit 日期分别注明；动态页面只记本轮所见，不能断言属于某一历史日期。晚于会话当前日期的材料保留，但不能据此当作截至该日已发生的事实。

**证据级别**：固定版本的 GitHub 镜像是第三方副本，可证明该 commit 下的文件内容，非直接获得的 IEEE 原站文件；客户合同/发票/回单是既有资料的文字抽取，须与原件及银行/物流记录复核；厂商网站是自述，媒体引述是报道或受访者自述，贸易聚合是未经本轮逐票审计的样本，搜索片段只是线索。等级只描述可支持的结论，不为厂商技术、持股或营收背书。

**格式限制**：下表“工具可见文本”包括手工转录、规范化、分块拼接与可能的换行处理；本轮按篇章、重要数字和部分页面首尾检查，但**未作对工具响应的全量逐字节对比**。图片、布局、部分 OCR、JS、墙后内容与超出工具 PDF 处理上限的页面均可能缺失，不能称原文原件或已读墙后全文。两份复用内容尤其不宣称两个 URL 的 PDF 字节相同；LinkedIn 是第三方结构化结果。文件 SHA-256 是**本地保存产物**的完整性指纹，不是远端 HTML/PDF 的哈希。仓库根 `.gitattributes` 对本证据目录禁用 Git 自动换行转换，以保留 CSV 的 CRLF 和文本产物现有字节；每次取用仍应核对哈希。网页可能变化，广告尤可能变化。

**检索日志边界**：19 个 URL 仅指本目录实际存下的来源产物，并非本轮所有搜索结果、未成功请求及工具响应的完整日志；部分早前搜索输出未逐条落盘，现有接续材料不能重建其全部原文。报告中使用的旧证据指向既有独立档案；未保存或不可读的响应不得计成已归档全文。

## 一、工具可见文本逐 URL 清单（15/15）

| # | 来源 URL | 本地相对路径 | 采集范围、材料日期及限制 | 大小（bytes） | 本地 SHA-256 |
|---:|---|---|---|---:|---|
| 1 | <https://ictmedia.com.tr/haber/angora-networks-kanal-ortaklari-zirvede-bulusuyor> | [ictmedia.com.tr/haber/angora-networks-kanal-ortaklari-zirvede-bulusuyor/index.extracted.md](ictmedia.com.tr/haber/angora-networks-kanal-ortaklari-zirvede-bulusuyor/index.extracted.md) | 2 块；2022-10-18 预告；媒体报道，非活动授权书 | 14574 | `98fb83fbc39996e2dea7ce4e57b7e6239669305e1e59c19145e4bf0ac61bd4fd` |
| 2 | <https://ictmedia.com.tr/haber/yerli-bir-ureticiye-verilebilecek-en-buyuk-destek-onun-urunlerini-kullanmaktir> | [ictmedia.com.tr/haber/yerli-bir-ureticiye-verilebilecek-en-buyuk-destek-onun-urunlerini-kullanmaktir/index.extracted.md](ictmedia.com.tr/haber/yerli-bir-ureticiye-verilebilecek-en-buyuk-destek-onun-urunlerini-kullanmaktir/index.extracted.md) | 4 块；2023-06-08 专访；动态推荐不属采访事实 | 33514 | `b1a8bf492971465c1197a744c0778a2c1168e5f7964c54a4e20ff7200bc06bb3` |
| 3 | <https://maclookup.app/macaddress/70b3d5822> | [maclookup.app/macaddress/70b3d5822.extracted.md](maclookup.app/macaddress/70b3d5822.extracted.md) | 1 块；第三方 MA-S，2019 日期为该站自述 | 2761 | `cbf475c6053fc8c73023202e9cc4ca5c01433403224f6c2bcfec25d50016afe6` |
| 4 | <https://maclookup.app/macaddress/980637a> | [maclookup.app/macaddress/980637a.extracted.md](maclookup.app/macaddress/980637a.extracted.md) | 1 块；第三方 MA-M，2019 日期为该站自述 | 2459 | `27368d48677395bd290ea29d21a3bbb2f2a69305ca14e2bb426133106f66e003` |
| 5 | <https://www.angoranetworks.com/26/files/ANGORA-IRIS-SFP-DATASHEET_EN-1.pdf> | [www.angoranetworks.com/26/files/ANGORA-IRIS-SFP-DATASHEET_EN-1.pdf.extracted.md](www.angoranetworks.com/26/files/ANGORA-IRIS-SFP-DATASHEET_EN-1.pdf.extracted.md) | 1 块；厂商 PDF 工具文本；非 PDF 二进制 | 6565 | `8f0c228a1df763e7ee9c058997f0608177b0f4f062deba58530c2b00689c9114` |
| 6 | <https://www.angoranetworks.com/26/files/ANGORA-IRIS-SFP100-DATASHEET-20210423.pdf> | [www.angoranetworks.com/26/files/ANGORA-IRIS-SFP100-DATASHEET-20210423.pdf.extracted.md](www.angoranetworks.com/26/files/ANGORA-IRIS-SFP100-DATASHEET-20210423.pdf.extracted.md) | 1 块；文件名为 100G 但返回 1G/10G；复用规范化文本，非逐字节 | 6673 | `9c1f8cb65ef16013dba9ecfc91b92aa16389ef18cdcd6b57566550a6d7ca348e` |
| 7 | <https://www.angoranetworks.com/26/files/ANGORA-IRIS-SFP25-DATASHEET-20210423.pdf> | [www.angoranetworks.com/26/files/ANGORA-IRIS-SFP25-DATASHEET-20210423.pdf.extracted.md](www.angoranetworks.com/26/files/ANGORA-IRIS-SFP25-DATASHEET-20210423.pdf.extracted.md) | 1 块；厂商 25G PDF 文本；文件名日期不等于确证发布日 | 4033 | `6c10aae0129a9aec314c95f7531fee4c32200621403b2189e39f963d3c1e22ac` |
| 8 | <https://www.angoranetworks.com/26/urunler/> | [www.angoranetworks.com/26/urunler/index.extracted.md](www.angoranetworks.com/26/urunler/index.extracted.md) | 1 块；厂商动态产品索引；非历史快照 | 3593 | `0273d1a4cc78dcc7b78408f6ac67f867428f218bd145855792e6dc08db2aa5ee` |
| 9 | <https://www.angoranetworks.com/26/urunler/iris-sfp/> | [www.angoranetworks.com/26/urunler/iris-sfp/index.extracted.md](www.angoranetworks.com/26/urunler/iris-sfp/index.extracted.md) | 1 块；厂商动态 Iris 页面；五个规格非全部 SKU | 3665 | `7ed2999cce92897bfcfcbcbca2be37b9152f8bdfbe73cede0bda21910e3ecbfb` |
| 10 | <https://www.angoranetworks.com/angora-networks-completed-the-cisco-ise-integration/?lang=en> | [www.angoranetworks.com/angora-networks-completed-the-cisco-ise-integration/index.en.extracted.md](www.angoranetworks.com/angora-networks-completed-the-cisco-ise-integration/index.en.extracted.md) | 1 块；厂商自述 2021 ISE 项目；非独立测试 | 6441 | `f8ed928ca5d9d73eda6cc206bb3fb7c8708abad91675a71f400b0b5b96e49086` |
| 11 | <https://www.angoranetworks.com/angora-networks-completed-the-cisco-ise-integration-2/?lang=en> | [www.angoranetworks.com/angora-networks-completed-the-cisco-ise-integration-2/index.en.extracted.md](www.angoranetworks.com/angora-networks-completed-the-cisco-ise-integration-2/index.en.extracted.md) | 1 块；厂商 PacketFence 文，标题与首段 Cisco 日期冲突 | 6136 | `2d8daa1ed900acba0b202aee449fcd8090239fde8a0ba08fbce5b25e2cbfa32e` |
| 12 | <https://www.angoranetworks.com/qr/10203/ANW-IRS100-DS-EN.pdf> | [www.angoranetworks.com/qr/10203/ANW-IRS100-DS-EN.pdf.extracted.md](www.angoranetworks.com/qr/10203/ANW-IRS100-DS-EN.pdf.extracted.md) | 2 块；与 r95 100G 规范文本按章节核对后复用，非 PDF 字节比较 | 8753 | `a4f6ba9f6e56ee056765d3921446a639722e88626d44e88a24655d320da12a99` |
| 13 | <https://www.angoranetworks.com/verge-network-switch-serisi/> | [www.angoranetworks.com/verge-network-switch-serisi/index.extracted.md](www.angoranetworks.com/verge-network-switch-serisi/index.extracted.md) | 1 块；厂商 VERGE 动态页面；Gordion 配置需按 SKU 核 | 5598 | `89a14a75c29dc12e3ed078819438f735a046cd90f3cebb457adb2d63ed0f36af` |
| 14 | <https://www.linkedin.com/company/angora-networks> | [www.linkedin.com/company/angora-networks/index.extracted.md](www.linkedin.com/company/angora-networks/index.extracted.md) | 1 块；结构化工具结果而非网页原件；data build 2026-11-12，晚于会话给出的当前日期，时间待核 | 2833 | `d5abb285f771c28f11b623909a188667c20160694817343467e4876806601d6d` |
| 15 | <https://www.turkeytradedata.com/search/im/imp/co-angora-networks-bilisim-teknoloji-ticaret-sanayi-anonim-sirketi> | [www.turkeytradedata.com/search/im/imp/co-angora-networks-bilisim-teknoloji-ticaret-sanayi-anonim-sirketi/index.extracted.md](www.turkeytradedata.com/search/im/imp/co-angora-networks-bilisim-teknoloji-ticaret-sanayi-anonim-sirketi/index.extracted.md) | 1 块；第三方汇总；展示窗口 2023-08 至 2024-07；逐票锁定 | 2810 | `6fddcc85b951e3009911dc2f80b989d6d1deea8b49efd1386a348dc0f9deced8` |

## 二、历史固定版本的第三方镜像原样文件（3/3）

镜像仓库 `deepin-community/ieee-data`，固定 commit `4047c1278d20f3a576a98ce3baae3bb6e9d19508`；作者日期 2024-08-27、提交日期 2024-08-28，提交说明 `update ieee-data to 20240722`。两份 CSV 本轮分别重新从该固定版本获取并进行 SHA-256 比较一致，只有“同一固定 GitHub 镜像副本”的 byte-identical 验证，不能推广为与 IEEE 当前原始文件相同。`.lastupdate` 文件 Git blob SHA-1 与 API 所报相符，值 `1721654721` 换算 2024-07-22 13:25:21 UTC，仅是镜像元数据，不是两条地址分配的登记日。路径保留同一目录下不同文件，不合并。

| # | 固定版本 URL | 本地相对路径 | 大小（bytes） | 本地 SHA-256 |
|---:|---|---|---:|---|
| 1 | <https://github.com/deepin-community/ieee-data/blob/4047c1278d20f3a576a98ce3baae3bb6e9d19508/mam.csv> | [registry-copy/mam.csv](registry-copy/mam.csv) | 608108 | `b875206fa5b2ccd229bc61da781ea838df56c34511465f620c22a1a284a5618c` |
| 2 | <https://github.com/deepin-community/ieee-data/blob/4047c1278d20f3a576a98ce3baae3bb6e9d19508/oui36.csv> | [registry-copy/oui36.csv](registry-copy/oui36.csv) | 557084 | `07ee8fb2324a46282fbe8b5aaf99b7567514e174c02ab3794cb1c6124e018ce1` |
| 3 | <https://github.com/deepin-community/ieee-data/blob/4047c1278d20f3a576a98ce3baae3bb6e9d19508/.lastupdate> | [registry-copy/.lastupdate](registry-copy/.lastupdate) | 11 | `f2293212f935cf6b662802f9dbe1601a4042ca47940455e2740a0e600a4c5468` |

## 三、仅搜索片段（1/1，不纳入全文数）

| 来源 URL | 本地相对路径 | 内容范围与限制 | 大小（bytes） | SHA-256 |
|---|---|---|---:|---|
| <https://fliphtml5.com/kfal/gevh/05-ICT_MEDIA_MAYIS_2025/> | [fliphtml5.com/kfal/gevh/05-ICT_MEDIA_MAYIS_2025.search-snippet.md](fliphtml5.com/kfal/gevh/05-ICT_MEDIA_MAYIS_2025.search-snippet.md) | 搜索工具返回的一个结果片段，含省略号和 OCR 错误；非整本期刊，34–36 页直链均显示 Page Not Found；人物职务待核 | 3979 | `bf9664995057b8f9d62cf613fb7ce3209dbcbea4b7603f74683df5c6be7ae45b` |

## 四、公报内嵌图的派生图（5/5）

两幅源 JP2 已存于 [`../05-nontext-content/pdf-scan/ANGORA TICARET SICIL 11 MART 2024 .pdf/`](../05-nontext-content/pdf-scan/ANGORA%20TICARET%20SICIL%2011%20MART%202024%20.pdf/)，是抽取出的内嵌图像，并非完整原 PDF 或完整页面；5 张 PNG 仅为转换与颜色通道拉伸的观察副本。目视均不可读。下表哈希为 PNG 派生文件，不可与原 PDF 哈希混同。

| # | 本地相对路径 | 来源 | 大小（bytes） | SHA-256 |
|---:|---|---|---:|---|
| 1 | [visual-register/page-01-img-01-blue-stretched.png](visual-register/page-01-img-01-blue-stretched.png) | `page-01-img-01.jp2` 派生 | 15510 | `3a6f9ecb652b9634260e24edcb3c33a0953cbbc0db35f1381ec4a0c7a649122a` |
| 2 | [visual-register/page-01-img-01.png](visual-register/page-01-img-01.png) | `page-01-img-01.jp2` 派生 | 10484 | `20017cb1ba2c069b4042bd202c3db240288993cdb23c932d3528d2a6d8fa2895` |
| 3 | [visual-register/page-01-img-02-blue-stretched.png](visual-register/page-01-img-02-blue-stretched.png) | `page-01-img-02.jp2` 派生 | 44136 | `8f7f04884df68ed945674ed79c3e2195c623b7a7bbfd420b660ad3077ab57fdc` |
| 4 | [visual-register/page-01-img-02-green-stretched.png](visual-register/page-01-img-02-green-stretched.png) | `page-01-img-02.jp2` 派生 | 37844 | `1d98325db3f3cae5a6cc0dac937344ac415e1b0298a6fbb06aafcf2e3beb2141` |
| 5 | [visual-register/page-01-img-02.png](visual-register/page-01-img-02.png) | `page-01-img-02.jp2` 派生 | 147780 | `8ec63fb641f8aabb5566ccaa1ecc9cde8c584e823476af3dd8da84953b00f901` |

## 五、已知但未逐 URL 归档的检索 / 尝试（仅元数据）

以下条目只根据接续摘要登记已知 URL 或失败尝试，**没有本轮独立保存的完整工具响应**，不计入上面的 19 个来源产物；摘要也不足以还原所有检索或每次返回结果。历史已有单独材料不与这些条目合并。

| 已知 URL / 尝试 | 已知范围与缺口 |
|---|---|
| <https://find-and-update.company-information.service.gov.uk/company/14770313/filing-history> | 英国法人申报历史页；r95 单独保存三份申报 PDF 的文本抽取，但本轮没有该索引页的独立完整响应 |
| <https://www.volza.com/company-profile/angora-networks-informatics-technology-trade-industry-joint-stock-company-54698404/> | 第三方贸易概览线索；原页受限，未取得墙后逐票或保存本轮完整响应 |
| <https://www.angoranetworks.com/angora-networks-egm-trafik-sekillendirme-gereklilik-testlerini-gecti/> | Angora 的 EGM 相关自述；本轮未保存该页完整响应，不是原始证书 |
| <https://www.youtube.com/watch?v=I5kDVMWC79I> | 历史 KOZ 视频线索；本轮未单独保存完整视频或工具响应，不证明现售 |
| <https://www.youtube.com/watch?v=jrdoTa5owZk> | 历史 KOZ 视频线索；本轮未保存完整视频或工具响应 |
| <https://github.com/20214703018-A/endeks3/releases/tag/warehouse-pdf-11> | 公报第三方存档线索；是否含 2024-03-11 第 11040 期未证，本轮未保存页面完整响应 |
| <https://www.gebzeto.org.tr/tescil-ve-uyelik/belge-hizmetleri/ticaret-sicil-gazetesi> | 商会取件说明线索；本轮未保存完整响应，不代表已取得目标公报 |
| `fliphtml5` 期刊的 `page34.html`、`page35.html`、`page36.html` 访问尝试 | 接续记录为 Page Not Found；完整请求 URL 和逐次响应未单独保存，已保存的是上方期刊搜索片段，不是期刊全文 |

**全量读取完成（限定本清单的已归档产物）**：15/15 选择的 URL 可见分块已有独立保存产物，3/3 指定镜像文件和 1/1 搜索片段入库，5/5 视觉派生图存在；0 个不同来源被拼为一个文件。此结论仅核对归档范围与文件数量，手工转录未做全量逐字节对比，也不代表图像、版式、付费墙或原 781 件材料在本轮均已完整读取。上表未归档的响应仍是缺口；r95 的 11 份是另一轮工具可见文本，本轮增加镜像、结构化结果及复用文本，统计口径和覆盖范围均不同，不能直接比全文阅读量。
