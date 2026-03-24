---
title: "Domain Name System Nfs Not Allowing Hosts Specif"
category: "networking"
tags: ["networking", "domain", "name", "system", "nfs"]
---

[Skip to main content](#content)

[](#)

1.  [](https://serverfault.com/help "Help centre and other resources")
2.  [](https://stackexchange.com "A list of all 183 Stack Exchange sites")

5.  [Log in](https://serverfault.com/users/login?ssrc=head&returnurl=https%3a%2f%2fserverfault.com%2fquestions%2f1074540%2fnfs-not-allowing-hosts-specified-in-config-to-mount-share)
6.  [Sign up](https://serverfault.com/users/signup?ssrc=head&returnurl=https%3a%2f%2fserverfault.com%2fquestions%2f1074540%2fnfs-not-allowing-hosts-specified-in-config-to-mount-share)

[![Server Fault](../_resources/logo_627efbc59ab74d60a9584fe59c51cb00-1.htm)](https://serverfault.com)

1.  1.  [Home](https://serverfault.com/)
    2.  <a id="nav-questions"></a>[Questions](https://serverfault.com/questions)
    3.  [Tags](https://serverfault.com/tags)
    
    5.  <a id="nav-users"></a>[Users](https://serverfault.com/users)
    6.  <a id="nav-labs-jobs"></a>[Jobs](https://serverfault.com/jobs?source=so-left-nav)
    7.  <a id="nav-companies"></a>[Companies](https://stackoverflow.com/jobs/companies?so_medium=serverfault&so_source=SiteNav)
    8.  <a id="nav-unanswered"></a>[Unanswered](https://serverfault.com/unanswered)
2.  Teams
    
    Now available on Stack Overflow for Teams! AI features where you work: search, IDE, and chat.
    
    [Learn more](https://stackoverflow.co/teams/ai/?utm_medium=referral&utm_source=serverfault-community&utm_campaign=side-bar&utm_content=overflowai-learn-more) [Explore Teams](https://stackoverflow.co/teams/?utm_medium=referral&utm_source=serverfault-community&utm_campaign=side-bar&utm_content=explore-teams)
    

# [NFS not allowing hosts specified in config to mount share](https://serverfault.com/questions/1074540/nfs-not-allowing-hosts-specified-in-config-to-mount-share)

[Ask Question](https://serverfault.com/questions/ask)

Asked 3 years ago

Modified [3 years ago](https://serverfault.com/questions/1074540/?lastactivity "2021-08-14 14:55:46Z")

Viewed 3k times

1

[](https://serverfault.com/posts/1074540/timeline)

I am having an issue where NFS is refusing to allow hosts that are specified in the config file to mount the share.

I am running an NFS server on Debian 10, BTRFS filesystem.

my `/etc/exports` reads:

```
/share  192.220.189.0/24(rw,sync,no_subtree_check) *.domain.lan(rw,sync,no_subtree_check)
```

I am trying to mount from `host.domain.lan`, but when I try to mount the share I get the following:

```
mount.nfs: access denied by server while mounting server.domain.lan:/share
```

The server log reads:

```
rpc.mountd[PID]: refused mount request from <host.domain.lan's ip> for /share (/share): unmatched host
```

I have verified that the server can resolve host.domain.lan's hostname courtesy of a local DNS server.

The mounting DOES work if I explicitly specify `host.domain.lan` in `/etc/exports` as opposed to `*.domain.lan`. This will not do however as I want to serve the folder to an entire subdomain of FQDNs.

I can find nothing about this online, and I have exhausted every option I can think of, please help!

- [domain-name-system](https://serverfault.com/questions/tagged/domain-name-system "show questions tagged 'domain-name-system'")
- [nfs](https://serverfault.com/questions/tagged/nfs "show questions tagged 'nfs'")
- [mount](https://serverfault.com/questions/tagged/mount "show questions tagged 'mount'")
- [internal-dns](https://serverfault.com/questions/tagged/internal-dns "show questions tagged 'internal-dns'")
- [nfs4](https://serverfault.com/questions/tagged/nfs4 "show questions tagged 'nfs4'")

[Share](https://serverfault.com/q/1074540 "Short permalink to this question")

[Improve this question](https://serverfault.com/posts/1074540/edit)

asked Aug 14, 2021 at 7:52

<img width="32" height="32" src="../_resources/MAf25_4cbcfae640ac41f685a7a76fd03295df-1.htm"/>](https://serverfault.com/users/798036/james)

[james](https://serverfault.com/users/798036/james)

113

11 silver badge

55 bronze badges

- Is that your only export?
    
    – [Michael Hampton](https://serverfault.com/users/126632/michael-hampton "249,805 reputation")
    
    [Commented Aug 14, 2021 at 13:03](#comment1400555_1074540)
    
- @MichaelHampton No, I have another export set up exactly like the one in the post.
    
    – [james](https://serverfault.com/users/798036/james "113 reputation")
    
    [Commented Aug 14, 2021 at 16:02](#comment1400583_1074540)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid answering questions in comments.")

<a id="tab-top"></a>

## 1 Answer

Sorted by:

<a id="1074560"></a>

1

[](https://serverfault.com/posts/1074560/timeline)

Likely the domain name is not resolving correctly in DNS.

What do you get if you use the `host` command on the server to try to resolve the client's ip address to a hostname? DNS may not have the correct reverse mapping set up for this to work.

[Share](https://serverfault.com/a/1074560 "Short permalink to this answer")

[Improve this answer](https://serverfault.com/posts/1074560/edit)

answered Aug 14, 2021 at 14:55

<img width="32" height="32" src="../_resources/9b5095c9bb00eab5b0ac41543d62c2a4_635385e435f443519-1.png"/>](https://serverfault.com/users/675696/user10489)

[user10489](https://serverfault.com/users/675696/user10489)

614

11 gold badge

44 silver badges

1414 bronze badges

- It returns `Host not found: 3(NXDOMAIN)`. Which is weird, because if I explicitly specify host.domain.lan, it mounts just fine.
    
    – [james](https://serverfault.com/users/798036/james "113 reputation")
    
    [Commented Aug 14, 2021 at 16:05](#comment1400584_1074560)
    
- It's not weird... it's not even unusual. The name is registered for forward resolution but not reverse resolution. It has to be registered for both directions for this to work.
    
    – [user10489](https://serverfault.com/users/675696/user10489 "614 reputation")
    
    [Commented Aug 14, 2021 at 19:05](#comment1400619_1074560)
    
- Works perfectly after setting up reverse DNS resolution. Thank you! For anyone reading this in the future, when setting up your PTR records, remember to use `host.domain.lan.`, not `host.domain.lan`. Would have saved me hours knowing this.
    
    – [james](https://serverfault.com/users/798036/james "113 reputation")
    
    [Commented Aug 14, 2021 at 19:52](#comment1400622_1074560)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

## You must [log in](https://serverfault.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fserverfault.com%2fquestions%2f1074540) to answer this question.

## 

Not the answer you're looking for? Browse other questions tagged

- [domain-name-system](https://serverfault.com/questions/tagged/domain-name-system "show questions tagged 'domain-name-system'")
- [nfs](https://serverfault.com/questions/tagged/nfs "show questions tagged 'nfs'")
- [mount](https://serverfault.com/questions/tagged/mount "show questions tagged 'mount'")
- [internal-dns](https://serverfault.com/questions/tagged/internal-dns "show questions tagged 'internal-dns'")
- [nfs4](https://serverfault.com/questions/tagged/nfs4 "show questions tagged 'nfs4'")

.

- The Overflow Blog
- [The hidden cost of speed](https://stackoverflow.blog/2024/09/05/the-hidden-cost-of-speed/?cb=1)
    
- [The creator of Jenkins discusses CI/CD and balancing business with open source](https://stackoverflow.blog/2024/09/06//kohsuke-kawaguchi-jenkins-ci-cd-cloudbees/?cb=1)
    
- Featured on Meta
- [Announcing a change to the data-dump process](https://meta.stackexchange.com/questions/401324/announcing-a-change-to-the-data-dump-process?cb=1)
    
- [Bringing clarity to status tag usage on meta sites](https://meta.stackexchange.com/questions/402121/bringing-clarity-to-status-tag-usage-on-meta-sites?cb=1)
    

#### Related

[21](https://serverfault.com/q/200759?rq=1 "Question score (upvotes - downvotes)")[exportfs: Warning: /home/user/share does not support NFS export](https://serverfault.com/questions/200759/exportfs-warning-home-user-share-does-not-support-nfs-export?rq=1)

[5](https://serverfault.com/q/347163?rq=1 "Question score (upvotes - downvotes)")[Mounting NFSv4 share from Debian Linux 6 to Freebsd 9-RC3 "server requires stronger authentication"](https://serverfault.com/questions/347163/mounting-nfsv4-share-from-debian-linux-6-to-freebsd-9-rc3-server-requires-stron?rq=1)

[4](https://serverfault.com/q/364699?rq=1 "Question score (upvotes - downvotes)")[NFS. Non-root mount requests](https://serverfault.com/questions/364699/nfs-non-root-mount-requests?rq=1)

[1](https://serverfault.com/q/444360?rq=1 "Question score (upvotes - downvotes)")[Ubuntu client can't mount Nexenta NFS](https://serverfault.com/questions/444360/ubuntu-client-cant-mount-nexenta-nfs?rq=1)

[5](https://serverfault.com/q/520479?rq=1 "Question score (upvotes - downvotes)")[NFS issue: clients can mount shares as NFSv3 but not as NFSv4 -- or how to debug NFS?](https://serverfault.com/questions/520479/nfs-issue-clients-can-mount-shares-as-nfsv3-but-not-as-nfsv4-or-how-to-debug?rq=1)

[0](https://serverfault.com/q/547512?rq=1 "Question score (upvotes - downvotes)")[NFS host is not exporting the "share"](https://serverfault.com/questions/547512/nfs-host-is-not-exporting-the-share?rq=1)

[1](https://serverfault.com/q/737183?rq=1 "Question score (upvotes - downvotes)")[nfs mount fails due to same file handle](https://serverfault.com/questions/737183/nfs-mount-fails-due-to-same-file-handle?rq=1)

[17](https://serverfault.com/q/825652?rq=1 "Question score (upvotes - downvotes)")[mount.nfs: an incorrect mount option was specified](https://serverfault.com/questions/825652/mount-nfs-an-incorrect-mount-option-was-specified?rq=1)

[1](https://serverfault.com/q/1070210?rq=1 "Question score (upvotes - downvotes)")[Kubernetes can't mount NFS volumes after NFS server update and reboot](https://serverfault.com/questions/1070210/kubernetes-cant-mount-nfs-volumes-after-nfs-server-update-and-reboot?rq=1)

#### [Hot Network Questions](https://stackexchange.com/questions?tab=hot)

- [How to Interpret Statistically Non-Significant Estimates and Rule Out Large Effects?](https://stats.stackexchange.com/questions/653890/how-to-interpret-statistically-non-significant-estimates-and-rule-out-large-effe)
- [What's the benefit or drawback of being Small?](https://rpg.stackexchange.com/questions/213251/whats-the-benefit-or-drawback-of-being-small)
- [Is it helpful to use a thicker gage wire for part of a long circuit run that could have higher loads?](https://diy.stackexchange.com/questions/306528/is-it-helpful-to-use-a-thicker-gage-wire-for-part-of-a-long-circuit-run-that-cou)
- [Star Trek: The Next Generation episode that talks about life and death](https://scifi.stackexchange.com/questions/291347/star-trek-the-next-generation-episode-that-talks-about-life-and-death)
- [Does it make sense for the governments of my world to genetically engineer soldiers?](https://worldbuilding.stackexchange.com/questions/261379/does-it-make-sense-for-the-governments-of-my-world-to-genetically-engineer-soldi)

[more hot questions](#)

[Question feed](https://serverfault.com/feeds/question/1074540 "Feed of this question and its answers")

##### [Server Fault](https://serverfault.com/)

- [Tour](https://serverfault.com/tour)
- [Help](https://serverfault.com/help)
- [Chat](https://chat.stackexchange.com?tab=site&host=serverfault.com)
- [Contact](https://serverfault.com/contact)
- [Feedback](https://meta.serverfault.com)

##### [Company](https://stackoverflow.co/)

- [Stack Overflow](https://stackoverflow.com)
- [Teams](https://stackoverflow.co/teams/)
- [Advertising](https://stackoverflow.co/advertising/)
- [Talent](https://stackoverflow.co/advertising/employer-branding/)
- [About](https://stackoverflow.co/)
- [Press](https://stackoverflow.co/company/press/)
- [Legal](https://stackoverflow.com/legal)
- [Privacy Policy](https://stackoverflow.com/legal/privacy-policy)
- [Terms of Service](https://stackoverflow.com/legal/terms-of-service/public)

- [Cookie Policy](https://stackoverflow.com/legal/cookie-policy)

##### [Stack Exchange Network](https://stackexchange.com)

- [Technology](https://stackexchange.com/sites#technology)
- [Culture & recreation](https://stackexchange.com/sites#culturerecreation)
- [Life & arts](https://stackexchange.com/sites#lifearts)
- [Science](https://stackexchange.com/sites#science)
- [Professional](https://stackexchange.com/sites#professional)
- [Business](https://stackexchange.com/sites#business)
- [API](https://api.stackexchange.com/)
- [Data](https://data.stackexchange.com/)

- [Blog](http://blog.serverfault.com?blb=1)
- [Facebook](https://www.facebook.com/officialstackoverflow/)
- [Twitter](https://twitter.com/stackoverflow)
- [LinkedIn](https://linkedin.com/company/stack-overflow)
- [Instagram](https://www.instagram.com/thestackoverflow)

Site design / logo © 2024 Stack Exchange Inc; user contributions licensed under [CC BY-SA](https://stackoverflow.com/help/licensing) . <a id="svnrev"></a>rev 2024.9.4.14806