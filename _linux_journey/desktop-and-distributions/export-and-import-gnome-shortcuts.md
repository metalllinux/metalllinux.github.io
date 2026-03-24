---
title: "Export And Import Gnome Shortcuts"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "export", "import", "gnome", "shortcuts"]
---

The file this is stored in is: ~/.config/dconf/user

There is an extension, Extensions Sync - GNOME Shell Extensions 44

You can also do this manually with dconf or gsettings…
For example to backup my custom keyboard shortcuts: (Keyboard > Keyboard Shortcuts > Custom Shortcuts)
dconf dump /org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/ > custom.txt

To restore them:
cat custom.txt | dconf load /org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/

You can do similar for other settings or backup the full output.

OK for the extension.

relating to dconf dump :
it works with :

    dconf dump /org/gnome/settings-daemon/plugins/media-keys/

(without " `custom-keybindings/" at the end)

thanks for the quick reply and your help.

Can then do cat shortcuts.txt | dconf load /org/gnome/settings-daemon/plugins/media-keys/ to re-import the shortcuts again.