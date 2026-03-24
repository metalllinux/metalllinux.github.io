---
title: "Digitalocean Wordpress One Click Install Info"
category: "general-linux"
tags: ["digitalocean", "wordpress", "one", "click", "install"]
---

```
*** System restart required ***
********************************************************************************

Welcome to DigitalOcean's One-Click WordPress Droplet.
To keep this Droplet secure, the UFW firewall is enabled.
All ports are BLOCKED except 22 (SSH), 80 (HTTP), and 443 (HTTPS).

In a web browser, you can view:
 * The WordPress One-Click Quickstart guide: https://do.co/34TfYn8#start
 * The new WordPress site: http://170.64.239.180

On the server:
 * The default web root is located at /var/www/html
 * If you're using the embedded database, the MySQL root password
   and MySQL wordpress user password are saved in /root/.digitalocean_password
   If you've opted in to using a DBaaS instance with DigitalOcean, you will
   find your credentials written to /root/.digitalocean_dbaas_credentials and
   you will have access to a DATABASE_URL environment variable holding your
   database connection string.
 * The must-use WordPress security plugin, fail2ban, is located at
   /var/www/html/wp-content/mu-plugins/fail2ban.php
 * Certbot is preinstalled. Run it to configure HTTPS. See
   https://do.co/34TfYn8#enable-https for more detail.
 * For security, xmlrpc calls are blocked by default.  This block can be
    disabled by running "a2disconf block-xmlrpc" in the terminal.

IMPORTANT:
   After connecting to the Droplet for the first time,
   immediately add the WordPress administrator at http://170.64.239.180.

For help and more information, visit https://do.co/34TfYn8

********************************************************************************
To delete this message of the day: rm -rf /etc/update-motd.d/99-one-click
This script will copy the WordPress installation into
Your web root and move the existing one to /var/www/html.old
--------------------------------------------------
This setup requires a domain name.  If you do not have one yet, you may
cancel this setup, press Ctrl+C.  This script will run again on your next login
--------------------------------------------------
Enter the domain name for your new WordPress site.
(ex. example.org or test.example.org) do not include www or http/s
--------------------------------------------------

```