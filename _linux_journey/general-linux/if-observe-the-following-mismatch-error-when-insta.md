---
title: "If Observe The Following Mismatch Error When Insta"
category: "general-linux"
tags: ["observe", "following", "mismatch", "error", "when"]
---

```
error: db5 error(-30969) from dbenv->open: BDB0091 DB_VERSION_MISMATCH: Database environment version mismatch
```
* Run through these instructions:
```
sudo dnf upgrade --refresh rpm glibc
sudo rm /var/lib/rpm/.rpm.lock
sudo dnf upgrade dnf
```