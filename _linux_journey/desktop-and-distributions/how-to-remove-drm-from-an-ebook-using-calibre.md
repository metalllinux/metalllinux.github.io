---
title: "Install DeDRM_tools_10.0.9 into a Flatpak Calibre (Linux)"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "remove", "drm", "ebook", "calibre"]
---

# Install DeDRM_tools_10.0.9 into a Flatpak Calibre (Linux)

Summary
Calibre flatpak runs sandboxed, so install the DeDRM plugin by extracting DeDRM_tools_10.0.9.zip and loading the inner DeDRM_plugin.zip into Calibre’s plugin loader. If Calibre can’t see the file because of Flatpak sandboxing, copy DeDRM_plugin.zip into a location the flatpak can access (e.g., your home, Desktop, or a flatpak‑exposed folder) or run calibre with access to that file. Steps below assume a standard Flatpak install.

Steps
Download and unzip the tools archive:
unzip DeDRM_tools_10.0.9.zip
inside the extracted folder find DeDRM_plugin.zip (do NOT unzip DeDRM_plugin.zip).
Put DeDRM_plugin.zip somewhere the flatpak can read:
Recommended: ~/Downloads or ~/Desktop.
If you prefer another folder, ensure the flatpak has access (see step 4).
Open the flatpak Calibre app:
Launch Calibre normally (Applications menu).
If Calibre can’t access the file due to sandbox restrictions, either:
Move DeDRM_plugin.zip into ~/Downloads, ~/Desktop, or your Home; flatpak apps typically can read these.
Or grant the calibre flatpak extra filesystem access (optional):
Run: flatpak override --user --filesystem=/path/to/folder com.calibre_ebook.calibre
Replace /path/to/folder with the folder containing DeDRM_plugin.zip.
Install the plugin in Calibre:
Preferences → Plugins (Advanced → Plugins).
Click “Load plugin from file”.
Navigate to and select DeDRM_plugin.zip (the one extracted from the tools archive).
Confirm the security warning and accept the install.
Restart Calibre when prompted.
Configure DeDRM (if needed):
In Plugins list find DeDRM under “File type plugins” (or show only user plugins).
Select it → Customise plugin → enter keys/serials (Kindle serials, ADE keys, etc.) per your sources.
Test:
Remove and re‑import a DRMed book into Calibre; the plugin removes DRM during import.


