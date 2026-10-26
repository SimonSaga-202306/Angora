<!-- ============================================================ -->
<!-- FILE 773/781 -->
<!-- PATH: 警察局项目/CGKS_Field_Switch_DLink_DIS300G_Compliance.xlsx -->
<!-- SIZE: 13006 bytes -->
<!-- SHA256: a4748f6c312a2c00b0c4c4aaf6683800bab0b37c4ffcff28a431a16b4a90d0fb -->
<!-- EXTRACTION: openpyxl read-only - every sheet, every row, every cell, formulas preserved (data_only=False) -->
<!-- ============================================================ -->

Workbook: sheets=1

## SHEET: Compliance Matrix  (dims=A1:E32, max_row=32, max_column=5)
```tsv
ÇGKS Field Network Switch — RFP Compliance Assessment  |  D-Link DIS-300G Series
Reference: ÇGKS Yedek Malzeme Alımı Teknik Şartnamesi 2026, Section 3.3.2 — Clauses 3.3.2.1 through 3.3.2.23
Clause	RFP Requirement	DIS-300G Capability	Status	Notes / Gaps
3.3.2.1	Field Network Switch shall be of industrial type.	Industrial Gigabit Managed Switch; purpose-built for industrial environments.	✔  COMPLY	—
3.3.2.2	Min. 8 × 10/100/1000 Ethernet ports and min. 2 × 1000Base-X SFP ports. 1 × SFP transceiver (10 km reach) to be supplied.	DIS-300G-8PSW: 4 × PoE + 2 × BaseT + 2 × SFP = 8 ports total. DIS-300G-14PSW: 10 × BaseT/PoE + 4 × SFP. DIS-300G-12SW: 8 × BaseT + 4 × SFP.	✔  COMPLY	All three models meet the 8-port + 2 × SFP minimum. DIS-S310LX SFP (10 km, -40~85 °C) is a listed accessory; must be specified in BOM.
3.3.2.3	Operating temperature min. -40 °C to +60 °C.	Rated -40 °C to +75 °C.	✔  COMPLY	Exceeds the RFP lower bound of -40 °C and the upper bound of +60 °C.
3.3.2.4	Relative humidity: min. 10 % to 95 % (non-condensing).	Rated 5 % to 95 % RH (non-condensing).	✔  COMPLY	Specification exceeds the RFP humidity range.
3.3.2.5	Fanless cooling; no moving parts.	Fan-less design explicitly stated.	✔  COMPLY	—
3.3.2.6	Minimum IP20 ingress protection.	IP30 certified.	✔  COMPLY	IP30 > IP20; requirement met and exceeded.
3.3.2.7	Critical fault protection alarm relay outputs.	Alarm Relay Output: 0.5 A @ 24 VDC; configurable alarm profile (LED, relay, SNMP trap).	✔  COMPLY	—
3.3.2.8	Min. 1 m fibre optic patch cable per SFP port used shall be delivered.	Not mentioned in datasheet.	?  VERIFY	Patch cables are a procurement / delivery requirement. Confirm with D-Link distributor that cables are included in the supply package.
3.3.2.9	All ports shall operate on a non-blocking basis.	L2 wire-speed / non-blocking switching engine stated.	✔  COMPLY	—
3.3.2.10	Min. 8,000 MAC address table entries.	8K (8,192) MAC addresses.	✔  COMPLY	Meets exactly. Note: Indoor switch RFP requires 16K; this clause requires 8K only.
3.3.2.11	4 priority queues per port.	8 queues per port; scheduling SPQ + WRR.	✔  COMPLY	8 queues exceeds the 4-queue minimum.
3.3.2.12	RMON and SNMP v1, v2, v3; manageable via Telnet, console port, web interface.	SNMP v1/v2c/v3; RMON (RFC 1757 groups 1,2,3,9); Telnet (5 sessions); WEB management; CLI.	✔  COMPLY	Console port (RS-232) availability not explicitly stated in datasheet — confirm with D-Link.
3.3.2.13	ICMP and IGMP Snooping at L2.	IGMP v1/v2 snooping + querying; up to 255 multicast groups. ICMP not itemised.	⚠  PARTIAL	IGMP snooping confirmed. ICMP support is standard in all managed L2 switches but is not explicitly listed in the datasheet. Request formal confirmation from D-Link.
3.3.2.14	IEEE 802.1Q VLAN; MSTP (802.1s) or x-ring equivalent; VLAN tagging / trunking.	802.1Q tag-based VLANs; MSTP (802.1s); STP (802.1D); RSTP (802.1w); Fast Ring Railover < 20 ms.	✔  COMPLY	Ring redundancy (proprietary x-ring equivalent) recovers in < 20 ms. 802.1s MSTP explicitly supported.
3.3.2.15	IEEE 802.1p prioritisation and ToS standard.	IEEE 802.1p QoS; 8 queues per port. ToS / DSCP not listed in DIS-300G datasheet.	⚠  PARTIAL	802.1p confirmed. ToS/DSCP marking is not explicitly documented in this datasheet. Verify via firmware release notes or CLI guide.
3.3.2.16	Port security enforceable on a per-MAC-address basis.	IP and MAC-based access control; IEEE 802.1X authentication.	✔  COMPLY	—
3.3.2.17	IEEE 802.1X port-based network access control.	IEEE 802.1X authentication; RADIUS / TACACS+ AAA.	✔  COMPLY	—
3.3.2.18	Port mirroring.	Per-VLAN mirroring supported.	✔  COMPLY	Per-VLAN mirroring is a superset of standard port mirroring.
3.3.2.19	Each 10/100/1000 port shall support IEEE 802.3af (PoE) and/or 802.3at (PoE+).	DIS-300G-8PSW: 4 × PoE ports (802.3af/at, 120 W budget). DIS-300G-14PSW: 8 × PoE ports (802.3af/at, 240 W budget); ports 1-2 also support 60 W. DIS-300G-12SW: 0 PoE ports.	⚠  PARTIAL	DIS-300G-12SW has NO PoE capability — non-compliant with this clause. DIS-300G-8PSW and DIS-300G-14PSW comply. Model selection must be -8PSW or -14PSW to satisfy this requirement.
3.3.2.20	LACP (IEEE 802.3ad) — aggregate multiple Ethernet ports into a trunk.	IEEE 802.3ad Port Trunk with LACP (static or dynamic).	✔  COMPLY	—
3.3.2.21	IPv6 VLAN interface IP addressing and traffic.	Not explicitly stated in the DIS-300G datasheet.	✘  NON-COMPLY	IPv6 support is NOT documented in the published datasheet. This is a firm gap. Must be formally confirmed with D-Link engineering — if unsupported, the product does not satisfy this clause.
3.3.2.22	Switch and power adapter shall be DIN-rail mountable; delivered pre-connected, complete, in a single enclosure.	DIN-Rail and Wall mounting supported. Compatible DIN-Rail PSUs listed (DIS-H30-24, DIS-H60-24, DIS-N240-48, DIS-N480-48).	⚠  PARTIAL	Physical mounting confirmed. 'Pre-connected in a single enclosure' is a delivery / packaging condition — not verifiable from datasheet alone. Must confirm with D-Link / reseller.
3.3.2.23	Must hold 'C-Type Edge Switch and Traffic Shaping Test Report' issued by EGM BİLTEM with result 'SUCCESSFUL'.	Not referenced in D-Link datasheet.	✘  NON-COMPLY	This is a Turkish government homologation requirement specific to the EGM (Emniyet Genel Müdürlüğü) laboratory. D-Link must present this certificate independently. No publicly available evidence found. CRITICAL — without this certificate the product is ineligible regardless of technical compliance.

SUMMARY
✔  COMPLY	16	Fully documented compliance with RFP clause.
⚠  PARTIAL	4	Technically likely compliant but requires formal written confirmation from D-Link.
✘  NON-COMPLY	2	Not compliant as documented. IPv6 and EGM test certificate are firm disqualifiers.
?  VERIFY	1	Delivery / packaging condition; verify with D-Link or authorised reseller.
```
