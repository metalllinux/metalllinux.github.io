---
title: "Docker Exec Inside Container"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "docker", "exec", "inside", "container"]
---

* The below command runs `ls` inside a docker container:

docker exec -i 90817ddf8115 ls

* How to get rid of individual files inside a docker container:
* docker exec -i 90817ddf8115 rm -Rf /output/remove-me