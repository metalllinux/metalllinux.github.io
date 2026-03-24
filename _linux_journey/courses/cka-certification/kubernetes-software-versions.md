---
title: "Kubernetes Software Versions"
category: "cka-certification"
tags: ["cka-certification", "kubernetes", "software", "versions"]
---

* When we deploy a specific version of Kubernetes, it is deployed.
* Can find the version out from the `kubectl get nodes` command.
* The Kubernetse release versions consist of three parts.
* For example with `v1.11.3`:
	* `v1` - major version.
	* `11` - minor version.
	* `3` - patch version.
* `Patches` are released as Bug Fixes.
* `Minor` version changes contain Features and Functionality changes.
* Kubernetes releases new minor versions every few months.
* July 2015 - version 1.0 released.
* December 2018 - version 1.13.0 is the stable release.
* Will also see `alpha` and `beta` releases for fixes and bug improvements.
	* `alpha` releases are tagged for example like `v1.10.0-alpha`
	* `beta` release means it is well-test and new features are enabled by default. The tag looks like `v1.10.0-beta`.
	* Then ultimately the main stable release is called `v1.10.0` in this case.
* All releases are found in the Kubernetes GitHub Release page.
	* Download the tarball and it has all of the control plane components available:
		* `kube-apiserver`
		* `controller-manager`
		* `kube-scheduler`
		* `kubelet`
		* `kube-proxy`
		* `kubectl`
			* All of the above will have the same version number, for example `v1.13.4`.
	* What does not have the same version numbers are the `ETCD CLUSTER` and `CoreDNS` components.
		* This is because the `etcd cluster` and `coredns` are separate projects, with their own versioning.