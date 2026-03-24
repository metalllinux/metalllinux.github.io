---
title: "Solution Rolling Updates And Rollbacks"
category: "cka-certification"
tags: ["cka-certification", "solution", "rolling", "updates", "rollbacks"]
---

* Can set an `alias` for `kubectl`. A good character is `k`.
* Find the container image by running `kubectl describe deploy <deployment>`
	* Can also see the `StrategyType`.
* The `Rolling` update takes down one pod and a time and brings them back up.
* One way to update an image is `kubectl edit deployment <deployment_name>`
	* Another way to update is to use the `kubectl set image` command. Example `kubectl set image deploy <deployment_name> <container_name>=<new_image_name>`
	* Then running the `kubectl describe deploy <deployment>` command again shows the updated image.
* Check the `RollingUpdatesStrategy` to check the amount of pods that can be down at the same time. You check the amount of `Replicas` and then divide by the `RollingUpdatesStrategy` percentage --> the answer is `1`.
* How to change a `Deployment` strategy? Run `kubectl edit deploy <deployment_type>`, then under `spec` --> `strategy` --> `type`, change that to `Recreate`. `Recreate` does not need the `RollingUpdate` parameters, so everything between `strategy:` and `type:Recreate` can be removed.
* How to upgrade an application to `V3`?
	* We do `kubectl set image deploy frontend <deployment_name>=kodekloud/webapp-color:v3`
* 