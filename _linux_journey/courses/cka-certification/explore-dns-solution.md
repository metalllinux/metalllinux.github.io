---
title: "Explore Dns Solution"
category: "cka-certification"
tags: ["cka-certification", "explore", "dns", "solution"]
---

* How to identify the DNS solution used in a cluster:
```
kubectl get pods -n kube-system
```
* Usually this is CoreDNS.
* `kube-dns` is the name of the service for which to access CoreDNS with.
* How to check the IP of the CoreDNS server that should be configured on PODS to resolve services?
	* Run `kubectl get service -n kube-system` and then check the ClusterIP value.
* Where is the configuration file kept for configuring the CoreDNS service?
	* Check the `Args` field of the CoreDNS deployment:
```
kubectl -n kube-system describe deployments.apps coredns | grep -A2 Args | grep Corefile
```
* In this example, the answer is `/etc/coredns/Corefile`.
* How is the Corefile passed into the CoreDNS POD?
	* Check the ConfigMaps, run this command `kubectl get cm -n kube-system` and check the `coredns` ConfigMap.
	* It is configured as a ConfigMap object.
* What is the name of the ConfigMap object created for Corefile?
	* `coredns`
* How to check the `root` domain/zone of the cluster?
```
kubectl describe configmap coredns -n kube-system
```
* Example answer is `cluster.local`
* What name can be used to access the `hr` web server from the `test` application?
	* Run `kubectl get svc` and get the right service name and port.
		* The example answer is `web-service`.
* Anything that has `.pod` inside of it, cannot be accessed.
* Troubleshoot why a web server is unable to access a database pod.
	* Run `kubectl edit deploy webapp`
	* Correct the `DB_Host` value.
		* In this case it had to be changed from `mysql` to `mysql.payroll`.
* From an HR pod, `nslookup` the `mysql` service.
	* Run this command: `kubectl exec -it hr -- nslookup mysql.payroll > /root/CKA/nslookup.out`