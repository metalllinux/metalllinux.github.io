---
title: "How to Specify an SSH Key with rsync"
category: "networking"
tags: ["networking", "specify", "ssh", "key", "rsync"]
---

# How to Specify an SSH Key with rsync

Specify identity file (id_rsa) with rsync

https://unix.stackexchange.com/questions/127352/specify-identity-file-id-rsa-with-rsync

I need to make periodic backups of a directory on a remote server which is a virtual machine hosted by a research organisation. They mandate that access to VMs is through ssh keys, which is all good, except that I can't figure out how to point rsync to the ssh key for this server.

Rsync has no problem if the key file is ~/.ssh/id_rsa, but when it is something else I get Permission denied (publickey).

With ssh I can specify the identity file with -i, but rsync appears to have no such option.

I have also tried temporarily moving the key on the local machine to ~/.ssh/id_rsa, but that similarly does not work.

tl;dr

Can you specify an identity file with rsync?

    sshrsync

Share
Improve this question
Follow
asked May 1, 2014 at 0:15
Jangari's user avatar
Jangari
4,72822 gold badges1515 silver badges99 bronze badges

    4
    Useful also in order to do sudo rsync, which doesn't use one's own ssh keys, for some reason. – 
    ijoseph
    Commented Jul 27, 2018 at 21:19
    1
    @ijoseph Exactly, I use rsync -aAP "sudo -u user ssh" user@server:dir local_dir when syncing from cron scripts which run as root – 
    Martin Pecka
    Commented Dec 11, 2018 at 14:16

Add a comment
4 Answers
Sorted by:
715

You can specify the exact ssh command via the '-e' option:

rsync -Pav -e "ssh -i $HOME/.ssh/somekey" username@hostname:/from/dir/ /to/dir/

Many ssh users are unfamiliar with their ~/.ssh/config file. You can specify default settings per host via the config file.

Host hostname
    User username
    IdentityFile ~/.ssh/somekey

In the long run it is best to learn the ~/.ssh/config file.
Share
Improve this answer
Follow
edited Feb 10, 2017 at 14:18
answered May 1, 2014 at 0:23
Dan Garthwaite's user avatar
Dan Garthwaite
8,54611 gold badge1717 silver badges99 bronze badges

    1
    Does not help for me to have the IdentityFile in ssh_config. I can "ssh web1" without problems, but when using rsync to web1:... it fails with "Permission denied (publickey)". – 
    Zitrax
    Commented Oct 14, 2014 at 7:28
    2
    Try turning up verboseness of the ssh transport: rsync -e 'ssh -vv' web1:/etc/issue /tmp/issue – 
    Dan Garthwaite
    Commented Oct 14, 2014 at 14:49 

    1
    Ah. If you are automating this and will not be able to supply a password you will need an additional passwordless ssh key configured at both ends. If you would like rsync to work without a password in an interactive session you will need to use ssh-agent. – 
    Dan Garthwaite
    Commented Oct 14, 2014 at 21:48
    60
    Duuuuuuude! the ~/.ssh/config file - you have opened a new universe for me! – 
    demaniak
    Commented Jun 29, 2017 at 20:38
    6
    In my case for ~/.ssh/config to work I had to do chmod 600 ~/.ssh/config – 
    Tono Nam
    Commented Oct 21, 2019 at 4:21

Show 11 more comments
26

This can be done with SSH user config see: http://www.cyberciti.biz/faq/create-ssh-config-file-on-linux-unix/ basically edit ~/.ssh/config:

$ nano ~/.ssh/config
#Add Hosts below 
Host server1
HostName examplehost.com
User username
Port 22
IdentityFile /path/to/key

$ rsync -e ssh /home/user/directory user@remote.host.net:home/user/directory/

This should work for any program using SSH, rsync,
Share
Improve this answer
Follow
answered May 1, 2014 at 0:30
Cbaker510's user avatar
Cbaker510
42344 silver badges66 bronze badges

    1
    You can use rsync -e ssh /home/user/directory server1:home/user/directory/ as well – 
    Dexter
    Commented Nov 1, 2019 at 13:12

Add a comment
16

For me it was sufficient to start the ssh-agent as follows:

eval `ssh-agent -s`
ssh-add /path/to/mykey

See also a longer answer here https://stackoverflow.com/questions/17846529/could-not-open-a-connection-to-your-authentication-agent
Share
Improve this answer
Follow
edited May 23, 2017 at 12:40
Community's user avatar
CommunityBot
1
answered Apr 14, 2016 at 7:06
pietro's user avatar
pietro
26122 silver badges33 bronze badges
Add a comment
4

FYI:

1) The public key is always in the home directory of the user logging in to remote server i.e. if you login as "backup" it is located at /home/backup/.ssh/authorized_keys. User ID when you login defines the public key used at the destination.

You can choose the user ID when making connection by two different ways:

ssh user_id@destination.server
or
ssh -l user_id  destination_server     (<-- that is lower case "L")

On the other hand at your end the private key is in a similar way in homedir of user unless you override it like described in Dan's answer.

2) For backup purpose it may be desirable to create a restricted key which is limited to run just one command like "rsync". There is a good description about that related to "rsnapshot" backup which allows you to remote backup entire server using non privileged user account and "sudo":

"rsnapshot" howto

Rsnapshot can easily backup a bunch of remote or local servers making it handy scheduled & centralised backup server.
Share
Improve this answer
Follow
edited Jan 6, 2015 at 19:29

