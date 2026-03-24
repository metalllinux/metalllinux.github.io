---
title: "Service Accounts"
category: "cka-certification"
tags: ["cka-certification", "service", "accounts"]
---

* Two types of accounts in Kubernetes:
	* User Account - used by humans. Examples are `Admin` / `Developer`
	* Service Account - used by machines. Examples are `Prometheus` (polls Kubernetes API for performance metrics), `Jenkins` (automated build tool, deploys applications on the Kubernetes cluster)
* Good use of Python - create a Kubernetes dashboard of all the pods in a cluster and display it on a webpage. It polls the `kube-api` server.
	* The application has to be authenticated using a `service` account.
	* To create a `service` account, run `kubectl create serviceaccount <name>`
	* View the service accounts with this command: `kubectl get serviceaccount`
	* Check a service account with `kubectl describe serviceaccount <name>`
	* When a service account is created, a token is assigned to it automatically.
	* The account token has to be used by the external authentication, whilst connecting to the `kube-api` server.
	* The `token` is stored as a `secret` object.
	* When a `service` account is created, it starts with an object and then creates a token for the service account.
	* The `secret` object is created and the token is stored inside.
	* The `secret` is then linked to the service account.
	* In order to view the token, run `kubectl describe secret <secret_name>`
	* The token can then be used as an authentication bearer token, whilst making a call to the REST API.
* An example is using `curl`, provide the bearer token as an authorisation header, while making a REST call to the `kube-api` server.
```
curl https://192.168.1.1:6443/api --insecure 00header "Authorization: Bearer <TOKEN_HERE>"
```
* That is how you authenticate the dashboard application.
* What if the third party application is deployed on the Kubernetes cluster itself?
* It is better to host the token as a volume in the pod itself.
	* The token is then placed inside the pod and can be read by the application.
* Under `serviceaccounts`, there is a `default` account that exists already.
	* This is automatically created.
* Each namespace has its own default `serviceaccount`
* The `serviceaccount` and token are automatically mounted as a volume to the pod.
* For example:
```
apiVersion: v1
kind: Pod
metadata:
  name: my-kubernetes-dashboard
spec:
  containers:
	- name: my-kubernetes-dashboard
	  image: my-kubernetes-dashboard 
```
* When checking with the `kubectl describe pod <pod>` command, a secret is created within the volume.
* The secret contains the token.
* It is mounted at the following location:
```
/var/run/secrets/kubernetes.io/serviceaccount
```
* Inside the pod, if you run the `ls` command, you find the secret as three separate files:
```
kubectl exec -it my-kubernetes-dashboard -- ls /var/run/secrets/kubernetes.io/serviceaccount
```
* The output is:
```
ca.crt namespace token
```
* If you view the contents of the `token` file, you see the token that is needed to access the Kubernetes API:
```
kubectl exec -it my-kubernetes-dashboard cat /var/run/secrets/kubernetes.io/serviceaccount/token
```
* The default Service Account is very restricted - only has permissions to run basic kube-api queries.
* To use a different service account, change the pod definition file:
```
apiVersion: v1
kind: Pod
metadata:
  name: my-kubernetes-dashboard
spec:
  containers:
	- name: my-kubernetes-dashboard
	  image: my-kubernetes-dashboard
  serviceAccountName: dashboard-sa
```
* Cannot edit the service account of an existing pod.
* Must delete and recreate the pod.
* In the case of a `deployment`, the above is not necessary - any changes made to the definition file, automatically make changes on the `deployment` side.
* Checking the pod details shows the new service account is being used.
* Can set a service account to not be mounted automatically, by setting the `automountServiceToken` field to `false`:
```
apiVersion: v1
kind: Pod
metadata:
  name: my-kubernetes-dashboard
spec:
  containers:
	- name: my-kubernetes-dashboard
	  image: my-kubernetes-dashboard
  automountServiceToken: false
```
* Each namespace has a service account and that service account has a token associated with it.
* When a pod is created, it associates the service account with the pod. Mounts it as a known location in the pod.
* Allows the process to query the kube-api server.
* You can decode the token with this command:
```
jq -R 'split(".") | select(length > 0) | .[0],.[1] | @base64 | fromjson' <<< <token_here>
```
* The token has no expiry date.
* Current implementation of JWT is not time bound.
* The JWT is valid, as long as the service account exists.
* Each JWT requires a separate service account.
* A separate secret object is also required, which results in scalability issues.
* TokenRequestAPI introduced in Kubernetes v1.22 has the following:
	* Audience Bound
	* Time Bound
	* Object Bound
* Nowadays the token is mounted as projected volume like so :
```
projected:
  defaultMode: 420
  sources:
  - serviceAccountToken:
       expirationSeconds: 3607
       path: token
```
* With the spec in Kubernetes 1.24, the default expiry date of a token is 1 hour.
* https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/