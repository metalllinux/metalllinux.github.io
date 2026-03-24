---
title: "Where To Check For Errors With Munge"
category: "rocky-linux"
tags: ["rocky-linux", "where", "check", "errors", "munge"]
---

```
/var/log/munge/munged.log
```
or
```
journalctl -fxu munge
```
or
```
systemctl status --full munge.service
```