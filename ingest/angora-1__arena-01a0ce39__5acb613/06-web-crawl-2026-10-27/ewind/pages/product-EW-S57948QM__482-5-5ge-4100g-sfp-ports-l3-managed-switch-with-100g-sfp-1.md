# Ewind EW-S57948QM — 52-port L3 managed switch (48×2.5G + 4×10G SFP)

| field | value |
|---|---|
| URL | https://www.ewindnet.com/product/482-5-5ge-4100g-sfp-ports-l3-managed-switch-with-100g-sfp-1/ |
| WP post id | 10573 |
| published | 2026-05-11T17:36:54 (site local) |
| modified | 2026-05-11T17:36:55 |
| our capture | 2026-10-27T01:23Z (09:23 +0800) |
| capture fidelity | rendered text only — **raw HTML not saved** (sandbox has no egress; fetch_page returns extracted text) |
| datasheet | /wp-content/uploads/file/20260511/1778492053344125.pdf (NOT downloaded this round) |
| r24/r25 status | never captured — first appearance in our corpus is this file |

## Spec table (verbatim rows)

| item | spec |
|---|---|
| Product model | EW-S57948QM |
| Interface | 48× 2500/5000Base-T + 4× 4000/10000Base-X SFP |
| Console/MGMT | 1 console port + 1 MGMT port |
| Switching capacity | 1280 Gbps |
| Forwarding rate | 952 Mpps |
| Working temperature | 0 °C … 40 °C |
| Storage temperature | −40 °C … 70 °C |
| Working humidity | 10 % – 90 % RH (non-condensing) |
| Dimensions | 440 × 300 × 44 mm |
| Weight | 7 kg |
| Input voltage | AC 100–240 V, 50/60 Hz |
| Total power | 150 W |
| MAC address table | 112 K |
| Jumbo frame | 12 K |
| Lightning protection | 6 KV |
| VLAN | 4K VLANs; Voice VLAN, MAC VLAN, Protocol VLAN |
| Spanning tree | STP/RSTP/MSTP, ERPS (G.8032) |
| Routing | Static routing, RIP v1/v2, OSPF, **BGP** |
| Multicast | IGMP snooping, IGMP proxy, MVR, MLD snooping |
| DHCP | DHCP server / relay / snooping |
| Security | 802.1X, Portal, Radius authentication; ARP anti-DDoS; port isolation; IP source guard |
| Energy | IEEE 802.3az EEE |
| Management | CLI (console/Telnet/SSH), HTTP/HTTPS (Web), SNMP v1/v2 |

## Energy / cost-relevant readings
- 150 W total draw on a 52-port box ≈ 2.9 W/port — squarely *not* PoE; this is an aggregation/edge-uplink switch, not a camera switch.
- BGP on a box with 4×10G uplinks is the notable capability claim: Ewind is pushing L3 at the SMB/edge price point.

## ⚠ Discrepancy to flag (do not propagate the marketing wording)
The page **title/permalink** say "**100G SFP**". The spec table lists only **4 × 4000/10000Base-X** — i.e. 10G, not 100G. Either the title is aspirational, or a 100G variant exists but is not shown. Record the title as the seller's claim and the spec table as the technical fact; a buyer reading only the H1 would over-buy.

## Order list block
The page carries a "related/ordering" list with other L3 models (10569 `24×2.5GE + 6×10G SFP L3 managed PoE`, 10564 `48×10G + 4×100G managed fiber`, 10557 `24×10G + 4×100G L3 fiber SFP`) — these are the sibling "100G" builds, which is the likely origin of the title confusion.
