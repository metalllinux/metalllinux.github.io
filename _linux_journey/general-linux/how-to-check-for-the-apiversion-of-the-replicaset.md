---
title: "How To Check For The Apiversion Of The Replicaset"
category: "general-linux"
tags: ["check", "apiversion", "replicaset"]
---

`kubectl api-resources | grep replicaset`
Can also find out with this command as well:
`kubectl explain replicaset | grep VERSION`