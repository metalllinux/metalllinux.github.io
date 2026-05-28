---
title: "Posts"
layout: archive
permalink: /notes/posts/
sidebar:
  nav: "notes"
render_with_liquid: true
---

Notes and summaries from talks, articles, and other resources.

{% assign pages = site.notes | where_exp: "item", "item.path contains 'posts/'" | where_exp: "item", "item.path != 'posts/index.md'" | sort: "title" %}
{% for page in pages %}
- [{{ page.title }}]({{ page.url }})
{% endfor %}
