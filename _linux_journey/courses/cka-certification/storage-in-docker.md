---
title: "Storage In Docker"
category: "cka-certification"
tags: ["cka-certification", "storage", "docker"]
---

* How does Docker store data?
	* In particular on the local filesystem.
* Docker creates a directory structure at `/var/lib/docker/`
	* In that directory structure, there are also `aufs` containers, image `volumes`, `images` and more.
	* This is where Docker stores all of its data by default.
* All files related to `containers` are stored under the `/var/lib/docker/containers` directory.
* Any `volumes` are created under the `/var/lib/docker/volumes` directory.
* How does it store the above files? Need to know the `Layered architecture`
* The `architecture` is done via a `Dockerfile`. It has a concept of layers:
```
FROM Ubuntu
RUN apt-get update && apt-get -y install python
RUN pip install flask flask-mysql
COPY . /opt/source-code
ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
```
* Then build the image with:
```
docker build Dockerfile -t <repository>/<image_name>
```
* The first layer is installing a basic Ubuntu OS `FROM Ubuntu`
* The second `RUN apt-get` layer makes changes at the package level.
* The third layer `RUN pip` makes changes at the pip package level.
* The fourth layer is copying over the source code to the `/opt/source-code` directory.
* The fifth layer is updating the `ENTRYPOINT`.
* Each layer only stores the changes from the previous layer, the size of each code change is reflected (for example installing the base Ubuntu OS is 120 MB, then moving to changing the apt packages is 306MB and so on)
* Consider a second application:
```
FROM Ubuntu
RUN apt-get update && apt-get -y install python
RUN pip install flask flask-mysql
COPY app2.py /opt/source-code
ENTRYPOINT FLASK_APP=/opt/source-code/app2.py flask run
```
* Then building the image with the following:
```
docker build Dockerfile2 -t <repository>/<image_name>2
```
* This second application uses different source code in order to build it.
* Since the first 3 layers are the same as in the first `Dockerfile`, `docker` does not build the first 3 layers.
* Then creates the last two layers, with the new entrypoint.
	* Layer 4: Source code
	* Layer 5: Update Entrypoint
* It builds images faster and saves disk space.
	* Layers 1~3 would then be at 0MB.
	* Layer 4 is the same size as from first application.
	* Layer 5 has the Entrypoint updated.
* When the application code is updated, `app.py` as mentioned above, `docker` reuses all of the previous layers from cache and rebuilds the application image by updating the source code.
	* Saves time during rebuilds and updates.
* All Layers are known as `Docker Image Layers`.
* Layers are read-only.
	* Can only modify them by initiating a new build.
* Build the image with:
```
docker build Dockerfile -t <repository>/<image_name>
```
* Run the image with:
```
docker run <repository>/<image_name>
```
* Then a new Layer (Layer 6 in the above example) is created. This is a writable layer:
```
Layer 6: Container Layer
```
* This layer stores logs and any file modified by the user on that container.
* When the container is destroyed, Layer 6 and all of its changes are also destroyed.
* Same image layer is shared by all containers using this image.
* Can modify files that are part of the read-only (Layers 1~5 in the previous example).
	* What happens is that Docker copies these files to Layer 6, so they can be edited. It is a different version of the file and thus only in the Container Layer (Layer 6) can it be modified.
* The above two points are part of the Copy-On-Write mechanism.
* To make data persistent, then using `volumes` is best.
	* Create a volume using the `docker volume create` command.
	* For example, creating a `data_volume`, makes the volume under `/var/lib/docker/volumes/data_volume`
	* The `volume` sits on top of the read-only Image layer of the container.
	* To specify the newly created volume, run the following:
```
docker run -v data_volume:/var/lib/mysql mysql
```
* In the above example, the image name is `mysql` and stores the data under `/var/lib/mysql`
	* This creates a new container and mounts the `data_volume` into it.
* Even if the container is destroyed, the data is still active.
* Can also make more volumes by using this command:
```
docker run -v data_volume:/var/lib/mysql mysql
```
* In addition:
```
docker run -v data_volume2:/var/lib/mysql mysql
```
* To mount a volume that is not under `/var/lib/docker`, run this command:
```
docker run -v /data/mysql:/var/lib/mysql mysql
```
* The above is called `Bind Mounting`.
* Ultimately two types of mounts:
	* `Volume Mounting`
	* `Bind Mounting`
* Volume Mounting mounts a volume from the `volumes` directory.
* Bind Mounts mounts a directory from anywhere on the `docker` host.
* Using `docker run -v` is the old style.
* This way is better:
```
docker run --mount type=bind,source=/data/mysql,target=/var/lib/mysql mysql
```
* The `source` is the host and the `target` is the container.
* Docker uses `Storage Drivers` to enable the layered architecture.
	* Common storage drivers are `AUFS`, `VTRFS` and `ZFS`.
	* Others also include `BTRFS`, `Device Mapper`, `Overlay` and `Overlay2`
	* Ubuntu's default `AUFS`
		* This storage driver is not available on Fedora, CentOS.
			* Device Mapper would be better in that case.
* `Docker` chooses the best storage driver automatically based on the OS.
* Different storage drivers provide different performance and stability.
* 