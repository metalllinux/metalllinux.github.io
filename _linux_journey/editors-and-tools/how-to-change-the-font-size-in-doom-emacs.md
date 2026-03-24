---
title: "How to Change the Font Size in Doom Emacs"
category: "editors-and-tools"
tags: ["editors-and-tools", "change", "font", "size", "doom"]
---

# How to Change the Font Sise in Doom Emacs

1. **Open your Doom Emacs config file**
   Open `~/.config/doom/config.el` (this is the main config file for Doom Emacs).

2. **Set the font size**
   Add or modify the following line to change your default font and its size:

   ```elisp
   (setq doom-font (font-spec :family "Fira Code" :size 16))
   ```

   Replace `"Fira Code"` with your preferred font (must be installed on your system), and `16` with the size you want.

3. **Apply the changes**
   After saving the file, run this command in a terminal:

   ```sh
   doom sync
   ```

or 

```
spc + h + rr
```

   Then **restart Emacs**.

---

### 📌 Optional: Set other font types

You can also set fonts for different UI elements:

```elisp
(setq doom-font (font-spec :family "Fira Code" :size 16)
      doom-variable-pitch-font (font-spec :family "Cantarell" :size 16)
      doom-big-font (font-spec :family "Fira Code" :size 24)) ;; for presentations or zooming
```

You can toggle the big font (zoomed-in) mode with `SPC t z` (if you're using the default keybindings with `evil` and `doom`).

---

Let me know if you're using a different input method (e.g., GUI vs terminal) — font behaviour can differ slightly between `emacs`, `emacsclient`, and `terminal` Emacs.


