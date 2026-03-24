---
title: "How Install Epson Ew 052A Drivers On Arch"
category: "general-linux"
tags: ["install", "epson", "052a", "drivers", "arch"]
---

Extract the RPM file.
Copy from `epson-inkjet-printer-escpt` into `/opt`
`sudo chown root:root -R /opt/epson-inkjet-printer-escpr/`
Install the printer via CUPS. You can access it via `http://localhost:631/` Use the PID driver within the `/opt/epson-inkjet-printer-escpr/` directory