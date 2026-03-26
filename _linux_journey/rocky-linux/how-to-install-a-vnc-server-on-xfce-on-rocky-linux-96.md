---
title: "How to Install a VNC Server on XFCE on Rocky Linux 9.6"
category: "rocky-linux"
tags: ["rocky-linux", "install", "vnc", "server", "xfce"]
---

# How to Install a VNC Server on XFCE on Rocky Linux 9.6

# TigerVNC Server Setup on Rocky Linux 9.6 with XFCE

This guide provides the complete steps to set up a working TigerVNC server on Rocky Linux 9.6 with XFCE desktop environment, specifically configured to work with NVIDIA GPUs.

## Prerequisites

- Rocky Linux 9.6 with XFCE desktop environment already installed
- System with NVIDIA GPU (tested with A2000)
- Sudo user with admin rights
- System updated and rebooted

## Step 1: Install TigerVNC Server

```bash
# Update the system
sudo dnf update -y

# Install TigerVNC server
sudo dnf install tigervnc-server -y
```

## Step 2: Configure VNC Service

```bash
# Copy the VNC service template for display :3
sudo cp /usr/lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@:3.service

# Configure VNC users file
sudo tee /etc/tigervnc/vncserver.users << EOF
:3=myuser
EOF

# Replace 'myuser' with your actual username
```

## Step 3: Set VNC Password

```bash
# Set VNC password for your user
vncpasswd

# When prompted:
# - Enter a password (6-8 characters recommended)
# - Confirm the password
# - Type 'n' when asked about view-only password
```

## Step 4: Fix System-wide VNC Configuration

Rocky Linux defaults to GNOME sessions which cause black screen issues with NVIDIA GPUs. Fix this:

```bash
# Edit the system-wide VNC defaults
sudo vim /etc/tigervnc/vncserver-config-defaults

# Find the line that says:
# session=gnome

# Change it to:
# session=xfce
```

Or use sed to make the change automatically:

```bash
sudo sed -i 's/session=gnome/session=xfce/' /etc/tigervnc/vncserver-config-defaults
```

## Step 5: Configure VNC User Settings

Create VNC configuration files in your home directory:

```bash
# Create VNC directory
mkdir -p ~/.vnc

# Create VNC config file
cat > ~/.vnc/config << EOF
session=xfce
securitytypes=vncauth,tlsvnc
geometry=1920x1080
localhost=no
alwaysshared=yes
EOF

# Create xstartup script with software rendering (critical for NVIDIA systems)
cat > ~/.vnc/xstartup << 'EOF'
#!/bin/bash
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
export LIBGL_ALWAYS_SOFTWARE=1
export __GLX_VENDOR_LIBRARY_NAME=mesa
export GALLIUM_DRIVER=llvmpipe
export XKL_XMODMAP_DISABLE=1
exec dbus-launch --exit-with-session startxfce4
EOF

# Make xstartup executable
chmod +x ~/.vnc/xstartup

# Set session preference
echo "startxfce4" > ~/.session
```

## Step 6: Configure Firewall

```bash
# Allow VNC server through firewall
sudo firewall-cmd --permanent --add-service=vnc-server
sudo firewall-cmd --permanent --add-port=5903/tcp

# Reload firewall
sudo firewall-cmd --reload
```

## Step 7: Start and Enable VNC Service

```bash
# Reload systemd configuration
sudo systemctl daemon-reload

# Start VNC service
sudo systemctl start vncserver@:3.service

# Enable VNC service to start at boot
sudo systemctl enable vncserver@:3.service
```

## Step 8: Verify VNC Server is Running

```bash
# Check service status
sudo systemctl status vncserver@:3.service

# Verify VNC is listening on port 5903
sudo netstat -tlnp | grep 5903

# Check XFCE processes are running
ps aux | grep xfce | grep -v grep

# Check VNC log for any issues
cat ~/.vnc/$(hostname):3.log
```

## Step 9: Connect to VNC Server

Use a VNC client to connect:

- **Server**: `YOUR_SERVER_IP:3` or `YOUR_SERVER_IP:5903`
- **Password**: The password you set with `vncpasswd`

Replace `YOUR_SERVER_IP` with your actual server IP address.

## Troubleshooting

### If VNC Service Fails to Start or Crashes

1. Check the VNC log file:
   ```bash
   cat ~/.vnc/$(hostname):3.log
   ```

2. Look for graphics driver errors like:
   ```
   failed to load driver: nouveau
   glx: failed to create dri3 screen
   ```

3. Ensure the software rendering environment variables are set in `~/.vnc/xstartup`

### If You Get a Black Screen

This usually means GNOME session is still being used instead of XFCE:

1. Verify the system configuration:
   ```bash
   sudo cat /etc/tigervnc/vncserver-config-defaults | grep session
   ```
   Should show `session=xfce`

2. Check your VNC log shows:
   ```
   Using desktop session xfce
   ```

### Expected Warning Messages

The following warnings in the VNC log are normal and don't affect functionality:
- DPMS extension missing
- Power manager warnings
- Notification proxy failures
- Backlight property warnings

## Key Points for NVIDIA GPU Systems

1. **Software rendering is essential**: The `LIBGL_ALWAYS_SOFTWARE=1` environment variable prevents VNC from trying to use GPU acceleration
2. **XFCE works better than GNOME**: GNOME has known compatibility issues with VNC on NVIDIA systems
3. **llvmpipe renderer**: The log should show `Unsupported GL renderer (llvmpipe...)` which confirms software rendering is active

## Security Notes

- VNC traffic is not encrypted by default. For production use, consider:
  - Setting `localhost=yes` in config and using SSH tunneling
  - Using VNC over SSL/TLS
  - Restricting firewall access to specific IP ranges

## Display Numbers and Ports

- Display `:3` uses port `5903`
- Display `:1` uses port `5901`  
- Display `:2` uses port `5902`
- General formula: Port = 5900 + display number

I've created a comprehensive guide that consolidates all the working steps from our troubleshooting session. The guide focuses on the key solutions that resolved your black screen issue:

1. **Switching from GNOME to XFCE** in the system-wide VNC configuration
2. **Implementing software rendering** to bypass NVIDIA GPU conflicts
3. **Proper VNC configuration** with the correct environment variables

The most critical parts for systems with NVIDIA GPUs are:
- Editing `/etc/tigervnc/vncserver-config-defaults` to change `session=gnome` to `session=xfce`
- Setting the software rendering environment variables in the xstartup script (`LIBGL_ALWAYS_SOFTWARE=1`, etc.)

This guide should work reliably on your fresh Rocky Linux 9.6 installation with XFCE pre-installed, avoiding the graphics driver conflicts that were causing the session crashes and black screens.
