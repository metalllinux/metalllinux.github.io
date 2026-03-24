---
title: "Labels And Selectors"
category: "cka-certification"
tags: ["cka-certification", "labels", "selectors"]
---

* Standard method to group things together.
* For example a set of different specifies and filter them on their criteria (colour, bird, etc).
* Add properties to each itme.
	* For example, `class = mammal`
* In Kubernetes, you will need labels to group objects by their type, application or their functionality.
* Example of a labels for an `App1` pod --> `app`
* Example of a label for another pod called `Front-end` --> `function`
* For `Selectors`, filter by a specific condition, for example `app = App1`
* How do you specify labels in Kubernetes? Under the `pod-definition.yaml` file, specify the following:
```
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp
  labels:
      app: App1
      function: Front-en
spec:
  containers:
  - name: simple-webapp
    image: simple-webapp
    ports:
      - containerPort: 8080
```
* Add the `labels` in a key-value format.
* Once the pod is created, to select the pod by a particular label, use the following command:
```
kubectl get pods --selector app=App1
```
* Kubernetes uses labels and selectors internally, to connect different objects together.
* For example, to create a ReplicaSet, this is an example file:
```
apiVersion: apps/v1
kind: Replicaset
metadata:
  name: simple-webapp
  labels:
    app: App1
    function: Front-end
spec:
  replicas: 3
  selector:
    matchLabels:
      app: App1
  template:
    metadata:
      labels:
        app: App1
        function: Front-end
    spec:
      containers:
      - name: simple-webapp
        image: simple-webapp
```
* In the above file, the `labels` defined under the `template` section are the `labels` configured on the pods.
* The `labels` under `metadata` are those under the replicaset itself.
* We are trying to get the replicaset to discover the pods, so not interested in the `labels` under `metadata`.
* To connect the replicaset to the pod, we configure the selector field under the replicaset specification, to match the `labels` defined on the pod.
	* These are the `labels` that are under the `template` field.
* On creation, when the `labels` under `matchLabels` and under `template` --> `labels` match successfully, then the replicaset is created.
* It works the same for other objects such as a `service`.
* When the `service` is created, such as in the example below:
```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: App1
  ports
  - protocol: TCP
    port: 80
    targetPort: 9376 
```
* When a service is created, it uses the `selector` in the service definition file to match the labels set on the pods in the replicaset definition file (the same file as above, under `matchLabels` and `metadata` --> `labels`)
* Annotations - used to record other details, like build version, emails etc. Example using Annotations:
```
apiVersion: apps/v1
kind: Replicaset
metadata:
  name: simple-webapp
  labels:
    app: App1
    function: Front-end
  annotations:
    buildversion: 1.14
spec:
  replicas: 3
  selector:
    matchLabels:
      app: App1
  template:
    metadata:
      labels:
        app: App1
        function: Front-end
    spec:
      containers:
      - name: simple-webapp
        image: simple-webapp
```