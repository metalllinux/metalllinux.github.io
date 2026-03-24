---
title: "Tls Certificates Viewing"
category: "cka-certification"
tags: ["cka-certification", "tls", "certificates", "viewing"]
---

* How do you see all of the certificates in the cluster.
* If you deploy a Kubernetes cluster from scratch, you deploy all certificates yourself:
```
cat /etc/systemd/system/kube-apiserver.service
```
* Tools such as `kubeadm` take care of configuring the cluster for us:
```
cat /etc/kubernetes/manifests/kube-apiserver.yaml
```
* `kubeadm` deploys all of the services as pods.
* To perform a health check, look at everything in the system.
* A good way is to make a spreadsheet. The spreadsheet should contain:
	* `Components`
	* `Type` (Server, Client etc)
	* `Certificate Path`
	* `CN Name`
	* `ALT Names`
	* `Organization`
	* `Issuer`
	* `Expiration`
* For the certificate files, if the server is deployed using `kubeadm`, look for the certification files:
```
--client-ca-file=/etc/kubernetes/pki/ca.crt
--etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt
--etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt
--etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key
--kubelet-client-certificate=/etc/kubernetes/pki/apiserver-kubelet-client.crt
--kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key
--tls-cert-file=/etc/kubernetes/pki/apiserver.crt
--tls-priate-key-file=/etc/kubernetes/pki/apiserver.key
```
* Note down the location of each certificate.
* Take each certificate and examine in closer.
* A good start is the `apiserver.crt` file:
```
/etc/kubernetes/pki/apiserver.crt
```
* To decode the certificate and view the details, run:
```
openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout
```
* Check the `Subject` name, for example:
```
Subject: CN-kube-apiserver
```
* Then the Alternative Names as well:
```
X509v3 Subject Alternative Name:
	DNS:master, DNS:kubernetes, DNS:kubernetes.default, DNS:kubernetes.default.svc, DNS:kubernetes.default.svc.cluster.local, IP Address:10.96.0.1, IP Address:172.17.0.27
```
* Check the validity of the certificate for the expiry date:
```
Not After : Feb 11 05:39:20 2020 GMT
```
* Check the Issuer of the certificate:
```
Issuer: CN-kubernetes
```
* Use the above procedure on the rest of the certificates.
* Certificate requirements are in the Kubernetes documentation.
* For issues, check service logs:
```
journalctl -u etcd.service -l
```
* Look for words in the above log such as `ClientTLS: cert`, `bad certificate`
* Can also look at logs via the `kubectl logs <pod>` command.
* If the `kube-apiserver` or `etcd-server` are down, the `kubectl` commands do not work.
* Then you need to go one level lower in `Docker` to then fetch the logs.
* `docker ps -a` to show all logs.
* `docker logs <container_ID>` command to then show the logs from the container.
	* Should then see the same output as if you had ran `kubectl`.