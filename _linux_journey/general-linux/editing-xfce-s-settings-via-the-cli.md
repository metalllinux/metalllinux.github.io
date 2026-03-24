---
title: "Editing Xfce S Settings Via The Cli"
category: "general-linux"
tags: ["editing", "xfce", "settings", "cli"]
---

    I followed this guide to install and setup XFCE.
    Upon rebooting and selecting the Xfce session for the Desktop Environment at GDM, I was able to successfully log in.
    I set up NoMachine Free Edition version 8.14.2_1 on the Rocky Linux 8.10 machine as the Server and similarly installed the same version on my MacBook:

wget https://download.nomachine.com/download/8.14/Linux/nomachine_8.14.2_1_x86_64.rpm
sudo rpm -i nomachine_8.14.2_1_x86_64.rpm

    I confirmed the NoMachine service was running on the Rocky Linux 8.10 server. I could connect from my Macbook, logged in with my Admin credentials and clicked Ok to all prompts (no default settings such as Window Resising was changed).
    Confirmed on both the NoMachine Player and Server side for both devices that there were no screen lock or similar timeout settings that were applied.
    On the Rocky Linux 8.10 machine, I ensured the Settings --> Power Manager --> System --> System power saving's When inactive for option was set to Never (this was the default).
    Settings --> Power Manager --> System --> Security's Lock screen when system is going to sleep setting was unchecked.
    Under Settings --> Power Manager --> Display --> Display power management was set to ON.
    Settings --> Power Manager --> Display --> Display power management's Blank after, Put to sleep after and Switch off after settings were all set to Never.
    Under Settings --> Screensaver, I set Enable Screensaver to OFF.
    For Settings --> Screensaver --> Lock Screen, I also set Enable Lock Screen to OFF.
    I went through the customise-menu page from the XFCE Wiki and there were no options there for changing the Settings menu.
    Under Settings, there is the Settings Editor option. This has boolean options available for the screensaver and screen lock to be disabled and enabled. I researched further on the xfce4-settings-editor from this XFCE docs guide.
    xfce4-settings-editor is a GUI for the CLI tool Xfconf-query and is able to change settings in real-time.
    One way to lock the session is by running the following to automatically disable screen lock:

xfconf-query -c xfce4-session -p /general/LockCommand -s ""

    The above command will essentially set the value as empty under Settings Editor --> xfce4-session --> general --> LockCommand
    To then re-enable the lock screen, the following command can be applied:

xfconf-query -c xfce4-session -p /general/LockCommand -s "/usr/bin/gnome-screensaver-command --lock"

    Then afterwards you will see the LockCommand field populated with the /usr/bin/gnome-screensaver-command --lock option.
    Under Settings Editor --> xfce4-power-manager --> dpms-enabled, perform the equivalent of toggling Settings --> Power Manager --> Display --> Display power management's setting to OFF, this can be disabled with the following command:

xfconf-query -c xfce4-power-manager -p /xfce4-power-manager/dpms-enabled -T

    The power management options can also be re-enabled by running the same command again.
    To enable a screen lock, this is possible through running this command:

xfconf-query -c xfce4-screensaver -p /lock/enabled -T

    As before, running the command again will disable the screen lock.
    To disable the screensaver, this is done through this command:

xfconf-query -c xfce4-screensaver -p /saver/enabled -T

    This can also be disabled by performing the same command.
    It is also possible to be more specific if you want the command to be true or false:
    To specifically change a value to true or false rather than toggling it with the above -T option, you can use the following as an example to disable the lock screen:

xfconf-query -c xfce4-screensaver -p /lock/enabled -s true

    To disable the lock screen, then run:

xfconf-query -c xfce4-screensaver -p /lock/enabled -s false

    To add a delay to the screen lock, for example 10 minutes, run the below command:

xfconf-query -c xfce4-screensaver -p /lock/saver-activation/delay -s 10