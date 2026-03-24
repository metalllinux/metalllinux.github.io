---
title: "Patches Intro"
category: "cka-certification"
tags: ["cka-certification", "patches", "intro"]
---

# Patches Intro

* Kustomise patches provide another method for changing Kubernetes configurations.

* Patching provides a more surgical approach to changing certain Kubernetes resources.

* If you want to change something in a few objects, just use a `kustomize` patch.

    * Updating the number of replicas in a deployment would use a `kustomize` patch.
    
* To create a patch, we need to provide three different parameters.

    * The first one is Operation Type - what do we want to do with it.
    
        * The three common types are `add`, `remove` and `replace`.
        
   * For example you have a list of containers in a deployment and you wanted to add a container to the list. This would be an `add` operation.
   
   * `Remove` would be the opposite - removing a container from the list.
   
   * `Replace` - taking a value and replacing it with another value.
   
      * For example, the base config has a replica of 5, you change that to 10.
      
* `Target` - what resource should the patch be applied on:
  * `Kind`
  * `Version/Group`
  * `Name`
  * `Namespace`
  * `labelSelector`
  * `AnnotationSelector`
    * Can mix and match all of the above depending on the Kubernetes object you want to match on.

* `Value` - what is the value that will either be replaced or added with (only needed for add/replace operations).

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

* For example, we want to change the above example yaml file's `name: api-deployment` to `name: web-deployment`.

* The `kustomization.yaml` file would look like this:
```
patches:
  - target:
      kind: Deployment
      name: api-deployment
      
    patch: |-
      - op: replace
        path: /metadata/name
        value: web-deployment
```

* All of the patch configuration is done under the `patches` property.

* The above `|-` means inline patch.

* `path` is the specific property that we want to update.

    * It follows the yaml tree.
    
* Another example is using the above deployment.

* However, we want to change `replicas: 1`

* The `kustomzation.yaml` would look like this:
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

* In `kustomization`, there are two ways to define the patch:

    * The above method which is known as `Json 6902 Patch`
    
* Part of rfc6902

* The other `kustomization` syntax is `strategic merge patch`. An example is:
```
patches:
  - patch: |-
      apiVersion: apps/v1
      kind: Deployment
      metadata:
        name: api-deployment
      spec:
        replicas: 5
```

    * Copies an original API deployment files and uses the same syntax.
    
    * `metadata` says the object we want to update.
    
    * With `replicas`, merges the value of `5`.
    
    * Can even mix and match.
    
    * The above is more readable however, since it is more Kubernetes-focused.
