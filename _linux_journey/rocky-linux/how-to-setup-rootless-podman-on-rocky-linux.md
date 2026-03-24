---
title: "How to Setup Rootless Podman on Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "setup", "rootless", "podman", "rocky"]
---

# How to Setup Rootless Podman on Rocky Linux

Here is a complete, copy-paste–friendly summary of **how to configure rootless Podman on Rocky Linux 8.10** to restrict container traffic to **only the `192.168.1.0/24` subnet** and **block internet access for all users**, including all steps, commands, and explanation.

---

# ✅ Enforce Subnet-Restricted Networking in Rootless Podman (Rocky Linux 8.10)

### 🎯 Objective

* Run rootless Podman containers
* Allow containers to communicate only with `192.168.1.0/24`
* Block all other internet access (e.g., 8.8.8.8)
* Enforce this for all users
* Make the configuration default and persistent

---

## STEP 1: Install Required Packages

```bash
sudo dnf install -y podman netavark aardvark-dns podman-plugins nftables
```

---

## STEP 2: Configure Podman to Use Netavark

Edit `/etc/containers/containers.conf`:

```bash
sudo tee /etc/containers/containers.conf > /dev/null <<'EOF'
[network]
network_backend = "netavark"
default_network = "restricted"
EOF
```

---

## STEP 3: Create a Restricted Podman Network

Delete old broken network (if needed):

```bash
sudo sed -i 's/^default_network = .*/# &/' /etc/containers/containers.conf
sudo podman network rm restricted || true
```

Then create the new restricted network:

```bash
sudo podman network create \
  --driver bridge \
  --subnet 10.89.0.0/24 \
  --opt mtu=1500 \
  --opt no_default_route=1 \
  --route 192.168.1.0/24,10.89.0.1 \
  restricted
```

Restore the `default_network` setting:

```bash
sudo sed -i 's|# default_network =.*|default_network = "restricted"|' /etc/containers/containers.conf
```

---

## STEP 4: Make Network Available to All Users

### For Existing Users:

```bash
for user in $(awk -F: '$3 >= 1000 && $1 != "nobody" { print $1 }' /etc/passwd); do
    homedir=$(eval echo "~$user")
    mkdir -p "$homedir/.config/containers/networks"
    cp /etc/containers/networks/restricted.json "$homedir/.config/containers/networks/restricted.json"
    chown -R "$user:$user" "$homedir/.config"
done
```

### For New Users (via skel):

```bash
sudo mkdir -p /etc/skel/.config/containers/networks
sudo cp /etc/containers/networks/restricted.json /etc/skel/.config/containers/networks/restricted.json
```

---

## STEP 5: Block Internet Access Using nftables (Final Fix)

### 1. Identify Outbound Interface

```bash
ip route get 8.8.8.8
```

Example output:

```
8.8.8.8 via 192.168.1.1 dev eno1 src 192.168.1.123
```

Use the interface name shown (e.g., `eno1`) in the next step.

---

### 2. Configure nftables to Block NAT Egress

Replace `eno1` with your interface name and create the rule:

```bash
sudo tee /etc/nftables.conf > /dev/null <<'EOF'
#!/usr/sbin/nft -f

table ip nat {
  chain postrouting {
    type nat hook postrouting priority 100; policy accept;
    ip saddr 10.89.0.0/24 ip daddr != 192.168.1.0/24 oifname "eno1" drop
  }
}
EOF
```

---

### 3. Enable and Apply nftables

```bash
sudo systemctl enable --now nftables
sudo nft flush ruleset
sudo nft -f /etc/nftables.conf
```

---

## STEP 6: Test

```bash
podman run -it --rm rockylinux:8 bash
```

Inside the container:

```bash
ping 192.168.1.1   # ✅ should succeed
ping 8.8.8.8       # ❌ should fail (no route)
ip route           # should show only a route to 192.168.1.0/24
```

---

## ✅ Summary of What’s Now Enforced

* Podman uses `netavark` for networking
* All containers use the `restricted` network by default
* Users cannot override this without root
* Internet access is blocked by firewall for container IPs (10.89.0.0/24)
* Only access to `192.168.1.0/24` is allowed

---

Let me know if you’d like to:

* Block DNS lookups too
* Enforce outbound port filtering (e.g., allow only TCP 443)
* Use `firewalld` instead of `nftables`

This setup is hardened and scales across HPC or shared systems.
