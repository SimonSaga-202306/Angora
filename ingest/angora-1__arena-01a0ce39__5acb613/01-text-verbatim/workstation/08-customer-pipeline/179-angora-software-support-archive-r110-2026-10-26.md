# r110 · Angora 历史软件支持：升级、堆叠、认证与 CLI

> **结论先行**：本轮通过互联网档案馆取得 Angora 支持知识库的历史可见文字，补上 r109 尚未验证的文档层；但它们是厂商历史说明，不是现行兼容清单、软件发行记录、客户现场或独立测试。英文 TACACS 指南写版本**大于 4.0**，土文写 **4.0 及以上**；恰好 4.0 的支持边界不能由我们自行确定。堆叠、升级和 CLI 文档中也有需要保留的条件与歧义。
>
> 五个支持站直连均返回 522 错误内容；历史回放有一份只显示标题、另一份回放了无关页面，均已隔离。**回放索引显示 200 不等于抓到了目标正文。** 未访问设备、客户或服务门户，未下载固件或官网 PDF。

[来源及完整回读](../../../65-source-evidence-r110-2026-10-26/README.md) · [29 个保存产物目录](../../../65-source-evidence-r110-2026-10-26/source-catalog.csv) · [45 条原文行锚](../../../65-source-evidence-r110-2026-10-26/evidence-traceability.csv) · [19 项边界](../../../65-source-evidence-r110-2026-10-26/claim-boundaries.csv) · [双语对照](../../../65-source-evidence-r110-2026-10-26/cross-language-comparison.csv) · [具名增补与限定](../../../65-source-evidence-r110-2026-10-26/issues-and-corrections.csv) · [档案附录](../09-orders/120-angora-orders-dossier-2026-10-21.r110-appendix.md) · [字段映射](../09-orders/120-angora-orders-master-2026-10-21.mapping-r110.md) · [审计](../../../67-audit-r110-2026-10-26.md)。

## 一、先看来源：历史厂商说明，不是独立证人

七份可分析的回放各有独立保存文件：2021 年[英文 TACACS](../../../65-source-evidence-r110-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/tacacs-authentication-with-cisco-ise/20210227205859/index.visible.md)和[土文 TACACS](../../../65-source-evidence-r110-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/tacacs-kimlik-dogrulama-cisco-ise-kullanarak/20210227213435/index.visible.md)；2022 年[堆叠](../../../65-source-evidence-r110-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/stacking/20220118063431/index.visible.md)；2025 年[英文升级](../../../65-source-evidence-r110-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/software-upgrade-tftp-verge/20250211051945/index.visible.md)、[土文升级](../../../65-source-evidence-r110-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/yazilim-guncelleme-tftp-verge-anahtarlar/20250211062909/index.visible.md)、[土文 ZTP](../../../65-source-evidence-r110-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp/20250123060822/index.visible.md)和[土文 CLI](../../../65-source-evidence-r110-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/komut-satiri-kullanimi/20250123072550/index.visible.md)。日期为档案馆捕获时间，不是文章首次发表日或我们的真实采集日。

这是工具可见 Markdown 的人工转存，包含档案工具栏和同一回放内的各个分块；没有取得原 HTML、图片、固件或自动逐字校对。英／土文是同一厂商的不同文件，不是两次独立试验。另有两份不同日期回放以较早转存为模板重建，已单独标注，**不用于本报告的精确引文或证明跨快照未变**。

## 二、TACACS：版本边界、身份认证和命令授权要分开

| 问题 | 历史文档可见文字 | 正确的证据边界 |
|---|---|---|
| 最低软件版本 | 英文 `version greater than 4.0`；土文 `4.0 versiyonu ve üzerini`（4.0 及以上）。`AUTH-EN-V`、`AUTH-TR-V` | 按字面，英文排除恰好 4.0、土文包含；同一段随后又泛称各型号／软件。**4.0 恰好这一点未解决**，不能替厂商选一个，也不能推断现在的全部产品。 |
| 用户登录与回退 | 两份示例均把服务器不可达与服务器明确拒绝区分开：只有不可达时示例才称可用本地用户。`AUTH-EN-FALLBACK`、`AUTH-TR-FALLBACK` | 这是特定示例的厂商说明，不是我们测试过的所有故障模式或生产配置建议。 |
| 命令授权 | 英文说当时 Verge 不支持 `tacacs command authorization`；土文有对应表述。`AUTH-EN-CMD`、`AUTH-TR-CMD` | **不能把用户登录认证、命令授权和计费合为一个功能**；也不能因历史文本断言当前固件仍不支持命令授权。 |
| Cisco ISE | 英文文档说编写示例时使用 ISE **2.6**，称示例经过基本用途测试。`AUTH-EN-ISE`、`AUTH-EN-TEST` | 是当时文档作者的说法；未取得独立测试记录、具体硬件、兼容矩阵或当前 ISE 版本声明。 |

这比只写“支持 TACACS+”更有商业判断价值：招标／技术评估应区分软件版本、登录认证、命令级授权、回退条件和实际测试，但这里没有安排主动联系或生产网测试。

## 三、软件升级：有双镜像描述，不等于已经验证可回滚

2025 年英／土文升级指南分别描述 AngoraOS 边缘交换机通过 **TFTP 或 USB** 加载镜像；英文说明 `Active-image` 是正在运行的镜像，加载后新镜像列为 `Inactive-image` 并设为下一次重启使用；还要求留意配置保存并建议在网络故障情形保有控制台访问。`UP-EN-METHOD`、`UP-EN-IMAGE`、`UP-EN-INACTIVE`、`UP-EN-CONSOLE`、`UP-EN-SAVE`。

- 文中的 `image_5.5.3.03.bin` 是**示例文件名**，不是我们取得的二进制、最新发布版本、发布时间或已安装证据。也不能把它与 r101 的 `7.3.13`、`ac5-release-7.5.0.bin` 或任何客户设备自动对应。
- 指南显示两种镜像状态和下一次重启的描述，**不证明所有型号均有相同分区、兼容任何版本、可无损升级或保证回滚**。截图仅为链接，图像本身没有取回。
- 两种语言的保存文字均提到 USB 的 FAT32／ExFAT 与约 8–10 秒识别；英文另写 15 秒未就绪代表格式问题，土文则在约定等待后建议重新格式化。`UP-EN-WAIT`、`UP-TR-WAIT`。这是不同保存稿中的表述差异，不证明格式是唯一故障原因，也不能断言原网站某种语言翻译必错。
- 土文回放链接一个 Angora 服务门户，称可从中取得最新软件；**只证明当时页面这样写和链接**，本轮未登录、下载或验证该门户现状。文档把直连电脑称作防止网络中断的更可靠方式，不能从这句话推断传输加密、签名验证或供应链安全已被证明。

## 四、堆叠：容量上限必须和兼容、恢复行为一起看

2022 年[堆叠回放](../../../65-source-evidence-r110-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/stacking/20220118063431/index.visible.md)称不同型号的 Angora 边缘交换机可堆叠、最多 **8 台／400 个可用端口**，描述环或链结构及通过 10G SFP+ 连接。它同时明确说兼容检查涉及**软件和硬件**，成员须使用相同软件；加入设备兼容验证失败时关闭的是**新设备的端口**。`STACK-MAX`、`STACK-TOPO`、`STACK-CABLE`、`STACK-SYNC`、`STACK-HW`。

这不是全部 Verge 型号都可任意混堆的表格，也不是 400 口现场交付证明。关于新设备被改成 `its own software version` 的英文指代并不清楚；结合上下文可知页面要求同软件，但不能自行补成已确定的逐型号固件迁移规则。文档列同步时的 syslog 字段，不证明任何客户现场真的发生了同步。

厂商另写备机接管最多 **30 秒**；冷备复制配置，但不复制所列 STP、MAC、组播和 LACP 动态表，接管时重新计算；其文字又声称除瞬间外不丢包。`STACK-TAKEOVER`、`STACK-DYNAMIC`。这些是同页的历史主张，**不是零中断／零丢包实测，也不能把 30 秒角色切换当业务恢复 SLA**。

选主段落分别写运行时间差**小于**和**大于** 10 分钟，并另提相同 10 分钟时段视为同龄；对**恰好 10 分钟**及两段如何对应没有给出足够清楚的统一规则。保留歧义，不虚构边界。`STACK-AGE`。

## 五、CLI 与零接触：接口示例不自行改写

[2025 CLI 土文回放](../../../65-source-evidence-r110-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/komut-satiri-kullanimi/20250123072550/index.visible.md)列出级别 1／15、用户／特权／全局配置／接口配置等命令区域，并称选定接口范围后变更会作用于所选接口。`CLI-LEVEL1`、`CLI-LEVEL15`、`CLI-AREAS`、`CLI-RANGE`。这些是该历史文档中的角色说明，不能推断所有当前固件权限矩阵；我们没有登录或执行命令。

同一文档把接口编号通式写为 **`[设备编号/0/接口编号]`**，后面例子却分别使用 **`1/1/1`** 和 **`1/2/1`**，中间段并非 0。`CLI-TEMPLATE`、`CLI-EXAMPLE1`、`CLI-EXAMPLE2`。可能存在版本、设备或文档解释未给出的条件；不能自行断言哪一个正确、归咎设备缺陷或将示例用于未知 SKU。

[ZTP 土文回放](../../../65-source-evidence-r110-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp/20250123060822/index.visible.md)称设备通过 DHCP 取得地址，并通过选项 **66／67** 提供的 TFTP 服务器及文件名获取配置，随后加入运行配置；文档还自称自首个软件版本即有该功能。`ZTP-INITIAL`、`ZTP-METHOD`、`ZTP-RUNNING`、`ZTP-66`、`ZTP-67`。这是厂商机制和历史自述，不是部署日志或全部型号／版本证明；本轮也没有取得配置来源认证、完整性或安全策略的独立证据。

## 六、与旧轮的关系：具名增补，不倒推

1. **增补 r109 `lifecycle-claim-boundaries` L09／报告第三节**：r109 当轮未验证在线 CLI／how-to，仍是当时事实；本轮取得部分**历史回放的可见文字**，不是替 r109 追认当时已抓取，也不证明当前站点、文档更新频率或售后 SLA。五个直连目标本轮仍返回 522。
2. **限定 r101 `170` 的平台映射**：AngoraOS 说明与旧 CENTEC／AC5 手册、7.3.13 及 7.5.0 文件卡继续分开；名称或版本数字相近不证明同固件、同设备、客户集成或验收。
3. **限定 r105 `174` 的家族规格外推**：堆叠页的不同型号描述与兼容条件同时成立，不能把上限或混堆能力无条件贴给每款 Verge 型号。既有逐型号／订单分离原则保留。
4. **复核 r105–r109 的时间口径**：那些报告注明的会话指定日 **2026-10-26 UTC** 与本会话给定日期相符；沙箱 UTC 钟显示 **2026-11-19**，二者冲突、未独立校准。不能仅凭沙箱钟把旧会话日期宣布为错误，更不能把它倒填为旧网页采集日期。r106 以给定日期判断较晚推荐栏，只是相对该日期的判断，不是已核实的网页发布时间。
5. **限定本轮 AR11 编号说明和 AR09 转存**：保留 CLI 模板与示例的不一致；AR09 相关文章链接标题一处人工漏字已在提交前根据工具结果更正。人工转存全文尚未自动逐字核对，不能宣称 byte-identical。

## 七、执行范围、失败与下一步边界

**全量读取完成（本轮限定本地清单）：48/48 个不同路径、258,517 bytes，逐项完整字节读取并记 SHA-256。** 其中既存比较材料 14 条／100,177 bytes；本轮已存回放、错误、索引和 GitHub 数据 28 条／130,178 bytes；r109 五份路径清单 5 条／12,813 bytes；补充 CLI 1 条／15,349 bytes。这不是全仓遍历或 48 份独立原件。14 条既存比较路径与 r109 的 49 条有 **4 条重合**；研究范围不同，不能仅凭数量判断覆盖面。

11 个档案回放的 **20/20 工具块**已取：7 份按捕获分别直接转存，2 份从既存模板重建并降级，1 份仅标题、1 份无关页面隔离。九个筛选后 CDX 响应共列 35 条按每次查询 digest 折叠的索引记录，查询截止 `2026-10-26`，不是全历史；四次 GitHub 查询返回零也不证明没有其他镜像。五个直连 URL 均是 522 错误页面，不能证明网站永久离线。没有原 HTML、截图、设备测试、正式兼容矩阵、补丁支持周期或客户验收。

**搜索归属修正**：14 次预列搜索的手工元数据缺少足够的并行调用—返回映射，不能确信每行的查询编号、排序或零结果标记。现已逐行警示并保留三个表各自的原字节副本；不能据它声称特定查询为零。历史回放的结论依赖分别列出的归档 URL 和保存文字，不依赖搜索分组。详见 [C12](../../../65-source-evidence-r110-2026-10-26/discovery-attribution-correction.md)。

**顺序与范围偏差披露**：五份新建错误页曾即时读回、九份 CDX 文件先解析、AR09 曾局部查看以纠正手抄字，均先于汇总文件范围清单；相应目标 URL 已在抓取前列计划，这些文件后来均完整列入并回读。[D04 明细](../../../65-source-evidence-r110-2026-10-26/local-scope-deviation-D04.md)；不把回读哈希说成首次访问顺序的证明。预列并完整回读的三份既有报告含旧订单或已停事项概述，比较范围选择过宽；未重新打开底层文书、未据停项产生新结论或跟进，详见 [D05](../../../65-source-evidence-r110-2026-10-26/local-scope-deviation-D05.md)。

入场环境钟为 `2026-11-19T10:57:43Z`，工作中后一次为 `2026-11-19T11:41:47Z`，相差约 **44 分 05 秒**；钟与会话日期冲突且未独立校准，后续仍继续整理核验。未穷尽 Angora 的商业信息；没有对已 PASS 的旧单、财务差异、RFQ/RFP、48 口澄清、报价或官网 PDF 作新分析或跟进。旧主档仅做哈希／前缀校验和限定末尾追加，不解释停项内容；既有报告的混合范围按 D05 披露。
