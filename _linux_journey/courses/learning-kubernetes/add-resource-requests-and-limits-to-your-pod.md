---
title: "Add Resource Requests And Limits To Your Pod"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "add", "resource", "requests", "limits"]
---

* Well configured containers let Kubernetes know how much CPU and RAM to assign to a worker node.
* `resources` refer to the amount of CPU and memory for the `worker` node running your pods.
* If you deploy a pod without a set of resource requests, it can be scheduled on a node that does not have enough processing power or memory. The node can fail because of this.
* You can also start a pod on a node, but the application can use all of the resources on the node, causing it to fail. This causes outages.
* How to add resource requests and limits to our pod info container.
* Example resource limitation yaml file:
```
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```
* We can add this to the deployment.yaml file like so:
```
--- 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: pod-info-deployment
  namespace: development
  labels:
    app: pod-info
spec:
  replicas: 1
  selector:
    matchLabels:
      app: pod-info
  template:
    metadata:
      labels:
        app: pod-info
    spec:
      containers:
      - name: pod-info-container
        image: kimschles/pod-info-app:latest
		    resources:
				  requests:
					  memory: "64Mi"
					  cpu: "250m"
				  limits:
					  memory: "128Mi"
					  cpu: "500m"
        ports:
        - containerPort: 3000
        env:
          - name: POD_NAME
            valueFrom:
              fieldRef:
                fieldPath: metadata.name
          - name: POD_NAMESPACE
            valueFrom:
              fieldRef:
                fieldPath: metadata.namespace
          - name: POD_IP
            valueFrom:
              fieldRef:
                fieldPath: status.podIP
```
* Now, we have set resource requests and limits for the pod-info container.
* To explain the `resources` sequence:
	* The `request` section says to not schedule the pod, unless the node has at least  64Mi (Mi is mebibyte). A mebibyte is `1,048,576 bytes`.
	* It also needs 250m of CPU. `m` is for `milliCPU`.
	* The `limits` section says to stop using this container, if it exceeds `128Mi` of memory and `500m` of CPU.
* How do you decide on these values, it depends on the container you are running in the pod.
* To update the pods, we then run:
```
kubectl apply -f deployment.yaml
```
* If you receive an output such as:
```
myuser@myhost:~$ kubectl get pod -n development
NAME                                   READY   STATUS        RESTARTS      AGE
pod-info-deployment-7587d5cc86-lkccq   1/1     Terminating   1 (25h ago)   4d19h
pod-info-deployment-7587d5cc86-vk6br   1/1     Running       1 (25h ago)   4d19h
pod-info-deployment-7587d5cc86-zs4kp   1/1     Terminating   1 (25h ago)   4d19h
```
* The old `pod-info` deployment pods are terminating.
* New `pod-info` deployment pods are running and this is because we ran the `deployment.yaml` script again.
	* These new pods would have the resource requests and limits.
	* Important step to avoid outages.