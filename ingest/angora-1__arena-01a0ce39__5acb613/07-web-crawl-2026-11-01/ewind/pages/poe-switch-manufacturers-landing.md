# Ewind SEO 落地页 `/poe-switch-manufacturers/` — 逐型号卡片（新型号编码来源）

| field | value |
|---|---|
| URL | https://www.ewindnet.com/poe-switch-manufacturers/ |
| lastmod | **2024-11-23T03:51:11+00:00**（页面骨架老，但**卡片内容由产品库动态拉取，随产品上新而变**） |
| capture | 2026-11-01T05:34Z，rendered text，10 个分块（本轮取 chunk0，含前 7 张卡片） |
| 与 r39 对比 | r39 未抓此页 → 首次入库 |

## 页面自述
> "EWIND … now owns **8 independent product lines**: Industrial POE Switch / POE Switch / Ethernet Switch / Din-rail Industrial Switch / Din-rail Managed Industrial Switch / Managed Commercial Switch / Media Converter / POE Accessories (PoE Injector, POE Splitter, SFP optical modules, Power Supply etc)."

（`/about/` 同日表述为 8 条线，但列的是 Cloud Managed PoE Switch、Wireless Products(AP/CPE/Router/LTE) —— **两条口径不完全一致**，一处算"云管"、一处算"无线"，实际产品线数量介于 8–9 条。）

## 首次见到的型号编码（均带官网 permalink，可直接核）
| 型号 | 描述 | 产品页 | 归类 |
|---|---|---|---|
| **EW-S1712CG-AP** | 8×GE RJ45 + 2×GE RJ45 + 2×100/1000 RJ45 非网管 PoE | `ewind-810-100-1000m-rj45-port210-100-1000m-rj452100-1000m-rj45-ports-unmanaged-poe-switch-1` | 1000M PoE |
| **EW-S1710FG-AP** | 8×GE PoE + 2×SFP（r39 已建档） | 同名页 | 1000M PoE |
| **EW-S2924SM-AP** | 24×GE + 4×Combo，**Lite Management**，300 W | `24ge4combo-gigabit-lite-management-switch300w-1` | **Lite Management Switch**（新类目） |
| **EW-S2910SM-DP** | 8×GE + 2×2.5G，Lite Management | `8ge22-5g-gigabit-lite-management-switch-1` | Lite Management |
| **EW-ES3028CGSH-AP** | 24×GE PoE + 2×GE + 2×GF 上联，**Cloud-Managed AI PoE** | `ewind-24ge-poe2ge2gf-uplink-gigabit-cloud-managed-ai-poe-switch-1` | Cloud PoE |
| **EW-ES3020CGSH-AP** | 16×GE PoE + 2×GE + 2×GF，Cloud AI PoE | `ewind-16ge-poe2ge2gf-…-1` | Cloud PoE |
| **EW-ES3010CGSH-AP** | 8×GE PoE + 1×GE + 1×GF，Cloud AI PoE | `ewind-8ge-poe1ge1gf-…-1` | Cloud PoE |
| **EW-ES3006FGSH-AP** | 4×GE PoE + 2×GF，Cloud AI PoE | `ewind-4ge-poe2gf-…-1` | Cloud PoE |

## 命名体系解读（对认型号有用）
- `EW-S1xxx` = **非网管/轻量百兆千兆**（S1712/S1710/S1806/S1827…）
- `EW-S2xxxSM` = **Lite-Management**（2026-06 新开的档位，网页 2026-06-25 发布）
- `EW-ES3xxxCG/FG**SH-AP` = **Cloud-Managed AI PoE**（2026-05 批量上线，`SH`=Smart Hybrid 推测，**推断，未证实**）
- `EW-PISxxxx` = 工业级（M = Managed，`-BT` = 802.3bt 大功率）
- `EW-ISxxxx` = 工业非网管
- 后缀 `-AP` = 支持 PoE 供电（非无线 AP 之意）；`-DP` = 双 2.5G 上联

⚠ 该页共有 10 个分块（约 60+ 张卡片），本轮只取 chunk0。**完整型号全集仍以 r39 的 REST 153 SKU 表为准**，本文件只用于补"型号 → 商品名"映射。
