---
title: "Install Makemkv On Opensuse Tumbleweed From Source"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "install", "makemkv", "opensuse", "tumbleweed"]
---

* For the `makemkv-oss-1.17.5` package.
	* `sudo zypper install -t pattern devel_basis`
	* `sudo zypper in openssl-devel`
	* Add the packman repository:
	* `sudo zypper ar -cfp 90 'https://ftp.gwdg.de/pub/linux/misc/packman/suse/openSUSE_Tumbleweed/' packman`
	* `sudo zypper refresh`
	* `sudo zypper dup --from packman --allow-vendor-change`
	* `sudo zypper in ffmpeg-6-libavcodec-devel`
	* `sudo zypper in libqt5-qtbase-devel`
		* `./configure`
		* `make`
		* `sudo make install`
* For the `makemkv-bin-1.17.5` package.
	* `make`
	* `sudo make install`