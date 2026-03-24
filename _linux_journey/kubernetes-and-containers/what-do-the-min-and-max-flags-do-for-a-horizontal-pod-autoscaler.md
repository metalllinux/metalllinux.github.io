---
title: "What do the Min and Max Flags do for a Horizontal Pod Autoscaler"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "min", "max", "flags", "horizontal"]
---

# What do the Min and Max Flags do for a Horizontal Pod Autoscaler

In a Kubernetes Horizontal Pod Autoscaler (HPA), the --max and --min flags set the scaling boundaries for your deployment:
--min-replicas (or --min)
Sets the minimum number of pod replicas that should always be running
The HPA will never scale below this number, even if CPU/memory usage is very low
Ensures you always have at least this many pods for availability and baseline capacity
Default is typically 1 if not specified
--max-replicas (or --max)
Sets the maximum number of pod replicas the HPA can scale up to
The HPA will never create more pods than this limit, even if demand is very high
Acts as a safety boundary to prevent runaway scaling that could consume excessive cluster resources
No default - you must specify this value
Example:
kubectl autoscale deployment my-app --cpu-percent=50 --min=2 --max=10
This creates an HPA that:
Maintains at least 2 pods at all times (--min=2)
Will never exceed 10 pods (--max=10)
Scales between 2-10 pods based on 50% CPU utilisation target
