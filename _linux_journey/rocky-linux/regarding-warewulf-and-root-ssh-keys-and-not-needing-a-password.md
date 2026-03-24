---
title: "Regarding Warewulf and Root SSH Keys and Not Needing a Password"
category: "rocky-linux"
tags: ["rocky-linux", "regarding", "warewulf", "root", "ssh"]
---

# Regarding Warewulf and Root SSH Keys and Not Needing a Password
  
you can ssh n1 as root from wwctl to root at n1 because warewulf transfers root ssh public key to compute nodes. You dont need to set password to ssh if you ssh n1 from root of wwctl, ssh key auth will automatically work
