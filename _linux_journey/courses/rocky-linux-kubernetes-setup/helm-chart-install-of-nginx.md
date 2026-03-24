---
title: "Helm Chart Install of nginx"
category: "rocky-linux-kubernetes-setup"
tags: ["rocky-linux-kubernetes-setup", "helm", "chart", "install", "nginx"]
---

# Helm Chart Install of nginx

* Install the chart
```
helm install nginx-test oci://registry-1.docker.io/bitnamicharts/nginx
```

* Check the `helm` charts:

```
helm list
```

* Update to the latest repositories:

```
helm repo update
```

* Search a repo:

```
helm search repo
```

* Upgrade like this:

```
helm upgrade nginx-test kk-mock1/nginx --vesrion 18.1.5
```






