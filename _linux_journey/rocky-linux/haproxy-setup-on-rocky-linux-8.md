---
title: "Haproxy Setup On Rocky Linux 8"
category: "rocky-linux"
tags: ["rocky-linux", "haproxy", "setup", "rocky", "linux"]
---

* I set up and updated all packages on three new Rocky Linux 8.10 VMs. One was to act as the HAProxy Load Balancer and the other two nodes are for distributing traffic between. My IP scheme was the following:
* HA Proxy Load Balancer (rocky-linux-810-1): 192.168.1.24
* Backend Server 1 (rocky-linux-810-2): 192.168.1.25
* Backend Server 2 (rocky-linux-810-3): 192.168.1.26

* Installed the `haproxy` package:
```
sudo dnf install -y haproxy
```
* Edited `/etc/haproxy/haproxy.cfg` and changed the `frontend` and `backend` configuration:
```
cat << "EOF" | sudo tee /etc/haproxy/haproxy.cfg
# Global settings
global
    log         /dev/log local0 debug
    chroot      /var/lib/haproxy
    pidfile     /var/run/haproxy.pid
    maxconn     4000
    user        haproxy
    group       haproxy
    daemon

    # turn on stats unix socket
    stats socket /var/lib/haproxy/stats

    # utilize system-wide crypto-policies
    ssl-default-bind-ciphers PROFILE=SYSTEM
    ssl-default-server-ciphers PROFILE=SYSTEM

# common defaults that all the 'listen' and 'backend' sections will
# use if not designated in their block
defaults
    mode                    tcp
    retries                 3
    timeout queue           1m
    timeout connect         10s
    timeout client          1m
    timeout server          1m
    timeout check           10s
    maxconn                 3000

# main frontend which proxys to the backends
frontend rocky_linux_810_load_balancer
    bind 192.168.1.24:23
    default_backend             rocky_linux_810_login_nodes

# static backend for serving up images, stylesheets and such
backend rocky_linux_810_login_nodes
    mode tcp
    balance     leastconn
    server      rocky-linux-810-2 192.168.1.25:23 check
    server      rocky-linux-810-3 192.168.1.26:23 check
EOF
```
* Checked the `haproxy` configuration:
```
haproxy -c -f /etc/haproxy/haproxy.cfg
```
* Created the `/dev` directory for the `haproxy` logs:
```
sudo mkdir /var/lib/haproxy/dev
```
* Generated the `rsyslog` configuration file so that `rsyslog` starts to handle the `haproxy` logs:
```
cat << "EOF" | sudo tee /etc/rsyslog.d/99-haproxy.conf
$AddUnixListenSocket /var/lib/haproxy/dev/log

# Send HAProxy messages to a dedicated logfile
:programname, startswith, "haproxy" {
  /var/log/haproxy.log
  stop
}
EOF
```
* Restarted the `syslog` service:
```
sudo systemctl restart syslog
```
* Disabled SELinux:
```
sudo setenforce 0
sudo sed -i 's/SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config
```
* Allowed traffic through on `ssh` port `23`:
```
sudo firewall-cmd --zone=public --add-port=23/tcp --permanent
sudo firewall-cmd --reload
```
* Enabled and started the `haproxy` service:
```
sudo systemctl enable --now haproxy
```
* Checked I could connect to port `23` successfully:
```
nc -zv 192.168.1.24 23
```

#### Backend Server Configuration

* Edited the `sshd` config to use port `23`:
```
cat << "EOF" | sudo tee /etc/ssh/sshd_config
#       $OpenBSD: sshd_config,v 1.103 2018/04/09 20:41:22 tj Exp $

# This is the sshd server system-wide configuration file.  See
# sshd_config(5) for more information.

# This sshd was compiled with PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin

# The strategy used for options in the default sshd_config shipped with
# OpenSSH is to specify options with their default value where
# possible, but leave them commented.  Uncommented options override the
# default value.

# If you want to change the port on a SELinux system, you have to tell
# SELinux about this change.
# semanage port -a -t ssh_port_t -p tcp #PORTNUMBER
#
Port 23
#AddressFamily any
#ListenAddress 0.0.0.0
#ListenAddress ::

HostKey /etc/ssh/ssh_host_rsa_key
HostKey /etc/ssh/ssh_host_ecdsa_key
#In FIPS mode Ed25519 keys are not supported, please comment out the next line
HostKey /etc/ssh/ssh_host_ed25519_key

# Ciphers and keying
#RekeyLimit default none

# This system is following system-wide crypto policy. The changes to
# crypto properties (Ciphers, MACs, ...) will not have any effect here.
# They will be overridden by command-line options passed to the server
# on command line.
# Please, check manual pages for update-crypto-policies(8) and sshd_config(5).

# Logging
#SyslogFacility AUTH
SyslogFacility AUTHPRIV
#LogLevel INFO

# Authentication:

#LoginGraceTime 2m
PermitRootLogin yes
#StrictModes yes
#MaxAuthTries 6
#MaxSessions 10

#PubkeyAuthentication yes

# The default is to check both .ssh/authorized_keys and .ssh/authorized_keys2
# but this is overridden so installations will only check .ssh/authorized_keys
AuthorizedKeysFile      .ssh/authorized_keys

#AuthorizedPrincipalsFile none

#AuthorizedKeysCommand none
#AuthorizedKeysCommandUser nobody

# For this to work you will also need host keys in /etc/ssh/ssh_known_hosts
#HostbasedAuthentication no
# Change to yes if you don't trust ~/.ssh/known_hosts for
# HostbasedAuthentication
#IgnoreUserKnownHosts no
# Don't read the user's ~/.rhosts and ~/.shosts files
#IgnoreRhosts yes

# To disable tunneled clear text passwords, change to no here!
#PasswordAuthentication yes
#PermitEmptyPasswords no
PasswordAuthentication yes

# Change to no to disable s/key passwords
#ChallengeResponseAuthentication yes
ChallengeResponseAuthentication no

# Kerberos options
#KerberosAuthentication no
#KerberosOrLocalPasswd yes
#KerberosTicketCleanup yes
#KerberosGetAFSToken no
#KerberosUseKuserok yes

# GSSAPI options
GSSAPIAuthentication yes
GSSAPICleanupCredentials no
#GSSAPIStrictAcceptorCheck yes
#GSSAPIKeyExchange no
#GSSAPIEnablek5users no

# Set this to 'yes' to enable PAM authentication, account processing,
# and session processing. If this is enabled, PAM authentication will
# be allowed through the ChallengeResponseAuthentication and
# PasswordAuthentication.  Depending on your PAM configuration,
# PAM authentication via ChallengeResponseAuthentication may bypass
# the setting of "PermitRootLogin without-password".
# If you just want the PAM account and session checks to run without
# PAM authentication, then enable this but set PasswordAuthentication
# and ChallengeResponseAuthentication to 'no'.
# WARNING: 'UsePAM no' is not supported in RHEL and may cause several
# problems.
UsePAM yes

#AllowAgentForwarding yes
#AllowTcpForwarding yes
#GatewayPorts no
X11Forwarding yes
#X11DisplayOffset 10
#X11UseLocalhost yes
#PermitTTY yes

# It is recommended to use pam_motd in /etc/pam.d/sshd instead of PrintMotd,
# as it is more configurable and versatile than the built-in version.
PrintMotd no

#PrintLastLog yes
#TCPKeepAlive yes
#PermitUserEnvironment no
#Compression delayed
#ClientAliveInterval 0
#ClientAliveCountMax 3
#UseDNS no
#PidFile /var/run/sshd.pid
#MaxStartups 10:30:100
#PermitTunnel no
#ChrootDirectory none
#VersionAddendum none

# no default banner path
#Banner none

# Accept locale-related environment variables
AcceptEnv LANG LC_CTYPE LC_NUMERIC LC_TIME LC_COLLATE LC_MONETARY LC_MESSAGES
AcceptEnv LC_PAPER LC_NAME LC_ADDRESS LC_TELEPHONE LC_MEASUREMENT
AcceptEnv LC_IDENTIFICATION LC_ALL LANGUAGE
AcceptEnv XMODIFIERS

# override default of no subsystems
Subsystem       sftp    /usr/libexec/openssh/sftp-server

# Example of overriding settings on a per-user basis
#Match User anoncvs
#       X11Forwarding no
#       AllowTcpForwarding no
#       PermitTTY no
#       ForceCommand cvs server
EOF
```
* I enabled port `23` on `firewalld` for both servers:
```
sudo firewall-cmd --zone=public --add-port=23/tcp --permanent
sudo firewall-cmd --reload
```
* I disabled SELinux:
```
sudo setenforce 0
sudo sed -i 's/SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config
```
* I restarted the `sshd` service on both servers:
```
sudo systemctl restart sshd
```