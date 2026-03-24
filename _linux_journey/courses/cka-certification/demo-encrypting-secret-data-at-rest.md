---
title: "Demo Encrypting Secret Data At Rest"
category: "cka-certification"
tags: ["cka-certification", "demo", "encrypting", "secret", "data"]
---

* Firstly start with `kubectl create secret generic --from-literal=key=supersecret`
* Then do `kubectl get secret` and `kubectl describe <secret>`
* Extract the `secret` with `kubectl get secret <secret> -o yaml`.
* Then check the secret with `echo "scrambled secret" | base64 --decode`
* How is the data stored in the `etcd` server?
* Need the `etcd-client` package (at least for Ubuntu 24.04).
* To run, use `etcdctl`, see this page:
* https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/ and https://pwittrock.github.io/docs/tasks/administer-cluster/encrypt-data/
* To get the `secret`, run the following command:
```
ETCDCTL_API=3 etcdctl --endpoints <IP>:<PORT> \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  get /registry/secrets/default/<SECRET_NAME> | hexdump -C
```
* The data is stored in an unencrypted format.
* Need to enable encryption at rest in etcd
* To check if encryption at rest is enabled, run this command:
```
ps -aux | grep kube-api | grep "encryption-provider-config"
```
* Also worth checking `ls /etc/kubernetes/manifests/` as well and check for the `encryption` option.
* Encryption at rest configuration:
```
kind: EncryptionConfig
apiVersion: v1
resources:
  - resources:
    - secrets
    providers:
    - identity: {}
    - aesgcm:
        keys:
        - name: key1
          secret: c2VjcmV0IGlzIHNlY3VyZQ==
        - name: key2
          secret: dGhpcyBpcyBwYXNzd29yZA==
    - aescbc:
        keys:
        - name: key1
          secret: c2VjcmV0IGlzIHNlY3VyZQ==
        - name: key2
          secret: dGhpcyBpcyBwYXNzd29yZA==
    - secretbox:
        keys:
        - name: key1
          secret: YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXoxMjM0NTY=
```
* In the above configuration, `identity: {}` means that no encryption is set.
* In the above configuration, multiple keys can be provided. The `keys` are used by the encryption algorithm.
* The order of the keys matters.
	* For example in the above, `identity: {}` means that no encryption is used at all in the above example, since it is at the top.
* An encryption config file:
```
kind: EncryptionConfig
apiVersion: v1
resources:
  - resources:
    - secrets
    providers:
    - aescbc:
        keys:
        - name: key1
          secret: <BASE 64 ENCODED SECRET>
    - identity: {}
```
* `kubeapi server` manifest file requires this line:
```
--encryption-provider-config=/etc/kubernetes/enc/enc.yaml
```
* The manifest file can be edited at `/etc/kubernetes/manifests/kube-apiserver.yaml`
* You then add `--encryption-provider-config=/etc/kubernetes/enc/enc.yaml
` to the bottom of `- --tls-private-key-files=/etc/kubernetes/pki/apiserver.key`
* The `/etc/kubernetes/enc` directory is then mapped to the directory inside the pod.
* To see the status of the `kubeapi` server, use `crictl pods` command to see all pods.
* Creating a `secret` and assigning a key:
```
kubectl create secret generic my-secret-2 --from-literal=key2=topsecret
```
* After encryption is enabled on the kubeapi server, everything will be encrypted.