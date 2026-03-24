---
title: "Create the metalinux-docs Namespace"
category: "rocky-linux-kubernetes-setup"
tags: ["rocky-linux-kubernetes-setup", "create", "metalinux", "docs", "namespace"]
---

# Create the metalinux-docs Namespace

```
cat <<EOF | tee ~/manifests/metalinux_docs-namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
     name: metalinux-docs
EOF
```

* Apply the manifest:

```
kubectl apply -f ~/manifests/metalinux_docs-namespace.yaml
```
