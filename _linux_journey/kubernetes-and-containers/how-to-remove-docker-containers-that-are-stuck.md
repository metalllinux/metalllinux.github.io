---
title: "How To Remove Docker Containers That Are Stuck"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "remove", "docker", "containers", "are"]
---

docker rm $(docker ps -q -f status=exited)

docker rm $(docker ps -a -f status=exited -f status=created -q)