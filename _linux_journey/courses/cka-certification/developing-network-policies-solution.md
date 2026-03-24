---
title: "Developing Network Policies Solution"
category: "cka-certification"
tags: ["cka-certification", "developing", "network", "policies", "solution"]
---

* How to check the amount of network policies available:
```
kubectl get networkpolicy
```
or
```
kubectl get netpol
```
* Describe a network policy with the following:
```
kubectl describe networkpolicy payroll-policy
```
* Create a network policy to allow traffic from the `Internal` application only to the `payroll-service` and `db-service`:
```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: internal-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      name: internal
  policyTypes:
  - Egress
  - Ingress
  ingress:
    - {}
  egress:
  - to:
    - podSelector:
        matchLabels:
          name: mysql
    ports:
    - protocol: TCP
      port: 3306

  - to:
    - podSelector:
        matchLabels:
          name: payroll
    ports:
    - protocol: TCP
      port: 8080

  - ports:
    - port: 53
      protocol: UDP
    - port: 53
      protocol: TCP
```