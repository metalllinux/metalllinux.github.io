---
title: "If You Want To Disable Repositories In Centos 7.9"
category: "rocky-linux"
tags: ["rocky-linux", "you", "want", "disable", "repositories"]
---

Edit `/etc/yum.repos.d/CentOS-Base.repo`
Add `enabled=0` under each repository you wish to disable.