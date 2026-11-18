# -*- coding: utf-8 -*-
"""r91 附录数据：土耳其公共交换机标的的「锁死条款」—— ETİ MADEN 规格书（同品牌 / Forescout 8.2 矩阵 /
原厂光模块不接受 OEM / Huawei AC6605 + E-Sight + S5735 堆叠）+ 渠道公示地图 v2（UEDAŞ 一标一 PDF、
OEDAŞ 编号页、TaahhütHaber 日报）+ TTK 中标方「因取消而不存在」的机制结论（2026-10-26）。"""

D = {}

D['72'] = """
#### r91 总览：**壁垒不在参数，在生态 —— 土耳其公共交换机标的的「锁死条款」**

> 载体说明：本附录块挂在管线行 072 名下，是 **builder 的机械挂载约定**（r85→066 … r89→070 / r90→071 / r91→072），**内容与该行客户无关**，整轮叙述见 `160`。

**① ⭐⭐⭐ ETİ MADEN 规格书 = 一份"排除法"范本（A 级，官方 PDF）**
采购人 **ETİ MADEN İŞLETMELERİ GENEL MÜDÜRLÜĞÜ · 管理信息系统部**；标的是各分局 + 备件库的**有线/无线网络与被动设备**。
**交换机 44 台**：**Fiber Anahtar 24 Port ×7** · **Kenar 48 Port ×13** · **Kenar 24 Port ×13** · **Kenar 12 Port ×11**；另 Indoor AP 23 + Outdoor AP 5、铜跳线 5,400 + 光纤跳线 1,000、理线器 400、机柜室内 26/室外 26。

**五条锁死条款（3.1.a–g 原文）**：
| 条款 | 内容 | 效果 |
|---|---|---|
| b | **全部交换机必须同一品牌**，且**必须列入 `Forescout 8.2` 兼容矩阵**，支持 Voip Detection / Switch Discovery / Assign to VLAN / Block Switch Port | **排除不在矩阵里的白牌** —— 也是唯一"非华为但可争取"的门槛 |
| **c** | **SFP/GBIC、XFP/SFP+ 必须为制造商原厂；OEM 不予接受** | **直接封死第三方光模块** |
| d | 无线须与现网 **`Huawei AC6605`** 完全兼容并受其管理 | 事实=只买华为 AP |
| e | 有线须被现网 **`Huawei E-Sight`** 纳管 | 事实=只买华为交换机 |
| **f** | **48 口边缘须能与现网 `Huawei S5735-S48P4X` 堆叠** | **决定性排除**：非华为无法与华为堆叠 |
| g | 铜/光纤跳线须同品牌 | 被动件也被绑 |
**第一层也没放过**：Fiber 24 口要 **≥24×1Gb SFP + ≥8×1Gb 铜 + ≥4×10Gb**、随机 **2×10G-LR 10 km + 12×1000LX 10 km**、**8 台堆叠/≥40 Gbps**、**≥144 Gbps / ≥108 Mpps**、**≥4,000 VLAN / 1,000 活跃**、**≥8K IPv4 路由**、MSTP+PVST+、DHCPv6/SNMPv6/TFTPv6、SSHv2+SFTP/SCP。
⇒ **144 G / 108 Mpps 与 TTK 的 128 G / 95.23 Mpps 是同一代 D-Link 家族的数字** ⇒ **土耳其公共标参数几乎同模板**；而 **"24 光 + 8 铜 + 4×10G" 的形态 Angora 有（`ANW-5713-24S8T6X`），我方没有对位机**。

**② ⭐⭐ 修正 r89 的 SFP 结论（划边界，不是推翻）**
r89：Angora 的 SFP 只到 10 km，KGYS 要 70 km ⇒ 长距 SFP 是我的机会。**r91：只要标书写了「原厂光模块、OEM 不接受」（ETİ MADEN 3.1.c），这条生意就不成立。**
| 场景 | SFP 生意 |
|---|---|
| 明文「原厂光模块、OEM 不接受」 | **不可直接卖**；只能做 **Angora 的隐形 ODM**（Angora 出标签/包装/质保/兼容责任） |
| 只写「兼容、支持 XX 标准」 | **可卖**（独立报价项或备件） |
| 现网扩容/备件（非招标） | **可卖**（最快现金流） |
⇒ 对 Angora 的提案改写为：**"做你的 SFP 白牌线 + 你出原厂标签"** —— 同时解决了 r90 的 62443 与"原厂"责任归属问题。

**③ ⭐ 渠道公示地图 v2（承 r90）**
| 机构 | 形态 | 例 |
|---|---|---|
| AYEDAŞ / Toroslar / Başkent（Enerjisa 系） | **网页表格**（AYEDAŞ 2,354 条、按年筛） | 防火墙+交换机材料 **$109,000.02**；Toroslar **$169,000 → REVOTEK**；Başkent **$101,500** |
| **UEDAŞ**（Uludağ） | **一标一 PDF**：`İHALE NO / TARİH / KONU / İHALE ÜZERİNDE KALAN FİRMA / SÖZLEŞME TUTARI` | `25-067` AG 配电箱 **$660,000 → ETİEN ENERJİ**；`24-044` LED **$75,750 → CEMDAĞ** |
| **OEDAŞ**（Osmangazi） | 编号列表 + 「İncele」子页（`2026/1`…，含 Doğrudan Alım） | 需逐页开 |
| **TaahhütHaber**（私营公报） | **每工作日一份 PDF**，按 EKAP 组列当日结果与中标方，**专设 `BOTAŞ/TPAO - ETİ MADEN - TKİ - TTK` 组** | 覆盖 TTK 组 |
⇒ **结果侧已有两条不依赖 EKAP 账号的通道**（EDAŞ 官网 + TaahhütHaber）；**规格侧仍要 EKAP 账号或转载站**（附件不转）。

**④ ⭐⭐ TTK 中标方：第四次确认不可查 + 机制结案**
`gecmis-list.php` 两轮（`2534053` 2026-01-15、`2625016` 2026-03-12）**状态均为「Geçmiş / İptal Edilmiş」**；新工具 TaahhütHaber 日报亦无结果。
⇒ **机制**：**被取消（iptal）的标不产生结果公告** ⇒ 任何渠道都查不到中标方 —— **不是没找到，是不存在**。
⇒ **正式记为「因流标/取消而不存在」**，而非「未获得」（对 r88/r89/r90 三次"不可查"的定性升级）；**唯一例外**：若第三轮重新招标并成交，则会有结果 ⇒ 监控 `taskomuru.gov.tr/ihale/`。

**⑤ 可执行清单**
1. **44 台 + 备件库字样 ⇒ 循环采购**（每 2–3 年），列入长期跟踪。
2. **不碰硬标（华为生态），改打它的 `AXVI 工业设施` / 采矿自动化 / SCADA 侧**（要工业交换机 + ICS 分段，不要 eSight）。
3. **唯一不需要换供应商就能解的生态门槛：`Forescout 8.2` 兼容矩阵** ⇒ 行动项：确认 Angora / 我方机型能否入矩阵（入了就能在标书里写"多品牌可选"）。
4. **被动件是生意**：6,400 条跳线 + 400 理线器 + 52 台机柜 + 4,000 螺母，无品牌锁死（g 条的"同品牌"可以是 Angora）。

**⑥ ⚠ 自我修正：第六节「Forescout 8.2 矩阵是唯一可解的生态门槛」判定过乐观**
Forescout 官方 `CounterACT Network Devices Compatibility Matrix`（有线交换机段）与 `Switch Plugin` 支持清单、`Switch Vendor ACL Support`（**仅 15 行**）——**只覆盖一级厂商**：**Cisco / HPE（ArubaOS-CX、ProCurve、Comware）/ Juniper / Avaya / Huawei / H3C / Alcatel / Arista / Brocade / Dell（OS10、DNOS 9.x、SONiC）/ Enterasys / Extreme / Hirschmann / DNI**。
⇒ **`D-Link`、`Zyxel`、`PLANET`、`Angora(ANW)` 全不在清单内** ⇒ **ETİ MADEN 的 b 条不是"可推开的门"，而是又一道品牌筛**（与 d/e/f 华为生态叠加 ⇒ **事实上的同品牌续购**）。
⇒ 要"进矩阵"须 **Forescout 官方为该 ODM 做验证并列入**（季度级周期、需品牌方出面）⇒ **不是我们这一层能单方面解决**；须先问 Angora 与 Forescout 土耳其代表处。
⇒ **话术修正**：**不要再说"我们能帮你进 Forescout 矩阵"**；改说 **"这类标只能守不能攻，我们的战场在没写 NAC 兼容条款的标"**。
⚠ 原文自述矩阵"represents a **subset** of each vendor's portfolio"（不可能逐一测试）⇒ 矩阵本身也不是全型号覆盖，但**厂商级仍那十几家**。

**⑦ ⭐ 21 家 EDAŞ 公示地图：已核 5 家，其余多为死路**
已核：**AYEDAŞ / Toroslar / Başkent（网页表，AYEDAŞ 2,354 条，2026 仍在更新：`AYEDAŞ MARMARA BÖLGESİ AG-YG` → **LTS LİTYUM TEKNOLOJİ 68.019.706,37 TRY**）· UEDAŞ（一标一 PDF）· OEDAŞ（编号 + İncele）**。
其余 16 家：**两次定向检索全被"配电私有化拍卖"旧闻淹没**（Vangölü 2013 **118 M USD** → Türkerler；Meram **440 M USD** → Alsim Alarko；Akdeniz **546 M USD** → Limak-Kolin-Cengiz）⇒ **记为死路，不再重复检索**；只能对 5 家定期巡检 + TaahhütHaber 兜底。

**⑧ 修正后的行动优先级（替换前节）**：① **守**——不投写死 NAC/网管/堆叠的标；② **攻**——投没写生态条款的标（**水务 / 市政 / 大学 / 医院**，如 İTÜ、İSU：只写参数与履历）；③ **绕**——通过 Angora / Trio / Ultron / Cyberwise 进，我方做**裸机 / 白牌 SFP / 板卡 ODM**，不露品牌；④ **不追**——Forescout 矩阵与 IEC 62443 均为"品牌方出面 + 季度级"，**先问不承诺**。

**证据等级**：ETİ MADEN 清单与 3.1.a–g = **A**（官方 PDF 逐条）· 3.1.1 硬指标 = **A** · UEDAŞ PDF 格式与两金额 = **A** · OEDAŞ 结果页 = **B**（页面抓取失败，SERP 摘要）· TaahhütHaber 覆盖 TTK 组 = **B+** · TTK"因取消而无中标方" = **A（机制）+ 推断**。
**空白**：ETİ MADEN 该标年份未标（PDF 路径 `tenders/2020/09`，正文无日期）· 该标中标方未知 · Forescout 8.2 矩阵是否含 Angora/我方未查 · 余下 16 家 EDAŞ 公示形态未逐一确认 · GDZ 规格仍缺 · EÜAŞ 结果未出。
"""
