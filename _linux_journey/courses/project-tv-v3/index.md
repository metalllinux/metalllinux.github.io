---
title: "Project TV v3 (Rocky)"
layout: archive
permalink: /linux-journey/courses/project-tv-v3/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Kubernetes-based media server on Rocky Linux 10, featuring EPGStation, Mirakurun, Jellyfin, Tube Archivist, and Navidrome.

Repository: [Metalllinux/project-tv-rocky-edition](https://github.com/metalllinux/project-tv-rocky-edition)

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/project-tv-v3/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
