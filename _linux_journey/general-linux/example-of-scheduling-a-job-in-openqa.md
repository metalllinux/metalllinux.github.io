---
title: "Example Of Scheduling A Job In Openqa"
category: "general-linux"
tags: ["example", "scheduling", "job", "openqa"]
---

```
openqa-cli api -X POST jobs ISO=Rocky-9.5-x86_64-boot.iso DISTRI=rocky-linux FLAVOR=boot VERSION=test BUILD=test TEST=_console_login
```