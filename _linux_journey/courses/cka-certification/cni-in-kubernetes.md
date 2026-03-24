---
title: "Cni In Kubernetes"
category: "cka-certification"
tags: ["cka-certification", "cni", "kubernetes"]
---

* CNI defines responsibilities of a container runtime.
* The Container Runtime must create the network namespace.
* Must identify and attach the namespaces to the appropriate container.
* Container Runtime to invoke Network Plugin (bridge) when a container is ADDed.
* Container Runtime to invoke the Network Plugin (bridge) when a container is DELeted.
* JSON format of the Network Configuration.
* CNI plugin must be invoked by the component within Kubernetes for creating containers.
	* That component must invoke the appropriate network plugin, after the container is created.
* The component responsible for creating containers is the Container Runtime.
	* Two good examples are `containerd` and `cri-o`.
	* `containerd` is an abstraction of `docker` and replaces it.
* All network plugins are installed under `/opt/cni/bin`
	* This is where the Container Runtimes find the plugins.
* Which plugin and which to use is configured in the `/etc/cni/net.d` directory.
	* May be multiple configuration files in this directory.
	* Examples are `bridge.conflist` and `flannel.conflist`.
* Checking the `/opt/cni/bin` directory will show the following available plugins:
```
bridge dhcp flannel host-local ipvlan loopback macvlan portmap ptp sample tuning vlan weave-ipam weave-net weave-plugin-2.2.1
```
* The `/etc/cni/net.d` directory has a bunch of configuration files:
```
10-bridge.conflist
```
* If there are multiple files in the above directory, it will choose the one in alphabetical order.
* The `10-bridge.conflist` file looks like this:`
```
{
	"cniVersion": "0.2.0",
	"name":	"mynet",
	"type":	"bridge",
	"bridge":	"cni0",
	"isGateway":	true,
	"ipam":	{
		"type":	"host-local",
		"subnet":	"10.22.0.0/16",
		"routes":	[
			{ "dst": "0.0.0.0/0"}
]
}
}
```
* The `isGateway` defines whether an IP Address should be assigned.
* `ipMasq` defines if a NAT rule should be added for IP masquerading.
* The IPAM section defines an IPAM configuration.
	* Specify the subnet and IPs that are assigned to pods and any required routes.
* `host-local` indicates the IP addresses are managed locally on the host. The `type` can also be set to `dhcp` to configure an external DHCP server.