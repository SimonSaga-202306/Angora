[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")

[1 capture](https://web.archive.org/web/*/https://support.angoranetworks.com/?ht_kb=802-1x-port-based-authentication-using-freeradius "See a list of every capture for this URL")

18 Jan 2022

|     |     |     |
| --- | --- | --- |
| Dec | JAN | Feb |
|  | 18 |  |
| 2021 | 2022 | 2023 |

success

fail
[Share via My Web Archive](https://web.archive.org/web/20220118064213/https://support.angoranetworks.com/?ht_kb=802-1x-port-based-authentication-using-freeradius# "Share via My Web Archive") [Sign In](https://archive.org/account/login.php "Sign In")[Get some help using the Wayback Machine](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine")[Close the toolbar](https://web.archive.org/web/20220118064213/https://support.angoranetworks.com/?ht_kb=802-1x-port-based-authentication-using-freeradius#close "Close the toolbar")

[screenshot](https://web.archive.org/web/20220118064213/http://web.archive.org/screenshot/https://support.angoranetworks.com/?ht_kb=802-1x-port-based-authentication-using-freeradius "screenshot")[video](https://web.archive.org/web/20220118064213/https://support.angoranetworks.com/?ht_kb=802-1x-port-based-authentication-using-freeradius# "video")[Share on Facebook](https://web.archive.org/web/20220118064213/https://support.angoranetworks.com/?ht_kb=802-1x-port-based-authentication-using-freeradius# "Share on Facebook")[Share on Twitter](https://web.archive.org/web/20220118064213/https://support.angoranetworks.com/?ht_kb=802-1x-port-based-authentication-using-freeradius# "Share on Twitter")

[About this capture](https://web.archive.org/web/20220118064213/https://support.angoranetworks.com/?ht_kb=802-1x-port-based-authentication-using-freeradius#expand)

TIMESTAMPS

![loading](https://web-static.archive.org/_static/images/loading.gif)

The Wayback Machine - https://web.archive.org/web/20220118064213/https://support.angoranetworks.com/?ht\_kb=802-1x-port-based-authentication-using-freeradius

# Knowledge Base

Search ForSearch

1. [Home](https://web.archive.org/web/20220118064213/https://support.angoranetworks.com/ "Home")
2. [Knowledge Base](https://web.archive.org/web/20220118064213/https://support.angoranetworks.com/?post_type=ht_kb "Knowledge Base")
3. [How To Guides](https://web.archive.org/web/20220118064213/https://support.angoranetworks.com/?ht_kb_category=how-to-guides "View all posts in How To Guides")
4. [802.1x Port Based Authentication (Using FreeRadius)](https://web.archive.org/web/20220118064213/https://support.angoranetworks.com/?ht_kb=802-1x-port-based-authentication-using-freeradius "802.1x Port Based Authentication  (Using FreeRadius)")

## Overview

802.1x is an IEEE standard to control access of endpoints into computer networks. It defines protocols and interactions of these protocols required to get access to network based resources.

It is configured on the device that provide network connectivity such as wired switches and wireless access points, called _Network Access Device_ or _NAD_. Further details of 802.1x can be found on this [IEEE link](https://web.archive.org/web/20220118064213/https://standards.ieee.org/standard/802_1X-2010.html).

This document describes basic 802.1x via freeradius as authentication server. All sample configuration files for freeradius can be found on [this link](https://web.archive.org/web/20220118064213/https://github.com/anwHub/3rdPartyConfigs/tree/master/freeRadiusConfigs). Please keep in mind that this is a basic setup that authenticates a user computer with username and password, and possibly needs modifications on authentication server side for more detailed access controls.

## Configuration

**Verge Configuration**

Angora Verge swithces running version 5.0 and above supports 802.1x authentication. All sub protocols in the scope of 802.1x authentication such as PEAP, EAP-TLS, EAP-GTC etc. with username/certificate/MAC based authentication options are supported.

In this example document, PEAP is used, for user authentication with the user credentials stored locally into the authentication server. Any directory service integration for user credentials are out of the scope of this document.

To start configuring 802.1x, you need to define the radius server to interact for authentication and configurations on ports that will be authenticated. You can configure more than one server and prioritize them to send the requests. Here, we are using only a single server for quick and easy setup. All timeouts are left at default values. You can check Radius and 802.1x commands and all default values from command line documentation, located on following links:

> [Radius Command Line Guide](https://web.archive.org/web/20220118064213/https://support.angoranetworks.com/?ht_kb=security-radius)
>
> [802.1x Command Line Guide](https://web.archive.org/web/20220118064213/https://support.angoranetworks.com/?ht_kb=security-802-1x)

Here are the configs used for basic 802.1x authentication with freeradius:

> `(config)#radius-server host 192.168.100.200 key [email protected]`

```
This command informs the switch to use the radius with IP address 192.168.100.200 and shared secret key [email protected]
The shared secret defined here must be the same with authentication server NAD config.
```

> `(config)#aaa authentication dot1x default radius`
>
> `(config)#aaa accounting dot1x start-stop group radius`

```
After the radius definition is done, you need to inform the switch
to process the dot1x authentication and accounting packets using the
radius authentication server created above.
It is now time to start the dot1x process
```

> `(config)#dot1x system-auth-control`

`Without this command, the switch will not process any 802.1x request.`

Above commands are the basic configuration for the switch as the network access device. Completing this step, proceeding interface config to enable port based authentication.

For example, to enable 802.1x on Gigabit Ethernet Interface 3, following commands should be applied:

> `(config)#interface GigabitEthernet3`
>
> `(config-if)#dot1x authentication 802.1x`
>
> `(config-if)#dot1x port-control auto`
>
> `(config-if)#dot1x timeout silence-period 60`

These are all the configuration lines that needs to be added to enable switch ports for network access controls.

If you configure the authentication server (freeradius) with appropriate config files, this configuration enables your endpoint access via 802.1x

Following commands can be used for 802.1x authentication monitoring:

> `Angora#show dot1x detailed`
>
> `gi3
> Host mode: multi-host
> Authentication methods: 802.1X
> Port Administrated Status: auto
> Guest VLAN: disabled
> VLAN Radius Attribute: disabled
> Open access: disabled
> Server timeout: 30 sec
> Port Operational Status: authorized
> Applied Authenticating Server: Radius
> Applied Authentication method: 802.1x
> Session Time (HH:MM:SS): 00:00:09
> MAC Address: d0:37:45:39:8e:31
> Username: testuser
> Reauthentication is disabled
> Reauthentication period: 3600 sec
> Silence period: 60 sec
> Quiet period: 60 sec
> Interfaces 802.1X-Based Parameters
> Tx period: 30 sec
> Supplicant timeout: 30 sec
> Max req: 2
> Authentication success: 4
> Authentication fails: 1`

`show dot1x detailed command shows interface level 802.1x status and configuration`

> `Angora#show dot1x users`
>
> `gi3      testuser         d0:37:45:39:8e:31 802.1X Remote 00:00:57`

`show dot1x users command shows current authentication status and user informations, for a specific port`

### Was this article helpful?

[Yes](https://web.archive.org/web/20220118064213/https://support.angoranetworks.com/?ht_kb=802-1x-port-based-authentication-using-freeradius#) [No](https://web.archive.org/web/20220118064213/https://support.angoranetworks.com/?ht_kb=802-1x-port-based-authentication-