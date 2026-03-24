---
title: "Deploy Pi Hole Pod In Kubernetes"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "deploy", "hole", "pod", "kubernetes"]
---

`kubectl create namespace pihole`
```
kubectl -n pihole create secret generic pihole-admin \
	--from-literal='password=password'
```
* Helm installation.
```
sudo curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
sudo chmod 700 get_helm.sh
sudo ./get_helm.sh
```
`helm repo add mojo2600 https://mojo2600.github.io/pihole-kubernetes/`
* values.yaml
```
# might increase replica in the future
replicaCount: 1
maxUnavailable: 0

image:
  # fixiate the version to use
  # https://hub.docker.com/r/pihole/pihole
  tag: "2023.03.1"

# I use Edge Router for DHCP
serviceDhcp:
  enabled: false

serviceDns:
  type: LoadBalancer
  # assign the preferred IP from the pool
  loadBalancerIP: 192.168.10.250
  annotations:
    # this annotation make sure we can use the same IP for the two services
    metallb.universe.tf/allow-shared-ip: pihole

serviceWeb:
  type: LoadBalancer
  loadBalancerIP: 192.168.10.250
  annotations:
    metallb.universe.tf/allow-shared-ip: pihole

resources:
  limits:
    cpu: 200m
    memory: 256Mi
  requests:
    cpu: 100m
    memory: 128Mi

persistentVolumeClaim:
  enabled: true

admin:
  # use the secret we just created
  existingSecret: "password"

extraEnvVars:
  TZ: America/Los_Angeles
```
`helm install pihole mojo2600/pihole -f values.yaml --namespace pihole`