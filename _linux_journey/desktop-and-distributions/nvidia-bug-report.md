---
title: "Nvidia Bug Report"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "nvidia", "bug", "report"]
---

If you have a problem, and would like assistance, please follow these steps:

1.  Please always include a detailed description of the problem (both when starting a new thread and when posting to existing threads), as distinct problems can have nearly identical symptoms (e.g. black screens, hung X servers, …). Reliable reproduction steps are especially useful. If you post a reply reading “I have the same problem” in response to another user’s bug report without the information requested in this post, you may make it more difficult for NVIDIA to track and diagnose the problem.
    
2.  **Please always include a copy of an `nvidia-bug-report.log.gz` file**, which can be generated with the `nvidia-bug-report.sh` script shipped with the NVIDIA Linux/FreeBSD graphics drivers and installed in your PATH; the log file will be placed in the current working directory. Attach the log file by clicking the Upload ![upload](../_resources/ea00e0e399b87cd1e9a5e93020868cf1_688c47937a424fdea-1.png) button in the post composition window.
    
    To make sure this log file includes as much relevant information as possible, please start the X server with `startx -- -logverbose 6` and run `nvidia-bug-report.sh` after the problem has occurred. If X can not be started or the machine appears to have crashed, please check if you can log into it remotely (e.g. via ssh) and run `nvidia-bug-report.sh` in the remote shell, if possible.
    
    If the machine can not be logged into remotely, please run the bug report script with X running (this will ensure that data points only available when the device is initialised, such as the VBIOS revision, are captured in the log file). All requests for assistance from NVIDIA must include the bug report, per the instructions above.
    
    If `nvidia-bug-report.sh` appears to hang, it may still have collected enough useful information about your problem. In this case, please provide the partial log file generated, if any.
    
3.  In case of NVIDIA Linux graphics driver installation problems (when using one of the official .run installers), please attach the NVIDIA installer log file, `/var/log/nvidia-installer.log`.
    
4.  If you have collected additional information, but are not sure if it is relevant / appropriate, please attach it anyway.
    
5.  When creating a new thread, please make the thread subject as descriptive as possible. For example,
    
    - Good title: "X server 1.2 crashes when Kopete opens a popup notification on GeForce 8800 GTX"
    - Bad title: "The X server keeps crashing"
    - Really bad title: "Help me!"

This information will help us help you.

Thanks!

- #### created
    
    <img width="24" height="24" src="../_resources/14043_2_6e3dee2adada4ff698260ca17b2de031-1.png"/> Nov 2012
    
- [#### last reply<br>![](https://sea2.discourse-cdn.com/nvidia/user_avatar/forums.developer.nvidia.com/aplattner/48/14043_2.png "aplattner") 28 Jun](https://forums.developer.nvidia.com/t/if-you-have-a-problem-please-read-this-first/27131/2)
- 148k
    
    #### views
    
- 1
    
    #### user
    
- 10
    
    #### likes
    
- 18
    
    #### links
    

If you have a problem running an application using VDPAU, please run the following commands, then run the failing command again, and post the results:

```
# If you use bash:
export VDPAU_TRACE=2
export VDPAU_NVIDIA_DEBUG=3
export VDPAU_TRACE_FILE=mplayer.log

# If you use csh:
setenv VDPAU_TRACE 2
setenv VDPAU_NVIDIA_DEBUG 3
setenv VDPAU_TRACE_FILE mplayer.log
```

Please also generate and post an “nvidia bug report” by running **nvidia-bug-report.sh** as root.

Please upload a copy of the media file you were playing. Even a short portion of the clip (e.g. truncated to include the first 5 seconds) should be enough for us to diagnose initialisation problems at least. We now accept files using the NVIDIA file drop:

- sftp to [partners.ftp.nvidia.com 5](http://partners.ftp.nvidia.com/) (note: scp will not work; use interactive sftp)

```
cd /path/to/your/local/file
sftp vdpau@partners.ftp.nvidia.com
...
vdpau@partners.ftp.nvidia.com's password:     [press enter/return]
...
sftp> put the_filename.ext
sftp> exit
```

The user ID is vdpau with no password (i.e. empty/blank). Simply upload files to whatever directory the system places you into. You will be able to upload files, and possibly list files, but not download files. Please let us know if you have any difficulties using this system.

Finally, please include the version of mplayer you tested with. You can determine this with

```
mplayer --help | tail -n 2
```

If you’re having problems with MPlayer, please try using the built-in software codecs, and see if the file plays correctly. To do this, use the same MPlayer command-line, but substitute the -vc parameter as follows:

ffmpeg12vdpau → ffmpeg12  
ffh264vdpau → ffh264  
ffwmv3vdpau → ffwmv3  
ffvc1vdpau → ffvc1

e.g.:

```
# HW accelerated:
./mplayer -vo vdpau -vc ffmpeg12vdpau file.mpg

# SW decoding:
./mplayer -vo vdpau -vc ffmpeg12 file.mpg
```

Some MPlayer problems may be solved by using a different demuxer; specify “-demuxer lavf” on the command-line.

When possible, please file video playback, corruption, slowness, and other such bugs using MPlayer as the video player. If MPlayer and another VDPAU-enabled media player (such as Xine or MythTV) exhibit different behaviour, please be sure to note that as well.