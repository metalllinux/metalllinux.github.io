---
title: "Enable Japanese Input On Solus"
category: "general-linux"
tags: ["enable", "japanese", "input", "solus"]
---

Install `ibus-mozc` via `eopkg`
Add the following to `.bashrc`

export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
ibus-daemon -drx

Then run `ibus-setup` and set Mozc as the input method.

Add Japanese Mozc keyboard to the System Settings as well.