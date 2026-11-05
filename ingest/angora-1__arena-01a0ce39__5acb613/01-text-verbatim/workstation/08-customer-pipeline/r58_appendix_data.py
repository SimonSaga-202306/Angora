# -*- coding: utf-8 -*-
"""r58 附录数据（键为主表 111 的行号字符串）。"""

D = {}

D['75'] = """
#### r58 新增：**Technopc 的「交换机」是纯文案，站点上零个交换机 SKU** —— ODM 缺口已确认

r53 只记了「Technopc 网络品类空目录」。本轮把 `technopc.com.tr/network-urunleri/` 逐项读完，**原因清楚了**：

| 型号 | 类型 | 原文关键配置 |
|---|---|---|
| `FW801` | x86 防火墙 | Intel 6./7. Nesil · 16 GB DDR3 · 2× 2.5" HDD · **SIM 卡支持** |
| `FW622` | x86 防火墙 | Celeron N3060 · 8 GB DDR3 · 2 TB · **6× Gigabit LAN** |
| `FW57` | x86 防火墙 | Celeron 3205U · 16 GB DDR3 · 2 TB · **2× COM + 2× LAN** |
| `NSW 4500` | x86 SD-WAN | Atom 2.2 GHz · 2× SO-DIMM DDR4 · **6× LAN + 4G LTE** |
| `NTSN 6500F` | x86 SD-WAN | Atom C3558 · 128 GB DDR4 · **6× LAN + 2× SFP** |

- 页面营销文案写满：`gigabit ve 10G destekli switch modelleri`、`PoE çözümleri`、`Layer 2/Layer 3 yönetilebilir switch`、`bulut tabanlı yönetim`；
- 但筛选结果为 **`Seçilen filtrelere uygun ürün bulunamadı`**，`/urun-kategori/network-urunleri/switch/` = **404**；
- 全部产品只有 **「Bize Ulaşın」联系表单，无价格**。

**⇒ 结论：Technopc 做的是 x86 网络安全盒子（防火墙 / SD-WAN），交换机是「对外宣传了、向内还没货源」的品类。**

而本管线 #75 的原有记录写的是：**「Switch/AP/Firewall = 近期扩张配套品类；工业 PoE 采购 E-wind」**（用户侧信息）。**两条合起来 = 一个正在找交换机货源、且已经在我方采购工业 PoE 的土耳其本土品牌。**

**⇒ 建议动作（本轮最高转化价值的一条）**

1. **不要卖成品，谈 ODM**：一句开场——`Sitenizde L2/L3 switch ve bulut yönetiminden bahsediyorsunuz ama katalogda tek bir switch SKU yok. Ürün mü eksik, sertifika mı? Biz OEM/ODM yapıyoruz: 24 port GE PoE + 4×10G ve 8 port 2.5G PoE iki hattı, MOQ 1 adet numune, 5–7 gün numune süresi.`
2. **ODM 报价逻辑**：我方 FOB × **1.6–1.8**（留给品牌方的毛利 + 本地库存成本），仍显著低于 FOREDGE `PS3028GT` **$408.8** 与 HPE Aruba ION `JL683A`（24 口 GE PoE）**$291** ⇒ 品牌方有得赚。
3. **认证可直接复用**：CE / RoHS / UKCA / DoC（我方阿里店铺已展示 5 张）。
4. **保修必须给 36 个月**：DMO 页面 `Garanti Süresi` 多数为 **24 月**，但 Ruijie `RG-S2915-10GT2MS-P-L` 与 `RG-S2915-24GT4MS-P-L` 是 **36 月** ⇒ **3 年保修已是公共采购的差异化点**，我方按 36 个月报，别只给 24。
5. ⚠ **前置欠账**：我方 **24 口 +4×10G / 8 口 2.5G PoE / 48 口 PoE** 的 FOB 仍未取得（r57 起连续两轮），**没有这三个数字，ODM 提案发不出去**。

**证据等级**：5 款型号与配置 = 页面原文；「零交换机 SKU / switch 子目录 404 / 无价格」= 页面原文；「Technopc 在采购 E-wind 工业 PoE」= **用户侧名单信息，我方未独立核实**；「ODM 报价 ×1.6–1.8」= 我方推算。

> **完整背景见** `127-dmo-dealers-technopc-odm-and-tr-own-brands-2026-11-01.md`（含 RESET / DAPA 完整联络档案、土耳其自有品牌低价带、阿里 MOQ 分布抽样）。
"""
