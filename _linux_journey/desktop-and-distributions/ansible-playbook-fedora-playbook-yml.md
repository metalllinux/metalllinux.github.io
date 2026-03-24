---
title: "Ansible Playbook Fedora Playbook.Yml"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "ansible", "playbook", "fedora", "playbookyml"]
---

```
---
- host: all
  become: true
  tasks:
    - name: Update all packages
      dnf:
	name: "*"
	state: latest

    - name: Install openssh-server
      dnf:
        name: openssh-server
	state: latest

    - name: Enable openssh-server service
      ansible.builtin.systemd_service:
	name: sshd
	enabled: true

    - name: Start openssh-server service
      ansible.builtin.systemd_service:
        name: sshd
	state: started

    - name: Install emacs
      dnf:
	name: emacs
	state: latest

    - name: Install flathub packages for the current user
      community.general.flatpak
	name:
	  - com.bitwarden.desktop
	  - org.gimp.GIMP
	  - fr.handbrake.ghb
	  - net.cozic.joplin_desktop
	  - org.libreoffice.LibreOffice
	  - com.makemkv.MakeMKV
	  - com.valvesoftware.Steam
	  - org.videolan.VLC
	state: present
	method: user

    - name: Install vim
      dnf:
        name: vim
	state: latest
```