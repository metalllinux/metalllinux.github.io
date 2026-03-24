---
title: "Sparky - Getting Started - RESF Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "sparky", "getting", "started", "resf"]
---

# Sparky - Getting Started - RESF Rocky Linux

## [](https://git.resf.org/testing/Sparky_Getting_Started#what-is-this-and-why)What is this and why?

## [](https://git.resf.org/testing/Sparky_Getting_Started#short-background-of-names-used)Short background of names used

Perl is a programming language. [Raku](https://raku.org/) is a member of the Perl family (aka: Perl 6). [Sparrow](https://github.com/melezhik/Sparrow6) is an automation framework built with Raku. [Sparky](https://github.com/melezhik/sparky) is an continuous integration server and distribute tasks runner written in Raku that leverages Sparrow.

## [](https://git.resf.org/testing/Sparky_Getting_Started#why-use-this-for-rocky)Why use this for Rocky?

The goal for Rocky to use Sparky is to have more test coverage of common use-cases that the Rocky Testing Team can verify on new releases (both major and point releases). Additionally, there are two other hopeful goals.

-   As the tests can be rather simple Bash code, there is a desire for more sys-admins to write automated tests about the things they care about. This provides a low-entry opportunity for community to contribute to Rocky about something they care about.
-   The tests can be used to verify documentation. Not only providing the documentation team an opportunity to find when an updated package breaks the documented process before a frustrated user finds it, but also to give users a way to check their install with a known working script.

The Venn-diagram overlap of OpenQA, Kickstart tests, and Sparky is fairly minimal. While the Testing Team had hope to integrate most of the documentation into OpenQA or the Kickstart tests the process was becoming complicated. Sparky provides a automation framework tool that is much easier for community to contribute to.

## [](https://git.resf.org/testing/Sparky_Getting_Started#install)Install

This is assuming a Rocky 9 base install. This guide should be everything you need to get started running the Rocky test scripts with Sparky. You CAN also run this as a VM so long as you have QEMU pass through to run virt-in-virt. That isn't covered in this guide but it helps if you are doing a lot of configuration testing and you just need to quickly restart/reset.

## [](https://git.resf.org/testing/Sparky_Getting_Started#install-dependencies)Install dependencies

`sudo dnf install -y wget tar perl xorriso bash-completion qemu-kvm vim sqlite git openssl-devel rsync tmux`

## [](https://git.resf.org/testing/Sparky_Getting_Started#install-raku)Install Raku

Two ways - Recommended is from the package repo even if it is a few more steps.

### [](https://git.resf.org/testing/Sparky_Getting_Started#from-package-repo)From Package Repo

```
sudo rpm --import 'https://dl.cloudsmith.io/public/nxadm-pkgs/rakudo-pkg/gpg.0DD4CA7EB1C6CC6B.key'
sudo curl -1sLf 'https://dl.cloudsmith.io/public/nxadm-pkgs/rakudo-pkg/config.rpm.txt?distro=el&codename=9' > /tmp/nxadm-pkgs-rakudo-pkg.repo
sudo dnf config-manager --add-repo '/tmp/nxadm-pkgs-rakudo-pkg.repo'
sudo dnf --refresh -y install rakudo-pkg
/opt/rakudo-pkg/bin/add-rakudo-to-path
source ~/.bash_profile
which raku # Verify raku is in the path
which zef # Verify zef is in the path - if it is, skip to the next section; if it is not continue
/opt/rakudo-pkg/bin/install-zef
source ~/.bash_profile
```

### [](https://git.resf.org/testing/Sparky_Getting_Started#from-internet-script)From Internet Script

```
curl https://rakubrew.org/install-on-perl.sh | sh
echo 'eval "$(~/.rakubrew/bin/rakubrew init Bash)"' >> ~/.bashrc
eval "$(~/.rakubrew/bin/rakubrew init Bash)"
rakubrew download moar-2025.02
```

Now test that it works. `# raku -v`

## [](https://git.resf.org/testing/Sparky_Getting_Started#clone-sparky)Clone Sparky

There's a high chance that /something/ will fail a test in this `zef install .` command. If the error is a missing package, try to install the missing package; I _think_ I got all the depenencies listed in the above install but things could change or I could have missed one. You might need to do a `dnf provides */missing.so` search. If the error is about a failed test, then try running this : `zef install --/test .` and if that works, continue.

Due to a known issue, this three stage install appears to work the most reliably.

```
mkdir ~/Code # Or wherever you want to store code repos...
cd ~/Code
git clone https://github.com/melezhik/sparky.git
cd sparky
zef install cro --deps-only
zef install cro
zef install .
```

## [](https://git.resf.org/testing/Sparky_Getting_Started#install-sparky)Install Sparky

Only run this after the last step is finished: `raku db-init.raku`

However, do note - sometimes you might get an error like: `⚠ sparky DBDish::SQLite: Error: no such table: builds (1)`

This could be because of a corrupt db (eg: you copied someone elses from a repo; or a test went really bad). This command will reset the db.

## [](https://git.resf.org/testing/Sparky_Getting_Started#install-sparky-job-api)Install Sparky Job API

`zef install Sparky::JobApi`

## [](https://git.resf.org/testing/Sparky_Getting_Started#configure)Configure

## [](https://git.resf.org/testing/Sparky_Getting_Started#firewall)Firewall

Ensure firewall allows port 4000

```
sudo firewall-cmd --add-port=4000/tcp --permanent
sudo firewall-cmd --reload
```

## [](https://git.resf.org/testing/Sparky_Getting_Started#project-setup)Project Setup

Now lets load some projects.

## [](https://git.resf.org/testing/Sparky_Getting_Started#code-repo-prep)Code Repo Prep

```
cd ~/Code
git clone https://git.resf.org/testing/Sparky_Rocky
cd Sparky_Rocky
bash scripts/sync_project.sh
```

### [](https://git.resf.org/testing/Sparky_Getting_Started#a-note-about-the-api-key)A note about the API key

This can and should be a random string. This needs to be on any system where the Sparky server is installed and run (in this demo so far, just this host). This key should have been generated from the above script and can be located in ~/sparky.yaml

## [](https://git.resf.org/testing/Sparky_Getting_Started#download-images)Download images

Now that the project is prepped, let's get some images (all that you want/need):

```
mkdir -p ~/rocky-linux-distro && cd ~/rocky-linux-distro 
wget https://dl.rockylinux.org/pub/rocky/9.5/images/x86_64/Rocky-9-GenericCloud-Base-9.5-20241118.0.x86_64.qcow2
wget https://dl.rockylinux.org/pub/rocky/8.10/images/x86_64/Rocky-8-GenericCloud-Base-8.10-20240528.0.x86_64.qcow2
```

In the code, it looks for a specific test image: `iso => "{%*ENV<HOME>}/rocky-linux-distro/distro.qcow2",` This is fine, because this lets us either re-use or re-create our images as needed. For now, we'll copy the 9 image.  
`cp Rocky-9-GenericCloud-Base-9.5-20241118.0.x86_64.qcow2 distro.qcow2`

## [](https://git.resf.org/testing/Sparky_Getting_Started#configure-sparky)Configure Sparky

The vars.yaml file holds a lot of important variables. The template should have been created from the above sync\_project.sh script. Please verify your `~/.sparky/templates/vars.yaml` file. The template can be found under the examples folder in the Sparky\_Rocky project.

### [](https://git.resf.org/testing/Sparky_Getting_Started#verify-qemu-binary)Verify QEMU Binary

Your qemu binary may be different. And you might have to specify a machine type. This is a simple guide to help you find your qemu binary but not exhaustive list. Once you know the binary/path - update it in the vars.yaml file.

```
which qemu-kvm
ls -lh /usr/libexec/qemu*
# If it isn't in your path here are a few ways to ensure it is.
# Try em all until you find one that works. :-)
alias qemu-kvm=/usr/libexec/qemu-kvm
echo 'alias qemu-kvm=/usr/libexec/qemu-kvm' >> ~/.bash_profile
mkdir ~/bin && ln -s /usr/libexec/qemu-kvm ~/bin/qemu-kvm
```

### [](https://git.resf.org/testing/Sparky_Getting_Started#verify-qemu-machine)Verify QEMU machine

After you know the qemu binary, you need to know what machine types your system supports. Pick the best one from the list generated by `qemu-kvm -machine ?`. Fill in the line `machine: ""` with the match. A common value is provided ascommented out `#machine: pc-q35-rhel9.4.0`. Remove the line above and the comment to use it.

### [](https://git.resf.org/testing/Sparky_Getting_Started#verify-ssh)Verify SSH

Verify your SSH key path. If you don't have one, create a SSH key and accept the defaults. `ssh-keygen`. Then verify your key path in `ls -l ~/.ssh/`.

## [](https://git.resf.org/testing/Sparky_Getting_Started#start-services)Start services

Now, there's a few ways of doing this next step - tmux, screen, opening multiple shells, or just backgrounding the tasks. Doesn't matter which. Personally, I like seeing the messages while I'm debugging so I open new shells in the corner of my second monitor... Either way, run these two commands in seperate windows/tabs/background/whatever from the sparky directory (eg: `cd ~/Code/sparky`). `sparkyd`  
`cro run`

Steps for doing this in tmux (see [tmux cheat sheet](https://tmuxcheatsheet.com/) for more info).

```
tmux
sparkyd
"Ctrl+b" then ":new"
cd ~
cro run
"Ctrl+b" then "s" to switch sessions
"Ctrl+b" then "d" to detach
```

If you get an error along the lines of "Did not encounter any .cro.yml files... could it be .cro.yml file is missing?" then before running the command ensurre you are in the sparky folder `cd ~/Code/sparky` and try `cro run` again. You should get a `sparky run sparky web ui on host: 0.0.0.0, port: 4000` message if it's working.

## [](https://git.resf.org/testing/Sparky_Getting_Started#start-web-browser)Start Web Browser

Now open a web browser to [http://your-IP:4000](http://your-ip:4000/)

Login as admin:admin

## [](https://git.resf.org/testing/Sparky_Getting_Started#launch-test)Launch Test

Now go to Projects. You should see "sparky-rocky". Click the link to view project details, then click "Build now". (or just click "Build now" if you don't care to see the details.)

There's a drop down for tests to run. For first run, pick the Rocky Linux Lamp Check as it runs fairly quick and is a simple example. Options: repo - Primary repo for Rocky.  
branch - main.  
qemu\_binary - Options for which binary to run against. See alias above. Leave it as qemu-kvm.  
qemu\_machine - pc-q35-rhel9.4.0 - Also set this in ~/.sparky/templates/vars.yaml .  
ssh\_key\_path - This is set in ~/.sparky/templates/vars.yaml . skip\_bootstrap - This is useful for re-testing on the same image. It MUST be unchecked for first time runs.  
qemu\_new\_session - rebuild the qemu session. Most of the time, you will want this checked.  
qemu\_shut - Unchecked means that the test qemu session will remain available for you to manually log in (See Closing Sessions section below). Checked means that when the test is done, close down the qemu session.

For the first run, make sure skip\_bootstrap is unchecked and click Submit. You should see activity in the two window panes where you started sparky and cro run. You should also see "build has started" which will then change to a job number link to the job report.

Click "Recent Builds". You should see the build running. Click the ID link for details about where the job is in it's state. The "start qemu session" will take a few minutes to run.

## [](https://git.resf.org/testing/Sparky_Getting_Started#closing-sessions)Closing sessions

For those times when the qemu session doesn't shut down due either to the selection above or a failure that doesn't close it, `ssh -p 10022 admin@127.0.0.1` and then you can shut down the VM with `sudo init 0`.

If there's a notice about bad ssh keys, remove them from ~/.ssh/known\_hosts before trying to ssh again. `ssh-keygen -R \[127.0.0.1\]:10022`

## [](https://git.resf.org/testing/Sparky_Getting_Started#clean-session-start)Clean session start

Some tests do not impact other tests, while other tests require a new QEMU VM image. By default, the QEMU image will be re-used. Should you want a fresh install (don't forget to uncheck skip\_bootstrap!): `cp ~/rocky-linux-distro/Rocky-9-GenericCloud-Base-9.5-20241118.0.x86_64.qcow2 ~/rocky-linux-distro/distro.qcow2`. You should be able to always start with a fresh QEMU image on any of these tests. If you run into failures re-using an image, please verify the issues on a fresh QEMU image before filing a report.

## [](https://git.resf.org/testing/Sparky_Getting_Started#results-of-the-rocky-linux-lamp-check)Results of the Rocky Linux Lamp Check

There will be several sub-jobs launched. Results should be the same for Rocky 8.10 & 9.5

-   sparky-rocky - triggered by admin - should end with a result of "succeed"
-   qemu-session - start qemu session - should be in a "running" or "succeed" state
-   qemu-bootstrap - bootstrap qemu box - should end with a result of "succeed"
-   qemu-use-case - use case scenario - should end with a result of "succeed"
-   -   Click on the ID for this job to get more details. There should be a successful connection at the end for the "http check for WP localhost"

## [](https://git.resf.org/testing/Sparky_Getting_Started#results-of-the-zfs-test)Results of the ZFS test

There will be several sub-jobs launched. Results are for Rocky 9.5 as 8.10 needs tweaks not in test yet.

-   sparky-rocky - triggered by admin - should end with a result of "succeed"
-   qemu-session - start qemu session - should be in a "running" or "succeed" state
-   qemu-bootstrap - bootstrap qemu box - should end with a result of "succeed"
-   qemu-use-case - use case scenario - should end with a result of "succeed"
-   qemu-reboot - reboot qemu box - will probably end with failed, however, a fix is being worked on. It works, but the exit code is returned negative when the reboot happens.
-   qemu-use-case - use case scenario - should end with a result of "succeed".
-   -   Click on the ID for this job to get more details. You should see successful banners for zpool status, zpool iostat, and zpool list. Verify all items returned "True" under the "\[task check\]" section.

## [](https://git.resf.org/testing/Sparky_Getting_Started#results-of-the-slurm-test)Results of the Slurm test

There will be several sub-jobs launched. Results are for Rocky 9.5 as 8.10 has issues installing slurm at this time.

-   sparky-rocky - triggered by admin - should end with a result of "succeed"
-   qemu-session - start qemu session - should be in a "running" or "succeed" state
-   qemu-bootstrap - bootstrap qemu box - should end with a result of "succeed"
-   qemu-use-case - use case scenario - should end with a result of "succeed"
-   -   Click on the ID for the job to get more details. You should see a successful partition ("normal\* up 7-00:00:00 1 idle master") followed by a message "Test complete!"

## [](https://git.resf.org/testing/Sparky_Getting_Started#writing-new-tests)Writing new tests

## [](https://git.resf.org/testing/Sparky_Getting_Started#create-a-repo)Create a repo

This is assuming two things: 1) you know how to handle Git and 2) you can create a repo somewhere.

First, create a new directory to work from. This example will use sparky-newtest and this will create the template you will need.

```
cd ~/Code
mkdir -p sparky-newtest/files/tasks/check-newtest
cd sparky-newtest
echo "This is your README content; please explain something about this test." > README.md
echo -e '#!raku\ntask-run "files/tasks/check-newtest";' > main.raku
echo -e '#!/bin/bash -\necho "new test code here"' > files/tasks/check-newtest/task.bash
```

main.raku is the file that tells the Sparky job the details about what tasks to run. This is a very simple example; please refer to the documentation for more details.

task.bash is the task to run. This would be the shell script you want run inside of the qemu VM.

At this point, commit this into a Git repo.

## [](https://git.resf.org/testing/Sparky_Getting_Started#modify-vars-yaml-to-see-your-test)Modify vars.yaml to see your test

Once you've commited your code to a remote repo, edit vars.yaml:  
`vim ~/.sparky/templates/vars.yaml`

Under the vars section, under vars -> qemu\_tests -> use\_case\_repo add a new entry following yaml syntax with the Git url.

Refresh the web interface. It should be there. Select your Git repo, configure it as needed (don't forget to start with a fresh qemu image, which if you do then don't forget to uncheck skip\_bootstrap!).

Once you have something that works well, submit a Pull Request for us to add the repo.

## [](https://git.resf.org/testing/Sparky_Getting_Started#credit)Credit

Resources I used in putting this together.

-   [https://github.com/melezhik/rocky-linux-lamp-check](https://github.com/melezhik/rocky-linux-lamp-check)

