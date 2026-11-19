# r98 · 来源与逐源目录

## 时间、范围和证据边界

本轮 Angora 第三至第六单、2025-12 数据中心需求、2026 L3 回复及相关供应侧文件。会话工作日期为 2026-10-26 UTC；运行时沙箱时钟显示 2026-11-19，两者不一致，无法将网页显示内容当作 10 月 26 日归档快照。用户未设 10 月 26 日历史资料截止。目录命名沿用前序命名，不改变旧文件或捏造网页采集日。

历史输入仓原 commit `5acb6132a6a6090bfc777c324cfea6bc8dfb877a` 的 [`FILE-INDEX.csv`](../00-manifest/FILE-INDEX.csv) 有原相对路径、原大小和源 SHA；原文件大多不在本工作区。这里读取的是既有派生产物字节，而非声称重新获取原件；Office/PDF 文字、PSD 图层、纯元数据各有不同证据等级，所有路径独立保留，不合并同名/同哈希文件。

## 一、本轮存下的四个 URL：完整工具可见文本人工转录

以下每个 URL 一个独立 `.extracted.md` 产物，保留全部已返回的可见文本（两个两分块均已拼接）；**不是原 HTML、二进制 PDF、图片或墙后内容**，人工转录未能自动与工具返回逐字逐字节比对。大小/SHA 只用于核本地文件稳定，不证明网页内容未经转录误差或采集日期。无关引用、页脚及原页面中出现的名称只作原文保留，不转为对已叫停对象的研究或主动接触。

| URL | 本地产物 | bytes | SHA-256 |
|---|---|---:|---|
| https://www.angoranetworks.com/angora-networks-_en/?lang=en | [Angora About](www.angoranetworks.com/angora-networks-_en/index.extracted.md) | 4899 | `99681613647cda3ed1fef034fa3184872ff3b8b6e863d41b26ab31b0081ce927` |
| https://www.gov.uk/guidance/customs-valuation/incoterms | [GOV.UK Incoterms](www.gov.uk/guidance/customs-valuation/incoterms/index.extracted.md) | 7512 | `79821a0116d3394045711d7f025f22aa86cbe9ca4606767009838f3b16d7a619` |
| https://www.trade.gov/know-your-incoterms | [美国贸易局](www.trade.gov/know-your-incoterms/index.extracted.md) | 13616 | `21b9bbfaff3403a70238fcf20560b0c8ba89a7409feecfb57b638a11de645fa2` |
| https://www.chrobinson.com/en-us/resources/resource-center/guides/incoterms-tool/ | [C.H. Robinson](www.chrobinson.com/en-us/resources/resource-center/guides/incoterms-tool/index.extracted.md) | 10655 | `f9a95b8f2a0afc7c181f670bbc229af67dcd3b9f633fa64c98cb3faa6777c329` |

第一项为厂商自述，不是独立工商记录；三份 Incoterms 资料是一般说明，不是 Angora 实际合同或法律意见。GOV.UK 页所述 CIP 覆盖水平可能涉及不同规则版本，本轮**不据此判断本单 CIP**；实际 CPT 文书另有保险条款，是否投保/理赔未知。

另外本轮曾查看 ICC Academy CPT/CIP 页面第 0 块（共 5 块）、DAP/DDP 页面第 0 块（共 3 块），以及 [ICC Checklist PDF](https://library.iccwbo.org/content/clp/Others/incoterms_2020_checklist_2024-update.pdf) 第 0 块（共 3 块），未取得/保存它们的全部可见内容；这些探索**不计入上表的四个已归档完整文本，也不作为本报告独立证据**。另有需要登录的 ICC 数字馆入口和搜索结果，未取得墙后原文。此处明确记录未保存内容缺口，不将摘要冒充原文。没有下载网页中链接的视频或图像。

## 二、历史本地目录：187 个源路径、187 个派生产物

[逐文件 CSV](local-order-dc-inventory.csv) 列每条原相对路径、原大小/SHA、抽取方式及派生产物实际大小/SHA；前四单路径数为：第三单 47、第四单 51、第五单 36、第六单 27，合计 **161**；`INFO_2025.12.17/` 16；跨目录对照材料 10（含第二单手册、三份会议资料、L3 建议与回复、两本成本/运费表、MAC 表、微信文本）。

- 187/187 本地产物已逐个完整读取字节并计算 SHA-256：**87 个文字/图层/结构抽取、98 个元数据、2 个原样文本**（含 DXF），读取总量 **22,218,235 bytes**；原样文本两项与旧源索引 SHA/长度相符。
- 表中“原文件合计 388,771,437 bytes”仅为历史源索引相加，不是本轮下载或重读原二进制的数量。历史原图、部分 PDF 签章、银行/承运人服务端和实际设备未核。
- 部分 PDF 为图片或文本乱码；PSD 只见可抽取文字/图层树，无法替代视觉、印章或签章核验。Office 图片、公式计算结果、图像等提取不一定完整；源具体抽取范围以每个派生文件说明为准。
- r97 的 108 条为首两单，r98 的 187 条为上述范围；二者有 **1 条第二单手册重合**，并集 294 个历史源路径，但并集不是全仓 781 件原件的本轮全量读取。不同主题与颗粒度，不拿 108、187 或网页数量比较研究深度。

[交叉引用 CSV](photo-and-manual-crossreferences.csv) 逐路径保留 **7 组照片/21 路径**和 **1 组手册/5 路径**的历史同 SHA 记录；这些 SHA 是当年索引数据，本轮未重新读取相应照片/手册原始二进制，也不意味着独立交付、拍摄批次或造假。相同文件名或 SHA 均不触发合并。

## 三、RAR 目录与散件

[INFO.rar 目录](../04-archive-members/INFO_2025.12.17/INFO.rar.inventory.json)显示 15 个成员的名称和目录大小；其中软件清单目录记 154,139 bytes，历史散件索引 154,107 bytes。`tools/extract_archives.py` 的 `handle_rar_listing` 使用散件哈希作为该字段、并仅比较名称/大小决定 `covered-by-loose-file`；即使其他 14 项大小相同也未比较成员载荷。历史 `tools/verify_ingest.py` 对该状态主要检查散件存在，其“verified loose copy”文字不等于对 RAR 与散件逐字节验证。请以本段和 [映射](../01-text-verbatim/workstation/09-orders/120-angora-orders-master-2026-10-21.mapping-r98.md)覆盖旧叙述。

按用户已定 PASS，不解压或建议解压 INFO.rar；也不将新旧软件版本混同。其内容、实际附件一致性与功能真实性仍未知。

## 四、完整读取口径

**全量读取完成：本轮限定的 187/187 条历史源路径，均已完整读取并哈希各自现存本地派生产物；4/4 个列示 URL 的全部工具可见文本已人工转录。** 这不是原二进制、未存探索页面、未见图片或全文远端响应的全量读取，也不是 Angora 全部商业维度已穷尽。核验 `python3 tools/verify_r98.py` 只检查本地字节、选定文本、算术和链接，不验证真实性、签名、履约或远端响应一致性。
