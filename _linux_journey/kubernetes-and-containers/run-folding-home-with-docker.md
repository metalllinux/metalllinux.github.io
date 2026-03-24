---
title: "Run Folding@Home With Docker"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "run", "foldinghome", "docker"]
---

* Uses https://hub.docker.com/r/stefancrain/folding-at-home

```
docker run \
  -p 7396:7396 \
  stefancrain/folding-at-home:latest \
  --user=metalinux \
  --team=229500 \
  --power=full \
  --cpu-usage=100
```