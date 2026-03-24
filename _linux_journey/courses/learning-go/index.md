---
title: "Learning Go"
layout: archive
permalink: /linux-journey/courses/learning-go/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Go programming language notes.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/learning-go/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
