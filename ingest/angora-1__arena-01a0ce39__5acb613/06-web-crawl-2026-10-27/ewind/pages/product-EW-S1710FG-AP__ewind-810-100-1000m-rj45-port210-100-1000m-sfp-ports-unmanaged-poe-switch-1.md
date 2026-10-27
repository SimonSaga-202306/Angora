# Ewind EW-S1710FG-AP — 8×1G + 2×SFP unmanaged PoE switch, 120 W, dial-code AI-PoE

| field | value |
|---|---|
| URL | https://www.ewindnet.com/product/ewind-810-100-1000m-rj45-port210-100-1000m-sfp-ports-unmanaged-poe-switch-1/ |
| WP post id | 10869 |
| published | 2026-08-06T11:36:52 |
| modified | **2026-08-07T00:07:44 — newest product modification on the whole site** |
| our capture | 2026-10-27T01:23Z (09:23 +0800) |
| capture fidelity | rendered text only — raw HTML not saved |
| datasheet | /wp-content/uploads/file/20260806/EW-S1710FG-AP.pdf (NOT downloaded this round) |
| r24/r25 status | never captured — first appearance in our corpus is this file |

## Spec table (verbatim rows)

| item | spec |
|---|---|
| Model | EW-S1710FG-AP |
| Downlinks | 8× 10/100/1000M RJ45 (PoE) |
| Uplinks | 2× 1000M SFP |
| Management | **unmanaged** (plug-and-play) |
| PoE standard | IEEE 802.3af/at, 15.4 W per port standard, 30 W max per port |
| PoE power budget | **120 W built-in** power supply |
| PoE pins | 1,2 (+), 3,6 (−) — mode A only, no 4,5/7,8 |
| Switching capacity | 20 Gbps |
| Forwarding rate | 14.88 Mpps |
| MAC table | 8 K |
| Jumbo frame | 10 K |
| Case | metal, 19" rack-ear optional |
| Dial switch | **E / V / D** three-position (see below) |
| Warranty | **1 year** |
| Working temp | 0 °C … 50 °C |

## The dial code — the actual differentiator
- **E (Extend)** — forces 10 M mode on ports 1–8 and pushes reach to **300 m** over Cat5e/Cat6. This is the "cheap long-run camera" trick: negotiate down, run long.
- **V (VLAN isolation)** — hardware per-port isolation, so 8 cameras cannot talk to each other (tenant / multi-operator CCTV installs).
- **D (Default / AI-PoE)** — AI watchdog: the switch detects a dead PD, cuts PoE and re-powers the port, rebooting the frozen camera without a truck roll.

## Price-segment signals
- **1-year warranty** is the shortest we have observed in the whole Ewind catalogue (siblings advertise 3 years: ids 8998, 8488, 7030, 3876). That is the clearest public marker of the entry-level tier.
- Built-in 120 W PSU (not an external brick) at this class is a cost-engineering choice worth flagging to the buyer for thermal/MTBF comparison against Angora's Hitit 120 W PoE units.

## Competitive read
Direct functional overlap with **Angora Hitit ANW-1008-MGP120 / -MMP120** (8-port, 120 W PoE). Ewind wins on price positioning and the dial simplicity; Angora wins on being managed-optional and quoting −10…+60 °C industrial range. Keep both numbers in the same comparison sheet rather than quoting marketing "industrial grade" from either side.
