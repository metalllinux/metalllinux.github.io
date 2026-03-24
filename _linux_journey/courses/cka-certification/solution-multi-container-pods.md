---
title: "Solution Multi Container Pods"
category: "cka-certification"
tags: ["cka-certification", "solution", "multi", "container", "pods"]
---

* Good example multi-container pod definition file:
```
apiVersion: v1
kind: Pod
metadata:
  name: yellow
spec:
  containers:
  - name: lemon
    image: busybox
    command:
      - sleep
      - "1000"

  - name: gold
    image: redis
```
* An example command to inspect a container's logs within a pod:
```
kubectl -n elastic-stack logs kibana
```
* Go through this documentation to add a side car container: https://kubernetes.io/docs/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume/
* A good manifestation file surrounding the `elastic-stack`
* Good video on the Kubernetes Stack and the Kibana Dashboard.
* To check the containers that running under a pod, run `kubectl describe pod <pod_name>`
* Example container create:
```
kubectl run yellow --image=busybox --dry-run=client -o yaml
```
* Then edit the file that is generated.
```
apiVersion: v1
kind: Pod
metadata:
  name: yellow
spec:
  containers:
  - name: lemon
    image: busybox
    command:
      - sleep
      - "1000"

  - name: gold
    image: redis
```
* Can also do the `sleep` command like the above using the following:
```
apiVersion: v1
kind: Pod
metadata:
  name: yellow
spec:
  containers:
  - name: lemon
    image: busybox
    command: ["sleep", "1000"]
  - name: gold
    image: redis
```
* Then create the pod with `kubectl create -f yellow.yaml`.
* Firstly, explore the namespace `kubectl get pods -n elastic-stack`
* Check logs with `kubectl logs pod <app_name> -n <namespace>`
	* These logs are also stored in the pod as well:
```
kubectl -n <namespace> exec -it <pod_name> -- cat <log_location_of_container>
```
* How to edit a pod for sidecar:
```
kubectl edit pod <pod_name>
```
* Then add an image under `spec:` --> `containers:`
```
spec:
  containers:
  - image: kodekloud/filebeat-configured
    name: sidecar
    volumeMounts:
    - mountPath: /var/log/event-simulator/
      name: log-volume
```
* Save and quit. Take the `temp` file that is created and then run the following to recreate the pod with the additional container added:
```
kubectl replace --force -f /tmp/kubectl-edit-234235234.yaml`
```