# 固件容器全解 — lite-hotfix-7.3.13.bin

- 源文件：`3rd order 176台2光16电 L2 PoE/lite-hotfix-7.3.13.bin`（62,289,840 bytes）
- sha256：`7fe48e24a87cdd731f9f238f3607ae9b1d41cb46b20ba8b64fa6feb52e5a70d4`
- 源 commit：`5acb6132a6a6090bfc777c324cfea6bc8dfb877a`

## 容器链（逐层解开，非猜测）

| 层 | 魔数 | 判定 | 解开后 |
|---|---|---|---|
| 1 | `fd377a585a00` | XZ 流 | tar，98,078,720 bytes |
| 2 | `ustar` | POSIX tar | 3 个成员 |
| 3 | — | tar 成员 `rootfs.xz` | 97,124,352 bytes, mode 0o644 |
| 3 | — | tar 成员 `upgrade.cfg` | 859 bytes, mode 0o755 |
| 3 | — | tar 成员 `uboot.bin` | 945,600 bytes, mode 0o644 |
| 4 | `UBI#` | UBI 镜像（NAND 磨损层） | UBIFS 卷 `rootfs` |
| 5 | `0x2f4cc1e3` superblock | UBIFS 文件系统 | 见 rootfs-FILELIST.tsv |

## upgrade.cfg 声明的 md5 与实际计算值（完整性自证）

| 对象 | upgrade.cfg 声明 | 实际计算 | 结果 |
|---|---|---|---|
| rootfs.xz | `a0a6d06a59697a59da79cddc8f343d35` | `a0a6d06a59697a59da79cddc8f343d35` | 一致 ✔ |
| uboot.bin | `8abb4e02b809adaec4b77e387d928932` | `8abb4e02b809adaec4b77e387d928932` | 一致 ✔ |
| rootfs 尺寸 | 97124352 | 97124352 | 一致 ✔ |

## UBI 几何（ubireader_display_info 原文）

```
UBI File
---------------------
	Min I/O: 2048
	LEB Size: 126976
	PEB Size: 131072
	Total Block Count: 741
	Data Block Count: 739
	Layout Block Count: 2
	Internal Volume Block Count: 0
	Unknown Block Count: 0
	First UBI PEB Number: 0

	Image: 1443069730
	---------------------
		Image Sequence Num: 1443069730
		Volume Name:rootfs
		PEB Range: 2 - 740

		Volume: rootfs
		---------------------
			Vol ID: 1
			Name: rootfs
			Block Count: 739

			Volume Record
			---------------------
				alignment: 1
				crc: '0xa7c5ccd0'
				data_pad: 0
				errors: ''
				flags: 0
				name: 'rootfs'
				name_len: 6
				padding: '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
				rec_index: 1
				reserved_pebs: 1688
				upd_marker: 0
				vol_type: 'dynamic'
```

## UBIFS 内容规模

- 条目总数：9,655（文件 6,999 + 目录/链接）
- 文本文件：4,881 个 / 39,164,587 bytes → `rootfs-text/` 逐字节副本
- 非文本文件：2,118 个 / 118,280,374 bytes → sha256 见 `rootfs-binary-index.tsv`

## 版本指纹（固件内自带）

- `version.txt`:

```
hotfix/7.3.13 (r1431 25e364a)
2026-05-22 19:46:52
```

- `www/version.txt`:

```
dkweb: 7.3.9 (r760 b910fcb4) 2025-10-11 10:56:33 +0800, build time 2025年10月11日 11:39:08
```

- `etc/debian_version`:

```
7.9
```


## upgrade.cfg 全文

```ini
name = "upgrade";

version = "";

configure =
{ 
  serials = ( { title  = "MAC3L"; },
              { title  = "MAC3LS"; },
              { title  = "MAC3LC"; },
              { title  = "MAC3LCS"; },
              { title  = "SMB"; },
              { title  = "MPC3"; }, 
              { title  = "LTIE"; },   
              { title  = "JK"; }
	);

  mtd =   ( { title = "rootfs0";  mtdid = 0; device = "/dev/mtdblock0"; },
            { title = "rootfs1";  mtdid = 1; device = "/dev/mtdblock1"; }
          );
           
  firewall = "rootfs.xz";
  
  md5 = "a0a6d06a59697a59da79cddc8f343d35";
  
  size = 97124352;
  
  uboot_version = "";
  uboot_image = "uboot.bin";
  uboot_upgrade_flag = 0;
  
  uboot_mtd_id =  4;
  uboot_mtd_offset = 0;
  uboot_mtd_blks = 256;
          
  uboot_md5 = "8abb4e02b809adaec4b77e387d928932";
  uboot_size = 945600;
};
```
