---
title: "Managing Application Logs"
category: "cka-certification"
tags: ["cka-certification", "managing", "application", "logs"]
---

* Useful docker command that generates random events:
```
docker run kodekloud/event-simulator
```
* Events streamed.
* To run the application in the background, use the `docker run -d` flag
* To follow the log trail, use `docker logs -f <container_id>`
* In Kubernetes, the above can be done as well.
* Create a yaml file called `event-simulator.yaml`:
```
apiVersion: v1
kind: Pod
metadata:
  name: event-simulator-pod
spec:
  containers:
  - name: event-simulator
    image: kodekloud/event-simulator
```
* Then deploy the above with `kubectl create -f event-simulator.yaml`
* Then logs can then be followed with `kubectl logs -f event-simulator`
* The command is specific to the container running inside the pod.
* In the event one pod has multiple containers, like in the below example:
```
apiVersion: v1
kind: Pod
metadata:
  name: event-simulator-pod
spec:
  containers:
  - name: event-simulator
    image: kodekloud/event-simulator
  - name: image-processor
    image: some-image-processor
```
* If you then run `kubectl logs -f event-simulator`, which container's logs would show?
	* Must specify the container explicitly --> `kubectl logs -f event-simulator-pod event-simulator`