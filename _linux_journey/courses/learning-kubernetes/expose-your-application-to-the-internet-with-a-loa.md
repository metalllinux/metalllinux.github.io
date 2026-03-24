---
title: "Expose Your Application To The Internet With A Loa"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "expose", "your", "application", "internet"]
---

* To expose an application to the Internet, you need to use a `kubernetes service`.
* A `kubernetes service` is a loadbalancer that directs traffic from the Internet to the Kubernetes Pods.
* A loadbalancer service has a **public** and **static** IP address.
* The static IP is important, as pods and their IPs change frequently.
	* The `service` IP needs to remain the same.
* Example `yaml` manifest for a service:
```
---
apiVersion: v1
kind: Service
metadata:
  name: demo-service
  namespace: development
spec:
  selector:
    app: pod-info
  ports:
    - port: 80
      targetPort: 3000
  type: LoadBalancer
```
* Very important part of the above `yaml` is the:
```
selector:
    app: pod-info
```
* That sends traffic to any pods with the label `pod-info`.
* All the pods deployed in the `deployment.yaml` file also need the label `pod-info`.
	* If they do not have this, they will not be able to direct traffic to the pods.
* In the `service.yaml` file, we set the `port` to `80`, so that the `port` does not need to be typed in the URL:
```
  ports:
    - port: 80
```
* The service however is directing traffic to port `3000` in the container:
```
targetPort: 3000
```
* Finally, we are specifying that the service `type` is a `loadbalancer`:
```
  type: LoadBalancer
```
* A `LoadBalancer` is one type of Kubernetes service. There are in fact 3 types of services:
	* `LoadBalancer`
	* `NodePort`
	* `ClusterIP`
* Another command is `minikube tunnel`. This shows an output similar to:
```
Status:	
	machine: minikube
	pid: 69570
	route: 10.96.0.0/12 -> 192.168.49.2
	minikube: Running
	services: []
    errors: 
		minikube: no errors
		router: no errors
		loadbalancer emulator: no errors
```
* This allows minikube to access the external network. Exposes the application to the Internet.
	* `ctrl + c` to stop the service.
* We create the service with:
```
kubectl apply -f ./Ex_Files_Learning_Kubernetes/Exercise\ Files/04_01/service.yaml
```
* Running `kubectl get services -n development`, then shows the internal IP as `CLUSTER-IP` and the external IP as `EXTERNAL-IP`
* If you create a Kubernetes cluster on AWS, Azure, GCP etc, they provide you with a public IP address.
* For example, copy and paste the external IP into your browser and you will see the JSON object: `10.101.236.59` like so:
```
{"pod_name":"pod-info-deployment-7587d5cc86-vk6br","pod_namespace":"development","pod_ip":"10.244.0.9"}
```
