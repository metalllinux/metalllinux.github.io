---
title: "How Enable Optical Drives In Nixos"
category: "general-linux"
tags: ["enable", "optical", "drives", "nixos"]
---

`sudo modprobe sg`

To permanently enable these drives, add the following to your nix config:

`boot.kernelModules = [ “sg” ];`
