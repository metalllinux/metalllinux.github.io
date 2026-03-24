---
title: "Doom Emacs Setup On Rocky Linux 9"
category: "rocky-linux"
tags: ["rocky-linux", "doom", "emacs", "setup", "rocky"]
---

* Build emacs from source:

* Make sure all of these development packages are installed:

```
sudo dnf groupinstall -y "Development Tools"
sudo dnf install gtk3-devel
sudo dnf install -y giflib-devel
sudo dnf install -y gnutls-devel
sudo dnf install -y libjpeg-devel
sudo dnf install -y libXpm-devel
sudo dnf install -y ncurses-devel
```

* Download the tarball of the latest version of emacs:

```
https://ftp.gnu.org/pub/gnu/emacs/
```

* Untar the archive:

```
tar -axvf emacs-VERSION.tar.xz
```

* Change into the directory:

```
cd emacs-VERSION
```

* Build and install `emacs`:

```
./configure
make
sudo make install
```

* emacs will then be available under the following directory:

```
/usr/local/bin/emacs
```

```

* Install `git`:
```
sudo dnf install -y git
```
* Clone the git repo:
```
git clone --depth 1 https://github.com/doomemacs/doomemacs ~/.config/emacs
```
* Install Doom Emacs:
```
~/.config/emacs/bin/doom install
```
* Helper information at the end of the installation;
```
But before you doom yourself, here are some things you should know:

1. Don't forget to run 'doom sync' and restart Emacs after modifying init.el or
   packages.el in ~/.config/doom. This is never necessary for config.el.

2. If something goes wrong, run `doom doctor` to diagnose common issues with
   your environment, setup, and config.

3. Use 'doom upgrade' to update Doom. Doing it any other way will require
   additional steps (see 'doom help upgrade').

4. Access Doom's documentation from within Emacs via 'SPC h d h' or 'C-h d h'
   (or 'M-x doom/help').
```
* Add `.emacs.d/bin` to the existing `PATH`:
```
cat << "EOF" | tee -a ~/.bashrc
# Doom Emacs
export PATH="$HOME/.config/emacs/bin:$PATH"
EOF
```
* Then `source` `~/.bashrc`:
```
source ~/.bashrc
```
* Run `doom sync`
* Add an autostart script for the `Emacs server`:
```
/usr/bin/emacs --daemon
```
* In KDE's `Autostart`, place the `--daemon` part in the `Arguments` section, behind the `%F`.
* Launch Emacs with the following:
```
emacsclient -c -a 'emacs'
```
