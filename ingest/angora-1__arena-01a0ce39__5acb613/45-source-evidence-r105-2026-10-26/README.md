# r105 · 交换机产品族：限定来源、派生表与执行边界

## 本轮来源：逐路径，不混合原件

| 组别 | 先列范围／回读清单 | 路径与原始读取字节 | 代表什么 |
|---|---|---:|---|
| 旧产品页面、TSV、方法 | [先列](local-scope-before-read.csv) / [回读](local-read-inventory.csv) | 7/7，22,889 | r39 的三个中文派生摘要、两份旧 TSV 与两个方法说明；不是原始 HTML 或当前 CMS API。 |
| 背景及旧档前缀 | [先列](context-scope-before-read.csv) / [回读](context-prefix-read-inventory.csv) | 7/7，153,411 | r94、r103、r104 报告，120 档案，两份 README 与根属性；后续两处仅追加，哈希绑定原前缀。 |
| r104 交集与追加记录 | [先列](previous-index-scope-before-read.csv) / [回读](previous-index-read-inventory.csv) | 6/6，8,979 | r104 自己的来源清单和追加日志；只用于范围交集与保护，不是六个新一手资料。 |
| 本轮补充审计输入 | [先读／扫描后列](additional-scope-after-first-read.csv) / [回读](additional-read-inventory.csv) | 4/4，18,967 | r104 审计、旧日期清单经 `read_file` 全读；r104 来源 README 和映射经 `rg` 扫描。**四项都在本清单前已访问**，然后完整回读字节并哈希；审计后续只追加。 |

四组合计 **24/24 不同本地路径、204,246 bytes**，哈希约束的是各文件在本轮原读取时的完整字节；不宣称 24 个原件或对每份长背景全文作商业结论。额外的安全核查先列 r104 入场对照总表、再核 [31 个保护副本](../44-entry-safety-r105-2026-10-26/protected-variants-read-inventory.csv)，共 17,455,599 bytes；只核字节，不算进 24 条研究来源。

本轮对 4 个既有文件作**仅追加**，先列 [追加计划](append-plan-before-write.csv)，后留 [原前缀、追加段、最终字节和 SHA-256](append-log.csv)：原前缀共 95,306 bytes，最终追加 3,755 bytes。交付前为避免误解厂商 30W 原文，对本轮新追加的一个段落做过[文字修订并留前后哈希](append-suffix-revision-log.csv)，原前缀未动。r104 的六个最终文件曾在追加前完整相等，见[当时的检查结果](r104-final-protection-inventory.csv)；其后二者末尾追加，四者仍全文不变，六者原始前缀都保留。并未执行旧 verifier、解压或使用隔离 PDF 文本。

## 五个官网 URL：网页工具可见文字，不是原 HTML

[初始 URL 预列](web-initial-scope-before-fetch.csv)和[补充 URL 预列](web-supplement-scope-before-fetch.csv)均在各自获取前写入；[网页清单](web-visible-inventory.csv)记录 URL、标题、路径、单块、字节、SHA-256 和表示方式。**5/5 URL、5/5 返回块，分别人工转存为 5 个独立文字产物，总计 22,840 bytes**：

1. [Hitit 土文](external-visible/www.angoranetworks.com/hitit-yerli-network-switch-ailesi/index.tr.extracted.md)。
2. [Synapse 土文](external-visible/www.angoranetworks.com/synapse-network-switch-ailesi/index.tr.extracted.md)。
3. [Verge 土文](external-visible/www.angoranetworks.com/verge-network-switch-serisi/index.tr.extracted.md)。
4. [network-devices 土文](external-visible/www.angoranetworks.com/network-devices/index.tr.extracted.md)。
5. [Verge 英文](external-visible/www.angoranetworks.com/verge-network-switch-family/index.en.extracted.md)。

人工转存的本地哈希只标识保存的文本；没有程序逐字比对工具原响应，末尾可能有转存换行。工具显示的网页主体、链接和表格文字不等于完整 HTML／CSS／图片／原始响应、设备照片、测试或认证。五个 URL 同属一个厂商，英土版本不是独立验证；不因 URL 数量宣称五个厂商或五个商业事件。新网页的真实页面发布日期及抓取日均不能由目录日期反推。

## 搜索发现及偏差

[三条后续查询](web-query-plan-02-before-search.csv)在搜索前列出，搜索共返回 15 个结果；仅将每条结果的标题、URL、搜索显示年龄和处置记为[发现元数据](web-discovery-metadata.csv)，没有转存全部搜索片段，故**不计为全文来源、不以片段作为技术结论**。其中部分无关结果的片段带公开登录／配置示例；它们属于超出本轮型号分析的输出，未复写这些示例、未访问对应支持页面、未尝试登录或操作设备。查询结果出现既有网页不构成新的独立来源。未以搜索结果重新访问已 PASS 的 PDF 或评论区。

## 可复核派生表

- [50 条行锚](evidence-traceability.csv)绑定来源字节长度、SHA-256 和 1-based 行号；旧文件若有追加，验证原前缀，不修改其证据行。
- [Hitit 11 个厂商可见型号行](hitit-web-model-rows.csv)与 [11 个旧摘要同名匹配](hitit-model-name-crossrefs.csv)只比较字符串，不断言历史内容或硬件无变化；[8 个 PoE 行均分预算算术](hitit-budget-conditional.csv)不是单口额定值。
- [Synapse 五型号 × 11 行、55 个字面单元格](synapse-five-model-literal-cells.csv)只解析每行恰有五个型号值的网页表格；`Boşta Güç Tüketimi`、`Voltaj ve Koruma`、温度与 MTBF 等只有一个可见单元格的行不自动填到所有型号。另有[三个选定型号](synapse-selected-models.csv)。
- [12 个供电假设](poe-conditional-arithmetic.csv)与 [4 个端口速率／包速算术](switching-conditional-arithmetic.csv)均是条件计算，不是 PoE 协商、热设计、线速或转发测试；`5713` 的 24S 速率不明，故未假定其参与运算。
- [四个页面的旧 TSV 字面时间字段](page-timestamp-fields.csv)、[13 项差异／具名纠错](issues-and-corrections.csv)保留来源与不确定性。r105 七个产品来源与 r104 的 35 路径重合 4；[七个背景路径重合 6](overlap-r104-context.csv)，见[本地交集](overlap-r104-local.csv)。范围随主题变化，不能解释为漏源、删源或全业务穷尽。

## 日期及 PASS

本会话提供日期 **2026-10-26 UTC**，环境 `date -u` 观察到 **2026-11-19 UTC**；两者冲突。沿用路径上的旧标签不改名，不把环境日期当会话日期或旧网页实际采集日。用户已 PASS 的历史财务差异、未成交／未付款旧单、仓库旧 RFQ/RFP、INFO.rar 解压、官网评论验证、48 口澄清、阶梯报价和主动下载官网 PDF 都不重启。

**全量读取完成（仅限本轮本地清单）：24/24 路径、204,246 bytes；其中 4 条先读／扫描后列并已补列回读。另 5/5 URL 的 5/5 工具可见文本块人工转存。** 该声明不包含搜索摘要、整站、二进制原件或现场产品。
