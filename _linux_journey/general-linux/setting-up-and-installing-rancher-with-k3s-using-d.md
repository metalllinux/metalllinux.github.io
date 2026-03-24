---
title: "Setting Up And Installing Rancher With K3S Using D"
category: "general-linux"
tags: ["setting", "installing", "rancher", "k3s"]
---

* Set up `docker` on the machine.
* Create the following file and add these modules:
```
sudo tee -a /etc/modules-load.d/rancher.conf <<EOF
ip_tables
ip_conntrack
iptable_filter
ipt_state
EOF
```
* `sudo reboot`
* Add HTTPS to the public zone and reload the firewall:
```
sudo firewall-cmd --permanent --zone=public --add-service=https
sudo firewall-cmd --reload
```
* Create the Rancher container:
```
docker run -d --restart=unless-stopped \
  -p 80:80 -p 443:443 \
  --privileged \
  rancher/rancher:latest
```
* Check the Docker logs for the password:
```
docker logs <container_ID> 2>&1 | grep "Bootstrap Password:"
```
* Access the node via its IP address (no need to specify a port) and continue the setup.