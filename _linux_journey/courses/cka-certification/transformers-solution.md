---
title: "Transformers Solution"
category: "cka-certification"
tags: ["cka-certification", "transformers", "solution"]
---

# Transformers Solution 

* Good kustomisation directory structure overview:
```
controlplane ~/code ➜  ls -lrR /root/code/k8s
/root/code/k8s:
total 16
drwxr-xr-x 2 root root 4096 Jun 20 14:30 nginx
drwxr-xr-x 2 root root 4096 Jun 20 14:30 monitoring
-rw-r--r-- 1 root root  151 Jun 20 14:30 kustomization.yaml
drwxr-xr-x 4 root root 4096 Jun 20 14:30 db

/root/code/k8s/nginx:
total 12
-rw-r--r-- 1 root root 196 Jun 20 14:30 nginx-service.yaml
-rw-r--r-- 1 root root 299 Jun 20 14:30 nginx-depl.yaml
-rw-r--r-- 1 root root 125 Jun 20 14:30 kustomization.yaml

/root/code/k8s/monitoring:
total 12
-rw-r--r-- 1 root root 151 Jun 20 14:30 kustomization.yaml
-rw-r--r-- 1 root root 215 Jun 20 14:30 grafana-service.yaml
-rw-r--r-- 1 root root 317 Jun 20 14:30 grafana-depl.yaml

/root/code/k8s/db:
total 16
drwxr-xr-x 2 root root 4096 Jun 20 14:30 Sql
drwxr-xr-x 2 root root 4096 Jun 20 14:30 NoSql
-rw-r--r-- 1 root root  143 Jun 20 14:30 kustomization.yaml
-rw-r--r-- 1 root root  118 Jun 20 14:30 db-config.yaml

/root/code/k8s/db/Sql:
total 12
-rw-r--r-- 1 root root 119 Jun 20 14:30 kustomization.yaml
-rw-r--r-- 1 root root 217 Jun 20 14:30 db-service.yaml
-rw-r--r-- 1 root root 490 Jun 20 14:30 db-depl.yaml

/root/code/k8s/db/NoSql:
total 12
-rw-r--r-- 1 root root 119 Jun 20 14:30 kustomization.yaml
-rw-r--r-- 1 root root 213 Jun 20 14:30 db-service.yaml
-rw-r--r-- 1 root root 671 Jun 20 14:30 db-depl.yaml
```
* Good kustomzation example yaml file:
```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - NoSql/
  - Sql/
  - db-config.yaml

namePrefix: data-
```
* How to check the namespace that all monitoring resources will be applied to?

    * Under `kustomization.yaml`, look for:
    ```
    namespace: logging
    ```
* Example of assigning an annotation in a `kustomzation.yaml` file:
```
commonAnnotations:
  owner: bob@gmail.com
```
* An example of changing nginx with  a tag:
```
images:
  - name: nginx
    newName: nginx:1.23
```
