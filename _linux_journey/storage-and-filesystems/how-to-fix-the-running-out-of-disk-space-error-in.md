---
title: "How To Fix The Running Out Of Disk Space Error In"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "fix", "running", "out", "disk"]
---

[Skip to main content](#content)

[Stack Overflow](https://stackoverflow.com)

1.  [About](https://stackoverflow.co/)
2.  [Products](#)
3.  [OverflowAI](https://stackoverflow.co/teams/ai/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav-bar&utm_content=overflowai)

3.  [Log in](https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f51238891%2fhow-to-fix-the-running-out-of-disk-space-error-in-docker)
4.  [Sign up](https://stackoverflow.com/users/signup?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f51238891%2fhow-to-fix-the-running-out-of-disk-space-error-in-docker)

1.  1.  [Home](https://stackoverflow.com/)
    2.  <a id="nav-questions"></a>[Questions](https://stackoverflow.com/questions)
    3.  [Tags](https://stackoverflow.com/tags)
    
    5.  <a id="nav-users"></a>[Users](https://stackoverflow.com/users)
    6.  <a id="nav-companies"></a>[Companies](https://stackoverflow.com/jobs/companies?so_medium=stackoverflow&so_source=SiteNav)
    7.  Labs
    8.  <a id="nav-labs-jobs"></a>[Jobs](https://stackoverflow.com/jobs?source=so-left-nav)
    9.  <a id="nav-labs-discussions"></a>[Discussions](https://stackoverflow.com/beta/discussions)
    10. Recent Tags
        
    11. [docker](https://stackoverflow.com/questions/tagged/docker)
    12. [docker-machine](https://stackoverflow.com/questions/tagged/docker-machine)
    13. [centos](https://stackoverflow.com/questions/tagged/centos)
    14. Collectives
        
    15. Communities for your favourite technologies. [Explore all Collectives](https://stackoverflow.com/collectives-all)
        
2.  Teams
    
    Now available on Stack Overflow for Teams! AI features where you work: search, IDE, and chat.
    
    [Learn more](https://stackoverflow.co/teams/ai/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=overflowai-learn-more) [Explore Teams](https://stackoverflow.co/teams/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams)
    

# [How to fix the running out of disk space error in Docker?](https://stackoverflow.com/questions/51238891/how-to-fix-the-running-out-of-disk-space-error-in-docker)

[Ask Question](https://stackoverflow.com/questions/ask)

Asked 6 years, 2 months ago

Modified [1 month ago](https://stackoverflow.com/questions/51238891/?lastactivity "2024-07-18 03:57:05Z")

Viewed 135k times

71

[](https://stackoverflow.com/posts/51238891/timeline)

When I am trying to build the docker image I am getting out of disk space error and after investigating I find the following:

```
df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/vda1        4G   3.8G     0 100% /
```

How do I fix this out of space error?

- [docker](https://stackoverflow.com/questions/tagged/docker "show questions tagged 'docker'")
- [docker-machine](https://stackoverflow.com/questions/tagged/docker-machine "show questions tagged 'docker-machine'")

[Share](https://stackoverflow.com/q/51238891 "Short permalink to this question")

[Improve this question](https://stackoverflow.com/posts/51238891/edit)

[edited Jul 10, 2018 at 8:27](https://stackoverflow.com/posts/51238891/revisions "show all edits to this post")

asked Jul 9, 2018 at 5:46

<img width="32" height="32" src="../_resources/TgQ5O_76393f9a131f443cbc2d5c93ffc0f0f6-1.htm"/>](https://stackoverflow.com/users/1475228/pritam-banerjee)

[Pritam Banerjee](https://stackoverflow.com/users/1475228/pritam-banerjee)

18.8k

1010 gold badges

9696 silver badges

110110 bronze badges

- 6
    
    There's no error here, just the output of `df -h`. Also when you say "memory" you probably mean "disk space"?
    
    – [jannis](https://stackoverflow.com/users/4494577/jannis "5,190 reputation")
    
    [Commented Jul 9, 2018 at 7:41](#comment89459438_51238891)
    
- 2
    
    Here solution: **[stackoverflow.com/questions/25713773](https://stackoverflow.com/questions/25713773/)**
    
    – [T.Todua](https://stackoverflow.com/users/2377343/t-todua "55,730 reputation")
    
    [Commented Jun 26, 2019 at 9:54](#comment100095542_51238891)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid answering questions in comments.")

<a id="tab-top"></a>

## 12 Answers

Sorted by:

<a id="51242704"></a>

130

[](https://stackoverflow.com/posts/51242704/timeline)

```
docker system prune [-a]
```

https://docs.docker.com/engine/reference/commandline/system_prune/

This will clean up all images, containers, networks, volumes not used. We generally try to clean up old images when creating a new one but you could also have this run as a scheduled task on your docker server every day.

Other answers address listing system memory usage and increasing the amount of Docker disk space in Docker Desktop:

> The `docker system df` command can be used to view reclaimable memory --Abishek_Jain

> Open up the docker settings -> Resources -> Advanced and up the amount of Hard Drive space it can use under disk image size. --Nico

[Share](https://stackoverflow.com/a/51242704 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/51242704/edit)

[edited Dec 13, 2023 at 21:30](https://stackoverflow.com/posts/51242704/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/6c6205448de1b8ad8d5baf0f3416d899_e16e42b86e2b4ea18-1.png"/>](https://stackoverflow.com/users/13969/rjurney)

[rjurney](https://stackoverflow.com/users/13969/rjurney)

5,088

55 gold badges

4242 silver badges

6464 bronze badges

answered Jul 9, 2018 at 9:55

<img width="32" height="32" src="../_resources/690cb84d0ee26d129ad947a2421384e1_bce70d65a759407a9-1.png"/>](https://stackoverflow.com/users/1794961/nick-spicer)

[Nick Spicer](https://stackoverflow.com/users/1794961/nick-spicer)

2,617

44 gold badges

2222 silver badges

2626 bronze badges

- 26
    
    You need to pass the `--volumes` flag to prune the volumes as well. Without this only 'unused containers, networks, images (both dangling and unreferenced)' will be pruned.
    
    – [jannis](https://stackoverflow.com/users/4494577/jannis "5,190 reputation")
    
    [Commented Jul 27, 2018 at 8:28](#comment90074611_51242704)
    
- 2
    
    I feel that this is only a temporary solution. We have over 14Gb free disk space and Docker still says that no space is left. We called "docker system prune" and it worked, but only for a while. Not to mention that the database was deleted as well but thats our fault (always make regular backups people!)
    
    – [Ziga Petek](https://stackoverflow.com/users/430997/ziga-petek "4,112 reputation")
    
    [Commented Oct 4, 2019 at 7:07](#comment102836917_51242704)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="53143653"></a>

30

[](https://stackoverflow.com/posts/53143653/timeline)

use command - `docker system prune -a` This will clean up total Reclaimable Sise for Images, Network & Volume..... This will remove all images related reclaimable space which are not associated with any running container.....

Run `docker system df` command to view Reclaimable memory

In case there is some Reclaimable memory then if above command does not work in first go then run the same command twice then it should cleaned up.... I have been experiencing this behaviour almost on daily basis..... Planning to report this bug to Docker Community but before that want to reproduce this bug with new release to see if this has been fixed or not with latest one....

[Share](https://stackoverflow.com/a/53143653 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/53143653/edit)

[edited Nov 2, 2022 at 5:56](https://stackoverflow.com/posts/53143653/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/N8Jbo_71b468320589430f8f3e187172113a1c-1.htm"/>](https://stackoverflow.com/users/2458858/tryingtolearn)

[tryingToLearn](https://stackoverflow.com/users/2458858/tryingtolearn)

11.5k

1212 gold badges

8484 silver badges

126126 bronze badges

answered Nov 4, 2018 at 17:46

<img width="32" height="32" src="../_resources/photo_c2b93c948f6849d68c6688ffc0c840da-1.jpg"/>](https://stackoverflow.com/users/9819333/abhishek-jain)

[Abhishek Jain](https://stackoverflow.com/users/9819333/abhishek-jain)

4,119

22 gold badges

2929 silver badges

3030 bronze badges

- 15
    
    Be very careful with `-a`. This will wipe every image on your system that doesn't have a container associated with it. Usually just `docker system prune` is sufficient.
    
    – [Josh](https://stackoverflow.com/users/395457/josh "2,789 reputation")
    
    [Commented Nov 27, 2019 at 2:51](#comment104363732_53143653)
    
- 1
    
    I did mention about user has to be careful when using -a as it will remove all images for which containers are not running....
    
    – [Abhishek Jain](https://stackoverflow.com/users/9819333/abhishek-jain "4,119 reputation")
    
    [Commented Nov 27, 2019 at 12:18](#comment104378075_53143653)
    
- Be very careful with -a. This will also remove unused networks and you may lose network connectivity.
    
    – [Lawrence Patrick](https://stackoverflow.com/users/13022099/lawrence-patrick "379 reputation")
    
    [Commented Dec 9, 2020 at 4:23](#comment115285510_53143653)
    
- The statement "if above command does not work in first go then run the same command twice" helped me. Not sure, why it did not free up space in 1 shot.
    
    – [tryingToLearn](https://stackoverflow.com/users/2458858/tryingtolearn "11,463 reputation")
    
    [Commented Nov 2, 2022 at 5:58](#comment131148033_53143653)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="63248975"></a>

20

[](https://stackoverflow.com/posts/63248975/timeline)

Open up the docker settings -> Resources -> Advanced and up the amount of Hard Drive space it can use under disk image size.

[Share](https://stackoverflow.com/a/63248975 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/63248975/edit)

answered Aug 4, 2020 at 14:23

<img width="32" height="32" src="../_resources/8a224b8fe21209548063673f86d0b2e7_bf3ea83f516f4d1aa-1.png"/>](https://stackoverflow.com/users/1143358/nico)

[Nico](https://stackoverflow.com/users/1143358/nico)

1,162

1313 silver badges

1717 bronze badges

- 1
    
    Works great for me on docker desktop version 2.3.0.4 on Mac os Mojave.
    
    – [user674669](https://stackoverflow.com/users/674669/user674669 "12,018 reputation")
    
    [Commented Sep 15, 2020 at 21:26](#comment113013426_63248975)
    
- 9
    
    Is there any way to do this on Linux?
    
    – [nCoder](https://stackoverflow.com/users/1829356/ncoder "145 reputation")
    
    [Commented Oct 27, 2021 at 16:31](#comment123277025_63248975)
    
- @nCoder docker does not run in a VM on (most) linux machines, so there is no artificial limitation on the amount of disk space it can use to begin with.
    
    – [DragonBobZ](https://stackoverflow.com/users/4728007/dragonbobz "2,424 reputation")
    
    [Commented Dec 5, 2023 at 15:20](#comment136817394_63248975)
    
- 1
    
    This should be top answer in combination with the original and second answer.
    
    – [rjurney](https://stackoverflow.com/users/13969/rjurney "5,088 reputation")
    
    [Commented Dec 13, 2023 at 21:25](#comment136905938_63248975)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="62554053"></a>

13

[](https://stackoverflow.com/posts/62554053/timeline)

If you are using linux, then most probably docker is filling up the directory `/var/lib/docker/containers`, because it is writing container logs to `<CONTAINER_ID>-json.log` file under this directory. You can use the command `cat /dev/null > <CONTAINER_ID>-json.log` to clear this file or you can set the maximum log file size be editing `/etc/sysconfig/docker`. More information can be found in this [RedHat documentation](https://access.redhat.com/solutions/2334181). In my case, I have created a crontab to clear the contents of the file every day at midnight. Hope this helps!

NB:

1.  You can find the docker containers with **ID** using the following command `sudo docker ps --no-trunc`
2.  You can check the size of the file using the command `du -sh $(docker inspect --format='{{.LogPath}}' CONTAINER_ID_FOUND_IN_LAST_STEP)`

[Share](https://stackoverflow.com/a/62554053 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/62554053/edit)

[edited Jun 24, 2020 at 11:40](https://stackoverflow.com/posts/62554053/revisions "show all edits to this post")

answered Jun 24, 2020 at 11:30

<img width="32" height="32" src="../_resources/voypA_eb735dbfc7604ee79a5625f9f21ecd9c-1.htm"/>](https://stackoverflow.com/users/784929/kaushik)

[kaushik](https://stackoverflow.com/users/784929/kaushik)

2,473

66 gold badges

3838 silver badges

5353 bronze badges

- Does Log files takes larger memory space?
    
    – [adnan](https://stackoverflow.com/users/10795530/adnan "556 reputation")
    
    [Commented Nov 8, 2023 at 10:06](#comment136530356_62554053)
    
- 1
    
    @adnan, yes, it will takeup diskspace eventually
    
    – [kaushik](https://stackoverflow.com/users/784929/kaushik "2,473 reputation")
    
    [Commented Nov 8, 2023 at 11:27](#comment136531222_62554053)
    
- Some linux distros it's /var/lib/docker/overlay2
    
    – [Geordie](https://stackoverflow.com/users/796634/geordie "2,066 reputation")
    
    [Commented Jan 27 at 21:20](#comment137320941_62554053)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="52816734"></a>

4

[](https://stackoverflow.com/posts/52816734/timeline)

Nothing works for me. I change the disk images max size in Docker Settings, and just after that it free huge size.

[Share](https://stackoverflow.com/a/52816734 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/52816734/edit)

answered Oct 15, 2018 at 12:24

<img width="32" height="32" src="../_resources/jLVka_98c1b58cc2b44b208e7f55d0444aca50-1.htm"/>](https://stackoverflow.com/users/471137/troger19)

[troger19](https://stackoverflow.com/users/471137/troger19)

1,289

22 gold badges

1515 silver badges

3131 bronze badges

- 1
    
    Wow, I didn't see this option! Was wondering why my Windows showed 60GB free disk space, but Docker containers said "Not enough disk space left" - I had my limit at 50GB (which was all used up) - set it to 200 and it worked!
    
    – [Alex](https://stackoverflow.com/users/4556479/alex "3,311 reputation")
    
    [Commented Jul 13, 2019 at 18:44](#comment100574153_52816734)
    
- well the command should be as mentioned above, the thing is it doesnt work for me.. only manually clicking on a button
    
    – [troger19](https://stackoverflow.com/users/471137/troger19 "1,289 reputation")
    
    [Commented Apr 9, 2021 at 9:33](#comment118462626_52816734)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="76123330"></a>

4

[](https://stackoverflow.com/posts/76123330/timeline)

Not sure if this is still relevant, but in case of `docker system prune` not working, and if you don't want to go `docker system prune -a`, you should pick and delete images using either

- `docker image prune --filter`

or

- Picking and deleting them from Docker for Dekstop

[Share](https://stackoverflow.com/a/76123330 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/76123330/edit)

[edited May 1, 2023 at 13:36](https://stackoverflow.com/posts/76123330/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/QTwMP_87dc7cfec0a94a809b6d89d95862213e-1.htm"/>](https://stackoverflow.com/users/13393940/cconsta1)

[cconsta1](https://stackoverflow.com/users/13393940/cconsta1)

807

11 gold badge

99 silver badges

2222 bronze badges

answered Apr 27, 2023 at 17:51

<img width="32" height="32" src="../_resources/c8b20fc767206f44293cb3fe2c2efb08_010a71f2d25d4e228-1.jpg"/>](https://stackoverflow.com/users/12505078/l0t)

[L0t](https://stackoverflow.com/users/12505078/l0t)

61

44 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="58338673"></a>

3

[](https://stackoverflow.com/posts/58338673/timeline)

Going to leave this here since I couldn't find the answer.

Go to the Docker GUI -> Prefereces -> Reset -> Uninstall

Completely uninstall Docker.

Then install it fresh using [this link](https://docs.docker.com/v17.09/docker-for-mac/install/)

My docker was using 20GB of space when building an image, after fresh install, it uses 3-4GB max. Definitely helps!

Also, if you using a macbook, have look at `~/Library/Containers/docker*`

This folder for me was 60 GB and was eating up all the space on my mac! Even though this may not be relevant to the question, I believe it is vital for me to leave this here.

[Share](https://stackoverflow.com/a/58338673 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/58338673/edit)

answered Oct 11, 2019 at 9:51

<img width="32" height="32" src="../_resources/EwFLW_5901e3d2ed924fafb227d18233eb536f-1.htm"/>](https://stackoverflow.com/users/11317776/dudanf)

[DUDANF](https://stackoverflow.com/users/11317776/dudanf)

2,932

11 gold badge

1515 silver badges

4444 bronze badges

- This actually helped me a lot, thanks. I didn't have to reinstall, but finding where all the junk data that was not getting pruned was did the trick.
    
    – [Jim Crozier](https://stackoverflow.com/users/736443/jim-crozier "1,398 reputation")
    
    [Commented Feb 16 at 14:56](#comment137524231_58338673)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="78412380"></a>

1

[](https://stackoverflow.com/posts/78412380/timeline)

There are at least two directories where docker can fill up space. Assuming you have a bigger disk partition on your computer, say /bigdisk, here are the possible solution:

1.  Temp dir in /var/tmp: docker will honour the TMPDIR settings

```
mkdir -p /bigdisk/bigtmp
chmod 1777 /bigdisk/bigtmp
export TMPDIR=/bigdisk/bigtmp
```

2.  /var/lib/containers (older version of docker might use /var/lib/docker). You can solve this by making /var/lib/containers to be a symlink to the bigger disk:

```
mkdir -p /bigdisk/var-lib/containers
ln -s /bigdisk/var-lib/containers /var/lib/containers
```

Now if you have already some docker images in /var/lib/containers, you need to move those first. First stop any docker daemon running

```
mkdir -p /bigdisk/var-lib/containers
##### copy existing container content to bigdisk
(cd /var/lib/containers; tar cvf - . ) | (cd /bigdisk/var-lib/containers; tar xvf - )
#### ensure the copy is good.
du -sh /var/lib/containers 
du -sh /bigdisk/var-lib/containers
rmdir /var/lib/containers
ln -s /bigdisk/var-lib/containers /var/lib/containers
```

Then run docker to verify things run as before

[Share](https://stackoverflow.com/a/78412380 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/78412380/edit)

answered May 1 at 6:47

<img width="32" height="32" src="../_resources/AGNmyxYM3pqsTP_v25VcVXxRsprPWGqo_8c1f5af184d34a14b-1.png"/>](https://stackoverflow.com/users/21485043/monapy)

[MonaPy](https://stackoverflow.com/users/21485043/monapy)

159

11 silver badge

55 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="78014595"></a>

0

[](https://stackoverflow.com/posts/78014595/timeline)

I wanted to add this to my CI/CD pipeline so I won't have to do it manually on my AWS EC2 instance.

The **\-f** option ensured there was **no prompt for confirmation**

Without it, I kept getting: **Are you sure you want to continue? \[y/N\]** And my updates failed to deploy.

Here's what worked for me: In my .yml file, :

```
deploy:
   steps:
      - name: Prune and free some space in images and containers
      run: docker system prune -f
```

[Share](https://stackoverflow.com/a/78014595 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/78014595/edit)

answered Feb 18 at 4:50

<img width="32" height="32" src="../_resources/EboNd_6498f6ebdeab496da301daebdf39bc0d-1.htm"/>](https://stackoverflow.com/users/1585461/chelathegreat)

[ChelaTheGreat](https://stackoverflow.com/users/1585461/chelathegreat)

75

11 silver badge

88 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="78049656"></a>

0

[](https://stackoverflow.com/posts/78049656/timeline)

Unless you are using a logging driver other than the default `json_file` logging driver with its default `unlimited` max-size, your container logs may grow large and fill up either your host machine's disk (Linux host machine) or your docker machine VM's disk (macOS host machine and probably also Windows). This can be hard to inspect (ref: [my question](https://stackoverflow.com/questions/78049466/how-can-i-inspect-the-disk-usage-of-docker-container-logs-on-macos/78049467)).

kaushik's answer explains how to truncate the log files on Linux. On macOS though it's more complicated because the log files are stored in the Docker Machine VM. See [my answer here](https://stackoverflow.com/a/78044877/2562319) for full details.

[Share](https://stackoverflow.com/a/78049656 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/78049656/edit)

answered Feb 23 at 19:01

<img width="32" height="32" src="../_resources/918wA_4d4bc4aed657492f8e8eb1b4ff154665-1.htm"/>](https://stackoverflow.com/users/2562319/jbyler)

[jbyler](https://stackoverflow.com/users/2562319/jbyler)

7,672

33 gold badges

3838 silver badges

4444 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="78341770"></a>

0

[](https://stackoverflow.com/posts/78341770/timeline)

I have the same problem with my Mac. I didn't want to remove docker and found a new way

Go to the Docker GUI -> Troubleshooting -> Reset to factory defaults

This made about 50 GB available

[Share](https://stackoverflow.com/a/78341770 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/78341770/edit)

answered Apr 17 at 14:29

<img width="32" height="32" src="../_resources/dc09101d1646f95673fe84875ca099a2_e915deb43d614cf6b-1.png"/>](https://stackoverflow.com/users/5382500/%d0%9f%d0%b5%d1%82%d1%80-%d0%94%d1%80%d1%83%d0%b1%d0%be%d0%b2)

[Петр Друбов](https://stackoverflow.com/users/5382500/%d0%9f%d0%b5%d1%82%d1%80-%d0%94%d1%80%d1%83%d0%b1%d0%be%d0%b2)

81

11 gold badge

11 silver badge

66 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="78762347"></a>

0

[](https://stackoverflow.com/posts/78762347/timeline)

I run following command:

```
 docker system prune -a
```

before prune: [![enter image description here](https://i.sstatic.net/3KM4pjol.png)](https://i.sstatic.net/3KM4pjol.png)

when running: [![enter image description here](https://i.sstatic.net/19JUUsF3.png)](https://i.sstatic.net/19JUUsF3.png)

after prune: [![enter image description here](https://i.sstatic.net/KPPExN0G.png)](https://i.sstatic.net/KPPExN0G.png)

[Share](https://stackoverflow.com/a/78762347 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/78762347/edit)

answered Jul 18 at 3:57

<img width="32" height="32" src="../_resources/jd3uN_26d85def6fc94a51ab8947e4eaca5bc4-1.htm"/>](https://stackoverflow.com/users/3610643/m-namjo)

[M.Namjo](https://stackoverflow.com/users/3610643/m-namjo)

412

33 silver badges

1515 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="new-answer"></a>

## Your Answer

### Sign up or <a id="login-link"></a>[log in](https://stackoverflow.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f51238891%2fhow-to-fix-the-running-out-of-disk-space-error-in-docker%23new-answer)

Sign up using Google

Sign up using Email and Password

### Post as a guest

Name

Email

Required, but never shown

By clicking “Post Your Answer”, you agree to our <a id="tos"></a>[terms of service](https://stackoverflow.com/legal/terms-of-service/public) and acknowledge you have read our <a id="privacy"></a>[privacy policy](https://stackoverflow.com/legal/privacy-policy).

## 

Not the answer you're looking for? Browse other questions tagged

- [docker](https://stackoverflow.com/questions/tagged/docker "show questions tagged 'docker'")
- [docker-machine](https://stackoverflow.com/questions/tagged/docker-machine "show questions tagged 'docker-machine'")

or [ask your own question](https://stackoverflow.com/questions/ask).

- The Overflow Blog
- [The evolution of full stack engineers](https://stackoverflow.blog/2024/09/10/evolution-full-stack-engineers-mrina-sugosh/?cb=1)
    
- [One of the best ways to get value for AI coding tools: generating tests](https://stackoverflow.blog/2024/09/10/gen-ai-llm-create-test-developers-coding-software-code-quality/?cb=1)
    
- Featured on Meta
- [Join Stack Overflow’s CEO and me for the first Stack IRL Community Event in...](https://meta.stackexchange.com/questions/402759/join-stack-overflow-s-ceo-and-me-for-the-first-stack-irl-community-event-in-nyc?cb=1 "Join Stack Overflow’s CEO and me for the first Stack IRL Community Event in NYC on October 10th, 2024 (space is very limited)")
    
- [User activation: Learnings and opportunities](https://meta.stackexchange.com/questions/402813/user-activation-learnings-and-opportunities?cb=1)
    
- [Staging Ground Reviewer Motivation](https://meta.stackoverflow.com/questions/431399/staging-ground-reviewer-motivation?cb=1)
    
- [What does a new user need in a homepage experience on Stack Overflow?](https://meta.stackoverflow.com/questions/431331/what-does-a-new-user-need-in-a-homepage-experience-on-stack-overflow?cb=1)
    

#### Linked

[105](https://stackoverflow.com/q/41091634?lq=1 "Question score (upvotes - downvotes)")[How to clean Docker container logs?](https://stackoverflow.com/questions/41091634/how-to-clean-docker-container-logs?noredirect=1&lq=1)

[6](https://stackoverflow.com/q/25713773?lq=1 "Question score (upvotes - downvotes)")[disk space is full by \`vda\` files, how to clear them?](https://stackoverflow.com/questions/25713773/disk-space-is-full-by-vda-files-how-to-clear-them?noredirect=1&lq=1)

[\-1](https://stackoverflow.com/q/78049466?lq=1 "Question score (upvotes - downvotes)")[How can I inspect the disk usage of docker container logs on macOS?](https://stackoverflow.com/questions/78049466/how-can-i-inspect-the-disk-usage-of-docker-container-logs-on-macos?noredirect=1&lq=1)

#### Related

[743](https://stackoverflow.com/q/30604846?rq=3 "Question score (upvotes - downvotes)")[Docker error : no space left on device](https://stackoverflow.com/questions/30604846/docker-error-no-space-left-on-device?rq=3)

[3](https://stackoverflow.com/q/30845650?rq=3 "Question score (upvotes - downvotes)")[Docker run, no space left on device](https://stackoverflow.com/questions/30845650/docker-run-no-space-left-on-device?rq=3)

[152](https://stackoverflow.com/q/31909979?rq=3 "Question score (upvotes - downvotes)")[Docker Machine: No space left on device](https://stackoverflow.com/questions/31909979/docker-machine-no-space-left-on-device?rq=3)

[82](https://stackoverflow.com/q/37645879?rq=3 "Question score (upvotes - downvotes)")[How can I fix Docker/Mac no space left on device error?](https://stackoverflow.com/questions/37645879/how-can-i-fix-docker-mac-no-space-left-on-device-error?rq=3)

[1](https://stackoverflow.com/q/40340978?rq=3 "Question score (upvotes - downvotes)")[docker start: no space left on device](https://stackoverflow.com/questions/40340978/docker-start-no-space-left-on-device?rq=3)

[58](https://stackoverflow.com/q/41227546?rq=3 "Question score (upvotes - downvotes)")[How can I fix 'No space left on device' error in Docker?](https://stackoverflow.com/questions/41227546/how-can-i-fix-no-space-left-on-device-error-in-docker?rq=3)

[7](https://stackoverflow.com/q/43111587?rq=3 "Question score (upvotes - downvotes)")[Docker Error : no space left on device on windows](https://stackoverflow.com/questions/43111587/docker-error-no-space-left-on-device-on-windows?rq=3)

[77](https://stackoverflow.com/q/48668660?rq=3 "Question score (upvotes - downvotes)")[docker no space left on device macOS](https://stackoverflow.com/questions/48668660/docker-no-space-left-on-device-macos?rq=3)

[1](https://stackoverflow.com/q/56578563?rq=3 "Question score (upvotes - downvotes)")[docker load : no space left on device](https://stackoverflow.com/questions/56578563/docker-load-no-space-left-on-device?rq=3)

[1](https://stackoverflow.com/q/58776842?rq=3 "Question score (upvotes - downvotes)")[Why did my docker volume run out of disk space?](https://stackoverflow.com/questions/58776842/why-did-my-docker-volume-run-out-of-disk-space?rq=3)

#### [Hot Network Questions](https://stackexchange.com/questions?tab=hot)

- [Is the closest diagonal state to a given state always the dephased original state?](https://quantumcomputing.stackexchange.com/questions/39801/is-the-closest-diagonal-state-to-a-given-state-always-the-dephased-original-stat)
- [Why Pythagorean theorem is all about 2?](https://math.stackexchange.com/questions/4969755/why-pythagorean-theorem-is-all-about-2)
- [Is there mathematical significance to the LaGuardia floor tiles?](https://mathoverflow.net/questions/478547/is-there-mathematical-significance-to-the-laguardia-floor-tiles)
- [Maximise finds solution outside the constraint](https://mathematica.stackexchange.com/questions/306862/maximise-finds-solution-outside-the-constraint)
- [Why is the area covered by 1 steradian (in a sphere) circular in shape?](https://physics.stackexchange.com/questions/827478/why-is-the-area-covered-by-1-steradian-in-a-sphere-circular-in-shape)
- [Navigating career options after a disastrous PhD performance and a disappointed advisor?](https://academia.stackexchange.com/questions/213492/navigating-career-options-after-a-disastrous-phd-performance-and-a-disappointed)
- [Is this map real?](https://puzzling.stackexchange.com/questions/128290/is-this-map-real)
- [Two sisters live alone in a house after the rest of their family died](https://literature.stackexchange.com/questions/27759/two-sisters-live-alone-in-a-house-after-the-rest-of-their-family-died)
- [4/4 time change to 6/8 time](https://music.stackexchange.com/questions/137353/4-4-time-change-to-6-8-time)
- [What would the natural diet of Bigfoot be?](https://worldbuilding.stackexchange.com/questions/261606/what-would-the-natural-diet-of-bigfoot-be)
- [Does the Supremacy Clause allow states to retain abortion rights enshrined in each states' constitution?](https://law.stackexchange.com/questions/104934/does-the-supremacy-clause-allow-states-to-retain-abortion-rights-enshrined-in-ea)
- [Does any row of Pascal's triangle contain a Pythagorean triple?](https://math.stackexchange.com/questions/4970116/does-any-row-of-pascals-triangle-contain-a-pythagorean-triple)
- [How will the Polaris Dawn cabin pressure and oxygen partial pressure dovetail with that of their EVA suits? (100% oxygen?)](https://space.stackexchange.com/questions/66881/how-will-the-polaris-dawn-cabin-pressure-and-oxygen-partial-pressure-dovetail-wi)
- [Can a V22 Osprey operate with only one propeller?](https://aviation.stackexchange.com/questions/106632/can-a-v22-osprey-operate-with-only-one-propeller)
- [Why do "modern" languages not provide argv and exit code in main?](https://langdev.stackexchange.com/questions/4041/why-do-modern-languages-not-provide-argv-and-exit-code-in-main)
- [Why were there so many OSes that had the name "DOS" in them?](https://retrocomputing.stackexchange.com/questions/30603/why-were-there-so-many-oses-that-had-the-name-dos-in-them)
- [jq - ip addr show in tabular format](https://unix.stackexchange.com/questions/783284/jq-ip-addr-show-in-tabular-format)
- [A journal has published an AI-generated article under my name. What to do?](https://academia.stackexchange.com/questions/213473/a-journal-has-published-an-ai-generated-article-under-my-name-what-to-do)
- [If a friend hands me a marijuana edible then dies of a heart attack am I guilty of felony murder?](https://law.stackexchange.com/questions/104914/if-a-friend-hands-me-a-marijuana-edible-then-dies-of-a-heart-attack-am-i-guilty)
- [Book that features clones used for retirement](https://scifi.stackexchange.com/questions/291546/book-that-features-clones-used-for-retirement)
- [How long should a wooden construct burn (and continue to take damage) until it burns out (and stops doing damage)](https://rpg.stackexchange.com/questions/213291/how-long-should-a-wooden-construct-burn-and-continue-to-take-damage-until-it-b)
- [Word switching from plural to singular when it is many?](https://judaism.stackexchange.com/questions/144837/word-switching-from-plural-to-singular-when-it-is-many)
- [Electrical panel not sending 240](https://diy.stackexchange.com/questions/306863/electrical-panel-not-sending-240)
- [Spacing between mathrel and mathord same as between mathrel and mathopen](https://tex.stackexchange.com/questions/726262/spacing-between-mathrel-and-mathord-same-as-between-mathrel-and-mathopen)

[Question feed](https://stackoverflow.com/feeds/question/51238891 "Feed of this question and its answers")

[](https://stackoverflow.com)

##### [Stack Overflow](https://stackoverflow.com)

- [Questions](https://stackoverflow.com/questions)
- [Help](https://stackoverflow.com/help)
- [Chat](https://chat.stackoverflow.com/?tab=site&host=stackoverflow.com)

##### [Products](https://stackoverflow.co/)

- [Teams](https://stackoverflow.co/teams/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=teams)
- [Advertising](https://stackoverflow.co/advertising/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=advertising)
- [Talent](https://stackoverflow.co/advertising/employer-branding/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=talent)

##### [Company](https://stackoverflow.co/)

- [About](https://stackoverflow.co/)
- [Press](https://stackoverflow.co/company/press/)
- [Work Here](https://stackoverflow.co/company/work-here/)
- [Legal](https://stackoverflow.com/legal)
- [Privacy Policy](https://stackoverflow.com/legal/privacy-policy)
- [Terms of Service](https://stackoverflow.com/legal/terms-of-service/public)
- [Contact Us](https://stackoverflow.com/contact)

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

- [Blog](https://stackoverflow.blog?blb=1)
- [Facebook](https://www.facebook.com/officialstackoverflow/)
- [Twitter](https://twitter.com/stackoverflow)
- [LinkedIn](https://linkedin.com/company/stack-overflow)
- [Instagram](https://www.instagram.com/thestackoverflow)

Site design / logo © 2024 Stack Exchange Inc; user contributions licensed under [CC BY-SA](https://stackoverflow.com/help/licensing) . <a id="svnrev"></a>rev 2024.9.11.15092