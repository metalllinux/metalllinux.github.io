---
title: "If Add Network Interface Card Into Host How To B"
category: "networking"
tags: ["networking", "add", "network", "interface", "card"]
---

* Check if the card is detected by NetworkManager with:
```
nmcli device status
```
* Then bring up the device with:
```
sudo nmcli device connect <interface_name>
```
* The device should then be automatically brought up and provided an address via DHCP.
* Give the device a static IP address:
```
sudo nmcli connection modify <INTERFACE_NAME> ipv4.addresses <STATIC_IP/SUBNET_MASK> ipv4.method manual
```
* Provide a gateway address:
```
sudo nmcli connection modify <INTERFACE_NAME> ipv4.gateway <GATEWAY_IP>
```
* Assign a DNS address:
```
sudo nmcli connection modify <INTERFACE_NAME> ipv4.dns <DNS_IP>
```
* Bring the connection down:
```
sudo nmcli connection down <INTERFACE_NAME>
```
* Bring the connection back up:
```
sudo nmcli connection up <INTERFACE_NAME>
```