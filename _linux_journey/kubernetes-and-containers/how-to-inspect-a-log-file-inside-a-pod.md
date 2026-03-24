---
title: "How To Inspect A Log File Inside A Pod"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "inspect", "log", "file", "inside"]
---

```
kubectl -n elastic-stack exec -it app -- cat /log/app.log
```