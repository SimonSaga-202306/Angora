# INFO.rar 完整内容清单（2025-12-17 Angora 交付包）

> 来源：`INFO_2025.12.17/INFO.rar`（51.4 MB，RAR **5.0** 格式）
> ⚠️ **沙箱内无法解压**：RAR5 需要 `unrar` 原生二进制，本环境无 root 且 `unrar-cffi` 编译失败。
> **清单已完整读取**（rarfile 可解析 RAR5 目录区），下列内容即该包全部信息。
> 若需提取其中 PPTX，请在本地执行：`unrar x INFO_2025.12.17\INFO.rar`

## 战略意义

> 本包是 **2025-12-17 发给 Angora 的资料包**（对应微信 2026 记录中的 `INFO.rar` / `Please check the info`）。
> 其中 **PeakNetX / VastLakes 是 CENTEC 的芯片平台名**，与 `Reply on SAGA Enterprise L3` 中
> 「Saga 芯片方案已定为 **Marvell L2+ + CENTEC L3**」直接呼应 —— 这是 CENTEC L3 路线的一手物料。

## 内容清单

| 文件 | 大小 | 是否已在仓库单独存在 |
|---|---:|---|
| `User Manual.docx` | 12,445,592 | ✅ 是 |
| `STH1G Series Switches Datasheet_EN.pptx` | 9,009,253 | ✅ 是 |
| `STH-8C48DX/5.png` | 4,978,829 | ✅ 是 |
| `STH25G Series Switches Datasheet_EN.pptx` | 4,891,176 | ✅ 是 |
| `STH-8C48DX/2.png` | 4,509,768 | ✅ 是 |
| `STH-8C48DX/4.png` | 3,968,879 | ✅ 是 |
| `STH-8C48DX/3.png` | 3,833,628 | ✅ 是 |
| `Web Manual.docx` | 3,351,215 | ✅ 是 |
| `CLI Manual.docx` | 2,704,581 | ✅ 是 |
| `STH-8C48DX/1.png` | 2,268,398 | ✅ 是 |
| `CENTEC web gui.jpg` | 548,089 | ✅ 是 |
| `Saga Software Function List_EN.pptx` | 154,139 | ✅ 是 |
| `ANW-DC-RFP-EN.pdf` | 114,015 | ✅ 是 |
| `Performance of VastLakes Platform_EN.pptx` | 105,121 | ✅ 是 |
| `Performance of PeakNetX Platform_EN.pptx` | 97,089 | ✅ 是 |

## ⚠️ 仅存在于 rar 内、仓库其他地方没有的文件（需本地解压后补充）

## r98 修正并取代本文件的对应说法（保留历史正文）

- 对话 `INFO.rar` / `Please check the info` 的日期是 **2025-12-17**，不是上文误写的“2026 微信”。
- 本文件所列为 RAR 目录，不是载荷全部信息；软件清单成员目录记 **154,139 bytes**，同名散件旧索引为 **154,107 bytes**。两者不能当同版本；其他同名同大小项也未做成员载荷对比，不能声称逐字节相同。
- 当年成员清单中的 `sha256` 源自同名散件而非 RAR 成员内容；可参见 `tools/extract_archives.py` 的 `handle_rar_listing`。[来源说明](../../../../18-source-evidence-r98-2026-10-26/README.md)。
- 用户已对 **INFO.rar 解压 PASS**，上文“若需提取执行 unrar”的旧建议失效，不执行、不建议客户执行。

本附录显式改变了这个工作档文件；原先字节可由 Git `98006ef` 读取，不把附录后的文件冒称源仓 byte-identical 产物。
