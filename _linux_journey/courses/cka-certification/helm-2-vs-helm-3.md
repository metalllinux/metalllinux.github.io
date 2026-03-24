---
title: "Helm 2 vs. Helm 3"
category: "cka-certification"
tags: ["cka-certification", "helm", "helm"]
---

# Helm 2 vs. Helm 3

* There are charts online for both of the `Helm` versions.

* History of releases:

    * Helm 1.0 - February 2016
    
    * Helm 2.0 - November 2016
    
    * Helm 3.0 - November 2019
    
* Kubernetes improved and thus so did Helm.

* Helm 3 is in use in this course.

* Helm has the `helm cli` installed on the machine, this lets you run various actions against the cluster.

* During the era of Helm 2, Kubernetes did not have `Role Based Access Control` or `Custom Resource Definitions`.

    * To allow Helm 2 to work effectively, `Tiller` had to be installed in the Kubernetes Cluster.
    
    * Whenever Helm 2 needed to run a specific operation, it would need to go through `Tiller` and `Tiller` would communicate with Kubernetes.
    
* Security concerns with Helm 2 and Tiller. Tiller ran with escalated privileges - problematic and allows any user access in the cluster.

* When RBAC and Custom Resource Definitions were added, `tiller` was removed in Helm 3.

    * RBAC allows to define user permissions.
    
        * RBAC sets the same permissions of the user regardless of tool used.
        
* Helm 3 includes the `3-Way Strategic Merge Patch`. 

* Helm has a snapshot feature. 

    * Firstly, install an application and this example can be `helm install wordpress`, This creates `Revision: 1`.
    
    * Then running `helm upgrade wordpress` creates `Revision: 2`.
    
    * Can then rollback to `Revision: 1` using `helm rollback wordpress`. Moves the package. However, while the content will be `Revision: 1`, the system counts this as `Revision: 3`.
    
        * When running the `rollback` command, Helm compares the previous charts. 
        
* What happens in this situation:

    * Create `Revision: 1` with `helm install wordpress`.
    
    * Then a user updates the image with `kubectl set image wordpress wordpress:5.8-apache`
    
        * Running the `kubectl set image` command does not create a Revision in Helm.
        
    * When you `rollback`, there are no two versions to compare to. Only `Revision: 1` is available.
    
       * With Helm 2, this doesn't help us - a manual change made by the user is still active, even with a `rollback`.
       
    * With Helm 3 however, it cares about the `Live State` of the Kubernetes objects. It checks the `Live State`, Current Chart, Previous Chart 
    
* When upgrading with Helm 2, all custom changes will be lost, since those don't stay in the system when moving between charts.

    * Helm 3 however looks at the chart and the live state - therefore it performs the upgrade and preserves anything that may have been added.

