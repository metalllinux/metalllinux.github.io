---
title: "How To Remove All Docker Containers"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "remove", "all", "docker", "containers"]
---

```
docker rm $(docker ps -a -q)
```