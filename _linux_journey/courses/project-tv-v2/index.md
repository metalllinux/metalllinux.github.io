---
title: "Project TV v2 (Ubuntu)"
layout: archive
permalink: /linux-journey/courses/project-tv-v2/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Media server v2 on Ubuntu.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/project-tv-v2/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
