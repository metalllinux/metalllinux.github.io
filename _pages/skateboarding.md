---
title: "Skateboarding"
layout: single
permalink: /skateboarding/
author_profile: true
header:
  overlay_image: /assets/images/metalinux-2.png
  overlay_filter: 0.5
---

Welcome to my Skateboarding section. Here I document skate parks, sessions, and everything skateboarding.

## Posts

{% for post in site.categories.skateboarding %}
- [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%B %-d, %Y" }}
{% endfor %}
