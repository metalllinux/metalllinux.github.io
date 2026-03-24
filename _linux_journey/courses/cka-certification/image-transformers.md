---
title: "Image Transformers"
category: "cka-certification"
tags: ["cka-certification", "image", "transformers"]
---

# Image Transformers

* This allows us to modify an image that a specific deployment or container is going to use via Kustomise.

* We have the following `Web-depl.yaml` file as an example:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      component: web
  template:
    metadata:
      labels:
        component: web
    spec:
      containers:
        - name: web
          image: nginx
```

* Then define the `kustomization.yaml` file:
```
images:
  - name: nginx
    newName: haproxy
```

* The `name` part makes reference to the specific image we want to replace.

    * It looks through all Kubernetes configs and checks for containers that use `nginx`.
    
    * Then we replace the image with `newName`, which is `haproxy`.
    
* The name under the `kustomization.yaml` file specifies the name of the image, not the container.

    * It looks specifically for `nginx` in the above case.
    
* When set, this changes the yaml file to the following:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      component: web
  template:
    metadata:
      labels:
        component: web
    spec:
      containers:
        - name: web
          image: haproxy
```

* We can also change the tag of the image using the following in the `kustomization.yaml` file as well:
```
images:
  - name: nginx
  newTag: 2.4
```

* This would then change the yaml file to the following:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      component: web
  template:
    metadata:
      labels:
        component: web
    spec:
      containers:
        - name: web
          image: nginx:2.4
```

* You can also change the image and the tag as well by specifying the new image name and tag in the `kustomzation.yaml` file:
```
images:
  - name: haproxy
  newTag: 2.4

```
