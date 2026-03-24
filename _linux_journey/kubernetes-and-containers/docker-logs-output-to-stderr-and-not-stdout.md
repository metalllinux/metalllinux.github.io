---
title: "Docker Logs Output To Stderr And Not Stdout"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "docker", "logs", "output", "stderr"]
---

To therefore grep docker logs, we need to do:
```
sudo docker logs <SERVICE> 2>&1 | grep "<field>"
```