---
title: "Machines"
layout: archive
permalink: /linux-journey/courses/machines/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Machine configuration reference.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/machines/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
