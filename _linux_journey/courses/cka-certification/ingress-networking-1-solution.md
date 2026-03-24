---
title: "Ingress Networking 1 Solution"
category: "cka-certification"
tags: ["cka-certification", "ingress", "networking", "solution"]
---

* Namespace for the Ingress Controller is in `nginx-ingress`
* What is the name of the Ingress Controller deployment?
	* Find this out with `kubectl get deploy -A` / `kubectl get deploy --all-namespaces`
	* The answer here was `ingress-nginx-controller`
* How to find how many applications are deployed in a particular namespace:
```
kubectl get deploy -A
```
* How to find the host configured on the Ingress Resource? Run `kubectl describe ingress --namespace app-space` and then check under the `Rules` section for `Host`.
	* A star under `Host` means this affects all hosts.
* How to check the backend and see which permission
```
kubectl describe ingress --namespace app-space
```
* Then check under the `rules`.
* If the requirement listed there does not match any of the configured paths in the Ingress, to which service is the request forwarded too?
	* `default-backend-service` is the answer here.
* How to change the URL at which an application is made available:
* Use this manifest file:
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
  name: ingress-wear-watch
  namespace: app-space
spec:
  rules:
  - http:
      paths:
      - backend:
          service:
            name: wear-service
            port: 
              number: 8080
        path: /wear
        pathType: Prefix
      - backend:
          service:
            name: video-service
            port: 
              number: 8080
        path: /stream
        pathType: Prefix
```
* Then apply this with `kubectl create -f <name>`.
	* How to add a new path to the Ingress, that is customer-facing.
* Here is the manifest file to deploy for that:
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
  name: ingress-wear-watch
  namespace: app-space
spec:
  rules:
  - http:
      paths:
      - backend:
          service:
            name: wear-service
            port: 
              number: 8080
        path: /wear
        pathType: Prefix
      - backend:
          service:
            name: video-service
            port: 
              number: 8080
        path: /stream
        pathType: Prefix
      - backend:
          service:
            name: food-service
            port: 
              number: 8080
        path: /eat
        pathType: Prefix
```
* Example manifest file to make the application available at `/pay`:
```
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: test-ingress
  namespace: critical-space
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
spec:
  rules:
  - http:
      paths:
      - path: /pay
        pathType: Prefix
        backend:
          service:
           name: pay-service
           port:
            number: 8282
```