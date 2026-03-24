---
title: "Additional Considerations for coredns When Tailscale is Installed"
category: "rocky-linux-kubernetes-setup"
tags: ["rocky-linux-kubernetes-setup", "additional", "considerations", "coredns", "tailscale"]
---

# Additional Considerations for coredns When Tailscale is Installed

* Edit the `config` map:

```
kubectl edit configmap coredns -n kube-system
```

* Look for a line that says `forward .`

* Change the line to look like this to pull from `Cloudflare`'s DNS:

```
forward . 1.1.1.1
```

* Once saved and exited, manually restart the `coredns` pods with:

```
kubectl rollout restart deployment coredns -n kube-system
```

* Good command for checking the last x amount of logs a pod generated:

```
kubectl logs -n kube-system -l k8s-app=kube-dns --tail=100
```

* Good tests to check for DNS from within a pod:

```
kubectl exec -n metalinux-docs -it busybox-dns-test -- /bin/sh

# Try internal DNS
nslookup kubernetes.default

# Try external DNS (via CoreDNS)
nslookup cloudflare.com

# Ping CoreDNS IP directly
ping 10.96.0.10
```
