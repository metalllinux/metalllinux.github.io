---
title: "What Does no_default_route Mean in the Context of Pod Networking?"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "default", "route", "mean", "context"]
---

# What Does no_default_route Mean in the Context of Pod Networking?

A) What does no_default_route mean?
In container networking context, no_default_route would typically be an option to prevent the container network from adding a default route (0.0.0.0/0) to the routing table. This means:

With default route: Containers can reach any destination not explicitly defined in other routes by using the default gateway
Without default route (no_default_route=1): Containers can only reach destinations explicitly defined in the routing table, providing more network isolation

In your case, you're trying to create a network that:

Has its own subnet (10.10.10.0/24)
Has a specific route to 192.168.1.0/24 via 10.10.10.1
Doesn't add a default route for everything else
