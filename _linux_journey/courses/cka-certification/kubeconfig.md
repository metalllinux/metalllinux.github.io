---
title: "Kubeconfig"
category: "cka-certification"
tags: ["cka-certification", "kubeconfig"]
---

* Check with the kubernetes API using `curl`:
```
curl https://my-kube-playground:6443/api/v1/pods --key admin.key --cert admin.crt --cacert ca.crt
```
* The response you receive would be the following:
```
{
    "kind": "PodList",
	"apiVersion":  "v1",
	"metadata": {
       "selfLink": "/api/v1/pods",
    },
    "items": []
}
```
* The above is then validated by the `kube-apiserver` to authenticate the user.
* How do you do that using the `kubectl` command?
* To do the same as the above with the `kubectl` command:
```
kubectl get pods --server my-kube-playground:6443 --client-key admin.key --client-certificate admin.crt --certificate-authority ca.crt
```
* Performing the above every time is tedious. It is better to move it all to a configuration file called `KubeConfig`.
* `KubeConfig File`:
```
--server my-kube-playground:6443
--client-key admin.key
--client-certificate admin.crt
--certificate-authority ca.crt
```
* Then specify the file using the `--kubeconfig` option like so:
```
kubectl get pods
  --kubeconfig config
```
* By default, the `kubectl` command looks for the file `config` under `$HOME/.kube/config`
* If you create the `KubeConfig` file under `$HOME/.kube`, you only need to run this part of the command:
```
kubectl get pods
```
* The `KubeConfig` file is in a special format. It has three sections:
	* `Clusters` - various Kubernetes clusters you need access to. Can have different environment such as `Development`, `Production` or Cloud Providers such as `GCP`.
	* `Contexts` - marries `Clusters` and `Users` together. They define which user account can access which cluster. `Admin@Production` being a good example of merging `Production` and `Admin`
		* With this, not configuring any users or authorising any access within the cluster. Using existing users with existing privileges.
	* `Users` - user accounts for which you have access to the above `Clusters`. Examples are `Admin`, `Dev User` and `Prod User`. The users can have different privileges on different clusters.
* How does this command fit in?
```
--server my-kube-playground:6443
--client-key admin.key
--client-certificate admin.crt
--certificate-authority ca.crt
```
* Clusters:
```
--server my-kube-playground:6443
--certificate-authority ca.crt
```
* Users:
```
--client-key admin.key
--client-certificate admin.crt
```
* Then create a `Context` to allow the `MyKubeAdmin` to access the `my-kube-playground` cluster.
* A real `KubeConfig` file:
```
apiVersion: v1
kind: Config

clusters:

- name: my-kube-playground
  cluster:
    certificate-authority: ca.crt
    server: https://my-kube-playground:6443

contexts:

- name: my-kube-admin@my-kube-playground
  context:
    cluster:
    user:

users:

- name: my-kube-admin
  user:
    client-certificate: admin.crt
    client-key: admin.key
```
* The above sections `clusters`, `contexts` and `users` is in an array format.
	* Can then specify multiple `clusters`, `users` etc in the same file with the help of arrays.
* Another good real `KubeConfig` example:
```
apiVersion: v1
kind: Config

clusters:
- name: my-kube-playground
  cluster:
    certificate-authority: ca.crt
    server: https://my-kube-playground:6443
- name: development
- name: production
- name: google

contexts:
- name: dev-user@google
- name: prod-user@pr
- name: my-kube-admin@my-kube-playground
  context:
    cluster:
    user:

users:

- name: my-kube-admin
  user:
    client-certificate: admin.crt
    client-key: admin.key
- name: admin
- name: dev-user
- name: prod-user
```
* When the file is ready, no need to run `kubectl create -f` or similar, just leave it and it will automatically be read by the `kube api-server`.
* How does `kubectl` know which context to choose from?
	* Can add the following option:
```
current-context: dev-user@google
```
* What this looks like when added to the file:
```
apiVersion: v1
kind: Config

current-context: dev-user@google

clusters:
- name: my-kube-playground
  cluster:
    certificate-authority: ca.crt
    server: https://my-kube-playground:6443
- name: development
- name: production
- name: google

contexts:
- name: dev-user@google
- name: prod-user@pr
- name: my-kube-admin@my-kube-playground
  context:
    cluster:
    user:

users:

- name: my-kube-admin
  user:
    client-certificate: admin.crt
    client-key: admin.key
- name: admin
- name: dev-user
- name: prod-user
```
* To view the current file being used:
```
kubectl config view
```
* Displays the above KubeConfig output.
* If you don't specify the KubeConfig file, the default under `$HOME/.kube/config` is used.
* Then to view a specific KubeConfig file, do:
```
kubectl config view --kubeconfig=my-custom-config
```
* How do you change the `Context`?
* To change the `current-context` field, run `kubectl config use-context prod-user@production` and that will change the `Context` in the file.
* You can make other changes, other options that can be listed are:
```
kubectl config -h
```
* How about Namespaces?
* Can you configure a `Context` to switch to a particular `Namespace`?
* Add the `namespace` option like so:
```
apiVersion: v1
kind: Config

clusters:
- name: production
  cluster:
    certificate-authority: ca.crt
    server: https://172.17.0.51:6443

contexts:
- name: admin@production
  context:
    cluster: production
    user: admin
    namespace: finance

users:
- name: admin
  user:
     client-certificate: admin.crt
     client-key: admin.key
```
* Then when you swittch to `admin@production`, you will be automatically added to the `finance` namespace.
* For certificates in the KubeConfig file, it is better to list the full path:
```
apiVersion: v1
kind: Config

clusters:
- name: production
  cluster:
    certificate-authority: /etc/kubernetes/pki/ca.crt
    server: https://172.17.0.51:6443

contexts:
- name: admin@production
  context:
    cluster: production
    user: admin
    namespace: finance

users:
- name: admin
  user:
     client-certificate: /etc/kubernetes/pki/users/admin.crt
     client-key: /etc/kubernetes/pki/users/admin.key
```
* There is another way to specify the certificate credentials.
* Instead of the `certificate-authority:` field under `clusters` and a path to the file, can just add the `certificate-authrority-data:` instead and provide the contents of the certificate itself:
```
apiVersion: v1
kind: Config

clusters:
- name: production
  cluster:
    certificate-authority-data: <CERTIFICATE_IN_BASE64_FORMAT_EXAMPLE: ca.crt | base64>
    server: https://172.17.0.51:6443

contexts:
- name: admin@production
  context:
    cluster: production
    user: admin
    namespace: finance

users:
- name: admin
  user:
     client-certificate: /etc/kubernetes/pki/users/admin.crt
     client-key: /etc/kubernetes/pki/users/admin.key
```
* Decode the certificate again using this option:
```
echo "LS0...bnJ(base64 encoded certificate)" | base64 --decode
```