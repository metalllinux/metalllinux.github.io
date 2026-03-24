---
title: "Design A Kubernetes Cluster"
category: "cka-certification"
tags: ["cka-certification", "design", "kubernetes", "cluster"]
---

* Need to ask the following questions:
	* Learning
	* Testing
	* Production-grade application?
	* Cloud or On-prem
	* What workloads to be ran?
		* What applications?
			* Web
			* Big data / Analytics?
		* Application resource requirements?
			* Heavy traffic or burst?
* Education purposes:
	* Minikube
	* Single node cluster with `kubeadm`/GCP/AWS
* Development and Testing:
	* Multi-node cluster.
	* Use `kubeadm` or quickly provisioning with (Google Container Engine) GCP, AWS or AKS.
* Hosting Production-grade Applications
	* High availability multi node cluster with ultiple master nodes.
	* kubeadm or GCP or Kops on AWS
	* Cluster restrictions:
		* Up to 5000 nodes.
		* Up to 150,000 PODs in the cluster.
		* Up to 300,000 total containers
		* Up to 100 Pods per node
* The size of the node really depends. A good chart is the following:
1-5 nodes --> GCP - N1-standard-1 1 vCPU 3.75GB RAM / AWS - M3.medium - 1 vCPU 3.75GB
  101-250 --> GCP - N1-standard-8 8 vCPU 30GB RAM / AWS - M3.2xlarge - 8 vCPU 30GB
  f> 500 --> GCP - N1-standard-32 32 vCPU 120GB RAM / AWS - C4.8xlarge - 36 vCPU 60GB

* Deploying OnPrem clusters, use the above guides.
* Use kubeadm for on-prem
* GKE for GCP
	* Has one-click cluster upgrade feature for simple upgrades.
* Kops for AWS
* Azure Kubernetes Service for Azure

* Storage concerns:
	* High performance - SSD backed storage.
	* Multiple concurrent connections - network-based storage
	* Persistent shared volumes for shared access across multiple PODs.
	* Label nodes with specific disk types.
	* Use Node Selectors to assign applications to nodes with specific disk types.

* Nodes:
	* Physical or virtual is fine.
	* Minimum of 4 Node Cluster (Sise-based on workload)
	* Master vs. Worker Nodes
		* Not a strict requirements that Worker Nodes should use
		* Master Nodes should be ran with Control Plane items only.
		* Deployment tools like kubeadm, prevent deployments being placed on Master Nodes.
			* It adds a taint to a Master Node to stop this.
	* Linux x86_64 Architiectures.

* Master Nodes:
	* On large clusters, can separate the `ETCD` cluster away from the Master Node.
		* It will be placed on its own cluster node.

* Won't be tested on anything in this section in the exam.