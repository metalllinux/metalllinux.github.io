---
title: "Navigation Menu"
category: "general-linux"
tags: ["help", "changing", "service", "node", "port"]
---

[Skip to content](#start-of-content)

## Navigation Menu

[](https://github.com/)

- [Pricing](https://github.com/pricing)

[Sign in](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fk3d-io%2Fk3d%2Fissues%2F186)

[Sign up](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Fvoltron%2Fissues_fragments%2Fissue_layout&source=header-repo&source_repo=k3d-io%2Fk3d)

https://github.com/k3d-io/k3d/issues/186
# \[HELP\] changing service-node-port-range from default brings cluster in "stopped" state #186

Closed

[vldvasi](https://github.com/vldvasi) opened this issue Feb 7, 2020 · 3 comments

Closed

# [\[HELP\] changing service-node-port-range from default brings cluster in "stopped" state](#top) #186

[vldvasi](https://github.com/vldvasi) opened this issue Feb 7, 2020 · 3 comments

## Comments

<img width="40" height="40" src="../_resources/46647774_s_80_u_bce9b750e6d3060e_d207f57a6f1c429eb.jpg"/>](https://github.com/vldvasi)

### 

**[vldvasi](https://github.com/vldvasi)** commented <a id="issue-561644652-permalink"></a>[Feb 7, 2020](#issue-561644652) •

edited

<table class="d-block user-select-contain" data-paste-markdown-skip=""><tbody class="d-block"><tr class="d-block"><td class="d-block comment-body markdown-body  js-comment-body"><p dir="auto"><strong>What did you do?</strong><br>Created a k3d single nod cluster with altered node port ranges using the --server-arg option. Cluster was created successfully but it has a STOPPED state and cannot start it again.</p><ul dir="auto"><li>How was the cluster created?</li></ul><div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate" style="font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;"><code class="notranslate">k3d create --server-arg --kube-apiserver-arg --server-arg --service-node-port-range=20618-20828
INFO[0000] Created cluster network with ID 351307df750188ad375f206da13ed63a02f2823e45ab057d4454583a3fc1dc88 
INFO[0000] Created docker volume  k3d-k3s-default-images 
INFO[0000] Creating cluster [k3s-default]               
INFO[0000] Creating server using docker.io/rancher/k3s:v1.17.2-k3s1... 
INFO[0000] Using registries definitions from "/home/vasilevlad/.k3d/registries.yaml"... 
INFO[0000] SUCCESS: created cluster [k3s-default]       
INFO[0000] You can now use the cluster with:
<!-- -->
export KUBECONFIG="$(k3d get-kubeconfig --name='k3s-default')"
kubectl cluster-info 
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0"><clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0" data-copy-feedback="Copied!" data-tooltip-direction="w" value="k3d create --server-arg --kube-apiserver-arg --server-arg --service-node-port-range=20618-20828
INFO[0000] Created cluster network with ID 351307df750188ad375f206da13ed63a02f2823e45ab057d4454583a3fc1dc88 
INFO[0000] Created docker volume  k3d-k3s-default-images 
INFO[0000] Creating cluster [k3s-default]               
INFO[0000] Creating server using docker.io/rancher/k3s:v1.17.2-k3s1... 
INFO[0000] Using registries definitions from &quot;/home/vasilevlad/.k3d/registries.yaml&quot;... 
INFO[0000] SUCCESS: created cluster [k3s-default]       
INFO[0000] You can now use the cluster with:
<!-- -->
export KUBECONFIG=&quot;$(k3d get-kubeconfig --name='k3s-default')&quot;
kubectl cluster-info " tabindex="0" role="button"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2 joplin-clipper-svg-66" style="width: 16px; height: 16px;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></clipboard-copy></div></div><ul dir="auto"><li>What did you do afterwards?<ul dir="auto"><li>k3d commands?<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate" style="font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;"><code class="notranslate"> export KUBECONFIG="$(k3d get-kubeconfig --name='k3s-default')"
 k3d l
 k3d start
 k3d delete
 k3d create --server-arg --kube-apiserver-arg --server-arg --service-node-port-range --server-arg 20618-20828  &lt;--same STOPPED state
 k3d create --server-arg --kube-apiserver-arg --server-arg --service-node-port-range="20618-20828"   &lt;--same STOPPED state
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0"><clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0" data-copy-feedback="Copied!" data-tooltip-direction="w" value=" export KUBECONFIG=&quot;$(k3d get-kubeconfig --name='k3s-default')&quot;
 k3d l
 k3d start
 k3d delete
 k3d create --server-arg --kube-apiserver-arg --server-arg --service-node-port-range --server-arg 20618-20828  <--same STOPPED state
 k3d create --server-arg --kube-apiserver-arg --server-arg --service-node-port-range=&quot;20618-20828&quot;   <--same STOPPED state" tabindex="0" role="button"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2 joplin-clipper-svg-68" style="width: 16px; height: 16px;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></clipboard-copy></div></div></li><li>docker commands?</li></ul></li></ul><div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate" style="font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;"><code class="notranslate">docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
96623dc797b7        registry:2          "/entrypoint.sh /etc…"   4 hours ago         Up 4 hours          0.0.0.0:5000-&gt;5000/tcp   registry.local
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0"><clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0" data-copy-feedback="Copied!" data-tooltip-direction="w" value="docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
96623dc797b7        registry:2          &quot;/entrypoint.sh /etc…&quot;   4 hours ago         Up 4 hours          0.0.0.0:5000->5000/tcp   registry.local" tabindex="0" role="button"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2 joplin-clipper-svg-70" style="width: 16px; height: 16px;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></clipboard-copy></div></div><div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate" style="font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;"><code class="notranslate">- OS operations (e.g. shutdown/reboot)?
<!-- --> 
  Rebooted the host, no change.
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0"><clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0" data-copy-feedback="Copied!" data-tooltip-direction="w" value="- OS operations (e.g. shutdown/reboot)?
<!-- --> 
  Rebooted the host, no change." tabindex="0" role="button"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2 joplin-clipper-svg-72" style="width: 16px; height: 16px;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></clipboard-copy></div></div><p dir="auto"><strong>What did you expect to happen?</strong><br>Have a running cluster with service nodeport range 20618-20828.</p><p dir="auto"><strong>Screenshots or terminal output</strong><br><a target="_blank" rel="noopener noreferrer nofollow" href="https://user-images.githubusercontent.com/46647774/74032761-70e62900-49bd-11ea-96e7-ecba56c41593.png"><img src="https://user-images.githubusercontent.com/46647774/74032761-70e62900-49bd-11ea-96e7-ecba56c41593.png" alt="image" style="max-width: 100%;" width="806" height="322"></a></p><p dir="auto"><strong>Which OS &amp; Architecture?</strong></p><ul dir="auto"><li>Ubuntu 18.04.4</li></ul><p dir="auto"><strong>Which version of <code class="notranslate">k3d</code>?</strong></p><ul dir="auto"><li>output of <code class="notranslate">k3d --version</code><br><code class="notranslate">k3d version v1.6.0</code></li></ul><p dir="auto"><strong>Which version of docker?</strong></p><ul dir="auto"><li>output of <code class="notranslate">docker version</code></li></ul><div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate" style="font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;"><code class="notranslate">Client:
Version:           18.09.7
API version:       1.39
Go version:        go1.10.1
Git commit:        2d0083d
Built:             Fri Aug 16 14:20:06 2019
OS/Arch:           linux/amd64
Experimental:      false
<!-- -->
Server:
 Engine:
  Version:          18.09.7
  API version:      1.39 (minimum version 1.12)
  Go version:       go1.10.1
  Git commit:       2d0083d
  Built:            Wed Aug 14 19:41:23 2019
  OS/Arch:          linux/amd64
  Experimental:     false
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0"><clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0" data-copy-feedback="Copied!" data-tooltip-direction="w" value="Client:
Version:           18.09.7
API version:       1.39
Go version:        go1.10.1
Git commit:        2d0083d
Built:             Fri Aug 16 14:20:06 2019
OS/Arch:           linux/amd64
Experimental:      false
<!-- -->
Server:
 Engine:
  Version:          18.09.7
  API version:      1.39 (minimum version 1.12)
  Go version:       go1.10.1
  Git commit:       2d0083d
  Built:            Wed Aug 14 19:41:23 2019
  OS/Arch:          linux/amd64
  Experimental:     false" tabindex="0" role="button"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2 joplin-clipper-svg-74" style="width: 16px; height: 16px;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></clipboard-copy></div></div></td></tr></tbody></table>

<img width="20" height="20" src="../_resources/46647774_s_40_u_bce9b750e6d3060e_be84085f96ed47159.jpg"/>](https://github.com/vldvasi) [vldvasi](https://github.com/vldvasi) added the <a id="label-16215f"></a>[bug](https://github.com/k3d-io/k3d/labels/bug) label [Feb 7, 2020](#event-3017686476)

<img width="40" height="40" src="../_resources/25345277_s_80_u_a0fd1ee2a615e6eb_a0d2aff141f149e1a.png"/>](https://github.com/iwilltry42)

Member

### 

**[iwilltry42](https://github.com/iwilltry42)** commented <a id="issuecomment-583978871-permalink"></a>[Feb 10, 2020](#issuecomment-583978871)

Hi [@vldvasi](https://github.com/vldvasi) , thanks for opening this issue.  
Fortunately, this is not a bug, but rather a misunderstanding in how the flags are being used.  
With the command line that you used, you'll get the following error log (see `docker logs k3d-k3s-default-server`): `apiserver exited: bad flag syntax: ----service-node-port-range=20618-20828`  
\-> `--server-arg` is a k3d flag which passes the parameter to the k3s server, so `--kube-apiserver-arg='service-node-port-range=20618-20828'` would be a single parameter for it to work.

Here's the command line that works: `k3d create --server-arg --kube-apiserver-arg='service-node-port-range=20618-20828'`

<img width="20" height="20" src="../_resources/25345277_s_40_u_a0fd1ee2a615e6eb_8754e329f03c4a45a.png"/>](https://github.com/iwilltry42) [iwilltry42](https://github.com/iwilltry42) self-assigned this [Feb 10, 2020](#event-3021487783)

<img width="20" height="20" src="../_resources/25345277_s_40_u_a0fd1ee2a615e6eb_8754e329f03c4a45a.png"/>](https://github.com/iwilltry42)[iwilltry42](https://github.com/iwilltry42) added <a id="label-02e3c4"></a>[help](https://github.com/k3d-io/k3d/labels/help) <a id="label-b2942b"></a>[not a bug](https://github.com/k3d-io/k3d/labels/not%20a%20bug) labels [Feb 10, 2020](#event-3021488058)

<img width="20" height="20" src="../_resources/25345277_s_40_u_a0fd1ee2a615e6eb_8754e329f03c4a45a.png"/>](https://github.com/iwilltry42)[iwilltry42](https://github.com/iwilltry42) changed the title ~~\[BUG\] changing service-node-port-range from default brings cluster in "stopped" state~~ <ins>\[HELP\] changing service-node-port-range from default brings cluster in "stopped" state</ins> [Feb 10, 2020](#event-3021488297)

<img width="40" height="40" src="../_resources/46647774_s_80_u_bce9b750e6d3060e_d207f57a6f1c429eb.jpg"/>](https://github.com/vldvasi)

Author

### 

**[vldvasi](https://github.com/vldvasi)** commented <a id="issuecomment-583993834-permalink"></a>[Feb 10, 2020](#issuecomment-583993834)

Thanks a million [@iwilltry42](https://github.com/iwilltry42), I confirm its working also if I found that if I pass parameters as below seem to be working:  
`k3d create --server-arg --kube-apiserver-arg --server-arg service-node-port-range=20618-20828`

<img width="20" height="20" src="../_resources/46647774_s_40_u_bce9b750e6d3060e_be84085f96ed47159.jpg"/>](https://github.com/vldvasi) [vldvasi](https://github.com/vldvasi) closed this as [completed](https://github.com/k3d-io/k3d/issues?q=is%3Aissue+is%3Aclosed+archived%3Afalse+reason%3Acompleted) [Feb 10, 2020](#event-3021609548)

<img width="40" height="40" src="../_resources/25345277_s_80_u_a0fd1ee2a615e6eb_a0d2aff141f149e1a.png"/>](https://github.com/iwilltry42)

Member

### 

**[iwilltry42](https://github.com/iwilltry42)** commented <a id="issuecomment-584001784-permalink"></a>[Feb 10, 2020](#issuecomment-584001784)

Makes sense, since they're just appended in k3d and passed on to k3s. It's k3s that assumes that you're not passing in the leading `--` for flags passed on to the API-Server (same for kubelet, etc.).  
Glad that it works now for you :)

[Sign up for free](https://github.com/join?source=comment-repo) **to join this conversation on GitHub**. Already have an account? [Sign in to comment](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fk3d-io%2Fk3d%2Fissues%2F186)

Assignees

 <img width="20" height="20" src="../_resources/25345277_s_40_v_4_a235329439c84d08a726e5a4d96dbdcf.png"/>](https://github.com/iwilltry42)[iwilltry42](https://github.com/iwilltry42)

Labels

<a id="label-7c181d"></a>[bug](https://github.com/k3d-io/k3d/labels/bug) <a id="label-e0e796"></a>[help](https://github.com/k3d-io/k3d/labels/help) <a id="label-8db8fd"></a>[not a bug](https://github.com/k3d-io/k3d/labels/not%20a%20bug)

Projects

None yet

Milestone

No milestone

Development

No branches or pull requests

2 participants

 <img width="26" height="26" src="../_resources/25345277_s_52_v_4_11347b74efb34ca8a3e9ee78aed71786.png"/>](https://github.com/iwilltry42)<img width="26" height="26" src="../_resources/46647774_s_52_v_4_8c7b754385334498ba0f041537d93afc.jpg"/>](https://github.com/vldvasi) 

## Footer

[](https://github.com "GitHub")© 2024 GitHub, Inc.

### Footer navigation

- [Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)
- [Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)
- [Security](https://github.com/security)
- [Status](https://www.githubstatus.com/)
- [Docs](https://docs.github.com/)
- [Contact](https://support.github.com?tags=dotcom-footer)