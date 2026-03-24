---
title: "Kube Api Server"
category: "cka-certification"
tags: ["cka-certification", "kube", "api", "server"]
---

* This is the primary management component in Kubernetes.
* When you run a `kubectl` command, this is what talks to the \`kube-api\` server.
* The `kube-api` server firstly authenticates the request and then validates it.
* It then retries the data from the `etcd` cluster and then responds back with the requested information (showing the output of `kubectl get nodes` for example)
![screenshot.png](../../_resources/screenshot-16.png)
* Can also implement the APIs directly by sending a post request.
![screenshot.png](../../_resources/screenshot-8.png)
* The `kubeapi-server` creates a pod object, without assigning it to a node.
* It then updates the information in the `etcd` cluster.
* It then updates the user that the pod has been created.
* The Scheduler continuously monitors the `kubeapi-server`
* The Scheduler identifies the right node to place the pod on.
	* It indicates this back to the `kubeapi-server`
* The `kubeapi-server` then updates the information in the `etcd` cluster.
	* The information is then passed to the Kubelet, in the appropriate worker node.
	* The kubelet then creates the pod on the node and instructs the container runtime to deploy the application image. 
* Once done, the kubelet updates the status back to the API server.
* The `kubeapi-server` then updates the data back into the `etcd` cluster.
![screenshot.png](../../_resources/screenshot-12.png)
* A similar pattern is followed as soon as a change is requested. The `kubeapi-server` is the heart of all of the tasks and changes in the cluster.
* The above is not required, if you bootstrapped using the `kubeadm` tool.
* You can download and configure the `kube-api` server to run on your Master Node.
![screenshot.png](../../_resources/screenshot-10.png)
* The `kube-api` server is ran with a lot of parameters.
![screenshot.png](../../_resources/screenshot-9.png)
* Not need to understand all of the options right now.
* Having a high level understanding is good, when you configure the cluster from scratch.
* All components in a Kubernetes cluster need to know where they are.
* A lot of the components in the above config file are certificates, which are needed for the connectivity between different components.
	* These are part of the SSL / TLS certificates.
* The option `etcd-servers` is where you specify the location of the `etcd` server.
![screenshot.png](../../_resources/screenshot-17.png)
* This is how the `kube-api` server connects to the `etcd` servers.
* How to view the `kube-api` options in an existing cluster?
* An example is `kubectl get pods -n kube-system`
* If you set up the cluster with the `kubeadm` tool, the `kubeadm` tool deploys the `kube-api` server as a pod like so:
![screenshot.png](../../_resources/screenshot-14.png)
* You can see the  `api-server` options in the `/etc/kubernetes/manifests/kube-apiserver.yaml` file.
![screenshot.png](../../_resources/screenshot-15.png)
* In a non `kubeadm` setup, you can inspect the options in the `systemd` `kubeapi` service file.
![screenshot.png](../../_resources/screenshot-13.png)
* You can also see the running process and the implemented options, by running `ps -aux | grep kube-apiserver`. Run this on the Master Node.
![screenshot.png](../../_resources/screenshot-11.png)