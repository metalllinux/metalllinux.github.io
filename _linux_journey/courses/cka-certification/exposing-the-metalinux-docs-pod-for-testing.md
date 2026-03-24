---
title: "Exposing the metalinux-docs Pod for Testing"
category: "cka-certification"
tags: ["cka-certification", "exposing", "metalinux", "docs", "pod"]
---

# Exposing the metalinux-docs Pod for Testing

* Create the test pod:

```
cat <<EOF | tee ~/manifests/metalinux_docs-pod-test.yaml
apiVersion: v1
kind: Pod
metadata:
  name: metalinux-docs-test
  namespace: metalinux-docs
spec:
  replicas: 2
  selector:
    matchLabels:
      app: metalinux-docs
spec:
  containers:
  - name: metalinux-docs-container
    image: metalllinux/metalinux-docs:latest
    ports: 
    - containerPort: 80
  imagePullSecrets:
  - name: dockerhub-secret
EOF
```

* Apply the new pod:

```
kubectl apply -f ~/manifests/metalinux_docs-pod-test.yaml
```
