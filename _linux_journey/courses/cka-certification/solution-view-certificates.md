---
title: "Solution View Certificates"
category: "cka-certification"
tags: ["cka-certification", "solution", "view", "certificates"]
---

* A good way to find certificate files:
```
cat /etc/kubernetes/manifests/kube-apiserver.yaml

cat /etc/kubernetes/manifests/etcd.yaml
```
* Example of checking a common name for a certificate:
```
openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout | grep -i cn
```
* Check under the `/etc/kubernetes/manifests/` directory.
	* In particular you will find the `kube-apiserver` configuration.
* You can identify the keys in the `kube-apiserver` file.
* Anything to do with the `apiserver` is under the `/etc/kubernetes/pki` directory.
* For the `etcd` server certificates, these are under the `/etc/kubernetes/pki` directory.
* How to find the Common Name in the `kube-apiserver` certificate?
	* Check under the `Subject` field with the `openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout ` command.
* With the `etcd-server`, the above steps are ran and the Common Name is selected.

* `kubectl` stops responding to your commands. Someone edited the `/etc/kubernetes/manifests/etcd.yaml` file.
	* Check first with a `kubectl` command to see the output of that. Something like `kubectl get pods`
	* You would observe the following information:
```
The connection to the server controlplane:6443 was refused - did you specify the right host or port?
```
* If you see the above command, it means the `kubectl` utility is not able to communicate with the `kube-apiserver`.
* Then, run `docker ps -a` or if using `crio`, `crictl ps -a`
* Do a `grep` for `kube-apiserver`
* Check the logs of the `kube-apiserver` container with `docker logs <kube-apiserver_container_name>`
* Port `2379` is a port from `etcd`.
* The `kube-apiserver` is not connected to the `etcd` server.
* Then do a `docker ps -a | grep etcd`  and check the logs for that pod.
* Then check the logs for the `etcd` container with `docker logs <etcd_container>`
* For example, an error message of `etcdmain: open /etc/kubernetes/pki/etcd/server-certificate.crt: no such file or directory` is observed.
* The fix is to edit the `/etc/kubernetes/manifests/etcd.yaml` file and correct the `--cert-file`
* Then check the logs of the container again.
* Then the `kube-apiserver` should pick up the change and thus the `kubectl` command will work again when it can communicate with the `kube-apiserver`. No services need to be restarted.

* Next issue is that the `kube-apiserver` stopped again.
* This time when running the `kubectl` command, the following output is seen:
```
Unable to connect to the server: net/http: TLS handshake timeout
```
* We check the `kube-apiserver` container again with `docker ps -a` and check the logs with `docker logs <kube-apiserver>`.
* From the logs, we can see the `kube-apiserver` is unable to connect to port `2379` with an error about `transport: authentication handshake failed...signed by unknown authority`
* Then check the `etcd` container with `docker logs <etcd_server>`
	* Can see `rejected connection from` in the logs.
* Then check under `/etc/kubernetes/manifests/kube-apiserver.yaml`
	* Check the `--etcd-cafile`, `--etcd-certfile`, `--etcd-keyfile`, `--etcd-server`.
	* Also check under `/etc/kubernetes/pki/etcd/ca.crt` and make sure the settings are correct for `/etc/kubernetes/manifests/kube-apiserver.yaml`
* Make the required changes and no further container restarts are needed after that.
* 