---
title: "Tutorial On How To Write Basic Udev Rules In Linux"
category: "general-linux"
tags: ["tutorial", "write", "basic", "udev", "rules"]
---

[Skip to content](#content "Skip to content")

- [Ubuntu](https://linuxconfig.org/ubuntu)
    - [Ubuntu 20.04 Guide](https://linuxconfig.org/ubuntu-20-04-guide)
    - [Ubuntu 18.04](https://linuxconfig.org/ubuntu-18-04)
- [Debian](https://linuxconfig.org/debian)
- [Redhat / CentOS / AlmaLinux](https://linuxconfig.org/redhat)
- [Fedora](https://linuxconfig.org/fedora)
- [Kali Linux](https://linuxconfig.org/kali-linux)

[![Linux Tutorials – Learn Linux Configuration](../_resources/logo-lx_5b6199414a1947b4912f0cf562451eec.avif)](https://linuxconfig.org/)

- [Linux Tutorials](https://linuxconfig.org/linux-tutorials)
- [System Admin](https://linuxconfig.org/system-administration-configuration)
- [Programming](https://linuxconfig.org/programming-scripting)
- [Multimedia](https://linuxconfig.org/multimedia-games)
- [Forum](https://forum.linuxconfig.org/)
- [Linux Commands](https://linuxconfig.org/linux-commands)
- [Linux Jobs](https://linuxconfig.org/linuxcareers-com-linux-job-portal)

[](#)

# Tutorial on how to write basic udev rules in Linux

21 August 2018 by [Egidio Docile](https://linuxconfig.org/author/egidio "View all posts by Egidio Docile")

## Objective

Understanding the base concepts behind udev, and learn how to write simple rules

## Requirements

- Root permissions

## Difficulty

MEDIUM

## Conventions

- **#** – requires given [linux commands](https://linuxconfig.org/linux-commands) to be executed with root privileges either  
    directly as a root user or by use of `sudo` command
- **$** – requires given [linux commands](https://linuxconfig.org/linux-commands) to be executed as a regular non-privileged user

## Introduction

In a GNU/Linux system, while devices low level support is handled at the kernel level, the management of events related to them is managed in userspace by `udev`, and more precisely by the `udevd` daemon. Learning how to write rules to be applied on the occurring of those events can be really useful to modify the behaviour of the system and adapt it to our needs.

## How rules are organised

Udev rules are defined into files with the `.rules` extension. There are two main locations in which those files can be placed: `/usr/lib/udev/rules.d` it’s the directory used for system-installed rules, `/etc/udev/rules.d/` is reserved for custom made rules.

The files in which the rules are defined are conventionally named with a number as prefix (e.g `50-udev-default.rules`) and are processed in lexical order independently of the directory they are in. Files installed in `/etc/udev/rules.d`, however, override those with the same name installed in the system default path.

* * *

* * *

## The rules syntax

The syntax of udev rules is not very complicated once you understand the logic behind it. A rule is composed by two main sections: the “match” part, in which we define the conditions for the rule to be applied, using a series of keys separated by a comma, and the “action” part, in which we perform some kind of action, when the conditions are met.

## A test case

What a better way to explain possible options than to configure an actual rule? As an example, we are going to define a rule to disable the touchpad when a mouse is connected. Obviously the attributes provided in the rule definition, will reflect my hardware.

We will write our rule in the `/etc/udev/rules.d/99-togglemouse.rules` file with the help of our favourite text editor. A rule definition can span over multiple lines, but if that’s the case, a backslash must be used before the newline character, as a line continuation, just as in shell scripts. Here is our rule:

```
ACTION=="add" \
, ATTRS{idProduct}=="c52f" \
, ATTRS{idVendor}=="046d" \
, ENV{DISPLAY}=":0" \
, ENV{XAUTHORITY}="/run/user/1000/gdm/Xauthority" \
, RUN+="/usr/bin/xinput --disable 16"
```

Let’s analyze it.

## Operators

First of all, an explanation of the used and possible operators:

#### \== and != operators

The `==` is the equality operator and the `!=` is the inequality operator. By using them we establish that for the rule to be applied the defined keys must match, or not match the defined value respectively.

#### The assignment operators: = and :=

The `=` assignment operator, is used to assign a value to the keys that accepts one. We use the `:=` operator, instead, when we want to assign a value and we want to make sure that it is not overridden by other rules: the values assigned with this operator, in facts, cannot be altered.

#### The += and -= operators

The `+=` and `-=` operators are used respectively to add or to remove a value from the list of values defined for a specific key.

* * *

* * *

## The keys we used

Let’s now analyze the keys we used in the rule. First of all we have the `ACTION` key: by using it, we specified that our rule is to be applied when a specific event happens for the device. Valid values are `add`, `remove` and `change`

We then used the `ATTRS` keyword to specify an attribute to be matched. We can list a device attributes by using the `udevadm info` command, providing its name or `sysfs` path:

```
udevadm info -ap /devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.2/2-1.2:1.1/0003:046D:C52F.0010/input/input39


Udevadm info starts with the device specified by the devpath and then
walks up the chain of parent devices. It prints for every device
found, all possible attributes in the udev rules key format.
A rule to match, can be composed by the attributes of the device
and the attributes from one single parent device.

  looking at device '/devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.2/2-1.2:1.1/0003:046D:C52F.0010/input/input39':
    KERNEL=="input39"
    SUBSYSTEM=="input"
    DRIVER==""
    ATTR{name}=="Logitech USB Receiver"
    ATTR{phys}=="usb-0000:00:1d.0-1.2/input1"
    ATTR{properties}=="0"
    ATTR{uniq}==""

  looking at parent device '/devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.2/2-1.2:1.1/0003:046D:C52F.0010':
    KERNELS=="0003:046D:C52F.0010"
    SUBSYSTEMS=="hid"
    DRIVERS=="hid-generic"
    ATTRS{country}=="00"

  looking at parent device '/devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.2/2-1.2:1.1':
    KERNELS=="2-1.2:1.1"
    SUBSYSTEMS=="usb"
    DRIVERS=="usbhid"
    ATTRS{authorized}=="1"
    ATTRS{bAlternateSetting}==" 0"
    ATTRS{bInterfaceClass}=="03"
    ATTRS{bInterfaceNumber}=="01"
    ATTRS{bInterfaceProtocol}=="00"
    ATTRS{bInterfaceSubClass}=="00"
    ATTRS{bNumEndpoints}=="01"
    ATTRS{supports_autosuspend}=="1"

  looking at parent device '/devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.2':
    KERNELS=="2-1.2"
    SUBSYSTEMS=="usb"
    DRIVERS=="usb"
    ATTRS{authorized}=="1"
    ATTRS{avoid_reset_quirk}=="0"
    ATTRS{bConfigurationValue}=="1"
    ATTRS{bDeviceClass}=="00"
    ATTRS{bDeviceProtocol}=="00"
    ATTRS{bDeviceSubClass}=="00"
    ATTRS{bMaxPacketSize0}=="8"
    ATTRS{bMaxPower}=="98mA"
    ATTRS{bNumConfigurations}=="1"
    ATTRS{bNumInterfaces}==" 2"
    ATTRS{bcdDevice}=="3000"
    ATTRS{bmAttributes}=="a0"
    ATTRS{busnum}=="2"
    ATTRS{configuration}=="RQR30.00_B0009"
    ATTRS{devnum}=="12"
    ATTRS{devpath}=="1.2"
    ATTRS{idProduct}=="c52f"
    ATTRS{idVendor}=="046d"
    ATTRS{ltm_capable}=="no"
    ATTRS{manufacturer}=="Logitech"
    ATTRS{maxchild}=="0"
    ATTRS{product}=="USB Receiver"
    ATTRS{quirks}=="0x0"
    ATTRS{removable}=="removable"
    ATTRS{speed}=="12"
    ATTRS{urbnum}=="1401"
    ATTRS{version}==" 2.00"

    [...]
```

* * *

* * *

Above is the truncated output received after running the command. As you can read it from the output itself, `udevadm` starts with the specified path that we provided, and gives us information about all the parent devices. Notice that attributes of the device are reported in singular form (e.g `KERNEL`), while the parent ones in plural form (e.g `KERNELS`). The parent information can be part of a rule but only one of the parents can be referenced at a time: mixing attributes of different parent devices will not work. In the rule we defined above, we used the attributes of one parent device: `idProduct` and `idVendor`.

The next thing we have done in our rule, is to use the `ENV` keyword: it can be used to both set or try to match environment variables. We assigned a value to the `DISPLAY` and `XAUTHORITY` ones. Those variables are essential when interacting with the X server programmatically, to setup some needed information: with the `DISPLAY` variable, we specify on what machine the server is running, what display and what screen we are referencing, and with `XAUTHORITY` we provide the path to the file which contains Xorg authentication and authorisation information. This file is usually located in the users “home” directory.

Finally we used the `RUN` keyword: this is used to run external programs. Very important: this is not executed immediately, but the various actions are executed once all the rules have been parsed. In this case we used the `xinput` utility to change the status of the touchpad. I will not explain the syntax of xinput here, it would be out of context, just notice that `16` is the id of the touchpad.

Once our rule is set, we can debug it by using the `udevadm test` command. This is useful for debugging but it doesn’t really run commands specified using the `RUN` key:

```
$ udevadm test --action="add" /devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.2/2-1.2:1.1/0003:046D:C52F.0010/input/input39
```

What we provided to the command is the action to simulate, using the `--action` option, and the sysfs path of the device. If no errors are reported, our rule should be good to go. To run it in the real world, we must reload the rules:

```
# udevadm control --reload
```

This command will reload the rules files, however, will have effect only on new generated events.

We have seen the basic concepts and logic used to create an udev rule, however we only scratched the surface of the many options and possible settings. The udev manpage provides an exhaustive list: please refer to it for a more in-depth knowledge.

### Related Linux Tutorials:

- [How to handle ACPI events on Linux](https://linuxconfig.org/how-to-handle-acpi-events-on-linux)
- [Advanced Logging and Auditing on Linux](https://linuxconfig.org/advanced-logging-and-auditing-on-linux)
- [How to monitor filesystem events on files and…](https://linuxconfig.org/how-to-monitor-filesystem-events-on-files-and-directories-on-linux)
- [An Introduction to Linux Automation, Tools and Techniques](https://linuxconfig.org/an-introduction-to-linux-automation-tools-and-techniques)
- [How to export repositories with the git-daemon](https://linuxconfig.org/how-to-export-repositories-with-the-git-daemon)
- [Assigning File Permissions to Specific Users with…](https://linuxconfig.org/assigning-file-permissions-to-specific-users-with-chmod-and-setfacl)
- [Linux Configuration files: Top 30 most important](https://linuxconfig.org/linux-configuration-files-top-30-most-important)
- [Can Linux Get Viruses? Exploring the Vulnerability…](https://linuxconfig.org/can-linux-get-viruses-exploring-the-vulnerability-of-linux-systems)
- [MX Linux vs Ubuntu](https://linuxconfig.org/mx-linux-vs-ubuntu)
- [How to install Linux kernel headers on Raspberry Pi](https://linuxconfig.org/how-to-install-linux-kernel-headers-on-raspberry-pi)

Categories [Programming & Scripting](https://linuxconfig.org/programming-scripting)

[How to find all files with a specific text using Linux shell](https://linuxconfig.org/how-to-find-all-files-with-a-specific-text-using-linux-shell)

[How to use DNSenum to scan your server’s DNS records](https://linuxconfig.org/how-to-use-dnsenum-to-scan-your-server-s-dns-records)

* * *

* * *

**Comments and Discussions**  
![Linux Forum](../_resources/linuxconfig-forum-logo-1_77f013d2fd2044389084b0486.webp)

* * *

### NEWSLETTER

Subscribe to Linux Career Newsletter to receive latest news, jobs, career advice and featured configuration tutorials.

[SUBSCRIBE](https://bit.ly/2X5D30q)

### WRITE FOR US

LinuxConfig is looking for a technical writer(s) geared towards GNU/Linux and FLOSS technologies. Your articles will feature various GNU/Linux configuration tutorials and FLOSS technologies used in combination with GNU/Linux operating system.

When writing your articles you will be expected to be able to keep up with a technological advancement regarding the above mentioned technical area of expertise. You will work independently and be able to produce at minimum 2 technical articles a month.

[APPLY NOW](https://www.linuxcareers.com/jobs/floss-technical-writer-new-york-city-new-york/1-1/)

## TAGS

[18.04](https://linuxconfig.org/tag/18-04) [administration](https://linuxconfig.org/tag/administration) [apache](https://linuxconfig.org/tag/apache) [applications](https://linuxconfig.org/tag/applications) [backup](https://linuxconfig.org/tag/backup) [bash](https://linuxconfig.org/tag/bash) [beginner](https://linuxconfig.org/tag/beginner) [browser](https://linuxconfig.org/tag/browser) [centos](https://linuxconfig.org/tag/centos) [centos8](https://linuxconfig.org/tag/centos8) [commands](https://linuxconfig.org/tag/commands) [database](https://linuxconfig.org/tag/database) [debian](https://linuxconfig.org/tag/debian) [desktop](https://linuxconfig.org/tag/desktop) [development](https://linuxconfig.org/tag/development) [docker](https://linuxconfig.org/tag/docker) [error](https://linuxconfig.org/tag/error) [fedora](https://linuxconfig.org/tag/fedora) [filesystem](https://linuxconfig.org/tag/filesystem) [firewall](https://linuxconfig.org/tag/firewall) [gaming](https://linuxconfig.org/tag/gaming) [gnome](https://linuxconfig.org/tag/gnome) [Hardware](https://linuxconfig.org/tag/hardware) [installation](https://linuxconfig.org/tag/installation) [kali](https://linuxconfig.org/tag/kali) [multimedia](https://linuxconfig.org/tag/multimedia) [networking](https://linuxconfig.org/tag/networking) [nvidia](https://linuxconfig.org/tag/nvidia) [programming](https://linuxconfig.org/tag/programming) [python](https://linuxconfig.org/tag/python) [raspberrypi](https://linuxconfig.org/tag/raspberrypi) [redhat](https://linuxconfig.org/tag/redhat) [rhel8](https://linuxconfig.org/tag/rhel8) [scripting](https://linuxconfig.org/tag/scripting) [security](https://linuxconfig.org/tag/security) [server](https://linuxconfig.org/tag/server) [ssh](https://linuxconfig.org/tag/ssh) [storage](https://linuxconfig.org/tag/storage) [terminal](https://linuxconfig.org/tag/terminal) [ubuntu](https://linuxconfig.org/tag/ubuntu) [ubuntu 20.04](https://linuxconfig.org/tag/ubuntu-20-04) [video](https://linuxconfig.org/tag/video) [virtualisation](https://linuxconfig.org/tag/virtualisation) [webapp](https://linuxconfig.org/tag/webapp) [webserver](https://linuxconfig.org/tag/webserver)

[ABOUT US](https://linuxconfig.org/about-us)

### FEATURED TUTORIALS

- [VIM tutorial for beginners](https://linuxconfig.org/vim-tutorial)
- [How to install the NVIDIA drivers on Ubuntu 20.04 Focal Fossa Linux](https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-20-04-focal-fossa-linux)
- [Bash Scripting Tutorial for Beginners](https://linuxconfig.org/bash-scripting-tutorial-for-beginners)
- [How to check CentOS version](https://linuxconfig.org/how-to-check-centos-version)
- [How to find my IP address on Ubuntu 20.04 Focal Fossa Linux](https://linuxconfig.org/how-to-find-my-ip-address-on-ubuntu-20-04-focal-fossa-linux)
- [Ubuntu 20.04 Remote Desktop Access from Windows 10](https://linuxconfig.org/ubuntu-20-04-remote-desktop-access-from-windows-10)
- [Howto mount USB drive in Linux](https://linuxconfig.org/howto-mount-usb-drive-in-linux)
- [How to install missing ifconfig command on Debian Linux](https://linuxconfig.org/how-to-install-missing-ifconfig-command-on-debian-linux)
- [AMD Radeon Ubuntu 20.04 Driver Installation](https://linuxconfig.org/amd-radeon-ubuntu-20-04-driver-installation)
- [Ubuntu Static IP configuration](https://linuxconfig.org/how-to-configure-static-ip-address-on-ubuntu-18-10-cosmic-cuttlefish-linux)
- [How to use bash array in a shell script](https://linuxconfig.org/how-to-use-arrays-in-bash-script)
- [Linux IP forwarding – How to Disable/Enable](https://linuxconfig.org/how-to-turn-on-off-ip-forwarding-in-linux)
- [How to install Tweak Tool on Ubuntu 20.04 LTS Focal Fossa Linux](https://linuxconfig.org/how-to-install-tweak-tool-on-ubuntu-20-04-lts-focal-fossa-linux)
- [How to enable/disable firewall on Ubuntu 18.04 Bionic Beaver Linux](https://linuxconfig.org/how-to-enable-disable-firewall-on-ubuntu-18-04-bionic-beaver-linux)
- [Netplan static IP on Ubuntu configuration](https://linuxconfig.org/how-to-configure-static-ip-address-on-ubuntu-18-04-bionic-beaver-linux)
- [How to change from default to alternative Python version on Debian Linux](https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux)
- [Set Kali root password and enable root login](https://linuxconfig.org/how-to-enable-root-login-on-kali-linux)
- [How to Install Adobe Acrobat Reader on Ubuntu 20.04 Focal Fossa Linux](https://linuxconfig.org/how-to-install-adobe-acrobat-reader-on-ubuntu-20-04-focal-fossa-linux)
- [How to install the NVIDIA drivers on Ubuntu 18.04 Bionic Beaver Linux](https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-18-04-bionic-beaver-linux)
- [How to check NVIDIA driver version on your Linux system](https://linuxconfig.org/how-to-check-nvidia-driver-version-on-your-linux-system)
- [Nvidia RTX 3080 Ethereum Hashrate and Mining Overclock settings on HiveOS Linux](https://linuxconfig.org/nvidia-rtx-3080-eth-hashrate-and-overclock-settings-on-hiveos)

### LATEST TUTORIALS

- [Using sed and Bash to Fill Empty Cells in a CSV File](https://linuxconfig.org/how-to-fill-all-empty-valued-cells-within-a-csv-file-with-sed-and-bash-shell)
- [SSH Tunnels: Secure Remote Access and Port Forwarding](https://linuxconfig.org/introduction-to-ssh-port-forwarding)
- [Self-Host Immich: Open Source Google Photos Alternative](https://linuxconfig.org/introduction-to-immich-the-open-source-alternative-to-google-photos)
- [How to manage files on cloud storage with Rclone on Linux](https://linuxconfig.org/how-to-manage-files-on-cloud-storage-with-rclone-on-linux)
- [How to write and perform Ubuntu unattended installations with autoinstall](https://linuxconfig.org/how-to-write-and-perform-ubuntu-unattended-installations-with-autoinstall)
- [How to install and configure a restic REST server on Linux](https://linuxconfig.org/how-install-and-configure-a-restic-rest-server-on-linux)
- [Securing Linux with TCP Wrappers: A Quick How-To](https://linuxconfig.org/securing-linux-with-tcp-wrappers-a-quick-how-to)
- [Using Logwatch for Basic Security Monitoring on Linux](https://linuxconfig.org/using-logwatch-for-basic-security-monitoring-on-linux)
- [Container Security Best Practices: Securing Docker](https://linuxconfig.org/container-security-best-practices-securing-docker)
- [Advanced Firewall Management with nftables: Transitioning from iptables](https://linuxconfig.org/advanced-firewall-management-with-nftables-transitioning-from-iptables)
- [How to check Raspberry Pi Java versions](https://linuxconfig.org/how-to-check-raspberry-pi-java-versions)
- [Automating Security Audits with Lynis on Linux Systems](https://linuxconfig.org/automating-security-audits-with-lynis-on-linux-systems)
- [How to automate interactive cli commands with expect](https://linuxconfig.org/how-to-automate-interactive-cli-commands-with-expect)
- [How to run Podman containers under Systemd with Quadlet](https://linuxconfig.org/how-to-run-podman-containers-under-systemd-with-quadlet)
- [Netplan network configuration tutorial for beginners](https://linuxconfig.org/netplan-network-configuration-tutorial-for-beginners)
- [How to use docker-compose with Podman on Linux](https://linuxconfig.org/how-to-use-docker-compose-with-podman-on-linux)
- [Ubuntu: Change Default Terminal Emulator](https://linuxconfig.org/ubuntu-change-default-terminal-emulator)
- [How to orchestrate restic backups with autorestic on Linux](https://linuxconfig.org/how-to-orchestrate-restic-backups-with-autorestic-on-linux)
- [How to Fix: Too Many Levels of Symbolic Links Error](https://linuxconfig.org/how-to-fix-too-many-levels-of-symbolic-links-error)
- [Ubuntu Restricted Extras: What They Are and How to Install Them](https://linuxconfig.org/ubuntu-restricted-extras-what-they-are-and-how-to-install-them)

© 2024 TOSID Group Pty Ltd - LinuxConfig.org

[](# "Scroll back to top")