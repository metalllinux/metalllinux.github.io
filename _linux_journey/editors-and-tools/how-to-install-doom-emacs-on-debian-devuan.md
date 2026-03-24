---
title: "How to Install Doom Emacs on Debian / Devuan"
category: "editors-and-tools"
tags: ["editors-and-tools", "install", "doom", "emacs", "debian"]
---

# How to Install Doom Emacs on Debian / Devuan

What Is Doom Emacs and How to Install It
By Ramces Red
Updated Nov 16, 2023

Table of Contents

    What is Doom Emacs?
    Preparing Your System for Doom Emacs
    Installing Doom Emacs
    Configuring Doom Emacs

A photograph of a laptop on top of a couch.

Doom Emacs provides an easy and approachable way to start with the Emacs environment. It does this by providing you with an editor that is already complete with plugins and working right out of the box. This article will show you how to install Doom Emacs in Linux as well as configure it for personal use.

Note: Emacs made our list of the best Linux software.
What is Doom Emacs?

At its core, Doom Emacs is a custom Emacs distribution. It is a version of Emacs that contains various tools and tweaks to streamline the text editor’s default feature set. For example, Doom Emacs comes with its own helper utility that automatically updates and configures your personal installation.
A screenshot showing the default Doom Emacs welcome screen.

The developers of Doom Emacs also designed it to be a “configuration framework” for the text editor. As a result, Doom is often flexible enough that you can use it as a start for your own text editor through custom plugins and settings.

Good to know: Emacs is more than just a powerful text editor. Learn how you can connect Emacs to IRC using ERC.
Preparing Your System for Doom Emacs

Note: If you already have a running base Emacs install along with ripgrep and Git, you can skip this step and move on to installing Doom Emacs.

The first step in installing Doom is to obtain its primary dependencies: Emacs, ripgrep and Git. To do that, open a terminal window and run the following command:

Ubuntu/Debian

sudo apt install emacs-gtk ripgrep git

For RHEL and Fedora, you can install Doom’s primary dependencies through dnf:

sudo dnf install emacs ripgrep git

In Arch-based distros, using pacman:

sudo pacman -S emacs ripgrep git

Tip: Find out why Emacs is our favourite text editor of choice.
Installing Doom Emacs

Doom requires a clean Emacs install to work properly. Ensure that the default Emacs config folder does not exist in your home directory:

rm -rf /home/$USER/.emacs.d/

Note: You can preserve your previous Emacs setup by creating a tarball of your original “.emacs.d” folder before deleting it: tar cvzf ~/emacs-d-backup.tar.gz ~/.emacs.d.

Clone the Doom repository from the developer’s Github page and save it as your current user’s Emacs config directory:

git clone --depth 1 https://github.com/hlissner/doom-emacs ~/.emacs.d

A terminal showing the Git clone process for the Doom Emacs repository.

Go inside your new config directory, then run the Doom install utility:

cd ~/.emacs.d
./bin/doom install

Type Y, then press Enter to create a local environment variable file for Doom. This will ensure that Doom will work out of your machine even if you are loading it from a remote session.
A terminal showing the external environment variable file during Doom install.

Wait until the installer utility prints a “Have fun!” message, then run the following command. This will double-check your config folder and ensure that Doom is working properly:

./bin/doom doctor

A terminal showing the Doom doctor utility running.

Open the current user’s “.bash_profile” using your favourite text editor:

nano ~/.bash_profile

Go to the end of the file, then add the following line of code:

export PATH=$PATH:$HOME/.emacs.d/bin

This will update the PATH variable to include the bin directory for Doom and will ensure that you can run the doom utility even outside your config folder.

Log out of your current user to apply your new settings, then test if it works by running the following:

doom doctor

Configuring Doom Emacs

Doom Emacs allows you the choice of more than 150 modules to tweak and enable. These range from basic language support to UI modifications and they allow us to customise Doom to be our own personal computing environment.

FYI: Emacs on its own also has a variety of tricks up its sleeve. Learn some of its hidden features that you can use to improve Emacs.

To start, open Doom and press Space + F, then P.
A screenshot showing a list of the available configuration files for Doom Emacs.

Select the “init.el” file, then press Enter.
A screenshot highlighting the init.el file for Doom Emacs.

Scroll down the file until you find a line that starts with (doom!.
A screenshot highlighting the Doom function for the current Doom Emacs install.

Find a module that you like in the list, then remove the two semi-colons (;;) in front of the one that you want to enable.
A screenshot highlighting a disabled module.

Similar to Gentoo’s USE flags, these Doom modules can also contain flags that you can activate to fine-tune how a module would run during your session.

To add a flag, enclose the module name in parenthesis, then type a “+” sign followed by the flag that you want. In this example, we have added the journal flag to the org module to enable journal support.
A screenshot highlighting a module with an extra modifier flag.

Press Ctrl + X, then Ctrl + C to save your new config file.

Open a new terminal session, then run the following to install the new modules to your Emacs session:

doom sync

Lastly, open your Doom Emacs client and check whether the new modules work properly.
A screenshot showing a working Doom Emacs installation with a custom module flag.

Installing Doom Emacs is just the first step in diving into the rabbit hole of Emacs and its near-endless potential for extensibility. Learn how you can turn this powerful text editor into a music player through EMMS as well as use it as an adaptable RSS reader with Elfeed.

