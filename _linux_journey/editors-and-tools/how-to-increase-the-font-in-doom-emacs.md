---
title: "✅ Step-by-step: Set permanent font size in Doom Emacs"
category: "editors-and-tools"
tags: ["editors-and-tools", "increase", "font", "doom", "emacs"]
---

To **permanently increase the font size in Doom Emacs**, you need to edit your Doom Emacs configuration file: `~/.doom.d/config.el`. Here's how:

---

### ✅ Step-by-step: Set permanent font size in Doom Emacs

1. **Open your Doom config:**

   ```emacs-lisp
   SPC f p             ;; (or M-x doom/open-private-config)
   ```

   or manually open:

   ```sh
   ~/.doom.d/config.el
   ```

2. **Set the font face (including size):**

   Add or edit the `doom-font` variable:

   ```emacs-lisp
   ;; Example: Fira Code, size 18
   (setq doom-font (font-spec :family "Fira Code" :size 18))
   ```

   If you use other fonts (e.g., JetBrains Mono, Source Code Pro), just change the `:family`.

3. **Optional – configure variable-pitch and big font (used for presentations):**

   ```emacs-lisp
   (setq doom-variable-pitch-font (font-spec :family "sans" :size 18)
         doom-big-font (font-spec :family "Fira Code" :size 24)) ;; for SPC z b
   ```

4. **Apply changes:**

   Run the following in your terminal:

   ```sh
   doom sync
   ```

5. **Restart Emacs** (or run `M-x doom/reload` or `SPC h r r`) to apply the new font.

---

### 🧪 Tips for Troubleshooting

* To see available fonts:
  Run this in Emacs:

  ```elisp
  (print (font-family-list))
  ```

* Ensure the font is **installed on your system** (e.g., Fira Code, JetBrains Mono).

* You can use `M-x describe-font` to inspect currently active font.

---

* Install the `fira-code` font on Rocky Linux:

```
sudo dnf install -y fira-code-fonts
```
