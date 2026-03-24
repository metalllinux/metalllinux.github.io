---
title: "Image Transformers Demo"
category: "cka-certification"
tags: ["cka-certification", "image", "transformers", "demo"]
---

# Image Transformers Demo

* In the `k8s` directory there is the `api` directory and the `db` directory.

* Each directory has a `depl.yaml`, `service.yaml` and `kustomization.yaml` file per directory.

* In the `db` directory, the `kustomization.yaml` file looks like this:
```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - api/
  - db/
  
commonLabels:
  department: engineering
```

* Another `commonLabels` is:
```
commonLabels:
  feature: api
```

* There is also another one:

```
commonLabels:
  feature: <>
```

* In the root `kustomization.yaml` file, you can set the `namespace` with:
```
namespace: debugging
```

* Adding a suffix and prefix:
```
namePrefix: KodeKloud-
nameSuffix: -web
```

* To apply configs to every single resource, you add this to the root `kustomization.yaml` file.

* For an Annotation Transformation:

```
commonAnnotations:
  logging: verbose
```

* For Image Transformations:

```
resources:
  - db-config.yaml
  - db-depl.yaml
  - db-service.yaml
```

* Specifiying images:

```
images:
  - name: mongo
    newName: postgres
    newTag: "4.2"
```
