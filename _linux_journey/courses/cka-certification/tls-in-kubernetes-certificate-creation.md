---
title: "Certificate Authority Setup"
category: "cka-certification"
tags: ["cka-certification", "tls", "kubernetes", "certificate", "creation"]
---

* There are different ways to generate certificates for a cluster:
	* `EASYRSA`
	* `OPENSSL`
	* `CFSSL`
### Certificate Authority Setup
* Create a private key using `openssl`:
```
openssl genrsa -out ca.key 2048
```
* Create a certificate signing request:
```
openssl req -new -key ca.key -subj "/CN=KUBERNETES-CA" -out ca
```
* The signing request is like a regular certificate with all of your details, but no signature.
* Sign the certificate with this method:
```
openssl x509 -req -in ca.csr -signkey ca.key -out ca.crt
```
* This is self-signed by the CA itself using the private key from `openssl genrsa -out ca.key 2048`.
* The CA now has its own Private Key and Root Certificate files.
### Admin User Setup
* Create a private key:
```
openssl genrsa -out admin.key 2048
```
* Generate a Certificate Signing Request (CSR):
```
openssl req -new -key admin.key -sub "/CN=kube-admin" -out admin.csr
```
* The above `CN=kube-admin` is the name that the `kubectl` client authenticates with.
* The name can be anything, it doesn't have to be `kube-admin`.
* Generate a signed certificate:
```
openssl x509 -req -in admin.csr -CA ca.crt -CAkey ca.key -out admin.crt
```
* The above `admin.crt` file is the certificate that the admin user will use to authenticate to the Kubernetes cluster.
* The `admin.crt` is the validated user ID and the key is the password.
* To add users into specific groups, add them using the `O=<group>` flags:
```
openssl req -new -key admin.key -subj "/CN=kube-admin/O=system:masters" -out admin.csr
```
### Client Certificates
* The above Admin Process is the same process that each client component takes to generate its own certificates.

* The `kube-scheduler` is part of the Kubernetes Control Plane, so its name must be prefixed with `system:`
	* Same for `kube-controller-manager`
	* Same for `kube-proxy`

* For the `admin` side, you can use the certificates instead of a username and password in the REST API call:
```
* admin.crt
* admin.key
```
* Then include these in the `kube-apiserver` call:
```
curl https://kube-apiserver:6443/api/v1/pods --key admin.key --cert admin.crt --cacert ca.cert
```
* You can also do the above and add it to the `kube-config.yaml` file instead:
```
apiVersion: v1
clusters:
- cluster:
	certificate-authority: ca.crt
	server: https://kube-apiserver:6443
  name: kubernetes
kind: Config
users:
- name: kubernetes-admin
  users:
- name: kubernetes-admin
  user:
    client-certificate: admin.crt
	client-key: admin.key
```

* All of the above clients in order to verify with each other, need a coy of the CA's root certificate, that being `ca.crt`.

* If a cluster is set up for high availability, the `etcd-server` needs the following key scheme:
```
etcd server:

etcdserver.crt
etcdserver.key
etcdpeer1.crt
etcdpeer1.key
```
* The `etcd peer 1`:
```
etcdpeer1.crt
etcdpeer1.key
```
* The `etcd peer 2`:
```
etcdpeer2.crt
etcdpeer2.key
```
* When the certificates are generated, specify the keys in the `etcd.yaml` file:
```
- --key-file=/path-to-certs/etcdserver.key
- --cert-file=/path-to-certs/etcdserver.crt
- --peer-cert-file=/path-to-certs/etcdpeer1.crt
- --peer-client-cert-auth=true
- --peer-key-file=/etc/kubernetes/pki/etcd/peer.key
- --peer-trusted-ca-file=/etc/kubernetes/pki/etcd/ca.crt
- --trusted-ca-file=/etc/kubernetes/pki/etcd/ca.crt
```

* The `kube-apiserver` is the most popular, everyone talks to it and all communication goes through it.
	* It goes through a lot of different names: `kubernetes`, `kubernetes.default`, `kubernetes.default.svc`, `kubernetes.default.svc.cluster.local` or IP addresses.
		* All of the above names need to be present in the certificate.
* To generate the certificates:
	* `open ssl genrsa -out apiserver.key 2048`
	* `openssl req -new -key apiserver.key -subj "/CN=kube-apiserver" -out apiserver.csr`
* For this command, you have to create an `openssl` configuration file:
```
openssl req -new -key apiserver.key -subj "/CN=kube-apiserver" -out apiserver.csr --config openssl.cnf
```
```
[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name
[v3_req]
basicConstraints = CA:FALSE
keyUsage = nonRepudiation
subjectAltName = @alt_names
[alt_names]
DNS.1 = kubernetes
DNS.2 = kubernetes.default
DNS.3 = kubernetes.default.svc
DNS.4 = kubernetes.default.svc.cluster.local
IP.1 = 10.96.0.1
IP.2 = 172.17.0.87
```
* Include all of the DNS names that the `kube-apiserver` goes by.
* Sign the certificate:
```
openssl x509 -req -in apiserver.csr -CA ca.crt -CAkey ca.key -out apiserver.crt
```
* The location of the configurations is passed into the `kube-apiserver`'s configuration file:
```
ExecStart=/usr/local/bin/kube-apiserver
--etcd-cafile=/var/lib/kubernetes/ca.pem
--etcd-certfile=/var/lib/kubernetes/apiserver-etcd-client.crt
--etcd-keyfile=/var/lib/kubernetes/apiserver-etcd-client.key
--kubelet-certificate-authority=/var/lib/kubernetes/ca.pem
--kubelet-client-certificate=/var/lib/kubernetes/apiserver-kubelet-client.crt
--kubelet-client-key=/var/lib/kubernetes/apiserver-kubelet-client.key
--client-ca-file=/var/lib/kubernetes/ca.pem
--tls-cert-file=/var/lib/kubernetes/apiserver.crt
--tls-private-key-file=/var/lib/kubernetes/apiserver.key
```

* The `kubelet server` is an HTTPS server that runs on each Worker Node.
	* The `kube-apiserver` talks to this, as well as deciding which pods need to be scheduled.
* Create the certificates and then add them to the following file:
```
kubelet-config.yaml
kind: kubeletConfiguration
apiVersion: kubelet.config.k8s.io/v1beta1
authentication:
  x509:
    clientCAFile: "/var/lib/kubernetes/ca.pem"
authorization
  mode: Webhook
clusterDomain: "cluster.local"
clusterDNS:
  - "10.32.0.10"
podCIDR: "$(POD_CIDR)"
resolvConf: "/run/systemd/resolve/resolv.conf"
runtimeRequestTimeout: "15m"
tlsCertFile: "/var/lib/kubelet/node01.crt"
tlsPrivateKeyFile: "/var/lib/kubelet/node01.key"
```
* Must do the above for each node in the cluster.
* The `kubectl` nodes:
	* The nodes need to have the right names in the right formats.
	* The naming scheme is the following: `system:node:<node_name>`
	* Like for example `system:node:node01`
* The nodes must be added to a group called `system:nodes`.