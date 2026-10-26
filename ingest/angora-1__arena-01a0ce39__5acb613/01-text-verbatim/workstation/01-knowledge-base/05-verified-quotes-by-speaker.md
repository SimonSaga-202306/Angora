# 可引用原话台账 · 逐行归属已验证

> **方法**：25 张微信长截图 → 保留行坐标的 OCR → 按**气泡贴边**判定说话人
> （`left_gap ≤ 左贴边阈值` → **Levent**；`right_gap ≤ 右贴边阈值` → **Simon/我方**；
> 再以称呼证据 "Hi Simon" / "Hi Levent" 覆盖）。
> **交叉验证：413 条含明确称呼的轮次，100% 与几何判定一致，零冲突。**
> 语料：`workstation/01-knowledge-base/wechat-conversation-aligned.{md,json}`（2,601 轮，2024-05-02 → 2026-10-03）
>
> ⚠️ **引用任何原话前，一律以本文件为准。** 旧版 `wechat-conversation.md` 按"一个时间戳 = 一个说话人"切块，
> 已证实会把我方的话误归到 Levent 名下（见 §A 案例）。

---

## A. 已发生的归属错误（引以为戒）

| 原话 | 旧版误归 | ✅ 实际说话人 | 判定依据 |
|---|---|---|---|
| *"Security projects.. Dahua is just too strong"* | Levent | **Simon（我方 / 用户本人）** | 行中心 xc=1261（右栏）；同块相邻 Levent 行 xc=214/234/351/436 |
| *"I understand Dahua got it"* | Simon | **Levent** | xc=214（左栏） |
| *"Dahua won it?"* | （未标） | **Simon** | xc=1381（右栏） |
| *"Truth is, we do not stand a good chance to win though I hate to say this.."* | （易误为 Levent） | **Simon（我方）** | 贴右边缘 |
| *"Marvell model is a little over-standard for this project / So the price is not competitive"* | （易误为 Levent） | **Simon（我方）** | 贴右边缘 |
| *"Our strategy is to focus on limited valuable clients. You are one of them"* | （易误为 Levent） | **Simon（我方）** | 贴右边缘 |

---

## B. Levent KILIÇ（Angora）· 可引用原话

### B1. 关系与战略定位
- **2026-04-25 18:21** — *"Hi Simon, thank you. **We are proceeding with Saga products. You are our strategic partner.**"*
- **2026-04-25 18:21** — *"Our partners are also not sure whether to participate in. They have some cold feet."*
- **2026-04-25 18:21** — *"**The whole tender is not commercially viable. It is just for marketing.** Even with that, no one is sure to participate."*
- **2026-04-25 18:21** — *"**We try to associate our brand with quality. So we are happy to go with Marvell.**"*
- **2026-04-25 18:21** — *"If customer wants cheap then we can also give them products. But not our first choice."*
- **2026-04-25 18:21** — *"Sure. With commercial we are okay. The quantity is very small too."*
- **2026-04-25 19:11** — *"No worries, Simon. Thank you for all your support."*
- **2026-05-20 14:09** — *"Hi Simon, thank you for your support as always."*
- **2026-05-20 15:10** — *"thanks for this Simon... Appreciate that. And I promise we will make best efforts."*
- **2026-05-20 14:36** — *"Right. I got you.. That's great.. I think I should bring some orders to you... would be fair. So I am just pushing to close some orders asap."*
- **2026-05-20 00:34** — *"**I want to make a name in the market.** Let's see how this one will end up."*

### B2. 投标机制与竞争（安卡拉警方项目）
- **2026-04-16 14:09** — *"**Pricing part is open auction. electronic open auction in 5 rounds total. End of 5th round, best price wins.** Then paperwork check, if all okay then sample testing."*
- **2026-04-16 14:15** — *"All paperwork is uploaded BEFORE the tender. They are all checked."* / *"Technical compliance is a given ;-)"*
- **2026-04-16 14:21** — *"**not in this tender... other projects yes.. This one is a price war...** Of course AFTER the win, relations are important at Final Acceptance Tests."*
- **2026-04-16 14:53** — *"**We will need to say okay to minimum profit and maximum business in switches.**"* / *"we also need to increase volume and minimize profit."*
- **2026-04-16 14:58** — *"yes. The technician should be able to install the switch in the DIN rail when he opens the box."*
- **2026-04-16 12:28** — *"There is a camera part of the tender. So they want (Dahua) on the switch side to get better pricing on the camera side."*
- **2026-04-16 12:28** — *"One partner is dancing with DLink. So they will be opportunistic on the price."*
- **2026-04-16 12:28** — *"Last partner is loyal to us. They are the ones that got 200 switches last year... did not make any money last year. So this year they want to make some margin."*
- **2026-04-16 12:33** — *"My strategy is NOT to lose money as Angora, but to get the tender. This is for reputation."*
- **2026-04-16 12:35** — *"I asked 25 Yuan for 1G-LX SFP from Karen for this deal. Just so you know."*
- **2026-04-16 15:12** — *"In other projects it even more relations.. Even price is not enough sometimes."*
- **2026-04-28 19:40** — *"Yes today the partners have initial proposal for tender. **Waiting for a date for e-auction for open price war.** I'm not sure even if they proposed us."*
- **2026-04-28 19:40** — *"I have a very aggressive pricing to encourage them choose us. But we will see."*
- **2026-04-28 19:40** — *"As for technology part, **yes Taylan is the guy**. I will ask him to share his opinion with you as soon as possible."*
- **2026-05-22 18:51** — *"Hi Simon, **our partner ended up 3rd on the tender** with a small difference with the second."*
- **2026-05-22 21:39** — *"No not a small difference. It was again a physical security project with cameras."* / *"Yes with cameras and switches."* / *"Our partner went with our switches and Hikvision cameras."*

### B3. D-Link 竞品情报
- **2026-03-06 16:33** — *"Hi Simon here is the DLink model from last year / DIS-300G-10PS"*
- **2026-04-22 11:25** — *"I found out DLink offer to the partner yesterday... 1- the box includes switch + power supply + SFP + fiber cable and a short po[wer]... 2- 30% down payment at order and 70% when the goods arrive at the Customs... 3- unit price is $135. This is the price to the partner."*
- **2026-03-16 14:57** — *"Hi Simon, here is the output from Taylan. **It seems the chipset is Vitesse.**"*

### B4. 技术诉求
- **2026-01-20 23:18** — *"Just a quick question about the industrial switches / **Do we have IEC61850 certificate?**"*（⚠️ 至今未答复）
- **2026-04-16 14:53** — *"One last thing before I forget, pls do include the **DIN rail Apparatus** in the 8-port industrial switch."*

---

## C. Simon（我方）· 可引用原话

### C1. 战略与客户定位
- **2026-05-20 14:44** — *"**Our strategy is to focus on limited valuable clients. You are one of them.** We are trying to find out ways to close more orders and enhance the presence."*
- **2026-05-20 14:44** — *"Ways: it could be prices, services and technical support etc."*
- **2026-05-20 14:44** — *"Our strategy... not like that"（回应 Levent 的"该给你带单了"）*
- **2026-05-20 14:29** — *"1. what I meant is a **long-term price support**."*
- **2026-05-20 14:51** — *"long-term means anytime that price could helps or you need a discount etc."*
- **2026-05-20 14:51** — *"**As I explained before, we are switching from Marvell AC3 to AC5 for full managed... this is almost done.**"*
- **2026-05-20 14:51** — *"We are also working hard to develop some new software features. So its like, we put in decent efforts to build our Marvell Eco."*
- **2026-05-20 14:51** — *"**we would like to loop in some very good clients like Angora to move forward... its more than orders.**"*
- **2026-05-20 14:4x** — *"if price could be a big help in this or future orders, lets do it / as long as it helps / **or we will be stuck here / efforts made, but no good outcome**"*

### C2. 价格与成本
- **2026-04-16 11:51** — *"**825 YUAN is a big pressure, let's do 830 YUAN/PC.** Hope this helps."*
- **2026-04-16 12:46** — *"Same here, we will provide any more possible discount / **for now its 830 YUAN/PC and 20K for FOB shipment.** probably less on shipment cost."*
- **2026-04-16 12:46** — *"**for product cost, 830YUAN is the limit**... we will see if we can do better on shipment."*
- **2026-04-16 14:30** — *"For prices, we will give our best offer(I mean not just about this tender) including after ones."*
- **2026-04-16 14:30** — *"well, the point is Saga can only handle the front parts, product cost and sh[ipping]... So we will do our best as long as it takes."*
- **2026-04-16 15:12** — *"our plan is a little different, its **standard items and customized items**."*
- **2026-04-16 15:12** — *"for standard items, like your plan, as long as there is any profit, lets go for it / **but our focus is on customized ones that will give us decent profit and long-term biz relationship**."*
- **2026-04-16 15:12** — *"its kinda like discover and foster some specific needs like **dual AC input, D[IN]**."*
- **2026-04-22 11:38** — *"1. I guess they are still using Vitesse chip? / If we only talk about features itself..."*

### C3. 对 Marvell / 产品竞争力的**自我诚实评估**（内部参考，勿外发）
- **2026-04-25 18:21** — *"And sorry for this, as I explained, **Marvell model is a little over-standard for this project. So the price is not competitive**..."*
- **2026-04-25 18:21** — *"maybe just commercial model? it should be competitive."*
- **2026-04-25 18:21** — *"I get it / but for now, **industrial switch(Marvell model) is far from being competitive** / This CCTV project is not requiring very high specs. / **Marvell is over standard now** / **Truth is, we do not stand a good chance to win though I hate to say this..**"*
- **2026-04-25 18:26** — *"commercial model should be competitive / yes I know the quantity / its up to your marketing purpose etc."*
- **2026-04-28 17:45** — *"**I am learning Marvell AC5/AC5+ features with the help of AI. As I introduced before, we are transitioning from AC3 to AC5. This is a big leap!**"*
- **2026-04-28 17:45** — *"For now, AC5/AC5+ is the best option considering both cost and performance. **We will stick to it for a very very long time!**"*
- **2026-04-28 17:45** — *"For a long while, it is you talking about projects with Saga. **Any technical feedback from Taylan?** He deals with technical issues, right? This is also important. Helps us understand our market positioning!"*

### C4. 对土耳其安防市场的判断
- **2026-05-22 21:39** — *"**Security projects.. Dahua is just too strong.**"* ⭐（我方定性，非 Angora）
- **2026-04-16 14:24** — *"price war... kinda same here / prices and relations."*

---

## D. 人事线索（新增）

| 人物 | 身份 | 依据 |
|---|---|---|
| **Peter** | **Simon 的直属上级**（Saga 内部）；亦出现在此前的售后支持群 | 2026-05-20 14:29 **Simon**：*"on Monday evening, **my supervisor Peter**(the guy is also in the previous after-sales support group) talked with me about Turkey market"* |
| **Taylan** | Angora 技术负责人 | 2026-04-28 Levent：*"As for technology part, yes Taylan is the guy"*；2026-03-16 Levent 转来 Taylan 的 `sh ver` 输出 |
| **Karen LEE** | NEM Engine（伙伴）；1G-LX SFP ¥25 | 2026-04-16 Levent：*"I asked 25 Yuan for 1G-LX SFP from Karen for this deal."* |

⚠️ **Peter 的身份需谨慎**：此处原文为 "my supervisor Peter"，即 **Simon 的上级**，
与先前档案中"SmartByte 的 Peter"是否同一人待核 —— 若非同一人，则我方内部存在两位 Peter。

---

## E. 投标机制要点（安卡拉警方项目，Levent 原话）

1. **电子竞价公开拍卖，共 5 轮**；第 5 轮结束**最低价者中标**。
2. 所有资质文件在投标**前**上传并审核完毕（含日期、金额、签章）。
3. 竞价结束后才是文件复核 → **样品测试** → 合同签署。
4. 技术符合性是**既定前提**（"Technical compliance is a given"）—— 即**技术达标只是入场券，胜负在价格**。
5. **此标纯价格战**，关系不起作用；但中标**后**的关系在最终验收、样品、交货签收（质保起算）环节很重要。
6. Levent 原话：*"not in this tender... other projects yes.. This one is a price war."*

---

## F. 2026-10-06 补录（第 13 轮 · 877 图 = 第 26 张截图）

| 说话人 | 原文 | 时间 | 归属依据 |
|---|---|---|---|
| **Levent** | *"Hi Simon, I think the price has increased quite a bit. Do you have the same price we discussed last time?"* | 2026-10-02 | xc=106.5（左贴边）+ "Hi Simon" 称呼证据 |
| **Levent** | *"We expect an order for 88 pieces of L2+ industrial 8-port together with 48V power supply."* | 2026-10-02 19:56 | xc=477.8（左）+ 同轮 "Hi Simon" |
| **Levent** | *"Can you please share a pricing for this in the same box"* | 2026-10-02 | xc=207.0（左） |
| **Levent** | *"Thanks Simon. Great."* | 2026-10-03 00:40 | xc=188.5（左）+ "Thanks Simon" |
| **Simon** | *"Hi Levent" / *"sure, same as last time, right?" / *"let me get it tor u"* | 2026-10-03 00:19 | xc=1132.9（右贴边）+ "Hi Levent" |
| **Simon** | *"STI-288DGGPM" / *"875RMB/PC"* / *"Power supply 240W meanwell original brand" / *"250RMB/PC"* | 2026-10-03 00:19 | 右栏 |
| **Simon** | *"for the switch itself, we keep the price low, basically the same as last order" / *"we will handle the material costs here.."* | 2026-10-03 00:19 | 右栏 |
| **Simon** | *"Thanks for your cooperation" / *"same packing box, right?" / *"Send"* | 2026-10-03 00:22~00:40 | 右栏 |

> **业务背景**：88 台 STI-288DGGPM（L2+ 工业 8 口）+ 240W 全汉原厂 48V 电源的报价 = 875+250 RMB/套；
> **截至 2026-10-06 未落单**。末次落单 = 2025-06-19（6 台）→ 15.4 个月零订单（用户"15+ 个月"陈述经仓库 STSC 订单时间戳验证）。
