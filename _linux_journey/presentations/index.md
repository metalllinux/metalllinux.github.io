---
title: "Presentations"
layout: archive
permalink: /linux-journey/presentations/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Talks and slide decks I've given at Linux / open-source meetups and conferences.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'presentations/'" | where_exp: "item", "item.path != 'presentations/index.md'" | sort: "event_date" | reverse %}
{% for page in pages %}
- [{{ page.title }}]({{ page.url }}){% if page.event %} — {{ page.event }}{% endif %}{% if page.event_date %} ({{ page.event_date }}){% endif %}
{% endfor %}
