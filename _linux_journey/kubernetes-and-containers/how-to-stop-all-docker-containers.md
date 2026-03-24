---
title: "How To Stop All Docker Containers"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "stop", "all", "docker", "containers"]
---

```
docker stop $(docker ps -a -q)
```