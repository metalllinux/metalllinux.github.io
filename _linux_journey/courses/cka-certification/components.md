---
title: "Components"
category: "cka-certification"
tags: ["cka-certification", "components"]
---

# Components

* This is a feature of `kustomize`.

    * Provides the ability to define reusable pieces of configuration logic (resources + patches) that can be included in multiple overlays.
    
    * Useful in situations where applications support multiple optional features that need to be enabled only in a subset of overlays.
    
   * Components are essentially reusable blocks of Kubernetes configurations.
   
       * All of the config-maps etc go into a Component.
       
* For example, we have an application that is deployed on different configurations:

    * `base`
    
    * `dev`
    
    * `Premium` - Premium Customers
    
    * `Self-hosted`
    
* Our application has an optional feature called `Caching`, this is available for Premium and Self-hosted customers only.

    * Need to enable a Redis database and all of the configs with Redis to enable caching.
    
* An external Postgres database is also needed in the `dev` / `Premium` spaces.

* Where do we put the caching config in the directory structure?

    * Only self-hosted and Premium should have this.
    
    * Can copy the config into Premium and Self-hosted, however that causes double-work.
      
          * Components are reusable blocks of code that we can use in all of the overlays.
          
* At the root directory, we add another directory called `Components` and this includes `caching` and `db`.

    * Contains all of the configs that we need for a specific feature.

* For all of the overlays that import the database, they can import the database component.

* Under `components/db` you would have the following:

    * `kustomization.yaml`
    
    * `deployment-patch.yaml`
    
    * `postgres-depl.yaml`
    
* The `postgres-depl.yaml` file is a deployment for a `postgres` database.

* The `postgres-depl.yaml` looks like this:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      component: postgres
  template:
     metadata:
       labels:
         component: postgres
     spec:
       containers:
         - name: postgres
           image: postgres
```

* The `kustomization.yaml` file looks like this:

```
apiVersion:
kustomize.config.k8s.io/v1alpha1
kind: Component

resources:
  - postgres-depl.yaml
  
secretGenerator:
  - name: postgres-cred
    literals:
      - password=postgres123

patches:
  - deployment-patch.yaml
```

* `resources` is where we input the yaml file we need.

* `secretGenerator` is where we need to add a password.

* `patches` is an environment variable, so it provides the password to the database.

* `deployment-patch` looks like this:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    spec:
      containers:
        - name: api
          env:
            - name: DB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: postgres-cred
                  key: password
```

* There is also the `kustomization.yaml` file in the Overlays, we need to import the `Components` from above.

* Example of `Overlay/premium/kustomization`:

```
bases:
  - ../../base
  
components:
  - ../../components/db
```
