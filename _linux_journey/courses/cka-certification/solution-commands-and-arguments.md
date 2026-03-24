---
title: "Solution Commands And Arguments"
category: "cka-certification"
tags: ["cka-certification", "solution", "commands", "arguments"]
---

* Good example use of a command in a pod definition file:
```
apiVersion: v1
kind: Pod 
metadata:
  name: ubuntu-sleeper-2
spec:
  containers:
  - name: ubuntu
    image: ubuntu
    command: 
      - "sleep"
      - "5000"
```
* Another good example:
```
apiVersion: v1 
kind: Pod 
metadata:
  name: webapp-green
  labels:
      name: webapp-green 
spec:
  containers:
  - name: simple-webapp
    image: kodekloud/webapp-color
    command: ["python", "app.py"]
    args: ["--color", "pink"]
```
* How to check the commands that a pod runs?
	* Run `kubectl describe pod <pod_name>` and then under the `Containers` tab you'll see the `Command` section and that is where all of the commands a container runs will be.
* How to create a pod with an Ubuntu image and with the `sleep` command.
* To do this, create this definition file:
```
apiVersion: v1
kind: Pod 
metadata:
  name: ubuntu-sleeper-2
spec:
  containers:
  - name: ubuntu
    image: ubuntu
    command: 
      - "sleep"
      - "5000"
```
* Can also do it in an array like so:
```
apiVersion: v1
kind: Pod 
metadata:
  name: ubuntu-sleeper-2
spec:
  containers:
  - name: ubuntu
    image: ubuntu
    command: [ "sleep 5000" ]
```
* Always need the command as the first item.
* Can also specify it as `args`:
```
apiVersion: v1
kind: Pod 
metadata:
  name: ubuntu-sleeper-2
spec:
  containers:
  - name: ubuntu
    image: ubuntu
    command: [ "sleep" ]
	args: [ "5000" ]
```
* Then `kubectl create -f` to create the file.
* All elements in the `command` string have to be a string and not a number (i.e. everything needs to be within double quotations).
* `kubectl apply` can only be applied to some pods you can change and some pods you can't.
* To get past these restrictions, use `kubectl replace --force -f <definition_file>`
	* This command deletes the pod and recreates it based on the edited one.
* Best practice however to delete the pod, update the local file and then re-deploying the pod again.
* Commands in a Docker image which run at startup? That would be `ENTRYPOINT`.
	* Anything that comes in `CMD` after that is an argument to the `ENTRYPOINT` commands.
* The `command` field in a definition file always overrides the `ENTRYPOINT` of a Docker image. For example `command: ["--color", "pink"]` in a definition file would take precedence over a Docker `ENTRYPOINT` field.
* Can run the following:
```
kubectl run webapp-green --image=kodekloud/webapp-color --dry-run=client -o yaml
```
* `kubectl run nginx --image=nginx -- <arg1> <arg2>`
* The `--` separates the `kubectl` utility and the arguments that are passed through to the `nginx` application inside.
* Can also override commands as well:
`kubectl run nginx --image=nginx --command -- <cmd ><arg1> <arg2>`
* `kubectl run webapp-green --image=kodekloud/webapp-color -- --color green`