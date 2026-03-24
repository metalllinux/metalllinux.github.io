---
title: "Create a Vertical Pod Autoscaler for the metalinux-docs deployment"
category: "rocky-linux-kubernetes-setup"
tags: ["rocky-linux-kubernetes-setup", "create", "vertical", "pod", "autoscaler"]
---

# Create a Vertical Pod Autoscaler for the metalinux-docs deployment

* Create the manifest:

```
cat <<EOF | tee ~/manifests/metalinux_docs-vertical_pod_autoscaler.yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metdata: 
  name: metalinux_docs-vertical_pod_autoscaler
  namespace: metalinux-docs
spec:
  targetRef: 
    apiVersion: apps/v1
    kind: Deployment
    name: metalinux-docs
  updatePolicy: 
    updateMode: "Auto"
EOF
```

* Apply the manifest:

```
kubectl apply -f ~/manifests/metalinux_docs-vertical_pod_autoscaler.yaml
```
