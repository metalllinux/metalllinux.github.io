---
title: "Ansible Roles Overview"
category: "automation-and-configuration"
tags: ["automation-and-configuration", "ansible", "roles", "overview"]
---

# Ansible Roles Overview

An **Ansible Role** is a structured way to organise Ansible playbooks and related files. It allows you to **reuse**, **share**, and **maintain** automation code more efficiently.

### ✅ Working Definition

An **Ansible Role** is a self-contained unit of configuration or automation. It includes everything needed to configure or manage a system component, such as installing a package, configuring a service, or deploying an application.

### 📁 Standard Role Directory Structure

```bash
my_role/
├── defaults/
│   └── main.yml          # Default variables
├── files/
│   └── ...               # Static files to copy
├── handlers/
│   └── main.yml          # Handlers (e.g., restart service)
├── meta/
│   └── main.yml          # Role metadata (dependencies, etc.)
├── tasks/
│   └── main.yml          # Main list of tasks
├── templates/
│   └── ...               # Jinja2 templates
├── vars/
│   └── main.yml          # Other variables
```

### 🛠 How to Use a Role in a Playbook

```yaml
- hosts: webservers
  roles:
    - my_role
```

### 📦 Creating a Role

Use the Ansible command:

```bash
ansible-galaxy init my_role
```

This creates the full directory structure for you.
