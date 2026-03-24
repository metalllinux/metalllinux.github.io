---
title: "While Loops For Holistic Logging"
category: "general-linux"
tags: ["while", "loops", "holistic", "logging"]
---

```
while true
do
    echo -e "$(date '+TIME:%Y-%m-%d-%H:%M:%S')\n $(docker stats --no-stream)" | tee -a docker_stats_--no-stream 
done
```
* The next command is to capture the output of `docker info`:
```
while true
do
    echo -e "$(date '+TIME:%Y-%m-%d-%H:%M:%S')\n $(docker info)" | tee -a docker_info
done
```
* Again, created another `tmux` window and wanted to capture the output of `docker ps -a`.
```
while true
do
    echo -e "$(date '+TIME:%Y-%m-%d-%H:%M:%S')\n $(docker ps -a)" | tee -a docker_ps_-a
done
```
* Command to capture the running processes.
```
while true
do
    echo -e "$(date '+TIME:%Y-%m-%d-%H:%M:%S')\n $(ps aux)" | tee -a ps_aux
done
```
* Capture the output of `top`.
```
while true
do
    echo -e "$(date '+TIME:%Y-%m-%d-%H:%M:%S')\n $(top -b -n1)" | tee -a top_output
done
```
* Installed the `sysstat` package, to then be able to use `mpstat`:
```
sudo dnf install -y sysstat
```
* Command to capture the `mpstat` output for each processor core.
```
while true
do
    echo -e "$(date '+TIME:%Y-%m-%d-%H:%M:%S')\n $(mpstat -P ALL)" | tee -a mpstat
done
```
* Command to capture `iostat` output.
```
while true
do
    echo -e "$(date '+TIME:%Y-%m-%d-%H:%M:%S')\n $(iostat)" | tee -a iostat
done
```
* Run `docker inspect` on select containers to see CPU and memory usage.
```
while true
do
    echo -e "$(date '+TIME:%Y-%m-%d-%H:%M:%S')\n $(docker inspect <YOUR_CONTAINER_NAME_HERE>)" | tee -a docker_inspect_<YOUR_CONTAINER_NAME_HERE>
done
```
* In addition, alongside the `docker inspect` command, take regular readings of the same container's `cpuacct.usage_all` file.
```
while true
do
    echo -e "$(date '+TIME:%Y-%m-%d-%H:%M:%S')\n $(cat /sys/fs/cgroup/cpu/docker/<YOUR_CONTAINER_ID_HERE>/cpuacct.usage_all)" | tee -a cpuacct.usage_all_<YOUR_CONTAINER_ID_HERE>
done
```
* Capturing memory output.
```
while true
do
    echo -e "$(date '+TIME:%Y-%m-%d-%H:%M:%S')\n $(free -h)" | tee -a free_-h
done
```
* Continuously capture the output of `dmesg`.
```
dmesg -T --follow > dmesg_output.log
```
* Write the output of `ethtool -S` to a file.
```
while true
do
    echo -e "$(date '+TIME:%Y-%m-%d-%H:%M:%S')\n $(ethtool -S <YOUR_INTERFACE_HERE>)" | tee -a ethtool_-s_<YOUR_INTERFACE_HERE>
done
```
* Output CPU `sar` readings to a file.
```
sar -u ALL 1 | tee -a sar_cpu
```
* Output memory `sar` readings to a file.
```
sar -r 1 | tee -a sar_memory
```
* Output swap `sar` readings to a file.
```
sar -S 1 | tee -a sar_swap
```
* Output I/O `sar` readings to a file.
```
sar -b 1 | tee -a sar_io
```
* Record IO for individual block devices.
```
sar -p -d 1 | tee -a sar_block_device_io
```
* Record context switches per second.
```
sar -w 1 | tee -a sar_context_switches
```
* Note run queue and load average.
```
sar -q 1 | tee -a sar_run_queue_load_average
```
* Check network statistics.
```
sar -n ALL 1 | tee -a sar_network_statistics
```