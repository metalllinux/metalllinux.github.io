---
title: "How To Encrypt A Rocky Linux 9.5 Installation With"
category: "rocky-linux"
tags: ["rocky-linux", "encrypt", "rocky", "linux", "installation"]
---

* Select `Custom` and then `OK`.
* Remove any current partitions.
* Check the box that says `Encrypt these partitions` and then click the button to allow the installer to automatically create the partitions.
* Delete the Home partition and readjust the `/` partition.
* Recreate the Home partition and it will be automatically labelled as encrypted.