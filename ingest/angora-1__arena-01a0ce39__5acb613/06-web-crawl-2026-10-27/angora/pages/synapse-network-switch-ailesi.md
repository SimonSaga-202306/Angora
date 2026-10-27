# Angora **Synapse** — enterprise switch family（2026-10-27 复核）

## ⚠ 同 Hitit：不是"本轮新发现"
`01-text-verbatim/workstation/04-website-mirror/12-pages-part3-specs-and-codes.md` §一 已在 **2026-09-23** 全量收录 Synapse 规格表（含尺寸、风扇数、满载功耗，比本轮抓到的还细）。本轮新增的只有：REST 时间戳、与 Ewind L3 机型的速度档位对比。

| field | value |
|---|---|
| URL | https://www.angoranetworks.com/synapse-network-switch-ailesi/ |
| WP page id | 1781 |
| published | 2026-01-15T09:48:09 |
| modified | **2026-01-15T10:20:01**（≈ 9 个月未再改） |
| capture r39 | 2026-10-27T01:24Z，rendered text，raw HTML 未保存 |
| 内容变更判定 | 与 09-23 镜像一致（端口/PoE/温度/MTBF 逐行对上），**无变化** |
| 宣传册 | /download/1797/（未下载） |

## 型号表（r39 复核值）
| 型号 | 接入 | 上联 | 交换容量 | 转发率 | PoE 预算 | 电源 | 风扇 | 重量 |
|---|---|---|---|---|---|---|---|---|
| ANW-2712-8T4X | 8×1G PoE+ | 4×10G SFP+ | 128 Gbps | 72 Mpps | 125 W | 160 W AC | **0（无风扇）** | 1.6 kg |
| ANW-2712-24T4X | 24×1G PoE+ | 4×10G SFP+ | 128 Gbps | 99 Mpps | 370 W | 410 W AC | 2 | 3 kg |
| ANW-2712-48T4X | 48×1G PoE+ | 4×10G SFP+ | 216 Gbps | 162 Mpps | 370 W (AC) | **450 W AC / 800 W DC** | 2 | 5.2 kg |
| ANW-2712-48T6X | 48×1G PoE+ | 6×10G SFP+ | 216 Gbps | 162 Mpps | 370 W (AC) / **740 W (DC)** | 450 W AC / 800 W DC | 2 | 5.2 kg |
| ANW-5713-24S8T6X | 24×10G SFP+ + 8×1G | 6×10G SFP+ | 128 Gbps | 106 Mpps | 370 W (AC) | 450 W AC | 2 | 3.9 kg |

环境/可靠性：工作温度 **−10 … +60 °C**，MTBF **> 1,000,000 h**，220 VAC / 48 VDC，6 kV 浪涌。空载 <25 W、满载（不含 PoE）<35 W（8 口）/ <48 W（24·48 口）。

## 与 Ewind 的档位差（r39 新增）
- Ewind **EW-S57948QM**：48× **2.5G** + 4×10G SFP+，1280 Gbps，952 Mpps，**BGP**，150 W，0–40 °C。
- Synapse 全线是 **1G 接入 + 10G 上联**，**没有 2.5G 接入档**，也没有 25G/100G 上联（Angora 的 100G 在 `/network-devices/` 的 DC/TOR 编码里，属另一条线）。
- 结论：**接入侧 Angora 慢一档（1G vs 2.5G），可靠性侧 Angora 领先（−10…+60 °C + MTBF 白纸黑字 vs Ewind 的 0–40 °C 且无 MTBF）**。对外话术不要互相抵消，按场景拆分引用。
- 2026-09-23 镜像已裁定"Synapse 是商用级、不能替代工业机"；r39 的温度/尺寸数据不改变该结论。
