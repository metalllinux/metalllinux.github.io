---
title: "RHCSA Cert Prep 1"
layout: archive
permalink: /linux-journey/courses/rhcsa-cert-prep-1/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

RHCSA EX200 -- deployment, configuration, and management.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/rhcsa-cert-prep-1/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
