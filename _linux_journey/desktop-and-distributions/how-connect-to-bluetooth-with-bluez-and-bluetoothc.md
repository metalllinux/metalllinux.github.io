---
title: "How Connect To Bluetooth With Bluez And Bluetoothc"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "connect", "bluetooth", "bluez", "bluetoothc"]
---

`bluetoothctl`
`power on`
`agent on`
`default-agent`
`scan on`
`pair [hex-address]`
`connect [hex-address]`
`trust [hex-address]`

Other options also include:
`disconnect [hex-address]`
`remove [hex-address]`
* Check for paired devices in bluetoothctl with:
* `devices`