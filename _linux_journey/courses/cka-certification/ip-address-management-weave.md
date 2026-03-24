---
title: "Ip Address Management Weave"
category: "cka-certification"
tags: ["cka-certification", "address", "management", "weave"]
---

* How are the virtual bridges in the nodes assigned an IP subnet?
* How are the Pod assigned an IP?
* Where is the information stored?
* How are duplicate IP not assigned?
* CNI Plugin Responsibilities:
	* Must support arguments ADD/DEL/CHECK.
	* Must support parameters container id, network ns.
	* Must manage IP Address assignment to PODs.
	* Must return results in a specific format.
* How assign IP Address?
* How do we not assign duplicate IPs during the `ip -n <namespace> addr add` and `ip -n <namespace> route add` commands?
	* An easy way is to store all required IPs in a file.
* The file would look like this:
```
IP         STATUS   POD
10.244.1.2 ASSIGNED BLUE
```
* The above file is placed on each host and the IPs of each pod per host are assigned appropriately.
* In the network assignment script, you'd add `ip = get_free_ip_from_file()` before running the `ip -n` names.
* You can outsource the above actually and use two built-in plugins with CNI --> `DHCP` and `host-local`
	* You'd call that in the network assignment script with `ip = get_free_ip_from_host_local()`
* The CNI has a configuration file under `/etc/cni/net.d/net-script.conf`. It looks like this:
```
{
	"cniVersion": "0.2.0",
	"name":	"mynet",
	"type":	"net-script",
	"bridge":	"cni0",
	"isGateway": true,
	"ipMasq":	true,
	"ipam":	{
		"type": "host-local",
		"subnet":	"10.244.0.0/16",
		"routes":	{
			{	"dst":	"0.0.0.0/0"	}
}

}
```
* The above `ipam` section is the one of interest with CNI.
	* The `ipam` config settings are read from the network assignment script.
* WEAVEWORKS by default allocates the IP range of `10.32.0.0/12` for the entire network.
	* Provides an IP range of `10.32.0.1` to `10.47.255.254`. 1,048,574 IPs are available.
		* This is now split between each node. Node A is assigned `10.32.0.1`, Node B is assigned `10.38.0.0` and Node C is assigned `10.44.0.0`. This is for the pods, not the actual node IPs themselves.
* 