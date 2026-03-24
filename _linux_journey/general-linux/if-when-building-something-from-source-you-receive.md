---
title: "If When Building Something From Source You Receive"
category: "general-linux"
tags: ["when", "building", "something", "source", "you"]
---

* Ensure the appropriate repos are activated.
* In the example of Rocky Linux 8.10, this was:
```
dnf config-manager --set-enabled powertools
```
* Then `dnf install -y texinfo`