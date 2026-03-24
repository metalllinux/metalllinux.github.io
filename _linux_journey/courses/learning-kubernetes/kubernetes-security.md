---
title: "Kubernetes Security"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "kubernetes", "security"]
---

* Standard set of security practices to apply to a cluster.
* Hackers want one of three things:
	* Steal Data inside the cluster.
	* Harness the computational power of the cluster for Cryptomining.
	* Or cause a DDoS attack.
* Example secure deployment yaml file:
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
  replicas: 3
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
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
        securityContext:
          allowPrivilegeEscalation: false
          runAsNonRoot: true
          capabilities:
            drop:
              - ALL
          readOnlyRootFilesystem: true
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
* The first way to secure the cluster, is to add Security Context Info to the pods:
```
securityContext:
          allowPrivilegeEscalation: false
          runAsNonRoot: true
          capabilities:
            drop:
              - ALL
          readOnlyRootFilesystem: true
```
* If someone accesses your cluster and can remotely control your container, it causes security issues.
	* To prevent this, you can add two items to the container:
		* Make sure that containers are run as non-root.
			* I.E. by `exec`ing into the pod, you can't use `sudo` to run installation commands.
			* In a manifest, it looks like the above example.
			* To not allow privilege escalation, we use `allowPrivilegeEscalation: false`
			* We make sure it does not run as `root` with `runAsNonRoot: true`
			* All capabilities are dropped like:
```
capabilities:
            drop:
              - ALL
```
* The second item is to make sure the file system is read-only. Therefore, we use:
```
readOnlyRootFilesystem: true
```
* Another Kubernetes security practice is to scan your Kubernetes manifests with a security tool such as `Snyk`. Scans through Infrastructure as Code Files.
* To scan, we use:
```
snyk iac test deployment.yaml
```
* Will show multiple issues, such as a low severity issue like:
```
Container is running with writable root filesystem
```
* Would therefore need to set `readOnlyRootFilesystem: true
` in the deployment.yaml file.
* Medium severity issues are:
```
Container is running without root user control
```
* We fix that with: `runAsNonRoot: true`.
* If we have `Container does not drop all default capabilities`, that is fixed with:
```
capabilities:
            drop:
              - ALL
```
* If you see `Container is running without privilege escalation control`, we have to set the following to `false`:
```
allowPrivilegeEscalation: false
```
* Fnal option to harden against attacks, is to update the version of Kubernetes. Can check Open CVE for any security flaws with Kubernetes.
* There is also the Kubernetes Hardening Guide, released by the US National Security Agency.