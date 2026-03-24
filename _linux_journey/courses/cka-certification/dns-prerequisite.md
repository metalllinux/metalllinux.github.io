---
title: "Dns Prerequisite"
category: "cka-certification"
tags: ["cka-certification", "dns", "prerequisite"]
---

* Two Hosts, Host A and Host B.
* Share a network between them, which is `192.168.1.0`
* Host A is on `192.168.1.10`
* Host B is on `192.168.1.11`
* Want to ping Host B by its name `db`, instead of its address.
	* If you attempt to ping Host B in the current state of the network with the name `db`, you'll receive `ping: unknown host db`.
* Need to tell Host A that when it refers to Host B's `db` name, to tie that to its address of `192.168.1.11`
* Therefore to set the DNS, add an entry into the `/etc/hosts` file of:
```
192.168.1.11	db
```
* Pings for host `db` are now sent to the right place.
* With the above configuration, Host A does not check if Host B's actual name is `db` in this case.
* Even if Host B changes its name to `Host2`, Host A still refers to it by `db` in the `/etc/hosts` table if that hasn't changed.
* Can even fool Host A into redirecting traffic to IPs from certain websites:
```
192.168.1.12    www.trollsite.com
```
* Can even set the separate DNS names for one IP address. Therefore if you ping either name, it still redirects to the right IP address:
```
192.168.1.12	www.test-me.com
192.168.1.12	test
```
* Regardless of the action taken, the above method still works (using IP Mapping).
* The above process is known as `Name Resolution`.
* In a small network, the above method works great. It does not work on a scaled network.
	* If one IP in a server changes, have to update the `/etc/hosts` file for all hosts.
* A central point for managing `Name Resolution` is a DNS server.
	* Just point all hosts to that server and the DNS server will point them in the right direction of whom owns which IP with which hostname.
* How do we point a host to a DNS server?
* Every host has a DNS Resolution File at `/etc/resolv.conf`
* You specify the address of the DNS server you want to navigate to there:
```
nameserver	192.168.1.100
```
* Configure the above on all hosts.
* Can still combine the above method with manually adding hosts to `/etc/hosts` with adding a DNS server to the `/etc/resolv.conf` file, such as a test server.
* Linux will check in the `/etc/hosts` file first and then the `/etc/resolv.conf` file.
	* The above order can be changed, by editing the configuration in the `/etc/nsswitch.conf` file:
```
# Configuration here
hosts:	files dns
# Configuration also here
```
* `files` refers to the `/etc/hosts` file.
* `dns` is for the `DNS` server.
* What if you try to ping a server that is not in `/etc/hosts` nor `/etc/resolv.conf`?
	* This fails and you see the message `Temporary failure in name resolution`
		* You can solve this by pointing to a place that knows the website:
```
nameserver	192.168.1.100
nameserver	8.8.8.8
```
* Can have multiple configurations as listed above on each host.
* The last bit at the end of a domain name such as `.com`, `.net`, `.edu`, `.org` and `.io` - all of these are `top level domains`.
* `.com` --> commercial or general purpose.
* `.net` --> network
* `.edu` --> educational purposes
* `.org` --> for non-profit organisations.
* The `www` is the subdomain.
	* In addition, `maps` from `maps.google.com` is a subdomain and so is `apps` from `apps.google.com`, `mail.google.com` as well.
* From example you try to access `apps.google.com` from within the organisation.
	* This goes to your organisation's DNS server.
	* If it does know, it goes out to the `Root DNS` server.
	* The `Root DNS` server checks the request and points to the DNS server handling `.com` addresses.
	* That then points to `Google`'s DNS server.
* In order to speed up the above process however, the Organisation's DNS server will cache the `apps.google.com` IP address for a period of time.
* An example within an organisation.
	* Your ORG DNS points to `mycompany.com`, which has multiple subdomains, `www`, `pay`, `hr`, `mail`, `drive`
	* Theses are all configured with the organisation's DNS server.
* In the previous example, if you now try to ping `web`, you can't because the DNS server has `web` as `web.mycompany.com` and
	* We want to address this as just `web` though.
	* How do you resolve `web` to `web.mycompany.com`?
	* To do this, add an entry into the `/etc/resolv.conf` file:
```
nameserver	192.168.1.100
search	mycompany.com
```
* Next time if you ping `web`, the host will intelligently ping `web.mycompany.com`
* Of course you can also `ping web.mycompany.com` as well.
* Can also add other addresses there:
```
nameserver	192.168.1.100
search	mycompany.com	prod.mycompany.com 
```
* The host will also try to search for all of these domain names, for example `web.prod.mycompany.com`.
* Record Types:
```
A	web-server	192.168.1.1
AAAA	web-server	2001:df3421:0000:0000
CNAME	food.web-server	eat.web-server.hungry-web-server
```
* How are the above records stored in the DNS server?
* IPv4 to Host Names --> known as A records.
* Storing IPv6 Host Names --> known as AAAA records.
* Mapping one name to another --> known as CNAME records.
	* Regarding CNAMEs, have multiple aliases within one application, like a food delivery service.
	* Does Name to Name mapping.
* `ping` is not always the right tool to test resolution, using `nslookup` is also good.
	* `nslookup` queries a hostname from a DNS server.
	* `nslookup` **Does Not** take into account the entries in the `/etc/hosts` file.
	* For example adding an entry into `/etc/hosts` for your web application, means that it won't have any luck finding it.
		* The entry has to be present in your DNS server.
* `dig` - useful tool for testing DNS name resolution.
	* `dig <site name>`