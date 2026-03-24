---
title: "Taints & Tolerations Vs Node Affinity"
category: "cka-certification"
tags: ["cka-certification", "taints", "tolerations", "node", "affinity"]
---

* Three nodes and three pods in three colours.
* Want apply the appropriate coloured pod on the same coloured node.
* We apply the right Tolerations to the same pod.
* Similarly the right Taint is applied to the nodes/
* A combination of Taints and Tolerations and Node Affinity can ensure that pods are 100% applied to the right node they need to be applied to.