---
title: "Helm Components"
category: "cka-certification"
tags: ["cka-certification", "helm", "components"]
---

# Helm Components

* We have the `helm cli`.

    * Used for `helm` actions.
    
* Adds charts and installs the objects listed in the charts.

* A `Release` is created - a single application instance coming from a `helm` chart.

    * Within each `Release`, you can have multiple `Revision`.
    
    * After an upgrade or change of replicas etc is made, a new `Revision` is created.
    
* Can find `helm` charts in a public repository.

* Helm needs a place to store `metadata` --> data about data. 

    * `Helm` stores the `metadata` in the Kubernetes cluster as a `Secret`.
    
        * This way the data survives and the cluster survives. Everyone in the team can access it.
        
* `Charts` are a collection of files.

    * By using `Charts` to install the objects is done.
    
* Nginx web server and service to expose it - good Hello World example.

    * In the Nginx example there are two objects --> `service.yaml` and `deployment.yaml`.
    
`service.yaml`:
```
apiVersion: v1
kind: Service
metadata:
  name: hello-world
spec:
  type: NodePort
  ports:
    - port: 80
    targetPort: http
    protocol: TCP
    name: http
  selector:
    app: hello-world
```

`deployment.yaml`:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world
spec:
  replicas: {{ .Values.replicaCount  }}
  selector:
    matchLabels:
      app: hello-world
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
        - name: nginx
          image: "{{ .Values.image.repository }}"
          ports:
            - name: http
              containerPort: 80
              protocol: TCP
```

There is a `values.yaml` file:

```
replicaCount: 1

image:
  repository: nginx
```

* The `image` and `replicas` above are specified in a different form. This is called `templating`.

* No need to build charts ourselves.

    * What is a good idea however if configuring values in the downloaded chart.
    
* The `values.yaml` file is where the configurable values are stored.

* Another good `helm install` command example: `helm install my-site bitnami/wordpress`

* The syntax is `helm install [release-name][chart-name]`

* Why have a `release` name?

    * This allows us to install multiple releases, based on the same chart.
    
        * Can have another site --> `helm install my-SECOND-site bitnami/wordpress`
          
          * Therefore you can have two separate sites that are different entities.
          
    * A good example is a release of a customer-facing website and the other version which is internal and only visible by the developers.
    
        * Since the two releases are on the same chart, they can transfer any changes over to the customer-facing application and it looks good.
        
* What if we want to deploy a new chart? Good `helm` chart repositories:

    * Appscode
    * TrueCharts
    * Bitnami
    * Community Operators
    
       * All of the above repositories have listed their charts in a single repository --> ArtifactHub.io.
       
       * The `Official` stamped charts are the best ones to use.
