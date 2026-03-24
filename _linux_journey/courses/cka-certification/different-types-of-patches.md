---
title: "Different Types of Patches"
category: "cka-certification"
tags: ["cka-certification", "different", "types", "patches"]
---

# Different Types of Patches

* The first method is `inline` - you define the patch within the `kustomization.yaml` file like this:
```
patches:
  - target:
      kind: Deployment
      name: api-deployment
    patch: |-
      - op: replace
        path: /spec/replicas
        value: 5
```

* The other method is using a separate file. Can give path to yaml file that contains all patches.

    * The `Kustomization.yaml` would look like this:
    
```
patches:
  - path: replica-patch.yaml
    target: 
      kind: Deployment
      name: nginx-deployment
```

  * The `replica-patch.yaml` would look like this:
  
```
- op: replace
  path: /spec/replicas
  value: 5
```
