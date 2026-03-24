---
title: "Patches Solution"
category: "cka-certification"
tags: ["cka-certification", "patches", "solution"]
---

# Patches Solution

* How many `nginx` pods will be created?
```
patches:
  - target:
      kind: Deployment
      name: nginx-deployment
    patch: |-
      - op: replace
        path: /spec/replicas
        value: 3
```

* What are labels that will be applied to the mongo development?
```
- op: add
  path: /spec/template/metadata/labels/cluster
  value: staging

- op: add
  path: /spec/template/metadata/labels/feature
  value: db
```

* What is the target port of the mongo-cluster-ip service?
```
- target:
      kind: Service
      name: mongo-cluster-ip-service
    patch: |-
      - op: replace
        path: /spec/ports/0/port
        value: 30000

      - op: replace
        path: /spec/ports/0/targetPort
        value: 30000
```

* How many containers are there in the API pod?
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    spec:
      containers:
        - name: memcached
          image: memcached
```

* What path in the mongo container is the mongo-volume pointed at?
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    spec:
      containers:
        - name: memcached
          image: memcached
```

* Create a Strategic Merge Patch to remove the memcached container:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    spec:
      containers:
        - $patch: delete
          name: memcached
```

+ Then run:
```
kubectl apply -k /root/code/k8s/
```

* Create an inline Json6902 patch in `kustomization.yaml` to remove the label `org: KodeKloud` from the mongo-deployment:
```
patches:
  - target:
      kind: Deployment
      name: mongo-deployment
    patch: |-
      - op: remove
        path: /spec/template/metadata/labels/org
```
* Then run:
```
kubectl apply -k /root/code/k8s/
```
