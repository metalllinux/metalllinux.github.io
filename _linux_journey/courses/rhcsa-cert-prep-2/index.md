---
title: "RHCSA Cert Prep 2"
layout: archive
permalink: /linux-journey/courses/rhcsa-cert-prep-2/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

RHCSA EX200 -- file access, storage, and security.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/rhcsa-cert-prep-2/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
