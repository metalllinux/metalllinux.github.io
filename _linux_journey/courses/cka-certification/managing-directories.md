---
title: "Managing Directories"
category: "cka-certification"
tags: ["cka-certification", "managing", "directories"]
---

# Managing Directories

* This example uses a `k8s` directory.

    * Inside are the following yaml files:
    
        * `api-depl.yaml`
        * `api-service.yaml`
        * `db-depl.yaml`
        * `db-service.yaml`

* We can manage Kubernetes manifests spread across multiple directories.

* Usually we go into the `k8s` directory and run a `kubectl apply` to the manifests there.

* For example, over time the amount of yaml files grows.

* Over time however, we move yaml files into sub directories. For example all of the `db` files go into the `db` directory and `api` files go into the `api` directory.

* To deploy manifests in particular directories, you would use the below command as an example:
```
kubectl apply -f k8s/api/
kubectl apply -f k8s/db/
```

* Every time we apply or delete configs, we'd have to run the above commands in each directory and the CI/CD pipelines become murky.

* Therefore a good way is to add a `kustomization.yaml` file just under the `k8s` directory.

* The `kustomization.yaml` file would look like the following in this example:
```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

# kubernetes resources to be managed by kustomize
resources:
  - api/api-depl.yaml
  - api/api-service.yaml
  - db/db-depl.yaml
  - db/db-service.yaml
```

* Now `kustomize` is aware and we'd just need to run this command:
```
kustomize build k8s/ | kubectl apply -f -
```

  * We run the above in the root of the `k8s` directory.
  
* Can apply this natively with Kubernetes using `kubectl apply -k k8s`

* What happens if the amount of directories grows - we now have a `cache` directory as well as a `kafka` directory.

  * That means all of the `kustomization` resources will be pulled in from the above directories.  
  
      * Can also add a `kustomization.yaml` file within each of the sub-directories. The configs will only be imported for that single directory.
      
         * Within the sub-directory `kustomization.yaml` files, we add the following:

* Example below for the `db` directory:

```
k8s/db/kustomization.yaml

resources:
  - db-depl.yaml
  - db-service.yaml
```

* Then in the `root` `k8s` directory, you would have (each of the above directories listed)
```
resources:
  - api/
  - db/
  - cache/
  - kafka/
```

  * It will go into the sub-directory and look for a `kustomization.yaml` file.
  
* Keeps everything clean and neat.

* Then as before, to apply the manifests:
```
kustomize build k8s/ | kutcle apply -f -

```
or 
```
kubectl apply -k k8s/
```
