---
title: "Advanced Linux Kernel"
layout: archive
permalink: /linux-journey/courses/advanced-linux-kernel/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Deep dive into the Linux kernel.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/advanced-linux-kernel/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
