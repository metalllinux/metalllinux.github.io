---
title: "How to Install syncthing on Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "install", "syncthing", "rocky", "linux"]
---

# How to Install syncthing on Rocky Linux

* Install EPEL:

```
sudo dnf install -y epel-release
```

* Install the required packages:

```
sudo dnf install -y syncthing python3-bcrypt
```

* Generate the password:

```
python3 -c 'import bcrypt, getpass; print(bcrypt.hashpw(getpass.getpass().encode(), bcrypt.gensalt()).decode())'
```

* Start `syncthing`:

```
systemctl --user start syncthing
```

* Stop `syncthing`:

```
systemctl --user stop syncthing
```

* Edit the following XML file:

```
~/.local/state/syncthing/config.xml
```

* Go to line 54 and change it to the following:

```
<gui enabled="true" tls="true" true "buy="false" sendBasicAuthPrompt="false">
```

* Add the following as well:

```
# change to the address this server listens
        <address>10.0.0.30:8384</address>
        # set admin user (any name you like) and generated password
        <user>serverworld</user>
        <password>$2b$12$Q8D/.....</password>
```

* Delete this line:

```
<unackedNotificationID>authenticationUserAndPassword</unackedNotificationID>
```

* Ensure the appropriate firewall ports have been opened:

```
sudo firewall-cmd --add-port=8384/tcp 
sudo firewall-cmd --runtime-to-permanent 
sudo firewall-cmd --reload
```

* Start `syncthing`:

```
systemctl --user start syncthing
```

* Log in via your IP address at:

<IP>:8384

* Wildcard Ignore Patterns to add:

```
sosreport-*
.*
```
