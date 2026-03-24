---
title: "No Impact on a VM when Using the fstrim Command to Save Space"
category: "general-linux"
tags: ["impact", "when", "fstrim", "command", "save"]
---

# No Impact on a VM when Using the fstrim Command to Save Space

## Impact of `fstrim` Command on VM

### Safety and Normal Operation
The `fstrim` command is generally safe to run on a VM and is considered a standard maintenance operation. It's designed to be non-destructive and only discards blocks that are already marked as unused by the filesystem.

### Potential Impacts During Execution

#### Performance Considerations
- Temporary I/O increase: `fstrim` generates disk I/O activity while scanning and discarding unused blocks
- Brief performance degradation: The VM may experience slower disk response times during the operation
- CPU usage: Minimal CPU impact, primarily I/O bound operation
- Duration: Depends on disk size and amount of unused space (typically minutes for a 93GB disk)

#### What Actually Happens
- `fstrim` sends `TRIM/DISCARD` commands for unused blocks to the underlying storage
- In your case with `QCOW2`, it allows the host to reclaim unused space from the image file
- Only affects genuinely unused blocks - no data loss occurs
- The filesystem remains fully accessible during the operation

### Best Practices for Running `fstrim`

1. Run during low-activity periods if possible (though not strictly necessary)
2. Start with a specific mount point: `sudo fstrim -v /` before using `-a` for all mount points
3. Monitor the output - it will show how much space was trimmed
4. The VM remains fully operational - no downtime required

### Expected Outcome for Your Situation
- Should help reduce the `rootdisk.qcow2` file size on the host
- May free up some of that 92.6 GB usage if there are unused blocks within the guest
- No negative impact on VM data or applications
- Worst case: No space is reclaimed (if all blocks are genuinely in use)

The command is reversible in the sense that if space is needed again, the `QCOW2` file will simply grow back as required.
