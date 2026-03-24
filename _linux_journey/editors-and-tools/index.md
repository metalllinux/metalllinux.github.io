---
title: "Editors & Tools"
layout: archive
permalink: /linux-journey/editors-and-tools/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Notes on Emacs, Vim, tmux, Git, awk, sed, and command-line utilities.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'editors-and-tools/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
