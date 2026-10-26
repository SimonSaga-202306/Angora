# Angora 网站镜像 · 第 3 部分：完整规格表、产品编码、宣传册、合作伙伴

> 2026-09-23 · 来源：旧域名 `angoranetworks.com`（新域名 `angorateknoloji.com` 本轮疑似被 Cloudflare 限流，
> 先前已抓到的内容在 `10-pages-part1.md` / `11-pages-part2.md`）

---

## ⭐ 一、SYNAPSE 完整技术规格表（逐字）

来源：https://www.angoranetworks.com/synapse-network-switch-ailesi/
标题：**SYNAPSE KURUMSAL AĞ ANAHTARI AİLESİ**（SYNAPSE 企业网交换机家族）

| 特性 | ANW-2712-8T4X | ANW-2712-24T4X | ANW-2712-48T4X | ANW-2712-48T6X | ANW-5713-24S8T6X |
|---|---|---|---|---|---|
| **端口** | | | | | |
| 千兆 PoE+ | 8 | 24 | 48 | 48 | 8T + 24S |
| 10G/GE SFP+ | 4 | 4 | 4 | 6 | 6 |
| Console (RJ45) | 1 | 1 | 1 | 1 | 1 |
| **性能** | | | | | |
| 交换容量 (Gbps) | 128 | 128 | 216 | 216 | 128 |
| 包转发率 (Mpps) | 72 | 99 | 162 | 162 | 106 |
| **物理** | | | | | |
| 重量 (kg) | 1.6 | 3 | 5.2 | 5.2 | 3.9 |
| 尺寸 宽×深×高 (mm) | 280×180×44 | 441.1×207.5×44 | 440×280×44 | 440×280×44 | 440×280×44 |
| 风扇数 | **0（无风扇）** | 2 | 2 | 2 | 2 |
| **电源** | | | | | |
| 空载功耗 | <25W | <25W | <25W | <25W | <25W |
| 满载（不含 PoE） | <35W | <35W | <48W | <48W | <48W |
| 电源 | 160W AC | 410W AC | **450W AC / 800W DC** | **450W AC / 800W DC** | 450W AC |
| PoE 预算 | 125W | 370W | 370W(AC) / **740W(DC)** | 370W(AC) / **740W(DC)** | 370W(AC) |
| 电压与防护 | 220V AC / 48V DC / **6kV 浪涌保护** | 同 | 同 | 同 | 同 |
| **环境与可靠性** | | | | | |
| **工作温度** | **−10 / +60 °C** | 同 | 同 | 同 | 同 |
| MTBF | > 1,000,000 小时 | 同 | 同 | 同 | 同 |

### 🔴 关键结论：SYNAPSE 是商用级，不是工业级

> **工作温度 −10°C ~ +60°C。**
>
> 对照：
> - **我方 TT-2208-PG / ANW-11xx 工业机：−40°C ~ +75°C**
> - **Angora 旧版 VERGE 工业 8 口标称：−40°C ~ +80°C**
> - **Türk Telekom 招标要求：−45°C ~ +85°C**
>
> **→ SYNAPSE 在温度这一项上比我方工业机差了整整一个等级（50°C 的差距）。**
> **SYNAPSE 不能用于 TT 的基站/户外机柜场景，也不能用于 EGM/KGM 等户外项目。**
>
> 这直接说明：**SYNAPSE 不是我方工业机的替代品，它补的是"企业网/机房接入"这一档。**
> 我方被替换的若是工业 8 口（ANW-1104/1108 系列），那替代者**不是 SYNAPSE**，
> 需继续查 HITIT 或新版 VERGE 的 `ANW-IND-8P-2SFP`。

### 其他观察
- ANW-2712-8T4X **无风扇（0 fan）** + 280×180×44 小尺寸 + 125W PoE → 典型的**小型办公室/壁挂**定位。
- 48 口机型支持 **800W DC 输入 + 740W PoE 预算** —— 这个规格**明显高于**旧版 VERGE 48 口的 740W AC，
  说明 **48 口这一档确实升级了**（对应 Levent 要的"双电源 / 高 PoE 预算"）。
- 6kV 浪涌保护、MTBF>100 万小时 —— 这是**运营商级话术**，说明 SYNAPSE 是冲着**电信/政企招标**去的。

---

## ⭐ 二、产品编码全表（`/network-devices/`，2025-06 版）

来源：https://www.angoranetworks.com/network-devices/

| 系列 | 型号编码 |
|---|---|
| **工业 8 口国产交换机** | **ANW-1104-TG、ANW-1104-PG、ANW-1104-PX**<br>**ANW-1108-TG、ANW-1108-TX、ANW-1108-PG、ANW-1108-PX** |
| **企业级 8 口** | **ANW-2108-TG、ANW-2108-TX** |
| **8/24/48 口** | **ANW-2208-TG、ANW-2208-TX**<br>**ANW-2224-TG、ANW-2224-TX**<br>**ANW-2248-TG、ANW-2248-TX** |
| **数据中心 / TOR 边缘路由** | **2420-24 / 3224-RCF / 4124X-6Z**<br>**2420-48 / 3248-RCF / 4148X-6Z**<br>**2520-32Q / 3232-RSE**<br>**4432Z-2TX-100/400**<br>**2520-48 / 3248-RSE**<br>**4224Y-8Z** |

### 🔴 重大发现：数据中心/TOR 这一档**没有 ANW 前缀**

```
2420-24 / 3224-RCF / 4124X-6Z
2420-48 / 3248-RCF / 4148X-6Z
2520-32Q / 3232-RSE
4432Z-2TX-100/400
2520-48 / 3248-RSE
4224Y-8Z
```

**这些不是 Angora 自己的型号命名体系**（其他三档全是 `ANW-` 开头）。

**推断：数据中心/TOR 这一档是外部平台的原厂型号直接沿用** —— 极可能就是
**Larch Networks 或其 ODM（Marvell 参考设计 / Lanaotek / Scodeno）的平台编号**。

> **这与以下事实互相印证**：
> ① Larch 官网有 **Data Center Switches** 与 **Network Packet Brokers** 两个设备分类；
> ② Larch 是 **Marvell 认证方案提供商**，卖"含板卡布局+软件+生产测试工具的交钥匙设计"；
> ③ Angora 在 Larch 的 **Clients 客户页**上；
> ④ Angora 官方宣称"软件 100% 自研"却同时挂着 Larch —— **刻意淡化**。
>
> **→ DC/TOR 这一档几乎可以断定来自 Larch。建议逐型号去 Larch 官网比对。**

### 规格表其他要点（2025-06 版）
- 工业 8 口：**−40°C ~ +80°C，48V DC，PoE+，DIN 导轨**，Layer 2/2+/3
- 8/24/48 口：Layer 2/2+/3，180W / 380W AC，PoE / 非 PoE
- DC/TOR：**3.6 Tbps 超低时延**，6×100G QSFP28，**Advanced L3 Routing**，
  **OTP、LISP、VXLAN、MC-LAG、BGP6、REST API、MPLS、Multicast RSVP、L3VPN、VRF**，
  **冗余热插拔电源**，端口 24/48×1G/10G/25G + 4/6/8×100G
- 安全特性：IEEE 802.1X、动态 ARP 检测、IP 源保护、DHCP Snooping、**ND Inspection**、**OTV、LISP、VXLAN**
- 管理：CLI、**Angora 管理平台（Angora Yönetim Platformu）**、智能物理接口、SNMP、**REST API**
- 页面底部："Sabit kurumsal gigabit ethernet kenar anahtarlar ve **10/25/40/100G fiber omurga anahtarlar**"

---

## ⭐ 三、全部下载资源直链（`/brosurler/` + 产品页；汇编官方版见 `90-downloads.md`）

| 产品线 | 直链 |
|---|---|
| **Verge 交换机家族** | https://www.angoranetworks.com/download/1015/ |
| **Gordion 交换机家族**（Gordion 数据中心系列） | https://www.angoranetworks.com/download/1053/ |
| **Angora NMS 管理平台** | https://www.angoranetworks.com/download/1035/ |
| **Iris SFP 模块家族** | https://www.angoranetworks.com/download/1039/ |
| **Thince 瘦客户机** | https://www.angoranetworks.com/download/1027/ |
| **Karınca 网络数据包代理** | https://www.angoranetworks.com/download/1031/ |
| **Arrow 数据二极管** | https://www.angoranetworks.com/download/1057/ |
| **Arı 安全处理设备** | https://www.angoranetworks.com/download/1062/ |
| **工业国产交换机数据表**（已解析） | https://www.angoranetworks.com/download/425/ |
| **8-24-48 口国产交换机** | https://www.angoranetworks.com/download/428/ |
| **Synapse 交换机**（新） | https://www.angoranetworks.com/download/1797/ |
| **IRIS-10G Data Sheet** | https://www.angoranetworks.com/download/485/ |
| **IRIS-5G SFP Data Sheet** | https://www.angoranetworks.com/download/488/ |
| **IRIS 100G SFP Data Sheet** | https://www.angoranetworks.com/download/491/ |

> **`ANW-GORDION`** 出现在 2026 新版 VERGE 型号列表里 —— 现在确认
> **Gordion 是一个独立的数据中心交换机家族**，有自己的宣传册（download/1053/）。
> **这是 Karınca NPB 之外的第二条高端产品线。**

---

## 四、合作伙伴墙（完整，来自 RU 首页）

来源：https://www.angoranetworks.com/?lang=ru

`alaattin_bilisim`、`fi_teknoloji`、`sonersan`、**intel**、**abb**、**ubuntu**、
**larch**、**marvell**、`rasberrie`（Raspberry Pi）、`sixfab`、`samm`、`dmy`、`astesan`

| 类别 | 伙伴 |
|---|---|
| **技术/芯片** | **Marvell**、**Larch Networks**、**Intel** |
| **软件/系统** | **Ubuntu**、Raspberry Pi |
| **工业/自动化** | **ABB**、Sixfab（IoT 蜂窝） |
| **土耳其本地渠道/集成** | **Alaattın Bilişim**、**Fİ Teknoloji**、**Sonersan**、SAMM、DMY、**Astesan**（国防电子） |

### 新增发现
- **Alaattın Bilişim** —— 与 Angora 合作完成 **PacketFence NAC（802.1x）集成**，
  "可交钥匙交付 PacketFence + Angora Networks 方案"。
- **Astesan** —— 土耳其国防电子公司，出现在伙伴墙上。
- **ABB / Sixfab** —— 工业自动化与 IoT 方向，对应 Angora 的"智慧灯杆/工业路由器/智能箱"等 Integrated Network 产品线。
- **此前发现的 Advensis**（advensis.com.tr/en/angora-en/）—— 另一家分销商/方案商，
  代理 VERGE、THiNCE、IRIS SFP、ANGORA NMS，地址 Çankaya/ANKARA No:14/7。

### 客户墙（References）—— 第三次确认**没有 Türk Telekom**
MSB（国防部）、ASELSAN、Anadolu Üniversitesi、HAVELSAN、TSK（军队）、
Sağlık Bakanlığı（卫生部）、TÜRKSAT、TCDD（铁路）、KGM（公路总局）、
Turkcell KKTC、EGM（警察总局）

---

## 五、公司发展时间线（旧站 About 页）

```
2016  Foundation                成立
2017  First Services            咨询、维护与研发
2018  First Product             首款产品：24 口交换机（PoE 与非 PoE）
2019  Sales Channels            现货商用（COTS）产品销售 + 销售渠道建立
2020  New Generation Products   新一代产品成长、海外业务拓展
```

> **"2019 COTS（Commercial Off-The-Shelf，现货商用）产品销售"** ——
> **这是 Angora 自己承认的"贴牌/转售"阶段。** 与海关数据（2023–2024 大量中国进口）完全吻合。

---

## 六、爬取状态与问题记录

| 项 | 状态 |
|---|---|
| 新域名 `angorateknoloji.com` | ⚠️ 本轮**疑似被限流**：首页 fetch 失败，`/iletisim/`、`/blog/`、`/verge-network-switch-serisi/` 等**之前成功抓过的页面现在返回 404**。待稍后重试。 |
| 旧域名 `angoranetworks.com` | ✅ **完全正常**，已抓：首页 TR/EN/**RU**、`/network-devices/`、`/verge-network-switch-family/?lang=en`、`/synapse-network-switch-ailesi/`、`/brosurler/`、`/yerli-network-packet-broker/?lang=en` |
| `/submarine/`（新域） | ❌ 404（可能不存在） |
| `/gizlilik-politikasi/`（新域） | ❌ 404 |
| `/blog/page/2/`（新域） | ❌ 404（只有 1 页，或分页路径不同） |
| 抓取工具注意事项 | ⚠️ `fetch_page` 会剥掉路径尾部斜杠，导致部分站点返回假 404。加 `?lang=xx` 查询参数**仍会被剥离**，无法绕过。 |

### 待抓（下一轮）
- 新域名恢复后：全部 RU 页面、`/blog/` 各篇文章全文、隐私政策
- 旧域名：`/hitit-yerli-network-switch-ailesi/`（对比新旧 HITIT）、
  `/iris-sfp-ailesi/`、`/ari-sd-wan-.../`、`/angora-nms/`、`/ozgun-tasarim-oem-odm-hizmeti/`
- 宣传册 PDF：优先 **Gordion（1053）**、**Synapse（1797）**、**8-24-48 口（428）**
