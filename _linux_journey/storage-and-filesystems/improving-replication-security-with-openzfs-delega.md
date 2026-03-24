---
title: "Improving Replication Security With OpenZFS Delegation"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "improving", "replication", "security", "openzfs"]
---

[Skip to content](#content)

https://klarasystems.com/articles/improving-replication-security-with-openzfs-delegation/
# Improving Replication Security With OpenZFS Delegation

April 13, 2022

OpenZFS privilege delegation is an extremely powerful tool that enables system administrators to carefully provide unprivileged users the ability to manage ZFS datasets and zvols at an extremely precise level —with much finer control than would be possible with generic security tools like sudo or doas.

Enter your email address to subscribe to Klara's newsletter.

I agree to receive your newsletters and accept the data [privacy statement](https://klaradev.wpenginepowered.com/privacy-policy/). You may unsubscribe at any time using the link in our newsletter.

![](https://klarasystems.com/wp-content/uploads/2022/04/AdobeStock_496616426-scaled.jpeg)

Did you know?

Improve the way you make use of ZFS in your company.

Did you know you can rely on Klara engineers for anything from a ZFS performance audit to developing new ZFS features to ultimately deploying an entire storage system on ZFS?

[ZFS Support](https://klarasystems.com/openzfs-support/) [ZFS Development](https://klarasystems.com/openzfs-development/)

##### Additional Articles

Here are more interesting articles on ZFS that you may find useful:

- [Winter 2024 Roundup: Storage and Network Diagnostics](https://klarasystems.com/articles/winter_2024_roundup_storage_and_network_diagnostics/)
- [ZFS Storage Fault Management on Linux](https://klarasystems.com/articles/zfs-storage-fault-management-linux/)
- [Fall 2024 Top Reads for Open Source Enthusiasts](https://klarasystems.com/articles/fall-2024-reads-open-source/)
- [Deploying pNFS file sharing with FreeBSD](https://klarasystems.com/articles/deploying-pnfs-file-sharing-with-freebsd/)
- [Applying the ARC Algorithm to the ARC](https://klarasystems.com/articles/applying-the-arc-algorithm-to-the-arc/)

[View More Articles](https://klarasystems.com/articles/)

Delegation is an OpenZFS feature which allows the system administrator to grant the permission to perform various ZFS operations to unprivileged (read: non-root) users. This sounds more complicated than it really is—in a nutshell, we’re talking about filesystem-like permissions, but applied at the underlying ZFS level.

There are as many use cases for OpenZFS delegation as there are for the direct filesystem permissions we’re all familiar with—for example, you could allow a user to snapshot their own home directory, but not the home directories of other users.

But rather than indulge in an academic treatise on every possible use of delegation, we’re going to focus on one in particular: unprivileged ZFS replication between machines.

* * *

## **A Quick Primer on OpenZFS Replication**

OpenZFS replication is based upon snapshots, which can be bundled up and sent as binary blobs—or binary diffs—to other OpenZFS pools and/or systems.

At the most basic level, a full replication looks like this (assuming that SSH keys have already been shared between each machine):

```
root@sendbox:~# zfs send poolname/datasetname@snapshot1 | ssh root@recvbox zfs receive poolname/datasetname
```

This is a full replication, which must copy each block contained within snapshot1 to recvbox. Crucially, a full replication must have an empty target—poolname/datasetname must not already exist on recvbox! Once we’ve completed this first full replication, we can follow it up with an incremental replication:

```
root@sendbox:~# zfs send -I poolname/datasetname@snapshot1 poolname/datasetname@snapshot2 | ssh root@recvbox zfs receive poolname/datasetname
```

This incremental replication will proceed much faster, since it must only send the changes made to poolname/datasetname in between the first and second snapshots. After we complete both the initial full and follow-up incremental replication, we can see both datasetname and its two snapshots on recvbox:

```
root@recvbox:~# zfs list –rt all poolname/datasetname
NAME                            USED   AVAIL     REFER  MOUNTPOINT
poolname/datasetname            114G   5.80T     57.5G  -
poolname/datasetname@snapshot1  8.45G      -     45.0G  -
poolname/datasetname@snapshot2  6.52G      -     44.9G  -
```

OpenZFS replication is massively faster than filesystem-agnostic tools like rsync—in many cases, it can be literally *thousands* of times faster. But by default, replication requires root privileges on both ends of the transaction—which makes it much easier for a potential attacker to pivot from the machine initiating the replication to its partner.

## **First delegation: allowing the sending user to take snapshots**

Now that we understand why we’d want to replicate without giving up root privilege, let’s see how to do it. We’ll start out on the box which is sending the replicated dataset, which we’ve cleverly named “sendbox.”

By default, a completely unprivileged user on sendbox can list snapshots, but not create them:

```
senduser@sendbox:~$ zfs list
NAME       USED  AVAIL     REFER  MOUNTPOINT
data       150K  18.9G       24K  /data
data/ds1    24K  18.9G       24K  /data/ds1
data/ds2    24K  18.9G       24K  /data/ds2

senduser@sendbox:~$ zfs snapshot data/ds1@1
cannot create snapshots : permission denied
```

So our first step will be to allow *senduser*—the unprivileged account we’ll use on the replication source, sendbox—to take snapshots, using OpenZFS delegation:

```
root@sendbox:~# zfs allow senduser snapshot data/ds1
```

In the above delegation command, we (as root) grant the *senduser* account permissions to create snapshots—but we’ve only granted that permission to a specific dataset (and its children, if any).

**Let’s test the newly granted permission:**

```
senduser@sendbox:~$ zfs list
NAME       USED  AVAIL     REFER  MOUNTPOINT
data       150K  18.9G       24K  /data
data/ds1    24K  18.9G       24K  /data/ds1
data/ds2    24K  18.9G       24K  /data/ds2

senduser@sendbox:~$ zfs snapshot data/ds1@1

senduser@sendbox:~$ zfs snapshot data/ds2@1
cannot create snapshots : permission denied
```

This works exactly as intended: our unprivileged user can now create snapshots, but only on the particular dataset (or zvol) we’ve granted it access to, along with any of its children.

There are additional arguments to zfs allow which make the permissions granted *only* apply to the specified dataset, or *only* to the specified dataset’s children—but for right now, we’re just going to keep things simple.

## **Next Steps: Granting send and receive permissions appropriately**

Now that we’ve seen the basics of how delegation works, let’s get serious about putting together all the privileges we need for OpenZFS replication on both sides.

Obviously, *senduser* will need the send permission, and *recvuser* will need the receive permission. So let’s grant those. Notice that in these examples, the two users are also on entirely separate machines:

```
root@sendbox:~# zfs allow senduser send data/ds1

root@recvbox:~# zfs allow recvuser receive data
```

Notice that we granted *receive* permissions to the entire *data* pool on recvbox, although we only granted send permissions to *data/ds1.* That’s because, as discussed earlier, our *first* full replication must actually create *data/ds1* in its entirety!

Although you might think *send* on one end and *receive* on the other would be enough, full replication will require two more privileges on the receiving side: *create* and *mount*. If you forget to grant these additional privileges, you’ll get a “cannot receive new filesystem stream: permission denied” error on recvbox. Let’s go ahead and grant these now:

```
root@recvbox:~# zfs allow recvuser create data
root@recvbox:~# zfs allow recvuser mount data
```

## **A First Attempt at Unprivileged Replication**

With *snapshot* and *send* granted to the sending user and *receive*, *create*, and *mount* granted to the receiving user, we can successfully replicate... although we’ll still receive an error:

```
senduser@sendbox:~$ zfs send data/ds1@1 | pv | ssh recvuser@recvbox zfs receive data/ds1
45.1KiB 0:00:00 [2.09MiB/s] [ <=>                                 ]
cannot mount '/data/ds1': failed to create mountpoint
```

```
senduser@sendbox:~$ ssh recvuser@recvbox zfs list –rt all data
NAME         USED  AVAIL     REFER  MOUNTPOINT
data         140K  18.9G       24K  /data
data/ds1      24K  18.9G       24K  /data/ds1
data/ds1@1     0B      -       24K  -
```

There are a couple of things to notice here: the first is a new command we stuck into our replication pipeline, *pv*. The pv tool doesn’t actually affect replication itself, but it does provide a convenient progress bar that lets you know how much data you’ve transferred, and how quickly. We strongly recommend its use in real-world replication tasks, which could potentially take hours!

The second thing to notice is that although we received an error, it didn’t affect our actual replication task, which succeeded quite nicely. The “failed to create mountpoint” error we’re seeing isn’t from OpenZFS, it’s from the underlying unix filesystem—although *recvuser* has the ZFS privileges to set a mountpoint, it does not have the underlying system privilege to make Unix filesystem mounting succeed.

One way to deal with this error is simply to ignore it: it only comes up on the initial replication, and it doesn’t do any harm. Future incremental replication tasks won’t need to create new mountpoints for the same dataset, so they shouldn’t typically generate the same error.

Another, possibly cleaner way of dealing with this error is to set *mountpoint=none* on or above your replication target. This results, as you might expect, in a received dataset which is not mounted—but the replication itself still works swimmingly, you don’t get any errors, and you can of course manually mount the dataset yourself as root at any time you like afterward.

If you really, *really* need your unprivileged user to be able to mount newly replicated datasets, this is a task for the underlying system, not OpenZFS. On FreeBSD, you can set *vfs.usermount=1* in /etc/sysctl.conf, and on Linux systems you can accomplish the same goal by faffing about with polkit—but we cannot stress enough that many potential security dragons lie down this path.

We strongly recommend simply issuing *zfs set mountpoint=none* on the datasets in question to resolve this error!

Now that we understand the issues with filesystem mounting, let’s first destroy our earlier attempt at replication, and set *mountpoint=none* on the receiving end as described:

```
root@recvbox:~# zfs destroy –r data/ds1
root@recvbox:~# zfs set mountpoint=none data
```

Now we can replicate without *any* errors, either ZFS or system level:

```
senduser@sendbox:~$ zfs send data/ds1@1 | pv | ssh recvuser@recvbox zfs receive data/ds1
45.1KiB 0:00:00 [46.2KiB/s] [ <=>        ]

senduser@sendbox:~$ ssh recvuser@recvbox zfs list –rt all data
NAME         USED  AVAIL     REFER  MOUNTPOINT
data         140K  18.9G       24K  /data
data/ds1      24K  18.9G       24K  /data/ds1
data/ds1@1     0B      -       24K  -
```

Perfect.

## **Tighten Up - Limiting Permissions on the Receiver**

Now that *data/ds1* exists on *recvbox*, we can tighten up permissions on that side if we like, by first removing them from the *data* pool in its entirety, then re-granting them to *data/ds1* only:

```
root@recvbox:~# zfs unallow recvuser create,mount,receive data
root@recvbox:~# zfs allow recvuser create,mount,receive data/ds1
```

We can demonstrate that our newer permissions work only for data/ds1 and its children, by creating a new child dataset on *sendbox* and replicating it in:

```
root@sendbox:~# zfs create data/ds1/child1

senduser@sendbox:~$ zfs snapshot data/ds1/child1@1

senduser@sendbox:/root$ zfs send data/ds1/child1@1 | pv | ssh recvuser@recvbox zfs receive data/ds1/child1
45.1KiB 0:00:00 [65.5KiB/s] [ <=>                                   ]
```

And we can verify that our newly-tightened permissions will *not* allow recvuser to receive replication outside the boundaries it’s been given:

```
senduser@sendbox:/root$ zfs send data/ds1@1 | pv | ssh recvuser@recvbox zfs receive data/lol
45.1KiB 0:00:00 [61.3KiB/s] [ <=>                          ]
cannot receive new filesystem stream: permission denied
```

We can also verify that our *sending* user doesn’t have permissions to receive, as it should not:

```
senduser@sendbox:/root$ zfs send data/ds1@1 | pv | zfs receive data/ds1clone
cannot receive new filesystem stream: permission denied
44.2KiB 0:00:00 [2.20MiB/s] [ <=>
```

In the case of a “pull” backup—one in which the receiving (backup) side shells into the sending (production) side to initiate replication—this greatly mitigates the ability of an attacker which compromises your backup stack to immediately kill off your production stack.

Similarly, in the case of a “push” backup—in which production shells into backup, rather than vice versa—the attacker’s ability to destroy your backups is greatly limited, since it does not have the *destroy* permission.

We now have simple OpenZFS replication that works where it should—and equally important, doesn’t work where it should not. Now, let’s look at what’s necessary to get one of the more common replication *tools* functioning without the use of root!

## **Enabling Unprivileged, Automated Replication with Syncoid**

Although OpenZFS replication is extremely powerful and efficient, it’s not the easiest thing in the world to automate—you need to know which snapshots are present on both the sending and receiving systems ahead of time, craft the proper send command (which could be full or incremental), pipe it across an ssh tunnel, ideally perhaps add inline network buffering and compression, craft a zfs receive command on the other side, and so forth.

Although this might not *sound* all that difficult, in practice it’s a pretty tricky set of requirements—which is where tools like syncoid come in. Syncoid boils this entire mess down to a single rsync-like command, which figures out and handles all of the above (and more!) for you.

Unfortunately, this does require a few extra delegated permissions on the ZFS side, and a couple of extra arguments passed to syncoid. Rather than feed it all to you at once, let’s see how we might explore and troubleshoot the setup as an exercise. First of all, we’ll just try to run syncoid with no privileges:

```
recvuser@recvbox:~$ syncoid --no-privilege-elevation senduser@sendbox:data/ds1 data/ds1
cannot rollback 'data/ds1': permission denied
Sending incremental data/ds1@2 ... syncoid_recvbox_2022-03-23:19:45:36-GMT00:00 (~ 4 KB):
cannot hold: permission denied
cannot send 'data/ds1': permission denied
624 B 0:00:00 [24.4KiB/s] [==========>                                              ] 15%
cannot receive: failed to read from stream

CRITICAL ERROR: ssh     -S /tmp/syncoid-senduser@sendbox-1648064735 senduser@sendbox ' zfs send  -I '"'"'data/ds1'"'"'@'"'"'2'"'"' '"'"'data/ds1'"'"'@'"'"'syncoid_recvbox_2022-03-23:19:45:36-GMT00:00'"'"' | lzop  | mbuffer  -q -s 128k -m 16M 2>/dev/null' | mbuffer  -q -s 128k -m 16M 2>/dev/null | lzop -dfc | pv -p -t -e -r -b -s 4096 |  zfs receive  -s -F 'data/ds1' 2>&1 failed: 256 at /usr/local/bin/syncoid line 817.
```

We can see two important errors above: *cannot rollback data/ds1 : permission denied*, and *cannot hold: permission denied*. Unfortunately, we don’t immediately know which *side* these errors occurred on—but with a bit of thought exercise, we can assume that *senduser* would like to put a ZFS hold on the dataset it’s sending, and that *recvuser* wants to roll back the target to the most recent matching snapshot.

Let’s test our assumptions:

```
root@recvbox:~# zfs allow recvuser rollback data/ds1
root@sendbox:~# zfs allow senduser hold data/ds1

recvuser@recvbox:~$ syncoid --no-privilege-elevation senduser@sendbox:data/ds1 data/ds1
Sending incremental data/ds1@2 ... syncoid_recvbox_2022-03-23:19:49:40-GMT00:00 (~ 4 KB):
2.13KiB 0:00:00 [35.3KiB/s] [======================================>                                   ] 53%
cannot destroy snapshots: permission denied
WARNING: ssh     -S /tmp/syncoid-senduser@sendbox-1648064979 senduser@sendbox ' zfs destroy '"'"'data/ds1'"'"'@syncoid_recvbox_2022-03-23:19:45:36-GMT00:00' failed: 256 at /usr/local/bin/syncoid line 1380.
```

There we have it! This time, our replication itself went off without a hitch—but we’re still getting an error, because *syncoid* wants to both create special replication snapshots on the sending side, and *remove* them from both sides when they’re no longer necessary.

We could, of course, simply grant the *destroy* permission to both *recvuser* and *senduser*—but instead, let’s simply tell *syncoid* not to bother creating special replication snapshots in the first place:

```
recvuser@recvbox:~$ syncoid --no-privilege-elevation --no-sync-snap senduser@sendbox:data/ds1 data/ds1
NEWEST SNAPSHOT: syncoid_recvbox_2022-03-23:19:49:40-GMT00:00
INFO: no snapshots on source newer than syncoid_recvbox_2022-03-23:19:49:40-GMT00:00 on target. Nothing to do, not syncing.
```

Success! Note that although we got no errors, *syncoid* is warning us that it didn’t actually do anything, since sendbox didn’t have any snapshots newer than the newest one present on recvbox, and we told syncoid not to create (and then need to destroy) replication snapshots for itself.

In the real world, we would typically use an automated tool like sanoid to regularly create new snapshots on sendbox—and to prune stale snapshots on both sendbox and recvbox. For our purposes today, let’s just manually take a new snapshot so that we can then see syncoid successfully replicate it:

```
recvuser@recvbox:~$ ssh senduser@sendbox zfs snapshot data/ds1@3
recvuser@recvbox:~$ syncoid --no-privilege-elevation --no-sync-snap senduser@sendbox:data/ds1 data/ds1
NEWEST SNAPSHOT: 3
Sending incremental data/ds1@syncoid_recvbox_2022-03-23:19:49:40-GMT00:00 ... 3 (~ 4 KB):
1.52KiB 0:00:00 [26.4KiB/s] [===========================>                                   ] 38%
```

Perfect.

## **Conclusions**

OpenZFS privilege delegation is an extremely powerful tool that enables system administrators to carefully provide unprivileged users the ability to manage ZFS datasets and zvols at an extremely precise level—with much finer control than would be possible with generic security tools like *sudo* or *doas*.

In today’s article, we examined how to use delegation to greatly minimise the available attack surface for an attacker to pivot from a backup system to a production system, *or* vice versa. If you’re currently using root-level SSH access from one system to another to allow replication, we highly recommend tightening that up using the tools we’ve shown you today.

## **One more thing...**

The experts at Klara have been designing NAS solutions for over two decades and have in-the-trenches experience with using new technologies and planning for technology upgrades. Reach out to us if you would like to discuss the practicalities of creating your own NAS solution.

Topics / Tags

[delegation](https://klarasystems.com/articles/?tag=delegation) [Open Source](https://klarasystems.com/articles/?tag=open-source) [openzfs](https://klarasystems.com/articles/?tag=openzfs) [replication](https://klarasystems.com/articles/?tag=replication) [security](https://klarasystems.com/articles/?tag=security) [vdev](https://klarasystems.com/articles/?tag=vdev)

[Back to Articles](https://klarasystems.com/articles)

## More on This Topic

[![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)<br>Article<br>###### Winter 2024 Roundup: Storage and Network Diagnostics<br>Check out this season's investigation-themed collection of top diagnostics stories. From uncovering…<br>Read Now](https://klarasystems.com/articles/winter_2024_roundup_storage_and_network_diagnostics/)

[![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)<br>Article<br>###### ZFS Storage Fault Management on Linux<br>Hardware failures are unavoidable, but ZFS fault management ensures your data stays secure. From…<br>Read Now](https://klarasystems.com/articles/zfs-storage-fault-management-linux/)

[![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)<br>Article<br>###### Fall 2024 Top Reads for Open Source Enthusiasts<br>This season’s must-reads for open source enthusiasts include ZFS pool optimisation tips,…<br>Read Now](https://klarasystems.com/articles/fall-2024-reads-open-source/)

[![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)<br>Article<br>###### Deploying pNFS file sharing with FreeBSD<br>The venerable Network File System (NFS) has been expanded with distributed capabilities, pNFS v4.2…<br>Read Now](https://klarasystems.com/articles/deploying-pnfs-file-sharing-with-freebsd/)

[![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)<br>Article<br>###### Applying the ARC Algorithm to the ARC<br>ZFS uses the ARC (Adaptive Replacement Cache) to perform high efficiency responsive caching to…<br>Read Now](https://klarasystems.com/articles/applying-the-arc-algorithm-to-the-arc/)

[![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)<br>Article<br>###### Introducing OpenZFS Fast Dedup<br>OpenZFS new feature, inline deduplication, lets you store identical files or blocks without…<br>Read Now](https://klarasystems.com/articles/introducing-openzfs-fast-dedup/)

[![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)<br>Article<br>###### DKMS vs kmod: The Essential Guide for ZFS on Linux<br>ZFS integrates tightly with FreeBSD, enabling seamless updates, but licensing prevents its…<br>Read Now](https://klarasystems.com/articles/dkms-vs-kmod-the-essential-guide-for-zfs-on-linux/)

[![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)<br>Article<br>###### 5 Reasons Why Your ZFS Storage Benchmarks Are Wrong<br>ZFS benchmarking is challenging because it requires careful consideration of the many different…<br>Read Now](https://klarasystems.com/articles/5-reasons-why-your-zfs-storage-benchmarks-are-wrong/)

### Getting expert ZFS advice is as easy as reaching out to us!

At Klara, we have an entire team dedicated to helping you with your ZFS Projects. Whether you’re planning a ZFS project or are in the middle of one and need a bit of extra insight, we are here to help!

[ZFS Support](https://klarasystems.com/openzfs-support/) [ZFS Development](https://klarasystems.com/openzfs-development/)

[![Klara](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)](https://klarasystems.com/)

© 2024 Klara Inc. All Rights Reserved.

[Privacy Policy](https://klarasystems.com/privacy-policy/)

- [](https://twitter.com/klarainc?lang=en)
- [](https://ca.linkedin.com/company/klara-inc)
- [](https://www.facebook.com/klarainc/)
- [](https://klarasystems.com/feed/)

- [Embedded](https://klarasystems.com/embedded-systems/)
- [CPU & Arm Development](https://klarasystems.com/embedded-systems/cpu-and-arm-development/)
- [Board Support Packages](https://klarasystems.com/embedded-systems/board-support-packages/)
- [Performance Tuning](https://klarasystems.com/embedded-systems/performance-tuning/)
- [Product Development](https://klarasystems.com/embedded-systems/embedded-product-development-services/)

- [ZFS](https://klarasystems.com/zfs/)

- Development
- [Custom Feature Development](https://klarasystems.com/zfs/development/custom-feature-development/)
- Solutions
- [ZFS Storage Design](https://klarasystems.com/zfs/solutions/zfs-storage-design/)
- Support
- [ZFS Infrastructure Support](https://klarasystems.com/zfs/support/zfs-infrastructure-support/)

- [FreeBSD](https://klarasystems.com/freebsd/)
- Development
- [Kernel Development](https://klarasystems.com/freebsd/development/kernel-development/)
- Solutions
- [FreeBSD Bug Investigation](https://klarasystems.com/freebsd/solutions/freebsd-bug-investigation/)
- Support
- [FreeBSD Infrastructure Support](https://klarasystems.com/freebsd/support/freebsd-infrastructure-support/)

- Resources
- [Articles](https://klarasystems.com/articles/)
- [Webinars](https://klarasystems.com/webinars/)
- [Content](https://klarasystems.com/content/)
- [Emergency Help](https://klarasystems.com/emergency-help/)

- [About](https://klarasystems.com/company/about/)

- Company
- [About](https://klarasystems.com/company/about/)
- [Careers](https://klarasystems.com/company/careers/)
- [Contact Us](https://klarasystems.com/company/contact-us/)
- Community
- [Licensing](https://klarasystems.com/community/licensing/)
- [Open Source](https://klarasystems.com/community/open-source/)

<img width="22" height="24" src="../_resources/facebook_8a2ec5fde52a4e4aa0b8a128a15d416e.svg"/> Share

<img width="22" height="24" src="../_resources/twitter_d01dfc195fe9469b86e4c50eb2642abe.svg"/>Tweet

<img width="22" height="24" src="../_resources/sharethis_b0b0995ebdac46af9803ad7391cc87e4.svg"/>Share

<img width="22" height="24" src="../_resources/linkedin_286a64eaece04d38a4dafa9ed1c97d16.svg"/>Share

<img width="22" height="24" src="../_resources/reddit_7707ef865cbd44499be9f5a2d6e22f45.svg"/>Share

![arrow_left sharing button](../_resources/arrow_left_ceb4392a83274962b21cf6c3b3eb9307.svg)