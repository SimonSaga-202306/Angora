# r102 · Angora 品牌交付与标识追溯：限定来源

本轮聚焦 Angora 标签、设备序列号、MAC、界面与包装文书的证据链；不联系客户、不修改设备，不重启历史财务差异和旧项目。**每一阶段均先列该阶段路径与大小，再完整读取本地产物字节并计算 SHA-256**；逐字节读取不等于对所有内容逐项语义审计。各原始路径和派生文件分别保留，不合并客户或源记录。

## 全部限定来源的路径、大小及哈希

| 阶段 | 读取前的范围 | 完整字节读取清单 | 路径 / 本地字节 |
|---|---|---|---:|
| 既有目录、两份 Word 文本、标签/界面元数据、四份手册文字层及两份聊天派生 | [scope-before-read.csv](scope-before-read.csv) | [read-inventory.csv](read-inventory.csv) | 15 / 1,413,626 |
| 四张截图各自的对齐 OCR、另一 OCR 和原图元数据 | [supplement-ocr-scope-before-read.csv](supplement-ocr-scope-before-read.csv) | [supplement-ocr-read-inventory.csv](supplement-ocr-read-inventory.csv) | 12 / 236,997 |
| 第三单既有质保证书 PSD 文本派生，仅核序列号范围 | [supplement-certificate-scope-before-read.csv](supplement-certificate-scope-before-read.csv) | [supplement-certificate-read-inventory.csv](supplement-certificate-read-inventory.csv) | 1 / 2,545 |
| r96 固定版本 IEEE MA-M 镜像副本，仅查 Angora 前缀 | [supplement-ieee-scope-before-read.csv](supplement-ieee-scope-before-read.csv) | [supplement-ieee-read-inventory.csv](supplement-ieee-read-inventory.csv) | 1 / 608,108 |
| **合计** | 每组先列本组范围 | **29/29 唯一路径完整字节读取并哈希** | **29 / 2,261,276** |

另将 9 个旧报告、公司史及入口作为**分析背景**，在内容核对前保存[范围](context-before-read.csv)和[原前缀大小及 SHA-256](context-prefix-read-inventory.csv)，共 178,368 bytes；不计入上表 29 项。后续勘误只追加、保留旧前缀。

- [13 条原始资产路径交叉索引](asset-records-crossrefs.csv)逐项保留历史索引的路径、大小、SHA-256 和当前派生哈希；6 个图像/压缩包元数据 JSON 与历史索引核对一致。它们**不是本轮重取的 13 个原始资产**。
- [14 条 MAC 表行](mac-address-table-rows.csv)保留同一 Word 派生文档中两个表、各七行的原位置。两表值完全相同，只有七个不同地址；这些是文本记录，不证明 14 台设备，更不证明实际烧录或固定预留块大小。
- [29 条选定行锚](evidence-traceability.csv)、[15 条 OCR 日期边界索引](ocr-event-date-boundaries.csv)和[逐路径旧轮重合索引](overlap-by-path.csv)是分析产物，不替代各来源全文，也不增加原件数。29 条行锚对应选定论点，并非每个来源各有一条。日期边界索引逐条记录同一对齐 OCR 中事件行及其前后最近时间行；只用于限定日期范围，不把邻近时间、自动说话人标签当成原截图上的确定发言时间或主体。

## 不同来源形态与限制

1. 两份 Word 为先前 python-docx 文字抽取：原始 Word、其中图片、完整视觉排版及审批修订均未重取；问答段未必逐句标注讲话人。2025 文档页眉写 `2025/Q1`，不能把序列号字符当成经核实的实际生产日期。
2. 四份 PDF 是已有文字层，不是 PDF 原件或装箱证据。通用手册的包装清单与聊天中某次包装观察没有证明针对同一设备；无法据此判断哪一箱实际缺件。
3. 五个原始图像和一个 ZIP 目前仅有元数据：文件名、历史大小/哈希及部分尺寸可供索引，不提供图像像素、标贴文字、界面内容或 ZIP 成员载荷。`GUI after change.png` 是历史文件名，**不证明 GUI 已按要求成功更改**。本轮没有打开或解压 ZIP，也没有触碰已 PASS 的 INFO.rar 解压。
4. 四张聊天截图原图未取；各自的两种 OCR 及对齐聊天只是同源派生，不是独立证人。查到的文本可能受识别、分段和说话人标注影响；对时间、主体、设备及最终状态均保留限制。初始对齐对话中先发现有关线索，随后才分别列单并回读截图 OCR，不能倒称先前已取得原图。
5. 质保证书是 PSD 的既有文字派生，不是签章鉴定或逐台实物验收；IEEE 文件是 r96 已保存的固定镜像，不是当前在线登记的实时查询。登记前缀不能证明 Angora 制造、销售或安装的设备数量。
6. 涉及历史原产地标识的文字只作为历史文书观察；本轮未给出“删除产地标识即可合规”的建议或法律结论。目标市场与真实原产地应按适用法规独立评估，不应隐瞒真实来源。

## 和旧轮的交集、工作日期

与 r97 的 108 项重合 8、r98 的 187 项重合 7、r99 的 30 项完整范围重合 5、r99 的 21 项局部背景重合 5、r100 的 4,903 项重合 4、r101 的 38 项重合 7；这是**逐派生路径集合**，不同派生可来自同一原件。r102 的 29 项少于 r101 的 38 项，是因为研究范围改为品牌交付和标识，不是删除来源或声称新得 29 个原件。

会话日期为 **2026-10-26 UTC**；执行环境时钟显示 2026-11-19，仅作相对工作时长参考，不以它倒填采集日期。本轮没有新抓取网页。历史路径日期、来源原字节与既有哈希不改。

**全量读取完成（限定本轮清单）：29/29 个既有派生路径、2,261,276 bytes，逐项计算 SHA-256；另 9/9 个背景工作档、178,368 bytes。** 不代表 29 个独立原件、全量微信原图或 Angora 全部业务均已穷尽。
