---
title: "Project TV"
layout: archive
permalink: /linux-journey/courses/project-tv/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Media server infrastructure project.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/project-tv/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
