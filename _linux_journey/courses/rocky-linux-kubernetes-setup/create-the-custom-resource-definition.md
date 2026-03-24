---
title: "Create the Custom Resource Definition"
category: "rocky-linux-kubernetes-setup"
tags: ["rocky-linux-kubernetes-setup", "create", "custom", "resource", "definition"]
---

# Create the Custom Resource Definition

```
cat <<EOF | tee ~/manifests/metalinux_docs-custom_resource_definition-crontabs.yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  # name must match the spec fields below, and be in the form: <plural>.<group>
  name: metalinuxdocs.stable.crontabs.com
spec:
  # group name to use for REST API: /apis/<group>/<version>
  group: stable.crontabs.com
  # list of versions supported by this CustomResourceDefinition
  versions:
    - name: v1
      # Each version can be enabled/disabled by Served flag.
      served: true
      # One and only one version must be marked as the storage version.
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                cronSpec:
                  type: string
                image:
                  type: string
                replicas:
                  type: integer
  # either Namespaced or Cluster
  scope: Namespaced
  names:
    # plural name to be used in the URL: /apis/<group>/<version>/<plural>
    plural: metalinuxdocs
    # singular name to be used as an alias on the CLI and for display
    singular: metalinuxdoc
    # kind is normally the CamelCased singular type. Your resource manifests use this.
    kind: MetalinuxDoc
    # shortNames allow shorter string to match your resource on the CLI
    shortNames:
    - ct
EOF
```

* Create the custom resource definition:

```
kubectl apply -f ~/manifests/metalinux_docs-custom_resource_definition-crontabs.yaml
```

* Check the Custom Resource Definition was created:

```
kubectl get crd
```
