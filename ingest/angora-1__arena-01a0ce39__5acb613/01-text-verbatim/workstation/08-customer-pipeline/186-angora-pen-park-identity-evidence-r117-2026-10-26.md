# r117 · Angora 历史深挖：2021 企业编号、科技园与同名辨别

> **结论先看**：历史版本库显示，`58029 / Angora Networks` 这一企业编号记录在一个镜像的 **2021-10-20 16:45:45 UTC** 自标提交中新增；父子完整文件及变更已逐字节和 Git blob 核对。这是**镜像记录的时间锚**，不是精确获配时间、工商登记、客户订单或交付证明。科技园旧目录和人物同名问题也补了证据，法人仍为 **主体未确认**。

[来源与路径目录](../../../92-source-evidence-r117-2026-10-26/source-catalog.csv) · [逐项证据锚](../../../92-source-evidence-r117-2026-10-26/evidence-traceability.csv) · [来源限制](../../../92-source-evidence-r117-2026-10-26/source-observations-and-limitations.md) · [具名更正](../../../92-source-evidence-r117-2026-10-26/issues-and-corrections.md) · [独立档案附录](../09-orders/120-angora-orders-dossier-2026-10-21.r117-appendix.md) · [主体映射](../09-orders/120-angora-orders-master-2026-10-21.mapping-r117.md) · [单主体备忘](../../../93-followup-angora-r117-2026-10-26/angora-networks.md) · [审计与回读](../../../94-audit-r117-2026-10-26.md)。

## 1. 从“当前登记行”推进到 2021 年镜像变更

| 证据 | 已核实的限定事实 | 不能推出 |
|---|---|---|
| IETF 版本库 [父提交](https://github.com/ietf-tools/iana-registries/commit/ae9ceebec6bf7a4034e6c8d6768e13b7f4f95883)／[子提交](https://github.com/ietf-tools/iana-registries/commit/fe367b60547788ed755be66dbec17e819f63c77c) | 子 commit 自标 **2021-10-20 16:45:45 UTC**；完整父文件中精确行 `58029`、`Angora Networks` 均未命中，完整子文件第 **231668–231669 行**相邻列出这两项，第 231670 行列联系人姓名。父文件 4,425,964 bytes、子文件 4,426,103 bytes，Git blob 均与 API 匹配。 | IANA 在 16:45:45 直接分配；这一定是全网首次出现；编号证明法人或设备已经使用。 |
| [本地父子差异](../../../92-source-evidence-r117-2026-10-26/pen-ietf-parent-child-local.diff)／[核对结果](../../../92-source-evidence-r117-2026-10-26/pen-ietf-parent-child-comparison-result.json) | 本地 Git diff 的 hunks 与 GitHub commit API patch 一致，均新增该数字与名称。父子文件头均自标 `last updated 2021-10-20`，但这是整份登记清单的日期。 | 清单全表更新时间就是该编号的获配时刻；Git commit 自报时间具有不可伪造的独立授时。 |
| [另一版本库的 2021-10-27 提交](https://github.com/rfinnie/iana-tracker/commit/0829494816a42c337fe42e869ee9114b816a96ee) | 对应父子文件分别不含／含同一记录；本地 diff 与该 commit 的 API patch 一致。IETF 的父文件与该镜像父文件**逐字节相同**；IETF 10-22 文件与该镜像 10-27 文件也**逐字节相同**。 | 两份历史副本是两家独立登记机构或两次独立分配；两份镜像能证明交易、认证或交付。 |

**修正／取代 r116 mapping 中继续沿用 r114 的“PEN 时点未知”这一宽泛表述**：此前只见本次 IANA 页面登记行，现在有上述 2021 年镜像出现的时间锚。**r114 对精确分配时间未知的限定仍成立**，2026-10-26 当日状态亦未仅凭历史文件证明。16 份完整历史文件分路径保留并与 Git blob 对照，是版本链而非 16 个独立证人。

PEN 的 `1.3.6.1.4.1` 命名空间与 r116 的 MAC `/36` 不同；编号大小不能推算产量、客户数或出货数。GitHub 仓库描述其为 IANA 清单镜像，尚未取得 IANA 当年原始分配通知或工商原证。

## 2. 科技园：补齐两次旧回放，仍不能反推入驻时间

- 对 r116 未保存正文的 2022-10-01、2024-02-26 两个 `www.kirikkaleteknopark.com` 回放，本轮**分别重新请求四块**，每块独立留存。对本地八个文件按 `angora` 不区分大小写扫描均零；这只是本轮工具可见文本的字符串结果，不是现实中未入园的证明。2024 年第 1–3 块依据目视相同的 2022 文本与本次边界重构，未与工具原响应自动逐字节比对。[扫描](../../../92-source-evidence-r117-2026-10-26/park-new-full-scan-results.json)／[方法](../../../92-source-evidence-r117-2026-10-26/source-observations-and-limitations.md)。
- r116 所存的 [2024-09-20](../../../88-source-evidence-r116-2026-10-26/archive-chunks/kirikkaleteknopark.com/firma-rehberi/20240920103752/chunk-0.visible.md#L100-L108) 与 [2026-01-20](../../../88-source-evidence-r116-2026-10-26/archive-chunks/kirikkaleteknopark.com/firma-rehberi/20260120061616/chunk-0.visible.md#L100-L108) `non-www` 回放则列 Angora 和域名。不同主机、网站改版、分页或其他名称都可能影响比较；不能据这些样本算出入驻／离开日期或证明采购。
- [2023 年 ICT Media 访谈摘要](../../../53-source-evidence-r107-2026-10-26/corrected-r106/ictmedia.com.tr/haber/yerli-bir-ureticiye-verilebilecek-en-buyuk-destek-onun-urunlerini-kullanmaktir/index.tr.extracted.md#L81-L83)引述负责人称已转到 `teknokent`、设计与生产在向园区转移。**该段没有点名 Kırıkkale**，不能因后来目录列名就断言 2023 年所指必是同一园区；访谈是企业表述，不是独立交付证明。

## 3. 同名人：避免把公职履历错归给创始人

[r114 的 2021 组织方归档简介](../../../81-source-evidence-r114-2026-10-26/archive-replay/ortakakil.org.tr/ozgecmisler/levent-kilic/20210622052721/index.visible.md#L48)称 Angora 创始合伙人 Levent Kılıç 有电子工程背景；本轮 [Sincan 政府简介](../../../92-source-evidence-r117-2026-10-26/external-visible/sincan.gov.tr/makam/chunk-0.visible.md#L41-L47)的同名官员所列出生年份、教育和履历不同。资料本身仍可能有误，且政府页是动态当前文本；但**仅同名不能合并身份**，不把该官员的职位、2020 活动或其他履历归给 Angora 创始人，也不另建客户。

## 4. 延续旧轮、日期及尚未完成

- **增补 r116**：新增 2021 PEN 父子变更、补录两次园区回放和同名防误认；不改变 2019 MAC 映射、地址比较或法人未确认的边界。**延续 r115**：培训方伙伴展示不等于开班，e-Safe 候选不等于获奖；10-20 能源项目报道中的 10-28 展示按当前会话日期仍是计划。
- **更正 r117 研究计划的用户截止表述**：2026-10-26 是会话提供日期及本轮分析边界，不是用户另行指定的截止。容器墙钟显示 2026-11-20，未经校准；网页自标日、Git commit、Wayback 捕获及实际取文分开。自标 10-29 结果与 10-31 商会目录均晚于会话日，不作为截止前事实。[时间纠正](../../../92-source-evidence-r117-2026-10-26/date-scope-correction-r117.md)。
- 访谈原视频工具返回 **177 块**，首块却是大量动态 JavaScript；只保存第 0 块和修订记录，**没有完整字幕或原音**，不以此证明采访内容。商会目录仍只有 r116 的首块；其余八块本轮未取。没有官方工商原件、采购／合同或实际履约凭据，不声称穷尽。
- 本轮没有新增 Ewind 事实、未联络任何主体、未操作设备或访问关闭的 Gmail／Drive。C 档不跟进，重复主体只交叉提示、最多联系一次；所有既定 PASS 和停项持续有效。

## 5. 采集与可核验性

先列后完整读取旧轮限定清单 **33/33 路径、172,338 bytes**；补充旧园区／媒体 **13/13、120,172 bytes**；同名对照 **2/2、14,468 bytes**。16 个历史编号文件 **70,958,756 bytes**均完整回读、UTF-8 解码并与 API Git blob 匹配；本轮新园区 8 块 **8/8、55,657 bytes**完整读取。这些数字有重叠路径和同源副本，不能相加当作独立证人数。

20 次预列检索人工计 44 条结果，含重复和无关，3 次零结果；**16/20 响应手工转存，4 次因隔离、财务或带签名 URL 不保存全文**。网页及搜索结果均非原 HTML／原 API 字节，人工转存仍有误差；当前轮限定产物的完整清单、SHA、测试和真实耗时见[审计](../../../94-audit-r117-2026-10-26.md)。
