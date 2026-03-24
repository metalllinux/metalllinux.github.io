---
title: "How To Check The Pod Count Of An Sosreport"
category: "rocky-linux"
tags: ["rocky-linux", "check", "pod", "count", "sosreport"]
---

`cat ./<SOS_REPORT>/df | grep "/var/lib/kubelet/pods" | wc -l`