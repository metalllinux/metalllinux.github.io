---
title: "Setting Up Infiniband On Rocky Linux 9.X"
category: "rocky-linux"
tags: ["rocky-linux", "setting", "infiniband", "rocky", "linux"]
---

* Install these packages:
```
sudo dnf install -y libibverbs-utils infiniband-diags
```
* Check the InfiniBand card is detected:
```
ibv_devices
```
* Display more information about an InfiniBand device:
```
ibv_devinfo -d <card_name>
```
* Display the status of a device:
```
ibstat <card_name>
```
* Install the `rdma-core` package:
```
sudo dnf install -y rdma-core
```
* Check that the two InfiniBand machines can talk to each other:
* Start a server on one machine on Port 1:
```
ibping -S -C mlx4_0 -P 1
```
* On the other machine, send the following packets:
```
ibping -c 50 -C mlx4_0 -P 1 -L 2
```
* `-L` is Local Identifier.
* `-C` is InfiniBand Channel Adapter.
* Get the `LID` value from the `ibstat` command.
* Setup the IP addressing.
* Create the InfiniBand connectino on each host:
```
sudo nmcli connection add type infiniband con-name ibp1s0 ifname ibp1s0 transport-mode Connected mtu 65520
```
* Set a `P_Key`:
```
sudo nmcli connection modify ibp1s0 infiniband.p-key 0x8002
```