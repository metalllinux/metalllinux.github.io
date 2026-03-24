---
title: "Setting Up And Mounting Nfs Shares For Server To C"
category: "networking"
tags: ["networking", "setting", "mounting", "nfs", "shares"]
---

sudo mount -t nfs -vvvv 10.110.1.48:/mnt/mustakrakish/mustakrakish_nfs_share /mnt/mustakrakish_nfs_share/

Contents of  `/etc/exports` on the server side:

/mnt/mustakrakish/mustakrakish_nfs_share *(rw,sync,no_root_squash,insecure) 

Refreshed the above config with

`sudo exportfs -rav`

Make sure all of these services have been started as well:

sudo systemctl enable rpcbind                                                                                                              sudo systemctl enable nfs-server                                                                                                           sudo systemctl enable nfs-lock                                                                                                               sudo systemctl enable nfs-idmap                                                                                                            sudo systemctl start rpcbind                                                                                                                    sudo systemctl start nfs-server                                                                                                                sudo systemctl start nfs-lock  

How I set up the directory on the server side:

sudo mkdir /mnt/mustakrakish/mustakrakish_nfs_share                                                                        
sudo chown howard:howard /mnt/mustakrakish/mustakrakish_nfs_share/                                          
chmod 777 /mnt/mustakrakish/mustakrakish_nfs_share/ 

Finally, if you want to copy anything into the directory on the client side and the user is not root, use `chown` to set the permissions.