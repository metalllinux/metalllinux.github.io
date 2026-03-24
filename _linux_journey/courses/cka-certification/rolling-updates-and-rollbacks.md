---
title: "Rolling Updates And Rollbacks"
category: "cka-certification"
tags: ["cka-certification", "rolling", "updates", "rollbacks"]
---

* When first creating a Deployment, it triggers a `Rollout`.
* A new `Rollout` creates a new `Deployment Revision`
* When the application is updated in the future i.e. to a newer version (Revision 2) `nginx 1.7.0` --> `nginx 1.7.1`
* Can see the `rollout status` with this command:
```
kubectl rollout status deployment/myapp-deployment
```
* To see the history and revisions of the deployment, run this command:
```
kubectl rollout history deployment/myapp-deployment
```
* Deployment Strategy
	* One way is to destroy all pods of X version and upgrade them with Y version.
	* The problem is there is a period where all applications are down, but the upgraded applications come back up. This is known as `Recreat`.
	* The second and better strategy is to take down each deployment and bring it back up with the new version one by one. This is known as `Rolling Update`
* Regarding `kubectl apply` to update the image from `image: nginx` to `image: nginx:1.7.1`:
```
apiVersion:
kind:
metadata:
spec:
deployment-definition.yml
name: myapp-deployment
labels:
app: myapp
type: front-end
apps/v1
metadata:
name: myapp-pod
labels:
app: myapp
type: front-end
spec:
containers:
- name: nginx-container
image: nginx:1.7.1
replicas:
selector:
matchLabels:
type: front-end
```
* Just run `kubectl apply -f deployment-definition.yml` and this will create a new rollout with the changes. A new revision of the deployment is created.
* To update the image of your application, use the `kubectl set image deployment/myapp-deployment nginx container=nginx:1.9.1`
	* Doing it this way means the deployment definition file will have a different configuration.
* Run `kubectl describe deployment` to see deployment details.
	* Can see the `Recreate` and `Rolling` in action.
* When first deployed, the `Replica Set` will be deployed.
	* When the Rollout begins, under the hood a `Replica Set-2` is created. Then in `Replica Set - 1`, the pods are slowly removed and then upgraded versions are added to `Replica Set - 2`.
	* This can be seen in action by running the `kubectl get replicasets` command.
* How do you `Rollback` and update?
	* To rollback to a previous version of the app in all instances, can run `kubectl rollout undo deployment/myapp-deploym`
	* Then pods will be destroyed in the new `Replica Set` and the older pods will be brought back up in the previuous `Replica Set`.
* Can compare `Rollback` with `kubectl get replicasets`.
* To see the history of the `Rollout` commands, run:
```
kubectl rollout status deployment/myapp-deployment
kubectl rollout history deployment/myapp-deployment
```