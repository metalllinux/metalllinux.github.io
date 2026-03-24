---
title: "Installation Guide for StarCraft 1998 and Brood War Expansion from CD with Lutris"
category: "general-linux"
tags: ["starcraft", "brood", "war", "expansion", "install"]
---

## Installation Guide for StarCraft 1998 and Brood War Expansion from CD with Lutris
* * *
### This guide is for those that wish to install the game using the original CD.
#### Retrieving the Game Files
- For the CD version, Blizzard created two partitions - one for Windows and one for macOS.
- Firstly, create an ISO image of the CD. I used Brasero on my Fedora 36 machine.
	- If you create a .bin and .cue version of the CD, you can output an ISO file by using the application `bchunk` with `bchunk sc.bin sc.cue sc.iso`
- Next, **please do not mount the ISO image.** Linux will mount the macOS partition instead and you will not be able to access the Windows partition, which is where the required game files are .
	- Instead, please open the ISO in your favourite archive manager (I used Archive Manager on Fedora 36 Workstation) and you will then be able to extract the Windows game files that you need.
#### Installing StarCraft Through the Community Lutris Install Script
- Next open Lutris, click the "plus" icon on the top left-hand corner and then select the `Search the Lutris website for installers` option.
- After that, search for `Starcraft` and select the option that has `Starcraft 1998 Mac,Windows` in the title name.
- Then select the `wine` -> `CD` option and click `Install`. Many thanks to the person who wrote this script.
- When the installer prompts for the game files, point the installer at the directory you extracted the Windows game files at.
- The latest official StarCraft 1.16.1 patch is also downloaded from archive.org and installed.
- When you hit `Play` in Lutris and start the game, the game will complain that it is missing files from the CD.
	- To bypass this, grab `INSTALL.EXE`from the Windows game files and copy that into your StarCraft directory inside the WINE Prefix. Then rename `INSTALL.EXE` to `StarCraft.mpq` 
- FInally, right-click on the StarCraft application within Lutris, select `Configure` -> `Runner options` and toggle `Windowed(virtual desktop` on.
	- I found that if I didn't do this, the game would start with a black screen.
#### Installing Brood War Manually
- I unfortunately had difficulties installing Brood War via the community install scripts. Even after editing the scripts to the exact path of my install directory, they still hanged. I will have to do some editing and testing of the scripts when times allows.
-  Instead, run the same steps as mentioned above for creating the ISO file and extracting the Windows game files for the Brood War expansion.
-  Then click on your StarCraft install in Lutris, click the dropdown arrow next to the WINE icon at the bottom of the application and select `Run EXE inside Wine prefix`.
-  Select your `SETUP.exe` file in your Brood War Windows game files and install the expansion (the expansion will automatially be installed in your WINE Prefix's StarCraft directory).
-  Once done, copy the `INSTALL.exe` file from your Brood War Windows game files and place that into your StarCraft directory within your WINE Prefix.
	-  Rename the `INSTALL.exe` file to `BroodWar.mpq`, so the game again doesn't complain to you about not having some of the required files from the CD.
- Install the Brood War 1.16.1 patch from [archive.org](https://web.archive.org/web/20140908042547/http://ftp.blizzard.com/pub/starcraft/patches/PC/SC-1161.exe) using the same method listed above for running an exe file within the WINE Prefix. **YOU CAN SKIP THIS STEP, IF YOU INSTALLED STARCRAFT THROUGH THE COMMUNITY LUTRIS INSTALL SCRIPT.**
-  Once done, just run StarCraft as normal via Lutris and once you get into the game and click on "Single Player", you will then be given the option to play the original campaign or the Brood War expansion.
#### Testing
-  The game runs at 640x480 natively, so you have to adjust your display. I change my display to 800x600 and the game is very playable.
- I have played 2 hours 50 minutes of the original StarCraft, without a single crash or issues with video, graphics, audio or controls.
- Multiplayer was not tested.
- I started up Brood War, to at least make sure it works.
#### Closing Thoughts
- I hope this guide helps someone easily install and play StarCraft on their Linux box and have as much fun playing this game as I did in 1998 and continue to do so today. "Let's Burn!"