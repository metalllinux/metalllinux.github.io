---
title: "To Add A Device And Sync The Default Folder Via Th"
category: "general-linux"
tags: ["add", "device", "sync", "default", "folder"]
---

syncthing cli config devices add --device-id $DEVICE_ID_B

syncthing cli config folders $FOLDER_ID devices add --device-id $DEVICE_ID_B

The default folder ID would be `default`

Find the device ID with this command.

syncthing cli show system | jq .myID