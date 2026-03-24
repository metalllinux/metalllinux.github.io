---
title: "Virtualisation"
layout: archive
permalink: /linux-journey/virtualisation/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Notes on KVM, QEMU, libvirt, VMware, and virtual machine management.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'virtualisation/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
