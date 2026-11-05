# -*- coding: utf-8 -*-
"""r55 补录（2026-11-01）：CryptoLink 剩余 PDF 读完 + Cebeci 的品牌方 FOREDGE 全产品线（推翻 r54）。"""

D = {}

# ---------------- A / 005 CryptoLink ----------------
D['5'] = """
### ⭐ r55：`CRL-MC02` 与 `CRL-SFP-10G-LC` 两份 PDF 读完 —— **datasheet 自相矛盾，换牌痕迹更明显**

#### A. `CRL-MC02`（媒体转换器）
| 项 | 值 |
|---|---|
| 品名 | 2 Ports Media Converter：**1×100M RJ45 + 1×100M 光纤** |
| 光口 | **ST / SC / FC，100 Mbps 全双工** |
| 距离档位 | 多模 850/1310 nm **0–2 km**；单模 1310 nm **20 / 40 / 60 km**；单模 1550 nm **80 / 100 / 120 km**（灵敏度 −25 ~ −44 dBm） |
| 协议 | IEEE802.3/u/z/ab、10Base-T / 100Base-TX / 1000Base-TX（**原文把 1000Base 也列进来，与"100M 口"矛盾**） |
| 功耗 | **< 5 W**（DC 5 V 1000–3000 mA） |
| 尺寸 / 重量 | **11×7×2.5 cm / 0.18 kg** |
| 温度 / MTBF | **−20~50 °C**（存储 −40~85 °C）/ **100,000 h** |

#### B. `CRL-SFP-10G-LC`（10G 光模块）—— ⚠ **原文自相矛盾**
- 型号与标题写 **SFP+ 10GbE**，参数栏写 **Transmit Distance: 10Gbs**；
- 但正文第一段写 **「the speed rate up to **155Mbps** and the transmission distance up to 20km」**；
- 实测参数：**1310 nm、发射 −15~−3 dBm、接收灵敏度 −34 dBm、单模 20 km / 多模 2 km、DC 3.15–3.45 V、1 W、55.4×13.7×6.25 mm、0.17 g、0~70 °C**。

⇒ **同一份官方 datasheet 里 155M / 10G 并存** —— 这是**换牌厂商直接沿用 OEM 模板、没校对**的典型痕迹（与 r53 发现的上游 `CrystalWAN` 页眉同源）。
→ **销售可用**：客户若拿它的 datasheet 做招标附件，**参数自相矛盾可直接质疑**；我方 datasheet 只需**准确、可对标**就能赢这一分。

#### C. 至此 CryptoLink 全 7 份 PDF 已读（4 份本轮前已读，2 份本轮读完，1 份重复）
`CRL-SW-L3-2404-10G` · `CRL-SW-2402` · `CRLISW-08` · `CRLISW-14P` · **`CRL-MC02`** · **`CRL-SFP-10G-LC`** · `CRL-SFP-125 LC`（未单独读，与 10G 版同族）。

### 证据等级（r55）
- 已核实：**两份 datasheet 全表**、**155M vs 10G 的矛盾文本**。
- 仍空白：`CRL-SFP-125 LC` 单独规格。
"""

# ---------------- B / 062 Cebeci（品牌方 FOREDGE 被推翻） ----------------
D['62'] = """
### 🛑 r55：**它的品牌方 FOREDGE 比我方强** —— r54 在这里的结论被推翻

r54 写「Cebeci 卖的是 FOREDGE 白牌，**没有 2.5G、没有 bt、没有云**，所以我方可以靠这三条差异化」。r55 打开 `foredgetech.com/tr` 后**全部不成立**：

| r54 的判断 | r55 实测（`foredgetech.com/tr/products/` 原文） |
|---|---|
| 无 2.5G | ❌ 有整条 2.5G 线：`PS3024XGPSH`（8×2.5G + 16 GE PoE + 4×10G）· `PS3016XGPSH` · `PS3008XGPSH` · `NS3024XGSH` · `NS3016XGSH` · `NS3008XGSH` · `AI1009XG` · `AI1009XGP` · ⭐ **`S6700-48GXP-4TF-2QF` = 48×2.5G + 4×10G + 2×100G** |
| 无 802.3bt | ❌ 全线标 **「90W per port」**；`S6700-48GXP-4TF-2QF` **PoE 1200 W** |
| 无云管理 | ❌ **`Apollo Cloud`** 云平台，多型号标配 |
| （未评估） | ❌ **数据中心线 6 款**：`S6700-24TF-2QF`（24×10G + 2×100G / 880 Gbps）、`S6700-32QF`（6.4 Tbps）、`S6700-48TF-8QF-H`、`S6700-48YF-8QF-H`（25G）、`S6700-32CQ`（25.6 Tbps）、**`S6700-64CQ`（64×400G / 51.2 Tbps / 38 Bpps）**；**SONiC 或自有 RunOS** |
| （未评估） | ❌ **它自己也做 OEM/ODM**：**180,000 sqft、3 条 SMT、年产能 200 万台、MOQ 500、交期 6–8 周**、2021 年以来 12 个贴牌项目 |

⇒ **对 Cebeci 的打法必须改**：**不要再讲"我们有 2.5G/bt/云"**（它老大有）。
**改讲三件它老大确实没有的**：
1. **本地化速度**：Foredge 的 DMO 框架合同**2026-10-21 到期**，续约前的价格与供应有不确定性；
2. **小批量弹性**：**它 MOQ 500**；我方若能给 **100–200 台试单**，就是真差异；
3. **响应**：Foredge 工程师在中国，**我方若能在土耳其派驻/联合备件**，项目响应就是差异。

**首封（改写）**：`Foredge alternatifi değil, tamamlayıcı: düşük MOQ + hızlı sevkiyat + 2.5G stok`
**必问**：① Foredge 的 DMO 合同 2026-10 到期后你们怎么办？② 你们的 MOQ 卡在哪一档？③ 项目里 Foredge 交期多久？

### 证据等级（r55）
- 已核实：**Foredge 土耳其站 72 个企业级型号（已读 4 页 40+ 个）+ 6 个数据中心型号 + OEM/ODM 能力页**。
- 仍空白：Foredge 的**实际成交价**（除 DMO 两个型号）、**FS Grup 是分公司还是代理**。
"""
