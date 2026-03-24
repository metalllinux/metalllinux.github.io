---
title: "How Run Pihole On Microk8S"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "run", "pihole", "microk8s"]
---

sudo snap install microk8s --classic
microk8s enable ingress storage dns metallb
microk8s kubectl create namespace pihole
microk8s kubectl apply -f ./yaml_manifests/pihole.yaml
microk8s kubectl config set-context --current --namespace=pihole
microk8s kubectl get services
microk8s kubectl rollout restart deployment.apps/pihole
* pihole.yaml file used:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: pihole # Name of the deployment
  namespace: pihole # Name of the namespace
spec:
  selector:
    matchLabels:
      app: pihole-app # Name of your application
  replicas: 3 # Number of replicas
  template:
    metadata:
      labels:
        app: pihole-app # Name of your application
    spec:
      containers:
        # Containers are the individual pieces of your application that you want
        # to run.
        - name: pihole # Name of the container
          image: samuel19982/securepihole # The image you want to run
          env:
            - name: TZ
              value: 'Asia/Tokyo'
            - name: WEBPASSWORD
              value: 'vXsGB#kmq6RF'
            - name: PIHOLE_DNS_
              value: '1.1.1.1;8.8.8.8;8.8.4.4'
            - name: QUERY_LOGGING
              value: 'false'
          ports:
            # Ports are the ports that your application uses.
            - containerPort: 80 # The port that your application uses
            - containerPort: 53
            - containerPort: 67
          livenessProbe:
            httpGet:
              path: /admin
              port: 80
            periodSeconds: 3600
          startupProbe:
            httpGet:
              path: /admin
              port: 80
            failureThreshold: 6
            periodSeconds: 10
          volumeMounts:
            - mountPath: /etc/pihole
              subPath: custom.list
              name: pihole-local
      volumes:
        # Volumes are the persistent storage that your application uses.
        - name: pihole-local # Name of the volume
          persistentVolumeClaim:
            claimName: pvc0 # Name of the persistent volume claim
        # Volumes are the persistent storage that your application uses.
---
apiVersion: v1
kind: Service
metadata:
  name:  pihole-dns
  namespace: pihole
spec:
  type: LoadBalancer
  selector:
    app: pihole-app
  ports:
    - protocol: UDP
      port: 53
      targetPort: 53
---
apiVersion: v1
kind: Service
metadata:
  name: pihole
  namespace: pihole
spec:
  type: ClusterIP
  selector:
    app: pihole-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: pihole-ingress
  annotations:
    nginx.ingress.kubernetes.io/affinity: "cookie"
    nginx.ingress.kubernetes.io/session-cookie-name: "pihole-cookie"
    nginx.ingress.kubernetes.io/session-cookie-expires: "172800"
    nginx.ingress.kubernetes.io/session-cookie-max-age: "172800"
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
    nginx.ingress.kubernetes.io/affinity-mode: persistent
    nginx.ingress.kubernetes.io/session-cookie-hash: sha1
spec:
  ingressClassName: public
  rules:
    - host: pi.hole
      http:
        paths:
          - path: /admin
            pathType: Prefix
            backend:
              service:
                name: pihole
                port:
                  number: 80
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: pihole-ingress-2
  annotations:
    nginx.ingress.kubernetes.io/app-root: /admin
    nginx.ingress.kubernetes.io/affinity: "cookie"
    nginx.ingress.kubernetes.io/session-cookie-name: "pihole-cookie"
    nginx.ingress.kubernetes.io/session-cookie-expires: "172800"
    nginx.ingress.kubernetes.io/session-cookie-max-age: "172800"
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
    nginx.ingress.kubernetes.io/affinity-mode: persistent
    nginx.ingress.kubernetes.io/session-cookie-hash: sha1
spec:
  ingressClassName: public
  rules:
    - host: pihole.local
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: pihole
                port:
                  number: 80
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc0
  namespace: pihole
  labels:
    app: pihole
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 20Mi
```