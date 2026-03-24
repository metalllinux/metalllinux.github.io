---
title: "How Get Latest Version Of Nginx Installed"
category: "networking"
tags: ["networking", "latest", "version", "nginx", "installed"]
---

sudo vim /etc/yum.repos.d/nginx.repo

Paste in the following:
```
[nginx-stable]
name=nginx stable repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true

[nginx-mainline]
name=nginx mainline repo
baseurl=http://nginx.org/packages/mainline/centos/$releasever/$basearch/
gpgcheck=1
enabled=0
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true
```

Install nginx:
```
sudo dnf install nginx -y
```

Check the version:
```
nginx -v
```

Enable it with systemd:
```
sudo systemctl enable nginx --now
```