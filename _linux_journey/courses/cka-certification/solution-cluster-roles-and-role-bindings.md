---
title: "Solution Cluster Roles And Role Bindings"
category: "cka-certification"
tags: ["cka-certification", "solution", "cluster", "roles", "role"]
---

* How to check the amount of clusterroles there are:
```
kubectl get clusterroles
```
* How to check the amount of `clusterRoleBindings`:
```
kubectl get clusterRoleBindings
```
* How to check the namespace that the `cluster-admin` is in:
```
kubectl api-resources --namespaced=false
```
* `ClusterRole` is a non-namespaced resource. Correct answer:
`Cluster Roles are cluster wide and not part of any namespace`
* How find which groups the cluster-admin role is bound to?
```
kubectl describe clusterrolebinding cluster-admin
```
* The group would be the following:
```
kubectl describe clusterrolebinding cluster-admin
```
* A `Cluster Admin` can perform any action in the cluster.
* A `clusterRole` and a `clusterRoleBinding` for the Michelle user:
```
---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: node-admin
rules:
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["get", "watch", "list", "create", "delete"]

---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: michelle-binding
subjects:
- kind: User
  name: michelle
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: node-admin
  apiGroup: rbac.authorization.k8s.io
```
* Allow the MIchelle user to access and control storage:
```
---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: storage-admin
rules:
- apiGroups: [""]
  resources: ["persistentvolumes"]
  verbs: ["get", "watch", "list", "create", "delete"]
- apiGroups: ["storage.k8s.io"]
  resources: ["storageclasses"]
  verbs: ["get", "watch", "list", "create", "delete"]

---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: michelle-storage-admin
subjects:
- kind: User
  name: michelle
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: storage-admin
  apiGroup: rbac.authorization.k8s.io
```