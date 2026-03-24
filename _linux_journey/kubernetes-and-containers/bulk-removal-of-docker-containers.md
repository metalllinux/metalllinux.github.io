---
title: "Bulk Removal Of Docker Containers"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "bulk", "removal", "docker", "containers"]
---

docker rm -v $(docker ps --filter status=created -q)