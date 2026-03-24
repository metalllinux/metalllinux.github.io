---
title: "To Create A Yaml Definition File, Use The Dry Ru"
category: "general-linux"
tags: ["create", "yaml", "definition", "file", "dry"]
---

`kubectl run redis --image=redis123 --dry-run=client -o yaml`
* To direct the output to a file, we would do `kubectl run redis --image=redis123 --dry-run=client -o yaml > redis.yaml`
* Create the pod using `kubectl create -f redis.yaml`