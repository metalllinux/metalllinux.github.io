---
title: "Prerequisite Docker Networking"
category: "cka-certification"
tags: ["cka-certification", "prerequisite", "docker", "networking"]
---

* Example is a server with `Docker` and an `eth0` interface of `192.168.1.10`.
* When a container is `run`, different networking options are available, such as:
```
docker run --network none nginx
```
* With the `none` network, the container is not attached to any network and cannot reach the outside world. Likewise no one from the outside world can reach the container.
* If you run multiple containers (for example running the above command multiple times), they cannot talk to each other or the outside world.
* Next is the `Host` network - the container is attached to the `Host`'s network.
	* No network isolation between the Host and the container.
	* Can make a web application available on port 80.
	* The command for that is `docker run --network host nginx`.
	* No need for additional port mapping.
	* If you try to bring up another container that uses the same port, this won't work (for example running the above command again).
* Third networking option is the `Bridge` network - an internal private network on the host is created. The `Docker` host and containers attach to this.
	* By default, the network has an IP range of `172.17.0.0`
	* Each device that connects receives its own internal private address.
	* How does `Docker` create and manage the network?
		* This `bridge` network (intentionally has a lowercase `b`) is created by default when `Docker` is installed on the host.
		* On the host itself, this `bridge` network is seen as `docker0`. This can be seen from the output of the `ip link` command.
		* When installing `Docker`, it essentially runs `ip link add docker0 type bridge` on the host OS.
		* When checking the network on the host with `ip link`, you'll see that the `docker0` interface is in a `DOWN` state.
		* The `bridge` network is like an interface to the host - but a switch to the namespaces or containers within the host.
		* The interface `docker0` on the host is assigned an IP of `172.17.0.1/24`
		* When a container is created, `Docker` creates a network namespace for it.
		* To list the namespace, run the `ip netns` command.
		* There is a hack required to get the `ip netns` command to list the namespaces created by `Docker`.
		* For example, `ip netns` outputs the following: `b3123<numbers-letters>`
		* If you inspect a `Docker` container, for example `docker inspect 324ghj`, you would see the above namespace as part of a larger string of alphanumeric charactersin the `SandboxID` and `SandboxKey` sections.
		* You can see this if you run `docker network ls`
* How does `Docker` attach the container from its network namespace to the bridge network?
* As said before, the container has two network interfaces on each end.
	* Running the `ip link` command shows the interface attached to the `docker0` interface.
	* Run the same command again with `ip -n b3123<numbers-letters> link` (`-n` is for showing namespaces).
		* The output then shows the other end of the interface in the container namespace, for example `eth0@if8`.
		* The container is also assigned an IP, which can be viewed with the `ip -n b3123<numbers-letters> addr`. In this example, the container is assigned an IP of `172.17.0.3`.
			* Can also view this same information by attaching to the container and seeing the information that way.
* Essentially:
	* Docker creates a namespace and a pair of interfaces.
	* One interface is attached to the container.
	* The other interface is connected to the `bridge` network.
	* The interface pairs can be identified by their numbers - odd and even.
		* `9 and 10`, `7 and 8`, `11 and 12` as examples of paired interfaces.
* Now to focus on Port Mapping
	* For example I want to bring up an `nginx` web server on port 80.
		* In the current `bridge` setup, only other containers on the host or the host itself, can access the `nginx` container.
		* For example, using a simple `curl http://172.17.0.3:80` will view the webpage
		*  Trying the same `curl` command outside of the host will not work.
*  In order to allow external users access, `Docker` provides a port publishing option.
	*  When running containers, map port `8080` on the host to port `80` on the container.
	*  Example command: `docker run -p 8080:80 nginx`
		*  Any traffic to port `8080` on the `Docker` host, will be forwarded to port `80` on the container.
	*  `curl http://192.168.1.10:8080` on the `Docker` host's external interface will then provide access to the container on port 80.
*  How does `Docker` forward traffic from one port to another?
	*  A NAT rule is required, an example of how this can be utilised on the host with `iptables`:
```
iptables \
      -t nat \
      -A PREROUTING \
      -j DNAT
	  --dport 8080 \
      --to-destination 80
```
* The rules are appended to the `PREROUTING` chain.
* Docker does it the same way:
```
iptables \
      -t nat \
      -A DOCKER \
      -j DNAT
	  --dport 8080 \
      --to-destination 172.17.0.3:80
```
* Sets the destination IP to include the container as well.
* You can see the rules that `Docker` creates, when you list the rules in `iptables` with `iptables -nvL -t nat`