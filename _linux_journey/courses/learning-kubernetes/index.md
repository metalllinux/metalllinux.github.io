---
title: "Learning Kubernetes"
layout: archive
permalink: /linux-journey/courses/learning-kubernetes/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Kubernetes fundamentals and hands-on exercises.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/learning-kubernetes/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
