---
title: "Authentication"
category: "cka-certification"
tags: ["cka-certification", "authentication"]
---

* Access to the cluster comes from these groups:
	* Admins
	* Developers
	* Application End Users
	* Bots - Service Accounts
* Will discuss how to secure access to the Kubernetes cluster with authentication mechanisms.
* Kubernetes does not manage user accounts natively.
* Kubernetes can create Service Accounts: `kubectl create serviceaccount sa1`
* To get the number of generated service accounts:
```
kubectl get serviceaccount
```
* All user access is managed by the `kube-apiserver`.
	* This is either through the admin accessing via the `kubectl` tool or the `kube-apiserver` directly with a `curl` command like:
```
curl https://kube-server-ip:6443
```
* The `kube-apiserver` firstly `Authenticates` the request and then `Processes` the request.
* Authentication Mechanisms are the following:
	* `Static Password File`
	* `Static Token File`
	* `Certificates`
	* `Identity Services`
* For `Static Password File`, create a CSV file and store the information like so:
```
password,user,user_id
```
* The filename is then passed as an option to the `kube-apiserver` using `--basic-auth-file=<file.csv>`
* Specify the `--basic-auth-file` option in the `kube-apiserver.service` file.
* Restart the `kube-apiserver` for the options to take effect.
* If set up the cluster using the `kubeadm` tool, must modify the `kube-apiserver.yaml` file at `/etc/kubernetes/manifests/kube-apiserver.yaml`
* The `kube-apiserver` will be updated automatically.
* To authenticate using the basic credentials whilst accessing the `kube api-server`, specify the user and password in a `curl` command like this:
```
curl -v -k https://master-node-ip:6443/api/v1/pods -u "user1:password123"
```
* In the user CSV file, can have a fourth option for `group id` to assign users to specific groups.
* A static token file can be also used and looks like this:
```
<token_string>,user,user_id,group_id
```
* The token file is then added to the `kube-apiserver` file using the following:
```
--token-auth-file=user-token-details.csv
```
* When authenticating, specify the token as an `Authorization: Bearer` token with the `curl` command:
```
curl -v -k https://master-node-ip:6443/api/v1/pods --header "Authorization: Bearer <token>"
```
* A basic authentication mechanism is not recommended.
* Considered using a volume mount while providing the auth file in a `kubeadm` setup.
* Setup role-based authorisation for new users.
* 