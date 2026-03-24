---
title: "Oracle Linux and Virtualization Hardware Certification Program"
category: "rocky-linux"
tags: ["rocky-linux", "oracle", "hardware", "certification", "program"]
---

# Oracle Linux and Virtualisation Hardware Certification Program

![Oracle Logo](https://www.oracle.com/technetwork/server-storage/linux/infra-software-systems-oracle-logo-5814753.png)

<table><tbody><tr><td><div><img src="https://linux.oracle.com/hcl-images/Abstracts-Open-Light-6.png"><div><p data-darkreader-inline-colour="">Oracle Linux and Virtualisation</p><p data-darkreader-inline-colour="">Hardware Certification Program</p></div></div></td></tr><tr><td></td></tr></tbody></table>

Frequently Asked Questions (FAQ)

#### Section 1: General

(show all | hide all, or click each question to show/hide answer)

1.  What is the purpose of the Oracle Linux and Virtualisation Server Hardware Certification Program?
    
    The Oracle Linux and Virtualisation Server Hardware Certification Program enables established hardware partners, which are generally Independent Hardware Vendors (IHVs) and resellers with membership in the Modern OPN licence & Hardware Track, to qualify their hardware for Oracle Linux and Virtualisation environments using Oracle supplied hardware test kit.
    
    The output of this program is the [Hardware Compatibility List](https://linux.oracle.com/hardware-certifications) (HCL). This list documents servers certified for Oracle Linux with Unbreakable Enterprise Kernel (UEK). While not listed separately on the HCL, servers certified for Oracle Linux are also certified for Oracle Linux KVM.
    
    Through this qualification, Oracle and its hardware partners can help ensure that both parties are equipped to provide collaborative support to customers running Oracle Linux and Virtualisation environments.
    
    Please see the [Hypervisor HCL FAQ](https://linux.oracle.com/hcl_hypervisor_faq.html) for information about certification of Oracle Linux guests in virtualised environments.
    
2.  Do I have to be a part of Oracle Partner Network (OPN) to certify my server for Oracle Linux and Oracle Linux KVM?
    
    An IHV participating in the Hardware Certification Program must be an established hardware partner having a collaborative support agreement with Oracle. The necessary requirements are achieved by joining Modern OPN's licence & Hardware Track. This includes joint marketing activities and participation in the Oracle Collaborative Vendor Support Program (OCVS). An IHV can also establish a collaborative support agreement with Oracle through [TSANet](https://www.tsanet.org/). If you would like to become an OPN member, please contact us at [hcl-info\_ww@oracle.com](mailto:hcl-info_ww@oracle.com?subject=I%20am%20interested%20in%20OPN%20membership).
    
    Resellers (and occasionally customers) that wish to participate in the Oracle Linux and Virtualisation Server Hardware Certification Program, but who are not members of OPN or TSANet, must be sponsored by an Oracle Linux Sales Representative.
    
3.  As a reseller or customer without OPN or TSANet membership, how does my participation in the program differ?
    
    Using the Oracle supplied server certification test kit, resellers and customers test the hardware on which they plan to run Oracle Linux with UEK environments in the same manner as the OPN hardware partners. However, there are two important distinctions:
    
    -   Program participation must be sponsored by your Oracle Linux Sales Representative, and
    -   The way support is delivered for Oracle Linux on that hardware stack will vary depending upon the involvement of the hardware vendor in the certification process.
        -   If a reseller or customer performs the certification test in cooperation with their hardware vendor, and the hardware vendor has an established partnership with Oracle and approves, the resulting certification will benefit from all of the program features including optimised joint support from Oracle and the IHV.
        -   If a reseller or customer performs the certification test without cooperation from their hardware vendor, or if the hardware vendor does not have an established partnership with Oracle, the certification will still be published in the [HCL](https://linux.oracle.com/hardware-certifications) and Oracle Linux will be fully supported on that hardware by Oracle. However, customers deploying Oracle Linux on this certified hardware will not have the benefit of a joint support relationship between Oracle and the hardware vendor, and the hardware vendor may not consider this a supported environment.
    
4.  Does Oracle provide the certification tools? What will I need?
    
    Oracle provides an Oracle Linux (which includes Oracle Linux KVM) test kit that is downloaded by the program participant and run on their server environment.
    
    Test hardware environment requirements may vary, but are minimal. Oracle will provide hardware requirements after you engage with the program team (contact information included below).
    
5.  What is the difference between a "Certified for Joint Support" HCL status and a "Certified for Oracle Support" HCL status?
    
    _Certified for Joint Support:_ Oracle Linux or Oracle VM was rigorously tested on the hardware or hypervisor (referred to as platform) with the participation and/or approval of the platform partner, and both Oracle and the partner fully support the environment. Customers deploying Oracle Linux or Oracle VM on this platform benefit from streamlined joint support. If a customer encounters any problem with Oracle Linux or Oracle VM that involves the underlying platform, the customer will open a service request with Oracle Support. Oracle Support will engage the partner if necessary, and seamlessly manage a joint resolution. For support on Oracle platforms, no third-party vendors are involved in the support process. These configurations are fully supported by Oracle.
    
    _Certified for Oracle Support:_ Oracle Linux or Oracle VM was rigorously tested with the same standards as Certified for Joint Support and Oracle fully supports Oracle Linux and Oracle VM on this platform, however a collaborative support program is not in place with the partner for this platform, and the partner may not consider this a supported environment. Oracle provides support for Oracle Linux and Oracle VM, but a resolution to issues related to underlying platform drivers or other platform-specific issues cannot be guaranteed.
    
6.  What is the version number convention for Oracle's Unbreakable Enterprise Kernel (UEK) for Oracle Linux?
    
    The version number convention can change with each major release of UEK. The conventions for the most recent UEK releases are explained here.
    
    Using the following UEK Release 7 (UEK R7) kernel version as an example,  
    5.15.0-0.30.19.el9uek:
    
    <table><tbody><tr><td>5.15.0</td><td>Indicates the upstream Linux kernel version, 5.15, on which UEK R7 is based upon, and where kABI compatibility is maintained. This string remains unchanged throughout the UEK R7 life cycle.</td></tr><tr><td>-0</td><td>The range 0-99 indicate this is initial release of UEK R7. A value in the range 100-199 indic<span data-darkreader-inline-bgcolor="">ates </span>Update 1, in the range 200-299 indicates Update 2, on so on. This value will increment with each monthly errata where, for instance, 105 indicates the fifth monthly errata release to Update 1, and 210 indicates the tenth monthly errata to Update 2.<br>Monthly errata are released between updates. Monthly errata include fixes, security errata, drivers updates, and synchronisation with the upstream Long Term Stable (LTS) branch content. Updates can include all of the above plus new features, new drivers, and general stability improvements.<br>Updates and errata always maintain kABI compatibility with earlier UEK R7 builds.</td></tr><tr><td>.30</td><td>Indicates the Long Term Stable (LTS) branch with which this build is synchronised. For example, upstream stable tree 5.15.<strong>30</strong> content is delivered in UEK 5.15.0-x.<strong>30</strong>.z.</td></tr><tr><td>.19</td><td>Indicates interim builds since the last monthly errata or update.</td></tr><tr><td>.el9uek</td><td>This UEK kernel is compiled for Oracle&nbsp;Linux 9.</td></tr></tbody></table>
    
    Using the following UEK Release 6 (UEK R6) kernel version as an example,  
    5.4.17-2036.100.6.el8euk:
    
    <table><tbody><tr><td>5.4.17</td><td>Indicates the upstream Linux kernel version, 5.4.17, on which UEK R6 is based upon, and where kABI compatibility is maintained. This string remains unchanged throughout the UEK R6 life cycle.</td></tr><tr><td>-2036.100</td><td>The range 100-199 indicates this is UEK R6, Update 1, the range 200-299 indicates Update 2, and so on. This value is incremented with each monthly errata release to the update (318 indicates the 18th monthly errata to Update 3. Updates include fixes, security errata, new and updated drivers, and stability improvements, and always maintains kABI compatibility with prior UEK R6 updates.</td></tr><tr><td>.1</td><td>Indicates interim builds or errata releases since its monthly errata release.</td></tr><tr><td>.el8uek</td><td>this UEK kernel is compiled for Oracle&nbsp;Linux 8.</td></tr></tbody></table>
    
7.  Are there any fees to participate in the Hardware Certification Program?
    
    Partner participation in the program is free, but requires membership in OPN or TSANet (see related questions above).
    
8.  Where will the qualified servers be published?
    
    Certified servers, hypervisors, and storage are published on the Oracle Linux and Virtualisation [Hardware Certification List](https://linux.oracle.com/hardware-certifications) (HCL), and on the corresponding IHV's website.
    
9.  What are the requirements for getting published on the Oracle HCL web site?
    
    Participants must meet the following criteria to be eligible to publish certified hardware platforms on the Oracle Linux and Virtualisation [HCL](https://linux.oracle.com/hardware-certifications) website.
    
    To receive a qualification status of _Certified for Joint Support_,
    
    -   The certification effort must be performed by, or with the approval of, the IHV, and
    -   IHV must have an established partnership with Oracle providing for joint support, and
    -   Test results must be audited by Oracle, and
    -   IHV must publish results in the support matrix on their website within two weeks of Oracle approving the results.
    
    To receive a qualification status of _Certified for Oracle Support_,
    
    -   Reseller or customer must be sponsored by an Oracle Linux Sales Representative, and
    -   Results must be submitted and audited by Oracle.
    
10.  How do I get started?
    
    Please contact us at [hcl-info\_ww@oracle.com](mailto:hcl-info_ww@oracle.com?subject=Request%20for%20more%20info%20about%20HCL) for more information about joining the Oracle Linux and Virtualisation Server Hardware Certification Program.
    

#### Section 2: Server Hardware Certification

(show all | hide all, or click each question to show/hide answer)

1.  Can customers get support for a system that is not on the server certification list?
    
    The [HCL](https://linux.oracle.com/hardware-certifications) is always expanding. If the desired server meets the minimum requirements for the Oracle Linux release you want to deploy but the server is not listed on the HCL, Oracle will accept severity 2 or lower service requests (SR), but a resolution to hardware driver or other hardware-specific issues cannot be guaranteed. Work on the SR will continue normally, unless or until it is determined that resolution of the issue depends on a driver patch, a new driver from the hardware partner, full certification of the server by the hardware partner, or other software enhancements.
    
    If the resolution depends on a patch to a driver, Support will open an enhancement request with development to identify and deliver a patch if feasible. If a full server certification or a new driver is required from the hardware partner, the hardware partner will be engaged; the SR will be closed and a severity 2 enhancement request will be opened to track progress with the hardware partner. In either case, a resolution is not guaranteed and may take several weeks or longer.
    
2.  For servers on the HCL, does certification apply to all hardware components available for that server?
    
    For servers or storage already on the certified list, requests to support a specific component or peripheral (such as a specific NIC or CNA) that was not included with the initial certification will be evaluated by development as an enhancement requests. Resolution is not guaranteed and may take several weeks or longer.
    
3.  I understand that Oracle Linux comes packaged with two kernels— the Unbreakable Enterprise Kernel, and the Red Hat compatible kernel. Which kernel should I choose to certify my server?
    
    The goal of The Oracle Linux and Virtualisation Server Hardware Certification Program is to certify servers with UEK. Therefore, all certification testing is performed with UEK by vendors and partners using an certification test it provided by Oracle.
    
    Certification of Oracle Linux with the RHEL-compatible kernel (RHCK) isn't necessary because Oracle Linux is 100% application binary compatible with Red Hat Enterprise Linux. For example, a system certified with Red Hat Enterprise Linux 8 is inherently certified with Oracle Linux 8 with RHCK. For a list of systems certified with Oracle Linux running RHCK, please see the [Red Hat hardware catalogue](https://access.redhat.com/ecosystem/search/#/category/Server/).
    
4.  Why did you stop publishing certifications for maintenance updates, like Oracle Linux 7.x or Oracle Linux 8.x?
    
    Beginning with Oracle Linux 7, certifications are published for the major release. The minimum required maintenance update and corresponding UEK release is specified. The server is certified for all subsequent Oracle Linux 7 maintenance updates with the indicated UEK release. The same is true for Oracle Linux 8.
    
5.  What has changed now that Oracle VM is in sustaining mode? Will new hardware be certified to run with Oracle VM?
    
    Traditionally, Independent Hardware Vendors (IHV) certified servers for Oracle Linux with UEK and for Oracle VM operating environments, and they certified storage systems with Storage Connect for Oracle VM.
    
    Beginning on April 1, 2021, Oracle VM 3 is under Extended Support, thus there is no newer hardware certification for Oracle VM 3 per [Oracle Linux and Oracle VM Support Policies](https://www.oracle.com/us/support/library/enterprise-linux-support-policies-069172.pdf) and [Lifetime Support Policy: Coverage for Oracle Linux and Oracle VM](https://www.oracle.com/us/support/library/elsp-lifetime-069338.pdf).
    
    Oracle Linux KVM, with the Oracle Linux Virtualisation Manager, is the preferred virtualisation solution. While not listed separately on the HCL, servers certified for Oracle Linux are also certified for Oracle Linux KVM.
    
6.  What is Oracle Linux KVM and Oracle Linux Virtualisation Manager (OLVM)?
    
    Oracle Linux KVM refers to the hypervisor capability enabled by the Kernel-based Virtual Machine (KVM) feature of Oracle Linux. The Oracle Linux KVM hypervisor is not certified independently of Oracle Linux, therefore separate entries for Oracle Linux KVM are not listed in the HCL. Servers certified with Oracle Linux are inherently certified to run as an Oracle Linux KVM host.
    
    Oracle Linux Virtualisation Manager (OLVM) is a free, open source management interface to Oracle Linux KVM. Oracle offers full support for OLVM, which is based on the oVirt community project.
    
    For information about the operating system requirements of hosts that can be managed by Oracle Linux Virtualisation Manager (OLVM), refer to the [OLVM documentation](https://docs.oracle.com/en/virtualisation/oracle-linux-virtualisation-manager/index.html) in the Oracle Linux Documentation Library.
    
7.  What is the difference between Oracle VM Server for x86 and Oracle Linux KVM?
    
    Oracle Linux KVM is a modern virtual machine hosting environment that can be managed by [Oracle Linux Virtualisation Manager (OLVM)](https://docs.oracle.com/en/virtualisation/oracle-linux-virtualisation-manager/index.html), an open source oVirt-based management tool. Full support for OLVM is included with Oracle Linux Premier Support.
    
    Oracle VM is a xen-based hosting environment managed by the Oracle VM Manager. Oracle VM is now in sustaining mode and is no longer actively certified with server and storage hardware.
    
    See [Oracle Virtualisation](https://www.oracle.com/virtualisation/) product pages for additional information.
    
8.  On which platforms is Oracle Linux KVM available?
    
    Oracle Linux KVM refers to the KVM hypervisor capability of Oracle Linux. Beginning with Oracle Linux 7 and UEK Release 5, server certification with Oracle Linux inherently includes certification for Oracle Linux KVM.
    
9.  Which servers are certified for Oracle Linux KVM?
    
    All servers certified with Oracle Linux 7.6 (minimum) with UEK R5 Update 2 (minimum) are inherently certified with Oracle Linux KVM. [Oracle Linux KVM](https://docs.oracle.com/cd/E52668_01/E54669/html/ol7-kvm.html) refers to the hypervisor capability enabled by the Kernel-based Virtual Machine (KVM) feature of Oracle Linux; hosts running Oracle Linux KVM can be managed by Oracle Linux Virtualisation Manager (OLVM). KVM is part of the Oracle Linux operating system, and Oracle does not require server vendors to perform any additional certification testing outside the standard HCL test kit.
    
    Storage and component vendors may elect to validate their products with Oracle Linux KVM and OLVM using their own in-house certification to confirm compatibility with their products.
    
10.  If Oracle VM Server is certified on my server system, is Oracle Linux KVM also certified?
    
    Not necessarily. If Oracle Linux 7 with UEK Release 5 is certified, then Oracle Linux KVM is certified. Oracle VM Server certification requires a separate certification effort, and Oracle VM is no longer being certified for new servers.
    
11.  We have our own server qualification process. What additional value will Oracle Linux and Oracle VM certification test kit provide us?
    
    Performing certification testing using the hardware test kit from Oracle helps ensure that all of the critical features of Oracle Linux are functioning correctly on the target hardware. The test kit has proven to be very effective at verifying the compatibility of Oracle Linux with the target hardware, and the documentation produced by the test kit is a valuable tool for Oracle Support and for sustaining engineering when customer issues are discovered. For these reasons the use of the hardware test kit from Oracle has resulted in reduced support costs for Oracle and the partner while shortening implementation times for our mutual customers.
    
    Hardware vendors may elect to perform additional certification of individual features, such as the Oracle Linux KVM feature, outside of the Oracle Linux and Virtualisation Hardware Certification Program for their own purposes using their own certification tools. Oracle does not track or publish certification results performed outside the Oracle Linux and Virtualisation Hardware Certification Program.
    
12.  Is the testing outcome a strict pass or a fail, or is there a way to specify exceptions? For example, what if Oracle Linux lacks a single driver to fully complete the certification on a particular hardware platform?
    
    While not encouraged, exceptions are possible. Oracle will handle exceptions on a case-by-case basis, based on the test results submitted by program participants.
    
13.  There are many server models in the server family I want to certify. Do I need to certify each every model separately?
    
    If there are many server models within a product family, all sharing identical architectures, the server test kit must be run on a representative model of the server configured with the maximum supported amount of RAM and number of CPUs. It is not required to run the certification test kit on all the possible configurations of the server, or on each model within the product family.
    
14.  What mechanism do program participants use to communicate with Oracle during the server certification process?
    
    Participants submit certification requests, submit certification result logs for review, and file bugs against the hardware test kit content and environment via an issue tracking system.
    
15.  How long does it typically take to run the hardware test kit?
    
    The time required to complete the server certification testing depends upon the number of CPUs, amount of memory, and IO and networking options on the server. We expect the majority of server hardware to take somewhere between 2 to 10 hours. Test run times could be substantially larger for very large machines with dozens of CPU cores and hundreds of GB of memory.
    

### Section 3: Hypervisor Certification

(show all | hide all, or click each question to show/hide answer)

1.  Why are hypervisors certified and included on the Hardware Certification List?
    
    From the user perspective the guest must behave on a hypervisor exactly as it behaves on a physical server. Guests are certified with hypervisors to help ensure that the guest interacts with the virtualised hardware correctly. Just as the [Hardware Certification List](https://linux.oracle.com/hardware-certifications) (HCL) lists physical servers certified to host an Oracle Linux environment, the HCL lists hypervisors that are certified to host Oracle Linux guests. In this context there is no distinction between a physical server and hypervisor environment.
    
    Please see the [Server HCL FAQ](https://linux.oracle.com/hcl_faq.html) for information about servers certified with Oracle Linux, Oracle Linux KVM, and Oracle VM, and for general questions about the Oracle Linux and Virtualisation Hardware Certification Program.
    
    Please see the [Storage HCL FAQ](https://linux.oracle.com/ovm_storage_faq.html) for information about certifying storage systems with Oracle VM.
    
2.  Does certification of Oracle Linux as a guest OS on a hypervisor extend to all Oracle products running in that guest or hypervisor?
    
    Certification applies only to Oracle Linux as a guest operating system on the specified hypervisor. Oracle products that are certified with Oracle Linux are supported on Oracle virtualisation environments (such as Oracle KVM, Oracle VM VirtualBox, and Oracle VM Server). Certification of Oracle Linux as a guest operating system on non-Oracle hypervisors does not imply certification of other Oracle products running in that hypervisor environment. Information about certification of other Oracle products running on Oracle Linux with non-Oracle hypervisors is available in [My Oracle Support (MOS) article 417770.1](https://support.oracle.com/knowledge/Oracle%20Cloud/417770_1.html).
    
3.  What hypervisors environments are certified to run Oracle Linux guests on x86-based systems?
    
    Oracle Linux is a supported guest operating system on Oracle Linux KVM, and certified with some third-party hypervisors as well. Third-party hypervisor environments certified to run Oracle Linux guests are listed on the [HCL](https://linux.oracle.com/ords/f?p=117:1::::RP::). From the HCL home page, select "Hypervisors" from the Environment pull-down list. Please refer to question #2 for important information about the Oracle products running on hypervisors.
    
4.  Can customers get support for an Oracle Linux guests on a hypervisor that is not on the server certification list?
    
    Oracle Linux is supported as a guest operating system on Oracle Linux KVM, and on hypervisor environments listed on the [HCL](https://linux.oracle.com/hardware-certifications).
    
5.  What is PV, HVM and PVHVM and why is it important?
    
    Hypervisors support three modes of virtualisation: Paravirtualisation or modified guest (PV), hardware-assisted virtualisation or unmodified guest (HVM), and hardware-assisted virtualisation with paravirtualised disk drive and network drivers (PVHVM). The modes supported by a guest are dependent on the capabilities of the hypervisor, the features of the underlying hardware, and driver support within the guest.
    
6.  What kernels are certified for Oracle Linux guests?
    
    Oracle Linux with Unbreakable Enterprise Kernel (UEK) is tested and certified in hypervisor environments and listed on the [HCL](https://linux.oracle.com/hardware-certifications). For certification information about Oracle Linux guests running the RHEL-compatible kernel, users should refer to the certification matrices published by the vendor of that kernel.
    
7.  If a guest OS is certified with the current release of Unbreakable Enterprise Kernel (UEK), is it automatically certified for future releases of UEK too?
    
    Certifications published for one major release of UEK do not apply to future major releases of UEK. For instance, a guest OS certification for Oracle Linux 8.6 that specifies a minimum kernel requirement of UEK 5.4.17-2011.0.7 (UEK Release 6) is also certified with all subsequent UEK R6 updates, such as UEK 5.4.17-2136.300.7. The same guest OS is not necessarily certified with UEK 5.15.0-0.30.19 (UEK Release 7). Certifications of the guest OS with multiple major releases of UEK are listed individually.
    

### Section 4: Oracle VM Storage Certification

(show all | hide all, or click each question to show/hide answer)

1.  What is Oracle VM certified Storage?
    
    The Oracle VM Certified Storage program is no longer active because Oracle VM is now in maintenance mode. 
    
    Oracle VM certified storage is a storage system that has been tested using the _Storage Connect for Oracle VM Certification Test Kit_. All test results have been audited by Oracle and storage systems posted here are supported for use with the indicated versions of Oracle VM. The storage certification program enables established storage partners, which are generally Independent Hardware Vendors (IHVs) and resellers with Oracle Partner Network membership, to qualify their storage systems for use with Oracle VM software using an Oracle supplied storage hardware test kit.
    
    The output of this program is the Hardware Compatibility List ([HCL](https://linux.oracle.com/hardware-certifications)), which documents storage compatibility with Oracle VM.
    
    Through this qualification, Oracle and its storage system partners are able to help ensure that both parties are equipped to provide collaborative support to customers using the tested storage in an Oracle VM environment.
    
2.  What has changed now that Oracle VM is in sustaining mode? Will new hardware be certified to run with Oracle VM?
    
    Traditionally, Independent Hardware Vendors (IHV) certified servers for Oracle Linux with UEK and for Oracle VM operating environments, and they certified storage systems with Storage Connect for Oracle VM.
    
    Beginning on April 1, 2021, Oracle VM 3 is under Extended Support, thus there is no newer hardware certification for Oracle VM 3 per [Oracle Linux and Oracle VM Support Policies](https://www.oracle.com/us/support/library/enterprise-linux-support-policies-069172.pdf) and [Lifetime Support Policy: Coverage for Oracle Linux and Oracle VM](https://www.oracle.com/us/support/library/elsp-lifetime-069338.pdf).
    
    Oracle Linux KVM, with the Oracle Linux Virtualisation Manager, is the preferred virtualisation solution. While not listed separately on the HCL, servers certified for Oracle Linux are also certified for Oracle Linux KVM.
    
3.  What is Oracle VM Storage Connect?
    
    Oracle VM Storage Connect is an application programming interface (API) into Oracle VM. Through this interface Oracle VM Storage Connect enables administrators to directly manage storage operations through Oracle VM Manager, a component of Oracle VM 3.
    
    By integrating virtualised server and storage management operations into a single GUI-based tool, Oracle VM Storage Connect enables Oracle VM administrators to directly configure and manage the storage attached to their Oracle VM server pools. They can fully leverage their investments in advanced storage functionality, such as de-duplication and fast clone, and streamline the deployment and management of virtual infrastructure and applications in data centre and cloud environments.
    
    Storage systems that are certified with Oracle VM Storage Connect are listed in the [HCL](https://linux.oracle.com/hardware-certifications).
    
4.  I don't see my storage system listed on the HCL. Can I still get support?
    
    Oracle VM is in maintenance mode. No additional server or storage hardware will be certified or added to the HCL.
    
5.  Is storage that is certified with Oracle VM also certified with Oracle Linux with Unbreakable Enterprise Kernel?
    
    The storage certification program is specific to Oracle VM. The certification test kit verifies that the Storage Connect layer of Oracle VM communicates and functions properly with the target storage system. The storage certification program does not extend to Oracle Linux because Oracle Linux uses standard Fibre Channel, iSCSI and NFS protocols, storage adapters and drivers, and does not depend upon an API like Storage Connect to communicate with storage systems.
    

Resources

![](https://www.oracle.com/partners/campaign/newsletters/sectionline-dkbrown-5899863.png) 

![](https://linux.oracle.com/hcl-images/Abstract_strip_5.png)

This document is provided for information purposes only, and the contents hereof are subject to change without notice. This document is not warranted to be error-free, nor subject to any other warranties or conditions, whether expressed orally or implied in law, including implied warranties and conditions of merchantability or fitness for a particular purpose. We specifically disclaim any liability with respect to this document, and no contractual obligations are formed either directly or indirectly by this document. This document may not be reproduced or transmitted in any form or by any means, electronic or mechanical, for any purpose, without our prior written permission.

Copyright © 2013,2022 Oracle. All rights reserved. Oracle and Java are registered trademarks of Oracle and/or its affiliates. Other names may be trademarks of their respective owners. 0113

