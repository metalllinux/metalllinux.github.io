---
title: "Expose Metalinux Docs As A Service"
category: "rocky-linux-kubernetes-setup"
tags: ["rocky-linux-kubernetes-setup", "expose", "metalinux", "docs", "service"]
---

* Need to set the metalinux-docs node port as a service:

```
kubectl expose deployment metalinux-docs --type=NodePort --port=8080 --name=metalinux-docs-service --dry-run=client -o yaml temp.yaml
```
