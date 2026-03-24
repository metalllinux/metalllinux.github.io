---
title: "Lifecycle Management with Helm"
category: "cka-certification"
tags: ["cka-certification", "lifecycle", "management", "helm"]
---

# Lifecycle Management with Helm

* Each time we pull in a chart and install it, a release is created.

    * A release is a package or collection of Kubernetes objects.
    
       * The good thing about this system, is that `upgrades`, `downgrades` and uninstalls can be performed without touching other releases.
       
       * Each release can be managed independently, even if they are all based on the same chart.
       
* How to install a specific version of a release, you can do:

```
helm install nginx-release bitnami/nginx --version 7.1.0
```

* For example, if there are security vulnerabilities in a web app, have to make changes to more `nginx` objects. Or if a `secret` needs to be created for a while.

    * This can cause issues when tracking the changes.
    
* Helm can automatically upgrade all objects with one command.

* Use the `kubectl describe pod <pod_name>` to find out more about the version of the image in use.

* In order to upgrade, we tell `helm` we need to upgrade and then specify the chart that it is released on.

* We run the following command: `helm upgrade nginx-release bitnami/nginx`

* During the upgrade process, the old pod is destroyed and a new one is created.

    * Then we can see the new version of the pod by finding the name, then check the `kubectl describe`.
    
* `helm` can keep track of its current state and past states.

* Run the `helm list` commands to show the current releases.

* Run the `helm history <nginx-release (for example)>` to see more information about a particular release.

* Helm allows for rollback. 

* To rollback to a previous revision, run `helm rollback <nginx-release (for example)> <revision number>`

    * Technically however it does not go back to revision 1, it creates a new revision called revision 3.
    
       * There will be a note in the description of what is changed.
       
* `helm` cannot upgrade everything without administrative passwords.

* Depending on the app, `helm` may need access to passwords (of a database for example), it order to `rollback` and make changes.

* `helm` backs up the declaration files or persistent objects.

* Regarding `rollbacks` and data, a rollback won't restore the data.

    * For example, a MySQL database. The pods will be rolled back, however the actual database, its data will remain the same.
    
* There are options to take consistent backups of a database before a `rollback`, these are done by chart hooks.

