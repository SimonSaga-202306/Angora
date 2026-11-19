# r110 · Angora 历史软件支持字段映射（不改订单数据）

| 字段／旧项 | 可登记内容 | 证据与不能推断的内容 |
|---|---|---|
| **增补 r109 L09：文档可见性** | 7 个历史知识库回放分别转存；5 个本轮直连是 522 | [来源](../../../65-source-evidence-r110-2026-10-26/source-catalog.csv)；不推翻 r109 当轮失败，不证明现行可达、更新频率或软件支持承诺。 |
| **限定 r101 `170`：固件身份** | AngoraOS 文档以 `image_5.5.3.03.bin` 作例子 | `UP-EN-SAMPLE`；不能把样例与 7.3.13、AC5 7.5.0 文件卡、CENTEC 手册或某订单关联。 |
| TACACS 软件边界 | 英文 `greater than 4.0`、土文 `4.0 ... ve üzerini` | `AUTH-EN-V`、`AUTH-TR-V`；严格字面在恰好 4.0 处不一致，同厂商非独立；不推断当前所有版本。 |
| 用户认证／命令授权 | 示例区分不可达和拒绝；文档称当时不支持 TACACS 命令授权 | `AUTH-EN-FALLBACK`、`AUTH-EN-CMD`、`AUTH-TR-CMD`；不把认证与授权／计费合并，也不判断现行版本。 |
| 软件升级 | TFTP／USB、Active／Inactive，指南称新镜像在下次重启启用 | `UP-EN-METHOD`、`UP-EN-IMAGE`、`UP-EN-INACTIVE`；没有镜像文件、独立兼容矩阵、回滚测试或上线记录。 |
| USB 诊断文字 | 英文 8–10 秒且另提 15 秒，土文给约 8–10 秒建议 | `UP-EN-WAIT`、`UP-TR-WAIT`；这只是转存差异，不认定唯一故障原因或网站翻译错误。 |
| **限定 r105 `174`：堆叠适用范围** | 文档宣称至多 8 台／400 口；同页要求软件／硬件兼容 | `STACK-MAX`、`STACK-SYNC`、`STACK-HW`；不证明全型号可混堆或现场部署上限。 |
| 堆叠故障切换 | 厂商称角色切换最多 30 秒；动态表不复制并在接管时重算 | `STACK-TAKEOVER`、`STACK-DYNAMIC`；不是独立实测、零丢包证明或业务恢复 SLA。 |
| CLI 编号模板／示例 | 通式中间为 0；示例中间出现 1、2 | `CLI-TEMPLATE`、`CLI-EXAMPLE1`、`CLI-EXAMPLE2`；不自行选取语法或判设备错误。 |
| ZTP | 厂商文档描述 DHCP 66／67、TFTP 及运行配置 | `ZTP-METHOD`、`ZTP-RUNNING`、`ZTP-66`、`ZTP-67`；未验证安全属性、部署或全部版本。 |
| 归档真实性 | AR04 缺正文；AR07 是无关页面；AR02／AR06 为重建 | [回放结果](../../../65-source-evidence-r110-2026-10-26/archive-replay-results.csv)；状态 200 不保证身份，重建稿不作逐字相同或独立证人。 |
| **修正 r110 搜索查询归属** | 并行搜索结果缺少可可靠重建的查询对应；人工元数据逐行降级 | [C12](../../../65-source-evidence-r110-2026-10-26/discovery-attribution-correction.md)；不根据其编号、排序或零标记作事实；各表原字节副本分别保留。 |
| **复核 r105–r109 日期** | 会话指定 2026-10-26 UTC；环境观察 2026-11-19 UTC，冲突未校准 | r105–r109 的会话指定日与本会话给定值相符；不凭环境钟将旧报告日期视为错误，也不倒填真实采集日。r106 的未来推荐栏判断仅相对于所给会话日。 |
| 转存局限与先读 | AR09 一个相关文章链接 title 手抄漏字已更正；错误页、索引及 AR09 局部先读后纳入汇总清单 | `C07`、[D04](../../../65-source-evidence-r110-2026-10-26/local-scope-deviation-D04.md)；URL 已预列、文件后来完整回读；全文未自动逐字核验，哈希不证明顺序。 |
| 停项与联系人 | 未主动联系、下载 PASS PDF、重开底层旧单或操作设备 | 三份旧报告的回读范围含历史订单／停项概述，已披露 [D05](../../../65-source-evidence-r110-2026-10-26/local-scope-deviation-D05.md)；未据停项产生新结论或跟进。旧主档仅核哈希／前缀并限定末尾追加。 |

[主报告](../08-customer-pipeline/179-angora-software-support-archive-r110-2026-10-26.md) · [独立附录](120-angora-orders-dossier-2026-10-21.r110-appendix.md) · [45 条证据定位](../../../65-source-evidence-r110-2026-10-26/evidence-traceability.csv) · [来源说明](../../../65-source-evidence-r110-2026-10-26/README.md) · [审计](../../../67-audit-r110-2026-10-26.md)。
