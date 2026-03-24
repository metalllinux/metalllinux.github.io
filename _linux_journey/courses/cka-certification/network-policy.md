---
title: "Network Policy"
category: "cka-certification"
tags: ["cka-certification", "network", "policy"]
---

* Good setup --> 80 to a server, that goes to port 5000 on the kube-api server and then to the database on port 3306
* Ingress - incoming traffic from users.
* Outgoing request to app server is the Egress traffic.
	* Only looking at direction in which traffic originated.
* Rules:
	* Ingress - allow HTTP traffic on Port 80.
	* Egress - allow traffic on Port 5000 to the web server.
	* Ingress - Port 5000 - traffic coming in from the kube-api server.
	* Egress - Port 3306 - traffic going to the kube-api server.
	* Ingress - Port 3306 - traffic coming in to the database server.
* Each node and each pod and service has its own IP address.
	* The pods can communicate with each other without have to create additional settings such as routes.
	* Configured by default with an `All Allow` rule that allows traffic from any pod to any other pod or service in the cluster.
* In the above example, a pod is assigned for the web server, one for the API server and one for the database.
* What if you don't want the web server to not allow to connect directly to the database server.
* A Network Policy is another thing in the Kubernetes Objects.
	* Link a Network Policy to one or more pods.
	* Example policy is `Allow Ingress Traffic From API Pod on Port 3306`
	* Only applicable to the pod that it is applied to.
* To do this, need to label the pod:
```
podSelector:
  matchLabels:
     role:db
```
* Database Pod:
```
labels:
  role: db
```
* Then specify the policy rules in a definition file:
```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: db-policy
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  ingress:
  - from:
	- podSelector:
		matchLabels:
		  name: api-pod
	ports:
	- protocol: TCP
      port: 3306
```
* Ingress or Egress only comes into affect if you have those in the `policyTypes` section.
	* Otherwise there is no isolation.
* Solutions that Support Network Policies:
	* kube-router
	* calico
	* romana
	* weave-net
* Solutions that DO NOT Support Network Policies:
	* flannel