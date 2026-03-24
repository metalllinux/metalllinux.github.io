---
title: "Static Pods"
category: "cka-certification"
tags: ["cka-certification", "static", "pods"]
---

* The `kubelet` functions as one of the many Control Plane components in Kubernetes.
* The `kubelet` relies on the `kubeapi` server for which instructions to run on the node.
	* The decision was made by the `kubeScheduler`, which is then stored in the `etc data store`.
* What if you removed the ControlPlane node entirely from the cluster and only has the Worker Node and its `kubelet`.
	* The `kubelet` or “captain” of the node can manage the node independently.
	* On the Worker Node we have the  `kubelet` and `Docker` to run the containers.
	* A `kubeapi` server does not exist.
* The one action the `kubelet` knows to do is to create pods.
	* The one problem is there is no `kubeapi` server available to provide pod details.
	* How do you provide a pod definition file to the `kubelet` without a `kubeapi` server?
		* You can configure the `kubelet` to read the pod definition file from a set location (`/etc/kubernetes/manifests` instead).
			* Place the pod definition files there.
			* The `kubelet` periodically checks this directory and reads the files there.
			* It creates the pod and ensures that it stays alive (if the application crashes, the pod is also restarted).
			* If any of the pod definition files are changed in the directory, the `kubelet` recreates the pods.
			* If a file is removed from the directory, the pod is deleted automatically.
			* This setup is now known as a Static Pod. You cannot create Replicasets, Deployments or anything similar. Only Pods.
* The `kubelet` only works at a Pod level.
* The directory can be created anywhere on the host.
	* It is a passed in as an object whilst the `kubelet` is running the service.
* Under `kubelet.service`, the option to specify the directory where the pod manifest files are is:
```
--pod-manifest-path=/etc/Kubernetes/manifest
```
* The above line is under `ExecStart=/usr/local/bin/kubelet`
* Another way aside from mentioning the option specifically in the `kubelet.service` file, is by creating a separate `yaml` file and then linking to that `yaml` file in the `kubelet.service` file:
```
ExecStart=/usr/local/bin/kubelet
--config=kubeconfig.yaml
```
* Then in `kubeconfig.yaml` you have to set the `staticPodPath` like so:
```
staticPodPath: /etc/kubernetes/manifest
```
* When the Static Pods are created, you can view them via the `docker ps` command.
	* For `cri-o`, we use `crictl ps`.
	* For `containerd`, you can use `nerdctl ps`
		* We are not able to use `kubectl` here, as we do not have the `kube api server` available.
* The `kubelet` works by taking in requests from different inputs.
	* These can be from the pod definition files from the Static Pods directory as mentioned above.
	* The second way is from an HTTP API endpoint - that is how the `kube-apiserver` provides input to the `kubelet`.
* `kubelet` can create `Static Pods` and those from the `kube-apiserver` at the same time.
	* The `kube-apiserver` is also aware of the pods being created by the `kubelet`.
* `kubectl get pods` will show the `Static Pods` as well.
	* If the Worker Node's `kubelet` is part of the cluster, it creates a mirror object in the `kube-apiserver`. The `kube-apiserver` only has a read-only mirror of the pod.
		* Can receive details of the pods from the `kube-apiserver`, but you cannot edit or delete them.
			* The pods can only be deleted from the Worker Node's manifest directory.
		* The name of the pod is automatically appended with the node name `static-web-node01`.
* Useful uses of `Static Pods` to deploy ControlPlane components as Pods on a node.
	* Install a `kubelet` service on all of the Master Nodes.
	* Create pod definition files that use Docker images of the various Control Plane components --> `kube-apiserver`, `etcd`, `controller-manager` and so on.
	* Then place the manifest files in the directory of each Worker Node.
* It makes it easier not to need to download and setup additional applications.
	* The above method is how the `kubeadm` tool sets up a Kubernetes cluster.
		* That is why when you list the pods in the `kube-system` namespace with `kubectl get pods -n kube-system`, you see each component as a pod.
* Difference between static pods and DaemonSets -->
	* Static Pods:
		* Created by `kubelet`.
		* Deploys Control Plane components as Static Pods.
	* DaemonSets:
		* Created by the `kube-apiserver`.
		* Deploys Monitoring Agents, Logging Agents on Nodes.
* Both Static Pods and DaemonSets are ignored by the `kube-scheduler`.
* 