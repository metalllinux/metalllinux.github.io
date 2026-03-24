---
title: "Introduction To Gateway Api"
category: "cka-certification"
tags: ["cka-certification", "introduction", "gateway", "api"]
---

* Regarding Ingress, this is usually two services sharing the same Ingress resource.
* What if services are managed by completely different organisations (for example with `/watch` and `/wear`, these are controlled by different groups).
* Underlying Ingress resource is still a single resource.
* Can only be managed by one team at a time.
* Ingress has no support for:
	* Multi-tenancy.
	* Namespace isolation
	* No RBAC for Features
	* No Resource Isolation
* Ingress only supports HTTP-based rules.
	* host matching
	* path matching
* Ingress does not support:
	* TCP/UDP routing
	* Traffic splitting / weighting
	* Header manipulation
	* Authentication
	* Rate limiting
	* Redirects
	* Rewriting
	* Middleware
	* WebSocket support
	* Custom error pages
	* Session affinity
	* Cross-origin resource sharing (CORS)
* Example Ingress configuration file:
```
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ingress-wear-watch
  annotations: wear.my-online-store.com
   nginx.ingress.kubernetes.io/ssl-redirect: "true"
   nginx.ingress.kubernetes.io/force-ssl-redirect: "true"

spec:

  rules:
  - host: wear.my-online-store.com
  http:
    paths:
    - path: /foo
      backend:
        serviceName: wear-service
        servicePort: 80
  - host: watch.my-online-store.com
    http:
      paths:
      - backend:
          serviceName: watch-service
          servicePort: 80
```
* `Annotations` are considered this part from the above config:
```
annotations: wear.my-online-store.com
   nginx.ingress.kubernetes.io/ssl-redirect: "true"
   nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
```
* `Host Matching` is considered the following:
```
  - host: watch.my-online-store.com
```
* `Path Matching` would be:
```
- path: /foo
```
* `HTTP Only` would be set under:
```
http:
```
* Differences in rules can also be seen in the following:
* NGINX:
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
   name: cors-ingress
   annotations:
     nginx.ingress.kubernetes.io/enable-cors: "true"
	 nginx.ingress.kubernetes.io/cors-allow-methods: "GET, PUT, POST"
	 nginx.ingress.kubernetes.io/cors-allow-origin: "https://allowed-origin.com"
	 nginx.ingress.kubernetes.io/cors-allow-credentials: "true"
```
* traefik
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: traefik-ingress
  annotations:
    # CORS Configuration
	traefik.ingress.kubernetes.io/headers/customresponseheaders: |
  Access-Control-Allow-Origin: '*'
  Access-Control-Allow-Methods: GET,POST,PUT,DELETE,OPTIONS
  Access-Control-Allow-Headers: Content-Type, Authorization
  Access-Control-Allow-Credentials: true
  Access-Control-Max-Age: 3600
```
* Gateway API is an official Kubernetes project - focuses on Layer 4 and Layer 7 routing.
	* Ingress has a lack of support for multi-tenancy.
* Example ingress yaml file:
```
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ingress-wear-watch
spec:

  rules:
  - host: wear.my-online-store.com
    http:
      paths:
	  - backend:
		  serviceName: wear-service
		  servicePort: 80
  - host: watch.my-online-store.com
    http:
      paths:
      - backend:
		  serviceName: watch-service
		  servicePort: 80
```
* In the above example, Team A would own:
```
- host: wear.my-online-store.com
    http:
      paths:
	  - backend:
		  serviceName: wear-service
		  servicePort: 80
```
* Then Team B would own:
```
- host: watch.my-online-store.com
    http:
      paths:
      - backend:
		  serviceName: watch-service
		  servicePort: 80
```
* Gateway API introduces three separate objects managed by three separate personas.
* Infrastructure Providers configure the `GatewayClass`.
	* `GatewayClass` defines what the underlying network infrastructure would be.
* Cluster Operators then configure the `Gateway` - these are instances of the `GatewayClass`.
* Finally for the Application Developers, we have `HTTPRoute`. We also have `TCPRoute` and `GRPCRoute`.
* How is the `GatewayClass` converted:
```
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: example-class
spec:
  controllerName: example.com/gateway-controller
```
* Similarly to `Ingress`, need to deploy a controller for the gateway as well.
* Next we have the `Gateway` object:
```
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: example-gateway
spec:
  gatewayClassName: example-class
  listeners:
  - name: http
	protocol: HTTP
	port: 80
```
* Finally we have the HTTP Route:
```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: example-httproute
spec:
  parentRefs:
  - name: example-gateway
  hostnames:
  - "www.example.com"
  rules:
  - matches:
    - path:
        type: PathPrefix
		value: /login
	backendRefs:
	- name: example-svc
	  port: 8080
```
* parentRefs matches requests with the hostname.
* HTTP traffic from example-gateway with the host header set to www.example.com and it will be routed to example-svc on port 8080.
* HTTPRoute is a Layer 7 protocol.
* Ingress vs. Gateway API:
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: secure-app
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
	nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
spec:
  tls:
  - hosts:
    - secure.example.com
	secretName: tls-secret
```
* The above is a basic TLS configuration. This is the native Ingress way.
* To ensure all traffic uses HTTPS, need to redirect that using the following:
```
nginx.ingress.kubernetes.io/ssl-redirect: "true"
```
* In contract, the `GatewayAPI` approach is much more structured. An example is below:
```
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: secure-gateway
spec:
  gatewayClassName: example -gc
  listeners:
  - name: https
    port: 443
    protocol: HTTPS
	tls:
	  mode: Terminate
	  certificateRefs:
	  - kind: Secret
		name: tls-secret
	allowedRoutes:
	  kinds:
      - kind: HTTPRoute
```
* Listeners clearly shows setting up HTTPS endpoint port 443, Specific on TLS and killing those on the gateway.
* Here is another example - a canary deployment and send 80% of the traffic to here with Ingress:
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: canary-ingress
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-weight: "20"
spec:
  rules:
  - http:
      paths:
      - path: /
		pathType: Prefix
		backend:
		  service:
			name: app-v2
			port:
			  number: 80
```
* The above config only works with Nginx, other controllers may not understand.
* Here is the GatewayAPI version:
```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: split-traffic
spec:
  parentRefs:
  - name: app-gateway
  rules:
  - backendRefs:
    - name: app-v1
      port: 80
      weight: 80
    - name: app-v2
      port: 80
      weight: 20
```
* In the above, no hidden primary config needed.
* Easily see traffic which is split. 80% is app-v1 and 20% is app-v2.
* Another HTTPRoute example:
```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: cors-route
spec:
  parentRefs:
  - name: my-gateway
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /api
    filters:
    # CORS configuration using response header modification
    - type: ResponseHeaderModifier
      responseHeaderModifier:
        add:
        - name: Access-Control-Allow-Origin
          value: "*"
		- name: Access-Control-Allow-Methods
		  value: "GET,POST,PUT,DELETE,OPTIONS"
		- name: Access-Control-Allow-Headers
		  value: "Content-Type, Authorization"
		- name: Access-Control-Allow-Credentials
		  value: "true"
		- name: Access-Control-Max-Age
   		  value: "3600"
	backendRefs:
	- name: api-service
```
* Most Controllers have implemented this - Amazon EKS, Google Kubernetes Engine, 