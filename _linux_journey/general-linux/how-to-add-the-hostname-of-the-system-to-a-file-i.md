---
title: "How To Add The Hostname Of The System To A File, I"
category: "general-linux"
tags: ["add", "hostname", "system", "file"]
---

```
HOSTNAME=$(hostname)
tar -cvf ${HOSTNAME}.tar.gz directory_to_archive/
```