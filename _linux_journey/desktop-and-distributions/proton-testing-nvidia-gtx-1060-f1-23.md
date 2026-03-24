---
title: "nvidia-driver-535 - Proton 8.0-5"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "proton", "testing", "nvidia", "gtx"]
---

# nvidia-driver-535 - Proton 8.0-5
## Test 1
* Game version: `1.21.1093534`
* Selected - `No, I only want to play within my current platform`
* Game boots into main menu.
* Selected `Cancel and play offline.`
* All accessibility options set to `Off`.
### Graphical Settings
* Motion Blur Strength: `0`
* Steering Animation: `Off`
* Resolution: `1024x768`
* Display Mode: `Windowed`
* Aspect Ration: `Auto`
* VSync: `Off`
* Frame Rate Limit: `Off`
* Anisotropic Filtering: `Off`
* Anti-Aliasing: `TAA Only`
* Dynamic Resolution: `Off`
* HDR: `Off`
* Detail Preset: `Low`
* Weather Effects: `Low`
* Asynchronous Compute: `Off`
* Variable Rate Shading: `Off`
* Selected `Breaking Point`
* Selected `Normal`
* Selected `Start Breaking Point 2`
* Selected `Skip cinematic`
### Result
* Game crashes at the `Miami Grand Prix` screen.
* Eventually the game boots back to Steam.
## Test 2
* Same Graphics Settings as above.
* Autosave: `Off`
* On-Screen Display: `Off`
### Audio Settings
* Audio Simulation Quality: `Ultra Low`
* Formation Lap Parking Sensor: `Off`
* Radio Verbosity: `Response Only`
* Play Victory Radio Calls: `Off`
* Replay Music: `Off`
* Music Spatialisation: `Off`
* Music Type: `Theme`
### Telemetry Settings
* D-BOX: `Off`
* Fanatec LED: `Off`
* SLI Pro LED: `Off`
### EA Music
* Music Type: `Theme`
### Crossplay
* Crossplay: `Disabled`
### Simulation Settings
* Flashback Limit: `Low`
* Surface Type: `Simplified`
* Race Starts: `Manual`
### Rules & Flags
* Pit Stop Experience: `Broadcast`
### Result
* Game crashes at the `Miami Grand Prix` screen.
* Eventually the game boots back to Steam.
## Test 3
### Result
* Game crashes at the `choose avatar` screen in `Career` Mode.
# Upgraded to nvidia-550 Drivers
* Followed: https://ubuntu.com/server/docs/nvidia-drivers-installation
* Ran `sudo apt install linux-modules-nvidia-550-generic`
* Rebooted.
### Result
* Attempting to boot the game will crash on a black screen.
### Reverted Nvidia Drivers to Version 535
* Ran `sudo apt --purge remove '*nvidia*generic*'`
* Ran `sudo apt autoremove`
* Switched Back to nvidia-535 Drivers
# nvidia-driver-535 - GE-Proton9-5
* Enable the Steam Overlay while in-game: `Disabled`
* Steam Cloud: `Disabled`
### Result
* Running the game goes to a black screen and then crashes.