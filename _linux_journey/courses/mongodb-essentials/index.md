---
title: "MongoDB Essentials"
layout: archive
permalink: /linux-journey/courses/mongodb-essentials/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

MongoDB training notes.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/mongodb-essentials/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
