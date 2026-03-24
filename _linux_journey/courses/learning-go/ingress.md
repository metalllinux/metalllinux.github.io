---
title: "Ingress"
category: "learning-go"
tags: ["learning-go", "ingress"]
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
	* These solutions are called Ingress controllers.
	* The set of rules you configure are called Ingress Resources.
		* The resources are created via definition files (same ones for creating pods etc).
		* Deploy them on the Kubernetes cluster and configure them to route traffic to other services.
	* Configuration involves URL routes, SSL certificates and more.
	* Ingress is implemented by Kubernetes.
	* 