# 第 40 轮 · 外网复爬（2026-11-01）— 方法与时间戳

## 0. 本轮与上一轮的关系

| 项 | r39（2026-10-27） | **r40（2026-11-01）本轮** |
|---|---|---|
| 基线 | r24/r25（2026-10-21，档案 112/113） | **r39（2026-10-27，目录 `06-web-crawl-2026-10-27/`）** |
| 抓取时刻 | 2026-10-27T01:20–01:26Z | **2026-11-01T05:29–05:45Z = 13:29–13:45 (+0800)** |
| 手段 | 官网直连（首次成功） | 官网直连 + **宣传面真实站点**（Alibaba 店铺）+ **PDF 数据表/宣传册**（r39 只有路径）+ sitemap 剩余分块 |
| 新增能力 | REST 时间戳 | **PDF 正文**、**Alibaba 平台数据**、**多语言子站实测** |

> 沙箱 bash 无外网，全部经 fetch 工具；仍**不能保存原始 HTML 字节**，只存渲染文本。每个 artifact 头部标 `capture:`。
> 时间戳仍分三类：① 我方抓取时刻 ② 对方 `date`/`modified`/`lastmod` ③ 变化判定窗口 = **r39 抓取日 2026-10-27**。

## 1. 本轮抓取通道与结果

| 通道 | 端点 | 结果 |
|---|---|---|
| 产品 REST（按 modified 倒序，前 20） | `/wp-json/wp/v2/product?orderby=modified&order=desc` | ✅ 最新 modified = **2026-08-26T17:42:11**（id 8143，2024 年老品重存） |
| 文章 REST（前 15） | `/wp-json/wp/v2/posts` | ✅ 最新 = 2026-06-11（id 10678） |
| 产品 sitemap / 页面 sitemap 剩余分块 | `/page-sitemap.xml` chunk 1–2 | ✅ 拿到 2024-07/08 的 12 个行业垂直页 + 3 个 SEO 落地页 + 售后/质保/证书页 |
| 售后页 | `/after-sales-service/` | ✅ 电话号码 + 质保流程 |
| 质保页 | `/active-warranty/` | ✅ 同上（正文在 chunk 2，本轮未取） |
| 关于页 | `/about/` | ✅ 2017 成立、8 条产品线、**"3–5 年质保"**、ISO9001 |
| 证书页 | `/our-certificates/` | ⚠ 只有标题，证书是图片，**无文本** |
| SEO 落地页 | `/poe-switch-manufacturers/` | ✅ 8 条产品线 + 逐型号卡片（含**新型号编码**）+ 产品目录弹窗 |
| **Alibaba 店铺** | `ewindnet.en.alibaba.com/productgrouplist-825444145/8_port.html` | ✅ **通**（r25 只能靠索引快照，本轮直连成功）：店铺档案 + 价格 + 类目树 |
| **Alibaba 单品页** | `www.alibaba.com/product-detail/…` | ❌ 被重定向到图片搜索页（无反爬说明，纯粹路由变化） |
| **多语言子站** | `es.` / `tr.ewindnet.com` | ❌ **GTranslate Error 402: Subscription Inactive**（见下，重大发现） |
| 俄语站 | `ru.ewindnet.com` | ❌ fetch 失败（与 r39 同） |
| **PDF 数据表** | EW-S57948QM、EW-S1710FG-AP | ✅ 全文（r39 只有路径） |
| **Angora 宣传册** | `/download/1797/`(Synapse) `/1808/`(Hitit) `/425/`(Verge 工业) `/428/`(Verge 企业) | ✅ 全部有正文（1797/1808 全文 1 chunk；425/428 各 4 chunk，本轮取 0–2） |
| Facebook / LinkedIn / ZoomInfo / YouTube | — | ❌ 本轮未取（无可用入口，见 §5） |

## 2. 关键判据

- **"有没有新内容"** = 站点 `modified`/`lastmod` 是否 ≥ 2026-10-27。
- **"是不是宣传面变化"** = Alibaba 店铺的店铺分、在线营收、员工数、类目树、价格是否与 r25 记录不同。
- **"是不是我们自己的错误"** = 与 r39/REST 原值逐字对表，凡我方档案与站点原文冲突，一律以站点原文为准并在 `01-DELTA` 里单列更正。

## 3. 本轮产物（17 个文件）

见 `01-DELTA-2026-10-27-to-2026-11-01.md` §F。
