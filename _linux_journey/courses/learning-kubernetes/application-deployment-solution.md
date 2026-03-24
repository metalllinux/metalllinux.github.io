---
title: "Application Deployment Solution"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "application", "deployment", "solution"]
---

* Create a new deployment in the file `quote.yaml`.
* `quote.yaml` looks like this:
```
--- 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: quote-service
  namespace: development
  labels:
    app: quote-service
spec:
  replicas: 2
  selector:
    matchLabels:
      app: quote-service
  template:
    metadata:
      labels:
        app: quote-service
    spec:
      containers:
      - name: quote-container
        image: datawire/quote:0.5.0
        ports:
        - containerPort: 8080
```
* Next challenge is to name the deployment and name the app label as `quote-service`.
	* That would mean setting the name to the following:
```
metadata:
  name: quote-service
```
* The app label in this case would be:
```
labels:
    app: quote-service
```
* Remember to change that label for all of the `app` fields.
* Next is to use the `development` namespace and that has already been completed here:
```
  namespace: development
```
* Next requirement is to change the container name, which is:
```
    spec:
      containers:
      - name: quote-container
```
* We want to run two replicas and this is done by:
```
spec:
  replicas: 2
```
* Use the image `datawire`, service by Ambassador Labs that generates random quotes.
```
        image: datawire/quote:0.5.0
```
* We then create the pods using `kubectl apply -f quote.yaml`
* Check `kubectl get pods -n development`.
* How to use `BusyBox` to check the app works.
	* `kubectl exec -it <busybox pod name> -- /bin/sh`
	* Use `wget` to send a request to the pods.
		* Get the IP addresses with:
			* `kubectl get pods -n development -o wide`
			* `wget <pod ip>:8080`
				* If you get `can't open 'index.html': File exits`
					* Check if the file is already in the busy box environment with `ls`
					* Remove the `index.html` file and then run the command again.