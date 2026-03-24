#!/usr/bin/env python3
"""
Process ~/Documents/linux_journey/ markdown files for Jekyll.

Steps:
1. Filter out copied content (URLs/HTML at top)
2. Categorise root-level files by keyword matching
3. Apply British English corrections to prose (skip code blocks)
4. Add Jekyll front matter
5. Sanitise filenames
6. Copy to _linux_journey/ collection
"""

import os
import re
import shutil
import sys
from pathlib import Path

SOURCE_DIR = Path.home() / "Documents" / "linux_journey"
TARGET_DIR = Path(__file__).resolve().parent.parent / "_linux_journey"

# ── Subdirectory mappings ──────────────────────────────────────────────
SUBDIR_MAP = {
    "certified_kubernetes_administrator_(cka)_with_prac": "courses/cka-certification",
    "python_essential_training": "courses/python-essential-training",
    "learning_go": "courses/learning-go",
    "learning_kubernetes": "courses/learning-kubernetes",
    "learning_regular_expressions": "courses/learning-regular-expressions",
    "rhcsa_ex200_cert_prep__1_deploy,_configure_and_man": "courses/rhcsa-cert-prep-1",
    "rhcsa_(ex200)_cert_prep__2_file_access,_storage,_a": "courses/rhcsa-cert-prep-2",
    "lpic-2_linux_engineer_(201-450)_cert_prep__2_linux": "courses/lpic-2",
    "advanced_linux__the_linux_kernel": "courses/advanced-linux-kernel",
    "project_tv": "courses/project-tv",
    "project_tv_v2_-_ubuntu_edition": "courses/project-tv-v2",
    "rocky_linux_kubernetes_setup": "courses/rocky-linux-kubernetes-setup",
    "mongodb_essentials_training": "courses/mongodb-essentials",
    "ansible_playbooks": "courses/ansible-playbooks",
    "machines": "courses/machines",
}

# ── Category keyword rules (order matters - first match wins) ─────────
CATEGORY_RULES = [
    ("rocky-linux", re.compile(
        r"rocky|centos|rhel[^a-z]|dnf[^a-z]|rpm[^a-z]|yum[^a-z]|el[0-9]|"
        r"epel|alma|oracle.linux|red.hat|subscription.manager|sosreport|"
        r"kdump.*rocky|rocky.*kdump|warewulf|apptainer|fuzzball|munge|"
        r"openondemand|open.ondemand|openhpc|slurm", re.IGNORECASE)),
    ("kubernetes-and-containers", re.compile(
        r"kubernetes|k8s|kubectl|helm[^a-z]|pod[^a-z]|deployment.*kube|"
        r"service.mesh|ingress|etcd|docker|container[^a-z]|podman|buildah|"
        r"skopeo|compose[^a-z]|cri-o|containerd|enroot|singularity|"
        r"kubeadm|kubelet|kube.proxy|calico|flannel|cilium", re.IGNORECASE)),
    ("virtualisation", re.compile(
        r"libvirt|kvm[^a-z]|qemu|virt-|virsh|vmware|virtualbox|vagrant|"
        r"vfio|virtio|ovmf|spice|virt.manager|cloud.init|"
        r"virtual.machine", re.IGNORECASE)),
    ("kernel-and-system-internals", re.compile(
        r"kernel[^a-z]|/proc|sysfs|hugepage|numa[^a-z]|irq[^a-z]|"
        r"cpu.pin|perf[^a-z]|sar[^a-z]|strace|gdb[^a-z]|crash[^a-z]|"
        r"kdump|dmesg|sysctl|tuned|cgroup|"
        r"ftrace|bpf[^a-z]|ebpf|vmcore|kexec|grub|dracut|initramfs|"
        r"boot.*loader|efi[^a-z]|uefi", re.IGNORECASE)),
    ("networking", re.compile(
        r"network[^a-z]|firewall|nfs[^a-z]|ssh[^a-z]|dns[^a-z]|dhcp|"
        r"vlan|bridge[^a-z]|bond[^a-z]|tcp[^a-z]|udp[^a-z]|socket|"
        r"curl[^a-z]|wget|ip.route|nmcli|tailscale|wireguard|openvpn|"
        r"iptables|nftables|opnsense|haproxy|nginx|squid|"
        r"multicast|ethernet|mtu[^a-z]|100g|10g[^a-z]|rdma|"
        r"infiniband|netplan|resolved|networkmanager", re.IGNORECASE)),
    ("storage-and-filesystems", re.compile(
        r"zfs|btrfs|xfs[^a-z]|ext4|lvm[^a-z]|raid[^a-z]|disk[^a-z]|"
        r"mount[^a-z]|fstab|multipath|iscsi|ceph|gluster|nbd[^a-z]|"
        r"loop[^a-z]|swap[^a-z]|rsync|backup|borg[^a-z]|restic|"
        r"snapshot|timeshift|snapper|storage[^a-z]|sanoid|syncoid|"
        r"partition|fdisk|parted|blkid|smart[^a-z]|nvme[^a-z]", re.IGNORECASE)),
    ("security", re.compile(
        r"selinux|luks|crypt[^a-z]|encrypt|audit[^a-z]|pam[^a-z]|"
        r"ldap|freeipa|samba|kerberos|polkit|sudo[^a-z]|ssl[^a-z]|"
        r"tls[^a-z]|cert.*auth|gpg[^a-z]|ssh.key|firewalld|"
        r"apparmor|fips|cve[^a-z]|vulnerability|passwd|"
        r"privilege|permission|access.control", re.IGNORECASE)),
    ("editors-and-tools", re.compile(
        r"emacs|vim[^a-z]|neovim|tmux|screen[^a-z]|git(?!hub)[^a-z]|"
        r"awk[^a-z]|sed[^a-z]|regex|grep[^a-z]|find[^a-z]|"
        r"make[^a-z]|gcc[^a-z]|cmake|ripgrep|fzf|jq[^a-z]|"
        r"yq[^a-z]|bat[^a-z]|exa[^a-z]|fd[^a-z]", re.IGNORECASE)),
    ("desktop-and-distributions", re.compile(
        r"arch.linux|debian|ubuntu|fedora|suse|nix[^a-z]|gentoo|"
        r"flatpak|snap[^a-z]|appimage|nvidia|amd.gpu|gpu[^a-z]|"
        r"wayland|xorg|kde|gnome|desktop|bluetooth|wifi|"
        r"pipewire|pulse.audio|display.manager|sddm|gdm", re.IGNORECASE)),
    ("automation-and-configuration", re.compile(
        r"ansible|cron[^a-z]|systemd|puppet|terraform|packer|"
        r"cloud.formation|ci.cd|pipeline|jenkins|github.action|"
        r"makefile|kickstart", re.IGNORECASE)),
    ("general-linux", re.compile(r".*")),  # catch-all
]

# ── British English substitutions ─────────────────────────────────────
# Only applied to prose text (not code blocks, inline code, URLs)
BRITISH_SUBS = [
    # -ize -> -ise (but not "size", "prize", "seize")
    (re.compile(r'\b(\w+?)ize\b(?<!size)(?<!prize)(?<!seize)'), r'\1ise'),
    (re.compile(r'\b(\w+?)izing\b'), r'\1ising'),
    (re.compile(r'\b(\w+?)ization\b'), r'\1isation'),
    (re.compile(r'\b(\w+?)ized\b'), r'\1ised'),
    # -or -> -our (common words only to avoid false positives)
    (re.compile(r'\bcolor\b', re.IGNORECASE), 'colour'),
    (re.compile(r'\bcolors\b', re.IGNORECASE), 'colours'),
    (re.compile(r'\bfavor\b', re.IGNORECASE), 'favour'),
    (re.compile(r'\bfavors\b', re.IGNORECASE), 'favours'),
    (re.compile(r'\bfavorite\b', re.IGNORECASE), 'favourite'),
    (re.compile(r'\bfavorites\b', re.IGNORECASE), 'favourites'),
    (re.compile(r'\bbehavior\b', re.IGNORECASE), 'behaviour'),
    (re.compile(r'\bbehaviors\b', re.IGNORECASE), 'behaviours'),
    (re.compile(r'\bneighbor\b', re.IGNORECASE), 'neighbour'),
    (re.compile(r'\bneighbors\b', re.IGNORECASE), 'neighbours'),
    (re.compile(r'\bhonor\b', re.IGNORECASE), 'honour'),
    (re.compile(r'\bhonors\b', re.IGNORECASE), 'honours'),
    (re.compile(r'\bhumor\b', re.IGNORECASE), 'humour'),
    (re.compile(r'\blabor\b', re.IGNORECASE), 'labour'),
    (re.compile(r'\bharbor\b', re.IGNORECASE), 'harbour'),
    (re.compile(r'\barmor\b', re.IGNORECASE), 'armour'),
    # -er -> -re (careful list - exclude agent nouns)
    (re.compile(r'\bcenter\b', re.IGNORECASE), 'centre'),
    (re.compile(r'\bcenters\b', re.IGNORECASE), 'centres'),
    (re.compile(r'\bfiber\b', re.IGNORECASE), 'fibre'),
    (re.compile(r'\bfibers\b', re.IGNORECASE), 'fibres'),
    (re.compile(r'\bmeter\b(?![ -])', re.IGNORECASE), 'metre'),
    (re.compile(r'\bmeters\b', re.IGNORECASE), 'metres'),
    (re.compile(r'\btheater\b', re.IGNORECASE), 'theatre'),
    (re.compile(r'\btheaters\b', re.IGNORECASE), 'theatres'),
    # -ense -> -ence
    (re.compile(r'\bdefense\b', re.IGNORECASE), 'defence'),
    (re.compile(r'\boffense\b', re.IGNORECASE), 'offence'),
    (re.compile(r'\blicense\b', re.IGNORECASE), 'licence'),
    (re.compile(r'\blicenses\b', re.IGNORECASE), 'licences'),
    # -og -> -ogue
    (re.compile(r'\banalog\b', re.IGNORECASE), 'analogue'),
    (re.compile(r'\bcatalog\b', re.IGNORECASE), 'catalogue'),
    (re.compile(r'\bcatalogs\b', re.IGNORECASE), 'catalogues'),
    (re.compile(r'\bdialog\b(?!ue)', re.IGNORECASE), 'dialogue'),
    # -l -> -ll before suffix
    (re.compile(r'\bmodeling\b', re.IGNORECASE), 'modelling'),
    (re.compile(r'\blabeling\b', re.IGNORECASE), 'labelling'),
    (re.compile(r'\bcanceling\b', re.IGNORECASE), 'cancelling'),
    (re.compile(r'\btraveling\b', re.IGNORECASE), 'travelling'),
    (re.compile(r'\bleveling\b', re.IGNORECASE), 'levelling'),
    # Specific words
    (re.compile(r'\bgray\b', re.IGNORECASE), 'grey'),
    (re.compile(r'\bvirtualization\b', re.IGNORECASE), 'virtualisation'),
    (re.compile(r'\bcontainerization\b', re.IGNORECASE), 'containerisation'),
    (re.compile(r'\bcustomize\b', re.IGNORECASE), 'customise'),
    (re.compile(r'\bcustomization\b', re.IGNORECASE), 'customisation'),
    (re.compile(r'\boptimize\b', re.IGNORECASE), 'optimise'),
    (re.compile(r'\boptimization\b', re.IGNORECASE), 'optimisation'),
    (re.compile(r'\brecognize\b', re.IGNORECASE), 'recognise'),
    (re.compile(r'\bauthorize\b', re.IGNORECASE), 'authorise'),
    (re.compile(r'\bauthorization\b', re.IGNORECASE), 'authorisation'),
    (re.compile(r'\binitialize\b', re.IGNORECASE), 'initialise'),
    (re.compile(r'\binitialization\b', re.IGNORECASE), 'initialisation'),
    (re.compile(r'\bsynchronize\b', re.IGNORECASE), 'synchronise'),
    (re.compile(r'\bsynchronization\b', re.IGNORECASE), 'synchronisation'),
    (re.compile(r'\butilize\b', re.IGNORECASE), 'utilise'),
    (re.compile(r'\butilization\b', re.IGNORECASE), 'utilisation'),
    (re.compile(r'\bnormalize\b', re.IGNORECASE), 'normalise'),
    (re.compile(r'\bnormalization\b', re.IGNORECASE), 'normalisation'),
]

# Words that should NEVER be substituted (package names, commands, etc.)
EXCLUDE_WORDS = {
    "systemize", "capitalize", "initialize",  # when part of code/API names
}


def is_copied_content(filepath: Path) -> bool:
    """Check if a file is copied content (URL or HTML at the top)."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            first_line = f.readline().strip()
    except Exception:
        return True

    if not first_line:
        # Empty first line - read second line
        try:
            with open(filepath, "r", encoding="utf-8", errors="replace") as f:
                f.readline()
                second_line = f.readline().strip()
                if second_line.startswith(("http://", "https://")):
                    return True
        except Exception:
            pass
        return False

    # URL at top
    if first_line.startswith(("http://", "https://")):
        return True

    # HTML content at top
    html_indicators = ("<a ", "<a>", "<img", "<script", "<noscript",
                       "Skip to", "Featured link", "<!DOCTYPE", "<html",
                       "<div", "<span", "<p>", "<meta")
    if any(first_line.startswith(ind) for ind in html_indicators):
        return True

    return False


def categorise_file(filename: str, content: str) -> str:
    """Assign a category based on filename and first heading."""
    # Combine filename and first heading for matching
    text = filename.lower()
    # Extract first heading if present
    for line in content.split("\n")[:10]:
        stripped = line.strip()
        if stripped.startswith("#"):
            text += " " + stripped.lstrip("#").strip().lower()
            break

    for category, pattern in CATEGORY_RULES:
        if pattern.search(text):
            return category

    return "general-linux"


def split_prose_and_code(content: str):
    """Split content into segments of (text, is_code) tuples."""
    segments = []
    lines = content.split("\n")
    in_code_block = False
    current_segment = []
    current_is_code = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            if in_code_block:
                # End of code block
                current_segment.append(line)
                segments.append(("\n".join(current_segment), True))
                current_segment = []
                in_code_block = False
                current_is_code = False
            else:
                # Start of code block
                if current_segment:
                    segments.append(("\n".join(current_segment), False))
                current_segment = [line]
                in_code_block = True
                current_is_code = True
        else:
            if not current_segment and not in_code_block:
                current_is_code = False
            current_segment.append(line)

    if current_segment:
        segments.append(("\n".join(current_segment), in_code_block))

    return segments


def apply_british_english(text: str) -> str:
    """Apply British English substitutions to prose text only."""
    segments = split_prose_and_code(text)
    result_parts = []

    for segment_text, is_code in segments:
        if is_code:
            result_parts.append(segment_text)
        else:
            # Within prose, also skip inline code
            parts = re.split(r'(`[^`]+`)', segment_text)
            processed = []
            for part in parts:
                if part.startswith("`") and part.endswith("`"):
                    processed.append(part)
                elif part.startswith(("http://", "https://")):
                    processed.append(part)
                else:
                    for pattern, replacement in BRITISH_SUBS:
                        part = pattern.sub(replacement, part)
                    processed.append(part)
            result_parts.append("".join(processed))

    return "\n".join(result_parts) if len(result_parts) == 1 else "\n".join(
        # Rejoin without extra newlines from the split
        result_parts
    )


def sanitise_filename(name: str) -> str:
    """Convert filename to clean URL-safe slug."""
    # Remove .md extension
    name = name.rsplit(".", 1)[0] if name.endswith(".md") else name
    # Lowercase
    name = name.lower()
    # Replace special chars with hyphens
    name = re.sub(r"[^a-z0-9]+", "-", name)
    # Remove leading/trailing hyphens and collapse multiples
    name = re.sub(r"-+", "-", name).strip("-")
    # Truncate to 80 chars
    if len(name) > 80:
        name = name[:80].rsplit("-", 1)[0]
    return name + ".md"


def sanitise_yaml_string(s: str) -> str:
    """Make a string safe for use in YAML double-quoted values."""
    # Remove HTML tags
    s = re.sub(r'<[^>]+>', '', s)
    # Remove backslash escapes that aren't valid YAML
    s = s.replace('\\', '')
    # Remove characters that break YAML
    s = s.replace('"', "'")
    # Collapse whitespace
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def extract_title(content: str, filename: str) -> str:
    """Extract title from first heading or generate from filename."""
    for line in content.split("\n")[:10]:
        stripped = line.strip()
        if stripped.startswith("#"):
            title = stripped.lstrip("#").strip()
            if title:
                return sanitise_yaml_string(title)

    # Generate from filename
    name = filename.rsplit(".", 1)[0]
    name = re.sub(r"[_\-]+", " ", name)
    return sanitise_yaml_string(name.title())


def generate_tags(filename: str, category: str) -> list:
    """Generate tags from filename keywords."""
    name = filename.rsplit(".", 1)[0].lower()
    # Strip all non-alphanumeric chars before splitting
    name = re.sub(r"[^a-z0-9\s_\-]", "", name)
    words = re.split(r"[_\-\s]+", name)
    # Filter out very short, common words, or purely numeric
    stopwords = {"the", "a", "an", "in", "on", "of", "to", "for", "and",
                 "or", "is", "it", "by", "at", "as", "how", "what", "why",
                 "with", "from", "this", "that", "not", "but", "can", "do",
                 "does", "did", "will", "would", "should", "could", "may",
                 "might", "must", "shall", "has", "have", "had", "was",
                 "were", "been", "being", "get", "got", "set", "use",
                 "using", "used", "etc", "via", "per"}
    tags = [w for w in words
            if len(w) > 2 and w not in stopwords and not w.isdigit()]
    # Add category as a tag
    if category != "general-linux":
        tags.insert(0, category)
    # Limit to 5 tags
    return tags[:5]


def process_file(src_path: Path, target_subdir: str, category: str,
                 seen_filenames: dict) -> dict:
    """Process a single markdown file and return info dict."""
    try:
        content = src_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return {"error": str(e), "source": str(src_path)}

    # Extract title before modifying content
    title = extract_title(content, src_path.name)

    # Apply British English corrections
    content = apply_british_english(content)

    # Strip any existing front matter
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = parts[2].lstrip("\n")

    # Generate tags
    tags = generate_tags(src_path.name, category)
    tags_str = ", ".join(f'"{t}"' for t in tags)

    # Title is already sanitised by extract_title
    safe_title = title.replace('"', "'")

    # Build front matter
    front_matter = f'''---
title: "{safe_title}"
category: "{category}"
tags: [{tags_str}]
---

'''

    final_content = front_matter + content

    # Sanitise filename
    clean_name = sanitise_filename(src_path.name)

    # Handle collisions
    key = f"{target_subdir}/{clean_name}"
    if key in seen_filenames:
        base = clean_name.rsplit(".", 1)[0]
        counter = 2
        while f"{target_subdir}/{base}-{counter}.md" in seen_filenames:
            counter += 1
        clean_name = f"{base}-{counter}.md"
        key = f"{target_subdir}/{clean_name}"

    seen_filenames[key] = str(src_path)

    # Write to target
    target_path = TARGET_DIR / target_subdir / clean_name
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(final_content, encoding="utf-8")

    return {
        "source": str(src_path),
        "target": str(target_path),
        "category": category,
        "title": title,
    }


def create_category_index(category: str, display_name: str, description: str,
                          target_subdir: str):
    """Create an index.md for a category."""
    index_path = TARGET_DIR / target_subdir / "index.md"
    index_path.parent.mkdir(parents=True, exist_ok=True)

    content = f'''---
title: "{display_name}"
layout: archive
permalink: /linux-journey/{target_subdir}/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

{description}

{{% assign pages = site.linux_journey | where_exp: "item", "item.path contains '{target_subdir}/'" | sort: "title" %}}
{{% for page in pages %}}
{{% unless page.url contains 'index' %}}
- [{{{{ page.title }}}}]({{{{ page.url | relative_url }}}})
{{% endunless %}}
{{% endfor %}}
'''
    index_path.write_text(content, encoding="utf-8")


def main():
    print(f"Source: {SOURCE_DIR}")
    print(f"Target: {TARGET_DIR}")
    print()

    # Clean target directory
    if TARGET_DIR.exists():
        shutil.rmtree(TARGET_DIR)
    TARGET_DIR.mkdir(parents=True)

    seen_filenames = {}
    stats = {
        "total_scanned": 0,
        "excluded_copied": 0,
        "excluded_non_md": 0,
        "processed": 0,
        "errors": 0,
        "categories": {},
    }

    # ── Process subdirectories ────────────────────────────────────────
    print("Processing subdirectories...")
    for subdir_name, target_subdir in SUBDIR_MAP.items():
        subdir_path = SOURCE_DIR / subdir_name
        if not subdir_path.is_dir():
            print(f"  SKIP (not found): {subdir_name}")
            continue

        md_files = list(subdir_path.glob("**/*.md"))
        processed_count = 0

        for md_file in md_files:
            stats["total_scanned"] += 1

            if is_copied_content(md_file):
                stats["excluded_copied"] += 1
                continue

            # Subdirectory files use the mapped category
            category = target_subdir.split("/")[-1] if "/" in target_subdir else target_subdir
            result = process_file(md_file, target_subdir, category, seen_filenames)

            if "error" in result:
                stats["errors"] += 1
                print(f"  ERROR: {result['error']} ({result['source']})")
            else:
                stats["processed"] += 1
                processed_count += 1
                stats["categories"][target_subdir] = stats["categories"].get(
                    target_subdir, 0) + 1

        print(f"  {subdir_name}: {processed_count}/{len(md_files)} files")

    # ── Process root-level files ──────────────────────────────────────
    print("\nProcessing root-level files...")
    root_files = sorted(SOURCE_DIR.glob("*.md"))
    print(f"  Found {len(root_files)} root markdown files")

    for md_file in root_files:
        stats["total_scanned"] += 1

        if is_copied_content(md_file):
            stats["excluded_copied"] += 1
            continue

        try:
            content = md_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            stats["errors"] += 1
            continue

        category = categorise_file(md_file.name, content)
        result = process_file(md_file, category, category, seen_filenames)

        if "error" in result:
            stats["errors"] += 1
        else:
            stats["processed"] += 1
            stats["categories"][category] = stats["categories"].get(
                category, 0) + 1

    # ── Create category index pages ───────────────────────────────────
    print("\nCreating category index pages...")

    category_info = {
        "rocky-linux": ("Rocky Linux", "Notes on Rocky Linux, CentOS, RHEL, DNF, RPM, and related distributions."),
        "kubernetes-and-containers": ("Kubernetes & Containers", "Notes on Kubernetes, Docker, Podman, Helm, and container orchestration."),
        "virtualisation": ("Virtualisation", "Notes on KVM, QEMU, libvirt, VMware, and virtual machine management."),
        "kernel-and-system-internals": ("Kernel & System Internals", "Notes on the Linux kernel, crash analysis, kdump, performance tuning, and sysctl."),
        "networking": ("Networking", "Notes on firewalls, NFS, SSH, DNS, VLANs, TCP/IP, and network configuration."),
        "storage-and-filesystems": ("Storage & Filesystems", "Notes on ZFS, Btrfs, XFS, LVM, RAID, iSCSI, backups, and storage management."),
        "security": ("Security", "Notes on SELinux, LUKS, PAM, LDAP, SSL/TLS, and security hardening."),
        "editors-and-tools": ("Editors & Tools", "Notes on Emacs, Vim, tmux, Git, awk, sed, and command-line utilities."),
        "desktop-and-distributions": ("Desktop & Distributions", "Notes on Arch, Debian, Ubuntu, Fedora, Flatpak, NVIDIA, and desktop environments."),
        "automation-and-configuration": ("Automation & Configuration", "Notes on Ansible, cron, systemd, Terraform, and configuration management."),
        "general-linux": ("General Linux", "Miscellaneous Linux notes, tips, tricks, and reference material."),
    }

    course_info = {
        "courses/cka-certification": ("CKA Certification", "Certified Kubernetes Administrator exam preparation notes."),
        "courses/rhcsa-cert-prep-1": ("RHCSA Cert Prep 1", "RHCSA EX200 -- deployment, configuration, and management."),
        "courses/rhcsa-cert-prep-2": ("RHCSA Cert Prep 2", "RHCSA EX200 -- file access, storage, and security."),
        "courses/lpic-2": ("LPIC-2 Certification", "LPIC-2 Linux Engineer (201-450) certification prep."),
        "courses/advanced-linux-kernel": ("Advanced Linux Kernel", "Deep dive into the Linux kernel."),
        "courses/learning-kubernetes": ("Learning Kubernetes", "Kubernetes fundamentals and hands-on exercises."),
        "courses/learning-go": ("Learning Go", "Go programming language notes."),
        "courses/learning-regular-expressions": ("Learning Regular Expressions", "Regex patterns and usage."),
        "courses/python-essential-training": ("Python Essential Training", "Python programming fundamentals."),
        "courses/rocky-linux-kubernetes-setup": ("Rocky Linux K8s Setup", "Building a Kubernetes cluster on Rocky Linux."),
        "courses/project-tv": ("Project TV", "Media server infrastructure project."),
        "courses/project-tv-v2": ("Project TV v2 (Ubuntu)", "Media server v2 on Ubuntu."),
        "courses/mongodb-essentials": ("MongoDB Essentials", "MongoDB training notes."),
        "courses/ansible-playbooks": ("Ansible Playbooks", "Ansible automation examples."),
        "courses/machines": ("Machines", "Machine configuration reference."),
    }

    all_info = {**category_info, **course_info}
    for subdir, (display_name, description) in all_info.items():
        if stats["categories"].get(subdir, 0) > 0:
            create_category_index(subdir, display_name, description, subdir)
            print(f"  Created index: {subdir}")

    # ── Summary ───────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("PROCESSING COMPLETE")
    print("=" * 60)
    print(f"  Total scanned:    {stats['total_scanned']}")
    print(f"  Excluded (copied): {stats['excluded_copied']}")
    print(f"  Processed:        {stats['processed']}")
    print(f"  Errors:           {stats['errors']}")
    print()
    print("Category breakdown:")
    for cat, count in sorted(stats["categories"].items(),
                             key=lambda x: -x[1]):
        print(f"  {cat}: {count}")
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
