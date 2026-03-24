---
title: "If Pi Hole Is Unable To Connect To Port 53 On Ubun"
category: "general-linux"
tags: ["hole", "unable", "connect", "port", "ubun"]
---

systemctl disable systemd-resolved.service
systemctl stop systemd-resolved
Edit `/etc/resolv.conf`
Comment out any existing `nameserver` configuration and add `nameserver 8.8.8.8`
Once pi-hole is running, change the nameserver back again to `nameserver 127.0.0.1`