---
title: "Script To Add A User, Provide A Password And Add T"
category: "general-linux"
tags: ["script", "add", "user", "provide", "password"]
---

useradd <user>
echo <user>:<password> | chpasswd
usermod -aG wheel <user>