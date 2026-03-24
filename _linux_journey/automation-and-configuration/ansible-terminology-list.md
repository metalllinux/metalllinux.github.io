---
title: "Ansible Terminology List"
category: "automation-and-configuration"
tags: ["automation-and-configuration", "ansible", "terminology", "list"]
---


    Control Node: the machine where Ansible is installed, responsible for running the provisioning on the servers you are managing.
    Inventory: an INI file that contains information about the servers you are managing.
    Playbook: a YAML file containing a series of procedures that should be automated.
    Task: a block that defines a single procedure to be executed, e.g.: install a package.
    Module: a module typically abstracts a system task, like dealing with packages or creating and changing files. Ansible has a multitude of built-in modules, but you can also create custom ones.
    Role: a set of related playbooks, templates and other files, organised in a pre-defined way to facilitate reuse and share.
    Play: a provisioning executed from start to finish is called a play.
    Facts: global variables containing information about the system, like network interfaces or operating system.
    Handlers: used to trigger service status changes, like restarting or reloading a service.
