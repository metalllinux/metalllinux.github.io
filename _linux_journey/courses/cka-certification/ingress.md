---
title: "Ingress"
category: "cka-certification"
tags: ["cka-certification", "ingress"]
---

* For example, deploying an application for a company selling products.
* Build the application into a `docker` image and deploy it on the cluster as a pod.
	* The application requires a database, therefore deploy a MySQL database as a pod.
	* Create a service of type `ClusterIP`. The service is called `mysql-service` and therefore makes the `mysql` pod accessible to the Application.
* To make the Application itself accessible to the outside world, create another service of type `NodePort`. The Application is made available via a high port `38080` on the nodes in the cluster.
	* The users can then successfully access the application, by navigating to `http://<node-ip>:38080`
* When traffic increases, the number of `replicas` of the Application (not the `mysql` pod) also increases to handle the additional traffic. The Application's service also handles the additional replicas and splits the traffic between the three pods.
* We don't want the users to type in the address every time.
	* Therefore, configure DNS server to point to the IP of the nodes.
* The service takes care of splitting traffic between the pods.
* Don't want users to type in IP of node every time, thus configuring the DNS server to point to the node's IP address and the port.
* Service Node ports can only allocate high-numbered ports, that are greater than `30,000`.
	* To get around this, use a proxy-server --> It proxies requests on port `80` for example and forwards the requests to port `38080`.
	* Then point the DNS to the proxy server and thus, the Node IP AND the port are not needed to be specified in the URL anymore.
		* The above points work if the application is hosted on-prem on in a data centre.
* With a cloud platform however such as GCP, the above is not possible.
	* Instead, set the service to type `LoadBalancer` instead of `NodePort`.
	* Kubernetes would send a request to GCP or whichever cloud service and provision a loadbalancer for the service.
	* Then GCP as an example would create a separate load-balancer on a port (`80` for example).
		* The load-balancer has an external IP, that can be provided to users to access the application.
		* Set the DNS to point to the IP and specify the URL that needs to be used.
* Another example is if you have two websites, one called `my-online-store.com/wear` and `my-online-store.com/watch`. How do you keep both running?
	* The developers keep working on the new application.
	* To share the cluster's resources, deploy the application within the same cluster.
	* Create a `LoadBalancer` called `video-service`
	* For the `video-service` `LoadBalancer`, Kubernetes provisions a new load-balancer called `gcp load-balancer-2` and assigns it to port `38282`.
		* The new loadbalancer has a new IP.
		* Having many loadbalancers however affects your cloud bill.
	* How do you direct traffic between each of the loadbalancers, based on the URL the user types in?
		* Need another load-balancer / proxy based on the URLs to the different services.
		* When a new service is introduced, need to reconfigure the load-balancer.
		* Need to enable SSL for applications as well - users can then access applications via HTTPS.
			* How do you configure HTTPS in the application?
			* Can be done at the Application or loadbalancer or proxy server level.
				* Don't want developers to implement this into their applications, as they'll do it in different ways.
					* Additional burden for them with code.
			* Difficult to manage when application scales. For each service, a new cloud native loadbalancer needs to be provisioned.
* Best to add this to the Kubernetes cluster.
	* Ingress helps your users access your application - using a single externally accessible URL.
		* You can configure this to route traffic to different services.
			* Route traffic to different services in the cluster, based on the URL path.
			* Implement the SSL security as well.
	* Ingress is a layer7 load-balancer.
		* This is built-in to the Kubernetes cluster.
	* Need to expose Ingress for it to be accessible outside the cluster.
		* Have to publish it as a NodePort
		* Or with a cloud native load-balancer.
		* Configure all load-balancing configurations on the ingress controller.
* Without Ingress, you can use a reverse proxy solution such as Nginx HAProxy or Traefik.
	* These solutions are called Ingress Controllers.
		* Other Controllers include GCE (Google's Layer 7 HTTP Load Balancer), nginx, Contour, HAProxy, Traefik, Istio
			* GCE and Nginx are being maintained by the Kubernetes project.
		* These Ingress Controllers aren't just another Load Balancer or Nginx server. LoadBalancers are just one part of them.
			* Controllers also monitor the cluster for new definitions or Ingress resources and configure the Nginx server accordingly.
	* The set of rules you configure are called Ingress Resources.
		* The resources are created via definition files (same ones for creating pods etc).
		* Deploy them on the Kubernetes cluster and configure them to route traffic to other services.
	* Configuration involves URL routes, SSL certificates and more.
	* Ingress is implemented by Kubernetes.
* Kubernetes cluster does not come with an Ingress Controller by default.
* An Nginx Controller is deployed similarly to a Deployment in Kubernetes.
* An example definition file:
```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-ingress-controller
spec:
  replicas: 1
  selector:
    matchLabels:
	  name: nginx-ingress
  template:
	metadata:
      labels:
		name: nginx-ingress
	spec:
	  containers:
		- name: nginx-ingress-controller
  		  image: quay.io/kubernetes-ignress-controller/nginx-ingress-controller:0.21.0
	  args:
		- /nginx-ingress-controller
```
* The above nginx image is a specific build of Nginx, to be used specifically as a Controller.
* The Nginx Controller is located at `/nginx-ingress-controller` and that starts the Controller service.
* Nginx has the following functionality:
	* Path to store error logs --> `err-log-path`
	* `keep-alive`
	* `ssl-protocols`
	* Session timeout.
* To decouple the above functionality from the `nginx-ingress-controller` image, must create a `ConfigMap` for that to go into:
```
kind: ConfigMap
apiVersion: v1
metadata:
  name: nginx-configuration
```
* The ConfigMap object does not need any entries at this point.
* Adding the ConfigMap to the `nginx-ingress-controller` looks like the below:
* Need to also pass in two environment variables as well:
* Ports used by the Ingress Controller are `80` and `443`
```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-ingress-controller
spec:
  replicas: 1
  selector:
    matchLabels:
	  name: nginx-ingress
  template:
	metadata:
      labels:
		name: nginx-ingress
	spec:
	  containers:
		- name: nginx-ingress-controller
  		  image: quay.io/kubernetes-ignress-controller/nginx-ingress-controller:0.21.0
	  args:
		- /nginx-ingress-controller
		- --configmap=$(POD_NAMESPACE)/nginx-configuration

     env:
       - name: POD_NAME
         valueFrom:
		   fieldRef:
			 fieldPath: metadata.name
	   - name: POD_NAMESPACE
		 valueFrom:
		   fieldRef:
			 fieldPath: metadata.namespace

     ports:
       - name: http
		 containerPort: 80
	   - name: https
		 containerPort: 443
```
* Also need a service to expose the Controller to the external world.
	* Therefore create a service of type NodePort:
```
apiVersion: extensions/v1beta1
kind: Service
metadata:
  name: nginx-ingress
spec:
  type: NodePort
  ports:
  - port: 80
	targetPort: 80
	protocol: TCP
    name: http
  - port: 443
	targetPort: 443
	protocol:TCP
	name: https
  selector:
	name: nginx-ingress
```
* We add the `nginx-ingress` `selector` above to link the service to the Deployment.
* Ingress controllers have additional intelligence built into them.
	* They configure the underlying nginx server when something is changed.
	* To do this, a service account is required:
```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: nginx-ingress-serviceaccount
```
* To summarise, the Ingress Controller has the following:
	* Deployment
	* Service
	* ConfigMap
	* Auth
	* Roles, ClusterRoles and RoleBindings as well.
* What is an Ingress Resource?
	* Set of rules and configurations appleid on the Ingress Controller.
		* Can configure rules, for example:
			* Forward all incoming traffic to a single application or route traffic to different applications, based on the URL.
			* For example, my-online-store.com has two web pages, `/wear` and `/watch`. Navigating to `/wear` brings the user to the `/wear` web application in Kubernetes. `/watch` similarly brings you to the `/watch` web application in Kubernetes.
* The Ingress Resource is configured via a YAML file. For example:
```
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ingress-wear-watch
spec:
  backend:
      serviceName: wear-service
      servicePort: 80
```
* When deploying Ingress, refer to the Kubernetes documentation.
* If it is a simple backend, create the definition file like the above example.
* Create the Ingress as usual with the `kubectl create` command:
```
kubectl create -f Ingress-wear.yaml
```
* Check `ingress` with:
```
kubectl get ingress
```
* In the above example, Ingress is now created. It routes all incoming traffic to the `wear` service.
* Use Rules when wanting to route traffic based on different conditions.
* Ingress Resource - Rules
	* For example with a website, this can be split into different rules:
		* www.my-online-store.com - Rule 1
		* www.wear.my-online-store.com - Rule 2
		* www.watch.my-online-store.com - Rule 3
		* Everything Else - Rule 4
* Can get different domain names to reach cluster, add multiple DNS entries and point to same Ingress Controller service.
* Rule 1 - can set that to navigate to the `wear` or `watch` web application: www.my-online-store.com/wear
	* Anything else outside of that is sent to a 404 page.
* Rule 2, for example you have a URL that looks like this: wear.my-online-store.com and then wear.my-online-store.com/returns or wear.my-online-store.com/support.
* Rule 3 - show films and TV.
* Rule 4 - all traffic is sent to a 404 error.
* Another example definition file:
```
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ingress-wear-watch
spec:
  rules:
  - http:
	  paths:
      - path: /wear
	    backend:
          serviceName: wear-service
          servicePort: 80
      - path: /watch
        backend:
          serviceName: wear-service
          servicePort: 80
```
* How to view additional details about the Ingress resource:
```
kubectl describe ingress ingress-wear-watch
```
* From the output of the above command - user is directed and specified to the default backend, details.
* Third type of configuration is around hostnames:
```
Ingress-wear-watch.yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
   name: ingress-wear-watch
spec:
  rules:
  -
    http:
      paths:
      - backend:
          service Name: wear-service
          servicePort 0
  -
    http:
      paths:
       - backend:
		    serviceName: watC
```
* Host field in each rule specifies the right value.
* Can have mutliple path.