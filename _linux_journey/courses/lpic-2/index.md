---
title: "LPIC-2 Certification"
layout: archive
permalink: /linux-journey/courses/lpic-2/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

LPIC-2 Linux Engineer (201-450) certification prep.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/lpic-2/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
