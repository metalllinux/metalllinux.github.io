---
title: "override for pipewire-pulse.conf file"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "automatically", "direct", "audio", "arch"]
---

Create
```
~/.config/pipewire/pipewire-pulse.conf.d/switch-on-connect.conf
```
Add the following
```
# override for pipewire-pulse.conf file
pulse.cmd = [
    { cmd = "load-module" args = "module-always-sink" flags = [ ] }
    { cmd = "load-module" args = "module-switch-on-connect" }
]
```
* Restart `pulseaudio` or reboot.