---
title: "Patches Dictionary"
category: "cka-certification"
tags: ["cka-certification", "patches", "dictionary"]
---

# Patches Dictionary

* Another way to update a key using a `Json6902` patch.

* Example `api-depl.yaml` file:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      component: api
  template:
    metadata:
      labels:
        component: api
    spec:
      containers:
        - name: nginx
          image: nginx
```

* For example, we want to update `component: api` under `metadata` to be `component: web`

* Thus the `kustomization.yaml` file would look like this:

```
patches:
  - target:
      kind: Deployment
      name: api-
deployment
    patch: |-
      - op: replace
        path:
/spec/template/metadata/labels/component
        value: web
```

* We use `replace`, because we want to replace the component with a new value.

* Now how to do the above using a `Strategic Merge Patch`

* The `kustomization.yaml` file would look like this:
```
patches:
  - label-patch.yaml
```

* Then we look at `label-patch.yaml`, we see:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    metadata: 
      labels:
        component: web
```

* Can do the above inline, but in this case it is a separate file.

* Now how to add a new key.

* For example we want to add in a second label that says `org: KodeKloud`

* The `kustomization.yaml` file would look like this:
```
patches:
  - target:
      kind: Deployment
      name: api-deployment
      patch: |-
        - op: add
          path: /spec/template/metadata/labels/org
      value: KodeKloud
```

* The `op` is changed from `replace` to `add`.

  * This `adds` a new key to the dictionary.
  

* The final result is:
```
org: KodeKloud
```

* Add a Dictionary using a Strategic Merge Patch

* `kustomization` file:

```
patches:
  - label-patch.yaml
```

* label-patch.yaml file:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    metadata:
      labels:
        org: kodekloud
```

* How to remove a key from a dictionary using a `Json6902` patch.

* `kustomization.yaml` file:

```
patches:
  - target:
      kind: Deployment
      name: api-deployment
    patch: |-
      - op: remove
        patch:
          /spec/template/metadata/labels/org
```

* How to remove a key from a dictionary using a Strategic Merge Patch:

* `kustomization.yaml`:
```
patches:
  - label-patch.yaml
```

* `label-patch.yaml`:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    metadata:
      labels:
        org: nul
```
