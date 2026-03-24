---
title: "Commands To Check For Faulty Disks"
category: "general-linux"
tags: ["commands", "check", "faulty", "disks"]
---

sudo dmidecode -t 1 | grep -E ""Version"|"Serial""

udevadm info --query=all --name=/dev/<DRIVE_HERE> | grep ID_SERIAL

ls -l --colour /dev/disk/by-path/ | grep -v '\-part' | sort -k11

for i in a..j; do echo /dev/sd$i && sudo smartctl -a /dev/sd$i; done

for i in a..j; do echo /dev/sd$i && sudo smartctl -t short /dev/sd$i; done > 00078883_smart_ctl-a.txt

sudo smartctl -t short 

for i in $(lsscsi | awk 'print $NF'); do echo "Disk $i"; sudo smartctl -a $i |grep -E ""PASSED"|"Serial"|"User"|^ "5"|^"197"|^"198""; done

sudo lsblk