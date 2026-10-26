# 125 · TronX 官网全页取证（tronx.com.tr）

> 轮次：第 32 轮（2026-10-21）｜ 用户指令：谷歌搜 "tronx poe switch" 命中 `tronx.com.tr`「TronX Switch Ailesi」页 → 抓取相关信息 + **宪法式规则：抓到的信息全部入库**
> 取证日期：2026-10-21（+08）｜ 方法：直连全页抓取 + Wayback CDX
> 关联：`09-orders/124-...`（networkmarket 零售店取证）/ `06-competitors/41-larch-angora-partnership-timeline-2026-10-21.md` / 语料 `01-knowledge-base/wechat-conversation-aligned.md` L5852-5905

---

## 1. 公司实体（/about/ 页原文）

- **法定名**：**TRONX BİLİŞİM VE SAĞLIK TEKNOLOJİLERİ LTD**（TronX 信息与医疗科技有限公司）
- **成立**：**2008 年**，从**医疗/医院耗材销售**起家（原文：「2008 yılında tıbbi ve hastane malzemeleri satışı ile ticari faaliyetlerine başlayan」）
- **官网自述**：14+ 年经验（2008→2022 口径）；愿景 = 在医疗技术与 IT 公司间成为领导者
- **地址**：Mustafa Kemal Mahallesi 2124 Cad. No: 14/1, Çankaya / **ANKARA** / TÜRKİYE
- **电话/邮箱**：+90 312 309 19 54 / info@tronx.com.tr
- **三大业务线**（首页 + about 一致）：
  1. **Medikal**（医疗产品）—— 起家业务
  2. **Dijital Kürsüler**（数字讲台/Kiosk，医疗行业为主）
  3. **Network Ürünleri**（企业网络设备：「Kurumsal ağlar için son teknoloji kurumsal ağ cihazları ve yazılımları üretiyoruz」）
- 官网另有 **TRONX Sağlık Teknolojileri** 线（数字医院方案、病床旁患者身份认证系统 hastabasi-dogrulama）

## 2. ⭐ Levent 对 TronX 品牌定位的官方口径（微信 2025-07-23，verbatim）

> Simon（~20:48）：「…as I remember, there were TronX info on the models, at the same time you got https://tronx.com.tr/ so this is an individual brand? I mean what is its position? You are building this brand(TronX) like Angora Networks or just use it as a tool for import & promotion?」
>
> **Levent（20:58）：「3- TronX is a brand we have created together with a partner for his sales only. He has his own channel. We are more like backoffice for him. We manufacture, give him tech support etc」**

**定论**：TronX = Angora（Levent 方）与某伙伴**共同创建的专属品牌**，**仅该伙伴销售**（该伙伴自有渠道），**Angora 是其 backoffice**（制造 + 技术支持）。tronx.com.tr 的「参考客户」（EGM/卫生部/交通部/Jandarma）= 该伙伴的政企渠道资产，不是 Angora 直接客户。
（同段 20:51 Levent 还交代了 NetworkMarket.online = 自家电商橱窗，POS 对接银行支持信用卡/分期，license ~$1K/年 + 服务器，**年成本 ~$2K**，「We can carry the cost on our side」「We mainly focus on offline sales」「I think we know the mistake we made in the first round」→ 该店 2025-06-20 关闭，见 124 号。）

## 3. 全页清单与要点（2026-10-21 抓取）

| 页面 | URL | 状态/要点 |
|---|---|---|
| 首页 | `/` | WP（uploads 自 **2022/08**）；三大业务线 + REFERANSLARIMIZ 客户墙 + KVKK 隐私政策；导航含 Network→Switçler→`/verge-switch-ailesi/`、Packet Broker→`/network-packet-broker/` |
| Switch 家族 | `/switch-ailesi/` | ⭐ 全型号规格表（下表）；页面图 uploads **2023/07**；「Türkiye'nin öncü kurumları tarafından kullanılan yönetilebilir akıllı switch ailesi」；特性：L2+、PoE+ 每口 30W、**Türkçe arayüz**、CLI、SNMP、**REST API** |
| **Packet Broker** | `/network-packet-broker/` | ⭐ NPB 产品页（详 §4）；「Türkiye'nin ağ paket dağıtıcısı」；**Yasal Yakalama**（ISP 法定流量留存/监控）卖点 |
| 关于 | `/about/` | 公司实体（§1）+ 客户墙 |
| 联系 | `/contact/` | 安卡拉地址/电话/邮箱（§1） |
| 博客 | blog 页 | 仅 2 帖：2022-08-12 数字医院、2020-08-26 HIMSS EMRAM（医疗内容） |
| ❌ `/verge-switch-ailesi/` | 404 | 首页导航指向已改名/未上线的 VERGE 品牌页 = **站点半损坏**（与 about 页残留 `sap-station.com/tronx.com.tr/about-me/` 模板链接、首页 `/tronx.com.tr/dijital-kursu/` 双重路径损坏同因） |

## 4. ⭐ TronX 产品型号 ↔ 我方 ODM 订单映射

### 4.1 Switch 家族（/switch-ailesi/ 规格表，8 口~DC）

| TronX 型号 | 端口 | 关键规格 | 对应我方/订单 |
|---|---|---|---|
| Industrial 8 口 | 8×1G + 4×1/10G SFP+ | L2+、DIN 导轨、**-40°C~+80°C、48V DC、PoE+、IP40、防雷 6KV**（TRX-EN8-1 / TRX-EN8-2，MAC 8K，Jumbo 9.6K） | = 第 6 单 **6 台工业 2 光 8 电**（STI-288DGGPM 系） |
| Enterprise 8 口 | 8×1G + 2×1/10G | L2/L2+/L3、180W AC | VERGE 入门档 |
| 24 口 | 24×1G + 4×1/10G | L2/L2+/L3、380W AC、PoE/Non-PoE | = 第 3/4/5 单 24 口系（**TRX-KS24-1 / TRX-KS24-2** PoE 版） |
| 48 口 | 48×1G + 4×1/10G | L2/L2+/L3、740W AC、PoE/Non-PoE | = **TRX-KS48-1 / TRX-KS48-2** |
| **Data Center/TOR** | **48×1G/10G/25G + 6×100G QSFP28** | **3.6 Tbps**、Advanced L3（BGP/MPLS/L3VPN/VRF/RSVP）、TRILL/OpenFlow/Netconf、冗余热插电源 | = **TRX-OM1 / TRX-OM2**（48×25G SFP28 + 8×100G，L3 全协议，MAC 128K，VLAN 4K，IPv4 路由 64K） |

> 注：TronX 页面 OM1 标 4Tbps / OM2 标 1Tbps（同一端口配置的两种吞吐档）；与 networkmarket.online 2025-03 价目页同型号（见 124 号 §2：OM1 核心售价 $37,700）。
> L3 清单（全型号通用文案）：Static/IPv4&IPv6、RIPv1/v2、RIPng、OSPFv2/v3、IS-IS/IS-ISv6、BGP/BGPv6、VLAN 4K、MAC 128K、IPv4 路由 64K、TRILL、OpenFlow、Netconf。

### 4.2 ⭐ NPB（/network-packet-broker/ 规格表，verbatim）

| 项 | 值 |
|---|---|
| 型号 | **T-IQ-PB-1**（基础硬件+license：8×1/10/25G 100Gbps Throughput）、**T-IQ-PB-2**（**Ek Lisans = 追加 license**，同一硬件 = **license 分级销售结构**） |
| 1/10/25Gb 接口 | **48** |
| 100Gb 接口 | **6** |
| **Paket işleyici（包处理器）** | **Marvell** ⭐ |
| Flash – RAM | 16GB – 8GB |
| **Trafik Sınırı（吞吐上限）** | **1.9 Tbps** |
| 电源 / 风扇 | 1+1 冗余 220V 650W / 4+1 冗余 |
| 尺寸 | 1U，440×470×44 mm |
| 过滤维度 | L2 MAC / VLAN / MPLS / Ethertype；L3 IPv4&IPv6 / DSCP / 协议号；L4 TCP/UDP 端口 |
| 端口映射 | 单↔单、单↔多、多↔单、多↔多 + 负载组 |
| 功能 | 100% 无损复制、**Dedup**、**SSL 解密协助**、应用识别（**首 128 字节** + DPI 集成）、隧道终结/解封装、ERSPAN、GRE、VxLAN、包分割、端口打标、协议头剥离 |
| 管理 | 拖拽式 Web UI + SNMP 告警 |
| 定位文案 | 「**Yasal Yakalama** — 尤其服务于 ISP 的法定监控义务」；「基于 **TRONX 数据中心交换机**的包转发技术」 |

**映射结论**：T-IQ-PB-1/2 = 48×10/25G + 6×100G + Marvell + 1.9Tbps = **我方第 6 单 Marvell NPB（NEXUS-48X32T50 系）的 TronX 品牌化**（未了结项 TronX $1,480 见 121/122 号，PASSED）。TronX 品牌 = 同一批硬件换 TronX 外壳 + 独立渠道销售，印证 Levent「We manufacture, give him tech support」。

## 5. 参考客户（REFERANSLARIMIZ，uploads 2022/09）

**EGM（国家警察总局）** / **Jandarma（宪兵）** / **Ulaştırma（交通部）** / **Sağlık Bakanlığı（卫生部）** / Osmaniye 省卫生司 / Erzincan 省卫生司

→ EGM 与 Angora 2026-04-28/29 警队标（3,300+600+200 台，EGM = 同一客户，见 122 号）同源：TronX 伙伴方持 EGM 渠道，Angora 标单与 TronX 渠道**共用同一最终客户池**。

## 6. Wayback 与边界

- **tronx.com.tr Wayback = 0 快照**（CDX 域名级查询 2 次均空）→ 该站**从未被归档**，无历史取证可能；站点内容时间戳（uploads 2022/08~2023/07）显示 ~2022 建站、2023-07 上 switch/PB 产品页。
- 站点维护状态：内容冻结于 2022-2023（博客最后 2022-08），VERGE 改名半成品（404）→ 站点**低维护、半废弃**，但产品 = 我方在产 ODM 型号全映射。
- 边界：TronX「伙伴」本人身份未确认（Levent 未具名）；TronX 与 EGM 标的直接参与关系未证实（仅客户墙重叠推断）；T-IQ-PB 的「1.9 Tbps」vs 我方 datasheet 3.2Tbps 口径差异 = 官网降档标称，待核。
