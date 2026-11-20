# r116 来源目录与边界

**主问题**：补充 Angora Networks 2016–2026 的公开商业史；主体未确认。以会话日期 **2026-10-26 UTC** 为事实截止，不以冲突、未经校准的沙箱墙钟覆盖。历史提交、归档捕获、页面自标日期和本次实际取文观察分别记载；见[日期边界](date-boundary-and-refetch-note.md)。

## 按证据性质分开

- **版本库原字节**：Wireshark 2019-02-24 增加 `/36` 映射，保存父／子两个完整 `manuf`；Gentoo 保存 2018、2019、2020 三个完整 `ma-small.txt`。五份分别存入 `github-raw/github.com/<owner>/<repo>/<commit>/<original filename>`，`gh api` 原响应与 stderr、退出码分离；[Git blob 校验](github-blob-checks.json)、[更早两个镜像校验](github-historical-mirror-checks.json)、[完整文件精确子串扫描](scan-full-file-exact-results.json)。Git blob 匹配证实所取版本库文件字节与 API 对应，不证明 IEEE 签发时间、产品实际使用、客户交易或法人身份。数据可能共同源于 IEEE；Wireshark 文件头明确列了多个数据源，不能把两个镜像算作独立分配证书。
- **科技园目录工具可见文本**：AR01、AR04、AR05 分别是 2020-12-05、2024-09-20、2026-01-20 Wayback 回放；各 4 块，逐块保留，不拼接。AR01／AR05 后续为留存逐块重发请求；回放工具栏可能动态变化。AR04／AR05 的正文列 Angora 及域名；不能推断入驻始日、活动连续性或采购。AR01 本次四个转存块 `angora` 零命中，只表示有限字符串检索，不能断言未入园。人工转存有误抄风险，非原 HTML 或 byte-identical。
- **Advensis**：AR06／AR07 是同网站英文页 2020／2022 两次各一块；多为图片链接，图片未下载。与 r114 的土文版同一发布方，不是独立证人；不能由图片名推断合同、销售或履约。
- **旧轮证据**：Find 为未验证第三方目录；其列出的街道门牌与 Gentoo 镜像相同，但其地区字段写 Yenimahalle，镜像写 Cayyolu，不能单凭这些确认法人。r114 的 IANA PEN 属于不同编号空间，分配时间和截止时有效性未知。`?p=330` 已由 r114 保存；[支持页去重](support-dedup-and-discovery-limits.md)。

[逐产物目录](source-catalog.csv)逐行列 URL、时间锚、相对路径、保真度及禁推断；**每块／版本一行，不代表独立来源数**。[逐项锚](evidence-traceability.csv)与[取文元数据](fetch-response-metadata.csv)说明局限。三份 CDX 是过滤查询结果，不是全部历史。[详细失败和不完整情况](fetch-observations-and-limitations.md)。

## 搜索、缺失和转录纠正

Q01–Q84 均先列计划再执行；84 份 `search-discovery/Qxx.json` 仅是人工记录的查询、部分 URL 及结果数，包含重复且可能误数，**不是完整搜索响应**；原始搜索响应未完整持久化，不能冒称全量搜索结果。其他来源不得靠摘要升级。

P01、P02、P05 只保留首块；AR02／AR03 只看首块且原响应未转存，均未用于主体事实结论。P02 自标 2026-10-31，晚于会话截止；[初稿错误与重发修正](P02-transcription-correction-and-refetch.md)已具名留痕。自标 2026-10-29 的文章仅出现在搜索中，未取全文，不做获奖判断。Gmail／Drive 未开启且未访问，不请求开启。

## 读取和验证范围

- 起始先列旧轮范围并完整读入 UTF-8：17/17，102,536 bytes；另选 3/3，22,974 bytes；为支持页去重再列 5/5，12,307 bytes。它们不是独立外部来源数；逐项清单和 SHA 分别在 `prior-round-read-inventory.csv`、`prior-sources-extension-read-inventory.json`、`support-dedup-read-inventory.json`。
- 最终本轮产物限定范围须先列 `round-readback-scope.csv` 再逐文件完整读取、哈希；结果见 `round-readback-inventory.csv` 与 `round-readback-summary.json`。交付文档另列范围回读。文件字节读全不等于对人工转存逐字人工核验。
- [验证脚本](verify_r116.py)验证 Git blob、时间锚、限定检索、已存块、索引路径及交付链接；它只验证本地一致性，不能证明外部网页未变或资料穷尽。

保留各既有 PASS，不读取或引用隔离的官网 PDF／about 文件；不检索停项主体，不发送邮件、不使用设备。单一 follow-up 文件仅指向既有 Angora 档案，重复主体不合并、不重复联系，C 档不跟进。无新增 Ewind 事实。
