# r104 · 安全产品及工业协议：限定来源与保存说明

本轮以 Angora 为主体，逐项区分厂商自述、历史派生索引、工具可见文本、搜索片段和独立测试；不联系客户，不操作设备，不将网页参考 logo 当作产品订单或验收。总报告见 [173](../01-text-verbatim/workstation/08-customer-pipeline/173-angora-security-products-protocols-r104-2026-10-26.md)。

## 范围、时序和计数

| 组别 | 先列范围／回读清单 | 实际口径 |
|---|---|---:|
| 旧官网综合镜像完整目录与两次旧 WP 表 | [预列 10 项](local-product-scope-before-read.csv)、[逐字节与哈希](local-product-read-inventory.csv) | **10/10，100,270 bytes**；6 个综合镜像因混有已停内容不作分析，4 个旧 TSV 只核保存的字段与行数。 |
| 两份旧轮方法说明 | [预列](local-method-scope-before-read.csv)、[回读](local-method-read-inventory.csv) | **2/2，8,555 bytes**；只确定 r39／r40 和历史标注的方法，不视为当前原始 API。 |
| r101／r102／r103 的日期表述 | [范围](date-audit-scope-before-read.csv)、[回读](date-audit-read-inventory.csv)、[日期行锚](date-claims-index.csv) | **9/9，45,091 bytes**；文件名前三个 README **已在清单写入前读取**，该 CSV 文件名中的 `before-read` 对这 3 项不成立；其余 6 项在列单之后读取。 |
| r94／r101／r103 工作档、订单档、两入口与属性文件 | [预列](context-scope-before-read.csv)、[旧前缀](context-prefix-read-inventory.csv) | **7/7，150,595 bytes**；必要的更新只追加，哈希锁定原前缀。 |
| 厂商网页／PDF URL 工具可见文本 | [首批 3 URL](web-initial-scope-before-fetch.csv)、[补充 8 URL](web-supplement-scope-before-fetch.csv)、[再补充 3 URL](web-second-supplement-scope-before-fetch.csv)、[逐 URL 文件大小与 SHA-256](web-visible-inventory.csv)、[分块边界](web-chunk-inventory.csv) | **14/14 URL、16/16 返回块，共 89,981 本地 bytes**。其中 **10 网页 URL／11 块／65,130 bytes**可用于厂商声明分析；**4 PDF URL／5 块／24,851 bytes**因发现旧 PASS 而隔离，不用于本轮结论。 |

上述本地四组共 **28 个不同路径、304,511 bytes**。另为计算与 r102／r103 的路径交集，实际先读取了 **7 个旧轮清单、12,932 bytes**，之后才[补列并回读哈希](overlap-check-inputs-after-first-read.csv)；不能说这 7 项先列后读，其中一个 r102 背景清单被读取但未用于来源交集。连同前四组为 **35/35 个不同路径、317,443 bytes**。安全复验另读取 31 个既有保护副本、17,455,599 bytes，仅核哈希，不计入 35。逐字节读取／哈希不等于完整语义审计，也不代表 35 个原件；总来源数不把每个分块、语言版本或同源派生当作独立证人。

[初始 3 条搜索](search-plan-before-discovery.csv)和[补充 3 条搜索](supplement-search-plan-before-discovery.csv)均在相应搜索前列出，仅用于发现地址；三个分批 URL 清单分别在相应网页工具调用前保存。其余五次搜索响应仅用于选 URL，未逐条保存、不作为正文证据；有方向差异的一次[搜索响应片段](search-visible/query-03-result.json)单独保存，[大小和哈希](search-result-inventory.csv)可核。搜索内容自身只是摘录，`pageAge` 不当作发布日期。

## 原文形态、分块和止损

1. 每个 URL 的工具可见内容各存一个独立路径，保留原 URL 的主机及路径层级；同一 URL 的多个工具块按原序拼接，并用[字节范围清单](web-chunk-inventory.csv)记录边界。NPB 网页两块在段落之间分界；一个被隔离的 PDF 提取在单词中间分界，不人为插入字符。数据由工具输出**人工转存**，文件末尾可能补换行，未机器逐字比对工具原响应；本地 SHA-256 只标识保存产物。
2. `fetch_page` 提取可见 Markdown／PDF 文字，可能省略网页导航、图像、动态内容、原始排版或 PDF 页面；PDF 解析器最多 30 页。**未保存远端 HTML/PDF 二进制、图像或签名**，不能声称原始响应字节一致、完整原件或网页当日全部内容。厂商中英／土版本是同一来源机构；网页、公告、页脚、TSV 可互相定位，但不是独立客户证词。
3. NPB 英文网页的工具可见文本含 **3 个 0x1c 和 6 个 0x1e 控制字符**，原样保留，不能静默改成英文字母；2023 年英文协议公告首段也有文字断裂，按工具所示保留、不用土耳其语版本静默补写。这些可能是源文或抽取异常，不能据此判原站或实物有缺陷。行锚以 LF 为边界。
4. 回读历史综合镜像后发现旧索引记载“主动下载官网 PDF 数据表”已 PASS；**发现前** r104 已通过网页解析器读取 4 个 PDF 链接的文字层、r103 曾读取 2 个 QR PDF 链接。没有保存 PDF 二进制。本轮 4 个 PDF 文本在原已保存路径隔离，仅为透明审计而保留，**不纳入本轮技术结论**；发现后停止访问此类链接，不重启该停项。[审计](../43-audit-r104-2026-10-26.md)如实记录。
5. 综合镜像回读时还意外显示已停公司和官网评论验证的历史文字；发现后停止宽范围语义检查，不分析、不跟进。镜像文件未删除或修改，六个镜像不作本轮结论依据。
6. [44 条行锚](evidence-traceability.csv)、[11 条协议矩阵](protocol-capability-matrix.csv)、[4 条时序](publication-dates.csv)、[10 项差异及纠错](issues-and-corrections.csv)是可追溯索引，不替代各来源可见全文。[r39/r40 页面比较](wordpress-pages-compare.csv)和[帖子比较](wordpress-posts-compare.csv)仅核存储 TSV 内字段，不是实时 CMS 或原始 API；每个旧文件保留原路径，不合并记录。

## 时间与上一轮

本会话提供的日期为 **2026-10-26 UTC**，执行环境的 UTC 时钟显示 **2026-11-19**；两者冲突。环境时钟差仅用于估算工作间隔，不能倒填动态网页真实采集日。旧 r39／r40 记录自标 10-27／11-01 晚于会话日期；这些是历史文件自带的采集标签，并非本轮验证过的实际时点。r101／r102／r103 记录了 10-26 会话日期与 11-19 环境差异，不能凭后者把前者统一判错。

r103 有 16 个限定本地来源；本轮 10 个旧网站／TSV 路径与其按路径重合 **0**，与 r102 的 29 条限定来源也重合 **0**，见[交集索引](overlap-r102-r103-by-path.csv)。方向、白名单和证据形态不同，不是删源，不能将本轮 14 个 URL 算成 14 个独立来源机构或客户。

**全量读取完成（限定本轮本地路径）：35/35 个文件、317,443 bytes，逐项哈希；其中日期核对前三项和 7 个交集清单先读后列已披露。另 14/14 URL、16/16 工具块已人工转存，其中 4 个 PDF URL 隔离不用。** 不代表全网、完整官网 HTML/PDF、现场设备或 Angora 资料已穷尽。
