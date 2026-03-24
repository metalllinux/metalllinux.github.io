---
title: "How to Get Rid of a GPG Key Installed on Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "rid", "gpg", "key", "you"]
---

# How to Get Rid of a GPG Key Installed on Rocky Linux

* Run this command to list all GPG Keys:

```
rpm -qi gpg-pubkey
```

* Remove a key by referencing its `Version` and `Release` like so:

```
sudo rpm -e gpg-pubkey-be1229cf-5631588c
```
