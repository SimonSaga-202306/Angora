# r103 · 产品端口与 IRIS 光模块：限定来源

本轮聚焦 Angora 的型号、光模块规格和订单登记的证据边界；不联系客户、不操作设备，不重启已 PASS 的历史事项。所有来源按原相对路径保留；分析索引不替代来源全文，也不合并不同客户或原始文件。

## 先列范围，再读取

| 范围 | 读取前清单 | 读取/保存后清单 | 口径 |
|---|---|---|---:|
| 既有型号、手册、图纸与厂商光模块文本 | [source scope](source-scope-before-read.csv) | [完整字节及 SHA-256](source-read-inventory.csv) | 14 路径／335,008 bytes |
| 既有对齐 OCR 和登记表文字层 | [supplement scope](supplement-scope-before-read.csv) | [完整字节及 SHA-256](supplement-read-inventory.csv) | 2 路径／84,593 bytes |
| **本地来源合计** | 两组分别在读取前列路径及大小 | **16/16 完整字节读取** | **419,601 bytes** |
| 新取厂商工具可见资料 | [3 个 URL 与目标路径](web-scope-before-fetch.csv) | [3 个产物的大小、哈希和保存限制](web-visible-inventory.csv) | 3 个 URL／4 个工具块／18,498 bytes |
| 旧来源指南 | [读取前范围](guide-scope-before-read.csv) | [原前缀哈希](guide-read-inventory.csv) | 2 路径／19,722 bytes，不计入 16 |
| 背景报告与入口 | [首组范围](context-scope-before-read.csv)、[补充范围](supplement-context-scope-before-read.csv) | [首组前缀](context-prefix-read-inventory.csv)、[补充前缀](supplement-context-prefix-read-inventory.csv) | 9 路径／196,386 bytes，不计入 16 |
| 保护引用检查 | [检查前清单](protection-check-inputs-before-read.csv) | [完整字节及 SHA-256](protection-check-read-inventory.csv) | 31 个清单／脚本、1,489,548 bytes；只做静态引用检查，未执行旧脚本 |

读取前另保存 [66 条候选路径与文件大小](candidate-paths-metadata.csv)，共 969,202 bytes 为对应候选文件的大小总和，**不是 66 个文件内容读取量**。初始文件名过滤不完善，曾显示几条已停事项的历史财务／型号路径；它们没有进入 16 项来源白名单，也没有作为分析或跟进依据。后续停止宽筛。

## 一来源一产物，区别文本和原件

1. 14＋2 项均是仓库既有的文字抽取、元数据索引或 OCR；Word/PDF/AI/XLSX 和聊天截图原件本轮未重取。[8 条原始资产交叉索引](local-asset-crossrefs.csv)分别保留历史原始路径、大小、哈希、派生路径与当前哈希，历史索引不是本轮原件认证。
2. 三个 URL 的内容逐 URL 存为独立文件：`/qr/10201/` 的单块可见文本经人工分节核对，复用以前保存的归一化文本；英文页面的单块由工具可见文本人工转存；`/qr/10203/` 的两块按此前规范化文本和本轮可见块边界整理。均不声称与工具输出或远端 HTML/PDF 响应字节一致。
3. `/qr/10203/` 工具返回的两块在尺寸行附近出现疑似边界缺字；保留两个块的边界和缺口，不用旧来源默默填补，也不称完整取得 PDF 内容。PDF 工具还存在页数及文字层限制；无二进制、签名、页面图像或版面。
4. [四对派生正文比较](extracted-body-identity.csv)以 SHA-256 和字节长度核对：有些历史归一化文本是人工复用，不是独立原始证据；图纸、手册文字相同也不证明原件视觉、型号或实际设备相同。
5. [21 条选定行锚](evidence-traceability.csv)、[6 组规格疑点](optics-conflict-cases.csv)与[登记表 16 行原位置和哈希](tt-model-registry-row-index.csv)仅是分析索引；登记表的每行原文仍在原路径，索引不复制 MAC 或序列号。第二组 10 行未直接标 Angora，主体未确认，不合并为新订单。
6. 先前指南 [r96 README](../11-source-evidence-r96-2026-10-26/README.md) 只在记录的 15,228-byte 原前缀后追加了具名勘误；旧报告和入口也仅追加，原前缀哈希不变。不得把原前缀哈希误当成追加后的整个文件哈希。

## 日期、重合和限制

会话日期标注为 **2026-10-26 UTC**；本轮抓取时执行环境时钟显示 2026-11-19，二者不一致。保留这一差异，不倒填网页采集日，也不能证明这些动态页面在 2026-10-26 即为当前内容。厂商页面上的兼容性、认证、客户参考及产品规格是厂商自述，并非独立验收或销量；未取得网页原始 HTML、原始 PDF 或实物。

本轮 16 个既有本地来源，与 r102 的 29 项按路径重合 **7** 项，详见 [逐路径交集](overlap-r102-by-path.csv)；数量变化是主题和范围变化，不代表删除来源。三次网页抓取中 `/qr/10203/` 为已有 URL 的新工具读取，其余两项是本轮新增 URL；多 URL 或多派生不能自动算作独立原件或证人。网页搜索在这三个 URL 的清单建立前用于发现地址；随后先列清单再逐 URL 抓取，不把搜索片段作为完整来源，也不倒称搜索前已列出这些 URL。

**全量读取完成（限定本地清单）：16/16 个既有派生路径、419,601 bytes，逐项 SHA-256；另 3/3 URL 的 4/4 工具返回块已按上述限制保存。** 100G QR 块边界缺字、原件和现场设备仍未取得；不代表 Angora 全部信息已穷尽。
