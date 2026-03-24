---
title: "Command to Get the Full Total of MSI / MSI-X Capable Devices from an sosreport"
category: "rocky-linux"
tags: ["rocky-linux", "command", "full", "total", "msi"]
---

# Command to Get the Full Total of MSI / MSI-X Capable Devices from an sosreport

```
awk 'BEGIN{RS="";FS="\n"} 
{
    device=""
    for(i=1;i<=NF;i++) if($i ~ /^[0-9a-f]{2}:[0-9a-f]{2}\.[0-9]/) device=$i
    if(device && !seen[device]++) {
        if(/Capabilities:.*MSI:/ && !/MSI-X/) msi++
        if(/Capabilities:.*MSI-X:/) msix++
        if(/Capabilities:.*Express.*MSI/) express++
        if(/Capabilities:.*MSI:/ || /Capabilities:.*MSI-X:/ || /Capabilities:.*Express.*MSI/) unique++
    }
} 
END{
    print "Standalone MSI devices:", msi+0
    print "MSI-X devices:", msix+0
    print "PCIe Express MSI devices:", express+0
    print "----------------------------------------"
    print "Total unique MSI/MSI-X capable devices:", unique+0
}' ./<sosreport_name>/sos_commands/pci/lspci_-nnvv
```

