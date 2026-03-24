---
title: "How To Have Wkhtmltopdf Working"
category: "general-linux"
tags: ["wkhtmltopdf", "working"]
---

The easiest way was to download the AlmaLinux release and then rename it to EL9: https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox-0.12.6.1-3.almalinux9.x86_64.rpm
So it looks like this: `wkhtmltox-0.12.6.1-3.el9.x86_64.rpm`
Then do `sudo dnf localinstall ./wkhtmltox-0.12.6.1-3.el9.x86_64.rpm` and then I created a test PDF with `wkhtmltopdf https://apptainer.org/docs/user/latest/ test.pdf`