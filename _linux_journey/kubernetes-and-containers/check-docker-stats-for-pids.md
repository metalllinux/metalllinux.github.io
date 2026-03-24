---
title: "Check Docker Stats For Pids"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "check", "docker", "stats", "pids"]
---

docker stats --format "table {{.PIDs}}\t{{.Name}}" --no-stream | sort -rn | head -n 5