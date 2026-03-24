---
title: "Nextcloud Docker Container Using Tailscale"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "nextcloud", "docker", "container", "tailscale"]
---

* Create the `/home/howard/docker_compose_files/nextcloud` directory:
```
mkdir -p /home/howard/docker_compose_files/nextcloud
```
* Setup this `compose.yml` file:
```
cat << "EOF" | tee /home/howard/docker_compose_files/nextcloud/docker-compose.yaml
services:
  nextcloud-aio-mastercontainer:
    image: nextcloud/all-in-one:latest
    init: true
    restart: always
    container_name: nextcloud-aio-mastercontainer # This line cannot be changed.
    volumes:
      - nextcloud_aio_mastercontainer:/mnt/docker-aio-config
      - /var/run/docker.sock:/var/run/docker.sock:ro
    networks:
      - nextcloud-aio
    ports:
      - 0.0.0.0:8080:8080
    environment:
      APACHE_PORT: 11000
      APACHE_IP_BINDING: 127.0.0.1
      SKIP_DOMAIN_VALIDATION: true
  nextcloud-aio-caddy:
    build:
      context: .
      dockerfile: Caddy.Dockerfile
    restart: unless-stopped
    environment:
      NC_DOMAIN: tail5fa2b.ts.net
    volumes:
      - type: bind
        source: ./Caddyfile
        target: /etc/caddy/Caddyfile
      - type: volume
        source: caddy_certs
        target: /certs
      - type: volume
        source: caddy_data
        target: /data
      - type: volume
        source: caddy_config
        target: /config
      - type: volume
        source: tailscale_sock
        target: /var/run/tailscale/ # Mount the volume for /var/run/tailscale/tailscale.sock
        read_only: true
    network_mode: service:nextcloud-aio-tailscale
  nextcloud-aio-tailscale:
    image: tailscale/tailscale:v1.80.0
    environment:
      TS_HOSTNAME: tail5fa2b.ts.net
      TS_AUTH_KEY: tskey-client-kXGGbs6CNTRL # OAuth client key recommended
      TS_EXTRA_ARGS: --advertise-tags=tag:nextcloud # Tags are required when using OAuth client
    init: true
    restart: unless-stopped
    devices:
      - /dev/net/tun:/dev/net/tun
    volumes:
      - type: volume
        source: tailscale
        target: /var/lib/tailscale
      - type: volume
        source: tailscale_sock
        target: /tmp # Mounting the entire /tmp folder to access tailscale.sock
    cap_add:
      - NET_ADMIN
    networks:
      - nextcloud-aio
volumes:
  nextcloud_aio_mastercontainer:
    name: nextcloud_aio_mastercontainer # This line cannot be changed.
  caddy_certs:
    name: caddy_certs
  caddy_data:
    name: caddy_data
  caddy_config:
    name: caddy_config
  tailscale:
    name: tailscale
  tailscale_sock:
    name: tailscale_sock
networks:
  nextcloud-aio:
    name: nextcloud-aio
    driver: bridge
    enable_ipv6: false
    driver_opts:
      com.docker.network.driver.mtu: "9001" # Jumbo Frame
      com.docker.network.bridge.host_binding_ipv4: "127.0.0.1" # Harden aio
EOF
```
* My configuration:
```
cat << "EOF" | tee /home/howard/docker_compose_files/nextcloud/docker-compose.yaml
services:
  nextcloud-aio-mastercontainer:
    image: nextcloud/all-in-one:latest
    init: true
    restart: always
    container_name: nextcloud-aio-mastercontainer # This line cannot be changed.
    volumes:
      - nextcloud_aio_mastercontainer:/mnt/docker-aio-config
      - /var/run/docker.sock:/var/run/docker.sock:ro
    networks:
      - nextcloud-aio
    ports:
      - 0.0.0.0:8080:8080
    environment:
      APACHE_PORT: 11000
      APACHE_IP_BINDING: 127.0.0.1
      SKIP_DOMAIN_VALIDATION: true
  nextcloud-aio-caddy:
    build:
      context: .
      dockerfile: Caddy.Dockerfile
    restart: unless-stopped
    environment:
      NC_DOMAIN: tail5fa2b.ts.net
    volumes:
      - type: bind
        source: ./Caddyfile
        target: /etc/caddy/Caddyfile
      - type: volume
        source: caddy_certs
        target: /certs
      - type: volume
        source: caddy_data
        target: /data
      - type: volume
        source: caddy_config
        target: /config
      - type: volume
        source: tailscale_sock
        target: /var/run/tailscale/ # Mount the volume for /var/run/tailscale/tailscale.sock
        read_only: true
    network_mode: service:nextcloud-aio-tailscale
  nextcloud-aio-tailscale:
    image: tailscale/tailscale:v1.80.0
    environment:
      TS_HOSTNAME: tail5fa2b.ts.net
      TS_AUTH_KEY: tskey-auth-kXRsfaVipw11CNTRL-tPriFcECRsaRmKPkTyuBsagKGHadnCsK # OAuth client key recommended
      # TS_EXTRA_ARGS: --advertise-tags=tag:nextcloud # Tags are required when using OAuth client
    init: true
    restart: unless-stopped
    devices:
      - /dev/net/tun:/dev/net/tun
    volumes:
      - type: volume
        source: tailscale
        target: /var/lib/tailscale
      - type: volume
        source: tailscale_sock
        target: /tmp # Mounting the entire /tmp folder to access tailscale.sock
    cap_add:
      - NET_ADMIN
    networks:
      - nextcloud-aio
volumes:
  nextcloud_aio_mastercontainer:
    name: nextcloud_aio_mastercontainer # This line cannot be changed.
  caddy_certs:
    name: caddy_certs
  caddy_data:
    name: caddy_data
  caddy_config:
    name: caddy_config
  tailscale:
    name: tailscale
  tailscale_sock:
    name: tailscale_sock
networks:
  nextcloud-aio:
    name: nextcloud-aio
    driver: bridge
    enable_ipv6: false
    driver_opts:
      com.docker.network.driver.mtu: "9001" # Jumbo Frame
      com.docker.network.bridge.host_binding_ipv4: "127.0.0.1" # Harden aio
EOF
```
* Change into the `nextcloud` directory:
```
cd ~/docker_compose_files/nextcloud/
```
* Create the `Caddyfile`:
```
cat << "EOF" | tee /home/howard/docker_compose_files/nextcloud/Caddyfile
{
    layer4 {
        127.0.0.1:3478 {
            route {
                proxy {
                    upstream nextcloud-aio-talk:3478
                }
            }
        }
        127.0.0.1:3479 {
            route {
                proxy {
                    upstream nextcloud-aio-talk:3479
                }
            }
        }
    }
}
https://{$NC_DOMAIN} {
    reverse_proxy nextcloud-aio-apache:11000
}
http://{$NC_DOMAIN} {
    reverse_proxy nextcloud-aio-apache:11000
}
EOF
```
* Create the `Caddy.Dockerfile`:
```
cat << "EOF" | tee /home/howard/docker_compose_files/nextcloud/Caddy.Dockerfile
FROM caddy:2.9.1-builder-alpine AS builder
RUN xcaddy build --with github.com/mholt/caddy-l4@87e3e5e2c7f986b34c0df373a5799670d7b8ca03

FROM caddy:2.9.1-alpine
COPY --from=builder /usr/bin/caddy /usr/bin/caddyF
EOF
```
* Run:
```
docker compose up --build --wait
```
* Then follow the logs:
```
docker compose logs --follow
```
* Login:
```
https://ip.address.of.server:8080/
```