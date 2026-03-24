---
title: "Automation & Configuration"
layout: archive
permalink: /linux-journey/automation-and-configuration/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Notes on Ansible, cron, systemd, Terraform, and configuration management.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'automation-and-configuration/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
