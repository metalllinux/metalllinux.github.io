---
title: "Patches List"
category: "cka-certification"
tags: ["cka-certification", "patches", "list"]
---

# Patches List

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

* The `containers` section above expects a list, that's why you see the `-` before `name: nginx` 

* This is using a Replace List with Json6902

* `kustomization.yaml`:
```
patches:
  - target:
      kind: Deployment
      name: api-deployment
    patch: |-
      - op: replace
        path: /spec/template/spec/containers/0
        value:
          name: haproxy
          image: haproxy
```

* The `path` to a container 

* This is the first container, therefore it will have an index of `0`.

* Changes the `containers` `name` and `image` to `haproxy`.

* How to replace a list using the Strategic Merge Path

```
kustomization.yaml

patches:
  - label-patch.yaml
```

* The `label-patch.yaml` file looks like this:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    spec:
      containers:
        - name: nginx
          image: haproxy
```

* How to add an item to a list using a Json6902 patch.

* We have the same deployment configuration, this will be the `nginx` container.

* We want to add a second container to this list:
```
containers:
  - name: nginx
    image: ngin
```

* This is the `kustomization.yaml` file:
```
patches:
  - target:
      kind: Deployment
      name: api-deployment
    patch: |-
      - op: add
        path: /spec/template/spec/containers/-
    value:
      name: haproxy
      image: haproxy
```

* The operation is set to `add`.

* At the end of the `path`, we have a `-`. The dash means to add it at the end of the list. If we wanted to add the containers to the front of the list, this would be a zero.

* The final configuration would look like this:

```
containers:
  - name: nginx
    image: ngin
```

* Adding an item to a list using a Strategic Merge Patch:

* `kustomization.yaml`:
```
patches:
  - label-patch.yaml
```

* The `label-patch.yaml`:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    spec:
      containers:
        - name: haproxy
          image: haproxy
```

* How to delete an item from a list using a Json6902 patch.

* We have two containers and the one with the name of `database` needs to be deleted:
```
containers:
  - name: web
    image: nginx
  - name: database
    image: mongo
```

* `kustomization.yaml` file:
```
patches:
  - target:
      kind: Deployment
      name: api-deployment
    patch: |-
      - op: remove
        path: /spec/template/spec/containers/1
```

* We want to remove the second one, so therefore we use an index of `1`.

* How to delete an item using a Strategic Merge Patch:

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
    spec:
     containers:
       - $patch: delete
         name: database
```

* The `$patch` directive is the delete directive which specifies the container to delete
