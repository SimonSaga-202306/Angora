# r107 · 早期商业化：限定范围、来源和纠错

## 本地输入：完整字节读取及真实次序

| 组别 | 清单 | 路径／bytes | 表示与次序 |
|---|---|---:|---|
| 第一批旧索引、方法、报告、r106 访谈 | [范围](initial-local-scope-before-topic-read.csv)／[回读](initial-local-read-inventory.csv) | 12／163,154 | 包含两份旧文章 TSV、两份方法、五份既有报告、r106 审计／来源说明及其访谈转存。r94、r104 两份旧报告在专题清单前，已先按[本轮安全范围](../52-entry-safety-r107-2026-10-26/historical-append-final-scope-before-read.csv)列出并读过。 |
| r104 已存英文新闻索引 | [范围](news-index-scope-before-read.csv)／[回读](news-index-read-inventory.csv) | 1／5,695 | 已存工具可见文字，先列后读；同一厂商，不是独立来源。 |
| r106 旧访谈主张索引 | [补列范围](additional-scope-after-first-read.csv)／[回读](additional-read-inventory.csv) | 1／4,323 | **先读后补列**：生成漏字影响表时先打开；发现后如实补清单并完整回读，不能称先列后读。 |
| r106 六组来源清单 | [范围](previous-index-scope-before-read.csv)／[回读](previous-index-read-inventory.csv) | 6／3,981 | 先列后读，仅计算上一轮来源交集。 |

**20/20 个不同路径、177,153 bytes**，完整字节读取并按清单哈希。两条最初按安全范围先列后读、随后纳入专题，一条先读后补列；其余 17 条按各自本轮专题／比较范围先列后读。哈希不独立证明读取顺序或来源真实性；不把已存 DOCX、派生 TSV、手工网页文字说成原件。

[与 r106 的交集](overlap-r106-20.csv)：本轮前 14 条业务／背景路径中 **5** 条属于 r106 的 20 条；另 6 条为本轮新列的 r106 清单。两轮总数同为 20 仅是巧合，不是来源相同或已穷尽。安全核查另有 31 个保护副本、17,455,599 bytes，不计入上述 20 条。

## 新网页：每 URL 一文件，不把推荐链接当正文

- [早期 3 URL 的事先范围](web-first-scope-before-fetch.csv)与[本地字节](web-first-visible-inventory.csv)：3/3 成功、3 块、9,547 bytes，分别为出口页面、教师节页面和 EGM 测试公告。
- [2021 土文 2 URL](web-2021-scope-before-fetch.csv)和[英文训练页 1 URL](web-training-english-scope-before-fetch.csv)均先列再取；[回读](web-2021-visible-inventory.csv)为 3/3 成功、3 块、12,165 bytes。六页均属 Angora；两种语言不是独立发布方，也不是证书、合同、课堂、订单或设备测试证据。
- 合计 **6/6 成功 URL／6/6 块／21,712 bytes**，每 URL 分别保存；另一个[第三方页面先列后获取失败](web-agency-fetch-result.csv)，没有正文、不以搜索片段代替、不重复相同请求。故为 **7 个 URL 尝试，6 成功、1 失败**。
- 页面的关联文章是动态链接，与正文分离；未获取图片二进制、原 HTML、政府证书、签字协议或课程记录。工具块人工转存可能补末尾换行，没有自动逐字比较。手工复核发现本轮英文培训页一个缩略图路径复制错误，已修并留[前后哈希](r107-transcription-revision-log.csv)；仍不能保证其他字词全对。

## 上轮访谈漏字：旧版不动，修订版不算新来源

r106 四个工具块确曾获取，但前一版第 105 行漏掉 `sunmak katkıda bulunabilmek`。先写[修订计划](r106-transcription-correction-plan-before-write.csv)，再将其余字节不变地另存[修订版](corrected-r106/ictmedia.com.tr/haber/yerli-bir-ureticiye-verilebilecek-en-buyuk-destek-onun-urunlerini-kullanmaktir/index.tr.extracted.md)，留[前后哈希](r106-transcription-correction-log.csv)；没有重取、没有覆盖旧文件。这是同一来源的版本更正，不是第二个独立发布方。将修订版的替换逆向还原可逐字节得到原文件。

[九条 r106 主张定位行影响核对](r106-transcription-claim-impact.csv)为 9/9 不变，**只覆盖已索引行和这次单点替换**；不保证全文转存与旧工具响应完全一致，也不验证访谈事实。[r106 主报告](../01-text-verbatim/workstation/08-customer-pipeline/175-angora-design-service-delivery-r106-2026-10-26.md)、本说明原前缀和[旧审计](../51-audit-r106-2026-10-26.md)均只追加具名勘误，不改历史前缀或旧 verifier。

## 比较、派生与搜索边界

[10 条旧文章字段对照](saved-post-tsv-10-row-comparison.csv)按 ID 保留原两表行哈希；日期／修改字段 10/10 相同，但两个 slug 字符串有差异。第一表头称请求 `link,title`，第四列标 slug；第二表头称请求 slug。两表均是派生文字，不代表原 API、实时站点、重定向或任何真实变动。r104 已纠正第一表头的 9／10 行数。

[33 条行锚](evidence-traceability.csv)、[6 行事件矩阵](event-evidence-matrix.csv)与[9 项纠错／限定](issues-and-corrections.csv)仅为可追踪索引；厂商声称、媒体转述、旧索引、图片元数据与实际合同／证书／设备分层，不作独立证明。五个旧文的[追加计划](append-plan-before-write.csv)先于[写入日志](append-log.csv)，保留 108,050 bytes 原前缀、追加 4,385 bytes。

九条查询分别事先列于[第一组](discovery-plan-before-search.csv)、[第二组](discovery-organizations-plan-before-search.csv)、[第三组](discovery-primary-plan-before-search.csv)；[统计](discovery-query-summary.csv)共 **27 条结果元数据**，逐组保存为 [10](discovery-metadata.csv)／[10](discovery-organizations-metadata.csv)／[7](discovery-primary-metadata.csv) 条。搜索结果可能忽略排除词，且相关段落、搜索显示日期、片段并非页面原件；其中一个协会目录、一个培训伙伴墙和多数无关结果没有访问。**Q07 虽有 `-filetype:pdf`，仍返回两个政府财务 PDF 的片段**：未调用 PDF 抓取／主动下载，不保存片段、不引用、不作结论；搜索服务取得片段的方式未知。不能把此次搜索当财务调查或说搜索工具从未处理过 PDF 内容。

会话提供日期为 **2026-10-26 UTC**；环境时钟显示 **2026-11-19 UTC**，目录日期仅标签，不能倒填任何历史采集时点。历史财务差异、未成交／未付款旧单、仓库旧 RFQ/RFP、INFO.rar、评论验证、48 口澄清、阶梯报价、主动下载官网 PDF 均为 PASS，未重启；不接触客户、协会或培训方。

**全量读取完成（仅本轮本地清单）：20/20 路径、177,153 bytes；6/6 成功 URL 的 6/6 工具块分别转存，另 1 个 URL 失败。** 不代表 HTML 原件、图片、政府证书、协议、所有网页或 Angora 全部商业史已取得。
