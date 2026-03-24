---
title: "How Install Goverlay On Ubuntu 22.04 Or A Variant"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "install", "goverlay", "ubuntu", "variant"]
---

sudo apt install goverlay
* Requires install mangohud from source.
* Run:
```
git clone --recurse-submodules https://github.com/flightlessmango/MangoHud.git
cd MangoHud
sudo apt install meson
sudo apt install pip
pip3 install mako
sudo apt install cmake
sudo apt install pkg-config
sudo apt install libx11-dev
sudo apt install libwayland-dev
sudo apt install libdbus-1-dev
sudo apt install libxkbcommon-dev
sudo apt install glslang-dev
sudo apt install glslang-tools
sudo apt install libxnvctrl-dev
meson build
ninja -C build install
```
* Goverlay will then run afterwards.