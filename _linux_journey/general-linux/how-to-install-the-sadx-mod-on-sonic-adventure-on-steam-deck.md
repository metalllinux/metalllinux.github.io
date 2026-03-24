---
title: "Sonic Adventure DX – Mod installation (Steam Deck, GUI only)"
category: "general-linux"
tags: ["install", "sadx", "mod", "sonic", "adventure"]
---

# Sonic Adventure DX – Mod installation (Steam Deck, GUI only)

## What you need
- **Protontricks** – install it from the Discover store on the Deck (Flatpak is the recommended package).  
- **SADX Mod Installer** – the official Windows installer (`sadx_setup.exe`).  
  Download it from the project page: https://gitlab.com/PiKeyAr/sadx-mod-installer  

## Preparation
1. **Launch the game once** in Gaming mode and quit.  
   This creates the Proton compatibility folder for the game (AppID 71250).  

2. **Switch to Desktop mode** (Steam → Power → “Switch to Desktop”).

## Using Protontricks GUI to run the installer
1. Open the **File Manager** and navigate to the folder where you saved `sadx_setup.exe` (usually `~/Downloads`).  

2. **Right‑click** on `sadx_setup.exe` → **“Open With Protontricks”** → choose **“Sonic Adventure DX (AppID 71250)”** from the list.  
   *Protontricks will automatically pick the correct Proton prefix for the game*[0](#ref-0)[1](#ref-1).  

3. The **SADX Mod Installer** window appears.  
   - It detects the Steam installation path (`…/steamapps/common/Sonic Adventure DX`).  
   - In **Guide/Selection mode** tick the mods you want. Typical “best‑experience” set:  
     - **Dreamcast Conversion** (core graphics & models)[0](#ref-0)  
     - **BetterSADX / HD GUI** (menu polish, controller support)[4](#ref-4)  
     - **Texture Upscale (xBRZ / ESRGAN)** (higher‑res textures)[3](#ref-3)  
     - **Sound‑overhaul** (optional music replacement)[6](#ref-6)  
   - Click **Install** and wait while the installer patches the Steam executable, copies the selected mods into a `mods` sub‑folder, and writes a tiny configuration file.  

4. When the installer finishes, close it.

## Back to Gaming mode & launch
1. Click the **Steam** icon on the task‑bar → **“Return to Gaming Mode.”**  

2. In your library select **Sonic Adventure DX** → **Play**.  
   You should now see the Dreamcast opening cinematic, up‑scaled textures, and any extra audio you chose.

## Tweaking later (still GUI‑only)
- To enable/disable individual mods, open the game folder (`…/Sonic Adventure DX`) in Desktop mode, right‑click **`SADXModManager.exe`** → **“Open With Protontricks”** → select the SADX AppID.  
- The Mod Manager UI lets you reorder, toggle, or configure each mod without leaving the GUI[0](#ref-0).
