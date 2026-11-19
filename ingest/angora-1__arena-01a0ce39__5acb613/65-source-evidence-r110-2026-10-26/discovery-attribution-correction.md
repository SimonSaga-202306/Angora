# r110 · 搜索结果归属核验及降级（C12）

## 问题与影响

Q01–Q14 先分别列了搜索计划，但部分搜索并行执行；留存的搜索工具结果没有可用于可靠重建调用与返回对应关系的查询回显。尤其 Q09／Q11 以及 Q12–Q14 的编组不能在事后得到充分核实。不能因结果看起来相关或因为结果的位置相邻，就断定它由某一查询返回。Q01–Q08 也**保守地同样降级为未核实**，这不等于已证明每个标签均错误。

因此三个元数据表中原 `query_id`、`position` 和零结果标记只能视为**当时人工编组的暂定记录**，不得据此声称某个具体查询返回某个 URL、某查询为零，或以零结果证明没有公开发布说明／归档。表中 URL 是手工记录的发现线索，不能替代原搜索响应或页面全文，也未逐条自动校对工具输出。独立预列的 CDX 查询、各回放 URL、保存文字及其证据锚不以这些查询归属成立为前提；对于回放仍需遵守人工转存、重建和隔离的各自限制。

## 原始记录保留与显式警示

在更新表之前，把每个**当时的手工元数据文件**按原字节单独复制如下；它们不是网页原件，也不是搜索工具原始 JSON。原有文件名及每一行原字段保持，分别在每个现行表的每行追加 `query_attribution_status` 警示字段，不合并结果记录：

| 文件 | 行数 | 更新前原始字节数 | 更新前 SHA-256 | 原字节副本 |
|---|---:|---:|---|---|
| [discovery-metadata.csv](discovery-metadata.csv) | 32 | 5,085 | `60ae4759f747f0f20739daf5b500fc815eed87241de7a3535be30e080bb4cb3a` | [单独副本](metadata-attribution-originals/discovery-metadata.csv) |
| [upgrade-discovery-metadata.csv](upgrade-discovery-metadata.csv) | 7 | 1,103 | `6d285e57a05e37b9dc46c67240c61d3b19b22fc5bd2523817c81a40a9a91d7cd` | [单独副本](metadata-attribution-originals/upgrade-discovery-metadata.csv) |
| [archive-discovery-metadata.csv](archive-discovery-metadata.csv) | 7 | 926 | `f32b1139b8f09ea1df222c322870cc899b9b44a8f5269388c069a08af6aed9b3` | [单独副本](metadata-attribution-originals/archive-discovery-metadata.csv) |

两个零结果标记只是这两张表中原有的各一条**未核实标记**，不再归因给 Q11 或 Q14。未通过重新搜索来倒推过去的结果：搜索索引和排序会变化，重新查询不能证明先前工具调用的对应关系。

此次修正依据是在核验中发现缺少可靠映射记录；并非外部站点状态变化。它不影响已明确归档 URL 的历史来源定位，也不新造独立来源或声明任何检索已穷尽。日期仍区分会话给定日 `2026-10-26` 与沙箱钟显示 `2026-11-19`；不能以任一个倒填历史网页的真实采集日。
