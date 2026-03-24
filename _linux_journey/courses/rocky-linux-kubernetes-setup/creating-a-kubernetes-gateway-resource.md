---
title: "Creating a Kubernetes Gateway Resource"
category: "rocky-linux-kubernetes-setup"
tags: ["rocky-linux-kubernetes-setup", "creating", "kubernetes", "gateway", "resource"]
---

# Creating a Kubernetes Gateway Resource

* Create this file:

```
cat <<EOF | tee ~/manifests/metalinux_docs-gateway_resource.yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: metalinux_docs-gateway
  namespace: metalinux-docs
spec:
  gatewayClassName: nginx
  listeners:
  - name: http
    protocol: HTTP
    port: 80
EOF
```

* Apply the file:

```
kubectl apply -f <file.yaml>
```

* Find the gateway by running one of these commands:

```
kubectl get gateway
kubectl get gateway -n <namespace>
```
