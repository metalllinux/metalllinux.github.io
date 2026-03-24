---
title: "How Do Ulimit Settings Impact Linux Server Faul"
category: "general-linux"
tags: ["ulimit", "settings", "impact", "linux", "server"]
---

[Skip to main content](#content)

[](#)

1.  [](https://serverfault.com/help "Help centre and other resources")
2.  [](https://stackexchange.com "A list of all 183 Stack Exchange sites")

5.  [Log in](https://serverfault.com/users/login?ssrc=head&returnurl=https%3a%2f%2fserverfault.com%2fquestions%2f773609%2fhow-do-ulimit-settings-impact-linux)
6.  [Sign up](https://serverfault.com/users/signup?ssrc=head&returnurl=https%3a%2f%2fserverfault.com%2fquestions%2f773609%2fhow-do-ulimit-settings-impact-linux)

[![Server Fault](../_resources/logo_7506a7bcedf24c7eb81392f97a7164b0.htm)](https://serverfault.com)

1.  1.  [Home](https://serverfault.com/)
    2.  <a id="nav-questions"></a>[Questions](https://serverfault.com/questions)
    3.  <a id="nav-unanswered"></a>[Unanswered](https://serverfault.com/unanswered)
    4.  [Tags](https://serverfault.com/tags)
    
    6.  <a id="nav-users"></a>[Users](https://serverfault.com/users)
    
    8.  <a id="nav-companies"></a>[Companies](https://stackoverflow.com/jobs/companies?so_medium=serverfault&so_source=SiteNav)
2.  Teams
    
    <img width="140" height="24" src="../_resources/teams-promo_a5e4288be07346cab2f73c2c55c6ba59.htm"/>
    
    Ask questions, find answers and collaborate at work with Stack Overflow for Teams.
    
    [Try Teams for free](https://stackoverflowteams.com/teams/create/free/?utm_medium=referral&utm_source=serverfault-community&utm_campaign=side-bar&utm_content=explore-teams) [Explore Teams](https://stackoverflow.co/teams/?utm_medium=referral&utm_source=serverfault-community&utm_campaign=side-bar&utm_content=explore-teams)
    

# [How do ulimit settings impact Linux?](https://serverfault.com/questions/773609/how-do-ulimit-settings-impact-linux)

[Ask Question](https://serverfault.com/questions/ask)

Asked 8 years, 11 months ago

Modified [5 years, 7 months ago](https://serverfault.com/questions/773609/?lastactivity "2019-08-30 20:41:35Z")

Viewed 38k times

11

[](https://serverfault.com/posts/773609/timeline)

Lately, I had a `EAGAIN` error with some async code that made me take a closer look at `ulimit` settings. While I clearly understand certain limits, such as `nofile`, others are still quite confused to me.

It's quite easy to find resources on how to set those, but I couldn't find any article explaining precisely what each setting is about and how that could impact the system.

Definition taken from `/etc/security/limits.conf` is not really self-explanatory:

```
- core - limits the core file size (KB)
- data - max data size (KB)
- fsize - maximum filesize (KB)
- memlock - max locked-in-memory address space (KB)
- nofile - max number of open files
- rss - max resident set size (KB)
- stack - max stack size (KB)
- cpu - max CPU time (MIN)
- nproc - max number of processes
- as - address space limit (KB)
- maxlogins - max number of logins for this user
- maxsyslogins - max number of logins on the system
- priority - the priority to run user process with
- locks - max number of file locks the user can hold
- sigpending - max number of pending signals
- msgqueue - max memory used by POSIX message queues (bytes)
- nice - max nice priority allowed to raise to values: [-20, 19]
- rtprio - max realtime priority
- chroot - change root to directory (Debian-specific)
```

So I'd be glad if someone could enlighten me on those rather important Linux settings!

The error I face is actually:

```
{ [Error: spawn mediainfo EAGAIN]
  code: 'EAGAIN',
  errno: 'EAGAIN',
  syscall: 'spawn mediainfo',
  path: 'mediainfo',
  spawnargs: 
   [ '--Output=XML',
     '/home/buzut/testMedia' ],
  cmd: 'mediainfo --Output=XML /home/buzut/testMedia' }
```

As per the definition on [gnu.org](http://www.gnu.org/software/libc/manual/html_node/Error-Codes.html):

> An operation that would block was attempted on an object that has non-blocking mode selected. Trying the same operation again will block until some external condition makes it possible to read, write, or connect (whatever the operation).

I understand that `EAGAIN` error refers to a resource that is temporarily not available. It wouldn't be wise to set all parameters to `unlimited`. Thus I would understand the implication of which params to identify the one blocking and adjust – `ulimit` settings, my code or both – accordingly.

Here are my current limits:

```
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 127698
max locked memory       (kbytes, -l) 64
max memory size         (kbytes, -m) unlimited
open files                      (-n) 64000
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 127698
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
```

- [linux](https://serverfault.com/questions/tagged/linux "show questions tagged 'linux'")
- [ulimit](https://serverfault.com/questions/tagged/ulimit "show questions tagged 'ulimit'")

[Share](https://serverfault.com/q/773609 "Short permalink to this question")

[Improve this question](https://serverfault.com/posts/773609/edit)

[edited Jul 7, 2016 at 20:51](https://serverfault.com/posts/773609/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/1fb33c0507faeb381309536779716850_c7db5b4d31424931a.png"/>](https://serverfault.com/users/3038/sysadmin1138)

[sysadmin1138](https://serverfault.com/users/3038/sysadmin1138)♦

136k

1919 gold badges

183183 silver badges

306306 bronze badges

asked Apr 28, 2016 at 14:38

<img width="32" height="32" src="../_resources/SWDAg_908a0bf16b554bcea0b6c94c2360a578.htm"/>](https://serverfault.com/users/145978/buzut)

[Buzut](https://serverfault.com/users/145978/buzut)

895

33 gold badges

1111 silver badges

2323 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid answering questions in comments.")

<a id="tab-top"></a>

## 2 Answers

Sorted by:

<a id="773734"></a>

20

[](https://serverfault.com/posts/773734/timeline)

I have made my homework and (almost) found what each option does. Also, I've noted that there is more options in `/etc/security/limits.conf` than it appears with `ulimit -a`. Therefore, I've only documented the latter here. Of course, everyone is invited to enrich this answer!

- **core file size** (blocks, -c)
    
    The maximum size of core files created. Core dump is a system snapshot (RAM + context switch + processor registers).
    
    https://en.wikipedia.org/wiki/Core_dump
    

* * *

- **data seg size** (kbytes, -d)
    
    The maximum size of a process's data segment. a data segment is a portion of an object file or the corresponding virtual address space of a program that contains initialised static variables.
    
    https://en.wikipedia.org/wiki/Data_segment
    

* * *

- **scheduling priority** (-e)
    
    The maximum scheduling priority ("nice") a process can be given.
    
    https://en.wikipedia.org/wiki/Scheduling_%28computing%29
    

* * *

- **file size** (blocks, -f)
    
    The maximum size of files written by the shell and its children.
    

* * *

- **pending signals** (-i)
    
    Set of signals that are pending for delivery to the calling thread.
    
    https://unix.stackexchange.com/questions/197600/what-are-pending-signals
    

* * *

- **max locked memory** (kbytes, -l)
    
    The maximum size that may be locked into memory. Memory locking ensures the memory is always in RAM and never moved to the swap disk.
    
    https://stackoverflow.com/questions/9818755/why-would-we-need-to-lock-a-processs-address-space-in-ram
    

* * *

- **max memory size** (kbytes, -m)
    
    How much memory a process currently has in main memory (RAM), opposed to how much virtual memory the process has in total.
    
    https://en.wikipedia.org/wiki/Resident_set_size
    

* * *

- **open files** (-n)
    
    The maximum number of open file descriptors. A file descriptor is an abstract indicator used to access a file or other input/output resource, such as a pipe or network socket.
    
    https://en.wikipedia.org/wiki/File_descriptor
    
    List file descriptors: http://www.cyberciti.biz/tips/linux-procfs-file-descriptors.html
    

* * *

- **pipe size** (512 bytes, -p)
    
    Pipe's internal buffer size. See "pipe capacity" section in http://man7.org/linux/man-pages/man7/pipe.7.html
    

* * *

- **POSIX message queues** (bytes, -q)
    
    The maximum number of bytes in POSIX message queues. POSIX message queues allow processes to exchange data in the form of messages.
    
    http://linux.die.net/man/7/mq_overview
    
    Message queues in general https://en.wikipedia.org/wiki/Message_queue
    

* * *

- **real-time priority** (-r)
    
    The maximum real-time scheduling priority. A realtime priority thread can never be pre-empted by timer interrupts and runs at a higher priority than any other thread in the system.
    
    https://stackoverflow.com/questions/1663993/what-is-the-realtime-setting-for-for-process-priority
    

* * *

- **stack size** (kbytes, -s)
    
    The maximum stack size. The stack size is a reserved region of memory that is used to store the location of function calls in order to allow return statements to return to the correct location.
    
    https://en.wikipedia.org/wiki/Stack-based_memory_allocation
    

* * *

- **cpu time** (seconds, -t)
    
    The maximum amount of cpu time in seconds.
    
    https://en.wikipedia.org/wiki/CPU_time
    

* * *

- **max user processes** (-u)
    
    The maximum number of processes a user can start or fork.
    
    https://en.wikipedia.org/wiki/Process_%28computing%29
    
    This command shows how much processes each user is currently using:
    
    `ps h -Led -o user | sort | uniq -c | sort -n`
    

* * *

- **virtual memory** (kbytes, -v)
    
    The maximum amount of virtual memory available to the shell. Virtual memory maps memory addresses used by a program, called virtual addresses, into physical addresses in computer memory.
    
    https://en.wikipedia.org/wiki/Virtual_memory
    

* * *

- **file locks** (-x)
    
    File locking is a mechanism that restricts access to a computer file by allowing only one user or process access at any specific time.
    
    https://en.wikipedia.org/wiki/File_locking
    

[Share](https://serverfault.com/a/773734 "Short permalink to this answer")

[Improve this answer](https://serverfault.com/posts/773734/edit)

[edited Aug 30, 2019 at 20:41](https://serverfault.com/posts/773734/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/0fbe98c44d4b70bf9c9b5b824d4d496b_470dcece37c848d4a.png"/>](https://serverfault.com/users/537813/mopurizwarriors)

[mopurizwarriors](https://serverfault.com/users/537813/mopurizwarriors)

3

33 bronze badges

answered Apr 28, 2016 at 21:42

<img width="32" height="32" src="../_resources/SWDAg_908a0bf16b554bcea0b6c94c2360a578.htm"/>](https://serverfault.com/users/145978/buzut)

[Buzut](https://serverfault.com/users/145978/buzut)

895

33 gold badges

1111 silver badges

2323 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="773613"></a>

1

[](https://serverfault.com/posts/773613/timeline)

As you didn't mention what's your exact problem with limitation in Linux so it would be hard to fix it. You use `ulimit -a` for check all of you limitation in OS. Also you can change every limitation you have ( you can decrease it not increase except root can do anything ) Try to look at `man ulimit` to find out which option you need to change.

[Share](https://serverfault.com/a/773613 "Short permalink to this answer")

[Improve this answer](https://serverfault.com/posts/773613/edit)

answered Apr 28, 2016 at 14:44

<img width="32" height="32" src="../_resources/OK8Zz_51f5396ceb9b4d559104243fdc2fcecc.htm"/>](https://serverfault.com/users/351937/ali-ghasempour)

[Ali Ghasempour](https://serverfault.com/users/351937/ali-ghasempour)

111

22 bronze badges

- I edited my question to make my problem clearer. But beside that, I'd be glad to know which param does what (like `nofile` is the number of files a given user can have open simultaneously)!
    
    – [Buzut](https://serverfault.com/users/145978/buzut "895 reputation")
    
    [Commented Apr 28, 2016 at 15:09](#comment975600_773613)
    
- `Unlimited` didn't fix your problem ?
    
    – [Ali Ghasempour](https://serverfault.com/users/351937/ali-ghasempour "111 reputation")
    
    [Commented Apr 28, 2016 at 15:33](#comment975608_773613)
    
- I didn't try `unlimited` so far. I changed `nofiles` from `1024` to `64000`, but it didn't solve my problem. And I'd rather not change what I don't understand. And clearly, I don't know what others do…
    
    – [Buzut](https://serverfault.com/users/145978/buzut "895 reputation")
    
    [Commented Apr 28, 2016 at 15:39](#comment975611_773613)
    
- 1
    
    Only option you shouldn't change is `core` !!! Core is env + bug log of applications. Put it on default (zero ) if you don't your disk will be full soon. First check your limitation `ulimit -a` then try `unlimited`
    
    – [Ali Ghasempour](https://serverfault.com/users/351937/ali-ghasempour "111 reputation")
    
    [Commented Apr 28, 2016 at 15:42](#comment975613_773613)
    
- 1
    
    I don't know what kind of resource you mean but options `cpu` ( how much user take CPU for its process ) and `nproc` ( max number of process user can make or fork ) . Hope these will help you. Have fun ;)
    
    – [Ali Ghasempour](https://serverfault.com/users/351937/ali-ghasempour "111 reputation")
    
    [Commented Apr 28, 2016 at 16:10](#comment975623_773613)
    

[Show **2** more comments](# "Expand to show all comments on this post")

## You must [log in](https://serverfault.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fserverfault.com%2fquestions%2f773609) to answer this question.

Start asking to get answers

Find the answer to your question by asking.

[Ask question](https://serverfault.com/questions/ask)

Explore related questions

- [linux](https://serverfault.com/questions/tagged/linux "show questions tagged 'linux'")
- [ulimit](https://serverfault.com/questions/tagged/ulimit "show questions tagged 'ulimit'")

See similar questions with these tags.

- The Overflow Blog
- [How do you fact-check an AI?](https://stackoverflow.blog/2025/04/11/how-do-you-fact-check-an-ai/?cb=1)
    
- Featured on Meta
- [Changes to reporting for the \[status-review\] escalation process](https://meta.stackexchange.com/questions/407927/changes-to-reporting-for-the-status-review-escalation-process?cb=1)
    

#### Related

[1506](https://serverfault.com/q/62411?rq=1 "Question score (upvotes - downvotes)")[How can I sort du -h output by size](https://serverfault.com/questions/62411/how-can-i-sort-du-h-output-by-size?rq=1)

[409](https://serverfault.com/q/112795?rq=1 "Question score (upvotes - downvotes)")[How to run a server on port 80 as a normal user on Linux?](https://serverfault.com/questions/112795/how-to-run-a-server-on-port-80-as-a-normal-user-on-linux?rq=1)

[1](https://serverfault.com/q/324336?rq=1 "Question score (upvotes - downvotes)")[What are some basic ulimit settings for a student shared server?](https://serverfault.com/questions/324336/what-are-some-basic-ulimit-settings-for-a-student-shared-server?rq=1)

[45](https://serverfault.com/q/356962?rq=1 "Question score (upvotes - downvotes)")[where are the default ulimit values set? (linux, centos)](https://serverfault.com/questions/356962/where-are-the-default-ulimit-values-set-linux-centos?rq=1)

[1](https://serverfault.com/q/426321?rq=1 "Question score (upvotes - downvotes)")[Ulimit settings in Oracle 11g on Linux 5](https://serverfault.com/questions/426321/ulimit-settings-in-oracle-11g-on-linux-5?rq=1)

[2](https://serverfault.com/q/520975?rq=1 "Question score (upvotes - downvotes)")[10GbE be2net low pktgen performance](https://serverfault.com/questions/520975/10gbe-be2net-low-pktgen-performance?rq=1)

[28](https://serverfault.com/q/610130?rq=1 "Question score (upvotes - downvotes)")[How to set ulimit value permanently?](https://serverfault.com/questions/610130/how-to-set-ulimit-value-permanently?rq=1)

[0](https://serverfault.com/q/715241?rq=1 "Question score (upvotes - downvotes)")[PHP Sockets. Better on multiple ports or not?](https://serverfault.com/questions/715241/php-sockets-better-on-multiple-ports-or-not?rq=1)

[0](https://serverfault.com/q/731283?rq=1 "Question score (upvotes - downvotes)")[Trying to understand sysbench](https://serverfault.com/questions/731283/trying-to-understand-sysbench?rq=1)

[1](https://serverfault.com/q/1166477?rq=1 "Question score (upvotes - downvotes)")[Coredump file not generating](https://serverfault.com/questions/1166477/coredump-file-not-generating?rq=1)

#### [Hot Network Questions](https://stackexchange.com/questions?tab=hot)

- [Avoiding alligators with primitive technology?](https://worldbuilding.stackexchange.com/questions/265871/avoiding-alligators-with-primitive-technology)
- [Is John Brandenburg affiliated with Harvard University?](https://skeptics.stackexchange.com/questions/57822/is-john-brandenburg-affiliated-with-harvard-university)
- [How to make chocolate easter egg without a mould?](https://cooking.stackexchange.com/questions/130461/how-to-make-chocolate-easter-egg-without-a-mould)
- [Unexpected results when mixing highly concentrated CuCl2 with Al foil](https://chemistry.stackexchange.com/questions/188307/unexpected-results-when-mixing-highly-concentrated-cucl2-with-al-foil)
- [Difference in weights between two submerged objects](https://physics.stackexchange.com/questions/847515/difference-in-weights-between-two-submerged-objects)
- [Why exactly is the Riemann integral not adequate for representing linear functionals?](https://math.stackexchange.com/questions/5055514/why-exactly-is-the-riemann-integral-not-adequate-for-representing-linear-functio)
- [Is there a common description of the way Trump pronounces things he doesn't like?](https://english.stackexchange.com/questions/630780/is-there-a-common-description-of-the-way-trump-pronounces-things-he-doesnt-like)
- [How to apply the libertine font to a specific range in pdfLaTeX?](https://tex.stackexchange.com/questions/740735/how-to-apply-the-libertine-font-to-a-specific-range-in-pdflatex)
- [Should I be worried about this heat shield damage?](https://mechanics.stackexchange.com/questions/98864/should-i-be-worried-about-this-heat-shield-damage)
- [How can I replace one space with N spaces?](https://superuser.com/questions/1891475/how-can-i-replace-one-space-with-n-spaces)
- [If Jesus knew all about the fig tree, why was he ignorant about it not being in season? Matthew 21:18-20 cf. Matthew 24:32-33](https://hermeneutics.stackexchange.com/questions/103175/if-jesus-knew-all-about-the-fig-tree-why-was-he-ignorant-about-it-not-being-in)
- [Can we slightly modify the Schwarzschild metric to describe an evaporating black hole, and what would the geodesic be like?](https://physics.stackexchange.com/questions/847560/can-we-slightly-modify-the-schwarzschild-metric-to-describe-an-evaporating-black)
- [How do astronomers know that two objects appearing near one another are in fact close?](https://astronomy.stackexchange.com/questions/60014/how-do-astronomers-know-that-two-objects-appearing-near-one-another-are-in-fact)
- [How is maximum age handled in templated creatures?](https://rpg.stackexchange.com/questions/215244/how-is-maximum-age-handled-in-templated-creatures)
- [Are there any documented cases where Percival Treite committed any procedures that led to death?](https://history.stackexchange.com/questions/77682/are-there-any-documented-cases-where-percival-treite-committed-any-procedures-th)
- [Is the development of AI inevitable?](https://philosophy.stackexchange.com/questions/124168/is-the-development-of-ai-inevitable)
- [Should I use page numbers when citing information from physics papers?](https://academia.stackexchange.com/questions/217866/should-i-use-page-numbers-when-citing-information-from-physics-papers)
- [Writing Without Overplanning: How?](https://writing.stackexchange.com/questions/71191/writing-without-overplanning-how)
- [Merging sublists together based upon element criteria](https://mathematica.stackexchange.com/questions/312090/merging-sublists-together-based-upon-element-criteria)
- [Asymptotics of alternating sum of squared binomials by contour integration](https://mathoverflow.net/questions/490930/asymptotics-of-alternating-sum-of-squared-binomials-by-contour-integration)
- [Why is my new bike so slow](https://bicycles.stackexchange.com/questions/96531/why-is-my-new-bike-so-slow)
- [Does time dilation affect the date when arriving at a destination?](https://worldbuilding.stackexchange.com/questions/265856/does-time-dilation-affect-the-date-when-arriving-at-a-destination)
- [Which Hyrule Compendium entries can be missed?](https://gaming.stackexchange.com/questions/411849/which-hyrule-compendium-entries-can-be-missed)
- [Why is mechanical energy lost and linear momentum not conserved when a string suddenly becomes taut in a vertical two-mass system?](https://physics.stackexchange.com/questions/847452/why-is-mechanical-energy-lost-and-linear-momentum-not-conserved-when-a-string-su)

[Question feed](https://serverfault.com/feeds/question/773609 "Feed of this question and its answers")

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

Site design / logo © 2025 Stack Exchange Inc; user contributions licensed under [CC BY-SA](https://stackoverflow.com/help/licensing) . <a id="svnrev"></a>rev 2025.4.9.24965

By clicking “Accept all cookies”, you agree Stack Exchange can store cookies on your device and disclose information in accordance with our [Cookie Policy](https://stackoverflow.com/legal/cookie-policy).