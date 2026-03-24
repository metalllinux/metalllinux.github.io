---
title: "How Create A Vmcore Dump"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "create", "vmcore", "dump"]
---

Ensure `kdump` is running with `kdumpctl status`.
echo 1 > /proc/sys/kernel/sysrq 
echo c > /proc/sysrq-trigger
Then check `/var/crash` for a core dump. Depending on `/etc/kdump.conf`, it may be in a different location.
* A `vmcore` dump is also generated in `/proc/vmcore`.
* Good troubleshooting areas to check are:
* /var/log/messages
* /var/log/kdump.log