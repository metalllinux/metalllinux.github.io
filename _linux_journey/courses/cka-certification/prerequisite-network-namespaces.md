---
title: "Prerequisite Network Namespaces"
category: "cka-certification"
tags: ["cka-certification", "prerequisite", "network", "namespaces"]
---

* Used by `Docker` to enable network isolation.
* Containers are separated from the underlying host by namespaces.
* Namespaces are the rooms inside a house, which you provide to each of your children.
* When creating a container, want to make sure it is isolated - it should not see any other processes on the host or any other containers.
* Underlying host has visibility of all processes, including those running inside the containers.
* Running `ps aux` inside the container only shows the process running.
* When running `ps aux` from the host, you see all processes, including those running inside the container.
* Just the same process in both the container and host, but on two different process IDs.
* Network Namespaces - Host has Routing Table and ARP Tables, with information about the rest of the network.
	* Want to hide all of those details from the container.
* A Network Namespace is created for a container, so it has no network visibility anywhere on the host.
* Within the Network Namespace, a container can have its own `Routing Table` and `ARP Table`. It will also have its own network interface, such as `veth0`
* To create a new Network Namespace on a Linux host, run the `ip netns add` command.
	* Example of creating Network Namespaces:
```
ip netns add red
ip netns add blue
```
* To list all Network Namespace:
```
ip netns
```
* To list interfaces on the host, run `ip link`.
* How do we run the same `ip link` command inside the `red` or `blue` namespace?
	* Prefix the `ip link` command with this one:
```
ip netns exec <name> ip link
```
* In the above example, the `ip link` command is executed inside the `red` namespace.
* Another way to write it is using this syntax:
```
ip -n red link
```
* These commands only display the `loopback` interface, cannot see the `eth0` (or main Ethernet interface) on the host.
* Thus this prevents the host container from seeing the interface.
* Similarly with the `ARP` table. Run the `arp` command on the host and you see it filled with entries.
	* Doing the same in the container however, no entries are shown --> `ip netsns exec red arp`.
* The same also goes for the routing table when running the `route` command. `route` shows the command is populated on the host, but has no entries in the `container`.
* How do we establish connectivity between the namespaces themselves?
	* You cannot them together using a virtual cable.
* To create the cable, run this command:
```
ip link add veth-red type veth peer name veth-blue
```
* Specify the two ends, `veth-red` and `veth-blue`.
* Then each interface (`veth-red` and `veth-blue`) needs to be attached to the appropriate interface.
	* Assign the `veth-red` interface to the Red Namespace using this command:
```
ip link set veth-red netns red
```
* Attach the `veth-blue` interface to the Blue Namespace:
```
ip link set veth-blue netns blue
```
* IP address assignment for the Red Namespace:
```
ip -n red addr add 192.168.15.1 dev veth-red
```
* The Blue Namespace is then assigned `192.168.15.2`:
```
ip -n blue addr add 192.168.15.2 dev veth-blue
```
* Then each interface needs to be brought up per namespace:
```
ip -n red link set veth-red up
ip -n blue link set veth-blue up
```
* Then try an example `ping` to each other:
```
ip netns exec red ping 192.168.15.2
```
* Check the ARP table is being filled:
```
ip netns exec red arp
```
* Similarly can also have the Blue Namespace check its ARP Table.
* Then checking the host `ARP` table, cannot see the new namespaces or any traffic there.
	* Has no idea of the interfaces either.
* To connect multiple Namespaces together, need a virtual switch.
	* How do you connect the Namespaces to the Virtual Switch?
* Native solution called `LINUX BRIDGE` and Open vSwitch.
* In the example below, the `LINUX BRIDGE` option is used:
* The switch is provided an interface of `192.168.15.0`
* To create an internal bridge network, add a new interface to the host:
```
ip link add v-net-0 type bridge
```
* This appears as just another interface on the host from the `ip link` command output.
* Bring the interface up with the following:
```
ip link set dev v-net-0 up
```
* Need new cables for connecting Namespaces to the Virtual Switch.
* Need to firstly delete the old cable:
```
ip -n red link del veth-red
```
* The other side (`veth-blue`) is deleted automatically.
* Then create the new cable, this is called:
```
ip link add veth-red type veth peer name veth-red br
```
* The other end is called `veth-red br`, because this connects to the bridge network.
* Create a cable to connect the blue namespace to the network:
```
ip link add veth-blue type veth peer name veth-blue-br
```
* Then run the `ip link set veth-red netns red` command.
	* That attaches one part of the cable to the Red Namespace.
* After that, run `ip link set veth-red-br master v-net-0`
* The same procedure is for the Blue Namespace as well:
```
ip link set veth-blue netns blue
ip link set veth-blue-br master v-net-0
```
* Then need to set up IP addresses.
* Same IP addresses as before:
```
ip -n red addr add 192.168.15.1 dev veth-red
ip -n blue addr add 192.168.15.2 dev veth-blue
```
* Bring the interfaces up:
```
ip -n red link set veth-red up
ip -n blue link set veth-blue up
```
* Thus now 4 interfaces are connected to the same internal network.
* The Virtual Switch also needs an IP address assigned to it:
```
ip addr add 192.168.15.5/24 dev v-net-0
```
* Can therefore ping between the different containers in their separate namespaces.
	* This is ultimately a private network and restricted within the host.
	* The only door from the outside is the one on the Ethernet interface.
	* Nobody outside can access the containers.
* How do we reach a separate host, from one of the containers within a namespace?
	* Need to add an entry into the Routing Table in order to provide a gateway.
* Can add an entry into the Blue Namespace, such as the following:
```
ip netns exec blue ip route add 192.168.1.0/24 via 192.168.15.5
```
* Now it has two IP addresses, one on the Bridge Network on `192.168.15.5`, plus one on the external network of `192.168.1.2`.
* When pinging the external host (on `192.168.1.3`),you can send it, but you receive no response back from the ping.
* NAT is useful to send messages within its own LAN.
* Configuring NAT can be done via `iptables`:
```
iptables -t nat -A POSTROUTING -s 192.168.15.0/24 -j MASQUERADE
```
* The `MASQUERADE` part replaces the `FROM` address of all packets coming in from the source network (in this case `192.168.15.0`) with its own IP address.
* Anyone whom receives the packets outside the network, will think they come from the host and not from the namespace.
* Then pinging again allows the ping to reach the outside world:
```
ip netns exec blue ping 192.168.1.3
```
* For example, the `192.168.1.0` LAN is connected to the Internet.
* Attempt to ping the server on the Internet at `8.8.8.8`:
```
ip netns exec blue ping 8.8.8.8
```
* Check the `route` routing table and have routes to `192.168.1.0`, but nowhere else.
* Then say in that case, to reach any external network, talk to the host:
```
ip netns exec blue ip route add default via 192.168.15.5
```
* Can then properly see the host with:
```
ip netns exec blue ping 8.8.8.8
```
* What about connectivity from the outside world to one of the containers, in this example the Blue Namespace:
	* For example, an application in the Blue Namespace hosts a web app on Port 80.
* The namespaces can only be accessed from the host itself at this time.
* In order for cross-host talk, two options:
	* Give away the identity. Add an IP route entry to the second host. Tells the host that the network 192.168.15, can be reached through the host at `192.168.1.2`
	* The other option is a port forwarding role:
```
iptables -t name -a PREROUTING --dport 80 --to-destination 192.168.15.2
```