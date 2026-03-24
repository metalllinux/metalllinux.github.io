---
title: "A Good Collection of SAR Commands to Run on a CentOS System"
category: "rocky-linux"
tags: ["rocky-linux", "good", "collection", "sar", "commands"]
---

# A Good Collection of SAR Commands to Run on a CentOS System

    Install the sysstat package:

yum install -y sysstat

    Enable the sysstat systemd service:

systemctl enable --now sysstat

    To monitor CPU usage, run the following command which will run every second:

sar -u 1

    For Memory utilisation monitoring, please run this command:

sar -r 1

    For Swap utilisation, please run:

sar -S 1

    To combine all of the above commands together, log the output and have them run in the background, please run:

nohup sar -u -r -S 1 > /var/log/sar_realtime.log 2>&1 &

    To cancel the background process, please use:

pkill -f "sar -u -r -S"

    In addition, for network interface statistics, you can run:

sar -n DEV 1

    Furthermore, for I/O checks, this is available with:

sar -d 1

    Finally, if you want to run all of the above command together:

nohup sar -u -r -S -n DEV -d 1 > /var/log/sar_realtime.log 2>&1 &

    To terminate the background process, please run:

pkill -f "sar -u -r -S -n DEV -d"

