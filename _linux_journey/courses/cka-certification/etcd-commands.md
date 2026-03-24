---
title: "Etcd Commands"
category: "cka-certification"
tags: ["cka-certification", "etcd", "commands"]
---

* `etcdctl` supports the following commands in Version 2:
```
etcdctl backup
etcdctl cluster-health
etcdctl mk
etcdctl mkdir
etcdctl set
```
* `etcdctl` commands in Version 3:
```
etcdctl snapshot save 
etcdctl endpoint health
etcdctl get
etcdctl put
```
* Set the API level with this command.
```
export ETCDCTL_API=3
```
* If the API level is not set, it is assumed that Version 2 is in use.
* Must specify paths to certificates files, then `etcdctl` can then authenticate to the `etcd` API Server.
* The certificate files are available in the `etcd-master` pod at these paths:
```
--cacert /etc/kubernetes/pki/etcd/ca.crt     
--cert /etc/kubernetes/pki/etcd/server.crt     
--key /etc/kubernetes/pki/etcd/server.key
```
* You must specify the API version and paths to certificate files, like in the below example:
```
kubectl exec etcd-master -n kube-system -- sh -c "ETCDCTL_API=3 etcdctl get / --prefix --keys-only --limit=10 --cacert /etc/kubernetes/pki/etcd/ca.crt --cert /etc/kubernetes/pki/etcd/server.crt  --key /etc/kubernetes/pki/etcd/server.key" 
```