# r101 · 培训、手册与网管：限定范围与来源目录

本轮是 Angora 内部分析。**先按阶段列路径和大小，再对该阶段全部文件逐字节读取、计算 SHA-256；不把 OCR、文字抽取、网页转录或历史元数据称为原件。** 这不是对全部 Angora 资料或各文件每个技术断言的穷尽语义审计。历史文件名保留原样，来源一条路径一条记录，不合并客户和原记录。

## 全部纳入来源的目录、读取结果及核对

| 阶段 | 列范围（在该组内容读取之前） | 逐项回读及 SHA-256 | 唯一路径 / 本地字节 |
|---|---|---|---:|
| 初始：订单手册、对话、厂商网页旧转录、功能表、邮件及历史源索引 | [scope-before-read.csv](scope-before-read.csv) | [read-inventory.csv](read-inventory.csv) | 19 / 1,872,079 |
| 2026-07 培训截图的两种 OCR 和原图元数据 | [supplement-ocr-scope-before-read.csv](supplement-ocr-scope-before-read.csv) | [supplement-ocr-read-inventory.csv](supplement-ocr-read-inventory.csv) | 3 / 70,196 |
| 已存在的 CLI/Web 独立散件文字派生及邮件线派生 | [supplement-manual-scope-before-read.csv](supplement-manual-scope-before-read.csv) | [supplement-manual-read-inventory.csv](supplement-manual-read-inventory.csv) | 7 / 10,318,789 |
| 2025-11 日志监测计划截图的两种 OCR 和原图元数据 | [supplement-monitoring-scope-before-read.csv](supplement-monitoring-scope-before-read.csv) | [supplement-monitoring-read-inventory.csv](supplement-monitoring-read-inventory.csv) | 3 / 67,217 |
| 2026-08 AC5 样机/NMS 建议截图的两种 OCR 和原图元数据 | [supplement-ac5-scope-before-read.csv](supplement-ac5-scope-before-read.csv) | [supplement-ac5-read-inventory.csv](supplement-ac5-read-inventory.csv) | 3 / 21,172 |
| 已存在的 User Manual 独立散件三种文字派生 | [supplement-user-manual-scope-before-read.csv](supplement-user-manual-scope-before-read.csv) | [supplement-user-manual-read-inventory.csv](supplement-user-manual-read-inventory.csv) | 3 / 3,837,329 |
| **合计** | 每组均先列路径与大小 | **全部 38 项逐路径完整读字节并计算 SHA-256** | **38 / 16,186,782** |

[34 条逐项证据定位](evidence-traceability.csv)记录各源路径、该派生物 SHA-256、行号和短检索锚；它是分析索引，**不是 34 份新增原始来源，也不代替原文**。[10 条手册历史索引](manual-history-crossrefs.csv)逐原路径保留历史大小、历史 SHA、提取方法和现有派生物哈希，未把相同历史哈希的记录合并。

另有 [10 个既有工作档及入口的范围](context-before-read.csv) 与[修改前完整字节和 SHA-256](context-prefix-read-inventory.csv)，合计 159,790 bytes；它们是用于旧结论核对的**分析背景**，不计入上表 38 项。若向工作档追加勘误，校验器核对旧字节前缀。已被 r99 锁定哈希的 `05-verified-quotes-by-speaker.md` 不改动，另建独立勘误映射。

## 一源一产物及各证据的真实形态

1. 七个订单手册 PDF/PUB **历史原始路径分别保留**，对应七个现有派生文件。PDF 是 pypdf 文字层及提取器元数据，图片/排版不在文字层中；PUB 是可打印字符串提取，不能称可完整重建 Publisher 文档。历史文件索引的大小/哈希不是本轮重取原件。
2. 其中第二单 `ANW-1108-V User Manual.pdf` 与第三单 `User Manual_178台LT-IS6318GP-2GX16GT.pdf` 的历史索引同记 599,437 bytes 和 SHA-256 `b62601e199425ba687725a729d520165f00b63dd1cd03b6b3764694c16880e04`；当前两份抽取去各自来源头后正文也逐字节相等，SHA-256 为 `3a6c67372b9d463fa9ee379ad6aee055169b0bf5bfeed505e9835c46855b99ba`。**前者是旧索引一致，后者是本地文字正文一致，不是本轮对两份原始 PDF 的二进制复验。** 不据此推定两个订单的设备功能或安装相同。
3. 已有的 `INFO_2025.12.17/CLI Manual.docx`、`Web Manual.docx`、`User Manual.docx` 三个**独立散件的既有文本派生**分别留在原路径；CLI、Web、User 各有一份主抽取和 JSON/Markdown 派生。三份主抽取分别为 3,172,231、139,915、1,291,026 bytes；历史方法标注覆盖正文、表格、页眉页脚、文本框和注释等，但文字层不保证原 Word 的图片、布局和全部可见信息完整。三份文字派生的页脚均出现 `CENTEC STH Series / Saga Telecom`，不证明在客户现场安装，也不证明适用于 AC5。**不打开、不解压 INFO.rar，不把同名同大小的压缩包目录成员当作本轮验证的同字节载荷。**
4. 三张聊天截图仅有既有 OCR、坐标标注和截图元数据，本轮未取原图；对齐 JSON/Markdown、另一版 OCR 与原始截图是同源不同派生，不是多名独立证人。2026-07-20 15:15 说话人存在实际冲突，见[专门勘误](../01-text-verbatim/workstation/01-knowledge-base/05-verified-quotes-by-speaker.mapping-r101.md)。截图显示的培训 PDF 和 2026-08 的 bin 文件卡不等于相应文件内容或传输安装记录。
5. 三个官网材料是 r97 保留的**工具可见页面人工文本**，不是 HTML/PDF/截图或自动核验逐字一致的响应。本轮未重新联网采集，网页实际采集日未知。两份 VERGE PDF 为既有文本抽取，字形编码及多栏可能损坏，无法替代原图。
6. 2025 邮件是由既有 PDF 文字层和此前整理的邮件线两种派生物回读，均属于同一封邮件线；原始附件并未取得。没有复制、传播其中的账户或认证信息。

## 与上一轮口径及时间

r100 有 4,903 个派生路径，其中 4,881 个属于同一固件文本树；r101 不再遍历该树，改为 38 个培训/手册/NMS 相关派生路径。两轮数量相差是**范围变化，不是丢失来源、客户数下降或新增 38 个原件**。按上述路径精确集合比较，r101 与 r97 的 108 项重合 4；与 r98 的 187 项重合 9；与 r99 的 30 项完整范围重合 6、与其 21 项局部背景重合 8；与 r100 的 4,903 项重合 8。相同原件的不同派生路径不会被此计算自动识别为重复。

本次会话工作日期为 **2026-10-26 UTC**；执行环境时钟显示 2026-11-19，与会话日期不一致，仅用于测量相对工作时长，不能倒填官网动态页采集日期。旧来源的文件名和既有哈希不变；历史事件日期以各自文本/OCR为准。

**全量读取完成（仅限以上清单）：38/38 个既有派生路径、16,186,782 bytes，另 10/10 个背景工作档、159,790 bytes；逐路径计算 SHA-256。** 以上不等于 38 个原件、38 个独立事件，亦不等于逐字审计完整截图、Word 图片或整个 Angora 历史。
