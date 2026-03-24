---
title: "Rbac"
category: "cka-certification"
tags: ["cka-certification", "rbac"]
---

* Need to create an RBAC object for the role:
```
developer-role.yaml

apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["list", "get", "create", "update", "delete"]
```
* For the `Core` group, you leave the `apiGroups` section as blank.
* To allow a developer to create a `ConfigMap`, do the following:
```
developer-role.yaml

apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["list", "get", "create", "update", "delete"]

- apiGroups: [""]
  resources: ["ConfigMap"]
  verbs: ["create"]
```
* Create the rule using the `kubectl create -f <role_name.yaml>` command.
* The user has to be linked to the role. Another yaml file is needed (links a user object to a role):
```
devuser-developer-binding.yaml

apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: devuser-developer-binding
subjects:
- kind: User
  name: dev-user
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: developer
  apiGroup: rbac.authorization.k8s.io 
```
* `subjects` - user details.
* `roleRef` - details about the role.
* The Roles and Role Bindings fall under the scope of Namespaces.
* In the above example, the user is given access to pods and ConfigMaps within the default namespace.
* If you want to limit the user's access to different namespaces, specify that in the `metadata` section when creating the namespaces.
* To view created roles, run the following command:
```
kubectl get roles
```
* To view the rolebindings, run:
```
kubectl get rolebindings
```
* To view more details about the role:
```
kubectl describe role <role_name>
```
* To view more details on rolebindings:
```
kubectl describe rolebinding <binding_name>
```
* How to Check Access to a resource?
	* Run this command:
```
kubectl auth can-i <action> <thing>

kubectl auth can-i create deployments

kubectl auth can-i delete nodes
```
* As an admin, it is possible to impersonate another user to check permissions.
* Use the above command, with the `--as` user option to check a user's access from the admin's perspective:
```
kubectl auth can-i create deployments --as <user_here>
```
* For example to check a specific namespace as well:
```
kubectl auth can-i create pods --as <user> --namespace <namespace_here>
```
* Can restrict access to certain pods by adding a `Resource Names` field:
```
developer-role.yaml

apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["list", "get", "create", "update", "delete"]
  resourceNames: ["blue", "orange"]
```
* Thus the user with the assigned role only has access to the `blue` and `orange` pods.
* Create the required roles and role bindings to allow a specific user to do something:
* To create a role:
```
kubectl create role developer --namespace=default --verb=list,create,delete --resource=pods
```
* Create a role binding:
```
kubectl create rolebinding dev-user-binding --namespace=default --role=developer --user=dev-user
```
* The two role creations can be applied at the same time with this file:
```
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  namespace: default
  name: developer
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["list", "create","delete"]

---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: dev-user-binding
subjects:
- kind: User
  name: dev-user
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: developer
  apiGroup: rbac.authorization.k8s.io
```
* How to edit a role:
```
kubectl edit role developer -n blue
```
* How to add a new rule in an existing role `developer` and grant the `dev-user` permissions to create deployments in the `blue` namespace.
* Firstly edit the namespace:
```
kubectl edit role developer -n blue
```
* Change it so it looks like the following:
```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer
  namespace: blue
rules:
- apiGroups:
  - apps
  resourceNames:
  - dark-blue-app
  resources:
  - pods
  verbs:
  - get
  - watch
  - create
  - delete
- apiGroups:
  - apps
  resources:
  - deployments
  verbs:
  - create
```