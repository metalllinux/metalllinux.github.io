---
title: "Gnome Shortcut Outputs"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "gnome", "shortcut", "outputs"]
---

```
    dconf dump /org/gnome/settings-daemon/plugins/media-keys/
[/]
calculator=['<Super>c']
custom-keybindings=['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom2/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom3/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom4/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom5/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom6/']
home=['<Super>e']
www=['<Super>f']

[custom-keybindings/custom0]
binding='<Primary><Alt>t'
command='gnome-terminal'
name='Terminal'

[custom-keybindings/custom1]
binding='<Super>b'
command='flatpak run com.bitwarden.desktop'
name='Bitwarden'

[custom-keybindings/custom2]
binding='<Super>j'
command='flatpak run net.cozic.joplin_desktop'
name='Joplin'

[custom-keybindings/custom3]
binding='<Shift><Super>l'
command='flatpak run org.libreoffice.LibreOffice'
name='Libreoffice'

[custom-keybindings/custom4]
binding='<Super>g'
command='flatpak run org.gimp.GIMP'
name='Gimp'

[custom-keybindings/custom5]
binding='<Shift><Super>v'
command='flatpak run org.videolan.VLC'
name='VLC'

[custom-keybindings/custom6]
binding='<Shift><Super>s'
command='flatpak run com.valvesoftware.Steam'
name='Steam'
```