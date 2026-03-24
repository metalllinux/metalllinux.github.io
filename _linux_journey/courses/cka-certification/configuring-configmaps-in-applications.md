---
title: "Configuring Configmaps In Applications"
category: "cka-certification"
tags: ["cka-certification", "configuring", "configmaps", "applications"]
---

* In previous lectures, we saw how to define environment variables in pod definition files.
* ConfigMaps take that information out of the pod definition file and manage it centrally.
* ConfigMaps take configuration data in the form of key:value pairs. An example is below:
```
APP_COLOR: blue
APP_MODE: prod
```
* You then add the ConfigMap into the pod definition file to how the variables there.
* Example pod definition file:
```
apiVersion: v1
kind: `pd
metadata:
  name: simple-webapp-color
spec:
  containers:
  - name: simple-webapp-container
    image: simple-webapp-container
	ports:
	  - containerPort: <name>

	envFrom:
	- configMapRef:
		  name: app-contents
```
* Phases for creating ConfigMaps:
	* Create the ConfigMap.
	* Inject it into the pod.
* To create a ConfigMap in the imperative way, run the below command:
```
kubectl create configmap
```
* Or the declerative way by using a ConfigMap definition file:
```
kubectl create -f
```
* Imperative way option 1):
```
kubectl create configmap <config-name> --from-literal=<key>=<value>
```
* Imperative way option 2):
```
kubectl create configmap \
    app-config --from-literal=APP_COLOR=blue
```
* The option `--from-literal` - used to specify the key:value pairs within the command itself.
* If you wish to add multiple key:value pairs, add the `--from-literal` option multiple times:
```
kubectl create configmap \
    app-config --from-literal=APP_COLOR=blue --from-literal=APP_MODE=prod
```
* Imperative way option 3): through a file:
```
kubectl create configmap
   <config-name> --from-file=<path-to-file>
```
```
kubectl create configmap \
    app-config --from-file=app_config.properties
```
* The declerative approach looks like this:
```
kubectl create -f 
```
* Example ConfigMap yaml file:
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_COLOR: blue
  APP_MODE: prod
```
* `kubectl create -f ConfigMap`
* Map sure to rename multiple different ConfigMaps correctly for different applications. Example ConfigMaps are below:
app-config
```
APP_COLOR: blue
APP_MODE: prod
```
mysql-config
```
port: 3306
max_allowed_packet: 128M
```
redis-config
```
port: 6379
rdb-compression: yes
```
* To view ConfigMaps, run:
```
kubectl get configmaps
```
* Describe a ConfigMap with:
```
kubectl describe configmaps
```
* Configuration data is listed under the DATA section.
* Example pod definition file:
```
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp-color
spec:
  containers:
  - name: simple-webapp-color
    image: simple-webapp-color
	ports:
	  - containerPort: 8080

	envFrom:
	- configMapRef:
		  name: app-contents
```
* The ConfigMap we are pairing this with is:
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_COLOR: blue
  APP_MODE: prod
```
* Creating the above pod from the pod definition file creates an application with a blue background.
* There are other ways to inject environment variables into pods:
```
envFrom:
  - configMapRef:
	    name: app-config
```
* For single environment variables:
```
env:
   - name: APP_COLOR
	 valueFrom:
		configMapKeyRef:
		  name: app-config
		  key: APP_COLOR
```
* Also as files in a volume:
```
volumes:
- name: app-config-volume
  configMap:
	 name: app-config
```