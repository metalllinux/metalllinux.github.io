---
title: "Handbrake Cli Commands"
category: "general-linux"
tags: ["handbrake", "cli", "commands"]
---

* Bluray:
HandBrakeCLI -i /mnt/murmaider/videos/Peter_Rabbit/Peter\ Rabbit-B1_t00.mkv -o /mnt/murmaider/videos/Peter_Rabbit.mkv --x264-preset veryslow --x264-tune film --x264-profile high -q 20 -2 -T --vfr -a 1,2,3,4,5,6 -E vorbis -B 320 -6 6ch -s 1,2,3,4,5,6,7,8,9,10 -N eng
* DVD:
HandBrakeCLI -i <input_file>-o <output_file> --x264-preset veryslow --x264-tune film --x264-profile high -q 16 -2 -T --vfr -a 1,2,3,4,5 -E vorbis -B 320 -6 6ch -s 1,2,3,4,5,6,7,8,9,10 -N eng