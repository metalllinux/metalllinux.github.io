---
title: "Upgrading a Helm Chart Solution"
category: "cka-certification"
tags: ["cka-certification", "upgrading", "helm", "chart", "solution"]
---

# Upgrading a Helm Chart Solution

* How to add the `bitnami` `helm` chart:
```
helm repo add bitnami https://charts.bitnami.com/bitnami
```

* Check how many releases there are in the cluster:
```
helm list
```

* How to upgrade a `helm` chart to a later version:
```
helm upgrade dazzling-web bitnami/nginx --version 18.3.6
```

* How to rollback the application:
```
helm rollback dazzling-web
```
