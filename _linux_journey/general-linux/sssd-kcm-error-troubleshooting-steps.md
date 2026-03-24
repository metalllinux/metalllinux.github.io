---
title: "sssd_kcm Error Troubleshooting Steps"
category: "general-linux"
tags: ["sssd", "kcm", "error", "troubleshooting", "steps"]
---

# sssd_kcm Error Troubleshooting Steps

If you see the following errors:
```
May 22 15:00:44 hostname systemd[1]: Started SSSD Kerberos Cache Manager.
May 22 15:00:44 hostname sssd_kcm[27666]: Starting up
May 22 15:00:44 hostname sssd_kcm[27666]: ltdb: tdb(/var/lib/sss/secrets/secrets.ldb): tdb_transaction_setup_recovery: transaction data over new region boundary
May 22 15:00:44 hostname sssd_kcm[27666]: ltdb: tdb(/var/lib/sss/secrets/secrets.ldb): tdb_transaction_prepare_commit: failed to setup recovery data
May 22 15:00:44 hostname sssd_kcm[27666]: Failure during prepare_write): Corrupt database -> Operations error
May 22 15:00:44 hostname sssd_kcm[27666]: ltdb: tdb(/var/lib/sss/secrets/secrets.ldb): tdb_transaction_cancel: no transaction
May 22 15:00:51 hostname sssd_kcm[27666]: ltdb: tdb(/var/lib/sss/secrets/secrets.ldb): tdb_transaction_setup_recovery: transaction data over new region boundary
May 22 15:00:51 hostname sssd_kcm[27666]: ltdb: tdb(/var/lib/sss/secrets/secrets.ldb): tdb_transaction_prepare_commit: failed to setup recovery data
```

* Run through these steps:

* Stop the `sssd` service:
```
 systemctl stop sssd
```

* Stop the `sssd-kcm` service:
```
systemctl stop sssd-kcm.service
```

* Create a backup of the `secrets` directory:
```
cp -av /var/lib/sss/secrets /var/lib/sss/secrets-directory-backup
```

* Remove the `secrets.ldb` and `.secrets.mkey` files:
```
rm /var/lib/sss/secrets/secrets.ldb /var/lib/sss/secrets/.secrets.mkey
```

* Run `kinit` with your admin credentials, for example:
```
kinit administrator@example.com
```

* Remove the `mc` and `db` directories:
```
rm -fr /var/lib/sss/{mc,db}/
```

* Start `sssd`:
```
systemctl start sssd
```

* Since `SELinux` is set to `enforcing` mode, this can also cause issues with `sssd` if not configured correctly. For testing, either temporarily disable `SELinux` with:
```
setenforce 0
```
Or permanently disable SELinux with:
```
sed -i 's/SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config
```

* For further troubleshooting, under your `/etc/sssd/sssd.conf` file, I would add the following under `[domain/YOUR_DOMAIN_HERE]`:
```
debug_level = 9
```
* Then restart the `sssd` service:
```
systemctl restart sssd
```

