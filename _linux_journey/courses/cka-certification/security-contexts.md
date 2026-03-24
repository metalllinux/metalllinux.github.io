---
title: "Security Contexts"
category: "cka-certification"
tags: ["cka-certification", "security", "contexts"]
---

* When running a `docker` container, can run as a particular user:
```
docker run --user=1001 ubuntu sleep 3600
```
* `containerd` is with `nerdctl run`
* Linux capabilities that can be added:
```
docker run --cap-add MAC_ADMIN ubuntu
```
* The above `docker` stuff can be configured in Kubernetes as well.
* Can set security in Kubernetes at a `container` level or a `pod` level.
* If you configure security at a `pod` level, the settings apply to all of the `containers` in the pod.
* If you configure the security on both the `pod` and `container`, the settings on the `container` will override the settings on the pod.
* Example Security Context at the pod level:
```
apiVersion: v1
kind: Pod
metadata:
  name: web-pod
spec:
  securityContext:
    runAsUser: 1000
containers:
     - name: ubuntu
       image: ubuntu
       command: ["sleep","3600"]
```
* To set the above at the container level:
```
apiVersion: v1
kind: Pod
metadata:
  name: web-pod
spec:
  containers:
     - name: ubuntu
       image: ubuntu
       command: ["sleep","3600"]
       securityContext:
         runAsUser: 1000
		 capabilities:
			 add: ["MAC_ADMIN"]
```
* `Capabilities` are only supported at the container level, not the POD level.