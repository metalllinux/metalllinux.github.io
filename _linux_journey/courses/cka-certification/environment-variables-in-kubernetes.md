---
title: "Environment Variables In Kubernetes"
category: "cka-certification"
tags: ["cka-certification", "environment", "variables", "kubernetes"]
---

* Example pod definition file:
```
apiVersion: v1
kind: Pod
metadata:
  name: simple-web-color
spec:
  containers:
  - name: simple-webapp-color
    image: simple-webapp-color
	ports:
      - containerPort: 8080
```
* `docker run` command:
```
docker run -e APP_COLOR=pink simple-webapp-color
```
* To set an environment variable, use the `env` property:
```
apiVersion: v1
kind: Pod
metadata:
  name: simple-web-color
spec:
  containers:
  - name: simple-webapp-color
    image: simple-webapp-color
	ports:
      - containerPort: 8080
	env:
      - name: APP_COLOR
	    value: pink
```
* `env` is an array
* There are other ways to specify environment variables - `ConfigMaps` and `Secrets`
* The difference with `ConfigMap` is:
```
env:
  - name: APP_COLOR
	valueFrom:
		 configMapKeyRef:
```
* The difference with a `Secret` is:
```
env:
  - name: APP_COLOR
    valueFrom:
		 secretKeyRef:
```