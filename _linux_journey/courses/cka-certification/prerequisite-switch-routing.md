---
title: "Prerequisite Switch Routing"
category: "cka-certification"
tags: ["cka-certification", "prerequisite", "switch", "routing"]
---

* Switching - how does Host A reach Host B? Through a switch.
* The switch contains a network between the two systems.
* Require an interface on each host.
	* Run `ip link` as a good way to check.
* Add IPs to each host:
```
ip addr add 192.168.1.10/24 dev eth0
ip addr add 192.168.1.11/24 dev eth0
```
* Routing - On one network with `192.168.1.0` and another network of `192.168.2.0`, how do the two networks talk to each other?
	* Routers are therefore needed for this.
	* To bridge the two networks, one address is assigned to one side of the router `192.168.1.1` and `192.168.2.1`
* How does one Host on one Network know where to send its packet to on the second Network?
* Gateways - Use the `route` command to show routing information such as `Destination, Gateway, Genmask, Flags, Metric, Ref, Use, Iface`
	* `route` displays the kernel's routing table.
	* If there is nothing populated from the `route` command, Host A on `192.168.1.0` can't see any hosts on `192.168.2.0` and vice versa.
	* To therefore be able to reach hosts on `192.168.2.0`, need the `ip route add` command with `ip route add 192.168.2.0/24 via 192.168.1.1`
		* Need to select the interface on the router closest to the network.
	* Running the `route` command again will see the routing table populated.
	* Needs to be configured on all systems, not just `ip route add 192.168.2.0/24 via 192.168.1.1`, but also on the other side with `ip route add 192.168.1.0/24 via 192.168.2.1`
* Default Gateway - `ip route add default via 192.168.2.1`, then you don't need to add individual IPs for everything on the Internet
	* Can also write it as `ip route add 0.0.0.0 via 192.168.2.1`. `0.0.0.0` means all IPs.
	* For two separate routers, one for the outside Internet and one on the internal network.
		* For example, you have the router from above and also the secondary router with an interface of `192.168.2.2`. To add this, run `ip route add 192.168.1.0/24 via 192.168.2.2`
### How to set up a Linux Host as a Router
* Three hosts, Host A, Host B and Host C.
	* Hosts A and B are connected to network `192.168.1.0`
	* Hosts B and C are connected to network `192.168.2.0`
	* Host B has left-hand side IP of `192.168.1.6` and a right-hand side IP of `192.168.2.6`.
	* Host A has `192.168.1.5` and Host C has `192.168.2.5`
* How does Host A talk to Host C?
* Add the following to Host A:
```
ip route add 192.168.2.0/24 via 192.168.1.6
```
* If the packages reach Host C, Host C needs to send a response to Host A.
	* We need to tell Host C that it can reach Host A through Host B.
* We add the following to Host C:
```
ip route add 192.168.1.0/24 via 192.168.2.6
```
* Pinging from either Host A or Host C at this point and no `network unreachable` messages should be present.
* By default in Linux, packets are not forwarded from one interface to the next.
	* For example, packets received on Host B on Eth0 are not forwarded else here on Eth1.
		* This is for security reasons, if Eth0 is on the private network and Eth1 is on the public network, don't want anyone from the public network to easily send messages to the private network.
	* Therefore need to make sure the `cat /proc/sys/net/ipv4/ip_forward` says `1`
	* To quickly change this, run `echo 1 > /proc/sys/net/ipv4/ip_forward`
	* To persist between reboots:
```
/etc/sysctl.conf
net.ipv4.ip_forward = 1
```
* Key commands:
* `ip link` - list modifiable interfaces
* `ip addr` - see IP addresses assigned.
* `ip route` / `route` is to view the routing table.
* `ip route add` - add routes into the routing table.
* To persist changes, need to add them to the `/etc/network/interfaces` file.