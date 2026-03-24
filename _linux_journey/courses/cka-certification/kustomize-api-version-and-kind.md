---
title: "Kustomize API Version and Kind"
category: "cka-certification"
tags: ["cka-certification", "kustomize", "api", "version", "kind"]
---

# Kustomise API Version and Kind

* In the `kustomization.yaml` file, you can set the `apiVersion` and `kind`:

```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

# kubernetes resources to be managed by kustomize
resources:
  - nginx-deployment.yaml
  - nginx-service .yaml
  
# Customizations that need to be made
commonLabels:
  company: KodeKloud
```

* Worth hard coding the above values, in case there are breaking changes in the future.
