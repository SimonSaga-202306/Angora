# RFP_SFTP check List_2025.2.5.docx

> 来源：`RFP/RFP_SFTP check List_2025.2.5.docx`　·　字符数：1,459

---

基于LT-IS6310G- 2GX8GT的一台样品测试后的反馈以及相应需求
之前谈的SFTP项目和这个样品WEB改动都是为了Turk Telecom(下称TT)这个客户
直接并在一起考虑和处理
经过我和客户简单确认，基本如下
1, Turk_Telekom_Test_Items这个表格主要分为上下2个部分
TEST ITEMS: 这部分是TT经常需要用到的功能
TÜRK TELEKOM MSY TEAM QUESTIONS: 这部分是该项目具体的需求
What Levent mentioned is the sheet i sent to you. The first part is general requirements from Turk Telekom and the second part is project specific requirements. We ll need to comply with second part mostly. Both parts have many common items, but please focus on the second part starting with power requirements.
客户想让我们先针对LT-IS6310G- 2GX8GT型号来审核第二部分
客户没测的是否支持
ACL/HTTPS/SFTP/SFLOW
去年谈过的项目，好像是用AC5芯片来做，就直接支持HTTPS，然后SFTP研发一下
ACL和SFLOW原本是支持的
一些功能是否能加（尤其是L3相关的功能）
Of course i am not asking to comply with every item today, but any quick addition to current version is appreciated. If we can add, RIP, OSPF, HTTPS, SFLOW quickly in a bout a week, that would be great. If not, no worries, we ll tell Turk Telekom that we will support them ultimately.
之前与Peter沟通，一些功能目前没在做比如NAT
客户的回复基本也比较明确了，能加啥加啥（尤其是基于AC5方案）
客户比较在意NAT和Port Forwarding
上边客户提到了RIP, OSPF这些是三层功能，但L3管理型号中并没有8+2的端口形态
客户问能不能加
或者直接用3层的来改?(8+4改为8+2, 然后光口速率降下来...)
然后再审核评估第一部分TT常用的一些功能
客户没测的是否支持
一些表格上写的功能但目前并不支持的是否能研发
整体上就是用8+2形态来符合TT客户常用的功能需求
研发也好，改板子(L3改L2)也好...
请评估一下功能列表并写明
1, 哪些压根不做（即使有量有很高的研发费用）
2, 哪些能做（请写明研发周期和相关费用等）
3, 列出的一些常用功能是否都支持
大概就是这样了
这个TT客户很大的一个客户   https://www.turktelekom.com.tr/
我看背景介绍和政府渊源比较深
所以上边的功能请评估一下，如果需要费用或者较长的研发周期也行
因为客户也说了，第一部分是常用的功能，可能也有其他项目来问同样的功能