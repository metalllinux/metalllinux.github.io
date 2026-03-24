---
title: "Nixos And Epson Ew 052A"
category: "general-linux"
tags: ["nixos", "epson", "052a"]
---

* Follow https://nixos.wiki/wiki/Printing
* Enable this line: `services.printing.enable = true;`
* Add the following to enable searching for WiFi printers:
`services.avahi = {
  enable = true;
  nssmdns = true;
  openFirewall = true;
};`
* Add the ppd files with:
`services.printing.drivers = [ pkgs.epson-escpr ];`
* Configure the printer and select the appropriate ppd file for your model at localhost:631