---
title: "If Run Into Gpg Keyserver Received Failed No Rou"
category: "security"
tags: ["security", "run", "into", "gpg", "keyserver"]
---

* Create `~/.gnupg/gpg.conf`
* Add the line:
```
keyserver hkps://keys.gnupg.net
```
* Create `~/.gnupg/dirmngr.conf`
* Add the line:
```
keyserver hkps://keys.gnupg.net
```
* Reboot