# 122 · 规格实锤与目录空位（r53 · 2026-11-01）

> 本轮做三件事：**① 把 `CLR-MRS-8330P` 的规格挖到底（结果推翻我自己 r52 的判断）；② 读到 CryptoLink 两份工业线 PDF（拿到换牌实证）；③ 点开 Technopc 的 Network 目录（发现是空的）。**
>
> 一句话：**r52 说「它 2.5G 线没有 bt」是错的 —— 它有，1–4 口 90 W、总 400 W。真正的缝只剩「24 口全 bt + 800 W」。**

---

## 一、🛑 修正 r52：`CLR-MRS-8330P` 就是一台 **2.5G + bt** 的机器

| r52 判断 | r53 实测（`gelecekbt.com/2.5G-POE-Multirate-L3-Switch-30-Port-6-10G-Uplink-CLR-MRS-8330P` 技术表原文） | 判定 |
|---|---|---|
| 「没有一款 2.5G SKU 标 802.3bt」 | **`24* 100/1000/2500 Mbps PoE Ports (Ports 1-4 support IEEE802.3bt(90W))`**；PoE 栏列 **af 15.4 W / at 30 W / bt 90 W** | ❌ **推翻** |
| 「`-8330P` PoE 功率未知」 | **`PoE Total Power maximum 400W`**，整机 max 52 W，电源 **DC 54V 7.69A + 12V 5A** | ✅ **400 W** |
| 「2.5G PoE 只有 100 W」 | 100 W 是 8 口那台（`-8109P`）；24 口这台 **400 W** | ❌ 口径错，已改 |

### `CLR-MRS-8330P` 全表
| 项 | 值 |
|---|---|
| 端口 | **24×100/1000/2500 PoE（1–4 口 bt 90 W）+ 6×10G SFP+ + 1 Console** |
| 交换 / 转发 | **240 Gbps / 178.56 Mpps** |
| 内存 | DDR **512 MB** / Flash **32 MB** / Buffer 16 Mbit / MAC **32K** / Jumbo 10K |
| PoE | af/at/**bt 90 W**，**总 400 W** |
| VLAN | 1–4094（最大活跃 4K） |
| 温度 | **−10~50 °C**（商用级） |
| L3 | **只有 IPv4/IPv6 VLAN 接口 + IPv4 静态路由 + ARP**（**无 OSPF / 无 VRRP**） |
| 尺寸 / 重 | **440×281×44 mm** / N.W **4.37 kg**，5 台/箱 |
| 特色 | **PoE 使用率指示灯**（<90% 灭 / 90–95% 闪 / >95% 亮）+ 超温超压告警灯 |
| 认证 | CE / FCC / RoHS |

⭐ **两个可在谈判中打的具体短板**：
1. **工作温度 −10~50 °C** —— 这是**商用机箱**，不是工业级（对比它自家 `CLR-IES-T120N` 是 **−40~+85 °C**）。
2. **L3 只到静态路由**，**没有 OSPF / VRRP**（同样 2.5G 定位的 `CRL-SW-L3-2404-10G` 反而有 OSPF+VRRP）→ **「L3」是它的营销词，路由能力分层严重**。

### 修正后的正确话术
| 错（r52） | 对（r53） |
|---|---|
| 「它没有 2.5G bt」 | 「它**只有 4 个 bt 口**，总预算 **400 W**（24 口均摊 ≈16.7 W），要接 20 台 bt 摄像头就不够」 |
| 「补位 2.5G」 | 「**24 口全 bt + 800 W**」→ `EW-PIS5728GM-AP-BT`（28 口 L3 / 800 W / 24×bt） |
| — | 追加：**「L3 要 OSPF/VRRP 的话，它这台上没有」**（我方 `EW-S5748GM-AP` 有动态路由） |

---

## 二、⚠ 必须承认：**它有两档比我方齐**

| 档位 | CLR 型号 | 我方现状 |
|---|---|---|
| **10G 电口接入** | ⭐ **`CLR-SWT-7514C` = 12×10G RJ45 + 2×SFP+ 全 10G 网管** | 我方 2.5G 有（`EW-S6826`），**10G 电口 12 口这一档没有对位** |
| **工业 10G SFP+ 骨干** | ⭐ **`CLR-IES-T120N` = 12×1G/10G SFP+，240 Gbps，双核 1 GHz，32K MAC，DC12–48 V 防反接，−40~+85 °C，25 W，导轨 166×150×75** | 我方工业最高 8 口 GE（`EW-EPIS3910-8GE`） |

→ **谈判纪律：不要在这两档正面比。** 改打 **「2.5G 全口 bt + 大功率」** 与 **「2.5G 长距 300 m」**。
→ **r54 产品侧建议**：这两档是**产品缺口**（不是我方销售缺口），值得回传产品部。

### r53 新增 CLR 型号（累计 17 个）
`CLR-MRS-8330N/P`、`CLR-MRS-8226N`、`CLR-MRS-8218N`、`CLR-MRS-8312N/P`、`CLR-MRS-8109N/P`、`CLR-MRS-8106N/P`、`CLR-SWT-80F`、`CLR-DCS-2110N/P`、`CLR-DCS-6332F/6432F`、`CLR-SWT-5736F/3754F/7423F/7312F/7520F/**7514C**/4804N/4244F/2412P/L328P/2404`、`CLR-SWG-1716/1724`、`CLR-IES-T120N/L288P/2520P/7214P/2512P/G82P`、`CLR-SWF-9006BT`。

---

## 三、⭐⭐ CryptoLink：PDF 里还留着原厂牌子 **CrystalWAN**

`DatasheetofCRLISW-14.pdf` **封面页眉原文 = `CrystalWAN Network Solutions`**，内页型号 **`CRLISW-414`**；`CRLISW-08.pdf` 内页型号 **`CRLISW-8P`**。
→ **一份 PDF 三个名字**（CrystalWAN / CRLISW-414 / CryptoLINK）⇒ **它把 OEM 的 PPT 只改了封面**。**r52 的「代理品牌」判定成立，且证据从"页脚印 Authorized Dealer"升级为"原厂 logo 都没删"**。

| 项 | `CRLISW-08`(=`CRLISW-8P`) | `CRLISW-14P`(=`CRLISW-414`) |
|---|---|---|
| 端口 | **8×GE PoE + 2×GE SFP + Console** | **8×GE PoE + 4×GE SFP + Console** |
| PoE | af/at，**总 240 W** | af/at，**总 120 W** |
| 交换 / MAC | 24 Gbps / 8K | 24 Gbps / **16K** |
| 冗余 | STP/RSTP/MSTP + **ERPS** + LACP + **PD Alive (WatchDog)** | 同左 + NTP |
| 供电 | **双路 DC48–55 V 凤凰端子 + 防反接** | 同左 |
| 温度 / 防护 | **−40~85 °C** / **IP40** / 防雷 6 kV·4 kV·ESD 15 kV | 同左 |
| MTBF | 100,000 h | **800,000 h** |
| 光 | 多模 2 km；单模 20 / 60 / 80 / 100 / **120 km** | 同左 |

→ **工业段它 100% 停在 af/at 30 W**（温度做得好、功率小）⇒ 对「边界安全 / 车牌识别」这种**多摄像头 + 云台/加热器**场景，**bt 60 W 是硬需求**，我方 `EW-PIS3810M-8GE-BT` / `EW-EPIS3910-8GE` 是干净的一刀。

---

## 四、⭐⭐ Technopc（`A/075`）：**想卖交换机，但目录是空的**

`technopc.com.tr/network-urunleri/` 营销文案承诺 **「gigabit ve 10G destekli switch modelleri … Layer 2/3 yönetilebilir switch … bulut tabanlı yönetim」**，
但**实际只有 5 个产品，全是防火墙与 SD-WAN**：

| 型号 | 类别 | 配置 |
|---|---|---|
| `FW801` | Firewall | Intel 6./7. nesil / 16 GB / 2×2.5" HDD / **SIM kart** |
| `FW622` | Firewall | Celeron N3060 / 8 GB / 6×GE LAN |
| `FW57` | Firewall | Celeron 3205U / 16 GB / 2×COM + 2×LAN |
| `NSW 4500` | SD-WAN | Atom 2.2 GHz / **6×LAN + 4G LTE** |
| `NTSN 6500F` | SD-WAN | Atom C3558 / 128 GB / **6×LAN + 2×SFP** |

页面底部原文 **「Seçilen filtrelere uygun ürün bulunamadı.」**；`/switch/` → **404**。

**⇒ 全名单里唯一一个「已是我方客户 + 公开要做交换机 + 交换机目录为空」的 A 档。**
- 评级建议 **55 → 70**；
- 打法不是开发新客户，是**扩品类**：把 `EW-S1927CG-AP` → `EW-S2926GM-AP` → `EW-S5748GM-AP` → `EW-S6826`（2.5G）做成 **`Technopc` 牌 Network 首屏**，配 `EwindCloud` 正好对应它写的「bulut tabanlı yönetim」；
- 它强项是 **x86（Atom/Celeron/Intel）**，交换机纯外购，**无自研冲突**，比 Telkolink 好谈得多。

---

## 五、r54 待办

1. **TÜRKPATENT 六商标**（`Cifocs` / `Dayline` / `TGD` / `NVC` / `SWP` / `LNG`）—— 仍被 CAPTCHA 卡住，**需人工**；替代路径：查 Trendyol/Hepsiburada 店铺主体、查 `tekniksatgroup` 商标公告。
2. `CLR-MC02` / `CRL-SFP-10G-LC` / `CRL-SFP-125 LC` 三份 PDF。
3. `CLR-MRS-8226N/8218N` 交换容量、`CLR-MRS-8109P` 的 100 W 是否也含 bt 口。
4. **B 档"已在卖交换机"11 家 → 型号级**（Coptek / NFS / iotsistem / Eurocam …）—— 这是 A/B 档最后一块空白。
5. 价格复核 vs **$423 / $900 / $2,050** 三锚点。
6. 产品侧回传：**10G 电口 12 口**、**工业 12×10G SFP+ 骨干** 两个缺口。

---

**相关文件**：`121`（r52 自有品牌大清算，§一.4 已加 r53 修正框）· `116`（缺口矩阵）· `120`（r51 四家自有线）· `119` · `118` · `117`
