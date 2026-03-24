---
title: "Cluster Roles And Role Bindings"
category: "cka-certification"
tags: ["cka-certification", "cluster", "roles", "role", "bindings"]
---

* Roles and Role Bindings are `Namespaced` (created within namespaces).
* If you do not specify a namespace, they are created in the `default` namespace and only control access there.
* Can you group or isolate nodes into a namespace? - No, this is not possible, they are cluster-wide resources.
* Resources are categorised as either `namespaced` or `cluster-scoped`
* A list of `namespaced` things:
	* `pods`
	* `replicasets`
	* `jobs`
	* `deployments`
	* `services`
	* `secrets`
	* `roles`
	* `rolebindings`
	* `configmaps`
	* `PVC`
* To view or update Roles or Role Bindings, have to specify the right namespace.
* `Cluster Scoped` resources are those where you do not specify a namespace:
	* `nodes`
	* `PV`
	* `clusteroles`
	* `clusterrolebindings`
	* `certificatesigningrequests`
	* `namespaces`
* To see a full list of `namespaced` and `non-namespaced` resources:
```
kubectl api-resources --namespaced=true

kubectl api-resources --namespaced=false
```
* How to authorise a user to use `Cluster Scoped` resources?
	* Need to use `clusterroles` and `clusterrolebindings`.
* `clusteroles` and like `roles`, except for `Cluster Scoped` resources.
* `Cluster Admin` can be created. They have these powers:
	* `Can view Nodes`
	* `Can create Nodes`
	* `Can delete Nodes`
* `Storage Admin` role allows:
	* `Can view PVs`
	* `Can create PVs`
	* `Can delete PVCs`
* Need a cluster definition file:
```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cluster-administrator
rules:
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["list","get","create","delete"]
```
* Create the role as per usual:
```
kubectl create -f cluster-admin-role.yaml
```
* Next we have to link the user to the ClusterRole. Therefore need the ClusterRole Binding:
```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: cluster-admin-role-binding
subjects:
- kind: User
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: cluster-administrator
  apiGroup: rbac.authorization.k8s.io
```
* Apply this again using the `kubectl create -f <definition_file.yaml>`
* You can create a ClusterRole for `namespaced` resources as well.
	* If you do that, the user has access across all namespaces.
* With ClusterRoles, if you give the user access, they get access to all pods across the cluster.
* Kubernetes creates a number of clusterroles by default when the cluster is setup.