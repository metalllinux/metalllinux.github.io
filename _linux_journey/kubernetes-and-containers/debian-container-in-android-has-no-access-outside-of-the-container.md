---
title: "Debian Container in Android has No Access Outside of the Container"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "debian", "container", "android", "access"]
---

# Debian Container in Android has No Access Outside of the Container

The Debian Linux container feature in Android 15+ (running through Android Virtualisation Framework/AVF) is designed with strong isolation in mind. The container runs in a highly restricted sandbox with several layers of security:

## What the container **cannot** access by default:

- **Host Android filesystem** - The container cannot directly access files stored on your Android device outside its own virtual disk
- **Android apps and data** - No access to other apps, their data, or Android system services
- **Hardware devices** - Direct hardware access is extremely limited; most hardware interaction goes through virtualisation layers
- **Android network stack directly** - Network access is virtualised and can be restricted
- **Android sensors** - No direct access to cameras, microphones, GPS, etc.
- **Android system calls** - The container runs in a separate VM with its own kernel

## Limited exceptions and controlled access:

1. **Network connectivity** - The container typically gets network access through NAT, but this can be configured or disabled by the host

2. **Shared folders** - Android can explicitly share specific directories with the container through 9P filesystem mounts, but this requires explicit configuration

3. **Virtual devices** - Some virtualised devices may be exposed (like virtual GPU for graphics acceleration), but these are abstracted and controlled

4. **Resource limits** - CPU, memory, and storage are allocated by Android and the container cannot exceed these boundaries

The architecture uses nested virtualisation (KVM-based pKVM hypervisor) to ensure strong isolation. This is much more secure than traditional container solutions like chroot or even Docker, as it provides hardware-level isolation similar to running a separate OS in a traditional VM.

The security model is "deny by default" - the container has no access to Android resources unless explicitly granted through controlled interfaces. This makes it suitable for running untrusted code while protecting the Android system and user data.

