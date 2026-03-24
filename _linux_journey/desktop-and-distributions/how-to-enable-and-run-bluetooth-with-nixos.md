---
title: "How To Enable And Run Bluetooth With Nixos"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "enable", "run", "bluetooth", "nixos"]
---

* Enable/add the following configuration to `configuration.nix`:
`services.blueman.enable = true;`
`{
  hardware.pulseaudio.enable = true;
  hardware.bluetooth.enable = true;
}`
* Then run `nixos-rebuild switch` to enable the new configuration.
* After that, pair and connect with:
$ bluetoothctl
[bluetooth] # power on
[bluetooth] # agent on
[bluetooth] # default-agent
[bluetooth] # scan on
...put device in pairing mode and wait [hex-address] to appear here...
[bluetooth] # pair [hex-address]
[bluetooth] # connect [hex-address]

* Check for paired devices in bluetoothctl with:
* `devices`

* If still having problems connecting with an `Failed to connect: org.bluez.Error.Failed br-connection-profile-unavailable` error, run:
* `systemctl --user start pulseaudio`
* `systemctl --user enable pulseaudio`