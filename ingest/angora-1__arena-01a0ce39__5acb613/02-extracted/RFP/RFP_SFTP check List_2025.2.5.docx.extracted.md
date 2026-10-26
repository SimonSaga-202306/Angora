<!-- ============================================================ -->
<!-- FILE 334/781 -->
<!-- PATH: RFP/RFP_SFTP check List_2025.2.5.docx -->
<!-- SIZE: 25149 bytes -->
<!-- SHA256: a8c5495ee20252b7c71ed971f02a233805db58991ea5baaf8bffe375058eb10b -->
<!-- EXTRACTION: python-docx - body paragraphs + tables + headers/footers + text boxes + notes, document order -->
<!-- ============================================================ -->

[P1|Normal] 基于LT-IS6310G- 2GX8GT的一台样品测试后的反馈以及相应需求
[P2|Normal] 之前谈的SFTP项目和这个样品WEB改动都是为了Turk Telecom(下称TT)这个客户
[P3|Normal] 直接并在一起考虑和处理
[P4|Normal] 
[P5|Normal] 经过我和客户简单确认，基本如下
[P6|Normal] 1, Turk_Telekom_Test_Items这个表格主要分为上下2个部分
[P7|Normal] TEST ITEMS: 这部分是TT经常需要用到的功能
[P8|Normal] TÜRK TELEKOM MSY TEAM QUESTIONS: 这部分是该项目具体的需求
[P9|Normal] What Levent mentioned is the sheet i sent to you. The first part is general requirements from Turk Telekom and the second part is project specific requirements. We ll need to comply with second part mostly. Both parts have many common items, but please focus on the second part starting with power requirements. 
[P10|Normal] 
[P11|Normal] 客户想让我们先针对LT-IS6310G- 2GX8GT型号来审核第二部分
[P12|Normal] 客户没测的是否支持
[P13|Normal] ACL/HTTPS/SFTP/SFLOW
[P14|Normal] 去年谈过的项目，好像是用AC5芯片来做，就直接支持HTTPS，然后SFTP研发一下
[P15|Normal] ACL和SFLOW原本是支持的
[P16|Normal] 一些功能是否能加（尤其是L3相关的功能）
[P17|Normal] Of course i am not asking to comply with every item today, but any quick addition to current version is appreciated. If we can add, RIP, OSPF, HTTPS, SFLOW quickly in a bout a week, that would be great. If not, no worries, we ll tell Turk Telekom that we will support them ultimately. 
[P18|Normal] 之前与Peter沟通，一些功能目前没在做比如NAT
[P19|Normal] 客户的回复基本也比较明确了，能加啥加啥（尤其是基于AC5方案）
[P20|Normal] 客户比较在意NAT和Port Forwarding
[P21|Normal] 上边客户提到了RIP, OSPF这些是三层功能，但L3管理型号中并没有8+2的端口形态
[P22|Normal] 客户问能不能加
[P23|Normal] 或者直接用3层的来改?(8+4改为8+2, 然后光口速率降下来...)
[P24|Normal] 
[P25|Normal] 然后再审核评估第一部分TT常用的一些功能
[P26|Normal] 客户没测的是否支持
[P27|Normal] 一些表格上写的功能但目前并不支持的是否能研发
[P28|Normal] 
[P29|Normal] 整体上就是用8+2形态来符合TT客户常用的功能需求
[P30|Normal] 研发也好，改板子(L3改L2)也好...
[P31|Normal] 
[P32|Normal] 请评估一下功能列表并写明
[P33|Normal] 1, 哪些压根不做（即使有量有很高的研发费用）
[P34|Normal] 2, 哪些能做（请写明研发周期和相关费用等）
[P35|Normal] 3, 列出的一些常用功能是否都支持
[P36|Normal] 
[P37|Normal] 大概就是这样了
[P38|Normal] 这个TT客户很大的一个客户   https://www.turktelekom.com.tr/
[P39|Normal] 我看背景介绍和政府渊源比较深
[P40|Normal] 所以上边的功能请评估一下，如果需要费用或者较长的研发周期也行
[P41|Normal] 因为客户也说了，第一部分是常用的功能，可能也有其他项目来问同样的功能

[SECTION 1 header]
2025/Q1	                                                                                                                       s.sagatelecom@gmail.com
							                                                                       Saga Telecom
								                         www.sagatelecom.com.cn

[SECTION 1 footer]
Connecting, Converting, Creating
