---
title: "Creating a Deployment with Replicas of the Documentation Website"
category: "rocky-linux-kubernetes-setup"
tags: ["rocky-linux-kubernetes-setup", "creating", "deployment", "replicas", "documentation"]
---

# Creating a Deployment with Replicas of the Documentation Website

```
cat <<EOF | tee ~/manifests/metalinux_docs-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: metalinux-docs
  namespace: metalinux-docs
  labels:
    app: metalinux-docs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: metalinux-docs
  template:
    metadata:
      labels:
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

* Apply the manifest:

```
kubectl apply -f ~/manifests/metalinux_docs-deployment.yaml
```
