[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")

[4 captures](https://web.archive.org/web/*/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge "See a list of every capture for this URL")

30 Jun 2022 - 11 Feb 2025

|     |     |     |
| --- | --- | --- |
| [Jun](https://web.archive.org/web/20240623105359/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge "10:53:59 Jun 23, 2024") | FEB | Mar |
| [10:53:59 Jun 23, 2024](https://web.archive.org/web/20240623105359/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge "10:53:59 Jun 23, 2024") | 11 |  |
| [2023](https://web.archive.org/web/20231210132643/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge "13:26:43 Dec 10, 2023") | 2025 | 2026 |

success

fail
[Share via My Web Archive](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge# "Share via My Web Archive") [Sign In](https://archive.org/account/login.php "Sign In")[Get some help using the Wayback Machine](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine")[Close the toolbar](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge#close "Close the toolbar")

[screenshot](https://web.archive.org/web/20250211051945/http://web.archive.org/screenshot/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge "screenshot")[video](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge# "video")[Share on Facebook](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge# "Share on Facebook")[Share on Twitter](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge# "Share on Twitter")

[About this capture](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge#expand)

TIMESTAMPS

![loading](https://web-static.archive.org/_static/images/loading.gif)

The Wayback Machine - https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht\_kb=software-upgrade-tftp-verge

# Knowledge Base

Search ForSearch

1. [Home](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/ "Home")
2. [Knowledge Base](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?post_type=ht_kb "Knowledge Base")
3. [How To Guides](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb_category=how-to-guides "View all posts in How To Guides")
4. [Software Upgrade (TFTP/USB) – Verge Switches](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge "Software Upgrade (TFTP/USB) – Verge Switches")

This article describes, upgrade procedure of Angora Networks edge switches via TFTP protocol or by using USB file transfer.

AngoraOS operating system used to operate Angora Networks edge switches, provide robust, innovative and easy to use management capabilities for enterprise networks. On going developments and improvements are implemented into the operating system software to make sure hundreds of features works seamlessly and to add new requests to enhance the functionalities.

Software upgrades with latest image are needed to use all updated functions.

## **Prepare to upgrade**

If you prefer upgrading the software via TFTP protocol, you must install required applications to get ready connecting to your switches. Required steps are listed below:

1. TFTP (Trivial Transfer File Protocol) application: A TFTP server application (Example: TFTPD64) must be configured for network access.
2. AngoraOS software image file, must be placed inside TFTP server root directory.
3. In case of a failure, such as network loss, console connection is required for timely access and user intervention. (All software update procedure can run remotely. To keep CLI accessible against failures, update using console connection is recommended)
4. Switch and TFTP server must be reachable to each other via network connection. (Most secure way of upgrade is to directly connect a PC to one of switch ports to prevent network loss and delays)

Below is a sample connection diagram to be used for upgrade via locally connected PC.

![](https://web.archive.org/web/20250211051945im_/https://support.angoranetworks.com/wp-content/uploads/2022/02/image-6.png)

Figure 1 – Upgrade via local PC connection

* * *

To proceed with USB upgrade, make sure the USB disk to be used, is either FAT32 or ExFAT formatted.

## **Upgrade steps**

Before starting upgrade, do not forget to take note of current active and passive images. Use the following command to show this information:

_`#show version`_

The command will be as follows:

![](https://web.archive.org/web/20250211051945im_/https://support.angoranetworks.com/wp-content/uploads/2020/09/image-1.png)

Figure 2 – Active and passive software versions

* * *

This output shows two software image as “Active-image” and “Inactive-image” . Active-image is the software image currently running on the device. Inactive-image can be used if needed with a single command.

Once TFTP server is accessible, below command starts file transfer and software upgrade:

- `TFTP server address: 192.168.1.11`
- `Software image file to be uploaded: image_5.5.3.03.bin`

_`boot system tftp://192.168.1.11/image_5.5.3.03.bin`_

![](https://web.archive.org/web/20250211051945im_/https://support.angoranetworks.com/wp-content/uploads/2020/09/image-2.png)

Figure 3 – Software upgrade via TFTP

* * *

If you prefer installing the image via USB disk, plug the USB into the port located on the front panel of the device.

Wait around 8-10 seconds for the USB disk to be recognized. If the USB disk is not ready within 15 seconds, this indicates a formatting problem. In this case, please try re-formatting the disk.

Below command is used to start USB file load and installation:

_`boot system usb://image_5.5.3.03.bin`_

Installed software will be listed as “Inactive-image” and defined as the new software version for the next reboot.

![](https://web.archive.org/web/20250211051945im_/https://support.angoranetworks.com/wp-content/uploads/2020/09/image-3.png)

Figure 4 – Software status after installation

* * *

Above output confirms that the software upgrade is done and installed image is ready to be used after the next reboot.

You should save your configuration to keep all updated informations in the running configuration to be permanent after reboot. `“write memory”` command should be used to save the current config as the startup configuration.

New software can be used after the first reboot. To restart the device, please use the following command:

_`#reload`_

![](https://web.archive.org/web/20250211051945im_/https://support.angoranetworks.com/wp-content/uploads/2020/09/image-4.png)

_Figure 5 – Device reboot_

* * *

After device reboots, running _`"show version"`_ command, will output the Active-image with new installed software version.

![](https://web.archive.org/web/20250211051945im_/https://support.angoranetworks.com/wp-content/uploads/2020/09/image-5.png)

Figure 6 – End of the upgrade

### Was this article helpful?

[Yes](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge#) [No](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge#)

### Related Articles

- [Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)")  - 3
  - 1236
- [Sistem Bilgilerini Öğrenme](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "Sistem Bilgilerini Öğrenme")  - 1
  - 842
- [Link Katmanı Keşif Protokolü (LLDP)](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "Link Katmanı Keşif Protokolü (LLDP)")  - 0
  - 1207
- [Komut Satırı kullanımı](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "Komut Satırı kullanımı")  - 0
  - 1601
- [Hızlı Başlangıç Kılavuzu](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=hizli-baslangic-kilavuzu "Hızlı Başlangıç Kılavuzu")  - 1
  - 927
- [Yazılım Güncelleme (TFTP/USB) – Verge Anahtarlar](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar "Yazılım Güncelleme (TFTP/USB) – Verge Anahtarlar")  - 3
  - 981

### Leave A Comment? [Cancel Reply](https://web.archive.org/web/20250211051945/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge\#respond)

Save my name, email, and website in this browser for the next time I comment.