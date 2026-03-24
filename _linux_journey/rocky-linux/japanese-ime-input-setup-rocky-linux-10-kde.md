---
title: "Japanese IME Input Setup - Rocky Linux 10 KDE"
category: "rocky-linux"
tags: ["rocky-linux", "japanese", "ime", "input", "setup"]
---

# Japanese IME Input Setup - Rocky Linux 10 KDE

## Overview

This guide provides step-by-step instructions for setting up Japanese input on Rocky Linux 10 with KDE Plasma desktop. The solution uses **IBus-Anthy**, which is already included in Rocky Linux 10 repositories.

**System Requirements:**
- Rocky Linux 10 (Red Quartz)
- KDE Plasma Desktop
- IBus 1.5.32 and IBus-Anthy 1.5.17 (usually pre-installed)

**Key Features:**
- No restart or logout required
- Works with all KDE applications
- Compatible with GTK and Qt applications
- Automatic startup on login
- Toggle with Ctrl+Space

---

## Quick Setup (One Command)

Save this script and run it for automatic setup:

```bash
#!/bin/bash
# Quick setup script for Japanese IME on Rocky Linux 10 with KDE
# This script enables IBus-Anthy without requiring logout or restart

set -e

echo "=== Enabling Japanese IME (IBus-Anthy) ==="
echo ""

# 0. Install required packages (CRITICAL: ibus-panel is needed!)
echo "0. Installing required IBus packages..."
sudo dnf install -y ibus ibus-panel ibus-anthy
echo "   ✓ Packages installed"

echo ""

# 1. Add environment variables to .bashrc
echo "1. Configuring environment variables..."
if ! grep -q "GTK_IM_MODULE=ibus" ~/.bashrc; then
    cat >> ~/.bashrc << 'EOF'

# IBus configuration for Japanese input
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
EOF
    echo "   ✓ Added to ~/.bashrc"
else
    echo "   ✓ Already configured in ~/.bashrc"
fi

# 2. Set environment variables for current session
echo ""
echo "2. Setting environment variables for current session..."
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
echo "   ✓ Environment variables set"

# 3. Create autostart directory
echo ""
echo "3. Setting up autostart..."
mkdir -p ~/.config/autostart

# 4. Create autostart file
cat > ~/.config/autostart/ibus.desktop << 'EOF'
[Desktop Entry]
Type=Application
Name=IBus Daemon
Exec=/usr/bin/ibus-daemon -drx
Icon=ibus
Comment=Start IBus input method daemon
X-GNOME-Autostart-enabled=true
EOF
echo "   ✓ Autostart configured"

# 5. Start IBus daemon
echo ""
echo "4. Starting IBus daemon..."
if pgrep -x ibus-daemon > /dev/null; then
    echo "   ✓ IBus daemon already running"
else
    ibus-daemon -drx
    sleep 2
    if pgrep -x ibus-daemon > /dev/null; then
        echo "   ✓ IBus daemon started"
    else
        echo "   ⚠ Failed to start IBus daemon (may need graphical session)"
    fi
fi

echo ""
echo "=== Setup Complete ==="
echo ""
echo "Next steps:"
echo "1. Open IBus Preferences: ibus-setup"
echo "2. Go to 'Input Method' tab"
echo "3. Click 'Add' → Select 'Japanese' → 'Anthy'"
echo "4. Test in any application with Ctrl+Space"
echo ""
echo "Keyboard shortcuts:"
echo "  - Ctrl+Space or Zenkaku/Hankaku: Toggle Japanese input"
echo "  - Space: Convert hiragana to kanji"
echo "  - Enter: Confirm"
echo ""
```

**To use the one-command script:**

```bash
# Copy the script above to a file
cat > /tmp/enable-japanese-ime.sh << 'EOF'
[paste script here]
EOF

# Make it executable
chmod +x /tmp/enable-japanese-ime.sh

# Run it
bash /tmp/enable-japanese-ime.sh
```

Then you will need to go into Settings --> Virtual Keyboards and enable Ibus Wayland. Then you may need to remove the autostart file and environment variables from bashrc for a Wayland session.

---

## Manual Setup Steps

### Step 1: Install Required Packages

Install IBus and all required components (**IMPORTANT:** must include `ibus-panel`):

```bash
# Install all required packages
sudo dnf install -y ibus ibus-panel ibus-anthy

# Verify installation
rpm -qa | grep -E "^ibus|ibus-panel|ibus-anthy"
```

**Critical Note:** The `ibus-panel` package is essential. Without it, IBus daemon will fail to start with errors like:
- "Unable to connect to ibus: Error receiving data: connection reset by peer"
- "IBus daemon could not be started in 5 seconds"

### Step 2: Configure Environment Variables

Add IBus environment variables to your shell profile:

```bash
cat >> ~/.bashrc << 'EOF'

# IBus configuration for Japanese input
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
EOF
```

**Apply immediately to current session:**

```bash
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
```

### Step 3: Set Up Autostart

Create autostart directory and configuration:

```bash
# Create autostart directory
mkdir -p ~/.config/autostart

# Create IBus autostart file
cat > ~/.config/autostart/ibus.desktop << 'EOF'
[Desktop Entry]
Type=Application
Name=IBus Daemon
Exec=/usr/bin/ibus-daemon -drx
Icon=ibus
Comment=Start IBus input method daemon
X-GNOME-Autostart-enabled=true
EOF
```

### Step 4: Start IBus Daemon

Start IBus in the current session (no restart needed):

```bash
ibus-daemon -drx
```

**Verify it's running:**

```bash
ps aux | grep ibus-daemon | grep -v grep
# or
pgrep ibus-daemon
```

### Step 5: Configure Japanese Input Method

Open IBus Preferences:

```bash
ibus-setup
```

**In the IBus Preferences window:**

1. Click the **Input Method** tab
2. Click the **Add** button
3. Select **Japanese** from the language list
4. Select **Anthy** from the available input methods
5. Click **Add**
6. Close the preferences window

### Step 6: Test Japanese Input

1. Open any text application:
   - Kate (text editor)
   - Firefox
   - LibreOffice
   - Konsole
   - Any Qt or GTK application

2. Press **Ctrl+Space** to activate Japanese input mode

3. Type in romaji (e.g., `konnichiwa`)
   - It will appear as hiragana: こんにちは

4. Press **Space** to convert to kanji
   - You'll see suggestions: 今日は

5. Press **Enter** to confirm the selection

---

## Keyboard Shortcuts

| Key Combination | Function |
|----------------|----------|
| **Ctrl+Space** | Toggle Japanese input on/off |
| **Zenkaku/Hankaku** | Alternative toggle (on Japanese keyboards) |
| **Space** | Convert hiragana to kanji (cycles through candidates) |
| **Enter** | Confirm current selection |
| **Escape** | Cancel conversion and revert to original text |
| **↑ ↓** | Navigate through kanji candidates |
| **F6** | Convert to hiragana |
| **F7** | Convert to katakana |
| **F8** | Convert to half-width katakana |
| **F9** | Convert to full-width alphanumeric |
| **F10** | Convert to half-width alphanumeric |

---

## Verification Commands

### Check if packages are installed:

```bash
# Check IBus
rpm -qa | grep ibus

# Check Anthy specifically
rpm -qa | grep ibus-anthy

# Check IBus version
ibus version
```

### Check environment variables:

```bash
echo $GTK_IM_MODULE
echo $QT_IM_MODULE
echo $XMODIFIERS
```

Expected output:
```
ibus
ibus
@im=ibus
```

### Check if IBus daemon is running:

```bash
pgrep -a ibus
```

### List available input engines:

```bash
ibus list-engine | grep anthy
```

Expected output:
```
anthy
```

---

## Troubleshooting

### Problem: "Unable to connect to ibus" or "IBus daemon could not be started in 5 seconds"

**Error messages:**
```
Unable to connect to ibus: Error receiving data: connection reset by peer
IBus daemon could not be started in 5 seconds
```

**Root Cause:** The `ibus-panel` package is missing.

**Solution:**

1. **Install the missing ibus-panel package:**
   ```bash
   sudo dnf install -y ibus-panel
   ```

2. **Verify the panel executable exists:**
   ```bash
   ls -la /usr/libexec/ibus-ui-gtk3
   ```

3. **Clean up stale cache and restart IBus:**
   ```bash
   killall -9 ibus-daemon 2>/dev/null || true
   rm -rf ~/.cache/ibus/dbus-*
   ibus-daemon -drx
   ```

4. **Verify IBus is running with all components:**
   ```bash
   pgrep -a ibus
   ```

   You should see multiple IBus processes including:
   - `ibus-daemon`
   - `/usr/libexec/ibus-ui-gtk3` (the panel)
   - `/usr/libexec/ibus-dconf`
   - `/usr/libexec/ibus-x11`

5. **Test ibus-setup:**
   ```bash
   ibus-setup
   ```

**Why this happens:** The `ibus-panel` package is in the CRB (CodeReady Builder) repository and is not installed by default with the base `ibus` package. It's a critical component required for IBus to function.

---

### Problem: Japanese input doesn't work in an application

**Solutions:**

1. **Check if IBus daemon is running:**
   ```bash
   pgrep ibus-daemon
   ```
   If not running:
   ```bash
   ibus-daemon -drx
   ```

2. **Restart the application** after starting IBus

3. **Verify environment variables:**
   ```bash
   echo $GTK_IM_MODULE $QT_IM_MODULE $XMODIFIERS
   ```
   Should output: `ibus ibus @im=ibus`

4. **For applications that don't respect environment variables:**
   - Close all instances of the application
   - Start IBus first: `ibus-daemon -drx`
   - Then launch the application from terminal with variables:
   ```bash
   GTK_IM_MODULE=ibus QT_IM_MODULE=ibus application-name
   ```

### Problem: IBus icon doesn't appear in system tray

**Solutions:**

1. **Run IBus setup manually:**
   ```bash
   ibus-setup
   ```

2. **Check KDE system tray settings:**
   - Right-click on system tray
   - Configure System Tray
   - Ensure IBus is not hidden

3. **Restart IBus daemon:**
   ```bash
   killall ibus-daemon
   ibus-daemon -drx
   ```

### Problem: Can't toggle Japanese input with Ctrl+Space

**Solutions:**

1. **Check if another application is using Ctrl+Space:**
   - KDE's KRunner might use this shortcut
   - Check System Settings → Shortcuts

2. **Use alternative toggle key:**
   - Try the **Zenkaku/Hankaku** key (on Japanese keyboards)
   - Or configure a different hotkey in `ibus-setup`

3. **Configure IBus hotkey:**
   ```bash
   ibus-setup
   ```
   - Go to **General** tab
   - Configure **Next input method** hotkey

### Problem: Japanese input works but wrong characters appear

**Possible causes:**

1. **Wrong keyboard layout selected**
   - In `ibus-setup`, ensure the Anthy input method uses "default" layout
   - Check KDE keyboard layout settings

2. **Multiple input methods active**
   - In `ibus-setup`, disable or remove other input methods temporarily
   - Test with only Anthy enabled

### Problem: IBus starts but Anthy is not in the list

**Solutions:**

1. **Reinstall IBus-Anthy:**
   ```bash
   sudo dnf reinstall ibus-anthy
   ```

2. **Verify component file exists:**
   ```bash
   ls -la /usr/share/ibus/component/anthy.xml
   ```

3. **Restart IBus to reload components:**
   ```bash
   killall ibus-daemon
   ibus-daemon -drx
   ```

---

## Alternative: Using Fcitx5 with Mozc

If you prefer **Google's Mozc** input method or **Fcitx5** framework, note that:

- **Fcitx5 and Mozc are NOT available** in Rocky Linux 10 official repositories
- They may be available through third-party repos or require compilation from source
- **IBus-Anthy is the recommended** and officially supported solution for Rocky Linux

---

## Additional Configuration

### Configure Anthy Input behaviour

Open IBus Preferences and select Anthy:

```bash
ibus-setup
```

Click on **Anthy** in the input method list, then click **Preferences**.

**Available settings:**

- **Input Mode**: Hiragana (default), Katakana, Half-width Katakana, Latin, Wide Latin
- **Typing Method**: Romaji (default) or Kana
- **Conversion Mode**: Multi-segment or Single-segment
- **Period Style**: Japanese (。、) or Western (.,)
- **Symbol Style**: Japanese or Western brackets and symbols
- **Dictionary**: Add custom words and phrases

### Adding Custom Words to Dictionary

1. Open Anthy preferences: `ibus-setup` → Select Anthy → Preferences
2. Go to **Dictionary** tab
3. Click **Add** to add custom word entries
4. Specify:
   - Reading (in hiragana)
   - Word (in kanji or any characters)
   - Type (noun, verb, etc.)

---

## System Information

**Tested Configuration:**
- **OS**: Rocky Linux 10.1 (Red Quartz)
- **Desktop**: KDE Plasma 6.2
- **IBus Version**: 1.5.32
- **Anthy Version**: 1.5.17
- **Input Method Engine**: IBus-Anthy

---

## References

- [IBus Project](https://github.com/ibus/ibus/wiki)
- [Anthy Project](https://github.com/ibus/ibus-anthy)
- [Rocky Linux Documentation](https://docs.rockylinux.org/)
- [KDE Input Methods](https://userbase.kde.org/Plasma/Input_Methods)

---

## Notes

- **No system restart required**: All changes take effect immediately
- **Persistent across reboots**: Autostart configuration ensures IBus starts automatically
- **Compatible with Wayland and X11**: Works on both display servers
- **GTK and Qt support**: Works in all major Linux applications
- **Low resource usage**: IBus-Anthy is lightweight and efficient

---

*Last updated: 2026-02-06*
*System: Rocky Linux 10.1 KDE*
