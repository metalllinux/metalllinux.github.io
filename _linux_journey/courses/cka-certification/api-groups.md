---
title: "Api Groups"
category: "cka-certification"
tags: ["cka-certification", "api", "groups"]
---

* We interact with the `kube api-server`, either through the `kubectl` utility or REST APIs.
* Can find the API version by running a `curl` command with the following:
```
curl https://kube-master:6443/version
```
* To get a list of pods, we perform this command:
```
curl https://kube-master:6443/api/v1/pods
```
* API has many groups: `/metrics`, `/healthz`, `/version`, `/api`, `/apis`, `/logs`
* `/metrics` and `/healthz` - monitor the health of the cluster.
* Focus on the cluster's functionality.
* There are two categories of API's, `core` and `named` groups:
	* core - `/api`
	* named - `/apis`
* The core group is where the main functionality of Kubernetes lies:
	* `/v1` --> `namespaces`, `pods`, `rc`, `events`, `endpoints`, `nodes`, `bindings`, `PV`, `PVC (Persistent Volume Claims)`, `configmaps`, `secrets` and `services`
* The named groups are more organised.
	* `/apis` you have the following:
		* `/apps` --> `/v1` --> `/deployments`, `/replicasets` and `/statefulsets`
	* `/extensions`
	* `/networking.k8s.io` --> `/v1` --> `/networkpolicies`
* `/storage.k8s.io`
* `/authentication.k8s.io`
* `/certificates.k8s.io` --> `/v1` --> `/certificatesigningrequests`
* The main ones such as `/apps`, `/extensions`, `networking.k8s.io` are API Groups.
* The ones at the bottom such as `/deployments`, `/replicasets`, `/statefulsets` are Resources.
* Each resource has an action associated. For example under `/deployments`:
	* `list`
	* `get`
	* `create`
	* `delete`
	* `update`
	* `watch`
* All of the above are called Verbs.
* Can also list the available API groups with the following command:
```
curl http://localhost:6443 -k
```
* Running a `grep` for `name` returns all of the supported resource groups:
```
curl http://localhost:6443/apis -k | grep "name"
```
* Must authenticate to the API by passing in your certificate files:
```
curl http://localhost:6443 -k --key admin.key --cert admin.crt --cacert ca.crt
```
* Another option is to start a `kubectl proxy` client. Run `kubectl proxy` to start the service.
* Run the command and it starts a service on port `8001`.
	* The flow from the proxy is like so: `kubectl proxy` --> `kube apiserver`
		* It uses credentials and certificates from the user's kubeconfig file.
			* Can then successfully run `curl http://localhost:6443 -k
`
* Kube proxy is not the same as `kubectl proxy`
* Kube proxy allows connectivity between different pods and nodes in the cluster.
* `kubectl proxy` --> HTTP proxy service created by the kubectl utility to access the kube-apiserver.