---
title: "Command to Get the Full List of MSI / MSI-X Devices from an sosreport"
category: "rocky-linux"
tags: ["rocky-linux", "command", "full", "list", "msi"]
---

# Command to Get the Full List of MSI / MSI-X Devices from an sosreport

```
awk '
BEGIN { RS=""; FS="\n" }
{
    device=""; subsystem=""; numa=""; msi_caps=""
    
    for (i=1; i<=NF; i++) {
        if ($i ~ /^[0-9a-f]{2}:[0-9a-f]{2}\.[0-9]/) device=$i
        if ($i ~ /^\tSubsystem:/) subsystem=$i
        if ($i ~ /^\tNUMA node:/) numa=$i
        if ($i ~ /Capabilities:.*MSI-X:/) msi_caps = msi_caps "\n" $i
        else if ($i ~ /Capabilities:.*MSI:/) msi_caps = msi_caps "\n" $i
        else if ($i ~ /Capabilities:.*Express.*MSI/) msi_caps = msi_caps "\n" $i
    }
    
    if (device && msi_caps && !seen[device]++) {
        print device
        if (subsystem) print subsystem
        if (numa) print numa
        print msi_caps
        print ""
    }
}' ./<sosreport_name>/sos_commands/pci/lspci_-nnvv
```
