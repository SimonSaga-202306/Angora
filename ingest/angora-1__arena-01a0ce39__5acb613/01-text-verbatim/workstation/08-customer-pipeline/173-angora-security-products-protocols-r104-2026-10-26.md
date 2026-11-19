# r104 · Angora 网络安全产品与工业协议：产品、公告及证据边界

> **结论先行**：Angora 官网把 Arrow 描述为 Guardian／Postman 组成的单向数据传输方案，并在 2023 年公告中声称加入 ModBUS、OPC；Karınca 是带实体端口的网络包代理，Arı／BEE 是多型号安全处理硬件平台。以上是**厂商文字和历史索引**，不是独立协议互通测试、客户部署、销量或验收。

[来源范围与全文保存方式](../../../41-source-evidence-r104-2026-10-26/README.md) · [44 条证据行锚](../../../41-source-evidence-r104-2026-10-26/evidence-traceability.csv) · [协议能力矩阵](../../../41-source-evidence-r104-2026-10-26/protocol-capability-matrix.csv) · [公告日期矩阵](../../../41-source-evidence-r104-2026-10-26/publication-dates.csv) · [逐项纠错](../../../41-source-evidence-r104-2026-10-26/issues-and-corrections.csv) · [订单档案映射](../09-orders/120-angora-orders-master-2026-10-21.mapping-r104.md) · [内部记录](../../../42-followup-angora-r104-2026-10-26/angora-networks.md) · [审计](../../../43-audit-r104-2026-10-26.md)。

本轮**不联系客户、不操作设备**。旧索引记载“主动下载官网 PDF 数据表”已 PASS；发现前本轮和 r103 已解析过部分官网 PDF 链接，本轮四份 PDF 文字产物隔离留存、不用于下述技术结论，之后不再访问此类链接。没有保存 PDF 二进制。

## 一、三条产品线，不能混成同一功能

| 产品/范围 | 可观察到的厂商表述 | 不能推定 |
|---|---|---|
| [Arrow 数据二极管页面](../../../41-source-evidence-r104-2026-10-26/external-visible/www.angoranetworks.com/angora-data-diode/index.en.extracted.md) | 受限、受保护网络一侧的 **Guardian** 接收并准备数据，另一侧 **Postman** 转发或存储；页面称可选多个 Postman，并称特殊单向光纤模块阻断逆向传输。网页还列文件、Syslog、SNMP、SCADA、HTTP/HTTPS、Web API 和 ICAP 对外安全应用等。 | 不证明物理隔离、反向阻断、完整性或性能已由独立机构验证；“SCADA”是系统／场景名称，不是单一线缆协议。ICAP 是对外集成的厂商描述，不能推定杀毒／DLP 引擎必然内置或免费。 |
| [Karınca 网络包代理页面](../../../41-source-evidence-r104-2026-10-26/external-visible/www.angoranetworks.com/yerli-network-packet-broker/index.en.extracted.md) | 描述 ASIC＋x86 物理平台、流量复制／分发、L2–L4 分类和负载均衡；表列 48 个 1/10/25G 与 6 个 100G 口。SSL 段说把流量分发至算法处理／SSL 设备，不等于本机独立解密。 | 不是 Arrow 单向隔离设备；“100% 交付、无延迟”等营销措辞不是实测。页面没给出可核实测试条件或部署记录。 |
| [Arı／BEE 安全硬件页面](../../../41-source-evidence-r104-2026-10-26/external-visible/www.angoranetworks.com/network-packet-broker-test/index.en.extracted.md) | 安全处理／SD-WAN 硬件平台，列 7 个 `ANW-ARI-*` 型号；厂商提及 pfSense、OPNsense、PacketFence、OpenWISP、Cuckoo 等应用。`ANW-ARI-1200` 表列 ARM，其余所列为 Intel。 | 列举开源软件不是每款 SKU、每个版本的兼容测试；x86 软件叙述不能自动套用 ARM 机型。SD-WAN 硬件不等于这些软件均预装、持证或实际运行。 |

Arrow 页面还声称加密、指纹清理、脱敏、分层权限、日志／SIEM 和功能授权；具体算法、密钥管理、脱敏规则、默认许可及审计结果均未取得。**单向链路的宣传不能等同于对所有攻击或泄露的防护承诺**。页面上的机构 logo 是网站的参考展示，不能归属于某条产品线或当作对应订单与验收。

### 协议支持要保留的空白

[2023 英文公告](../../../41-source-evidence-r104-2026-10-26/external-visible/www.angoranetworks.com/angora-networks-unveils-game-changing-modbus-and-opc-protocol-support-in-its-data-diode-solution/index.en.extracted.md)和[土耳其语版本](../../../41-source-evidence-r104-2026-10-26/external-visible/www.angoranetworks.com/angora-networks-veri-diyotu-cozumunde-ezber-bozan-modbus-ve-opc-protokolu-destegini-tanitti/index.tr.extracted.md)同属 Angora，不是两份独立测试。英文正文首段工具可见文字存在断裂，已原样保留；两种语言均声称集成 ModBUS 和 OPC，并宣传实时监控，但没有说明 **Modbus TCP／RTU、功能码、读写与代理方式，也没明确 OPC UA／Classic、安全模式和具体版本**。因此不能把通用名称转成完整协议矩阵，不能声称任意控制器已互通。

Syslog、SNMP 和 HTTP/HTTPS 列表也未给出版本、消息模式、代理和授权；不能将常见的双向请求／响应直接假设为跨单向链路端到端工作。这里只记录技术边界，不联系客户询问，也不试图接入现场系统。

## 二、公告时序：正文、索引和旧 CMS 字段分列

| 事项 | 公告正文原有日期 | 索引／旧 TSV 字面日期 | 解读 |
|---|---|---|---|
| Cisco ISE | 英文正文 `June 21, 2021`；声称一个项目中完成交换机 802.1X 等软件开发。 | 英文新闻索引 `06/25/2021`；旧 WordPress 帖子 TSV 的对应 `date` 字段为 `2021-06-25T17:48:14`。 | 项目客户主体未公开；没有型号、版本、现场记录或独立验收。正文日期与索引字段不是同一概念。 |
| PacketFence NAC | 土耳其语正文 `26 Ağustos 2021`；厂商声称与伙伴完成测试。**英文页开头却写 June 21、Cisco ISE**，正文之后才讨论 PacketFence。 | 英文索引 `09/01/2021`；旧 TSV 字段 `2021-09-01T14:26:19`。 | 应保留语言版本的差异；厂商声称测试不等于取得测试报告，更不等于特定客户部署。不能用英文页错位开头确定 PacketFence 完成日。 |
| Arrow 发布 | 英文稿正文 `October 10, 2022`。 | 英文索引字面 `10/09/2022`。 | 两处日期不同，不猜测时区或把其中一个当成安装／首销日期。 |
| ModBUS／OPC | 英文正文 `December 05, 2023`，土耳其语 `05 Aralık 2023`。 | 英文索引 `12/06/2023`；两份旧 TSV 同记 `2023-12-06T14:27:03`。 | 2023-12-05 是**正文日期**，2023-12-06 是索引／旧 CMS 字段，不是已证功能上线或客户使用日期；TSV 未给出时区。 |

英文索引和两份旧 WordPress TSV 均有范围与采集方式限制，不是对其他语言、全部新闻渠道或当前全站历史的穷尽。英文／土耳其语文本和多个官网 URL 仍然来自同一厂商；相互印证文字不构成独立验证。

## 三、可复核的文字差异和计算

1. **Karınca 的指标名称不同**：页面正文写“最多 `1Tbps traffic distribution`”，技术表写 `Traffic Limit 1.9 Tbps`；未给一致的计量范围、报文、丢包或测试方法，不能直接判错，也不能把两者当同一实测指标。仅按表列最大端口速率做算术：`48×25G + 6×100G = 1,800 Gbps`，即单方向名义端口速率之和约 `1.8 Tbps`；若每口都能同时全双工则两方向之和约 `3.6 Tbps`。这**不是**转发性能、并发能力、包速或吞吐测试结果。
2. **Arı 型号同名而资料不一致**：[r94 历史报告](163-angora-corporate-chronicle-2016-2026-2026-10-26.md)把 `ANW-ARI-3800` 记为 `C3758`，把 `ANW-ARI-4600` 记为 `C3958 / 4×10G`；本轮厂商英文网页分别写 `C3756`、`C3956 / 2×10G`。旧报告引自先前文书，本轮未取其原件；版本、变更或抽取误差未明。不得静默挑选一组当作同名设备必然配置，也不能据此断言产品缺陷。
3. **检索片段与页面的方向表述**：一次[搜索工具片段](../../../41-source-evidence-r104-2026-10-26/search-visible/query-03-result.json)先写“untrusted → trusted”，随后又写“受保护 → 更开放”；本轮 `fetch_page` 可见正文没有前一句，产品正文和发布稿均描述受限网络向开放侧的情形。片段可能陈旧或由搜索工具拼接，不能据它判断设备可逆转或某个现场拓扑；原始 HTML 和实际设备均未取得。
4. **旧 TSV 的行数与字段差异**：r39、r40 两份页面 TSV 各有 **25 条数据行／25 个 ID**，文件头却各写 24；r39 帖子 TSV 有 **10 条／10 个 ID**，文件头写 9。r39 与 r40 的帖子 TSV 各有 10 条，10 个 ID 的 `date` 和 `modified` 值相同，但 **2 个 slug 字段不同**（ID 777、803），因此 r40 的“完全一致”不能按所有字段成立。逐行比较见[页面表](../../../41-source-evidence-r104-2026-10-26/wordpress-pages-compare.csv)和[帖子表](../../../41-source-evidence-r104-2026-10-26/wordpress-posts-compare.csv)。这只修正**已存 TSV 的计数与比较**，不是重新取得原始 API，也不能证明网站总记录数或 slug 何时改变。

## 四、具名修正与上一轮差异

- **修正并取代 r94 `163` 对 Karınca“唯一的纯软件许可型产品线”的断言**：本轮页面明确描述实体 ASIC、CPU、端口、电源和风扇；仅凭此也不能排除另有软件授权或软件版本，授权形式未确认。
- **修正／限定 r94 `163` 的 ARI-3800／4600 单一配置、`2023-12-05` 唯一新闻日期，以及“2024–2026 传播停摆／2026-06-15 必然站点迁移”判断**：保留不同来源及日期字段；批量相同 `modified`／`lastmod` 本身不能证明迁站原因，也不能排除其他渠道发布。[订单档案附录](../09-orders/120-angora-orders-dossier-2026-10-21.md)和[本轮映射](../09-orders/120-angora-orders-master-2026-10-21.mapping-r104.md)同步具名记录，旧前缀不改。
- **修正 r39／r40 已存 TSV 的文件头计数及 r40 帖子“完全一致”表述**，见上表和逐行比较；不重写旧 TSV。
- **复核 r101／r102／r103 日期，而非无依据倒改**：三轮文件标会话日期 `2026-10-26 UTC` 并记录环境时钟 `2026-11-19` 的冲突；按当前会话提供的日期，不能仅因为环境时钟就认定三轮日期误写，也不能把环境日期当成经独立验证的网页采集日。[逐文件日期行](../../../41-source-evidence-r104-2026-10-26/date-claims-index.csv)可查。
- 相比 r103 的**型号、端口和 IRIS**，本轮转为安全产品与协议。r103 的 16 项本地来源与本轮 10 项旧网站／TSV 清单按路径重合 **0**；本轮 10 项中 6 项旧综合镜像不作结论依据、4 项 TSV 用于字段核对。数量和交集的差别来自范围变化，不是删除资料，也不代表已穷尽 Angora 业务。

**全量读取完成（限定本地范围）：10/10 个旧网站／TSV 文件、100,270 bytes；另 2/2 方法文件 8,555 bytes、9/9 日期复核文件 45,091 bytes、7/7 背景／前缀文件 150,595 bytes，以及 7/7 旧轮交集清单 12,932 bytes；共 35/35 个不同路径、317,443 bytes。** 日期复核前三个 README 和 7 个交集清单首次读取在列单之前，已补列回读并披露；其余逐组先列后读。本轮 14/14 个 URL 的 16/16 工具返回块已人工转存，只有 10 个网页 URL 的 11 块用于分析；4 个 PDF URL 的 5 块隔离、不用于结论。人工转存、搜索片段、网页文字层均不是 HTML／PDF 原始字节、图片或实物，且不表示整个官网或企业资料已经穷尽。
