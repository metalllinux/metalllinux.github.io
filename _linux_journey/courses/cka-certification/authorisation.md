---
title: "Authorisation"
category: "cka-certification"
tags: ["cka-certification", "authorisation"]
---

* Once someone gains access to the cluster, what can they do?
* An admin can perform the following:
```
kubectl get nodes
kubectl get pods
kubectl delete node <node_name>
```
* Others also need to access the cluster such as Continuous Delivery things like Jenkins.
* We also need to take into account `Developers` and `Bots`. We don't want `Developers` to run `kubectl delete node <node_name>`
* Want to restrict access to users to their namespaces.
* There are multiple Authorisation Mechanisms available:
	* Node
		* Users access the `kube apiserver` and the `kubelet` also accesses the `kube apiserver`.
		* The `kubelet` Reads - Services, Endpoints, Nodes and Pods.
		* The `kubelet` Writes - Node status, Pod status and Events.
		* The above requests are handled by the Node Authoriser.
		* The `kubelet` should be part of the System Nodes group. Any request coming from the System Nodes Group or Authoriser is granted.
	* ABAC - Attribute-Based Access Control
		* Associate a user / group of users with a set of permissions.
		* For example, the `dev-user` creates a load of pods. They are provided `Can view PODSs`, `Can create PODs` and `Can Delete PODs` access.
		* The JSON format would be `"kind": "Policy", "spec": {"user": "dev-user", "namespace": "*", "resource": "pods", "apiGroup": "*"}`
			* The above file is passed into the `kube apiserver`.
		* A policy definition file is given to each user / group.
			* Any changes needs the policy file to be edited manually and the `kube api-server` to be restarted.
	* RBAC - instead of giving a user / group a set of permissions, a role is defined.
		* For example a `Developer` role has the following permissions: `Can view PODs`, `Can create PODs`, `Can Delete PODs`.
		* Another example is creating a role for `Security` users. Permissions would be `Can view CSR`, `Can approve CSR`
		* Any changes are done at the Role level and are then applied to all users.
	* Webhook - if you want toutsource all authorisation mechanisms.
		* `Open Policy Agent` is a third party tool.
		* Can have Kubernetes make a call to the `Open Policy Agent`.
		* Then the `Open Policy Agent` decides if a user is allowed or not.
	* AlwaysAllow - allows all requests without performing authorisation.
	* AlwaysDeny - Denies all requests.
* How do you set the above modes? These are set on the `kube api-server`, under `--authorization-mode=<mode_name>`
	* If you do not specify the optoin, `AlwaysAllow` is set by default.
	* Can add multiple mode s with commas, for example `--authorization-mode=Node,RBAC,Webhook` etc.
* If there are multiple authorisation settings added, the requests will be filtered in the order the settings have been placed in the `authorization-mode` option.
	* When a module denies a request, it moves to the next setting in the chain. As soon as a module approves a request, no more checks are done and the user has access to the item.