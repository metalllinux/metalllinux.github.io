---
title: "Useful Commands Audio Checking"
category: "general-linux"
tags: ["useful", "commands", "audio", "checking"]
---

`lspci -k | grep -A 4 Audio`
`dmesg | grep 'snd\|audio\|firmware'`
`journalctl -k | grep -i 'alsa\|hda\|sof\|snd'`