---
title: "Create a Persistent Volume for metalinux-docs"
category: "rocky-linux-kubernetes-setup"
tags: ["rocky-linux-kubernetes-setup", "create", "persistent", "volume", "metalinux"]
---

# Create a Persistent Volume for metalinux-docs

```
cat <<EOF | tee ~/manifests/metalinux_docs-persistent_volume.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: metalinux-docs-persistent-volume
spec:
  capacity:
    storage: 100Mi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteMany
  hostPath: 
    path: /pv/metalinux-docs-persistent-volume
EOF
```

* Apply the manifest:

```
kubectl apply -f ~/manifests/metalinux_docs-persistent_volume.yaml
```
