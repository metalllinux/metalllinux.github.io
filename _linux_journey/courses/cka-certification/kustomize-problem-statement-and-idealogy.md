---
title: "Kustomize Problem Statement & Idealogy"
category: "cka-certification"
tags: ["cka-certification", "kustomize", "problem", "statement", "idealogy"]
---

# Kustomise Problem Statement & Idealogy

* What problems does Kustomise try to address.

* We have three environments:

    * dev
    
    * stg
    
    * prod
    
* We want to customise the deployment, so it behaves a little differently in each environment.

* The manifest is the following:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      component: nginx
  template:
    metadata:
      labels:
        component: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
```

* For example, we want to change the amount of `replicas` in the `dev` environment.

* How do we modify it on a per configuration basis.

    * A simple solution is to create three separate directories, one for each variation of the above yaml file.
    
    * `stg` directory would have `replicas` set to `2`, `prod` would be `3` etc.
    
    * To push the changes out, run `kubectl apply -f dev/` for all three environments.
    
    * Not the most optimal or scaleable solution.
    
        * If create `service.yaml` file, this is needed to be copied to all directories.
        
           * Kustomise helps to customise individual environments, without replicating code.
          
* Kustomise has two terms - base config and overlay.

  * `base` config is identical across all environments.
  
    * This also includes default values, which you can override later on.
    
    * An example config is the `nginx` config listed above.
  
  * `overlays` - these allow us to customise behaviour on a per-environment basis.
  
    * An example of an overlay is:
    ```
    spec:
      replicas: 1
    ```
   
   * The above overlay would be `dev`.
     
     * The overlay changes what is in the base config. In the above example, we focus on `replicas`.
     
    * An overlay for `stg` for example:
    ```
    spec:
      replicas: 1
    ```
     
* The `directory` structure is like so:

  * `k8s` --> `base` / `overlays`
  
    * Under `base` you would have:
    
      * `kustomizaton.yaml`
      
      * `nginx-depl.yaml`
      
      * `service.yaml`
      
      * `redis-depl.yaml`
      
    * Under `overlays` you have:
    
      * `dev` --> `kustomization.yaml` and `config-map.yaml`
      
      * `stg` --> `kustomization.yaml` and `config-map.yaml`
      
      * `prod` --> `kustomization.yaml` and `config-map.yaml`
      
* `base` is shared across all environments. `overlay` is changes to specific environments.

* kustomise takes the `base` and `overlay` and mixes them together to create the final manifest.

* kustomise comes built-in with `kubectl`.

  * May want to install `kustomize cli`, as the one that comes with `kubectl` is not the latest version.
  
* With `kustomize`, no need to learn a templating language like `helm`.

  * Complex `helm` charts are difficult to read because of the templating system.
  
* `kustomize` is `yaml` only.
    
