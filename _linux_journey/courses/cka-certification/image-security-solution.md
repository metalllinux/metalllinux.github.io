---
title: "Image Security Solution"
category: "cka-certification"
tags: ["cka-certification", "image", "security", "solution"]
---

* The secret type you choose for the Docker registry is `docker-registry`.
* When changing an image:
```
kubectl edit deployment web
```
* Good example definition file:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    deployment.kubernetes.io/revision: "2"
  creationTimestamp: "2025-03-10T13:03:09Z"
  generation: 2
  labels:
    app: web
  name: web
  namespace: default
  resourceVersion: "1286"
  uid: 59701771-ebc6-4336-90c9-cd06d245c01b
spec:
  progressDeadlineSeconds: 600
  replicas: 2
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      app: web
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: web
    spec:
      containers:
      - image: myprivateregistry.com:5000/nginx:alpine
        imagePullPolicy: IfNotPresent
        name: nginx
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
status:
  availableReplicas: 2
  conditions:
  - lastTransitionTime: "2025-03-10T13:03:14Z"
    lastUpdateTime: "2025-03-10T13:03:14Z"
    message: Deployment has minimum availability.
    reason: MinimumReplicasAvailable
    status: "True"
    type: Available
  - lastTransitionTime: "2025-03-10T13:03:09Z"
    lastUpdateTime: "2025-03-10T13:07:20Z"
    message: ReplicaSet "web-7968dfbf7f" is progressing.
    reason: ReplicaSetUpdated
    status: "True"
    type: Progressing
  observedGeneration: 2
  readyReplicas: 2
  replicas: 3
  unavailableReplicas: 1
  updatedReplicas: 1
```
* Example command of creating a secret object:
```
kubectl create secret docker-registry private-reg-cred --docker-username=dock_user --docker-password=dock_password --docker-server=myprivateregistry.com:5000 --docker-email=dock_user@myprivateregistry.com
```
* Configure the deployment to use the new secret to pull images:
```

```