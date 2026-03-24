---
title: "Create a Horizontal Pod Autoscaler for the metalinux_docs-deployment"
category: "rocky-linux-kubernetes-setup"
tags: ["rocky-linux-kubernetes-setup", "create", "horizontal", "pod", "autoscaler"]
---

# Create a Horizontal Pod Autoscaler for the metalinux_docs-deployment

* Create the manifest:

```
cat <<EOF | tee ~/manifests/metalinux_docs-horizontal_pod_autoscaler.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: metalinux_docs-horizontal_pod_autoscaler
  namespace: metalinux-docs
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: metalinux-docs
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource: cpu
      target: 
        type: Utilization
        averageUtilization: 50
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300 
EOF
```

* Apply the manifest:

```
kubectl apply -f ~/manifests/metalinux_docs-horizontal_pod_autoscaler.yaml
```
