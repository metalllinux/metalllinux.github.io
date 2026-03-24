---
title: "Overlays"
category: "cka-certification"
tags: ["cka-certification", "overlays"]
---

# Overlays

* Kustomise allows us to take a base Kubernetes config and customise it on a per-environment basis.

   * Tweak on a `dev`, `stg` and `prod`.

* In `kustomize`, the `k8s/base` directory is what is applied to everything.

    * Then in the `k8s/overlays` directory, this will have directories containing `dev`, `stg` and `prod` with their own `kustomization.yaml` files and `config-map.yaml`.
    
* The base `kustomization` file looks like this:
```
resources:
  - nginx-depl.yaml
  - service.yaml
  - redis-depl.yaml
```

* The base `nginx-depl.yaml` file looks like this:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 1
```

* An example overlay of `/dev/kustomization`:
```
bases:
  - ../../base
  
patch: |-
      - op: replace
      path: /spec/replicas
      value: 2
```

* We update the value of `replicas` in the above to a value of `2`.

* You can have new configs in your `overlays` set of directories, that weren't defined in the base config.

    * For example under `k8s/overlays/prod`, you can have these files:
    
```
kustomization.yaml
config-map.yaml
grafana-depl.yaml
```

* The `grafana-depl.yaml` doesn't exist in the base directory.

  * You can add as many brand new resources as you want in an environment specific directory.
  
* The above `grafana-depl.yaml` would be imported using the following:
```
prod/kustomization.yaml

bases:
  - ../../base
  
resources:
  - grafana-depl.yaml

patch: |-
      - op: replace
        path: /spec/replicas
        value: 2 
```

* Kustomise doesn't force you into a specific directory structure.

* No need to place everything into the `base` directory. The sub-directories also do not matter.
