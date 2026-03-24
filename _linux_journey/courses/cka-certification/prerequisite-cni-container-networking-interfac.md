---
title: "Prerequisite Cni Container Networking Interfac"
category: "cka-certification"
tags: ["cka-certification", "prerequisite", "cni", "container", "networking"]
---

* Currently with Network Namespaces --> `1. Create Network Namespace` --> `2. Create Bridge Network / Interface` --> `3. Create VETH Pairs (Pipe, Virtual Cable)` --> `4. Attach vEth to Namespace` --> `5. Attach Other vEth to Bridge` --> `6. Assign IP Addresses` --> `7. Bring the interfaces up` --> `8. Enable NAT - IP Masquerade`
* How `Docker` does it --> `1. Crate Network Namespace` --> `2. Create Bridge Network / Inteface` --> `3. Create VETH Pairs (Pipe, Virtual Cable)` --> `4. Attach vEth to Namespace` --> `Attach Other vEth to Bridge` --> `6. Assign IP Addresses` --> `7. Bring the interfaces up` --> `8. Enable NAT - IP Masquerade`
	* `kubernetes`, `rkt`, `mesos` follows the exact same steps as above.
* Why code the same solution multiple times? Why not use one approach that everyone can follow?
* We split off `1. Crate Network Namespace` into its own part.
	* Then place `2. Create Bridge Network / Inteface` --> `3. Create VETH Pairs (Pipe, Virtual Cable)` --> `4. Attach vEth to Namespace` --> `Attach Other vEth to Bridge` --> `6. Assign IP Addresses` --> `7. Bring the interfaces up` --> `8. Enable NAT - IP Masquerade` under a `Bridge` config.
* We run a script that runs the above tasks to have a container connect to the `Bridge` network.
* Example of adding a container to a particular network namespace:
```
bridge add 2e34dcf34 /var/run/netns/2e34dcf34
```
* The `Bridge` program takes care of the rest, so the runtime environments don't need to bother with those tasks.
* For example, how `rkt` and `kubernetes` get networking configured for a particular container:
```
bridge add <cid> <namespace>
```
* What is a CNI?
	* Set of standards - define how programs should be developed to solve networking challenges in container runtime environments.
		* This type of program is referred to as a `plugin`.
* In the above case,the `Bridge` program would be a plugin for the CNI.
	* CNI defines how the plugin should be developed and how container run times should use them.
* Defines a set of runtimes and responsibilities:

* Container Runtime must create a network namespace.
* Identify the network that the container must attach to.
* Have the container runtime invoke the Network Plugin (bridge) when the container is ADDed (using the `add` command).
* The Container runtime invokes the Network Plugin (bridge) when the container is DELeted (using the `del` command).
* Specifies how to configure a network plugin on the runtime environment using a JSON file.
* It must support cmdline environments such ash `ADD/DEL/CHECK`.
* Must support parameters `container id`, `network ns`.
* Must manage IP address assignment to PODs.
* Must return results in a specific format.

* As long as the container runtimes and plugins, no problem.
* CNI already comes with this set of supported plugins:
	* `BRIDGE`
	* `VLAN`
	* `IPVLAN`
	* `MACVLAN`
	* `WINDOWS`
	* `DHCP`
	* `host-local`
* Other plugins from third-party advisors as well:
```
weaveworks flannel cilium nsx calico infobox
```
* All of the above container run time implement CNI standards.
* All of them can work with the above plugins.
* `Docker` does not implement CNI.
	* `Docker` has its own standard called CNM (Container Network Model).
	* Aims to solve container networking challenges.
* The above plugins do not natively integrate with `Docker` because of the different network model in use.
* Can't run a `docker` container and specify a CNI like the following:
```
docker run --network=cni-bridge nginx
```
* Doesn't mean you can't use `docker` with CNI at all. Have to work around it:
```
docker run --network=none nginx
```
* Then manually invoke the `bridge` plugin:
```
bridge add 2e34dcf34 /var/run/netns/2e34dcf34
```
* The above is how Kubernetes does it:
	* When Kubernetes creates `Docker` containers, it creates them on the non-network.
	* Invokes the CNI changes.
		* Takes care of the rest of the configuration.