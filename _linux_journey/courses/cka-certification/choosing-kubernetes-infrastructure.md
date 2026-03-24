---
title: "Choosing Kubernetes Infrastructure"
category: "cka-certification"
tags: ["cka-certification", "choosing", "kubernetes", "infrastructure"]
---

* Linux - can install binaries manually and setting up a cluster.
* Windows - cannot setup Kubernetes initially - need to rely on virtualisation solutions such as Virtual Box to create these on Kubernetes.
	* Can run Kubernetes components as Docker containers in Windows.
		* Remember that the containers are still Linux and under the hood they run on a small Linux OS called HyperV.
* Minikube is a single node cluster - needs Oracle Virtual Box to run the cluster components. Minikube deploys the VM part itself.
* `kubeadm` can deploy a single or multi-node cluster very quickly.
	* Must provision required host with support configuration yourself.
	* Requires VMs to be ready.
* On the cloud, there are two solutions: Turnkey or Hosted
	* Turnkey - provision required VMs - use tooling or scripts to configure a Kubernetes cluster on them.
		* Must maintain VMs yourself - for example Kubernetes on AWS with KOPS.
	* Hosted - Kubernetes-as-a-service.
		* Provider provisions VMs.
		* Installs Kubernetes for you.
			* Provider maintains VMs - done in Google Container Engine.
* Turnkey Solution:
	* OpenShift - popular on-prem Kubernetes platform by Red Hat.
		* OpenShift is an open source container platform and is built on top of Kubernetes.
		* Provides a nice set of tools and GUI for creating and managing Kubernetes constructs - easily integrate with CI/CD pipelines.
	* Cloud Foundry Container Runtime - made by Cloud Foundry - deploys and managers Kubernetes cluster using Open Source tool called BOSH.
	* If have VMware environment, can use VMware Cloud PKS
	* Vagrant - useful scripts to deploy a Kubernetes cluster on different cloud service provideres.
	* Need VMs / physical machines.
	* All of the above solutions are Kubernetes 1.13 certified.
* Hosted Solutions:
	* Google Container Engine.
	* OpenShift Online - receive access to a fully functional cluster on the web.
	* Azure Kubernetes Service
	* Amazon Elastic Container Service for Kubernetes (EKS) - Amazon:s hosted Kubernetes offering.
* Can create three machines using VirtualBox can be done using VirtualBox.