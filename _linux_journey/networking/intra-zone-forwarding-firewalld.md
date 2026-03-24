---
title: "Intra Zone Forwarding Firewalld"
category: "networking"
tags: ["networking", "intra", "zone", "forwarding", "firewalld"]
---

[![](../_resources/firewalld.org_872fb0f187b5403b9ce30c61991d6687.png)](https://firewalld.org/)

A service daemon with D-Bus interface

- [Home](https://firewalld.org/)
- [Blog](https://firewalld.org/blog/)
- [Community](https://firewalld.org/community.html)
- [Contribute](https://firewalld.org/contribute.html)
- [Documentation](https://firewalld.org/documentation/)
    - [Concepts](https://firewalld.org/documentation/concepts.html)
    - [Architecture](https://firewalld.org/documentation/architecture.html)
    - [Configuration](https://firewalld.org/documentation/configuration/)
        - [Directories](https://firewalld.org/documentation/configuration/directories.html)
        - [Runtime versus Permanent](https://firewalld.org/documentation/configuration/runtime-versus-permanent.html)
        - [firewalld.conf](https://firewalld.org/documentation/configuration/firewalld-conf.html)
    - [Utilities](https://firewalld.org/documentation/utilities/)
        - [firewall-cmd](https://firewalld.org/documentation/utilities/firewall-cmd.html)
        - [firewall-offline-cmd](https://firewalld.org/documentation/utilities/firewall-offline-cmd.html)
        - [firewall-config](https://firewalld.org/documentation/utilities/firewall-config.html)
        - [firewall-applet](https://firewalld.org/documentation/utilities/firewall-applet.html)
    - [The daemon: firewalld](https://firewalld.org/documentation/the-daemon-firewalld.html)
    - [Zone](https://firewalld.org/documentation/zone/)
        - [Predefined Zones](https://firewalld.org/documentation/zone/predefined-zones.html)
        - [Connections, Interfaces and Sources](https://firewalld.org/documentation/zone/connections-interfaces-and-sources.html)
        - [Configuration of Zones](https://firewalld.org/documentation/zone/configuration-of-zones.html)
        - [Default Zone](https://firewalld.org/documentation/zone/default-zone.html)
        - [Use of Zones](https://firewalld.org/documentation/zone/use-of-zones.html)
        - [Options](https://firewalld.org/documentation/zone/options.html)
        - [Examples](https://firewalld.org/documentation/zone/examples.html)
    - [Service](https://firewalld.org/documentation/service/)
        - [Options](https://firewalld.org/documentation/service/options.html)
        - [Examples](https://firewalld.org/documentation/service/examples.html)
    - [IPSet](https://firewalld.org/documentation/ipset/)
        - [Options](https://firewalld.org/documentation/ipset/options.html)
        - [Examples](https://firewalld.org/documentation/ipset/examples.html)
    - [Helper](https://firewalld.org/documentation/helper/)
        - [Options](https://firewalld.org/documentation/helper/options.html)
        - [Examples](https://firewalld.org/documentation/helper/examples.html)
    - [ICMP Type](https://firewalld.org/documentation/icmptype/)
        - [Options](https://firewalld.org/documentation/icmptype/options.html)
        - [Examples](https://firewalld.org/documentation/icmptype/examples.html)
    - [Direct Interface](https://firewalld.org/documentation/direct/)
        - [Options](https://firewalld.org/documentation/direct/options.html)
        - [Examples](https://firewalld.org/documentation/direct/examples.html)
    - [HowTo](https://firewalld.org/documentation/howto/)
        - [Enable and Disable firewalld](https://firewalld.org/documentation/howto/enable-and-disable-firewalld.html)
        - [Get firewalld State](https://firewalld.org/documentation/howto/get-firewalld-state.html)
        - [Reload firewalld](https://firewalld.org/documentation/howto/reload-firewalld.html)
        - [Open a Port or Service](https://firewalld.org/documentation/howto/open-a-port-or-service.html)
        - [Add a Service](https://firewalld.org/documentation/howto/add-a-service.html)
        - [Debug firewalld](https://firewalld.org/documentation/howto/debug-firewalld.html)
    - [Manual Pages](https://firewalld.org/documentation/man-pages/)
        - [firewalld(1)](https://firewalld.org/documentation/man-pages/firewalld.html)
        - [firewall-cmd(1)](https://firewalld.org/documentation/man-pages/firewall-cmd.html)
        - [firewall-offline-cmd(1)](https://firewalld.org/documentation/man-pages/firewall-offline-cmd.html)
        - [firewall-config(1)](https://firewalld.org/documentation/man-pages/firewall-config.html)
        - [firewall-applet(1)](https://firewalld.org/documentation/man-pages/firewall-applet.html)
        - [firewalld.conf(5)](https://firewalld.org/documentation/man-pages/firewalld.conf.html)
        - [firewalld.zones(5)](https://firewalld.org/documentation/man-pages/firewalld.zones.html)
        - [firewalld.zone(5)](https://firewalld.org/documentation/man-pages/firewalld.zone.html)
        - [firewalld.policies(5)](https://firewalld.org/documentation/man-pages/firewalld.policies.html)
        - [firewalld.policy(5)](https://firewalld.org/documentation/man-pages/firewalld.policy.html)
        - [firewalld.service(5)](https://firewalld.org/documentation/man-pages/firewalld.service.html)
        - [firewalld.ipset(5)](https://firewalld.org/documentation/man-pages/firewalld.ipset.html)
        - [firewalld.helper(5)](https://firewalld.org/documentation/man-pages/firewalld.helper.html)
        - [firewalld.icmptype(5)](https://firewalld.org/documentation/man-pages/firewalld.icmptype.html)
        - [firewalld.richlanguage(5)](https://firewalld.org/documentation/man-pages/firewalld.richlanguage.html)
        - [firewalld.direct(5)](https://firewalld.org/documentation/man-pages/firewalld.direct.html)
        - [firewalld.lockdown-whitelist(5)](https://firewalld.org/documentation/man-pages/firewalld.lockdown-whitelist.html)
        - [firewalld.dbus(5)](https://firewalld.org/documentation/man-pages/firewalld.dbus.html)
    - [External Resources](https://firewalld.org/documentation/external.html)
    - [Working With The Source](https://firewalld.org/documentation/working-with-the-source.html)
- [Download](https://firewalld.org/download/)
    - [All Releases](https://firewalld.org/download/all.html)
- [Search](https://firewalld.org/search.html)
- [](https://github.com/firewalld/firewalld)

[firewalld 0.7.4 release](https://firewalld.org/2020/04/firewalld-0-7-4-release) [firewalld 0.8.3 release](https://firewalld.org/2020/06/firewalld-0-8-3-release)

# Intra Zone Forwarding

Apr 29, 2020 • Eric Garver

A new feature, intra zone forwarding, is coming to firewalld. This feature allows packets to freely forward between interfaces or sources with in a zone.

## Why is it needed?

One axiom of zone based firewalls is that traffic with in a zone can flow from interface (or source) to interface (or source). The zone specifies the trust level of all those interfaces and sources. If they have the same trust level then they can communicate unencumbered. Firewalld has lacked this functionality until now.

## What does it look like?

This feature does not bring many CLI additions; only a couple knobs to enable or disable it for the zone.

Let’s say we have our `home` zone with two interfaces: dummy1, and dummy2

```
# firewall-cmd --zone=home --add-interface=dummy1 --add-interface=dummy2
```

Now let’s enable intra zone forwarding.

```
# firewall-cmd --zone=home --add-forward
```

This results in the following nftables rules being added to the zone.

```
table inet firewalld {
    chain filter_FWDI_home_allow {
        oifname "dummy1" accept
        oifname "dummy2" accept
    }
}
```

The rules say: if the packet is destined to the any interface in the zone `home` then go ahead and accept it.

If we were to add another interface or source to the home zone then we will see it show up in the ruleset as well.

```
# firewall-cmd --zone=home --add-source 10.10.10.0/24
```

And the result:

```
table inet firewalld {
    chain filter_FWDI_home_allow {
        oifname "dummy1" accept
        oifname "dummy2" accept
        ip daddr 10.10.10.0/24 accept
    }
}
```

## Doesn’t this already happen?

Some zones use a `--set-target` of `ACCEPT`. Those zones immediately accept *all* forwarded traffic. As such, the new `--add-forward` option has no effect for them.

For all others `--set-target` values forwarded traffic is dropped by default. This includes all stock zones except *trusted*.

## Caveats

When enabled in the *default zone*, intra zone forwarding can only be applied to the interfaces and sources that have been explicitly added to the current *default zone*. It can not use a catch-all for all outgoing interfaces as this would allow packets to forward to an interface or source assigned to a different zone.

## Default value

By default, all currently shipped zone definitions and user created zones have `forward` disabled. This is done as to not introduce any surprising behavioral changes.

In the future this may change. It may make sense to enable by default in at least these zones: internal, home, and work.

## Contributed By

This feature was initially contributed by github user [@danc86](https://github.com/danc86) in pull request [#586](https://github.com/firewalld/firewalld/pull/586).

## Recent Posts

- [Strict Forward Ports](https://firewalld.org/2024/11/strict-forward-ports)
- [Strict Filtering of Docker Containers](https://firewalld.org/2024/04/strictly-filtering-docker-containers)
- [firewalld 2.1.0 release](https://firewalld.org/2024/01/firewalld-2-1-0-release)
- [firewalld 2.0.0 release](https://firewalld.org/2023/06/firewalld-2-0-0-release)
- [Software fastpath with nftables flowtable](https://firewalld.org/2023/05/nftables-flowtable)

## Quick Links

- [Report a new issue](https://github.com/firewalld/firewalld/issues/new)
- [Browse issues](https://github.com/firewalld/firewalld/issues)

All website content subject to the [Unlicense](https://unlicense.org).