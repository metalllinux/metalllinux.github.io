---
title: "Python Essential Training"
layout: archive
permalink: /linux-journey/courses/python-essential-training/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Python programming fundamentals.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/python-essential-training/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
