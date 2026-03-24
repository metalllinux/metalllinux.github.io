---
title: "Reflash Scl21 Firmware"
category: "general-linux"
tags: ["reflash", "scl21", "firmware"]
---

* Use sudo heimdall --SYSTEM <firmware_image.tar.md5> --verbose
* Have to do it multiple times, sometimes Heimdall errors out with multiple libusb errors.
* Then Flash boot.img to get the AU screen to come up.
	* Use sudo heimdall --BOOT <boot.img> --verbose
* If it continues to not boot, then run:
	* sudo heimdall flash --SYSTEM system.img.ext4 --CACHE cache.img.ext4 --verbose
	* The phone should boot after that.