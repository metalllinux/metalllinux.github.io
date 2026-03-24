---
title: "How To Set The Vm Disk Size In Openqa"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "disk", "size", "openqa"]
---

An example:
```
podman exec -it openqa openqa-cli api -X POST jobs ISO=Rocky-8.10-x86_64-dvd1.iso DISTRI=rocky-linux FLAVOR=DVD TEST=_do_install_and_reboot HDDSIZEGB=20
```