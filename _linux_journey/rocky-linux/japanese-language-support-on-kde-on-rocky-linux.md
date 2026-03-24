---
title: "Japanese Language Support on KDE on Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "japanese", "language", "support", "kde"]
---

# Japanese Language Support on KDE on Rocky Linux

METHOD DOES NOT WORK, FCITX WILL NOT RUN ON WAYLAND! COMPILES and INSTALLS SUCCESSFULLY, BUT DOESN'T RUN. USE A VM WITH GNOME INSTEAD FOR ANY JAPANESE.

Sure! Here's a consolidated list of all the steps you need to run from the start to the finish:

### 1. Install Required Dependencies

```bash
sudo dnf install enchant-devel
sudo dnf install pango-devel
sudo dnf install gdk-pixbuf2-devel
sudo dnf install cmake
```

### 2. Clone the `fcitx5` repository and create the build directory:

```bash
cd ~
git clone --recursive https://github.com/fcitx/fcitx5.git
cd fcitx5
mkdir build
cd build
```

### 3. Configure the build with `cmake`:

```bash
cmake .. \
  -DISOCODES_ISO639_JSON=/usr/share/iso-codes/json/iso-639.json \
  -DISOCODES_ISO3166_JSON=/usr/share/iso-codes/json/iso-3166.json \
  -DXKEYBOARDCONFIG_XKBBASE=/usr/share/X11/xkb \
  -DXKEYBOARDCONFIG_DATADIR=/usr/share/X11/xkb
```

### 4. Build the project:

```bash
make
```

### 5. Install the built files:

```bash
sudo make install
```

echo "export XMODIFIERS=@im=fcitx" >> ~/.bashrc
echo "export GTK_IM_MODULE=fcitx" >> ~/.bashrc
echo "export QT_IM_MODULE=fcitx" >> ~/.bashrc
echo "export INPUT_METHOD=fcitx" >> ~/.bashrc
