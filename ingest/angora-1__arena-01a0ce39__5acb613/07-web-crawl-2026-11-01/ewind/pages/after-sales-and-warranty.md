# Ewind 售后 / 质保口径（2025-03-25 建页，2026-11-01 复爬）

| field | value |
|---|---|
| URLs | `/after-sales-service/`（lastmod **2025-03-25T08:40:01**）、`/active-warranty/`（lastmod **2025-03-25T08:48:15**） |
| capture | 2026-11-01T05:33Z，rendered text（raw HTML 不可得） |
| 与 r39 对比 | r39 未抓这两页（页面 sitemap 只取了 chunk0）→ **本轮首次入库** |

## 页面可见事实（非正文细节，正文在两页的第 2 分块，本轮未取）
- 24 小时热线：**+86 755-2100 6440**
- 邮箱：**info@ewindnet.com**
- WhatsApp：**+86 158 1559 1833**（页面按钮直连 api.whatsapp.com）

## 质保口径——三处互相打架，必须分开引用
| 来源 | 说法 | 时间 |
|---|---|---|
| `/about/` 正文 | "We provide a **3-5 year warranty** on our products" | 页面 modified 2026-01-21 |
| EW-S1710FG-AP 数据表 V1.5（见 `../datasheets/`） | "**1 years warranty**" + "lifetime maintenance" | PDF 文件名 20260806 |
| EW-S57948QM 数据表 | "**3 years warranty**" | PDF 文件名 20260511 |
| 官网多个产品页标题 | "…with 3 years warranty"（id 8998 / 8488 / 7030 / 3876） | 2024 起 |
| Alibaba 店铺部分商品 | 2 年 / 5 年（r25 记录，本轮未逐条复核） | — |

**结论（可对外引用）**：Ewind 的质保**不是统一政策**，而是按 SKU 分档：入门非网管 PoE 是 **1 年**，主流是 **3 年**，公司页面上限写到 **5 年**。采购谈判时按具体型号要书面质保条款，不能引用官网"3–5 年"的笼统说法。这也是我们区分"低价款/常规款"的一个可验证抓手。
