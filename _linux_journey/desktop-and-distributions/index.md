---
title: "Desktop & Distributions"
layout: archive
permalink: /linux-journey/desktop-and-distributions/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Notes on Arch, Debian, Ubuntu, Fedora, Flatpak, NVIDIA, and desktop environments.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'desktop-and-distributions/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
