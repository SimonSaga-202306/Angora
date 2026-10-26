# angoranetworks.com — 全站镜像 · 抓取清单与方法说明

- **目标站**：https://www.angoranetworks.com/ （Angora Networks, 安卡拉, 土耳其）
- **抓取日期**：2026-09-23
- **抓取方式**：经 `sitemap_index.xml` → 10 个子 sitemap 枚举全部 URL，逐页抓取正文
- **限制说明**（重要）：
  1. 沙箱直连出网被阻断（`curl`/`requests` 一律 `SSL_ERROR_SYSCALL`），因此**无法取得原始 HTML 与二进制资源**（图片/PDF/PSD）。本镜像为**全站可见文本（text-layer）的逐字摘录**，正文、表格、链接、图片 alt/URL 均保留。
  2. 站点为 **WordPress + WPML 多语言（tr / en / ru）**，同一页面存在多语言版本，已分别抓取并标注。
  3. 每页页脚的 `reCAPTCHA / Destek / Support` 为模板样板，逐字保留在第一处，后续页面注明相同。
- **下载资源（PDF 宣传册/数据表）清单**：见 `90-downloads.md`

## sitemap 结构（10 个子索引）

| 子 sitemap | 最后更新 | 内容 |
|---|---|---|
| page-sitemap.xml | 2026-04-03 | **41 条** 页面（产品/公司/联系/隐私等） |
| post-sitemap.xml | 2026-06-15 | **约 18 条** 新闻/博客 |
| tribe_events-sitemap.xml | 2023-07-06 | 活动（The Events Calendar 插件） |
| category-sitemap.xml | 2026-06-15 | 6 个分类归档 |
| post_tag-sitemap.xml | 2026-06-15 | 标签归档 |
| tribe_events_cat-sitemap.xml | 2023-07-06 | 活动分类 |
| client-types-sitemap.xml | 2022-12-21 | clients / partners 两个客户类型 |
| portfolio-types-sitemap.xml | 2017-02-03 | artwork / banner / design |
| slide-types-sitemap.xml | 2017-02-03 | 幻灯片 |
| author-sitemap.xml | 2021-05-03 | 单一作者 `wwwadmin` |

## robots.txt（原文）

```
# START YOAST BLOCK
# ---------------------------
User-agent: *
Disallow:

Sitemap: https://www.angoranetworks.com/sitemap_index.xml
# ---------------------------
# END YOAST BLOCK
```

> 全站允许抓取，无 Disallow 限制。

## 关键发现（先看这里）

1. **Angora 已取得 EGM 交通整形（traffic shaping）测试通过** —— 正是警方 ÇGKS 2026 项目（3,294 台）所要求的 "C 型边缘交换机与流量整形测试报告"。通过机型为**工业 8 口 L2+ 管理型交换机**。（见 `/angora-networks-egm-trafik-sekillendirme-gereklilik-testlerini-gecti/`）
2. **2026 年 Angora 重构了产品线，形成三大交换机家族**：**VERGE / HITIT / SYNAPSE**，另有 **GORDION**（数据中心）、**IRIS**（SFP）、**Karınca**（Packet Broker）、**Arrow**（数据二极管）、**Arı**（SD-WAN 安全硬件）、**Thince**（瘦客户机）、**ANMS**（网管平台）。
3. **⚠ 2026-04 新版 VERGE 页面已不再出现 Saga 供货的型号（ANW-11xx / ANW-22xx / ANW-21xx），改用 `ANW-2023-*` 与 `ANW-IND-8P-2SFP` 等新编号** —— 而旧版 `/network-devices/` 页面仍保留 `ANW-1104/1108/2108/2208/2224/2248` 系列（即 Saga 供货机型）。**这是需要向客户确认的重要信号。**
4. **官网 References（客户）列表中没有 Türk Telekom**，但有 EGM（警察总局）、KGM、TSK（军队）、TÜRKSAT、TCDD、MSB（国防部）、ASELSAN、HAVELSAN、Anadolu 大学、Turkcell KKTC、卫生部。
5. **Technology Partners 含 Marvell** —— 与其对外宣称的 Marvell 方案一致。
6. **罗马尼亚布加勒斯特设有欧洲区域销售办公室**（Aron Cotrus 57, Sector 1, Bucureşti 014131）。
7. **两个安卡拉地址**：销售 = Nergiz Sokak No:7 Via Flat Plaza Cubes Söğütözü 06560；生产 = Çamlıca Mh. Anadolu Blv. Timko sk Z Blok No:20/1 Yenimahalle 06200（即我方发货地址）。

---

## URL 清单与抓取状态

| # | URL | 语言 | 状态 |
|---|---|---|---|
| 1 | `/` | tr | ✅ |
| 2 | `/?lang=en` | en | ✅ |
| 3 | `/?lang=ru` | ru | ⏳ |
| 4 | `/network-devices/` | tr | ✅ |
| 5 | `/verge-network-switch-serisi/` | tr | ✅ |
| 6 | `/verge-network-switch-family/?lang=en` | en | ⏳ |
| 7 | `/verge-network-switch-family/?lang=ru` | ru | ⏳ |
| 8 | `/hitit-yerli-network-switch-ailesi/` | tr | ✅ |
| 9 | `/synapse-network-switch-ailesi/` | tr | ✅ |
| 10 | `/iris-sfp-ailesi/` | tr | ✅ |
| 11 | `/iris-sfp-family/?lang=en` | en | ⏳ |
| 12 | `/iris-sfp-family/?lang=ru` | ru | ⏳ |
| 13 | `/angora-networks-_en/?lang=en` | en | ✅ |
| 14 | `/about/` | tr | ✅ |
| 15 | `/about/?lang=ru` | ru | ⏳ |
| 16 | `/partners/` | tr | ✅ |
| 17 | `/partnership-form/?lang=en` | en | ⏳ |
| 18 | `/is-ortaklari/` | tr | ✅ |
| 19 | `/brosurler/` | tr | ✅ |
| 20 | `/iletisim/` | tr | ✅ |
| 21 | `/contact/?lang=en` | en | ⏳ |
| 22 | `/contact/?lang=ru` | ru | ⏳ |
| 23 | `/hizmetlerimiz/` | tr | ✅ |
| 24 | `/our-services/` | en | ⏳ |
| 25 | `/our-services-2/?lang=en` | en | ⏳ |
| 26 | `/angora-nms/` | tr | ✅ |
| 27 | `/angora-nms_en/?lang=en` | en | ⏳ |
| 28 | `/angora-nms_en/?lang=ru` | ru | ⏳ |
| 29 | `/ozgun-tasarim-oem-odm-hizmeti/` | tr | ✅ |
| 30 | `/yerli-network-packet-broker/` | tr | ✅（2 段，第 2 段待取） |
| 31 | `/yerli-network-packet-broker/?lang=en` | en | ⏳ |
| 32 | `/yerli-network-packet-broker/?lang=ru` | ru | ⏳ |
| 33 | `/network-packet-broker-test/?lang=en` | en | ⏳ |
| 34 | `/ari-sd-wan-guvenlik-ve-servis-donanimlari/` | tr | ✅ |
| 35 | `/ari-sd-wan-guvenlik-ve-servis-donanimlari/?lang=ru` | ru | ⏳ |
| 36 | `/angora-data-diode/?lang=en` | en | ✅ |
| 37 | `/arrow-диод-данных/?lang=ru` | ru | ⏳ |
| 38 | `/portfolio/` | tr | ⏳ |
| 39 | `/portfolio/?lang=en` | en | ⏳ |
| 40 | `/submarine/` | tr | ⏳ |
| 41 | `/submarine/?lang=en` | en | ⏳ |
| 42 | `/gizlilik-politikasi/` | tr | ⏳ |
| 43 | `/privacy-policy/?lang=en` | en | ⏳ |
| 44 | `/blog/` | tr | ⏳ |
| 45 | `/news/?lang=en` | en | ⏳ |
| 46–60 | 全部 post / category / author 页 | 多语 | ⏳ |

> `?page_id=298`（Anahtarlar 交换机）→ 301 至 `/verge-network-switch-serisi/`
> `?page_id=316`（SFP）→ 301 至 `/iris-sfp-ailesi/`
> `?page_id=275`（咨询/培训）→ 301 至 `/hizmetlerimiz/`
