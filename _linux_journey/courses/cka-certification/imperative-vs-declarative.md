---
title: "Imperative Vs Declarative"
category: "cka-certification"
tags: ["cka-certification", "imperative", "declarative"]
---

* Two ways of managing infrastructure as code: Imperative and Declarative.
	* Imperative Approach - what to do and how.
	* Declarative Approach - not giving step-by-step instructions and am instead specifying the final destination. The system figures out how to reach the final destination.
* Imperative instructions look like this:
```
1. Provision VM.
2. Install Nginx.
3. Edit configuration file to use port 8070.
4. Use web path /var/www/nginx
5. Load web pages to /var/www/nginx
6. Start Nginx
```
* Declarative instructions are these:
```
VM Name: web-server
Package: Nginx
Port: 8080
Path: /var/www/nginx
Code: GIT Repo - X
```
* Ansible, Puppet, Chef and Terraform fall into the Declarative category.
* In Kubernetes, Imperative instructions look like the following (no need to create yaml object files and are useful during the certification exams):
```
# Create New Objects
kubectl run --image=nginx nginx
kubectl create deployment --image=nginx nginx
kubectl expose deployment nginx --port 80
# Update New Objects
kubectl edit deployment nginx
kubectl scale deployment nginx --replicas=5
kubectl set image deployment nginx nginx=nginx:1.18
kubectl create -f <object_file.yml>
kubectl replace -f <object_file.yml>
kubectl delete -f <object_file.yml>
```
* The Delcarative approach in Kubernetes is to define files for the services, pods and other objects. Then with a single `kubectl apply -f <object_file.yml>` command, we can then bring up the infrastructure.
* The `apply` command looks at the current infrastructure and sees what changes need to be made to the system.
* The above Imperative approach is difficult in complex use-cases, such as creating a multi-container pod.
	* The commands were ran only in the user’s session and it is hard for another user to follow the commands.
		* This is where the object configuration (also known as “manifest” files can help.
* Example Imperative Configuration File to Create an Object:
```
apiVersion: v1
kind: Pod

metadata:
  name: myapp-pod
  labels:
     app: myapp
     type: front-end
spec:
  containers:
  - name: nginx-container
    image: nginx
```
* Apply the Object: `kubectl create -f nginx.yaml`
* Update the Object:
	* One way is to use the `kubectl edit deployment nginx` command.
		* This then opens a yaml definition file (not the local file you made, but one stored in the Kubernetes memory). This definition file will look like the one below, except with additional fields such as `status`:
```
apiVersion: v1
kind: Pod

metadata:
  name: myapp-pod
  labels:
     app: myapp
     type: front-end
spec:
  containers:
  - name: nginx-container
    image: nginx
status:
  conditions:
  - lastProbeTime: null
    status: "True"
    type: Initialized
```
* The `status` information above stores the status of the pod.
* Making changes to the above file and then saving and quitting will be applied to the live object.
	* For example, changing the `image: nginx` version of `nginx` to `nginx:1.18`.
		* This of course does not change the original file.
* A better approach is instead of changing the file that is in the Kubernetes Memory, change the original local object file and then run `kubectl replace -f nginx.yaml`. For example setting `image: nginx:1.18` to update the image instead in the file.
* May want to completely delete and recreate objects. This can be done with the `force` option: `kubectl replace --force -f nginx.yaml`
* Cannot use the `create` command for updating objects, as Kubernetes will complain that it already exists.
* Taxing for Administrators - have to be aware of all configurations.
* For the Declarative approach, the `kubectl apply -f nginx.yaml` command is used. It is intelligent enough to create options if the object does not already exist.
	* Can create multiple objects at once by specifying a directory, for example `kubectl apply -f /path/to/config-files`.
* Then for updating the objects, the `kubectl apply -f nginx.yaml` command is ran, after the `nginx.yaml` file (in this case) is updated.
	* We'd only need to update the configuration files in the `/path/to/config-files` directory and the `kubectl apply` command does the rest.
* From the CKA exam perspective, can use the Imperative approach to save time.
* To edit the properties of an existing object, then using the `kubectl edit` command is the quickest way.