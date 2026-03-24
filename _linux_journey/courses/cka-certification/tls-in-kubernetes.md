---
title: "Server Components"
category: "cka-certification"
tags: ["cka-certification", "tls", "kubernetes"]
---

* A CA has its own private and public keypairs - these are `Root Certificates`.
* A Server has its own certificates - `Certificate (Public Key)` and `Private Key`.
* A client also has `Client Certificates` as well.
* Certificates with public keys are usually have a `.pem` or `.crt` extension.
* Private Keys have a `.key` or `-key.pem`.
* The Admin when connecting to the Master Server's `kube-apiserver` has to do so via TLS. Same when going from the `kube-apiserver` to the `kube-scheduler` - that also has to be secured via TLS.
* The Master Node to the Worker Nodes also need to be secured with certificates.
* A Kubernetes Cluster uses `Server Certificates for Servers` and `Client Certificates for Clients `
### Server Components
* The `kube-apiserver` exposes an HTTPS service that the cluster and users use to connect.
	* The `kube-apiserver` has its own `apiserver.crt` certificate and `apiserver.key` files.
	* The certificate names can change depending on the setup.
* Another server in the cluster is the `etcd server`. This stores information about the cluster. This has the following files:
	* `etcdserver.crt`
	* `etcdserver.key`
* The other server in the cluster is on the Worker Nodes - these are the `kubelet` services or `kubelet server`.
	* This has the following files:
	* `kubelet.crt`
	* `kubelet.key`
### Client Components
* The `Admin` requires an `admin.crt` and `admin.key` to interact with the `kube-apiserver`.
	* The `Admin` interacts via the `kubectl REST API`.
* The `kube-scheduler` communicates with the `kube-apiserver` to work out which pods need scheduling.
* The scheduler has the following:
	* `scheduler.crt`
	* `scheduler.key`
* The `scheduler` is a client that access the `kube-apiserver`.
* The `kube-controller-manager` is another client that access the `kube-apiserver`.
	* This has these pairs of files:
		* `controller-manager.crt`
		* `controlller-manager.key`
* The last client component is the `kube-proxy`.
	* This also requires its own pairs of certificates:
		* `kube-proxy.crt`
		* `kube-proxy.key`

* The components even connect amongst each other, for example the `kube-apiserver` communicates to the `etcd-server`.
* The `kube-apiserver` is the only server that talks to the `etcd-server`.
* The `kube-apiserver` can use the same keys `apiserver.crt` and `apiserver.key` as mentioned above as API keys.
* Can also generate a pair of separate for the `kube-apiserver`, to then authenticate directly to the `etcd-server`. These are:
	* `apiserver-etcd-client.crt`
	* `apiserver-etcd-client.key`
* The `kube-apiserver` also communicates with the `kubelet` on each work node. It can either use the original `apiserver.crt` and `apiserver.key` certificates or specifically generate its own certificates with:
	* `apiserver-kubelet-client.crt`
	* `apiserver-kubelet-client.key`
* Kubernetes requires that all of the above certificates **need** to be signed by a Certificate Authority.
	* At least one Certificate Authority needs to be present on the cluster.
* You can have a configuration where there are multiple Certificate Authoritys present in the cluster, one for the `etcd-server` and `kube-apiserver` and then one for everything else.
* The certificate authority's certificate will be the following:
	* `ca.crt`
	* `ca.key`