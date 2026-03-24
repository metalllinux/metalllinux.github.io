---
title: "Learning Regular Expressions"
layout: archive
permalink: /linux-journey/courses/learning-regular-expressions/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Regex patterns and usage.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/learning-regular-expressions/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
