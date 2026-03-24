---
title: "How To Set Network Information Using Nmcli And Net"
category: "networking"
tags: ["networking", "network", "information", "nmcli", "net"]
---

* Find the interfaces
`nmcli connection show`
* Set the network information like the below format:
`nmcli connection modify <connection_name> ipv4.method manual ipv4.addresses <static_ip_address>/<subnet_mask> ipv4.gateway <gateway_ip_address> ipv4.dns <dns_server_ip>`
* Bring the connection up to enable the changes.
`nmcli connection up <connection_name>`
* Check that the network information has been saved.
`nmcli device show <connection_name>`