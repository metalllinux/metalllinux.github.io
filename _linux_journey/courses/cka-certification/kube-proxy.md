---
title: "Kube Proxy"
category: "cka-certification"
tags: ["cka-certification", "kube", "proxy"]
---

* Within a Kubernetes cluster, every pod can reach every other pod.
* Accomplished by a pod networking solution to the cluster.
* This is a `POD Network`, which expands across and is where all of the pods connect to.
	* There are many solutions available to accomplish this.
* For example, a web application deployed on Node 1 and a database application deployed on Node 2.
* For the web application to reach the database pod, there is no guarantee that this will always be the same.
![d073886a32fc3274dda010a95edcf800.png](../../_resources/d073886a32fc3274dda010a95edcf800.png)
* A better way for the web application to reach the database, is by using a service.
	* The service exposes the database application across the cluster.
* The web application can access the database, using the name of the service (in this case DB).
* The service also has an IP address assigned to it.
* Whenever a pod tries to access the service, it forwards the data to the backend pod.
* How does the service get an IP?
* The service cannot join the pod network - it is not a container.
	* It is a virtual component, that only lives in the Kubernetes' memory.
* The service should be accessible across the cluster from any node.
	* That is why Kube-Proxy is used.
* `Kube-proxy` is a process that runs on each node in the Kubernetes cluster.
![870b3451d25b82dc9c03c354383fe733.png](../../_resources/870b3451d25b82dc9c03c354383fe733.png)
* `Kube-proxy`'s job is to look for new services. Every time a service is created, it generates the appropriate rules on each node to forward traffic to those services, then to the backend pods.
	* One way `Kube-proxy` does the traffic forwarding is via IP Table rules.
	* It creates an IP Tables rule on each node in the cluster, to then forward traffic to the IP of the service, in this example 10.96.0.12, to the IP of the pod, which is 10.32.0.15.
![b8cacc05c520e5617fd8f743d31a0c6f.png](../../_resources/b8cacc05c520e5617fd8f743d31a0c6f.png)
* Installing `kube-proxy`, download the Kubernetes binary from the release page:
![4f8c2cf43011c64196e68cbfb22e8ec5.png](../../_resources/4f8c2cf43011c64196e68cbfb22e8ec5.png)
* Then run it as the `kube-proxy.service`.
![b33299045aae354deb78f960a6ed296c.png](../../_resources/b33299045aae354deb78f960a6ed296c.png)
* The `kubeadm` tool deploys `kube-proxy` as pods on each node.
* `kubectl get pods -n kube-system`
* `kubectl get daemonset -n kube-system`
* It is deployed as a `daemonset`, therefore deployed on each node in the cluster:
![ce42475b4f152cacefca7256be760643.png](../../_resources/ce42475b4f152cacefca7256be760643.png)
* 