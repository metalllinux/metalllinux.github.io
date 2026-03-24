---
title: "Solution Monitor Application Logs"
category: "cka-certification"
tags: ["cka-certification", "solution", "monitor", "application", "logs"]
---

* Check logs with `kubectl logs <application>`
* If there are two or more containers, must specify which container you want to check. An example command is:
```
kubectl logs webapp-2 -c simple-webapp
```