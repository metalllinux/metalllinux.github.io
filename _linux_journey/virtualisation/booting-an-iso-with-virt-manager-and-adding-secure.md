---
title: "Booting An Iso With Virt Manager And Adding Secure"
category: "virtualisation"
tags: ["virtualisation", "booting", "iso", "virt", "manager"]
---

* Add the ISO.
* Set up the ISO with all of the resource requirements, disk size and so on.
* Before installation, configure the ISO's `Boot Options` XML file.
* Add the following XML before `</os>`:
```
<os firmware='efi'>
  <firmware>
    <feature enabled='yes' name='secure-boot'/>
    <feature enabled='yes' name='enrolled-keys'/>
  </firmware>
</os>
```
* Apply the changes and then click `Begin Installation`