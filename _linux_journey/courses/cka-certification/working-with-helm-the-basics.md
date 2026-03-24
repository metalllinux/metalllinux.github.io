---
title: "Working with Helm - The Basics"
category: "cka-certification"
tags: ["cka-certification", "working", "helm", "basics"]
---

# Working with Helm - The Basics

* All operations are ran using `helm cli`.

* To invoke the `helm cli`, run `helm`.

* Can run `helm --help`

* To see what repository-related commands we can take, just run:
```
helm repo --help
```

* Can dig even deeper with sub-commands and what parameters those support.

    * `helm repo update --help`

* All charts are in artifacthub.io

    * Check for the Official / Verified publisher badge.
    
* It is up to the chart developers to decide what is important in the subscription page.

* The `helm search` command looks for an additional sub-command:
```
helm search wordpress
```

    * However, need to add `hub` or `repo` after the above. `hub` refers to `artifacthub`. If you want to search in particular repositories, use the `repo` option.
    
* We can deploy the application using two commands:

* The below example is with Wordpress:

```
helm repo add bitnami https://charts.bitnami.com/bitnami
```

* It has to be added as a repository to our local `helm` setup, when we run the `install` command, `helm` can then find the chart that needs to be installed.

* Deploy the application to the cluster using the `helm install my-release bitnami/wordpress`

* You get good instructions on how to use the Wordpress install.

* When a chart is deployed, it is deployed as a Release. To view all existing releases, run the `helm list` command.

    * Also good to see what hasn't been updated in a long time.
    
* Deleting the app by hand would need all traces of the cluster removed.

* When we have the name of the release, can remove all Kubernetes objects with one simple command:
```
helm uninstall my-release
```

* The `helm repo` command can be used to add, remove, list etc `helm` repositories.

* The `helm repo list` command lists existing repositories.

* The `helm repo update` command is similar to a `sudo apt get update` function.

    * This is good to run often so the latest repo information is available and nothing becomes stale
