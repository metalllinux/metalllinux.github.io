---
title: "Setting Up Certbot As Well As A Aaaa And Cname Rec"
category: "general-linux"
tags: ["setting", "certbot", "well", "aaaa", "cname"]
---

![Screenshot_20231116_004302.png](../_resources/Screenshot_20231116_004302.png)

* By using the above configuration via name cheap and then running `sudo certbot certonly --nginx -d metalinux.info -d www.metalinux.info
`, I received the following output:
`Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/metalinux.info/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/metalinux.info/privkey.pem
   Your cert will expire on 2024-02-13. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot
   again. To non-interactively renew *all* of your certificates, run
   "certbot renew"
`