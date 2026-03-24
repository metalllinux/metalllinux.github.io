---
title: "How to Change Modes in Emacs"
category: "editors-and-tools"
tags: ["editors-and-tools", "change", "modes", "emacs"]
---

# How to Change Modes in Emacs

Emacs displays the current mode in the mode line at the bottom of the window. If `C-x C-s` isn't working, you might be in a special mode where those keybindings are different. Here’s what you can do:

1. **Check the Mode Line:** Look at the bottom of the Emacs window—it's where your active modes are listed. The major mode (e.g., `Fundamental`, `Text`, `Org`, `Python`) appears on the left, followed by any enabled minor modes.

2. **Press `C-h m`:** This will show all active modes and their keybindings, helping you understand why certain shortcuts aren't behaving as expected.

3. **Try `M-x normal-mode`:** If keybindings feel off, running `M-x normal-mode` can reset the buffer to the default mode for your file type.

4. **Escape Key Issue:** Hitting `Esc` once in Emacs simply acts as a `Meta` key. If you're stuck in an unfamiliar mode, try `C-g` to cancel ongoing commands.

If `C-x C-s` is completely unresponsive, consider checking if you’re in a special minor mode that intercepts keybindings (like `overwrite-mode`). Let me know if you need more debugging tips.

