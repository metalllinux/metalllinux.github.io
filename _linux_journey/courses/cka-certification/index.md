---
title: "CKA Certification"
layout: archive
permalink: /linux-journey/courses/cka-certification/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Certified Kubernetes Administrator exam preparation notes.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/cka-certification/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
