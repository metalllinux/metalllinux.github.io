---
title: "Ansible Playbooks"
layout: archive
permalink: /linux-journey/courses/ansible-playbooks/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Ansible automation examples.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'courses/ansible-playbooks/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
