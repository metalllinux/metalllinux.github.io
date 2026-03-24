---
title: "General Linux"
layout: archive
permalink: /linux-journey/general-linux/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Miscellaneous Linux notes, tips, tricks, and reference material.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'general-linux/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
