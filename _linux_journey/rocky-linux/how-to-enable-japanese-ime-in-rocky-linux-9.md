---
title: "How to Enable a Japanese IME in Rocky Linux 9.6"
category: "rocky-linux"
tags: ["rocky-linux", "enable", "japanese", "ime", "rocky"]
---

# How to Enable a Japanese IME in Rocky Linux 9.6

Here’s a complete, working solution for enabling Japanese Input Method (IME) on **Rocky Linux 9.6**, which is compatible with RHEL 9:

---

## ✅ Step 1: Install Input Method Packages

First install the input method framework and Japanese engine:

```bash
sudo dnf install ibus ibus-anthy @input-methods
```

* `ibus` – the input framework
* `ibus-anthy` – Japanese IME using Anthy
* `@input-methods` – includes CJK IMEs ([docs.redhat.com][1], [en.wikipedia.org][2])

---

## 🛠 Step 2: Configure Environment

Add these lines to `~/.bashrc` (or `~/.bash_profile`, `~/.zshrc`):

```bash
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
```

Then reload the shell or log out/in:

```bash
source ~/.bashrc
```

This ensures graphical apps use IBus properly ([reddit.com][3], [reddit.com][4]).

---

## 🚀 Step 3: Start IBus

Launch the IBus daemon (auto-starts in GUI):

```bash
ibus-daemon -drx
```

* `-d` daemonise
* `-r` restart existing
* `-x` enable XIM support
  This sets up IME support according to the ArchWiki and Reddit guides ([reddit.com][4], [rockylinux.org][5]).

---

## 🌐 Step 4: Add Japanese Input in GNOME

If you're running GNOME (default in Rocky Linux GUI):

* Go to Settings --> Keyboard --> Japanese and select Anthy.
---

## ⌨️ Step 5: Switching Input Modes

* **Ctrl + Space** toggles between English and Japanese input once it's active ([askubuntu.com][9])
* You can customise shortcuts in **IBus Preferences**, accessible via the panel icon or running:

  ```bash
  ibus-setup
  ```

  From there, adjust global shortcuts (e.g., `Ctrl + J` to toggle).

---

## ✅ Quick Validation

1. Open a text editor (like Gedit or LibreOffice).
2. Press **Ctrl + Space** → the panel icon should show "A ち" or "あ".
3. Type using romaji (e.g. `konnichiwa`) — you’ll see hiragana/kanji candidates.

---

## 🔧 Alternative: ibus-mozc

If you'd prefer **Mozc** (Google’s Japanese IME), install it:

```bash
sudo dnf install ibus-mozc
```

Then add **Japanese (Mozc)** in Input Sources. Everything else remains the same ([issuetracker.google.com][8], [wiki.archlinux.org][10], [askubuntu.com][9], [en.wikipedia.org][11]).

---

## 🧩 Summary Table

| Step | Action                                       | Purpose                       |
| ---- | -------------------------------------------- | ----------------------------- |
| 1    | `dnf install ibus ibus-anthy @input-methods` | Install IME framework & Anthy |
| 2    | Add env variables to shell config            | Ensure GUI apps use IBus      |
| 3    | `ibus-daemon -drx`                           | Start IBus service            |
| 4    | GNOME Settings → Add Japanese (Anthy/Mozc)   | Enable IM in GUI              |
| 5    | Use **Ctrl + Space**                         | Switch input mode             |

---

With these steps, Japanese input will function fully in apps like GNOME Terminal, LibreOffice, VS Code, and more on Rocky Linux 9.6. Need help customising shortcuts, installing Mozc instead, or using KDE instead of GNOME? Let me know!

[1]: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/getting_started_with_the_gnome_desktop_environment/assembly_enabling-chinese-japanese-or-korean-text-input_getting-started-with-the-gnome-desktop-environment?utm_source=chatgpt.com "Chapter 7. Enabling Chinese, Japanese, or Korean text input"
[2]: https://en.wikipedia.org/wiki/Intelligent_Input_Bus?utm_source=chatgpt.com "Intelligent Input Bus"
[3]: https://www.reddit.com/r/linux/comments/byugan/how_to_install_japanese_input_in_linux_tutorial/?utm_source=chatgpt.com "How to install Japanese Input in Linux (tutorial) - Reddit"
[4]: https://www.reddit.com/r/LearnJapanese/comments/ik64mb/a_guide_for_installing_a_japanese_input_method_on/?utm_source=chatgpt.com "A guide for installing a Japanese Input Method on Linux - Reddit"
[5]: https://rockylinux.org/news/rocky-linux-9-6-ga-release?utm_source=chatgpt.com "Rocky Linux 9.6 Available Now"
[6]: https://forums.rockylinux.org/t/chinese-japanese-language-input-not-working/13436?utm_source=chatgpt.com "Chinese/Japanese language input not working? - Rocky Linux Forum"
[7]: https://gist.github.com/y56/c0fc4838a251fee072d94dcb871eab7a?utm_source=chatgpt.com "How to install Japanese Input in Linux (tutorial) - gist/GitHub"
[8]: https://issuetracker.google.com/issues/408309963?utm_source=chatgpt.com "Chrome 135 Linux: IMEs stopped working with X.org + ibus ..."
[9]: https://askubuntu.com/questions/184328/anthy-japanese-input-keyboard-shortcut?utm_source=chatgpt.com "Anthy (japanese input) keyboard shortcut - Ask Ubuntu"
[10]: https://wiki.archlinux.org/title/Input_Japanese_using_ibus?utm_source=chatgpt.com "Input Japanese using ibus - ArchWiki"
[11]: https://en.wikipedia.org/wiki/Anthy?utm_source=chatgpt.com "Anthy"

