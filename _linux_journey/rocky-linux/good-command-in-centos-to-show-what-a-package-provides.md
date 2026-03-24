---
title: "Good Command in CentOS to Show What a Package Provides"
category: "rocky-linux"
tags: ["rocky-linux", "good", "command", "centos", "show"]
---

# Good Command in CentOS to Show What a Package Provides

```
repoquery kernel-core --provides |grep -v -e 'kernel(.*)' |grep -ve 'kmod(.*)'
```

