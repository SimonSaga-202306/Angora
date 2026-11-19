# r106 · 设计服务与履约边界：来源、差异和执行记录

## 先列范围与完整读取

| 本地组别 | 预列与回读 | 路径／字节 | 表示及边界 |
|---|---|---:|---|
| 旧 CMS 页面表 | [范围](local-cms-scope-before-read.csv) / [回读](local-cms-read-inventory.csv) | 2 / 5,858 | 两份已存 TSV，不是本轮实时 API；原表头有已知计数误差。 |
| 旧抓取方法 | [范围](local-method-scope-before-read.csv) / [回读](local-method-read-inventory.csv) | 2 / 8,555 | 历史方法文本，目录标签及旧抓取日期不独立验证。 |
| 既有报告／档案 | [范围](context-scope-before-read.csv) / [回读](context-read-inventory.csv) | 6 / 126,312 | r94、r101、r102、r105 报告与审计、120 档案；不将背景全文都当新证据。 |
| r97 既存网页文字／方法 | [范围](local-existing-web-scope-before-read.csv) / [回读](local-existing-web-read-inventory.csv) | 3 / 12,920 | 英文服务页、英文网管页和方法 README。网管页含已停主体图标路径，**整页排除本轮结论**，不再扩展该页。 |
| 两个 DOCX 抽取及 r104 报告 | [范围](local-direct-scope-before-interpretation.csv) / [回读](local-direct-read-inventory.csv) | 3 / 20,908 | 两份独立历史文字抽取、r104 上轮报告，不是原 DOCX、实机或完成交付。 |
| r105 来源交集索引 | [范围](previous-index-scope-before-comparison.csv) / [回读](previous-index-read-inventory.csv) | 4 / 4,699 | 只比较路径；其中一个在本轮安全清单下已先列并读。 |

**20/20 不同路径、179,252 bytes**；各组清单写入后完整读并计算 SHA-256。其中三份旧文档（r94、r104 报告及 120 dossier）在专题清单前已按 [r105 安全目标清单](../48-entry-safety-r106-2026-10-26/r105-append-final-scope-before-read.csv)先列并完整字节读取；一个 r105 索引先在 [安全总表清单](../48-entry-safety-r106-2026-10-26/prior-ledger-scope-before-read.csv)先列后读，再纳入比较清单。不能把这些初读误写成发生在后续专题清单之后；未凭哈希反推执行时间。其他路径按各自范围先列后读。

两份历史 DOCX 是**已有文字抽取**，文件名或文字说有图片、已变更、已附图均不是原件、照片、设备、签字、交付或验收；说话人部分未独立确认。筛选定制字段时曾意外输出与本轮结论无关的一条旧标签表述；未引用或据此建议任何标识处理，不对旧单追问。

[上一轮交集](overlap-r105-24.csv)：本轮最初 16 个业务／背景路径中有 **7** 个属于 r105 的 24 条，另四条是本轮新列的 r105 索引；差异来自服务主题和材料范围，不是删源或全部业务穷尽。安全验证另核 31 个保护副本、17,455,599 bytes，不计入 20 条研究清单。

## 新网页、隔离及来源等级

[三条厂商 URL 预列](web-initial-scope-before-fetch.csv)后各取 1 块；后来先列[一次搜索计划](web-discovery-plan-before-search.csv)，再将五项结果保存为[发现元数据](web-discovery-metadata.csv)，只选媒体文章、先列[补充 URL](web-interview-scope-before-fetch.csv)再获取 4 块。合计 **4/4 URL、7/7 块、41,836 bytes**，每个 URL 一个保存文件；搜索结果只存类型、URL、搜索显示年龄和处置，没有保存完整搜索片段，不能把搜索计为全文或独立证据，四个未选结果均未访问。

- 厂商 OEM/ODM 土文页及土文服务页，**2/2 URL、3,868 bytes**；另以已存 r97 英文服务页对照。同一发布方不同页面／语言，不是独立验证。
- [ICT Media 访谈清单](web-interview-visible-inventory.csv)为 **1 URL／4 块／33,069 bytes**；四块仅按该同一 URL 的原先后相接，块边界和哈希见[记录](web-interview-chunk-inventory.csv)。页面说是 2023 年节目摘要，管理者的话仍为企业自述；动态推荐项含晚于会话日期的日期，不作采访事实或当时快照。手工复核发现块编号 2（从零计数）两处、编号 3 一处转存差错，已改正并保留[前后哈希](web-interview-transcription-corrections.csv)，其他块不变；未自动比对工具响应，仍可能有未察觉的转存误差。
- 另一个英文“关于”页的伙伴图墙意外带出已停主体的图标 URL。保留完整工具可见文字 **1/1、4,899 bytes** 于预列的原路径并隔离，**不作任何本轮结论依据**；不保存图片，不分析该主体、不接触，也不再访问类似伙伴墙页面。r97 既存网管页回读时也意外带出该类图标引用，整页从本轮结论排除。上述两次偏差已向用户说明。
- 人工转存可补末尾换行，未自动逐字核对工具响应；保存文件的 SHA-256 只标识本地字节，不是原 HTML、独立测评或履约。隔离页面标为 `-diff` 以免在 Git 文本 diff 中重复显示已停主体，文件自身不删、不截断；普通 `git diff --check` 因此不检查该文件。

## 派生索引与纠错

[87 条行锚](evidence-traceability.csv)绑定原始保存字节／原前缀、哈希和 1-based 行；[21 组英／土服务条目](services-cross-language-items.csv)、[6 门单项课程时长](training-catalog-durations.csv)、[6 项设计服务声明](oem-service-claim-matrix.csv)、[9 项访谈定位](interview-claim-matrix.csv)、[17 条既有定制文字](historical-design-text-lines.csv)及 [8 项具名纠错／限定](issues-and-corrections.csv)均为分析索引，不是独立原件。停主体相关页面不进入行锚、差异或业务结论。服务页含一般服务菜单用词，不等于启动仓库历史 RFQ/RFP 事项。

[r40／r39 的旧 CMS 相关行](cms-relevant-page-rows.csv)只表示两份保存 TSV 的字面字段，包含网管页面元数据但不使用网管页内容；[两条服务页字段对照](cms-service-fields-comparison.csv)与[两份表的 24／25 行数核对](cms-saved-row-counts.csv)不证明当时采集日、产品上市、网站从未修改或现行合同。[两份旧档追加计划](append-plan-before-write.csv)先列，后存 [原前缀及本轮追加哈希](append-log.csv)：79,373 bytes 前缀保留，追加 2,442 bytes；不修改旧 TSV 或根 `.gitattributes`。

本会话提供日期为 **2026-10-26 UTC**；环境时钟显示 **2026-11-19 UTC**，冲突未解决。各旧路径日期保留，不倒填真实采集日。历史财务差异、未成交／未付款旧单、仓库旧 RFQ/RFP、INFO.rar 解压、官网评论验证、48 口澄清、阶梯报价及主动下载官网 PDF 持续 PASS；未联系客户或操作设备。

**全量读取完成（仅限本轮本地清单）：20/20 个不同路径、179,252 bytes；4/4 URL 的 7/7 工具可见块按 URL 分别转存，其中 1 页隔离、不用于结论。** 不代表 HTML 原件、所有网页、源图像、合同、所有设备或 Angora 全部商业史已取得。


---

## r107 具名勘误：旧访谈转存漏字

四块工具响应曾获取，但原手工转存第 105 行遗漏 `sunmak katkıda bulunabilmek`。旧文件及原四块哈希清单不改；[r107 单次替换计划与哈希](../53-source-evidence-r107-2026-10-26/r106-transcription-correction-log.csv)另存修订版。原 9 条主张定位的行在本次修订前后相同，见[影响核对](../53-source-evidence-r107-2026-10-26/r106-transcription-claim-impact.csv)。尚未自动逐字比较全部工具响应，故不保证全文无其他错误；旧 verifier 的 PASS 不能证明转存忠实或访谈事实。
