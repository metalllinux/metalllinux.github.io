---
title: "How to Install Claude Emacs on Doom Emacs"
category: "editors-and-tools"
tags: ["editors-and-tools", "install", "claudeemacs", "doom", "emacs"]
---

# How to Install Claude Emacs on Doom Emacs

* Install the Claude Code CLI:

```
curl -fsSL https://claude.ai/install.sh | bash
```

* Add the following to Doom Emacs' `package.el`:

```
(package! claudemacs
  :recipe (:host github :repo "cpoile/claudemacs"))
```

* Add the following to `config.el`:

```
(use-package! claudemacs)
```

* Add the following to `packages.el` to install EAT `Emulate A Terminal`:

```
(package! eat)
```

* Add this configuration to the `config.el`:

```
(use-package! claudemacs
  :after (prog-mode)
  :config
  (define-key prog-mode-map (kbd "C-c C-e") #'claudemacs-transient-menu)
  (define-key emacs-lisp-mode-map (kbd "C-c C-e") #'claudemacs-transient-menu)
  (define-key text-mode-map (kbd "C-c C-e") #'claudemacs-transient-menu)
  (define-key python-base-mode-map (kbd "C-c C-e") #'claudemacs-transient-menu))

(with-eval-after-load 'eat
  (setq eat-term-scrollback-size 400000))
```

* Set up required fonts for Claude by placing the following into `config.el`:

```
(defun my/setup-custom-font-fallbacks-linux ()
  (interactive)
  "Configure font fallbacks on linux for symbols and emojis.
This will need to be called every time you change your font size,
to load the new symbol and emoji fonts."

  (setq use-default-font-for-symbols nil)

  ;; --- Configure for 'symbol' script ---
  ;; We add fonts one by one. Since we use 'prepend',
  ;; the last one added here will be the first one Emacs tries.
  ;; So, list them in reverse order of your preference.

  ;; Least preferred among this list for symbols (will be at the end of our preferred list)
  ;; (set-fontset-font t 'symbol "FreeSerif" nil 'prepend)
  ;; (set-fontset-font t 'symbol "NotoSansSymbols2" nil 'prepend)
  ;; (set-fontset-font t 'symbol "NotoSansCJKJP" nil 'prepend)
  ;; (set-fontset-font t 'symbol "unifont" nil 'prepend)
  (set-fontset-font t 'symbol "DejaVu Sans Mono" nil 'prepend)
  ;; Most preferred for symbols -- use your main font here
  (set-fontset-font t 'symbol "JetBrainsMono Nerd Font Mono" nil 'prepend)


  ;; --- Configure for 'emoji' script ---
  ;; Add fonts one by one, in reverse order of preference.

  ;; Least preferred among this list for emojis
  ;; (set-fontset-font t 'emoji "FreeSerif" nil 'prepend)
  ;; (set-fontset-font t 'emoji "NotoSansSymbols2" nil 'prepend)
  ;; (set-fontset-font t 'emoji "NotoSansCJKJP" nil 'prepend)
  ;; (set-fontset-font t 'emoji "unifont" nil 'prepend)
  (set-fontset-font t 'emoji "DejaVuSans" nil 'prepend)
  ;; (set-fontset-font t 'emoji "Noto Emoji" nil 'prepend) ;; If you install Noto Emoji
  ;; Most preferred for emojis -- use your main font here
  (set-fontset-font t 'emoji "JetBrainsMono Nerd Font Mono" nil 'prepend)
  )

;; to test if you have a font family installed:
;;   (find-font (font-spec :family "DejaVu Sans Mono"))

;; Then, add the fonts after your setup is complete:
(add-hook 'emacs-startup-hook
          (lambda ()
            (progn
              (when (string-equal system-type "gnu/linux")
                  (my/setup-custom-font-fallbacks-linux)))))
```

* The final `config.el` file looks like this:

```
;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; Place your private configuration here! Remember, you do not need to run 'doom
;; sync' after modifying this file!


;; Some functionality uses this to identify you, e.g. GPG configuration, email
;; clients, file templates and snippets. It is optional.
;; (setq user-full-name "John Doe"
;;       user-mail-address "john@doe.com")

;; Doom exposes five (optional) variables for controlling fonts in Doom:
;;
;; - `doom-font' -- the primary font to use
;; - `doom-variable-pitch-font' -- a non-monospace font (where applicable)
;; - `doom-big-font' -- used for `doom-big-font-mode'; use this for
;;   presentations or streaming.
;; - `doom-symbol-font' -- for symbols
;; - `doom-serif-font' -- for the `fixed-pitch-serif' face
;;
;; See 'C-h v doom-font' for documentation and more examples of what they
;; accept. For example:
;;
;;(setq doom-font (font-spec :family "Fira Code" :size 12 :weight 'semi-light)
;;      doom-variable-pitch-font (font-spec :family "Fira Sans" :size 13))
;;
;; If you or Emacs can't find your font, use 'M-x describe-font' to look them
;; up, `M-x eval-region' to execute elisp code, and 'M-x doom/reload-font' to
;; refresh your font settings. If Emacs still can't find your font, it likely
;; wasn't installed correctly. Font issues are rarely Doom issues!

;; There are two ways to load a theme. Both assume the theme is installed and
;; available. You can either set `doom-theme' or manually load a theme with the
;; `load-theme' function. This is the default:
(setq doom-theme 'doom-one)

;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
(setq display-line-numbers-type t)

;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(setq org-directory "~/org/")


;; Whenever you reconfigure a package, make sure to wrap your config in an
;; `after!' block, otherwise Doom's defaults may override your settings. E.g.
;;
;;   (after! PACKAGE
;;     (setq x y))
;;
;; The exceptions to this rule:
;;
;;   - Setting file/directory variables (like `org-directory')
;;   - Setting variables which explicitly tell you to set them before their
;;     package is loaded (see 'C-h v VARIABLE' to look up their documentation).
;;   - Setting doom variables (which start with 'doom-' or '+').
;;
;; Here are some additional functions/macros that will help you configure Doom.
;;
;; - `load!' for loading external *.el files relative to this one
;; - `use-package!' for configuring packages
;; - `after!' for running code after a package has loaded
;; - `add-load-path!' for adding directories to the `load-path', relative to
;;   this file. Emacs searches the `load-path' when you load packages with
;;   `require' or `use-package'.
;; - `map!' for binding new keys
;;
;; To get information about any of these functions/macros, move the cursor over
;; the highlighted symbol at press 'K' (non-evil users must press 'C-c c k').
;; This will open documentation for it, including demos of how they are used.
;; Alternatively, use `C-h o' to look up a symbol (functions, variables, faces,
;; etc).
;;
;; You can also try 'gd' (or 'C-c c d') to jump to their definition and see how
;; they are implemented.
(defun markdown-html (buffer)
  (princ (with-current-buffer buffer
           (format "<!DOCTYPE html><html><title>Impatient Markdown</title><xmp theme=\"united\" style=\"display:none;\"> %s  </xmp><script src=\"http://ndossougbe.github.io/strapdown/dist/strapdown.js\"></script></html>"
                   (buffer-substring-no-properties (point-min) (point-max))))
         (current-buffer)))

(use-package! claudemacs
  :after (prog-mode)
  :config
  (define-key prog-mode-map (kbd "C-c C-e") #'claudemacs-transient-menu)
  (define-key emacs-lisp-mode-map (kbd "C-c C-e") #'claudemacs-transient-menu)
  (define-key text-mode-map (kbd "C-c C-e") #'claudemacs-transient-menu)
  ;; For Python mode, use after! to ensure it's loaded first
  (after! python
    (define-key python-base-mode-map (kbd "C-c C-e") #'claudemacs-transient-menu)))

(with-eval-after-load 'eat
  (setq eat-term-scrollback-size 400000))

(defun my/setup-custom-font-fallbacks-linux ()
  "Configure font fallbacks on linux for symbols and emojis.
This will need to be called every time you change your font size,
to load the new symbol and emoji fonts."
  (interactive)

  (setq use-default-font-for-symbols nil)

  ;; --- Configure for 'symbol' script ---
  (set-fontset-font t 'symbol "DejaVu Sans Mono" nil 'prepend)
  (set-fontset-font t 'symbol "JetBrainsMono Nerd Font Mono" nil 'prepend)

  ;; --- Configure for 'emoji' script ---
  (set-fontset-font t 'emoji "DejaVuSans" nil 'prepend)
  (set-fontset-font t 'emoji "JetBrainsMono Nerd Font Mono" nil 'prepend))

;; Add the fonts after setup is complete:
(add-hook 'emacs-startup-hook
          (lambda ()
            (when (string-equal system-type "gnu/linux")
              (my/setup-custom-font-fallbacks-linux))))
```

* Then run `doom sync`

* In a terminal, log into your Claude account:

```
claude
```

* Then press `enter` and select the lower option (Claude Console).

* Log into Claude in your browser. Copy and paste the key into your terminal.

