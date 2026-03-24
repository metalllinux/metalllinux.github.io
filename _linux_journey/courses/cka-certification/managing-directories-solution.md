---
title: "Managing Directories - Solution"
category: "cka-certification"
tags: ["cka-certification", "managing", "directories", "solution"]
---

# Managing Directories - Solution

* Example `kustomization.yaml` file:

```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

# kubernetes resources to be managed by kustomize
resources:
  - db/db-config.yaml
  - db/db-depl.yaml
  - db/db-service.yaml
  - message-broker/rabbitmq-config.yaml
  - message-broker/rabbitmq-depl.yaml
  - message-broker/rabbitmq-service.yaml
  - nginx/nginx-depl.yaml
  - nginx/nginx-service.yaml
```

* An example of creating a `kustomization.yaml` file per directory:
```
controlplane ~/code ➜  tree
.
└── k8s
    ├── db
    │   └── kustomization.yaml
    ├── kustomization.yaml
    ├── message-broker
    │   └── kustomization.yaml
    └── nginx
        └── kustomization.yaml
4 directories, 12 files
```

* What the `kustomization.yaml` file would look like for `k8s/db` for example:
```
resources:
  - db-depl.yaml
  - db-service.yaml
  - db-config.yaml
```

* In the root `k8s` directory, what the `kustomization.yaml` file would also look like:
```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

# kubernetes resources to be managed by kustomize
resources:
  - db/
  - message-broker/
  - nginx/
#Customizations that need to be made
```

* How you would then apply the customisations:
```
controlplane ~/code ➜  kubectl apply -k /root/code/k8s/
--------------OR---------------
controlplane ~/code ➜  kustomize build /root/code/k8s/ | kubectl apply -f -
```
