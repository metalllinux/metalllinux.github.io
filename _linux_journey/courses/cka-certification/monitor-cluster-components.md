---
title: "Monitor Cluster Components"
category: "cka-certification"
tags: ["cka-certification", "monitor", "cluster", "components"]
---

* How to monitor resource consumption?
* Kubernetes currently does not come with a monitoring solution.
* There are solutions available for this, those being:
	* Metrics Server
	* Prometheus
	* Elastic Stack
	* Datadog
	* Dynatrace
* Heapster was an original project that allowed a lot of monitoring and analysis of a cluster for Kubernetes.
	* Heapster is now deprecated and `Metrics Server` is a slimmed down version of that.
* You can have one `Metrics Server` per cluster.
	* It retrieves metrics from each Kubernetes node and pod, gathers data and aggregates it.
	* This is all done in memory.
		* Not on disk.
		* Cannot see historical performance data.
* How are the metrics generated on each node?
	* Kubernetes has a `kubelet` per node.
		* Response for receiving instructions from the Kubernetes API Master Server.
		* Also for running pods on nodes.
		* Contains a sub-component called `cAdvisor`. Stands for Container Advisor.
			* This is responsible for collecting metrics from pods and exposing them with the `kubelet` API. That then gets sent to the `Metrics Server`
* If you are using `minikube`, then run `minikube addons enable metrics-server`
* For other environments, run the following `git clone` command:
```
git clone https://github.com/kubernetes-incubator/metrics-server.git
```
* Deploy the required components with the `kubectl create -f` command, such as `kubectl create -f deploy/1.8+/`
	* It deploys roles, pods and services to allow the `Metrics Server` to pole data from the cluster.
	* Performance data can then be viewed by running `kubectl top node`
		* Shows CPU and Memory usage for nodes.
	* `kubectl top pod` shows performance metrics of pods.
* 