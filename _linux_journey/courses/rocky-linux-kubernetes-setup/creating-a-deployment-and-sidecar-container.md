---
title: "Creating a Deployment and a Sidecar Container"
category: "rocky-linux-kubernetes-setup"
tags: ["rocky-linux-kubernetes-setup", "creating", "deployment", "sidecar", "container"]
---

# Creating a Deployment and a Sidecar Container

* The following command must be ran:

```
sh -c "while true; do echo 'Log entry' >> /var/log/app/app.log; sleep 5; done"
```

* The sidecar container has to run this command:

```
tail -f /var/log/app/app.log
```

* Deploy the following manfiest:

```
cat <<EOF | tee ~/manifests/metalinux_docs-deployment_with_sidecar.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: logging-deployment
  namespace: logging-ns
spec:
  replicas: 1
  selector:
    matchLabels:
      app: logger
  template:
    metadata:
      labels:
        app: logger
    spec:
      volumes:
        - name: log-volume
          emptyDir: {}
      containers:
      - name: app-container
        image: busy-box
        volumeMounts:
          - name: log-volume
            mount: /var/log/app
        command:
          - sh
          - c
          - "while true; do echo 'Log entry' >> /var/log/app/app.log; sleep 5; done"
      - name: log-agent
        image: busybox
        volumeMounts:
          - name: log-volume
            mount: /var/log/app
        command:
          - tail
          - -f
          - /var/log/app/app.log
EOF
```

* Apply the file:
```
kubectl apply -f <file.yaml>
```

* Check if it is logging:

```
kubectl logs logging-deployment-<container-name> -c log-agent -n logging-ns
```
