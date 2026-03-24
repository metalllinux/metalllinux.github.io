---
title: "Developing Network Policies"
category: "cka-certification"
tags: ["cka-certification", "developing", "network", "policies"]
---

* Example, have a Web Pod on port 80, an API Pod on port 5000 and a DB Pod on 3306
* Want to protect the DB Pod, so that no other pod can access it!
	* Except the `kube-apiserver` pod on port 3306
* Create a Network Policy for this:
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
  - Ingresss
  ingress:
  - from:
	- podSelector:
		  matchLabel
			name: api-pod
	  namespaceSelector:
		  matchLabels:
			name: prod
	- ipBlock:
		  cidr: 192.168.5.10/32
	ports:
	- protocol: TCP
	  port: 3306
```
* The label on the DB pod also has to be `db`.
* Do we require Ingress / Egress or both?
	* In this case we need an Ingress rule to allow traffic from the API pod.
	* Allows the API Pod to connect to the DB and run queries.
* When making rules, only need to be concerned about the direction that the request comes from?
* The rule listed above **does not** allow the DB Pod to connect to the API Pod.
	* That would be considered Egress traffic and would need to be specified.
* Each rule has a `from:` and `ports:` field - specify where the traffic is coming from.
* What if there are multiple API pods in the same cluster, with the same label, but in different namespaces?
	* In the above case, we only want to enable the API pod in the Prod namespace.
* What happens if you have the `namespaceSelector` instead of the `podSelectpr`
	* That means in the above example, all pods in the specified namespace will be able to reach the DB pod, not just the API Pod.
* `ipBlock` - allows all of these IPs to connect.
* Using the `podSelector` and the `ipBlock` is an `OR` - either one can be used.
* Adding a `-` before `namespaceSelector` makes it into a separate rule.
	* This is like an `AND` with the `podSe;ectpr` and `ipBlock`
* Example Egrees:
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
  - Ingresss
  - Egress
  ingress:
  - from:
	- podSelector:
		  matchLabel
			name: api-pod
	ports:
	- protocol: TCP
	  port: 3306
   egress:
   - to:
	  - ipBlock:
            cidr: 192.168.5.10/32
	  ports:
	  - protocol: TCP
		port: 80
```
* For example, an agent on the DB Pod is sending backups to the Backup Server on 192.168.5.10 on port `80`. The backup is external, therefore needs to be set via an `ipBlock`