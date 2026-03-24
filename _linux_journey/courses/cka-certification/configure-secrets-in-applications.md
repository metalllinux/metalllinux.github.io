---
title: "Configure Secrets In Applications"
category: "cka-certification"
tags: ["cka-certification", "configure", "secrets", "applications"]
---

* Example Python application:
```
import os
from flash import Flask

app = Flash(__name__)

@app.route("/")
def main():

	mysql.connector.connect(host='mysql', database='mysql', user='root', password='passwrd')

	return render_template('hello.html', color=fetchacolor())

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="8080")
```
* Secrets store sensitive information such as passwords or keys.
* Example secret:
```
DB_Host: mysql
DB_User: root
DB_Password: passwrd
```
* Two steps are the the following for creating secrets:
	1. Create the Secret.
	2. Inject it into a pod.
* Imperative way of creating a secret:
```
kubectl create secret generic
```
* Declarative way of creating a secret:
```
kubectl create -f
```
* Imperative way allows you to specify the key-value pairs:
```
kubectl create secret generic <secret-name> --from-literal=<key>=<value>
```
```
kubectl create secret generic app-secret --from-literal=DB_Host=mysql
```
* To specify multiple key-value pairs, add the `--from-literal` option multiple times like so:
```
kubectl create secret generic \
app-secret --from-liberal=DB_Host=mysql
--from-literal=DB=User=root
--from-literal=DB_Password=passwrd
```
* However, if there are multiple secrets, the above method is difficult.
* Add multiple secrets using a file:
```
kubectl create secret generic <secret-name> --from-file=<path-to-file>
```
```
kubectl create secret generic \
    app-secret --from-file=app_secret.properties
```
* The declarative approach is:
* A secret is again created:
```
DB_Host: mysql
DB_User: root
DB_Password: passwrd
```
* The definition file looks like:
```
apiVersion:
kind: Secret
metadata:
  name: app-secret
data:
  DB_Host: mysql
  DB_User: root
  DB_Password: passwrd
```
```
kubectl create -f <definition_file.yaml>
```
* The above version is unsafe, due to the secret being in plain text.
* Must encode the data. This can be done on a Linux host using `echo -n 'mysql' | base64`
```
# Example output
bXlzcWw=
```
* From that, you can then place the encoded data instead of the plain text:
```
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
data:
  DB_Host: bXlzcWw=
  DB_User: VH6L
  DB_Password: Y0Y0Y0
```
* View secrets with the following:
```
kubectl get secrets
```
* Kubernetes also creates its own internal secret, which is shown during the `kubectl get secrets` command.
	* The secret looks like `default-token-<string> kubernetes.io/service-account-token`
* You can also `describe` secrets as well with `kubectl describe secrets`
	* This shows the attributes in the command, but not the secrets themselves.
	* To show the values as well, run the command `kubectl get secrets <secret> -o yaml` and that will output the `secrets` and their values.
* How do you decode, encoded values? Run:
```
echo -n '<encoded_value_here>' | base64 --decode
```
* To inject the secret into a pod, we firstly have the secret definition file:
```
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
data:
  DB_Host: bXlzcWw=
  DB_User: VH6L
  DB_Password: Y0Y0Y0
```
* The pod definition file then looks like this:
```
apiVersion: v1
kind: Pod
metadata:
  name: simple-websapp-color
  labels:
	name: simple-webapp-color
spec:
  containers:
  - name: simple-webapp-color
    image: simple-webapp-color
    ports:
	  - containerPort: 8080
	envFrom:
	  - secretRef:
		    name: app-secret
```
* The `envFrom` property is a list and it contains as many environment variables as required.
* In the above case, `app-secret` has to be in both definition files.
* Then creating the pod definition file with `kubectl create -f <pod_definition_name>` then creates the pod and it can then refer to the secret file.
* There are other ways to inject environment variables, these can be single variables like so into the pod definition file:
```
env:
  - name: DB_Password
 	valueFrom:
	  secretKeyRef:
		name: app-secret
		key: DB_Password
```
* The whole secret can be injected as a file via a `volume`:
```
volumes:
- name: app-secret-volume
  secret:
	secretName: app-secret
```
* Expanding more on `secrets` and volumes, inside the container, the secrets are created under `/opt/app-secret-volumes` (whichever name was specified in the `- name` section) as individual files:
```
ls /opt/app-secret-volumes
DB_Host DB_Password DB_User
```
* Each of the above files will show the contents of each password.
* Secrets are not encrypted, they are only encoded!
* When uploading to GitHub, don't push up any `secret` files, as those contain un-encrypted credentials essentially.
* The `secrets` are not encrypted in `etcd` either.
* Consider enabling encryption at rest.
* Good documentation on that: https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/
* Anyone able to deploy pods / deployments in the same namespace can access the same secrets!
	* Consider Role-based Access Control (RBAC) for least-privilege access.
* Consider a third-party `secrets` store providers
	* AWS Provider, Azure Provider, GCP Provider, Vault Provider
	* `secrets` are stored then not in `ETCD` and then via an external provider 