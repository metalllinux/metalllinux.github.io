---
title: "Managing Directories Demo"
category: "cka-certification"
tags: ["cka-certification", "managing", "directories", "demo"]
---

# Managing Directories Demo

* In this demo, there is the `k8s` root directory.

* Under that directory are the `api`, `cache` and `db` directories.

* The `api` directory contains:

    * `api-depl.yaml`
    
    * `api-service.yaml`
    
* The `cache` directory contains:

    * `redis-config.yaml`
    
    * `redis-depl.yaml`
    
    * `redis-service.yaml`
    
* The `db` directory contains:

    * `db-config.yaml`
    
    * `db-depl.yaml`
    
    * `db-service.yaml`

* The `db` is a `mongo` database.

* In the `cache` directory there is a ClusterIP service, ConfigMap etc.

* Without Kustomisation, we'd have to go into each directory and run `kubectl apply -f k8s/<DIRECTORY_NAME>`

    * Can do everything in one line actually using `kubectl apply -f k8s/db -f k8s/cache -f k8s/api`

* The above process is cumbersome.

    * Delete all of the above with `kubectl delete -f k8s/db -f k8s/cache -f k8s/api`

* We create a `kustomization.yaml` file with the following:

```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - api/api-depl.yaml
  - api/api-service.yaml
  - cache/redis-config.yaml
  - cache/redis-depl.yaml
  - cache/redis-service.yaml
  - db/db-config.yaml
  - db/db-depl.yaml
  - db/db-service.yaml
```

* Then run `kustomize build k8s/` and print out what the final Kubernetes manifests will look like.

      * It just shows you what it will create - it does not apply anything to the actual Kubernetes cluster.
      
* To apply it to the cluster, need to run `kustomize build k8s/ | kubectl apply -f -`

* It then applies everything to the Kubernetes cluster.

* Then check with `kubectl get pods`.

* Now we want `kustomization.yaml` files in each directory. This would look like this:

* In each sub-directory you apply a `kustomization.yaml` file like so:
```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
```

* Then in the `api` directory for example, we input all files that reside in there:
```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - api-depl.yaml
  - api-service.yaml
```

* You do the same thing for each sub-directory.

* Then in the `root` `kustomization` directory, that `kustomization.yaml` file has the following:

```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - api/
  - cache/
  - db/
```

* Then to deploy you just run the command from above or `kubectl apply -k k8s/`
