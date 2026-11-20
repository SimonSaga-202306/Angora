# r116 · Angora 历史商业线索：2019 地址范围与科技园目录

> **结论**：Wireshark 上游 2019-02-24 的自动更新把 `Angora Networks` 加入一个 MAC `/36` 映射；Gentoo 随后的历史镜像列出相符范围与 Ankara 地址。Kırıkkale 科技园 2024-09-20 与 2026-01-20 的目录回放也分别列出 Angora 名称和域名。这些是有时间锚的公开记录，**不是工商原证、客户订单、认证或交付证明；法人主体未确认**。

[逐产物目录](../../../88-source-evidence-r116-2026-10-26/source-catalog.csv) · [逐项锚](../../../88-source-evidence-r116-2026-10-26/evidence-traceability.csv) · [问题与纠正](../../../88-source-evidence-r116-2026-10-26/issues-and-corrections.md) · [独立档案附录](../09-orders/120-angora-orders-dossier-2026-10-21.r116-appendix.md) · [主体映射](../09-orders/120-angora-orders-master-2026-10-21.mapping-r116.md) · [单主体备忘](../../../89-followup-angora-r116-2026-10-26/angora-networks.md) · [审计](../../../90-audit-r116-2026-10-26.md)。

**时间口径**：会话日期／截止为 **2026-10-26 UTC**。沙箱墙钟显示 2026-11-20，与会话日冲突且未经校准；不能倒填实际采集时间。Git 提交、Wayback 捕获、网页自标和动态内容分别标记。网页是工具可见文本的人工转存；原始 Git 文件才是 Git blob 校验过的完整字节。

## 1. 2016 主体线索：有第三方记录，未获官方原证

r111 已保存的 [Find 目录](../../../69-source-evidence-r111-2026-10-26/external-visible/www.find.com.tr/Company/angoranetworksbilisimteknolojiticaretsanayianonimsirketi/index.visible.md)列出全称、`28 Kasım 2016` 成立日期及 `ALACAATLI MAH. PARK CAD. 47/31`。同页标记**信息未验证**、记录未经企业确认／关联，工商编号仅会员可见。该日期是商业目录声称，不能写成已核验的工商成立事实；不以名称本身强行合并法人。

## 2. 2019：可追溯到版本库更新的地址范围

| 材料 | 已核事实 | 不可推断 |
|---|---|---|
| [Wireshark 上游提交](https://github.com/wireshark/wireshark/commit/0fcf4b1de93f79cc7d24ecb9c57193a61f822329)，以及[本地 API 原响应](../../../88-source-evidence-r116-2026-10-26/github-api/GH02.body.json) | commit 自标 `2019-02-24 08:32:11 UTC`；`manuf` patch 新增 `70:B3:D5:82:20:00/36  AngoraNe  Angora Networks`。本地[父版](../../../88-source-evidence-r116-2026-10-26/github-raw/github.com/wireshark/wireshark/95bf9f5e0acac09f35cd8e8467cb6d93fb5a0d78/manuf)和[子版](../../../88-source-evidence-r116-2026-10-26/github-raw/github.com/wireshark/wireshark/0fcf4b1de93f79cc7d24ecb9c57193a61f822329/manuf)完整字节均匹配 API Git blob；按预列三个字符串扫描，父版零命中，子版第 26100 行命中。 | 2019-02-24 是实际首次获配日或公司成立日；任何客户已购、设备已用该地址或发生交付。 |
| Gentoo `ma-small.txt` 的[2018 版](../../../88-source-evidence-r116-2026-10-26/github-raw/github.com/gentoo/hwids/41e194e41bcb65e764c67562e2fba877b0b4408b/ma-small.txt)、[2019 版](../../../88-source-evidence-r116-2026-10-26/github-raw/github.com/gentoo/hwids/2986daf9bf2626efe6ff1d62f9713dad6cb82dae/ma-small.txt)、[2020 版](../../../88-source-evidence-r116-2026-10-26/github-raw/github.com/gentoo/hwids/cad1d07b026dd2c04b6940cf9c72b4b8639ae55b/ma-small.txt) | 2018-09-17 文件对所列字符串零命中；2019-03-17 文件第 11069–11073 行列名称、`70-B3-D5`、`822000-822FFF`、Ankara 地址；2020 文件重复范围。三份完整字节均与 API Git blob 匹配。 | 2018 时必然不存在分配；范围的首次登记日；该镜像是 IEEE 的独立签发证书。 |

`/36` 的固定前 36 位对应 `70:B3:D5:82:20:00` 至 `70:B3:D5:82:2F:FF`，即数学上 4,096 个地址；这是范围大小，**不是制造或出货数量**。共享前缀 `70:B3:D5` 还有其他登记项，不能全部归于 Angora。Wireshark 文件头列 IEEE 与其他多个来源，两个项目可能复用同一上游数据，不是两份独立注册证明。

Gentoo 镜像和 Find 的 `Alacaatli Mah. Park Cad. 47/31` 门牌一致；前者的地址写 `Cayyolu`，后者写 `Yenimahalle`，地区字段有差异。即便相同门牌也只能构成核对线索，不自动证明同一法人。r114 的 [IANA PEN 58029](../../../81-source-evidence-r114-2026-10-26/external-visible/www.iana.org/assignments/enterprise-numbers/page-581/index.visible.md) 与 MAC 属不同命名空间；其分配日和会话截止时有效性仍未知。

## 3. 2020–2026：渠道页与机构目录

- **Advensis 网站**：英文页 [2020-10-21](../../../88-source-evidence-r116-2026-10-26/archive-replay/advensis.com.tr/en/angora-en/20201021095900/chunk-0.visible.md)／[2022-01-23](../../../88-source-evidence-r116-2026-10-26/archive-replay/advensis.com.tr/en/angora-en/20220123023037/chunk-0.visible.md) 回放分别保存完整的一块工具可见文字，多为图片链接及页脚；图片未下载。两次页脚地点不同只说明网页文本不同，不能推定实际搬迁日。与 r114 土文回放同属一个发布方，不以图片名证明代理协议、销售或交货。
- **科技园目录**：[2024-09-20 回放](../../../88-source-evidence-r116-2026-10-26/archive-chunks/kirikkaleteknopark.com/firma-rehberi/20240920103752/chunk-0.visible.md)和[2026-01-20 回放](../../../88-source-evidence-r116-2026-10-26/archive-chunks/kirikkaleteknopark.com/firma-rehberi/20260120061616/chunk-0.visible.md)均列 `Angora Networks Bilişim` 和域名。各 4 块已分开存；后一回放是本轮为留存逐块重发的请求。同一目录两次捕获不等于两个独立见证，不说明首次入驻、始终在园或发生采购。2020-12-05 回放的四个已存工具文本块按 `angora` 匹配零命中，**不等于当时未入园**，也不能排除其他名称或转存问题。
- **2019 支持页去重**：`?p=330` 的 CLI 公告已在 r114 保存，2024 捕获正文未显示 2019 日期；英文快启页面的搜索摘要日期没有同期存证，不能当新事实。详见[去重记录](../../../88-source-evidence-r116-2026-10-26/support-dedup-and-discovery-limits.md)。

## 4. 与上一轮差异和待补材料

本轮**增补 r114** 的 IANA／渠道线索：新增 2019 版本库时间锚、两个英文回放及 2024／2026 科技园目录；不修正其原有“分配日未知、图片未读、CLI 发布时间未证”结论。**延续 r115**：培训伙伴展示不等于开班，e-Safe 候选不等于获奖；能源行业媒体的 2026-10-20 预告所说 10-28 决赛仍是截止时的计划，不声称已经举行或 Angora 获奖。

仍缺独立可查的官方工商编号、原始 MA-S 分配时间、合同、订单和实际履约记录。后续只被动找合法公开原证，先列范围并去重，不重新打开既有 PASS、停项主体、官网 PDF 或隔离材料。重复主体只交叉提示、最多联系一次，C 档不跟进；没有新增 Ewind 事实或任何外联。

## 5. 可复核范围和诚实限制

预列 84 次查询已执行，但搜索全文没有全部持久化；查询文件只有人工元数据，不是完整响应或 84 个独立来源。P01、P02、P05 不完整，AR02／AR03 首块未转存；P02 还发生人工转录错误，保留初稿、重发请求并记[具名纠正](../../../88-source-evidence-r116-2026-10-26/P02-transcription-correction-and-refetch.md)。自标 10-29 的报道未取全文，10-31 商会目录自标日期晚于截止，均未当作截止前事实。

限定清单先列后逐文件完整字节回读、记录大小与 SHA-256；具体数量、范围、测试和耗时见[审计](../../../90-audit-r116-2026-10-26.md)。**本轮不声称穷尽；完整读取文件不等于人工转存与网页原文逐字节一致。** 关闭的 Gmail／Drive 未访问，设备未操作。
