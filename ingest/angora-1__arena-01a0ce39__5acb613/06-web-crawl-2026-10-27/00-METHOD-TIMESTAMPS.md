# 第 39 轮 · 外网直取（2026-10-27）— 方法与时间戳

## 0. 这一轮和 r24/r25 的根本差别

| 项 | r24/r25（2026-10-21） | 本轮 r39（2026-10-27） |
|---|---|---|
| 抓取手段 | ewindnet.com 直连 3 次全失败 → 只用 `web_search site:` 索引快照 | **直连成功**（fetch 工具可达），拿到**实时原文 + WordPress REST API + sitemap** |
| 时间戳来源 | 只有 Google 索引 pageAge，无页面自身时间 | **页面自带 date / modified（精确到秒）**、sitemap `lastmod`、文章正文时间 |
| 覆盖深度 | 索引摘要，部分型号只有摘要规格 | **完整规格表原文**（逐行）、完整正文、完整分类/模型清单 |
| 可核对性 | 无（快照随索引变） | 每个 URL + 抓取时刻 + 内容哈希，可复现 |

> 抓取时刻（UTC / 本地）：**2026-10-27T01:20Z ~ 01:23Z / 09:20 ~ 09:23 (Asia/Shanghai)**
> 源站时区：WordPress 输出为 `+00:00`（sitemap）与本地站时（posts），文中已注明。

## 1. 抓取通道

| 通道 | 端点 | 状态 |
|---|---|---|
| 站点首页 | `https://www.ewindnet.com/` | 200，2 chunk |
| 伙伴页 | `https://www.ewindnet.com/our-partner/` | 200 |
| sitemap 索引 | `/sitemap_index.xml`（= `/wp-sitemap.xml`） | 200 |
| 产品 sitemap | `/product-sitemap.xml` | 200，10 chunk（本轮取 chunk0） |
| 展会 sitemap | `/exhibition-sitemap.xml` | 200，全文 |
| 页面 sitemap | `/page-sitemap.xml` | 200，3 chunk（本轮取 chunk0） |
| WP REST | `/wp-json/wp/v2/product` | 200，**2 页 = 153 个产品**，逐条含 date/modified |
| WP REST | `/wp-json/wp/v2/posts` | 200，多页，逐条含 date/modified |
| 俄语站 | `https://ru.ewindnet.com/` | **失败**（fetch error），本轮无内容 —— 与 r24 记录的"12 语言站"一致但本次不可达 |
| Angora 站 | `https://www.angoranetworks.com/` | 200（TR 主站） |
| Angora REST | `/wp-json/wp/v2/pages`、`/posts` | 200，24 页面 / 9 文章，逐条含 date/modified |
| Larch | `https://larch-networks.com/` | 本轮**未取**（配额留给 Angora 新品发现，见 FINDINGS 第 5 节待办） |
| 社媒 | Facebook / LinkedIn / Alibaba | 本轮**未取**（需登录/强反爬），沿用 r25 记录并标注"未复核" |

> 说明：沙箱 bash 无外网（`curl` → `SSL_ERROR_SYSCALL`，无代理），全部抓取经 fetch 工具完成；
> 因此**无法保存原始 HTML 字节**，只能保存"渲染后正文文本"。此限制在每条记录的 `capture` 字段标注。

## 2. 时间戳三类，分开记，不混用

1. **抓取时刻**（我方）：`2026-10-27T01:2xZ`，每条 artifact 头部写死。
2. **站点发布/修改时间**（对方）：WP `date` / `modified`，sitemap `lastmod`，正文内嵌日期。
3. **变化判定窗口**：以 r24/r25 抓取日 **2026-10-21** 为基线 → 任何 `modified >= 2026-10-21` 的条目 = **本轮新增变化**。

## 3. 本轮结论一句话

**Ewind 站点自 r24/r25 之后没有新增内容**（最新产品 2026-08-07、最新文章 2026-06-11，均早于基线 2026-10-21）。
直连拿到的细节补上了 r24/r25 没有的层面：EW-S57948QM 完整规格表、EW-S1710FG-AP 的 E/V/D 拨码与"1 年质保"、153 个 SKU 的发布日期全表。

**Angora 侧：内容无变化。** 三个家族 Verge（page 298 / 1775）、Synapse（page 1781，2026-01-15）、Hitit（page 1804，2026-03-24）的 `modified` 都停在 2026-04-03 之前，本轮抓取正文与 **2026-09-23 网站镜像逐行一致**。

> 🔴 **口径更正**：本文件早前草稿写"Synapse / Hitit 是 r24/r25 完全没有的新家族"。**该说法已撤回。** 两个家族在 2026-09-23 的镜像里就已全量入库（`04-website-mirror/10-pages-part1.md` §⑤§⑥、`12-pages-part3-specs-and-codes.md` §一），r24/r25 的 112/113 **只覆盖 Ewind**，把它当 Angora 基线才会产生"新发现"的错觉。详见 `01-DELTA-2026-10-21-to-2026-10-27.md` C 段。

## 4. 本轮实测产物清单（16 个文件）

| 文件 | 内容 | 条数 |
|---|---|---|
| `ewind/sitemaps/sitemap_index.xml.txt` | 站点 12 个子 sitemap + lastmod | 12 |
| `ewind/sitemaps/product-sitemap.xml.txt` | 产品 sitemap chunk0（截断，注明不完整） | ~41 |
| `ewind/sitemaps/page-sitemap.xml.txt` | 页面 sitemap chunk0（截断） | 18 |
| `ewind/sitemaps/exhibition-sitemap.xml.txt` | 展会 sitemap 全文 | **11（完整）** |
| `ewind/api/wp-api-products.tsv` | 153 SKU 的 id/date/modified/slug | **153** |
| `ewind/api/wp-api-posts.tsv` | 文章 id/date/slug | **125** |
| `ewind/pages/product-EW-S57948QM__*.md` | 旗舰 L3 规格表 | 1 |
| `ewind/pages/product-EW-S1710FG-AP__*.md` | 低端 PoE + E/V/D 拨码 | 1 |
| `ewind/pages/exhibition-timeline.md` | 展会时间轴 + 缺失展位分析 | 13 行 |
| `angora/api/wp-api-pages.tsv` | 24 个页面 | **24（完整）** |
| `angora/api/wp-api-posts.tsv` | 10 条文章记录 | **10（完整）** |
| `angora/pages/{synapse,hitit,verge}*.md` | 三个家族复核档 | 3 |
| `00-METHOD-TIMESTAMPS.md` / `01-DELTA-*.md` | 方法与变更对照 | 2 |
