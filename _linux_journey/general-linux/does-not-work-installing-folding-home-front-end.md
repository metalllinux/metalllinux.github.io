---
title: "Does Not Work Installing Folding@Home Front End"
category: "general-linux"
tags: ["work", "installing", "foldinghome", "front", "end"]
---

```
sudo dnf install -y npm
git clone https://github.com/foldingathome/fah-web-client-bastet
cd fah-web-client-bastet
npm i
sudo firewall-cmd --permanent --add-port=5173/tcp
firewall-cmd --reload
npm run dev -- --host
```