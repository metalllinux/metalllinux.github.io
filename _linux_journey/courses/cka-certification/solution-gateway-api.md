---
title: "Solution Gateway Api"
category: "cka-certification"
tags: ["cka-certification", "solution", "gateway", "api"]
---

* Which API resource is used to define a gateway in Kubernetes?
	* `Gateway`.
* What is the purpose of the `allowedRoutes` field in a Gateway?
	* To define which namespaces you can attach to it.
* Which of the following protocols is NOT supported by the Kubernetes Gateway API?
	* `ICMP`
* How does a GatewayClass differ from a Gateway?
	* GatewayClass defines how a Gateway is created via a controller.
* What is the primary advantage of using Gateway API over Ingress?
	* Supports more advanced routing and multi-protocol support.
* Using Gateway API and NGINX Gateway Fabric*
* Install the Gateway API resources:
```
kubectl kustomize "https://github.com/nginx/nginx-gateway-fabric/config/crd/gateway-api/standard?ref=v1.5.1" | kubectl apply -f -
```
* Deploy the NGINX Gateway Fabric CRDs:
```
kubectl apply -f https://raw.githubusercontent.com/nginx/nginx-gateway-fabric/v1.6.1/deploy/crds.yaml
```
* Deploy NGINX Gateway Fabric:
```
kubectl apply -f https://raw.githubusercontent.com/nginx/nginx-gateway-fabric/v1.6.1/deploy/nodeport/deploy.yaml
```
* Verify the Deployment:
```
kubectl get pods -n nginx-gateway
```
* View the nginx-gateway service:
```
kubectl get svc -n nginx-gateway nginx-gateway -o yaml
```
* Update the nginx-gateway service to expose ports 30080 for HTTP and 30081 for HTTPS:
```
kubectl patch svc nginx-gateway -n nginx-gateway --type='json' -p='[
  {"op": "replace", "path": "/spec/ports/0/nodePort", "value": 30080},
  {"op": "replace", "path": "/spec/ports/1/nodePort", "value": 30081}
]'
```
* Create a Kubernetes Gateway resource with the following specifications:

    Name: nginx-gateway
    Namespace: nginx-gateway
    Gateway Class Name: nginx
    Listeners:
        Protocol: HTTP
        Port: 80
        Name: http
        Allowed Routes: All namespaces
* Deploy the following to create a Gateway Resource:
```
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: nginx-gateway
  namespace: nginx-gateway
spec:
  gatewayClassName: nginx
  listeners:
    - name: http
      port: 80
      protocol: HTTP
      allowedRoutes: 
       namespaces: 
        from: All
```
```
kubectl apply -f gateway.yaml
```
* Verify the deployment:
```
kubectl get gateways -n nginx-gateway
```
* A new pod named frontend-app and a service called frontend-svc have been deployed in the default namespace. Expose the service on the / path by utilising an HTTPRoute named frontend-route.

Is the frontend-route created?

Is the svc exposed to outside world?
* View the pods and services in the default namespace:
```
kubectl get pod,svc
```
* Expose the service to the outside world, using an HTTPRoute:
```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: frontend-route
  namespace: default
spec:
  parentRefs:
  - name: nginx-gateway
    namespace: nginx-gateway
    sectionName: http 
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /
    backendRefs:
    - name: frontend-svc
      port: 80
```
* Deploy:
```
kubectl apply -f frontend-route.yaml
```