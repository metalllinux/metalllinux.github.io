---
title: "Why You Shouldn't Have a GFS2 Cluster Size of Over 16 Nodes"
category: "general-linux"
tags: ["you", "shouldnt", "gfs2", "cluster", "size"]
---

# Why You Shouldn't Have a GFS2 Cluster Sise of Over 16 Nodes

From my research, the reasons for not supporting more than 16 nodes are the following:

* Distributed Lock Manager Overhead - as you add more nodes, the overhead from lock coordination and metadata updates increases considerably. This can slow down the entire cluster.

* Increased Complexity and Risk - managing quorum, network latency and the state of every node becomes more complex. Increases the risk of split-brain scenarios or miscommunication between nodes.

* [From Red Hat on workload scalability if there are more than 16 nodes](https://docs.redhat.com/pt-br/documentation/red_hat_enterprise_linux/9/html-single/configuring_gfs2_file_systems/index):
> When determining the number of nodes that your system will contain, note that there is a trade-off between high availability and performance. With a larger number of nodes, it becomes increasingly difficult to make workloads scale. For that reason, Red Hat does not support using GFS2 for cluster file system deployments greater than 16 nodes. 

