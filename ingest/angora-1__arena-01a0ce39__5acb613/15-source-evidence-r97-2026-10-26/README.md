# r97 · 来源清单与证据等级

## 使用边界

五个 URL 各保存一份 `fetch_page` 一块（1/1 chunk）的可见文字，按不同原 URL 分开；手工转录无逐字自动比对，**不是原始 HTML/PDF、不是 byte-identical，不含图片/OCR 未识别部分、不可见内容或付费墙**。会话日期 2026-10-26 UTC，沙箱时间晚于会话日期；动态页面只代表此次工具所见，无法证明其为 10 月 26 日历史快照。五项均属同一厂商资料，不能当五个独立主体的交叉证实。`download/1035/` 是 r95 同 URL 的重新读取，分别留存，不把其计作新的独立证据；网页、目录和手册之间可能复用同一宣传文本。5 个 URL 是本轮保存的可见响应数量，不是所有检索结果；搜索工具其他结果、未取到页面及未查看的图片不纳入全文计数。

| URL（逐源） | 本地可见文本 | 大小（bytes） | SHA-256（本地产物） | 性质 |
|---|---|---:|---|---|
| https://www.angoranetworks.com/angora-nms_en/?lang=en | [index.en.extracted.md](www.angoranetworks.com/angora-nms_en/index.en.extracted.md) | 4847 | `cb0239e81ff73534f02a3c10299502f17b2f5255848008e152805e2ef1ceda37` | 厂商英文网页；含非 Angora 设备管理自述 |
| https://www.angoranetworks.com/angora-nms/ | [index.extracted.md](www.angoranetworks.com/angora-nms/index.extracted.md) | 3002 | `99de27dbf2b90ecdf72d141637c9e192cf57490064eb234bfe1d57a2d9714bdb` | 厂商土语网页；100% 本土开发为厂商自述 |
| https://www.angoranetworks.com/download/1035/ | [index.extracted.md](www.angoranetworks.com/download/1035/index.extracted.md) | 3096 | `764b5294103641f80e20503513f002d427d1237fe8f325bf947736a1ec66044e` | 厂商手册文字层，r95 同 URL 曾采集；图文 OCR 可能错 |
| https://www.angoranetworks.com/brosurler/ | [index.extracted.md](www.angoranetworks.com/brosurler/index.extracted.md) | 2564 | `9666062a9cc8fc7bec1032031f5e2f9f16dc7a4828ba6898cd8f84a5484c4e7b` | 官网手册链接索引，不是现货证明 |
| https://www.angoranetworks.com/our-services-2/?lang=en | [index.en.extracted.md](www.angoranetworks.com/our-services-2/index.en.extracted.md) | 2298 | `e70175e3caaf8c38b75ca82276b7c0ce4e13dfa87c57ff4c6628ca808061672b` | 厂商服务/培训宣传，不是 SLA 合同或履约记录 |

## 本地原始目录、文本与元数据

- [首单/第二单全目录清单](local-first-second-inventory.csv)：原历史清单中 48 + 60 = **108 个源文件条目**；每行记录原相对路径、原大小及历史 SHA、逐文件对应产物路径、产物大小及本轮 SHA。不同文书不合并。
- 本轮对 108/108 对应产物完整读取字节并计算哈希，合计 **802,476 bytes**：32 个既有文本/图层抽取，76 个仅二进制元数据。**不等于 108 个原件被重新取得、图像被视觉读取或 108 件逐字审计**；源文件原始大小/哈希沿用历史 `FILE-INDEX.csv`，本轮不能验证缺失的源二进制。
- 另逐页回读 4 个既有邮件 PDF 文本抽取：`Gmail - layer 3 managed switch.pdf`（19 页）、`Gmail - Invoice_5pcs STC-424DGGPM-280W.pdf`（10 页）、`Gmail - Angora - Industrial RFP Question.pdf`（2 页）、`Gmail - TT switch administration guide.pdf`（2 页），合计 4 份、33 页文字层；它们的标题与原路径/字节数/哈希见下表。邮件 PDF 中 `[Quoted text hidden]`、附件及图片不是完整可读邮件内容。
- 已有微信对话是转录/对齐文本；相关段落按日期定位，未假称本轮访问 Google Drive、Gmail 或看到原截图。2024-11-28 商业方案、2025-01-17 PI 和 2024 RFP 的各自抽取仍在原目录，见报告逐项链接。
- 历史原件 `Certificate of Warranty.pdf` 没有可提取文字层；其 `.psd` 派生物只给图层名称，不能当完整证书。原付款截图仅元数据，不能把文件名当银行流水。

| 原邮件文件 | 历史原始大小（bytes） | 历史原件 SHA-256 | 本地文字产物大小（bytes） | 本地产物 |
|---|---:|---|---:|---|
| `Gmail - layer 3 managed switch.pdf` | 1114166 | `656c0f1272ce01bc8610ddadf44a200893838f757a54599552ae451bf3c410c6` | 31526 | [文本抽取](../02-extracted/Gmail%20-%20layer%203%20managed%20switch.pdf.extracted.md)；本地产物 SHA-256 `9b7f58bfeeec5e9677104b27a31c49ef5bc701e45abdbc51c2edeb942e4ac06b` |
| `Gmail - Invoice_5pcs STC-424DGGPM-280W.pdf` | 491784 | `45fd4cb058c867864c54333478a7e9db563bf2cdc028f69354fde0ea75376c8d` | 21905 | [文本抽取](../02-extracted/Gmail%20-%20Invoice_5pcs%20STC-424DGGPM-280W.pdf.extracted.md)；本地产物 SHA-256 `4c6c3ff1f4795bd32c6f57fd8d8c44c6e291730253ce2bb5b6e8ba96bc78dd9c` |
| `Gmail - Angora - Industrial RFP Question.pdf` | 169699 | `3dcfc7a44e51db258e0609018011bf899eafa18f91cc29960998306f8b414d18` | 5283 | [文本抽取](../02-extracted/Gmail%20-%20Angora%20-%20Industrial%20RFP%20Question.pdf.extracted.md)；本地产物 SHA-256 `0216660f33a89eea9761a0765d9686965f533d2def7f19f124461a8531ed8de9` |
| `Gmail - TT switch administration guide.pdf` | 128130 | `2e7b85d0d7724bbe995ce154ec60f2f11364e649b24456f780541272e7710dff` | 3567 | [文本抽取](../02-extracted/Gmail%20-%20TT%20switch%20administration%20guide.pdf.extracted.md)；本地产物 SHA-256 `942e047548161fb820ee891e4d572f7dbb5ae4a55b1c0a4d8809b02375838993` |

**全量读取完成（严格限定范围）**：上述首单、第二单 108/108 个既有派生文件完成完整字节读取与指纹计算；其中 32 为文字/图层提取，76 仅为元数据，未重取 108 个原始文件、未逐字审阅全部内容。4/4 选定的相关邮件提取逐页回读；5/5 上述 URL 的一块可见文字分别留存但未逐字校对。不是重新全量读取 781 个原件。
