---
title: "If Have An Amd R7 9 Series Card And Running Later"
category: "general-linux"
tags: ["amd", "series", "card", "running", "later"]
---

How to install the `amdgpu` drivers instead of `radeon` (which are defaulted to).

Add the following after the `quiet splash` in the following line of `/etc/default/grub`

`radeon.cik_support=0 radeon.si_support=0 amdgpu.cik_support=1 amdgpu.si_support=1 amdgpu.dc=1`

Then run `sudo grub2-mkconfig -o /boot/grub`

ALTERNATIVELY

Where it says `quiet` in the `/etc/default/grub` line, replace `quiet` with the above and then run `sudo grub-mkconfig -o /boot/grub`.
After that, restart. This was for openSUSE

If the above doesn't work, you can place the configuration AFTER the word `quiet` - worked for BlendOS 3

For Garuda Linux, This configuration worked:
`GRUB_CMDLINE_LINUX_DEFAULT='quiet radeon.cik_support=0 radeon.si_support=0 amdgpu.cik_support=1 amdgpu.si_support=1 quiet rd.udev.log_priority=3 vt.global_cursor_default=0 loglevel=3' # Modified by garuda-migrations: splash`
* Then:
`sudo grub-mkconfig -o /boot/grub/grub.cfg`

FOR DEBIAN:

You need this line:

GRUB_CMDLINE_LINUX_DEFAULT="quiet radeon.cik_support=0 radeon.si_support=0 amdgpu.cik_support=1 amdgpu.si_support=1"

Then 

sudo grub-mkconfig -o /boot/grub/grub.cfg

For Ubuntu and Linux Mint do:

Add the following after the `quiet splash` in `/etc/default/grub`

`radeon.cik_support=0 radeon.si_support=0 amdgpu.cik_support=1 amdgpu.si_support=1 amdgpu.dc=1`

Then 

sudo grub-mkconfig -o /boot/grub/grub.cfg

For Fedora:
Set `/etc/default/grub` to the following:

```
GRUB_TIMEOUT=5
GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"
GRUB_DEFAULT=saved
GRUB_DISABLE_SUBMENU=true
GRUB_TERMINAL_OUTPUT="console"
GRUB_CMDLINE_LINUX="rhgb quiet radeon.cik_support=0 radeon.si_support=0 amdgpu.cik_support=1 amdgpu.si_support=1 amdgpu.dc=1"
GRUB_DISABLE_RECOVERY="true"
GRUB_ENABLE_BLSCFG=true
```

* Then perform:
`sudo grub2-mkconfig -o /boot/grub`

FOR KDE NEON

Add the following after the `quiet splash` in the following line of `/etc/default/grub`

`radeon.cik_support=0 radeon.si_support=0 amdgpu.cik_support=1 amdgpu.si_support=1 amdgpu.dc=1`

* Then run `sudo grub-mkconfig -o /boot/grub/grub.cfg`

For Rocky Linux 9

Enable the CRB repo.
`sudo dnf config-manager --enable crb`
Download the drivers for RHEL 9.3: https://www.amd.com/en/support/linux-drivers
Install the RPM: `sudo dnf localinstall ./<file>`
Run: 
`amdgpu-install`
`reboot`