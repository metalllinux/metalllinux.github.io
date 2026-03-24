---
title: "Rocky Linux"
layout: archive
permalink: /linux-journey/rocky-linux/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Notes on Rocky Linux, CentOS, RHEL, DNF, RPM, and related distributions.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'rocky-linux/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
