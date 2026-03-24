---
title: "How Programatically Append Ip And Hostname To Etc"
category: "general-linux"
tags: ["programatically", "append", "hostname"]
---

```
hostnamectl set-hostname “8-6-lts-master”
IP_ADDRESS=$(hostname -I | cut -f1 -d ' ')
echo "$IP_ADDRESS 8-6-lts-master" >> /etc/hosts
```