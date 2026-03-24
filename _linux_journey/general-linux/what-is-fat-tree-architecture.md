---
title: "What Is Fat Tree Architecture"
category: "general-linux"
tags: ["fat", "tree", "architecture"]
---

Fat-tree architecture is a network design that’s especially common in high-performance computing (HPC) clusters, where it helps ensure high, non-blocking bandwidth between a large number of nodes. In a fat-tree network, switches near the network’s “root” aggregate more links (or “fatter” connections) than those at the edge, effectively balancing traffic and reducing bottlenecks. This design contrasts with a simple hierarchical tree, where every link has the same capacity regardless of its position in the network.