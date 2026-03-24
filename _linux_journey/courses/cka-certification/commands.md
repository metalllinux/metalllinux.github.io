---
title: "Commands"
category: "cka-certification"
tags: ["cka-certification", "commands"]
---

* Application commands in a pod definition file.
* `Docker` commands, for example running `docker run ubuntu` will run an Ubuntu image and then exit immediately.
* `docker ps -a` will show all containers **including** those which have stopped.
* Containers are meant to run a specific tasks or process.
* When the task is complete, the container exits. Similarly if the container is stopped.
* Within a container image, if you see the word `CMD`, that is the program that will start within the container.
	* For example `CMD ["bash"]`
	* If it cannot find a terminal, it exits.
		* Therefore the container itself exits.
* To change this, you can append a command to the Docker override command.
	* An example is the `docker run ubuntu sleep 5` (`sleep 5` being the added option).
		* When the container starts, it runs the `sleep` command for 5 seconds and then exits.
			* To make this permanent, edit the `docker` image and add `CMD sleep 5`
* The `CMD` can be placed in a `shell` form or a `json` array form as well.
	* For JSON, it should look like `CMD ["sleep","5"]`
* The image looks like this:
```
FROM Ubuntu
CMD sleep 5
```
* Then we build the image with `docker build -t <image-name> .` and run it with `docker run <image-name>`
* You can also change the image, by appending the new command to it, in this case `docker run <image-name> sleep 10`
	* Ideally we want to pass in the seconds only and invoke the `sleep` command automatically like so:
```
docker run <image-name> 10
```
* Therefore to do the above, you need the `ENTRYPOINT` instruction, that being `ENTRYPOINT ["sleep"]`. The image would then look like:
```
FROM Ubuntu
ENTRYPOINT ["sleep"]
```
* How do you configure a value automatically if one is not added in the command by the user. This can be done using:
```
FROM Ubuntu
ENTRYPOINT ["sleep"]
CMD ["5"]
```
* Therefore, the above command will be `sleep 5`, if a operand is not set by the user.
* You can also override the command using the `--entrypoint` option in `docker` like so:
```
docker run --entrypoint sleep2.0 <image-name> <value>
```