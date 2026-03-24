---
title: "How to Install the Latest Version of Emacs on Rocky Linux 9"
category: "rocky-linux"
tags: ["rocky-linux", "install", "latest", "version", "emacs"]
---

# How to Install the Latest Version of Emacs on Rocky Linux 9

```
sudo dnf groupinstall -y "Development Tools"
```

```
sudo dnf install autoconf automake texinfo \
    gtk3-devel libX11-devel libXpm-devel libjpeg-devel \
    giflib-devel libpng-devel libtiff-devel pango-devel \
    harfbuzz-devel ncurses-devel gnutls-devel
```

```
wget https://ftp.gnu.org/gnu/emacs/emacs-30.1.tar.xz
```

```
tar -xvf emacs-30.1.tar.xz 
```

```
cd emacs-30.1
```

```
./configure --with-x-toolkit=gtk3
```

```
make -j$(nproc)
sudo make install
```

```
/usr/local/bin/emacs --version
```

# If using Doom Emacs
```
doom sync
```
