---
title: "Customising Chart Parameters"
category: "cka-certification"
tags: ["cka-certification", "customising", "chart", "parameters"]
---

# Customising Chart Parameters

* This is done whilst installing a chart .

* When you install a chart, you also use its default values.

* The Wordpress chart deploys `values.yaml` and `deployment.yaml`

* In `deployment.yaml`, there is a line called `value: {{.Values.wordpressBlogName | quote}}` - this is where the value is displayed/

    * Then under the `values.yaml` file, this has `wordpressBlogName: User's Blog!`. Changing that will change the layout of the Wordpress website.
    
* The `helm install my-release bitnami/wordpress` command pulls the chart and deploys the application immediately - we cannot change any of it during this time.

    * To pass in values, can use the `--set` option. You can pass in any field from the `values.yaml` file, like so:
    ```
    helm install --set wordpressBlogName="Helm Tutorials" my-release bitnami/wordpress
    ```

    * This can be used multiple times to pass commands into the `helm install` command.
    
    * `--set wordpressEmail="john@example.com"` 

* If there are too many values, another option is to move the above `--set` commands to a custom values file.

* You would create a `custom-values.yaml` file with these parameters:
```
wordpressBlogName: Helm Tutorials
wordpressEmail: john@example.com
```

* Then to use the above file, you run:
```
helm install --values custom-values.yaml my-release bitnami/wordpres
```

* What if we want to override the `values.yaml` file itself.

    * Use the `helm pull` command like so:
    
    * `helm pull bitnami/wordpress`
    
   * This pulls the chart in an archived form.
   
       * Then need to unarchive or uncompress it.
       
   * `helm` can also decompress it using `helm pull --untar bitnamin/wordpress`
   
       * This creates a directory called `wordpress` and you can see all of the parts in the chart.
       
       * Can then edit the `values.yaml` that way.
       
   * Then when we want to install the application, we run `helm install my-release ./wordpress` at the local directory. 
