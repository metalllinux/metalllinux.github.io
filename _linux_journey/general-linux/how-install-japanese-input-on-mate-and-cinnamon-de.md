---
title: "Add the following:"
category: "general-linux"
tags: ["install", "japanese", "input", "mate", "cinnamon"]
---

sudo yum install @input-methods
sudo dnf install ibus-anthy
vim ~/.bashrc
# Add the following:
```
export XMODIFIERS=@im=ibus
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export LC_ALL=en_US.UTF-8
ibus-daemon &
```
ibus-setup
# Then select Anthy from the Japanese Language options.