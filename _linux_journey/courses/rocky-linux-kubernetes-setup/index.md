---
title: "Rocky Linux K8s Setup"
layout: archive
permalink: /linux-journey/courses/rocky-linux-kubernetes-setup/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Building a Kubernetes cluster on Rocky Linux.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/rocky-linux-kubernetes-setup/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
