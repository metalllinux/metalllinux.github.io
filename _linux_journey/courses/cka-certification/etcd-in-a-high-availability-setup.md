---
title: "Etcd In A High Availability Setup"
category: "cka-certification"
tags: ["cka-certification", "etcd", "high", "availability", "setup"]
---

* What is `ETCD`? Distributed and reliable key-value store - this is Simple, Secure and Fast.
* A key-value store has information stored in the form of documents or pages.
* For example:
```
key      value
Name     John Doe
```
* The above files can be in any format or structure.
* Changes in one file does not affect other files.
* When data becomes complex however, usually transact in JSON or YAML.
* What does "Distributed" mean?
* It is possible to have your data store across multiple servers.
	* Have three servers running etcd. All running an identical copy of the database.
	* If you lose one, you still have two copies of the data.
	* You can write to any instance and read from any instance.
	* `etcd` ensures that the same copy of data is available on all instances at the same time.
		* How does it do this?
			* Reads are no problem - all of the data is the same across all nodes and can be read from all nodes.
			* However with Writes, for example if write requests come in via two different instances? Which one goes through?
				* For example, one node gets `Name John` and the other node gets `Name Joe`. Cannot have two pieces of data on two different nodes.
				* `etcd` does not process the writes on each node. Only one of the instances is responsible for processing the writes.
				* Internally, the two nodes elect a leader among them.
				* In the instances, one node becomes the leader and the others become the followers.
					* If the data comes in through the leader node, then the leader processes the write.
						* If the data comes in through other nodes, but those nodes are not the leader, the data is forwarded onto the leader node itself and then the node processes the writes.
				* When writes a processed, the leader ensures that writes are distributed to other instances in the cluster.
* A Write is only considered complete, if the leader gets consent from other members in the cluster.
* How do they elect the leader among themselves? How do they ensure a write is propagated across all instances?
	* `ETCD` does consensus via a RAFT system.
		* When the cluster is setup, we have three nodes that don't have a leader elected.
			* The RAFT algorithm uses random timers for initiating requests.
				* A random timer is started on the three managers.
					* The first one to finish the timer sends a request to the other nodes, requesting permission to become the leader.
						* The other nodes receive the request and respond with their vote and the node assumes the leader role.
							* The leader node then sends out pings at regular intervals, assuming the role of the leader.
								* If the other nodes don't receive an update from the leader (for example with connectivity issues), the nodes re-initiative an election process amongst themselves. A new leader is then identified.
* A Write is only considered complete, when it is replicated to all other instances in the cluster.
	* The `ETCD` cluster is highly available, so even if a node is lost, it should still function without issue.
		* If a node goes down, a Write is still considered "Complete", if it can be written to the majority of nodes in the cluster.
			* If the node that is down comes back online, then the data is copied there as well.
* The calculation for Quorum is `N/2 + 1`. Quorum is the minimum number of nodes available, for the cluster to function properly and make a successful write.
	* For any size cluster, Quorum is the total amount of nodes, divided by 2, plus 1.
	* A Quorum of 3 nodes = 3/2 + 1 = 2.5 ~=2.
		* If there is ever a .5 remaining, consider the whole number only.
	* A Quorum of 5 nodes = 5/2 + 1 = 3.5 ~= 3.
	* A Quorum of 1 node = 1
		* If you lose the 1 node, everything disappears.
	* Quorum of 2 nodes = 2
		* Even if there are two instances in the cluster, the majority is still 2.
		* This doesn't offer any value, as Quorum cannot be met.
			* That is why it is recommended to have at least 3 instances in an etcd cluster.
				* It offers a fault tolerance of at least 1 node.
* Quorum chart:
![Screenshot From 2025-05-22 22-20-59.png](../../_resources/Screenshot%20From%202025-05-22%2022-20-59.png)
* When deciding on the number of Master Nodes, it is recommended to select an odd number. In the above table, this would be `3`, `5` or `7`.
	* With an even number of nodes, there is the possibility of a cluster failing due to network segmentation and leave the cluster without quorum in certain scenarios.
		* No matter how the network segments, the cluster has a higher chance of staying alive.
* To install `etcd` on a server:
	* Download the latest available binary with `wget`.
	* Extract the `etcd-v<version_number>-linux-amd64.tar.gz` tarball.
* Move the file over:
```
mv etcd-v<version_number>-linux-amd64/etcd* /usr/local/bin/
```
* Make the `etcd` directories:
```
mkdir -p '/etc/etcd /var/lib/etcd'
```
* Copy the certificate:
```
cp ca.pem kubernetes-key
```
* Then the `etcd` service needs to be configured.
* Section of note is:
```
--initial-cluster peer-1=https://${PEER1_IP}:2380,peer-2=https://${PEER2_IP}:2380 \\
```
* The above is how each `etcd` service knows it is part of a cluster and where its peers are.
* Then once installed, use the `etcdctl` utility to store and retrieve data.
* The `etcdctl` utility has two API versions, V2 and V3.
	* The commands are different per version.
	* Version 2 is default.
* Set an environment variable to fix this the API versions and use V3:
```
export ETCDCTL_API=3 
```
* Then run the `etcdctl` command and in this case the key-pair value is `name john`:
```
etcdctl put name john
```
* To retrieve data, run:
```
etcdctl get name
```
* This would retrieve the following:
```
etcdctl get name
```
* To get all keys, run this command:
```
etcdctl get / --prefix --keys-only
```
* How many nodes should an HA setup have? The answer is 3.
* For the best quorum, use 5 instances and that gives you 3 quorum and then a fault tolerance of 2.
* So ultimately we have 3 Master Nodes with `ETCD` running on them.
	* Then we also have two Worker Nodes.
		* A Stacked Topology means the `ETCD` servers are on the Master Nodes as well. 