# Angora 档案独立附录 · r116：历史地址范围与园区目录

> 截止 **2026-10-26 UTC**。这是原档的独立补充，不合并来源或客户；**法人主体未确认**。各证据的时间是提交／归档时间，不自动等于首获分配、入驻、订单、认证或交付日期。

[主报告](../08-customer-pipeline/185-angora-historical-address-park-evidence-r116-2026-10-26.md) · [逐产物目录](../../../88-source-evidence-r116-2026-10-26/source-catalog.csv) · [证据锚](../../../88-source-evidence-r116-2026-10-26/evidence-traceability.csv) · [主体映射](120-angora-orders-master-2026-10-21.mapping-r116.md) · [单主体备忘](../../../89-followup-angora-r116-2026-10-26/angora-networks.md)。

## 1. 2016 目录线索和 2019 技术登记镜像

- **Find 商业目录，非官方登记**：r111 留存页面列公司全称、自标成立 `28 Kasım 2016`，同时写资料未验证、企业未关联、工商编号仅会员可见。[旧页](../../../69-source-evidence-r111-2026-10-26/external-visible/www.find.com.tr/Company/angoranetworksbilisimteknolojiticaretsanayianonimsirketi/index.visible.md)。这一日期是第三方声称，不是本轮取得的原始工商证明。
- **Wireshark 历史提交**：上游 [2019-02-24 自动更新](https://github.com/wireshark/wireshark/commit/0fcf4b1de93f79cc7d24ecb9c57193a61f822329)的 patch 和[完整子版 `manuf`](../../../88-source-evidence-r116-2026-10-26/github-raw/github.com/wireshark/wireshark/0fcf4b1de93f79cc7d24ecb9c57193a61f822329/manuf)加入 `70:B3:D5:82:20:00/36` → `Angora Networks`。完整父版的限定字符串扫描无命中；父、子文件均与 API Git blob 匹配。这证明版本库那次出现映射，**不证明 IEEE 最初分配日、实物出货或合同**。
- **Gentoo MA-S 镜像**：[2019-03-17 快照](../../../88-source-evidence-r116-2026-10-26/github-raw/github.com/gentoo/hwids/2986daf9bf2626efe6ff1d62f9713dad6cb82dae/ma-small.txt)列 `70-B3-D5` 下的 `822000-822FFF` 和 Ankara 地址；2018-09-17 所存镜像对所列检索字符串零命中，2020 快照重复该记录。镜像与 Wireshark 可能同源，不是两份独立颁发证书；也不能把共享 `70:B3:D5` 整个前缀归给 Angora。
- 街道／门牌 `Alacaatli Mah. Park Cad. 47/31` 与 Find 相同，但 Find 的地区字段为 Yenimahalle，镜像写 Cayyolu；同名同地址线索不解决法人同一性。旧 r114 的 IANA PEN 58029 是另一命名空间，当前记录未给分配日期，不能换算为 MAC 分配日期。

## 2. 渠道页面和第三方园区目录

- [2020](../../../88-source-evidence-r116-2026-10-26/archive-replay/advensis.com.tr/en/angora-en/20201021095900/chunk-0.visible.md)／[2022](../../../88-source-evidence-r116-2026-10-26/archive-replay/advensis.com.tr/en/angora-en/20220123023037/chunk-0.visible.md) Advensis 英文页面工具可见文本主要为图片链接和页脚；图片未取，不由文件名推断销售。页脚地点不同只说明两次页面记录不同，不证明实际搬迁日或目前地址。它们和 r114 土文页同一网站，不算独立见证。
- 科技园目录的 [2024-09-20](../../../88-source-evidence-r116-2026-10-26/archive-chunks/kirikkaleteknopark.com/firma-rehberi/20240920103752/chunk-0.visible.md) 和 [2026-01-20](../../../88-source-evidence-r116-2026-10-26/archive-chunks/kirikkaleteknopark.com/firma-rehberi/20260120061616/chunk-0.visible.md) 回放分别列 `Angora Networks Bilişim` 与其域名。各 4 块独立保存，是同一园区目录的两个时间点；不证明入驻开始、持续经营、采购或交付。2020 回放四个已存文本块中 `angora` 字符串零命中，不得推定未入园。

## 3. 与旧轮关系及禁推断

**增补而非修正 r114**：新增历史 MAC 映射、英文渠道页和园区目录；r114 的 PEN 时间未知、渠道图像未解析、CLI 公告未证 2019 发布等限定继续有效。**延续 r115**：培训伙伴展示不等于授课；e-Safe 候选不等于获奖；自标 10-20 的能源决赛新闻只是截至 10-26 的预告，不能认定 10-28 已举办或 Angora 获奖。没有可核的客户、合同、收入、设备实测或法律注册编号。

新搜索响应未全部保存；部分探索页未取全，记录在[问题与限制](../../../88-source-evidence-r116-2026-10-26/issues-and-corrections.md)，不把搜索摘要升级为原文。所有既有 PASS 和停项继续有效；无外联。