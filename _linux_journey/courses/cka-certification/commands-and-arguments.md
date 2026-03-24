---
title: "Commands And Arguments"
category: "cka-certification"
tags: ["cka-certification", "commands", "arguments"]
---

* This is in a Kubernetes pod.
* Firstly we create a pod using the following image: `docker run --name ubuntu-sleeper ubuntu-sleeper 10`
* Then we place that into a pod definition file:
```
apiVersion: v1
kind: Pod
metadata:
 name: ubuntu-sleeper-pod
spec:
  containers:
    - name: ubuntu-sleeper
      images: ubuntu-sleeper
      args: ["10"]
```
* Then we create this with `kubectl -f pod-definition.yml`.
* The above pod definition file looks like the following in a Docker image:
```
FROM Ubuntu
ENTRYPOINT ["sleep"]
CMD ["5"]
```
* To change this further, in the `Docker` world the following is ran:
```
docker run --name ubuntu-sleeper \
     --entrypoint sleep2.0 ubuntu-sleeper 10
```
* The same pod definition file as the above command looks like this:
```
apiVersion: v1
kind: Pod
metadata:
 name: ubuntu-sleeper-pod
spec:
  containers:
    - name: ubuntu-sleeper
      images: ubuntu-sleeper
	  command: ["sleep2.0"]
      args: ["10"]
```
* The `command` field corresponds to an `ENTRYPOINT` in `docker`.
* The `args` field corresponds to the `CMD` field in `docker`.