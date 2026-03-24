---
title: "✅ Root Cause:"
category: "general-linux"
tags: ["regarding", "autorandr", "help", "xfce", "resume"]
---

This issue is caused by **how XFCE with the proprietary NVIDIA driver handles display detection and monitor layout on resume from suspend**. The root cause is **the NVIDIA driver reporting hotplug events when displays are re-initialised** after waking, which **XFCE misinterprets and resets the display layout**. This is exacerbated when:

* **XFCE does not persistently store layouts across users/machines** by default.
* **No unified display profile is present**, or it is **invalidated** when EDID or port layout changes (even slightly).
* `nofb` (disable framebuffer console) might **interfere with early modesetting** expected by tools like `xrandr` or DEs on resume.

---

### ✅ Root Cause:

> **XFCE with the proprietary NVIDIA driver on Rocky 8.10 resets multi-monitor layout after suspend/resume due to unreliable detection events, lack of system-wide layout persistence, and possibly compounded by `nofb`.**

---

### ✅ Working Solutions

#### ✅ 1. **Disable `nofb` in kernel cmdline**

`nofb` disables the framebuffer console and can lead to misbehavior during suspend/resume. Modern systems no longer need this.

**Edit `/etc/default/grub`**:

```bash
sudo sed -i 's/\bnofb\b//g' /etc/default/grub
sudo grub2-mkconfig -o /boot/efi/EFI/rocky/grub.cfg
```

Then reboot.

---

#### ✅ 2. **Set up a system-wide autorandr profile hook**

Install [`autorandr`](https://github.com/phillipberndt/autorandr), which can dynamically re-apply monitor layouts on resume.

```bash
sudo dnf install autorandr xrandr
```

Set up a known layout:

```bash
xrandr # identify displays
autorandr --save dual-display-layout
```

Then create a systemd sleep hook:

```bash
sudo tee /lib/systemd/system-sleep/autorandr-resume.sh > /dev/null << 'EOF'
#!/bin/sh
case "$1" in
  post)
    export DISPLAY=:0
    export XAUTHORITY=/home/<your-user>/.Xauthority
    /usr/bin/autorandr --change --force
    ;;
esac
EOF
sudo chmod +x /lib/systemd/system-sleep/autorandr-resume.sh
```

> **Make sure to replace `<your-user>` with the actual user account that owns the X session.**

If multiple users use the system, you'll need to dynamically detect active sessions using something like `loginctl`.

---

#### ✅ 3. **Avoid XFCE display profile per-user**

Since you can't create per-user profiles in a dynamic hardware layout environment, **disable XFCE from auto-saving changes** by setting:

```bash
xfconf-query -c displays -p /Default/AutoApply -s false
```

Do this for all user profiles (`/etc/skel` or via automation if many users).

---

#### ✅ 4. **Use `nvidia-settings` to persist X configuration**

Instead of relying on XFCE display settings, use NVIDIA’s own tool:

```bash
sudo nvidia-settings
```

Set layout, then save to `/etc/X11/xorg.conf` (requires root). This helps NVIDIA persist layouts across reboots and resumes.

---

#### ✅ 5. **Set `IgnoreEDIDChecksum` in xorg.conf if EDID is flaky**

If monitors are incorrectly detected, add:

```conf
Section "Device"
    Identifier "Device0"
    Driver "nvidia"
    VendorName "NVIDIA Corporation"
    Option "UseEDID" "TRUE"
    Option "IgnoreEDIDChecksum" "DFP-0"
EndSection
```

Replace `DFP-0` with your monitor if needed.

---

### 🔗 References

* XFCE bug on display layout reset: [https://gitlab.xfce.org/xfce/xfce4-settings/-/issues/245](https://gitlab.xfce.org/xfce/xfce4-settings/-/issues/245)
* NVIDIA hotplug issues and suspend: [https://forums.developer.nvidia.com/t/issue-with-dual-monitors-after-suspend/120605](https://forums.developer.nvidia.com/t/issue-with-dual-monitors-after-suspend/120605)
* `autorandr` project: [https://github.com/phillipberndt/autorandr](https://github.com/phillipberndt/autorandr)
* EDID problems on resume: [https://wiki.archlinux.org/title/Kernel\_mode\_setting#Forcing\_modes\_and\_EDID](https://wiki.archlinux.org/title/Kernel_mode_setting#Forcing_modes_and_EDID)

---

### ✅ Recommended Permanent Fix Strategy:

1. **Remove `nofb`** from kernel cmdline (to allow proper framebuffer handoff).
2. **Use `autorandr` + systemd sleep hook** to re-apply display layout post-resume.
3. **Configure users to not autosave broken layouts**.
4. **Optional**: use `nvidia-settings` for system-wide X layout persistence if consistent hardware.
