---
title: "Common Transformers"
category: "cka-certification"
tags: ["cka-certification", "common", "transformers"]
---

# Common Transformers

* How can we use `kustomize` to modify and transform Kubernetes configs.

* These are done using `kustomize transformers`.

    * Here, we will focus on a sub-group called `common transformations`.
    
* In the following examples, we have these `yaml` files:

* `db-depl.yaml`:

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

* `db-service.yaml`:

```
apiVersion: v1
kind: Service
metadata:
  name: db-service
spec:
  selector:
    component: db-depl
  ports:
    - protocol: "TCP"
      port: 27017
      targetPort: 27017
  type: LoadBalancer
```

* We want to apply a common configuration across all `yaml` files. For example, we want to add a label to each of the above `yaml` files for `org: KodeKloud`

* Or even append `-dev` to the end of `api-deployment` as an example.

* We can easily make common configuration changes across all Kubernetes resources.

* Types of Common Transformations:

    * `commonLabel` - adds a label to all Kubernetes resources.
    
    + `namePrefix/Suffix` - adds a common prefix-suffix to all resource names.
    
    * `Namespace` - adds a common namespace to all resources.
    
    * `commonAnnotations` - adds an annotation to all resources.

* Regarding the `commonLabel` transformer.

    * We want to add a label to all resources.
    
    * Go into the `Kustomization.yaml` file and add the following:
    
```
commonLabels:
  org: KodeKloud
```

    * The above then adds the label to all Kubernetes resources.
    
* Namespace Transformer.

    * Puts all Kubernetes resources under a particular namespace.
    
        * This looks like this: `namespace: lab`
        
* For the Prefix/suffix Transformer, can add in the following:

```
namePrefix: KodeKloud-
nameSuffix: -dev
```

    * This will map to the prefix of the name and the suffix of the name as well.
    
* CommonAnnotations Transformer

    * If you want to add commonAnnotations, add the following lines:
    
```
commonAnnotations:
  branch: master
```

* This will then be added to all Kubernetes objects.
