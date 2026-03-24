---
title: "What Does the %i Mean When Used in a Command"
category: "editors-and-tools"
tags: ["editors-and-tools", "mean", "when", "command"]
---

# What Does the %i Mean When Used in a Command

In these DNF (Dandified YUM) commands, `%i` is a systemd specifier that gets replaced with the instance name when used in a systemd service template unit file.

However, seeing `%i` in standalone DNF commands like this suggests these lines are likely from a systemd service template file (ending in `@.service`). When the service is instantiated, `%i` gets replaced with whatever comes after the `@` symbol.

For example, if you have a service template called `nvidia-cleanup@.service` and you run:
```bash
systemctl start nvidia-cleanup@550.service
```

Then `%i` would be replaced with `550`, resulting in:
- `dnf erase kmod-nvidia-550-*`
- `dnf erase lib-nvidia-550-*`
- `dnf erase nvidia*-550-*`

This pattern is commonly used for NVIDIA driver cleanup scripts where you want to remove all packages related to a specific driver version number. The `%i` allows you to create a single template that can work for any driver version by passing the version number as the instance parameter.

If these commands were meant to be run directly in a shell (not through systemd), you'd need to replace `%i` with the actual version number you want to target.

