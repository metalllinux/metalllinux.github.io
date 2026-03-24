---
title: "Kernel & System Internals"
layout: archive
permalink: /linux-journey/kernel-and-system-internals/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Notes on the Linux kernel, crash analysis, kdump, performance tuning, and sysctl.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'kernel-and-system-internals/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
