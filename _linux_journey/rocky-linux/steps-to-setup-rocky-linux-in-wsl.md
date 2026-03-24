---
title: "Steps To Setup Rocky Linux In Wsl"
category: "rocky-linux"
tags: ["rocky-linux", "steps", "setup", "rocky", "linux"]
---

Also, psst 
@David Godlove
 :
Download https://dl.rockylinux.org/pub/rocky/9/images/x86_64/Rocky-9-Container-Base.latest.x86_64.tar.xz
wsl --import Rocky9 /Users/<UserName>/Rocky9_WSL <path-to/Rocky-9-Container-Base.latest.x86_64.tar.xz> --version 2
wsl -d Rocky9
Run wsl to launch
Add systemd=true under [boot] in /etc/wsl.conf so you can run services.  May have to restart WSL
Start installing stuff
https://docs.rockylinux.org/guides/interoperability/import_rocky_to_wsl/