# r95 外部证据逐源文本清单

本目录 **每个来源 URL 一份文件**；不合并来源，不覆盖历史资料。以下为网页/PDF 经 `fetch_page` 生成的全文本抽取并逐份保存（行末空格标准化），**不是源网页 HTML 或原始 PDF，非 byte-identical**；图片、格式及工具 OCR 可能丢失或误识别。标为“完整”仅指保存工具可见的全部文本分块，不代表付费墙后的数据可见。取回了多块的材料按来源顺序在同一个同源文件拼接；不会拼入其他来源。

时间警告：本会话业务日期为 **2026-10-26 UTC**；实际工作环境 `date -u` 显示 **2026-11-19**，与会话日期不一致。这是系统时钟冲突，网页访问不能被证明是 10 月 26 日的历史快照；报告把有确切的文件日的资料按文件日记载，无历史版本证据的页面只记本次观察。

| 序号 | 来源原 URL | 本地相对文件（保留主机和路径） | 文件大小（bytes） | 本地抽取文本 SHA-256 |
|---|---|---|---:|---|
| 1 | <https://find-and-update.company-information.service.gov.uk/company/14770313/filing-history/MzQwNTY1NDQzMmFkaXF6a2N4/document?format=pdf&download=0> | `find-and-update.company-information.service.gov.uk/company/14770313/filing-history/MzQwNTY1NDQzMmFkaXF6a2N4/document.pdf.extracted.md` | 1751 | `d541ce3c81744253e5fadec287453f131685e0af4d4d3bbf41f46571180c5ffc` |
| 2 | <https://find-and-update.company-information.service.gov.uk/company/14770313/filing-history/MzQyNzc4MTAzM2FkaXF6a2N4/document?format=pdf&download=0> | `find-and-update.company-information.service.gov.uk/company/14770313/filing-history/MzQyNzc4MTAzM2FkaXF6a2N4/document.pdf.extracted.md` | 1585 | `06153eb66fa23f57d3e7c36b56ed1370ce849308d2a4fcbc0e076e444c03a31d` |
| 3 | <https://find-and-update.company-information.service.gov.uk/company/14770313/filing-history/MzQ5MzU5OTYwNWFkaXF6a2N4/document?format=pdf&download=0> | `find-and-update.company-information.service.gov.uk/company/14770313/filing-history/MzQ5MzU5OTYwNWFkaXF6a2N4/document.pdf.extracted.md` | 1692 | `8fde1a527941e184f3f859cd359cdac799d3c1fe70a2b1a5824b64a971161931` |
| 4 | <https://www.angoranetworks.com/download/1015/> | `www.angoranetworks.com/download/1015/index.extracted.md` | 3294 | `3a71dd209ec83786e32dd9876620fb3118d6fe475ce3fc68f26ce915d46b9371` |
| 5 | <https://www.angoranetworks.com/download/1027/> | `www.angoranetworks.com/download/1027/index.extracted.md` | 2767 | `be56b63327e6d12ee449b3013d10e9f1862f22ae6c142e7644e7cae97257b216` |
| 6 | <https://www.angoranetworks.com/download/1031/> | `www.angoranetworks.com/download/1031/index.extracted.md` | 3246 | `b8e341ab395df3f7aff0bd2fb37280db3ef187d00338f027655d417bdb1b33b1` |
| 7 | <https://www.angoranetworks.com/download/1035/> | `www.angoranetworks.com/download/1035/index.extracted.md` | 2748 | `68a8b9c6c009fee9ef207c4c04d0befe79f5d9cae2a11f8e6366ca5a70061652` |
| 8 | <https://www.angoranetworks.com/download/1039/> | `www.angoranetworks.com/download/1039/index.extracted.md` | 2568 | `ae6cd19f99776285e2a94401eab2e6683fb167ce90c823f4e57b2f64ebd40244` |
| 9 | <https://www.angoranetworks.com/download/1053/> | `www.angoranetworks.com/download/1053/index.extracted.md` | 2312 | `bc54a7cd0e6a0b7b9c6126072a2521733e0ea2ac0e904a5f7fb3c643711a605c` |
| 10 | <https://www.angoranetworks.com/26/files/Angora-Datasheet-SFP100G-20210330.pdf> | `www.angoranetworks.com/26/files/Angora-Datasheet-SFP100G-20210330.pdf.extracted.md` | 8267 | `78a2843b1366bcf4c5b725c3fbc273a5eee293e87d03b7e62160ebd67a95a7c7` |
| 11 | <https://www.turkeytradedata.com/company/angora-networks-bilisim/4da8548afd70d79878456c8e21724f57> | `www.turkeytradedata.com/company/angora-networks-bilisim/4da8548afd70d79878456c8e21724f57/index.extracted.md` | 11755 | `5096f7c0f879d3cdc26d6d418c55bd23d55f29019f63757b751a875ecb35e720` |

**全量读取完成：本目录已保存 11 个来源 URL 的完整可见抽取文本，11 份独立文件；0 份合并；0 份原始网页或 PDF 二进制。**
**未计入**：只读片段的搜索索引、超出本轮范围而未归档的页面、失效请求、以前已经入库的原始附件。它们在报告中按各自证据等级单列，不冒充全文归档。
**局限**：TurkeyTradeData 的 “Unlock” 表示付费锁定，不能称取到全部交易；图表文本的数字位置未必可靠。2024 土耳其公报原始扫描件本会话未再次取得，仅可引用仓库 OCR，并需要目视核验。
