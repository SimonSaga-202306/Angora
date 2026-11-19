# Angora 档案附录 r112：历史接入认证与支持记录

> 仅增补 Angora 本体的公开历史资料；不创建或合并客户，不联系主体，不把厂商自述、仓库样例或动态页面升级为真实部署、验收或认证。主体仍按 r111 标注 **未确认**。

## 1. 802.1X 与公开示例

- [AR01 2022 归档](../../../73-source-evidence-r112-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/802-1x-port-based-authentication-using-freeradius/20220118064213/index.visible.md#L39-L53) 的厂商文档称 Verge 5.0 及以上支持 802.1X，举 PEAP、EAP-TLS、EAP-GTC 等。它的基础示例使用 PEAP／本地用户，目录服务集成不在示例范围；不是实测或当前所有型号的承诺。
- **增补 r110 认证资料**：r110 TACACS 是设备管理认证，英文历史文档写大于 4.0；本轮 802.1X 是终端接入，两种功能和版本门槛不能混同，也不取代 r110 英／土文差异。
- 文档链接的 [7 份公共 FreeRADIUS 样例](../../../73-source-evidence-r112-2026-10-26/github-files-read-inventory.csv)已按原路径逐文件保存，91,709 bytes，Git blob 与大小核对一致；`eap` 样例中外层 PEAP、PEAP 段内 MSCHAPv2，样例日志含 Access-Accept。**样例不等于本轮设备实测、客户验收、安全认证或生产配置**；不在报告中摘录或使用公开样例账号／密钥；原文件按公开原字节保存。
- **增补并修正可能的 r110 GH03 零结果误读**：r110 保存的支持域名 GitHub 搜索结果为零，且当时已提示零不代表不存在；本轮由归档正文直接找到公开 README，里面有该域名。不是说 r110 当时响应错误，也不能倒推搜索索引原因。[原查询和响应](../../../73-source-evidence-r112-2026-10-26/prior-gh-read-inventory.csv)。

## 2. 2021 问题记录及版本边界

| 历史厂商页面 | 原文范围与状态 | 本轮限制 |
|---|---|---|
| [SSH 卡顿](../../../73-source-evidence-r112-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/ssh-baglantilarinda-donma/20210227205239/index.visible.md#L38-L46) | `5.5.1.x`／`5.5.3.x`；识别问题、等待解决；计划 `5.5.1.17`／`5.5.3.10`。 | 仅 2021 快照，未证明版本已发布或今日仍受影响。 |
| [SCP 传输错误](../../../73-source-evidence-r112-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/scp-kullaniminda-hata-olusmasi/20210227215720/index.visible.md#L38-L46) | 同版本族与计划；厂商称特定向远端发送文件操作可能导致错误重启。 | 未复现，不证明客户实际中断或当前未修复。 |
| [蓝色工作灯](../../../73-source-evidence-r112-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/guc-isiginin-yanmamasi/20210227223458/index.visible.md#L39-L47) | `5.5.1.13` 及以前；状态写已解决，另有“计划修复版本”字段。 | 两字段照录，未独立核实发布／修复，不断言供电硬件故障。 |

**限定 r110 升级示例**：r110 2025 捕获页面中的镜像文件名只是示例；不可将它当实际设备版本，再据上面的计划号判定已修复或未修复。原文中的 TFTP 建议仅记为历史厂商建议，不转成现场操作建议。

## 3. 其他增量及具名限制

- 本轮厂商 Packet Broker 文章是一般架构与营销说明，不能把通用场景数字、零损耗或回本话术当成具体型号的实测与承诺。旧 r104 P01 因混有已停端口相关字段及数据表链接，虽为网页文本仍在本轮排除出结论；未打开 PDF 或追问。
- **增补 r109 E03**：培训分类索引本轮可见两个动态摘要；r111 两个活动原页仍分别保留，不证明实办或人员数量。**限定 r109 V01／旧 `50`**：视频本轮发生分块漂移，局部隔离，不得升级为已核实流程。[失败记录](../../../73-source-evidence-r112-2026-10-26/fetch-failures/X02.visible.md)。
- 旧页范围过宽、视频不完整、手抄修正及先读后汇总等均已在[偏差记录](../../../73-source-evidence-r112-2026-10-26/scope-and-sequence-deviations.md)披露；没有重新开启旧单、财务差异、RFQ/RFP、报价、官网 PDF 或其他 PASS 项。

**全量读取完成（限定清单）：58/58 路径、355,715 bytes**；含 API／索引、失败、隔离块及同源重复分块，不是 58 个独立源。[完整路径、大小、哈希和方法](../../../73-source-evidence-r112-2026-10-26/README.md) · [43 条证据锚](../../../73-source-evidence-r112-2026-10-26/evidence-traceability.csv)。
