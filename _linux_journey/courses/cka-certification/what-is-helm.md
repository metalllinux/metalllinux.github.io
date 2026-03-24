---
title: "What is Helm"
category: "cka-certification"
tags: ["cka-certification", "helm"]
---

# What is Helm

* Kubernetes is good a managing complex structures.

* Humans struggle with complexity.

* A simple Wordpress site needs the following:

    * Deployment for pods. 
    
    * A Persistent Volume to store the database.
    
    * A Persistent Volume Claim.
    
    * A Service to expose the web server running in a pod.
    
    * A Secret to store credentials.
    
    * Other items if you want periodic backups etc.
    
        * We would need a separate yaml file for every object in the above example.
        
        * Need to run `kubectl apply` on each yaml file to create each object.
        
        * You would need to open each yaml file and change each to your needs.
        
            * Then need to upgrade parts of the application, therefore editing more yaml files.
            
        * One solution is writing all object declarations in a single yaml file.
        
            * Makes it difficult to find certain object arguments to change.
        
* Kubernetes doesn't care about the application being ran.

    * All Kubernetes knows is that we declared various objects and try to make each exist in the cluster.
    
    * It looks at all of the little pieces instead.
    
* Helm however takes into consideration the Application, as well as the little pieces. It is known as a package manager for Kubernetes.

    * In the previous example with Wordpress, Helm looks at all of those objects and sees them as one big package as a group.
    
    * We don't tell Helm which objects we want it to touch, just which application to act on.
    
    * Based on the package name, it knows which objects to change and how.
    
   * Imagine downloading each file of a game separately. This is bad. An installer helps to put the files into the right locations.
   
       * Helm does the same thing for the yaml files and Kubernetes objects as part of the application.
       
       * Example: `helm install wordpress`
       
       * Can customise settings by setting the right values at install time.
       
           * Don't need to change values in every yaml file - have a single location where we can state every custom setting. An example is `values.yaml`.
           
           * Can upgrade the application with a single command: `helm upgrade wordpress` - Helm knows what individual objects need changing.
           
               * Due to Helm keeping track of all of the changes, this allows us to `rollback` versions by using `helm rollback wordpress`.
               
               * To remove the app , we use `helm uninstall wordpress`.
               
                   * Removes all objects.
                   
* Allows us to treat Kubernetes Applications as apps and don't need to micromanage each object.
       
       
