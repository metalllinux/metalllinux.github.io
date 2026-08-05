---
title: "How to set up dawarich on Rocky Linux 10"
category: "rocky-linux"
tags: ["rocky-linux", "docker", "dawarich", "self-hosted", "tailscale", "gps-tracking"]
---

# How to set up dawarich on Rocky Linux 10

I have been looking for a self-hosted GPS tracking solution for a while. I wanted to record my journeys across Japan and potentially the world. That was until a while back, when I was listening to [Episode 47 of the Self Hosted show](https://selfhosted.show/147) and was introduced to [Dawarich](https://github.com/Freika/dawarich).

I deployed it on a Rocky Linux 10 box with 30 GB of RAM, 16 CPUs, and roughly 56 GB of free disk space. This is of course overkill for this app! Access is via Tailscale, so the setup is reachable from anywhere on the mesh network without opening any ports to the internet.

## Architecture

```
┌─────────────┐     Tailscale Mesh      ┌──────────────────────────────────────┐
│  Android    │◄───────────────────────►│  Rocky Linux 10                      │
│  Dawarich   │  http://<TAILSCALE_IP>  │                                      │
│  App        │         :3000           │  ┌────────────────────────────────┐  │
│             │                         │  │ Docker Containers               │  │
└─────────────┘                         │  │                                │  │
                                        │  │ dawarich_app (port 3000)      │  │
┌─────────────┐                         │  │ dawarich_db   (PostgreSQL)     │  │
│  Laptop     │◄───────────────────────►│  │ dawarich_redis (Redis)        │  │
│  (Browser)  │                         │  │ dawarich_sidekiq (Sidekiq)    │  │
└─────────────┘                         │  └────────────────────────────────┘  │
                                        └──────────────────────────────────────┘
```

All four containers run behind Tailscale, so nothing is exposed to the public internet.

## Phase 1: Docker Installation

Dawarich runs entirely in Docker containers, so the first real dependency is Docker Engine.

```bash
# Install dnf-utils for config-manager
sudo dnf install -y dnf-utils

# Add Docker CE repository for EL
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# Install Docker Engine, CLI, containerd, and plugins
sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Enable and start Docker service
sudo systemctl enable --now docker

# Add <user> to docker group (allows docker commands without sudo after re-login)
sudo usermod -aG docker <user>
```

Log out and back in for the group change to take effect.

## Phase 2: Tailscale Installation

Tailscale provides the encrypted mesh network so the Dawarich server is reachable from your laptop and phone without any port forwarding.

```bash
# Install Tailscale via official install script
curl -fsSL https://tailscale.com/install.sh | sh

# Enable and start Tailscale daemon
sudo systemctl enable --now tailscaled

# Authenticate with Tailscale (visit the printed URL in your browser)
sudo tailscale up
```

Take note of the Tailscale IP assigned to the machine — you will need it for the Dawarich configuration. You can find it with `tailscale ip`.

## Phase 3: Dawarich Configuration

Create a deployment directory and two files inside it.

```bash
mkdir -p ~/linux/projects/dawarich_deployment
cd ~/linux/projects/dawarich_deployment
```

### `.env`

```env
POSTGRES_PASSWORD=<random-64-char-hex>
SECRET_KEY_BASE=<random-128-char-hex>
DATABASE_PASSWORD=<same-as-POSTGRES-PASSWORD>
APPLICATION_HOSTS=localhost,127.0.0.1,<TAILSCALE_IP>
TIME_ZONE=Asia/Tokyo
RAILS_ENV=production
SELF_HOSTED=true
STORE_GEODATA=true
DAWARICH_APP_PORT=3000
```

Generate the random values with something like `openssl rand -hex 32` (for 64 hex chars) and `openssl rand -hex 64` (for 128 hex chars).

**Important:** Do not change `SECRET_KEY_BASE` after the first startup, as it will invalidate all existing sessions and API keys.

### `docker-compose.yml`

Base this on the official `docker/docker-compose.yml` from [dawarich](https://github.com/Freika/dawarich). It defines four services:

| Container | Image | Purpose |
|-----------|-------|---------|
| `dawarich_redis` | `redis:7.4-alpine` | Session cache and job queue |
| `dawarich_db` | `postgis/postgis:17-3.5-alpine` | PostgreSQL with PostGIS spatial extensions |
| `dawarich_app` | `freikin/dawarich:latest` | Rails web application (port 3000) |
| `dawarich_sidekiq` | `freikin/dawarich:latest` | Background job worker |

The compose file also creates five named volumes for persistent data:

- `dawarich_db_data` — PostgreSQL data
- `dawarich_shared` — shared temporary data
- `dawarich_public` — uploaded files
- `dawarich_watched` — import watch directory
- `dawarich_storage` — application storage

## Phase 4: Launch

```bash
cd ~/linux/projects/dawarich_deployment
sudo docker compose up -d
```

All four containers should reach a healthy status within about two minutes. You can verify with:

```bash
sudo docker compose ps
```

## Access

### Web Interface

- **URL**: `http://<TAILSCALE_IP>:3000` (via Tailscale)
- **Default username**: `demo@dawarich.app`
- **Default password**: `safepassword`

> **Security notice:** These are the generic default credentials provided by Dawarich. Change the password immediately after your first login via Account Settings, or create a new user and delete the demo account.

### Android Setup

1. Install **Dawarich** from Google Play.
2. Open the app and go to Settings.
3. Set **Server URL** to `http://<TAILSCALE_IP>:3000`.
4. Get an API key from the Dawarich web UI: Account Settings → API keys → Create key. Else you can scan the handy QR code that the app gives you.
5. Paste the API key into the app.
6. Tap "Test connection" — it should succeed.
7. Open the Map page, tap "Start tracking", then "Stop tracking" followed by "Upload points" when you are done.

Both your laptop and Android phone must be connected to the same Tailscale network for this to work.

## Maintenance

### Update Dawarich

```bash
cd ~/linux/projects/dawarich_deployment
sudo docker compose down
sudo docker compose pull
sudo docker compose up -d
```

Always backup before updating to a new version.

### Backup Data

```bash
# Backup all Docker volumes
sudo docker run --rm \
  -v dawarich_deployment_dawarich_db_data:/backup/db_data \
  -v dawarich_deployment_dawarich_public:/backup/public \
  -v dawarich_deployment_dawarich_storage:/backup/storage \
  -v ~/linux/projects/dawarich_deployment/backups:/out \
  alpine tar czf /out/dawarich-backup-$(date +%Y%m%d).tar.gz -C /backup .
```

### View Logs

```bash
cd ~/linux/projects/dawarich_deployment
sudo docker compose logs -f dawarich_app     # web app logs
sudo docker compose logs -f dawarich_sidekiq  # worker logs
sudo docker compose logs -f dawarich_db       # database logs
```

### Check Status

```bash
cd ~/linux/projects/dawarich_deployment
sudo docker compose ps
```

## Important Notes

- **Do not change `SECRET_KEY_BASE`** after the first startup — it will invalidate all existing sessions and API keys.
- **Do not delete original imported data** until you have verified Dawarich has ingested it correctly.
- Always **backup before updating** to a new version.
- Tailscale must be running on both the server and client devices for connectivity.

## Conclusion

Dawarich is a solid, privacy-focused GPS tracking solution that runs comfortably in Docker with minimal resource overhead. Paired with Tailscale for mesh networking, it gives you full control over your location data without exposing anything to the public internet. Give it a try if you are looking to take back control of your privacy and record your awesome memories of wherever you will travel to!
