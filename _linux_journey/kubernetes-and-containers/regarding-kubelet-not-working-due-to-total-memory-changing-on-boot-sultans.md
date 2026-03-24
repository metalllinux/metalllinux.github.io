---
title: "Regarding Kubelet Not Working Due To Total Memory Changing On Boot Sultans Explanation"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "regarding", "kubelet", "working", "due"]
---

kubelet retrieves the total memory value for a node by [extracting the MemTotal value from the node's meminfo](https://github.com/google/cadvisor/blob/5adb1c3bb38b4c5d50b31f39faf3214a44ae479b/utils/sysinfo/sysinfo.go#L398), as evidenced by the [memoryCapacityRegexp regex](https://github.com/google/cadvisor/blob/5adb1c3bb38b4c5d50b31f39faf3214a44ae479b/utils/sysinfo/sysinfo.go#L35) used on that line.

According to the kubelet errors listed in the description above, the only problematic memory value is the total one, which caused the allocatable value to change as a side effect. You can prove this for certain because the difference between the two total values is exactly the same as the difference between the two allocatable values. And [in kubelet, the allocatable value is derived](https://github.com/kubernetes/kubernetes/blob/30b34fbcca3e32eca6af77c7cc15f13d94ecac01/pkg/kubelet/cm/memorymanager/policy_static.go#L788-L792) by taking the total value and subtracting systemReserved from it as well as any memory from hugepages. Since the delta between the two allocatable values is exactly the same as the delta between the two total values, that means that there wasn’t any impact due to hugepages.

Long story short: the root cause for both of customer’s kubelet errors in the description above is the change in total memory.

Now, comparing reboot1 to reboot2 shows that MemTotal didn’t change across the reboot.

Therefore, the issue wasn’t reproduced in the meminfo.tar.gz logs Google provided.

I suspect what triggers the change in total memory isn’t a reboot, but instead a kernel or BIOS update.

