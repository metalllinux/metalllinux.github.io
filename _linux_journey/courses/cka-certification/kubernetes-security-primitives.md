---
title: "Kubernetes Security Primitives"
category: "cka-certification"
tags: ["cka-certification", "kubernetes", "security", "primitives"]
---

* Kubernetes is the go-to platform for production grid applications.
* The hosts themselves must be secured:
	* Password-based authentication is disabled.
	* Only `ssh` key-based authentication is enabled.
	* Other physical security considerations.
* The `kube-apiserver` is the centre of all operations with Kubernetes.
	* Can interact it with the `kubectl` utility or through accessing the API directly.
* First line of defence is controlling any access to the `kube-apiserver` itself.
	* Who can access the cluster?
	* What can they do?
* Who can access?
	* Files - Usernames and Passwords
	* Files - Username and Token
	* Certificates
	* External Authentication Providers - LDAP
	* Service Accounts
* What can the users when accessing the cluster via the above methods do?
	* RBAC Authorisation - users assigned to specific groups with X permissions.
	* ABAC Authorisation (Attribute Based Access Control).
	* Node Authorisation
	* Webhook Mode
* All communication within the cluster, such as with the `ETCD` cluster, `Kubelet` (worker node), `Kube Proxy` (worker node), `Kube Scheduler` and `Kube Controller Manager` is done using TLS encryption and certificates.
* How about communication between applications within the cluster - by default all applications can access each other in the cluster.
	* Can restrict access between them using network policies.