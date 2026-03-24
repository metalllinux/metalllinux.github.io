---
title: "Set Up Go(Lang) On An Arm64 Vm"
category: "general-linux"
tags: ["golang", "arm64"]
---

* Download Go from https://go.dev/dl/
*  `sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.22.2.linux-arm64.tar.gz`
*  Add /usr/local/go/bin to the PATH environment variable.
```
export PATH=$PATH:/usr/local/go/bin
```
* This is either `$HOME/.profile` or `/etc/profile` globally.
* Source the variable afterwards with:
```
source <path_to_variable_name>
```
* Check the version of Go you are running with:
```
go version
```