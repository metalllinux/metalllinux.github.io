---
title: "Image Security"
category: "cka-certification"
tags: ["cka-certification", "image", "security"]
---

* Start with a simple pod definition file:
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
  - name: nginx
	image: nginx
```
* Deploys an `nginx` container.
* What is the image and where is it pulled from?
* `image: nginx` --> the `nginx` part is the image/repository name.
	* When `nginx` is mentioned, it is actually `library/nginx`
	* If you don't provide a user / account name, the assumption is `libarary`.
	* The `library` images are ran by `docker` and they are the best when it comes to best practices for security
	* For your own account / repository, you remove the `library` part and add your own.
* Where are the images stored and pulled ffrom?
	* Since the location has not been specified, it is assumed the default registry is required, `docker.io`
		* DNS name is `docker.io`
* Google's registry is `gcr.io`.
* AWS / GCP provide an private registry by default.
* To run a private image, do the following:
	* Log into the private registry:
```
docker login private-registry.io
```
* Once successfully logged in, run the image from the private registry with:
```
docker run private-registry.io/apps/internal-app
```
* To implement a private registry in a Kubernetes pod definition file, run the following:
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
  - name: nginx
	image: private-registry.io/apps/internal-app
```
* How does Kubernetes get the credentials to access the private registry?
* How do you pass the credentials from the `docker` runtime to the worker nodes?
* Firstly, create a secret:
```
kubectl create secret docker-registry regcred --docker-server=private-registry.io --docker-username=registry-user --docker-password=registry-password --docker-email=registry-user@org.com
```
* The `regcred` part stores credentials.
* The secret is then defined in the pod definition file in the `imagePullSecrets`:
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
  - name: nginx
	image: private-registry.io/apps/internal-app
  imagePullSecrets:
  - name: regcred
```
* The secrets are then pulled. Add this in the definition file just under `spec:`
```
spec:
  imagePullSecrets:
  - name: <secret_name_here>
```