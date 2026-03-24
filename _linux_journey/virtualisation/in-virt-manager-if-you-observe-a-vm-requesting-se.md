---
title: "In Virt Manager, If You Observe A Vm Requesting Se"
category: "virtualisation"
tags: ["virtualisation", "virt", "manager", "you", "observe"]
---

* Go to `Preferences` and under `General` select `Enable XML editing`.
* Go to your virtual machine's `Show virtual hardware details` tab.
* Select `Boot options`, then go to the `XML` tab.
* Copy and paste the following under the `</os>` line:
```
<os firmware='efi'>
  <firmware>
    <feature enabled='yes' name='secure-boot'/>
    <feature enabled='yes' name='enrolled-keys'/>
  </firmware>
</os>
```
* Click `Apply`
* You may have to re-select your boot ISO under `SATA CDROM 1` --> `Source path`