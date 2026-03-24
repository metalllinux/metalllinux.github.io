---
title: "How Observe More Verbose Messages When Running Cra"
category: "general-linux"
tags: ["observe", "more", "verbose", "messages", "when"]
---

Use `-d8` for example:
```
crash -d8 /usr/lib/debug/lib/modules/3.10.0-1160.119.1.el7.x86_64.debug/vmlinux ./vmcore
```
* Check the release information with:
```
crash -d8 /usr/lib/debug/lib/modules/3.10.0-1160.119.1.el7.x86_64.debug/vmlinux ./vmcore | grep release
```