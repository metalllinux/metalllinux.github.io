---
title: "How To Troubleshoot Kubernetes Issues"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "troubleshoot", "kubernetes", "issues"]
---

* Define the scope of the problem: Before you do anything else, figure out how many resources are affected by the issue. Is it just a single Pod or node, or are you seeing unusual activity across large parts of your cluster? The scope of the problem helps you determine whether the root cause is linked to a component that affects the entire cluster, or just a specific workload or node.
* Look for error codes: Again, any error codes you can pull from Kubernetes itself are often your best starting-point for identifying likely root causes of problems.
* Identify data sources: The logs and metrics available for troubleshooting Kubernetes can vary widely depending on which observability software you've deployed and which logging options you've configured. Determine which data is available to you, since that information will play a central role in shaping your troubleshooting options.