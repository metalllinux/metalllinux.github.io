---
title: "Multi Container Pods"
category: "cka-certification"
tags: ["cka-certification", "multi", "container", "pods"]
---

* Splitting a monolithic thing into microservices allows for reusable code.
	* We can scale up, down and modify each service as required - no need to modify the entire application.
* Need one web server with each log agent.
* That is why multi-container pods are created together and destroyed together.
	* Can refer to each other as local host.
	* Have the same shared volumes.
* To create a multi-container pod, add the following to the pod definition file:
```
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp
  labels:
    name: simple-webapp
spec:
  containers:
  - name: simple-webapp
	image: simple-webapp
	ports:
      - containerPort: 8080
```
* The hypens added in the above definition file represent an array. Therefore you can add multiple containers.
* For example adding a new container:
```
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp
  labels:
    name: simple-webapp
spec:
  containers:
  - name: simple-webapp
	image: simple-webapp
	ports:
      - containerPort: 8080

  - name: log-agent
	image: log-agent
```
