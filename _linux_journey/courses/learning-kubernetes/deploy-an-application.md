---
title: "Deploy An Application"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "deploy", "application"]
---

* Kubernetes is designed to make application highly available.
	* That is why there are multiple replications and essentially multiple applications running at the same time.
	* If one stops working, then at least two others are accepting traffic.
* Pods are the Kubernetes resource that run our applications and microservices.
	* To make sure an applicaiton is highly available, is to organise your pods in a Kubernetes cluster.
* Example deployment.yaml:
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
* `apiVersion: apps/v1` --> This is the API group we are sending the request to.
* `kind: Deployment` --> This is the kind of Kubernetes object we want to create.
* The next section is `metadata`:
```
metadata:
  name: pod-info-deployment
  namespace: development
  labels:
    app: pod-info
```
* In the `metadata` section, the deployment name is `pod-info-deployment` . We are specifying that the pods should be in the `development` namespace. All pods in this group are labelled with the `app` name of `pod-info`.
* To make the applications highly available.
	* Under `spec`, we can specify how many replicas of the particular container that we want to run.
* At the following, we have:
```
    spec:
      containers:
      - name: pod-info-container
        image: kimschles/pod-info-app:latest
        ports:
        - containerPort: 3000
```
* The above are the specifics about the particular container that we want to run in the pod.
	* The name is `pod-info-container`
	* The image is from the authors Docker Hub Registry, which is `kimschles/pod-info-app:latest`.
	* The port for the traffic is going to be `3000`, this is where the traffic is directed.
* Then we have the environment variables of the container:
```
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
* Get the list of namespaces with `kubectl get ns`
* In this case, need to make sure the `development` namespace is applied first. This is again done with:
```
kubectl apply -f <yaml file>
```
* Then we apply the `deployment.yml` file with:
```
kubectl apply -f deployment.yml
```
* To list all of the deployments in the development namespace, we can do:
```
kubectl get deployments -n development
```
* The `-n` is for namespace.
* To check the pods that the delopment created, we can do:
```
kubectl get pods -n development
```
* To delete a pod, we do:
```
kubectl delete pod pod-info-deployment-7587d5cc86-9cm4t -n development
```
* The pod in the `development` namespace will now be deleted.
* There will be a new pod created however, as the Kubernetes deployment will always create 3 pods.