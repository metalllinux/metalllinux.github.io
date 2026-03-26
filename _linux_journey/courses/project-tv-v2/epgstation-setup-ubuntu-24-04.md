---
title: "For Ubuntu 24.04"
category: "project-tv-v2"
tags: ["project-tv-v2", "epgstation", "setup", "ubuntu"]
---

* Zip file attached:
[2024epg-plex.zip](../../_resources/2024epg-plex.zip)
## For Ubuntu 24.04
* Originally from https://www.digital-den.jp/simplelife/archives/8014/
* Install the `unzip` utility:
```
sudo apt install -y unzip
```
* Pull the required scripts and data:
```
wget https://www.digital-den.jp/simplelife/wp-content/uploads/2024/12/2024epg-plex.zip
```
* Extract the tarball:
```
unzip 2024epg-plex.zip
```
* Install `dkms` and `git` packages:
```
sudo apt install -y dkms git
```
* Copy the `data` directory into the `home` directory:
```
cp -r ~/2024epg-plex/data ~/git/epg-plex-data
```
* Install the card reader tools:
```
sudo apt install -y libpcsclite-dev pcscd pcsc-tools libccid
```
* Scan for any available card readers:
```
sudo pcsc_scan
```
* Stop the pcscd socket:
```
sudo systemctl disable --now pcscd.socket
```
* Check the status:
```
sudo systemctl status pcscd.socket
```
* Install the `gdebi` application:
```
sudo apt install -y gdebi
```
* Pull the latest `.deb` package for the Plex TV Card Unofficial Driver:
```
wget https://github.com/tsukumijima/px4_drv/releases/download/v0.5.2/px4-drv-dkms_0.5.2_all.deb
```
* Install the Plex driver:
```
sudo gdebi -n px4-drv-dkms_0.5.2_all.deb
```
* Reboot your machine:
```
sudo reboot
```
* Check that the Plex Tuner is recognised:
```
ls -l /dev/px*
```
* For those with a Plex W Series card such as `PX-W3PE5`, follow these steps:
* Change into the `git` directory:
```
cd ~/git
```
* Follow the rest of the steps:
```
cd ~/git
git clone https://github.com/l3tnun/docker-mirakurun-epgstation.git
cd docker-mirakurun-epgstation
cp docker-compose-sample.yml docker-compose.yml
cp epgstation/config/config.yml.template epgstation/config/config.yml
cp epgstation/config/enc.js.template epgstation/config/enc.js
cp epgstation/config/operatorLogConfig.sample.yml epgstation/config/operatorLogConfig.yml
cp epgstation/config/epgUpdaterLogConfig.sample.yml epgstation/config/epgUpdaterLogConfig.yml
cp epgstation/config/serviceLogConfig.sample.yml epgstation/config/serviceLogConfig.yml
git clone https://github.com/Chinachu/Mirakurun
cd ~/git/epg-plex-data
cp ./new-MirakurunDockerfile ~/git/docker-mirakurun-epgstation/Mirakurun/docker/Dockerfile
cp ./tuners-w.yml ~/git/docker-mirakurun-epgstation/Mirakurun/config/tuners.yml
cp ./channels.yml ~/git/docker-mirakurun-epgstation/Mirakurun/config/channels.yml
cp ./new-docker-compose-w.yml ~/git/docker-mirakurun-epgstation/docker-compose.yml
cd ~/git/docker-mirakurun-epgstation
```
* Apply this `docker compose` file:
```
cat << "EOF" | tee ./docker-compose.yml
services:
    mirakurun:
        container_name: mirakurun
        build:
          context: Mirakurun
          dockerfile: docker/Dockerfile
        image: chinachu/mirakurun
        cap_add:
            - SYS_ADMIN
            - SYS_NICE
        ports:
            - "40772:40772"
            - "9229:9229"
        volumes:
            - /etc/localtime:/etc/localtime:ro
            - ./Mirakurun/config/:/app-config/
            - ./Mirakurun/data/:/app-data/
        environment:
            TZ: "Asia/Tokyo"
        devices:
            - /dev/px4video0:/dev/px4video0
            - /dev/px4video1:/dev/px4video1
            - /dev/px4video2:/dev/px4video2
            - /dev/px4video3:/dev/px4video3
            - /dev/bus:/dev/bus
        restart: always
        logging:
            driver: json-file
            options:
                max-file: "1"
                max-size: 10m

    mysql:
        container_name: mysql-epgstation-v2
        image: mariadb:10.5
        volumes:
            - mysql-db:/var/lib/mysql
        environment:
            MYSQL_USER: epgstation
            MYSQL_PASSWORD: epgstation
            MYSQL_ROOT_PASSWORD: epgstation
            MYSQL_DATABASE: epgstation
            TZ: "Asia/Tokyo"
        command: --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --performance-schema=false --expire_logs_days=1 # for mariadb
        restart: always
        logging:
            options:
                max-size: "10m"
                max-file: "3"

    epgstation:
        container_name: epgstation-v2
        build:
            context: "./epgstation"
            dockerfile: "debian.Dockerfile"
        volumes:
            - /etc/localtime:/etc/localtime:ro
            - ./epgstation/config:/app/config
            - ./epgstation/data:/app/data
            - ./epgstation/thumbnail:/app/thumbnail
            - ./epgstation/logs:/app/logs
            - /mnt/mediapool/tv:/app/recorded
        environment:
            TZ: "Asia/Tokyo"
        depends_on:
            - mirakurun
            - mysql
        ports:
            - "8888:8888"
            - "8889:8889"
        #user: "1000:1000"
        restart: always

volumes:
    mysql-db:
        driver: local
EOF
```
* Bring up the containers:
```
docker compose pull
docker compose build --no-cache
docker compose up -d
```