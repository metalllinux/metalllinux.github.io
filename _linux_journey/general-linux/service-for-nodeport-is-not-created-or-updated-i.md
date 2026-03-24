---
title: "Navigation Menu"
category: "general-linux"
tags: ["service", "nodeport", "created", "updated"]
---

[Skip to content](#start-of-content)

## Navigation Menu

[](https://github.com/)

- [Pricing](https://github.com/pricing)

[Sign in](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Francher%2Francher%2Fissues%2F14366)

[Sign up](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Fvoltron%2Fissues_fragments%2Fissue_layout&source=header-repo&source_repo=rancher%2Francher)

[rancher](https://github.com/rancher) / **[rancher](https://github.com/rancher/rancher)** 

https://github.com/rancher/rancher/issues/14366
# Service for NodePort is not created or updated #14366

Closed

[dnauck](https://github.com/dnauck) opened this issue Jul 3, 2018 · 3 comments

Closed

# [Service for NodePort is not created or updated](#top) #14366

[dnauck](https://github.com/dnauck) opened this issue Jul 3, 2018 · 3 comments

## Comments

<img width="40" height="40" src="../_resources/97584_s_80_u_fbd3be9def17c69daf9_6832d4e369bd4aca8.jpg"/>](https://github.com/dnauck)

### 

**[dnauck](https://github.com/dnauck)** commented <a id="issue-338016289-permalink"></a>[Jul 3, 2018](#issue-338016289)

**Rancher versions:**  
rancher/server or rancher/rancher: 2.0.3  
rancher/agent or rancher/rancher-agent: 2.0.3

**Infrastructure Stack versions:**  
kubernetes (if applicable): 1.10.3-rancher2-1

**Setup details: (single node rancher vs. HA rancher, internal DB vs. external DB)**

custom cluster/rke on ubuntu

**Steps to Reproduce:**

add a new workload, e.g. `atmoz/sftp` and create a new port mapping for port 22:  
Type: NodePort  
Protocol: TCP  
Listening Port: 22001

**Results:**

The required service is not created by rancher.

You can also create a NodePort for port 22 with a random listening port, then rancher creates a service. Then change the NodePort to 22001 on the workload. Result is that rancher does not update the service.

I would expect that i can use every high port as node port, when specified by hand and not only the port range 30000/32767 that is used for random ports.

<img width="20" height="20" src="../_resources/11514927_s_40_u_03356edf13ba8993_e12429bb40cb4b01a.png"/>](https://github.com/tfiduccia) [tfiduccia](https://github.com/tfiduccia) added <a id="label-490314"></a>[kind/bug](https://github.com/rancher/rancher/labels/kind%2Fbug) <a id="label-6cef62"></a>[area/workload](https://github.com/rancher/rancher/labels/area%2Fworkload) <a id="label-c40ace"></a>[version/2.0](https://github.com/rancher/rancher/labels/version%2F2.0) labels [Jul 3, 2018](#event-1715138875)

<img width="40" height="40" src="../_resources/753917_s_80_u_69bddb249e2d819a58_de5e50a55cda42e29.png"/>](https://github.com/vincent99)

Contributor

### 

**[vincent99](https://github.com/vincent99)** commented <a id="issuecomment-402311587-permalink"></a>[Jul 3, 2018](#issuecomment-402311587)

NodePorts can only be in the range defined for the cluster (which defaults to 30000-32767). You can change the range on the cluster if you want, and you can choose any available port within that range instead or random. But you can't pick a number outside of the range and use that as a NodePort.

<img width="40" height="40" src="../_resources/753917_s_80_u_69bddb249e2d819a58_de5e50a55cda42e29.png"/>](https://github.com/vincent99)

Contributor

### 

**[vincent99](https://github.com/vincent99)** commented <a id="issuecomment-402312212-permalink"></a>[Jul 3, 2018](#issuecomment-402312212)

The UI should prevent you from putting in an out-of-range port, but it needs to [know what the range is first](https://github.com/rancher/rancher/issues/12422#issuecomment-402310902).

<img width="20" height="20" src="../_resources/753917_s_40_u_69bddb249e2d819a58_aa809e4a58db44a19.png"/>](https://github.com/vincent99) [vincent99](https://github.com/vincent99) removed the <a id="label-0817ad"></a>[kind/bug](https://github.com/rancher/rancher/labels/kind%2Fbug) label [Jul 3, 2018](#event-1715149175)

<img width="40" height="40" src="../_resources/21168270_s_80_u_ab757bc7c0e1882e_6c8e566fbd6a44a0b.jpg"/>](https://github.com/loganhz)

### 

**[loganhz](https://github.com/loganhz)** commented <a id="issuecomment-431567411-permalink"></a>[Oct 20, 2018](#issuecomment-431567411)

This issue will be fixed with [#15105](https://github.com/rancher/rancher/issues/15105)

<img width="20" height="20" src="../_resources/21168270_s_40_u_ab757bc7c0e1882e_f12165add1314a02b.jpg"/>](https://github.com/loganhz) [loganhz](https://github.com/loganhz) closed this as [completed](https://github.com/rancher/rancher/issues?q=is%3Aissue+is%3Aclosed+archived%3Afalse+reason%3Acompleted) [Oct 20, 2018](#event-1916146065)

[Sign up for free](https://github.com/join?source=comment-repo) **to join this conversation on GitHub**. Already have an account? [Sign in to comment](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Francher%2Francher%2Fissues%2F14366)

Assignees

No one assigned

Labels

<a id="label-0b31ac"></a>[area/workload](https://github.com/rancher/rancher/labels/area%2Fworkload)

Projects

None yet

Milestone

No milestone

Development

No branches or pull requests

4 participants

 <img width="26" height="26" src="../_resources/97584_s_52_v_4_664a7b05f37540d298e83be23d506441.jpg"/>](https://github.com/dnauck)<img width="26" height="26" src="../_resources/753917_s_52_v_4_3cb0899de23e4c51824cc2d30d38980e.png"/>](https://github.com/vincent99)<img width="26" height="26" src="../_resources/11514927_s_52_v_4_a167abbc945d4271bc85b89deb3f7901.png"/>](https://github.com/tfiduccia)<img width="26" height="26" src="../_resources/21168270_s_52_v_4_759796573afd4b089fd171f465e3d497.jpg"/>](https://github.com/loganhz) 

## Footer

[](https://github.com "GitHub")© 2024 GitHub, Inc.

### Footer navigation

- [Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)
- [Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)
- [Security](https://github.com/security)
- [Status](https://www.githubstatus.com/)
- [Docs](https://docs.github.com/)
- [Contact](https://support.github.com?tags=dotcom-footer)