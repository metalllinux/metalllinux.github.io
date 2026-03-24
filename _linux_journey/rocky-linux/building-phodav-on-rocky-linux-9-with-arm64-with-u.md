---
title: "Building Phodav On Rocky Linux 9 With Arm64 With U"
category: "rocky-linux"
tags: ["rocky-linux", "building", "phodav", "rocky", "linux"]
---

* Download Version 2.4 from https://download.gnome.org/sources/phodav/2.4/
* Install meson and ninja via:
	* sudo dnf install ninja-build
	* sudo dnf install pip3; pip3 install --user meson
* cd into the source directory and then run:
	* meson setup builddir
	* cd builddir
	* meson compile
* Download the davfs2 package for RHEL8 from https://dl.fedoraproject.org/pub/epel/8/Everything/aarch64/Packages/d/davfs2-1.5.6-1.el8.aarch64.rpm
	* Install the package with:
	* sudo dnf localinstall davfs2-1.5.6-1.el8.aarch64.rpm
* Place the build binary into your /usr/bin directory.
	* sudo cp ./spice-webdavd /usr/bin
* Run the binary with `sudo spice-webdavd -p 9843`
* You can access the share in Nautilus by navigating to Connect to a Server and using:
	* dav://localhost:9843/