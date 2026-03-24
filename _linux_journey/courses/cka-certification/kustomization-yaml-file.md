---
title: "Kustomization Yaml File"
category: "cka-certification"
tags: ["cka-certification", "kustomization", "yaml", "file"]
---

# Kustomisation Yaml File

* Example:

* `k8s` directory that contains `nginx-depl.yml` and `nginx-service.yml`.

    * `kustomize` does not look for either of the above files. In fact, it looks for a `kustomization.yaml` file.
    
* The `kustomization.yaml` file will contain all of the resources needed by `kustomize`:

```
# kubernetes resources to be managed by kustomize
resources:
  - nginx-deployment.yaml
  - nginx-service .yaml
  
# Customizations that need to be made
commonLabels:
  company: KodeKloud
```

* The `Cusotmizations that need to be made` section contains all of the changes that we want to apply.

* Once all customisations are done, we run `kustomize build <root directory>`. In the above example, `<root directory>` would be `k8s`.

    * It will input all resources and apply transformations that we have defined.
    
* If you check the terminal output, in the above case you'll see the `nginx` service and the `nginx` deployment output.

* Then you'll see the additions that were made. `commonLabels`:

```
kustomize build k8s/
apiVersion: v1
kind: Service
metadata:
  labels:
    company: KodeKloud
```

* The `kustomize build` command however **does not** **apply/deploy** the Kubernetes resources to the cluster.

* It just outputs what the final configuration file looks like in the terminal.

* If we want to apply what `kustomize build` outputs to the cluster, it needs to be directed to the `kubectl apply` command.
