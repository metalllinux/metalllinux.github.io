---
title: "Cluster Upgrade Process"
category: "cka-certification"
tags: ["cka-certification", "cluster", "upgrade", "process"]
---

* Regarding the core control plane components, it is not mandatory for them all to be the same version.
	* The `kube-apiserver` is the primary component in the ControlPlane.
	* None of the other components in the ControlPlane group should be at a higher version than the `kube-apiserver`.
* The `controller-manager` and `kube-scheduler` can be one version lower than the `kube-apiserver`.
* `kubelet` and `kube-proxy` can be two versions lower.
* `kubectl` can be one version higher, the same version or one version lower than the `kube-apiserver` .
* The skew in versions allows for live upgrades to be carried out.
* When should you upgrade?
	* Kubernetes only supports the latest 3 minor versions.
	* The recommended approach is to upgrade 1 minor version at a time.
		* Can upgrade to the latest version this way.
* The upgrade process varies depending on how the cluster was set up.
	* Google Kubernetes Engine allows you to upload with a few clicks.
	* `kubeadm` allows you to run these commands `kubeadm upgrade plan` and `kubeadm upgrade apply`.
	* You can also manually update each component of the cluster yourself as well.
* For example there is a cluster with one Master node and three Worker nodes.
	* You firstly upgrade the Master node, then the Worker node.
		* When the Master node is upgraded, the control plane components go down briefly - `kube-apiserver`
		* Because the Master node is down, doesn't mean the Worker nodes are impacted and these continue to server users.
* Since the Master Node is down, all cluster functionality such as deploying new pods is unavailable.
* Once the upgrade on the Master node is complete and the node is back up, the cluster should be back up.
* The the Master Node will be on one minor version later than the Worker Nodes.
* Strategy for updating the Worker Nodes - Upgrade them all at the same times means no users can access any applications.
	* New pods would then be scheduled and users can resume access.
* Second Strategy is to upgrade one Worker node at a time.
	* The workloads are therefore split between the nodes that are still up.
* A third strategy is to add new nodes to the cluster, that have a newer software version.
	* Move the workload over to the new node and remove the older node that is running an older version.
* Then run `kubeadm upgrade plan`.
	* `kubeadm` does not install or upgrade `kubelets`
* Example upgrade steps for `kubeadm`:
	* `dnf upgrade -y kubeadm=1.12.0-00`
	* Then `kubeadm upgrade apply v1.12.0`
		* It pulls the necessary images and upgrades the cluster components.
			* If you then run the `kubectl get nodes` command, you see the version of the nodes still displayed as the older version.
				* That is because it is showing the `kubelet` version that is registered with the `kube-apiserver`.
					* Not the `apiserver` itself.
* `kubeadm` uses `kubelets` to deploy things on the Master Node.
* Then upgrade the `kubelet` with `dnf upgrade -y kubelet=1.12.0-00`
* Then restart the `kubelet` service:
```
systemctl restart kubelet
```
* Then running the `kubectl get nodes` command will show the Master Node is upgraded to the new version.
* Steps to upgrade the Worker Nodes:
* The `kubectl drain <node>` command helps to remove all pods on a node and re-schedules those to other nodes.
	* It also cordons the node and marks it as unschedulable.
* Run `dnf upgrade -y kubeadm=1.12.0-00`
* Run `dnf upgrade -y kubelet=1.12.0-00`
* Run `kubeadm upgarde node config --kubelet-version v1.12.0`
* Restart the `kubelet` service:
```
sudo systemctl restart kubelet
```
* Then unmark it as non-schedulable with `kubectl uncordon <node>`.
* It is only marked as schedulable when pods are deleted from other nodes or new pods are created.
* Perform the above steps on each node.