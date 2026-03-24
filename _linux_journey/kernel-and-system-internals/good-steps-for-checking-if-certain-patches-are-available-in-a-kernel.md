---
title: "Good Steps to Check if Certain Patches are Available in a Particular Kernel"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "good", "steps", "checking", "certain"]
---

# Good Steps to Check if Certain Patches are Available in a Particular Kernel

I have been further looking into this issue today and please see my findings below:
 
Patch checks of the latest Rocky Linux 8.10 RT kernel currently available
 

    I checked under https://dl.rockylinux.org/pub/rocky/8.10/Devel/source/tree/Packages/k/ and observed the latest available kernel is kernel-rt-4.18.0-553.47.1.rt7.388.el8_10.src.rpm, updated on 03-Apr-2025

 

    I set up a fresh Rocky Linux 8.10 instance, with all packages fully updated.

 

    I downloaded the latest RT kernel:

wget https://dl.rockylinux.org/pub/rocky/8.10/Devel/source/tree/Packages/k/kernel-rt-4.18.0-553.47.1.rt7.388.el8_10.src.rpm

 

    Extracted the contents of the source RPM:

rpm -ivh ./kernel-rt-4.18.0-553.47.1.rt7.388.el8_10.src.rpm

 

    Changed into the SPECS directory:

cd rpmbuild/SPECS/

 

    Installed the required packages for rpmbuild:

dnf groupinstall -y "Development Tools"

dnf install -y python3-devel

 

    Executed the %prep stage of the spec file and unpacked the required sources:

rpmbuild --nodeps -bp ./kernel.spec

 

    Changed into the BUILD directory:

cd ../BUILD/kernel-rt-4.18.0-553.47.1.rt7.388.el8_10/linux-4.18.0-553.47.1.rt7.388.el8.x86_64

 

    Cross-referenced with the patch fix that you kindly referred to via this commit and under drivers/base/core.c, I observe no referenced to the following code:

+    /* Synchronise with module_remove_driver() */
+    rcu_read_lock();
+    driver = READ_ONCE(dev->driver);
+    if (driver)
+        add_uevent_var(env, "DRIVER=%s", driver->name);
+    rcu_read_unlock();

 

    Similarly under drivers/base/module.c, there is no reference to the this code either:

+    /* Synchronise with dev_uevent() */
+    synchronize_rcu();
+

 

    Thus at this time, the patch is not available for the RT kernel.

 
Patch checks for the latest Rocky Linux 8.10 non-RT kernel currently available
 

    Similarly I checked under https://dl.rockylinux.org/pub/rocky/8.10/BaseOS/source/tree/Packages/k/ and the latest available kernel is kernel-4.18.0-553.47.1.el8_10.src.rpm, which was updated on 03-Apr-2025 20:11.

 

    As I described above, I followed the same steps for checking the non-RT kernel.

 

    Checked drivers/base/core.c and again I do not see the following code included:

+    /* Synchronise with module_remove_driver() */
+    rcu_read_lock();
+    driver = READ_ONCE(dev->driver);
+    if (driver)
+        add_uevent_var(env, "DRIVER=%s", driver->name);
+    rcu_read_unlock();

 

    I also checked drivers/base/module.c and also do not see the code listed there:

+    /* Synchronise with dev_uevent() */
+    synchronize_rcu();
+

 

    Of note, there is another patch available in the non-RT and RT kernels, that helps with the DPDK binding process:

diff --git a/drivers/base/core.c b/drivers/base/core.c
index 2e776fcc31b695..2b4c0624b7043a 100644
--- a/drivers/base/core.c
+++ b/drivers/base/core.c
@@ -2739,8 +2739,11 @@ static ssize_t uevent_show(struct device *dev, struct device_attribute *attr,
     if (!env)
         return -ENOMEM;

+    /* Synchronise with really_probe() */
+    device_lock(dev);
     /* let the kset specific function add its keys */
     retval = kset->uevent_ops->uevent(&dev->kobj, env);
+    device_unlock(dev);
     if (retval)
         goto out;

 

    This one is already available in the non-RT kernel:

cat ./drivers/base/core.c | grep -A6 "Synchronise with really_probe"
        /* Synchronise with really_probe() */
        device_lock(dev);
        /* let the kset specific function add its keys */
        retval = kset->uevent_ops->uevent(kset, &dev->kobj, env);
        device_unlock(dev);
        if (retval)
                goto out;

 

    Same with the RT kernel:

linux-4.18.0-553.47.1.rt7.388.el8.x86_64]# cat ./drivers/base/core.c | grep -A6 "Synchronise with really_probe"
        /* Synchronise with really_probe() */
        device_lock(dev);
        /* let the kset specific function add its keys */
        retval = kset->uevent_ops->uevent(kset, &dev->kobj, env);
        device_unlock(dev);
        if (retval)
                goto out;

