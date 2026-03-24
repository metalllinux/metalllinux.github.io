---
title: "What Does The S Flag Do In Tcpdump"
category: "general-linux"
tags: ["flag", "tcpdump"]
---

       -s snaplen
       --snapshot-length=snaplen
              Snarf snaplen bytes of data from each packet rather than the default of 262144 bytes.  Packets truncated because of a limited snapshot are indicated in the output with ``[|proto]'', where proto is the name of the  pro‐
              tocol level at which the truncation has occurred.

              Note  that  taking  larger  snapshots both increases the amount of time it takes to process packets and, effectively, decreases the amount of packet buffering.  This may cause packets to be lost.  Note also that taking
              smaller snapshots will discard data from protocols above the transport layer, which loses information that may be important.  NFS and AFS requests and replies, for example, are very large, and much of the detail  won't
              be available if a too-short snapshot length is selected.

              If  you  need to reduce the snapshot size below the default, you should limit snaplen to the smallest number that will capture the protocol information you're interested in.  Setting snaplen to 0 sets it to the default
              of 262144, for backwards compatibility with recent older versions of tcpdump.
