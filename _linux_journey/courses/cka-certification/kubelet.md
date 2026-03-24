---
title: "Kubelet"
category: "cka-certification"
tags: ["cka-certification", "kubelet"]
---

* The kubelet is like the captain on the ship.
* Ones responsible for doing all of the paperwork to become part of the cluster.
* Sole point of contact for the Master Ship.
* They load and unload containers, instructed by the scheduler on the Master Node.
* They also send back reports at regular intervals on the status of the ship.
![776fb66b2f74cf30512f0172ad14927b.png](../../_resources/776fb66b2f74cf30512f0172ad14927b.png)
* The `kubelet` in the Kubernetes Worker Node, registers the node in the Kubernetes Cluster.
* When the `kubelet` receives a request to load a pod, it goes to the runtime engine (for example Docker) and pulls the required image to run an instance.
* The `kubelet` then continues to monitor the state of the pod and the containers within it and reports to the `kube-apiserver` on a timely basis.
![52d0879f084cb52c1dd67e9b3e8331e8.png](../../_resources/52d0879f084cb52c1dd67e9b3e8331e8.png)
* How do you install a `kubelet`?
* If you use the `kubeadm` tool, it does not automatically deploy the `kubelet`.
* Must always manually install the `kubelet` on your worker nodes.
	* Download the installer, extract it and run it as a service.
![b240845a7b483d776191ca8d55d9a971.png](../../_resources/b240845a7b483d776191ca8d55d9a971.png)
* You can view the `kubelet` and its options by running `ps -aux | grep kubelet` on the Worker Nodes.
![939854068c10d1dc7c51b48aa083df1c.png](../../_resources/939854068c10d1dc7c51b48aa083df1c.png)
