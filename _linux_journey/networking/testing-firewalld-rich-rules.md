---
title: "Testing Firewalld Rich Rules"
category: "networking"
tags: ["networking", "testing", "firewalld", "rich", "rules"]
---

# Testing Firewalld Rich Rules

Great — with two Rocky Linux 8.10 machines (let’s call them `firewall-host` and `client-host`), here’s a complete **test case** to validate your rich rule setup for port range access and blocking.

---

## ✅ **Step-by-Step Test Case**

### **1. On `firewall-host`: Set Up the Rich Rules**

```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" port port="60000-61000" protocol="tcp" accept'
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.2.0/24" port port="60000-61000" protocol="tcp" accept'
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" port port="60000-61000" protocol="tcp" drop'
sudo firewall-cmd --reload
```

### **2. On `firewall-host`: Start a test TCP server**

Install `socat` or `ncat` if not present:

```bash
sudo dnf install -y nmap-ncat
```

Start listeners on a few ports **in** and **out** of the range:

```bash
# In-range port (should be accepted)
ncat -lkp 60010 &

# Out-of-range port (should be blocked)
ncat -lkp 59000 &
```

### **3. On `client-host`: Try connecting from allowed subnet**

Assume `client-host` IP is in `192.168.1.0/24` or `192.168.2.0/24`.

Install `ncat` if needed:

```bash
sudo dnf install -y nmap-ncat
```

Run:

```bash
# Should succeed
ncat <FIREWALL-HOST-IP> 60010

# Type something, it should echo or remain connected

# Should fail (connection refused or timeout)
ncat <FIREWALL-HOST-IP> 59000
```

If 60010 connects and 59000 doesn't, **the rules are working correctly**.

### **4. From a non-allowed IP (optional negative test)**

If you have a third system on a different subnet (not in the /24 ranges), try the same connection to `60010`. It should **fail**, verifying the `drop` rule works.

---

## 🔎 Verifying the Connections

On `firewall-host`, you can check incoming connections:

```bash
sudo ss -tnlp | grep 60010
```

Also monitor logs (if log-deny is enabled):

```bash
sudo journalctl -f | grep firewalld
```

Or enable logging for debugging:

```bash
sudo firewall-cmd --set-log-denied=all
```

Then re-run tests and watch the logs.
