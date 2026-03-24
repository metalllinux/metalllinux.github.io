---
title: "Creating a Storage Class"
category: "rocky-linux-kubernetes-setup"
tags: ["rocky-linux-kubernetes-setup", "creating", "storage", "class"]
---

# Creating a Storage Class

* Create a storage class like so:

```
cat <<EOF | tee ~/manifests/metalinux_docs-storage_class.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: metalinux-docs-storage-class
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: kubernetes.io/no-provisioner
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
EOF
```

* Apply the above:

```
kubectl apply -f <file.yaml>
```

* See the sotrage class at:

```
kubectl get sc
```
