---
title: "Good Sed Command To Allow Root User Login"
category: "editors-and-tools"
tags: ["editors-and-tools", "good", "sed", "command", "allow"]
---

```
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /usr/etc/ssh/sshd_config
```