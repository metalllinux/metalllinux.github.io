---
title: "Kustomize vs Helm"
category: "cka-certification"
tags: ["cka-certification", "kustomize", "helm"]
---

# Kustomise vs Helm

* `helm` provides modifications to Kubernetes manifests on a per-environment basis.

   * `helm` uses a `go` template to assign variables to properties.
   
* An exmaple deployment configuration:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Values.name }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector: 
     matchLabels:
       app: {{ .Values.name }}
  template:
    metadata:
      labels:
        app: {{ .Values.name }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "nginx:{{ .Values.image.tag }}"
```

* The `go` templating uses two {{  }} on either side.

    * The variable can be changed on a per-environment basis.
    
* To then populate the `.Values.replicaCount` field, we create `values.yaml` and provide it with the following:
```
replicaCount: 1

image:
  tag: "2.4.4"
```

* When the application is deployed, value of 1 is set in the `replicas` property.

* Then under `"nginx:{{ .Values.image.tag }}"` is looks for `tag`, under `image:` --> `tag` as shown above.

* Here is a `helm` project structure that allows us to customise the `values` file:
```
k8s --> environments / templates
```
* Under `environments`, you have `values.dev.yaml`, `values.stg.yaml` and `values.prod.yaml`.

* Under `templates`, you then have `nginx-deployment.yaml`, `nginx-service.yaml`, `db-deployment.yaml` and `db-service.yaml`.

* In `environments`, this stores all of the values we want to set on a per-environment basis.

* `helm` doesn't just do the above - it is a package manager for the app as well.

* `helm` provides extra features like conditional, loops, functions and hooks.

* `helm` templates are not valid YAML - they are using `go`. The templating syntax makes things difficult to read.

* `kustomize` is just regular `yaml`. The base configuration are regular manifests and the `overlays` is also `yaml`
