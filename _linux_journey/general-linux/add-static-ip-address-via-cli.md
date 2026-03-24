---
title: "Add Static Ip Address Via Cli"
category: "general-linux"
tags: ["add", "static", "address", "cli"]
---

`sudo vim /etc/network/interfaces`

Example:
`# The primary network interface
allow-hotplug eno1
iface eno1 inet static
      address 10.189.1.234
      netmask 255.255.255.0
      gateway 10.189.1.1
      dns-nameserver 10.189.1.49`

Then restart the `networking` `systemd` service for the changes to be implemented:

`sudo /etc/init.d/networking restart`
