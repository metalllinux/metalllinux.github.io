---
title: "If You Run into Connection Renaming Issues with Libvirt"
category: "virtualisation"
tags: ["virtualisation", "run", "into", "connection", "renaming"]
---

# If You Run into Connection Renaming Issues with Libvirt

[howard@howard-ciq-rocky-linux-9 ~]$ sudo nmcli connection add type bridge-slave autoconnect yes con-name "Wired connection 1" ifname "Wired connection 1" master virbr0
Error: Failed to add 'Wired connection 1' connection: connection.interface-name: 'Wired connection 1': interface name contains an invalid character
[howard@howard-ciq-rocky-linux-9 ~]$ sudo nmcli connection add type bridge-slave autoconnect yes con-name "enp2s0" ifname "enp2s0" master virbr0

In the above example, use `enp2s0` instead and delete any existing `enp2s0` afterwards before bringing up the virtual connection with `sudo nmcli connection up <VIRTUAL_BRIDGE_CON-NAME>`

