---
title: "SUSE Support on GFS2"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "suse", "support", "gfs2"]
---

# SUSE Support on GFS2

Applies to SUSE Linux Enterprise High Availability 15 SP6

## 22 GFS2 [#](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/cha-ha-gfs2.html# "Permalink")

Global File System 2 or GFS2 is a shared disk file system for Linux computer clusters. GFS2 allows all nodes to have direct concurrent access to the same shared block storage. GFS2 has no disconnected operating-mode, and no client or server roles. All nodes in a GFS2 cluster function as peers. GFS2 supports up to 32 cluster nodes. Using GFS2 in a cluster requires hardware to allow access to the shared storage, and a lock manager to control access to the storage.

SUSE recommends OCFS2 over GFS2 for your cluster environments if performance is one of your major requirements. Our tests have revealed that OCFS2 performs better as compared to GFS2 in such settings.

![Important](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/static/images/icon-important.svg "Important")

Important: GFS2 support

SUSE only supports GFS2 in read-only mode. Write operations are not supported.

## 22.1 GFS2 packages and management utilities [#](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/cha-ha-gfs2.html#sec-ha-gfs2-utils "Permalink")

To use GFS2, make sure gfs2-utils and a matching gfs2-kmp-\* package for your Kernel is installed on each node of the cluster.

The gfs2-utils package provides the following utilities for management of GFS2 volumes. For syntax information, see their man pages.

fsck.gfs2

Checks the file system for errors and optionally repairs errors.

gfs2\_jadd

Adds additional journals to a GFS2 file system.

gfs2\_grow

Grow a GFS2 file system.

mkfs.gfs2

Create a GFS2 file system on a device, usually a shared device or partition.

tunegfs2

Allows viewing and manipulating the GFS2 file system parameters such as `UUID`, `label`, `lockproto` and `locktable`.

## 22.2 Configuring GFS2 services and a STONITH resource [#](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/cha-ha-gfs2.html#sec-ha-gfs2-create-service "Permalink")

Before you can create GFS2 volumes, you must configure DLM and a STONITH resource.

Procedure 22.1: Configuring a STONITH resource [#](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/cha-ha-gfs2.html#pro-gfs2-stonith "Permalink")

![Note](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/static/images/icon-note.svg "Note")

Note: STONITH device needed

You need to configure a fencing device. Without a STONITH mechanism (like `external/sbd`) in place the configuration fails.

1.  Start a shell and log in as `root` or equivalent.
    
2.  Create an SBD partition as described in [Procedure 13.3, “Initialising the SBD devices”](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/cha-ha-storage-protect.html#pro-ha-storage-protect-sbd-create "Initialising the SBD devices").
    
3.  Run `crm configure`.
    
4.  Configure `external/sbd` as the fencing device:
    
    ```
    crm(live)configure# 
    ```
    
5.  Review your changes with `show`.
    
6.  If everything is correct, submit your changes with `commit` and leave the crm live configuration with `quit`.
    

For details on configuring the resource for DLM, see [Section 20.2, “Configuring DLM cluster resources”](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/cha-ha-storage-dlm.html#sec-ha-storage-generic-dlm-config "20.2. Configuring DLM cluster resources").

## 22.3 Creating GFS2 volumes [#](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/cha-ha-gfs2.html#sec-ha-gfs2-create "Permalink")

After you have configured DLM as cluster resources as described in [Section 22.2, “Configuring GFS2 services and a STONITH resource”](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/cha-ha-gfs2.html#sec-ha-gfs2-create-service "22.2. Configuring GFS2 services and a STONITH resource"), configure your system to use GFS2 and create GFS2 volumes.

![Note](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/static/images/icon-note.svg "Note")

Note: GFS2 volumes for application and data files

We recommend that you generally store application files and data files on different GFS2 volumes. If your application volumes and data volumes have different requirements for mounting, it is mandatory to store them on different volumes.

Before you begin, prepare the block devices you plan to use for your GFS2 volumes. Leave the devices as free space.

Then create and format the GFS2 volume with the `mkfs.gfs2` as described in [Procedure 22.2, “Creating and formatting a GFS2 volume”](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/cha-ha-gfs2.html#pro-gfs2-volume "Creating and formatting a GFS2 volume"). The most important parameters for the command are listed below. For more information and the command syntax, refer to the `mkfs.gfs2` man page.

Lock Protocol Name (`-p`)

The name of the locking protocol to use. Acceptable locking protocols are lock\_dlm (for shared storage) or, if you are using GFS2 as a local file system (1 node only), you can specify the lock\_nolock protocol. If this option is not specified, lock\_dlm protocol is assumed.

Lock Table Name (`-t`)

The lock table field appropriate to the lock module you are using. It is _clustername_:_fsname_. The _clustername_ value must match that in the cluster configuration file, `/etc/corosync/corosync.conf`. Only members of this cluster are permitted to use this file system. The _fsname_ value is a unique file system name used to distinguish this GFS2 file system from others created (1 to 16 characters).

Number of Journals (`-j`)

The number of journals for gfs2\_mkfs to create. You need at least one journal per machine that will mount the file system. If this option is not specified, one journal is created.

Procedure 22.2: Creating and formatting a GFS2 volume [#](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/cha-ha-gfs2.html#pro-gfs2-volume "Permalink")

Execute the following steps only on _one_ of the cluster nodes.

1.  Open a terminal window and log in as `root`.
    
2.  Check if the cluster is online with the command `crm status`.
    
3.  Create and format the volume using the `mkfs.gfs2` utility. For information about the syntax for this command, refer to the `mkfs.gfs2` man page.
    
    For example, to create a new GFS2 file system that supports up to 32 cluster nodes, use the following command:
    
    ```
    # 
    ```
    
    The `hacluster` name relates to the entry `cluster_name` in the file `/etc/corosync/corosync.conf` (this is the default).
    
    Always use a stable device name (for example: `/dev/disk/by-id/scsi-ST2000DM001-0123456_Wabcdefg`).
    

## 22.4 Mounting GFS2 volumes [#](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/cha-ha-gfs2.html#sec-ha-gfs2-mount "Permalink")

You can either mount a GFS2 volume manually or with the cluster manager, as described in [Procedure 22.4, “Mounting a GFS2 volume with the cluster manager”](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/cha-ha-gfs2.html#pro-gfs2-mount-cluster "Mounting a GFS2 volume with the cluster manager").

Procedure 22.3: Manually mounting a GFS2 volume [#](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/cha-ha-gfs2.html#pro-gfs2-mount-manual "Permalink")

1.  Open a terminal window and log in as `root`.
    
2.  Check if the cluster is online with the command `crm status`.
    
3.  Mount the volume from the command line, using the `mount` command.
    

![Warning](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/static/images/icon-warning.svg "Warning")

Warning: Manually mounted GFS2 devices

If you mount the GFS2 file system manually for testing purposes, make sure to unmount it again before starting to use it via cluster resources.

Procedure 22.4: Mounting a GFS2 volume with the cluster manager [#](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/cha-ha-gfs2.html#pro-gfs2-mount-cluster "Permalink")

To mount a GFS2 volume with the High Availability software, configure an OCF file system resource in the cluster. The following procedure uses the `crm` shell to configure the cluster resources. Alternatively, you can also use Hawk2 to configure the resources.

1.  Start a shell and log in as `root` or equivalent.
    
2.  Run `crm configure`.
    
3.  Configure Pacemaker to mount the GFS2 file system on every node in the cluster:
    
    ```
    crm(live)configure# 
    ```
    
4.  Add the `gfs2-1` primitive to the `g-storage` group you created in [Procedure 20.1, “Configuring a base group for DLM”](https://documentation.suse.com/es-es/sle-ha/15-SP6/html/SLE-HA-all/cha-ha-storage-dlm.html#pro-dlm-resources "Configuring a base group for DLM").
    
    ```
    crm(live)configure# 
    ```
    
    Because of the base group's internal colocation and ordering, the `gfs2-1` resource can only start on nodes that also have a `dlm` resource already running.
    
5.  Review your changes with `show`.
    
6.  If everything is correct, submit your changes with `commit` and leave the crm live configuration with `quit`.

