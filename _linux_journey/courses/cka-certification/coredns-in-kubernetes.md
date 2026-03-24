---
title: "Coredns In Kubernetes"
category: "cka-certification"
tags: ["cka-certification", "coredns", "kubernetes"]
---

* How does one pod address another pod.
* Kubernetes over DNS will show how that is possible.
* For example, two pods with two IP addresses. One pod is called `test` and has an IP of 10.244.1.5. The other pod is called `web` and has an IP of `10.244.2.5`.
* To easily have them resolve each other, add an entry into each of their `/etc/hosts` files.
* In the `hosts` file, all you need to add is each pods `hostname` and `IP` address. Don't need both.
* If have thousands of pods, this setup is not practical.
* Just put the IP entries into a central DNS server instead.
* In each pod's `/etc/resolv.conf` file, you would add this entry, if the DNS server's IP was `10.96.0.10`:
```
nameserver 10.96.0.10
```
* Every time a new pod is created, add a record into the DNS server and add the DNS server into the `/etc/resolv.conf` file.
* The DNS servers look like this:
```
10-244-2-5  10.244.2.5
10-244-1-5  10.244.1.5
10-244-2-15 10.244.2.15
```
* Instead of adding the hostname of the pod, it adds the IP address again, but replaces it with dashes.
* Kubernetes deploys a DNS server in the cluster.
* Prior to version 1.12, the DNS server used was `kube-dns`.
* With v1.12 and onwards of Kubernetes, the recommended version is CoreDNS.
* CoreDNS is deployed as a pod in the `kube-system` namespace.
* Are actually deployed as two pods for redundancy as part of a ReplicaSet.
* The pod runs a CoreDNS executable.
* CoreDNS requires a configuration file called `Corefile`:
* Within the file, a number of plugins are configured:
```
.:53 {
    errors
    health
    kubernetes cluster.local in-addr.arpa ip6.arpa {
        pods insecure
        upstream
        fallthrough in-addr.arpa ip6.arpa
    }
    prometheus :9153
    proxy . /etc/resolv.conf
    cache 30
    reload

}
```
* Plugins are configured for handling errors, monitoring metrics, cache and more.
* The plugin that allows CoreDNS to work with `Kubernetes` is the `kubernetes` plugin.
    * This is where the top level domain name of the cluster is set. In the above example is `cluster.local`
* The above `pods` option is responsible for creating a record for pods in the cluster.
    * This is referring to the hostname to IP conversion.
* Any pod that tries to resolve an address, like `www.duckduckgo.com`, it will first check in the CoreDNS pod's `/etc/resolv.conf` file.
* The `/etc/resolv.conf` file is set to use the nameserver from the Kubernetes node.
* The CoreDNS file is also passed into the pod as a config map object:
```
kubectl get configmap -n kube-system
```
* What address do the pods use to reach the DNS server?
* When CoreDNS is deployed, it creates a service to make it available to other parts of the cluster.
* The service's name is `kube-dns' by default.
* The IP address of the pod, is configured as the nameserver on the pods.
* DNS configurations on pods are done by Kubernetes automatically.
* The `kubelet` is responsible for this.
* If you check the configuration file of the `kubelet`, you'll find the IP inside of it:
```
cat /var/lib/kubelet/config.yaml
clusterDNS:
- 10.96.0.10
clusterDomain: cluster.local
```
* Once the pods are configured with the right nameserver, can then access other services.
* If you try to manually look up the service using the host-lookup command, it will return the fully qualified domain name of the web service.
* For example:
```
host web-service

web-server.default.svc.cluster.local has address 10.107.37.188
```
* How does it look up the full name?
* The DNS server itself under `/etc/resolv.conf` has an entry called `nameserver 10.96.0.10`:
```
search default.svc.cluster.local svc.cluster.local cluster.local
```
* To reach a pod however, need to enter the full pod name:
```
host 10-244-2-5.default.pod.cluster.local

10-244-2-5.default.pod.cluster.local has address 10.244.2.5
```
