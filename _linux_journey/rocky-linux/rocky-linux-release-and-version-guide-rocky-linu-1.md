---
title: "Rocky Linux Release And Version Guide Rocky Linu 1"
category: "rocky-linux"
tags: ["rocky-linux", "rocky", "linux", "release", "version"]
---

[Skip to content](https://wiki.rockylinux.org/rocky/version/#current-supported-releases)

<img width="26" height="26" src="../_resources/icon-white_cc79942ca71243eeb7627249184d9143-1.svg"/>](https://wiki.rockylinux.org/ "Rocky Linux Wiki")

Rocky Linux Wiki

Rocky Linux Release and Version Guide

Type to start searching

[rocky-linux/wiki.rockylinux.org<br>- 40<br>- 23](https://github.com/rocky-linux/wiki.rockylinux.org "Go to repository")

- [Welcome](https://wiki.rockylinux.org/)
- [Link Directory](https://wiki.rockylinux.org/links/)
- [General Chat and IRC](https://wiki.rockylinux.org/irc/)
- [Rocky Linux](https://wiki.rockylinux.org/rocky/)
- [Guidelines](https://wiki.rockylinux.org/guidelines/bug_tracker_guidelines/)
- [Special Interest Groups](https://wiki.rockylinux.org/special_interest_groups/)
- [Teams](https://wiki.rockylinux.org/team/)
- [Events](https://wiki.rockylinux.org/events/FOSDEM_2024/)
- [Contributing](https://wiki.rockylinux.org/contributing/)
- [Archive](https://wiki.rockylinux.org/archive/)

- [Rocky Linux](https://wiki.rockylinux.org/rocky/)
    
    - [Getting Community Help & Support](https://wiki.rockylinux.org/rocky/support/)
    - [Reporting Bugs and RFE's](https://wiki.rockylinux.org/rocky/bugs/)
    - [Rocky Linux Errata](https://wiki.rockylinux.org/rocky/errata/)
    - [Rocky Linux ISOs and Images](https://wiki.rockylinux.org/rocky/image/)
    - [Rocky Linux Repositories](https://wiki.rockylinux.org/rocky/repo/)
    - [Rocky Linux RSS Feeds](https://wiki.rockylinux.org/rocky/rss/)
    - [Rocky Linux Release and Version Guide](https://wiki.rockylinux.org/rocky/version/)
        
        - [Current Supported Releases](https://wiki.rockylinux.org/rocky/version/#current-supported-releases)
        - [Timeline and Terminology](https://wiki.rockylinux.org/rocky/version/#timeline-and-terminology)
            
            - [Terminology](https://wiki.rockylinux.org/rocky/version/#terminology)
            - [Timeline](https://wiki.rockylinux.org/rocky/version/#timeline)
                
                - [Major Version Release](https://wiki.rockylinux.org/rocky/version/#major-version-release)
                - [Minor Version Release](https://wiki.rockylinux.org/rocky/version/#minor-version-release)
                
            - [Release Cadence](https://wiki.rockylinux.org/rocky/version/#release-cadence)
            
        - [Version Policy](https://wiki.rockylinux.org/rocky/version/#version-policy)
            
            - [General Update Timeline](https://wiki.rockylinux.org/rocky/version/#general-update-timeline)
            
        - [End of Life and Unsupported Release/Version Policy](https://wiki.rockylinux.org/rocky/version/#end-of-life-and-unsupported-releaseversion-policy)
            
            - [Example: An Unsupported Version](https://wiki.rockylinux.org/rocky/version/#example-an-unsupported-version)
            - [Example: An End of Life Release](https://wiki.rockylinux.org/rocky/version/#example-an-end-of-life-release)
            
        - [Beta to Stable Policy](https://wiki.rockylinux.org/rocky/version/#beta-to-stable-policy)
        - [Upgrade Policy](https://wiki.rockylinux.org/rocky/version/#upgrade-policy)
        
    - [PackageKit Missing Items](https://wiki.rockylinux.org/rocky/packagekit/)
    

[](https://github.com/rocky-linux/wiki.rockylinux.org/edit/development/docs/rocky/version.md "Edit this page")

# Rocky Linux Release and Version Guide

This page goes over the Rocky Linux Release Versions, their support, timelines, and how it affects our users.

## Current Supported Releases[¶](https://wiki.rockylinux.org/rocky/version/#current-supported-releases "Permanent link")

Below is a table of Rocky Linux versions, with accompanying general release and (planned or are planned) end of life dates.

| Release | Codename | Release Date | Active Support Ends | End of Life | Latest/Current Version |
| --- | --- | --- | --- | --- | --- |
| Rocky Linux 8 | Green Obsidian | May 1, 2021 | May 31, 2024 | May 31, 2029 | 8.9 (November 22, 2023) |
| Rocky Linux 9 | Blue Onyx | July 14, 2022 | May 31, 2027 | May 31, 2032 | 9.4 (May 9, 2024) |

For more detailed information on each version, click any of the tabs below.

[Rocky Linux 8](#__tabbed_1_1)[Rocky Linux 9](#__tabbed_1_2)

| Version | Release Kernel | Release Date | End of Life | Supported |
| --- | --- | --- | --- | --- |
| 8.3 | 4.18.0-240 | May 1, 2021 | June 21, 2021 | NO  |
| 8.4 | 4.18.0-305 | June 21, 2021 | November 15, 2021 | NO  |
| 8.5 | 4.18.0-348 | November, 15 2021 | May 15, 2022 | NO  |
| 8.6 | 4.18.0-372.9.1 | May 15, 2022 | November 11, 2022 | NO  |
| 8.7 | 4.18.0-425.3.1 | November 11, 2022 | May 20, 2023 | NO  |
| 8.8 | 4.18.0-477.10.1 | May 20, 2023 | November, 2023 | NO  |
| 8.9 | 4.18.0-513.5.1 | November 22, 2023 | May, 2024 | Yes |

See the [Timeline and Terminology](https://wiki.rockylinux.org/rocky/version/#timeline-and-terminology) and [Release Cadence](https://wiki.rockylinux.org/rocky/version/#release-cadence) sections for more information on how these dates are determined.

## Timeline and Terminology[¶](https://wiki.rockylinux.org/rocky/version/#timeline-and-terminology "Permanent link")

### Terminology[¶](https://wiki.rockylinux.org/rocky/version/#terminology "Permanent link")

Throughout this page, you will see terms such as "major version" or "minor version", among others. You will see these terms used throughout many discussions online forums, mail lists, or even our Mattermost. See below for their basic definitions.

| Term | Definition |
| --- | --- |
| Major Version | A major version is denoted by a whole number, such as "Rocky Linux 9". This number is left-most number in a version, such as 9.0, where "9" is the major version. |
| Minor Version | A minor version is denoted by the right-most number in a version, such as "Rocky Linux 9.3". "9" being the major version, "3" being the minor version. These updates come with version upgrades, rebases, new software and features. |
| Release | Release typically refers to a major version release, such as "Rocky Linux 9". It is typically assumed it is referring to the latest/current version of that release. |
| Minor Release | Used as "Minor Version" in most cases. |
| Active Support | Active support, also known as "full support" is the period of time in which minor releases are provided every six (6) months, whilst providing new software, rebases, or other new features. When Active Support ends, a release receives maintenance-only updates. |

### Timeline[¶](https://wiki.rockylinux.org/rocky/version/#timeline "Permanent link")

Rocky Linux strives to follow Red Hat Enterprise Linux and CentOS Stream within reason. As such, Rocky Linux releases should follow fairly close to our upstreams.

#### Major Version Release[¶](https://wiki.rockylinux.org/rocky/version/#major-version-release "Permanent link")

For a new Rocky Linux release, the following should be true:

- New major version is released with support of ten (10) years\[1\], starting at `.0`.
- Release will have five (5) years of minor version updates
    
    - Releases come with two minor version releases a year: Every six (6) months
    - Minor releases will come with new features, software rebases, and sometimes brand new software
    - Final minor version will almost always be `.10`

#### Minor Version Release[¶](https://wiki.rockylinux.org/rocky/version/#minor-version-release "Permanent link")

For a new Rocky Linux minor version release, the following should be true:

- New minor version is released with new features and/or software
- Previous minor version is moved to the [vault](https://wiki.rockylinux.org/rocky/repo/#vault) and is no longer supported

However, when the minor version is `.10`, this means:

- Rocky Linux (and other Enterprise Linux derivatives) go into security maintenance for the next five (5) years
- This version of Rocky Linux will likely not receive new features nor new software

### Release Cadence[¶](https://wiki.rockylinux.org/rocky/version/#release-cadence "Permanent link")

Based on Red Hat's life cycle policy, the month of May is when new major versions are released *and* every May and November a new minor version release is provided for prior supported releases. Rocky Linux attempts to follow as closely as possible to this same cadence.

Below is a general guideline (based on Red Hat documentation) for the "full support" cycle for Rocky Linux.

| Version | Month |
| --- | --- |
| .0  | May |
| .1  | November |
| .2  | May |
| .3  | November |
| .4  | May |
| .5  | November |
| .6  | May |
| .7  | November |
| .8  | May |
| .9  | November |
| .10 | May |

Upon a new minor release (`X.Y+1`), the previous Rocky Linux minor version is no longer supported and is moved to the [vault](https://wiki.rockylinux.org/rocky/repo/#vault).

After `X.10` is released, the following may be true:

- Maintenance Mode starts for the next five (5) years
- `X.10` is considered the final version for a release and only this receives updates until End of Life
- CentOS Stream X will cease development near the end of the month of May

## Version Policy[¶](https://wiki.rockylinux.org/rocky/version/#version-policy "Permanent link")

Rocky Linux attempts to follow closely with the updates of our upstream Red Hat Enterprise Linux. As such, updates aim to be released as on time as possible.

**For Rocky Linux 8**: Previous versions of packages will coexist in the repositories to allow a user to downgrade in case of a regression or other use cases (such as security only updates).

**For Rocky Linux 9**: This policy is not currently supported and can be expected in a future Rocky Linux version. Please see [Peridot Issue #18](https://github.com/rocky-linux/peridot/issues/18). Older versions of packages can by found in [Koji](https://kojidev.rockylinux.org) when they're uploaded or the vault.

**For all Rocky Linux versions**: When a new minor release arrives, all previous updates/versions are *not* carried over.

### General Update Timeline[¶](https://wiki.rockylinux.org/rocky/version/#general-update-timeline "Permanent link")

Updates for Rocky Linux are generally expected to be built and released between twenty-four (24) and fourty-eight (48) hours, assuming best effort allows the packages to build without any complications or unforeseen added dependencies by upstream mid-support cycle.

Minor releases for Rocky Linux are generally expected to be built and released at least a week (7 days) after upstream, assuming best effort allows the packages to build without any complications and it passes the Testing Team OpenQA and general testing.

## End of Life and Unsupported Release/Version Policy[¶](https://wiki.rockylinux.org/rocky/version/#end-of-life-and-unsupported-releaseversion-policy "Permanent link")

A release or version of Rocky Linux is considered unsupported if:

- The Rocky Linux minor version has been superseded by another minor release *or*
- The Rocky Linux release is End of Life

See the examples below.

### Example: An Unsupported Version[¶](https://wiki.rockylinux.org/rocky/version/#example-an-unsupported-version "Permanent link")

When a new Rocky Linux minor release arrives (`X.Y+1`) the following is true:

- The previous version is no longer supported by Release Engineering and the community
- This version is no longer updated and is moved to the [vault](http://dl.rockylinux.org/vault/rocky/).
- This version **does not** receive bug fix nor security updates.
- You are recommended to update your system with `dnf update`.

### Example: An End of Life Release[¶](https://wiki.rockylinux.org/rocky/version/#example-an-end-of-life-release "Permanent link")

When a Rocky Linux release has reached its End of Life date typically after ten (10) years (for example, May of 2029), the following is true:

- The release is no longer supported in full by Release Engineering and the community
- The final version is moved to the [vault](http://dl.rockylinux.org/vault/rocky/).
- This release no longer receives updates and thus no longer supported.
- You are recommended to install a supported Rocky Linux version and migrate your data.

If you cannot install a new system and migrate and you still need support for your system or systems, you may be able to find a support provider.

Warning

Support providers will maintain their own packages and policies outside of the Rocky Linux ecosystem, and thus their policies *do not* apply here. The release is still considered EOL and unsupported by the Rocky Linux project.

## Beta to Stable Policy[¶](https://wiki.rockylinux.org/rocky/version/#beta-to-stable-policy "Permanent link")

Rocky Linux may release beta versions when possible. These are typically close to our upstreams where reasonably possible. These are released specifically to find bugs or issues in our build process. This also helps correlate issues with our upstreams in the event they also have bugs. These are provided to our Testing Team members and others in the community and are free to download and test by anyone in the community.

However, when the stable minor version is released, updating from the beta to the stable version is not recommended nor is it supported, even for experienced users.

The following is unsupported:

- Updating from a stable release to beta release
- Updating from a beta release to stable release

## Upgrade Policy[¶](https://wiki.rockylinux.org/rocky/version/#upgrade-policy "Permanent link")

Upgrades are not generally supported by Release Engineering nor most of the Rocky community. If you wish to perform upgrades between releases, there is a tool called ELevate that may be able to help you. But as a note of caution, this has not been formally tested and we cannot provide official assistance.

Warning

Some users have expressed success with doing upgrades with this tool. However, it is not formally tested by the Rocky Linux project and we cannot provide official assistance.

Note

If you wish to be part of an effort to ensure upgrades are possible, we recommend that you join us in our Mattermost and ask how you can help.

2024-05-20

Copyright © 2023 Rocky Enterprise Software Foundation

Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)