[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")

[5 captures](https://web.archive.org/web/20240530151345*/https://support.angoranetworks.com/?ht_kb=tacacs-authentication-with-cisco-ise "See a list of every capture for this URL")

27 Feb 2021 - 30 May 2024

|     |     |     |
| --- | --- | --- |
| Apr | MAY | Jun |
|  | 30 |  |
| 2023 | 2024 | 2025 |

success

fail
[Share via My Web Archive](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=tacacs-authentication-with-cisco-ise# "Share via My Web Archive") [Sign In](https://archive.org/account/login.php "Sign In")[Get some help using the Wayback Machine](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine")[Close the toolbar](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=tacacs-authentication-with-cisco-ise#close "Close the toolbar")

[screenshot](https://web.archive.org/web/20240530151345/http://web.archive.org/screenshot/https://support.angoranetworks.com/?ht_kb=tacacs-authentication-with-cisco-ise "screenshot")[video](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=tacacs-authentication-with-cisco-ise# "video")[Share on Facebook](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=tacacs-authentication-with-cisco-ise# "Share on Facebook")[Share on Twitter](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=tacacs-authentication-with-cisco-ise# "Share on Twitter")

[About this capture](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=tacacs-authentication-with-cisco-ise#expand)

TIMESTAMPS

![loading](https://web-static.archive.org/_static/images/loading.gif)

The Wayback Machine - https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht\_kb=tacacs-authentication-with-cisco-ise

Tacacs+ Authentication (with Cisco ISE) – Angora Networks Support

# Knowledge Base

Search ForSearch

1. [Home](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/ "Home")
2. [Knowledge Base](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?post_type=ht_kb "Knowledge Base")
3. [How To Guides](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb_category=how-to-guides "View all posts in How To Guides")
4. [Tacacs+ Authentication (with Cisco ISE)](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=tacacs-authentication-with-cisco-ise "Tacacs+ Authentication (with Cisco ISE)")

## Overview

Tacacs+ is an authentication protocol used to validate users to access and manage network devices. It is widely used as part of network security applications. For more information about Tacacs protocol, we let the owner of the protocol to explain in [detail on this link](https://web.archive.org/web/20240530151345/https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_usr_tacacs/configuration/15-s/sec-usr-tacacs-15-s-book/sec-cfg-tacacs.html).

This document describes required action on both Verge switches and Cisco ISE. This is a tested configuration for basic usage. The configuration on ISE side can be improved, but this is out of our scope here.

## Configuration

### Verge Configuration

All Angora edge switches running version greater than 4.0, support TACACS+ . The exact same configuration provided below is applicable to all models and software versions (including stacked device groups)

To configure TACACS+ authentication, you basically need to define TACACS+ server (which in this document case, is a Cisco ISE) and tell the device to go and check the user validity with this server. You can configure more than one server and prioritize them to send the requests. Here, we are using only a single server for quick and easy setup. All timeouts are left at default values. You can check TACACS+ commands and all default values from the TACACS+ command line documentation, [located on this link](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=security-tacacs).

> `(config)#aaa authentication login authorization default tacacs local`

```
This command informs the switch to use tacacs server first, for user authentication. If tacacs server is unreachable (not when tacacs is rejecting the user information), only then, the local users can be used to access the device
```

> `(config)#aaa authentication enable authorization default tacacs`

```
This command is used to allow user to change their privilege level by entering "enable" command. If you will not add this line, any user that knows the local enable password can change their privilege level to 15
```

> `(config)#tacacs-server host 192.168.1.15 key angora`

```
You need to add the same key (here it is set to angora) on both switch and tacacs server side
```

> `(config)#tacacs-server host source-interface vlan 1`

```
Optionally you can specify which interface address to be used, to send tacacs requests. It is a good idea to set this address, as you must enter this address as network device address on tacacs server side.
```

This is all the configuration items you need on Verge Switches side. Now lets configure Cisco ISE.

### Cisco Identity Services Engine (ISE) Configuration

Cisco ISE is used to securely accessing to network resources for users and devices. It is basically a radius server, providing 802.1x services, with enhanced features such as profiling. Beside radius support, it can also act as a tacacs server, to simplify secure management access to network devices.

You can find information about the product from [Cisco website](https://web.archive.org/web/20240530151345/https://www.cisco.com/c/en/us/products/collateral/security/identity-services-engine/data_sheet_c78-656174.html).

This section of the document, will guide you configure Cisco ISE, to work with Verge switches for tacacs functionality. ISE software version used to prepare this document, is 2.6 which is the latest version as of the date of publication of this document.

To start configuring tacacs functionality, you need to make sure that, tacacs service is enabled.

To enable tacacs service, use following menu:

> Work Centers->Device Administration->Overview->Deployment

You need to activate all or specific ISE nodes, to provide tacacs services.

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.54.27-1024x428.png)

Once the tacacs service is enabled, you can start configuring the basics. Rest of the configuration will go through the “Work Centers->Device Administration” menu

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.19.37-1024x653.png)

#### Create network device

First, you must define the network device that will be accessed by tacacs credentials. To create a new device, use network resources menu

> Work Centers->Device Administration->Network Resources

From the network resources section menu, click “Network Devices”, and then “+Add” tab. A new page will be opened to enter, the device informations.

- Fill the mandatory fields on the form.
- Keep the “Device Profile” as Cisco
- Check “Tacacs Authentication Settings” and write the same secret that you entered in switch configuration, into the shared secret field.

Be aware that you need to enter the same secret on both side, otherwise your tacacs requests will be rejected, and you will not be able to enter into device CLI.

Below is a sample configuration:

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.33.30-1024x824.png)

Click save at the bottom of the page, to create the network device.

Once created, the device will be listed as shown below:

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.33.59-1024x264.png)

#### Create Tacacs Profile

Create new tacacs profile by clicking “+Add” from;

> Device Administration->Policy Elements->Results->Tacacs Profiles

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.35.03-1024x427.png)

In this example, a new profile to assign user into privilege level 15, which is capable to check all switch functionalities and configure the device.

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.35.58-1024x694.png)

#### Create Command Sets

Command sets are used. to identify the commands allowed to the users. As Angora Verge switches are currently not supporting tacacs command authorization, you simply need to create a simple command set that will allow all commands. Commands allowed to a user can be distinguished by the privileges defined in the tacacs profile.

To create a command set, click “+Add” from;

> Device Administration->Policy Elements->Results->Tacacs Command Sets

Simply add an appropriate name, check “Permit any command that is not listed below” box, and “Save”.

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-24-at-23.08.02-1024x474.png)

#### Create User Identity Groups

It is usually a good idea, to group users with the same privilege into a user group.

To create a new user group, click “+Add” from;

> Device Administration->User Identity Groups->User Identity Groups

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.40.49-1024x441.png)

In the following example, a user group named “Privilege 15 Users” is created:

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.41.34-1024x297.png)

#### Create User

To create actual user accounts to be used for device access, Click “+Add” from;

> Device Administration->Identities->Users

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.42.04-1024x266.png)

Add mandatory fields such as “Name” and “Login Password” and assign the user into appropriate group, in this case, “Privilege 15 Users”

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.43.06-1024x725.png)

Click save to create the user. You can add as many user as you want by repeating the same procedure. You can also use other directory services for username and password control, but the scope of this document is limited to ISE internal user database.

Since, devices and users are created, you need to create a policy to accept tacacs requests.

#### Update Policy Sets

Cisco ISE comes with a set of preconfigured policy sets. To check the policy sets, and add new policies, use the following menu:

> Device Administration->Device Admin Policy Sets

Click the gear icon on the right side of the “default” line to add a “new row above”

Change the name of new policy set, and click the “+” sign on the “Conditions” column.

For basic functionality, you can use a condition that will match to any device created before. In the right hand side “Editor” section, select “DEVICE:Device Type” Equals to All Device Types

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-24-at-22.55.07-1024x228.png)

Click Save to save this condition into the library, and then click “Use” to add this condition into policy set.

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.44.16-1024x284.png)

Once the new policy set is defined, click the “>” (arrow) sign to open the policy set details page.

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-24-at-23.01.52-1024x405.png)

Expand the “Authorization Policy” line. Add new row on above by clicking the gear icon on the end of the default policy line.

Rename the rule and click “+” to add a new condition. This condition will be used to match the user group.

On the editor section, select “Identity Group:Name” Equals to “User Identity Groups: Privilege 15 Groups”, and click save to add this condition into the library.

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-24-at-23.13.59-1024x234.png)

Click “Use” to return policy definition page.

To finalize the policy set, choose the command sets and shell profiles defined above, and click save to activate the policy sets.

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-24-at-23.15.35-1024x508.png)

This concludes the configuration required on Cisco ISE. You can now try to log into the device that you add into ISE, with the user created.

A successful login attempt, will be shown in tacacs live logs, that you reach from;

> Operations->Tacacs->Live logs

Here is a sample log:

![](https://web.archive.org/web/20240530151345im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-24-at-23.19.05-1024x242.png)

### Was this article helpful?

[Yes](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=tacacs-authentication-with-cisco-ise#) [No](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=tacacs-authentication-with-cisco-ise#)

### Related Articles

- [Software Upgrade (TFTP/USB) – Verge Switches](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge "Software Upgrade (TFTP/USB) – Verge Switches")  - 0
  - 720
- [Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)")  - 3
  - 1388
- [Sistem Bilgilerini Öğrenme](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "Sistem Bilgilerini Öğrenme")  - 1
  - 888
- [Link Katmanı Keşif Protokolü (LLDP)](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "Link Katmanı Keşif Protokolü (LLDP)")  - 0
  - 1313
- [Komut Satırı kullanımı](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "Komut Satırı kullanımı")  - 0
  - 1672
- [Hızlı Başlangıç Kılavuzu](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=hizli-baslangic-kilavuzu "Hızlı Başlangıç Kılavuzu")  - 1
  - 957

### Leave A Comment? [Cancel Reply](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=tacacs-authentication-with-cisco-ise\#respond)

Save my name, email, and website in this browser for the next time I comment.