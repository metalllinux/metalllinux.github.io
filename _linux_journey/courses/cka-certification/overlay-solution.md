---
title: "Overlay Solution"
category: "cka-certification"
tags: ["cka-certification", "overlay", "solution"]
---

# Overlay Solution

* Good overview of a  `kustomization` structure with Overlays:

```
controlplane ~/code ➜  ls -lR /root/code/k8s
/root/code/k8s:
total 8
drwxr-xr-x 2 root root 4096 Jun 23 10:18 base
drwxr-xr-x 6 root root 4096 Jun 23 10:18 overlays

/root/code/k8s/base:
total 16
-rw-r--r-- 1 root root 381 Jun 23 10:18 api-deployment.yaml
-rw-r--r-- 1 root root 112 Jun 23 10:18 db-configMap.yaml
-rw-r--r-- 1 root root  81 Jun 23 10:18 kustomization.yaml
-rw-r--r-- 1 root root 665 Jun 23 10:18 mongo-depl.yaml

/root/code/k8s/overlays:
total 16
drwxr-xr-x 2 root root 4096 Jun 23 10:18 dev
drwxr-xr-x 2 root root 4096 Jun 23 10:18 prod
drwxr-xr-x 2 root root 4096 Jun 23 10:18 QA
drwxr-xr-x 2 root root 4096 Jun 23 10:18 staging

/root/code/k8s/overlays/dev:
total 8
-rw-r--r-- 1 root root 627 Jun 23 10:18 api-patch.yaml
-rw-r--r-- 1 root root  56 Jun 23 10:18 kustomization.yaml

/root/code/k8s/overlays/prod:
total 12
-rw-r--r-- 1 root root 173 Jun 23 10:18 api-patch.yaml
-rw-r--r-- 1 root root  91 Jun 23 10:18 kustomization.yaml
-rw-r--r-- 1 root root 299 Jun 23 10:18 redis-depl.yaml

/root/code/k8s/overlays/QA:
total 4
-rw-r--r-- 1 root root 54 Jun 23 10:18 kustomization.yaml

/root/code/k8s/overlays/staging:
total 8
-rw-r--r-- 1 root root 118 Jun 23 10:18 configMap-patch.yaml
-rw-r--r-- 1 root root  60 Jun 23 10:18 kustomization.yaml
```

* Example question, what type of image will be used for the api-deployment?

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
          image: memcached
```

* How many replicas in api-deployment will get deployed in `prod`:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  replicas: 2
.
.
.
```

* What will be the value of the environment variable MONGO_INITDB_ROOT_PASSWORD in the mongo-deployment container in the staging environment?

* In the mongo-deployment, mongodb container grabs the value for the MONGO_INITDB_ROOT_PASSWORD env variable from the db-cred configmap. 
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: db-creds
data:
  username: mongo
  password: superp@ssword123
```

* When deploying to `prod`, how many pods are created?
```
resources:
  - redis-depl.yaml
```

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis-deployment
spec:
  replicas: 2
.
.
.
```

* How many environment variables are set on the nginx container in the api-deployment in dev environment?
```
In the base configuration for api-deployment.yaml, 1 environment variable DB_CONNECTION is set. 
In the dev overlay, a patch adds 2 extra environment variables DB_USERNAME & DB_PASSWORD.

...
      containers:
        - name: api
          image: nginx
          env:
            - name: DB_CONNECTION
              value: db.kodekloud.com
...

apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
.
.
.
      containers:
        - name: api
          image: nginx
          env:
            - name: DB_USERNAME
              valueFrom:
                configMapKeyRef:
                  name: db-creds
                  key: username
            - name: DB_PASSWORD
              valueFrom:
                configMapKeyRef:
                  name: db-creds
                  key: password
```

* Next question: Update the api image in the api-deployment to use caddy docker image in the QA environment.

Perform this using an inline JSON6902 patch.
```
patches:
  - target:
      kind: Deployment
      name: api-deployment
    patch: |-
      - op: replace
        path: /spec/template/spec/containers/0/image
        value: caddy
```

```
kubectl apply -k /root/code/k8s/overlays/QA
```

* Next question:

```
A mysql database needs to be added only in the staging environment.



Create a mysql deployment in a file called mysql-depl.yaml and define the deployment name as mysql-deployment.



Deploy 1 replica of the mysql container using mysql image and set the following env variables:



- name: MYSQL_ROOT_PASSWORD
  value: mypassword




NOTE: Please ensure to deploy the changes committed in the staging environment before validation.
```

* Answer:

```
First let's create overlays/staging/mysql-depl.yaml as per the requirements:

apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      component: mysql
  template:
    metadata:
      labels:
        component: mysql
    spec:
      containers:
        - name: mysql
          image: mysql
          env:
            - name: MYSQL_ROOT_PASSWORD
              value: mypassword

Now update the staging environment kustomization.yaml file to include the deployment file we created earlier: 


resources:
  - mysql-depl.yaml
  
  
Applying the changes to k8s cluster for staging environment:

kubectl apply -k /root/code/k8s/overlays/staging
```
