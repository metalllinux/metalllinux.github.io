---
title: "Services Load Balancer"
category: "cka-certification"
tags: ["cka-certification", "services", "load", "balancer"]
---

* Node ports help forward traffic to the respective pods.
	* Am able to access the applications using the IP of any of the nodes and the port.
		* However, users want one URL to navigate to to access the application.
* A solution is to create a VM to act as a load balancer, using `nginx` or similar tools.
	* Then routing traffic from the load balancer to the specific nodes.
	* Can also use cloud platforms such as Google Cloud Platform and AWS
	* The Front-End services would be set to `type: LoadBalancer`. The `service-definition.yml` file would look like the following and is **Only supported on certain cloud platforms**:
```
apiVersion: v1
kind: Service
metadata:
    name: myapp-service

spec:
	type: LoadBalancer
    ports:
	 - targetPort: 80
		port: 80
		nodePort: 30008
```
* Good example service definition file:
```
---
apiVersion: v1
kind: Service
metadata:
  name: webapp-service
  namespace: default
spec:
  ports:
  - nodePort: 30080
    port: 8080
    targetPort: 8080
  selector:
    name: simple-webapp
  type: NodePort
```
* You would then apply the file with `kubectl apply -f <filename>` / `kubectl create -f <filename>`