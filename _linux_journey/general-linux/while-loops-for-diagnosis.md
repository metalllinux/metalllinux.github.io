---
title: "While Loops For Diagnosis"
category: "general-linux"
tags: ["while", "loops", "diagnosis"]
---

* `ps -aux` to a file.
```
while true
do
    echo "$(date '+TIME:%Y-%m-%d%H:%M:%S') $(ps aux)" | tee -a ps_aux_log
    sleep 1
done
```
* Pod status to a file.
```
while true
do
    echo "$(date '+TIME:%Y-%m-%d%H:%M:%S') $(kubectl get pods)" | tee -a kubectl_get_pods_log
    sleep 1
done
```
* Kubernetes API response timings to a file.
```
while true
do
    echo "$(date '+TIME:%Y-%m-%d%H:%M:%S') $(kubectl get deployments -v=6)" | tee -a kubectl_get_deployments_log
    sleep 1
done
```
* Write memory status to a file.
```
while true
do
    echo "$(date '+TIME:%Y-%m-%d%H:%M:%S') $(sar -r)" | tee -a sar_memory_log
    sleep 1
done
```
* Write processor usage to a file.
```
while true
do
    echo "$(date '+TIME:%Y-%m-%d%H:%M:%S') $(sar -p)" | tee -a sar_processor_log
    sleep 1
done
```
* Write I/O usage to a file.
```
while true
do
    echo "$(date '+TIME:%Y-%m-%d%H:%M:%S') $(sar -b)" | tee -a sar_io_log
    sleep 1
done
```
* Write `docker stats` to a file.
```
while true
do
    echo "$(date '+TIME:%Y-%m-%d%H:%M:%S') $(docker stats --no-stream)" | tee -a docker_stats_log
    sleep 1
done
```