---
title: "Alternatives Command To Create New Command"
category: "general-linux"
tags: ["alternatives", "command", "create", "new", "command"]
---

sudo alternatives --install <sym_link> <new_name> <path_to_original_binary> <priority>
sudo alternatives --install /usr/bin/em uemacs /opt/em-legacy/em2 1
alternatives --install /usr/bin/editor editor /usr/bin/vim 1