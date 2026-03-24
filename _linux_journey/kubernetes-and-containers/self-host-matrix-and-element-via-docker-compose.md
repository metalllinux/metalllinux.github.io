---
title: "Self Host Matrix And Element Via Docker Compose"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "self", "host", "matrix", "element"]
---

* Following this guide and you see errors related to the `matrix_postgres_1` container and that it is looking for `C` in `Collate` and `Ctype` as opposed to UTF8. Firstly stop the container. You can access the `postgres DB` via  --> `docker exec -it matrix_postgres_1 bash` --> `su root` -->  `su - postgres (if that does not work, then the postgres user)P --> `psql -U synapse`
* Once that is done, go into the `postgres` DB as the `synapse` user with `\c postgres` and then drop the `synapse` DB with `DROP DATABASE synapse;`. When that is done, recreate the Database with `CREATE DATABASE synapse WITH LC_CTYPE = 'C' LC_COLLATE='C' TEMPLATE='template0';`

Server Setup
Update your OS and make sure everything is ready

sudo apt update && sudo apt upgrade
UFW Firewall
Lets make sure ports 80 and 443 are open on UFW

sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
Install Docker & Docker-Compose
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
apt-get install python3 python3-pip -y
pip3 install docker-compose
Prepare our compose file
Create a matrix folder, in this folder create a docker-compose.yml file with the following contents:

version: '2.3'
services:
  postgres:
    image: postgres:14
    restart: unless-stopped
    volumes:
     - ./postgresdata:/var/lib/postgresql/data

    # These will be used in homeserver.yaml later on
    environment:
     - POSTGRES_DB=synapse
     - POSTGRES_USER=synapse
     - POSTGRES_PASSWORD=STRONGPASSWORD
     
  element:
    image: vectorim/element-web:latest
    restart: unless-stopped
    volumes:
      - ./element-config.json:/app/config.json
        
  synapse:
    image: matrixdotorg/synapse:latest
    restart: unless-stopped
    volumes:
     - ./synapse:/data
Don’t forget to change the Postgres password on this file to a secure password.

Now on the same folder create a config file for the elements clients, named element-config.json.

Copy the example file from Elements.io into your own config file, and adjust the following settings:

Add our own homeserver at the top of the file:

"default_server_config": {
        "m.homeserver": {
            "base_url": "https://matrix.example.com",
            "server_name": "matrix.example.com"
        },
        "m.identity_server": {
            "base_url": "https://vector.im"
        }
    },
Generate Synapse config
Now its time to generate the initial config of our synapse server, run the following command to do so:

sudo docker run -it --rm \
    -v "$HOME/matrix/synapse:/data" \
    -e SYNAPSE_SERVER_NAME=matrix.example.com \
    -e SYNAPSE_REPORT_STATS=yes \
    matrixdotorg/synapse:latest generate
Configuring Synapse
Now lets adjust the freshly generated synapse config to our needs

Edit the synapse/homeserver.yaml file as follows:

Comment-out the SQLite database:

#database:
#  name: sqlite3
#  args:
#    database: /data/homeserver.db
And now add our Postgres database:

database:
  name: psycopg2
  args:
    user: synapse
    password: STRONGPASSWORD
    database: synapse
    host: postgres
    cp_min: 5
    cp_max: 10
Spin it up!
Time to get things moving, spin-up your docker stack:

sudo docker-compose up -d
Create our first (admin) user
sudo docker exec -it matrix_synapse_1 bash
register_new_matrix_user -c /data/homeserver.yaml http://localhost:8008
Follow the on-screen instructions to create your first user

Install Caddy Reverse Proxy
Caddy will be used for the reverse proxy. This will handle incomming HTTPS connections and forward them to the correct docker containers. It a simple setup process and Caddy will automatically fetch and renew Let’s Encrypt certificates for us!

First head over to our user directory

cd ~
Install Caddy:

sudo apt install caddy -y
Create a Caddy file:

sudo nano Caddyfile
Paste the following config:

matrix.example.com {
  reverse_proxy /_matrix/* 10.10.10.4:8008
  reverse_proxy /_synapse/client/* 10.10.10.4:8008
  
  header {
    X-Content-Type-Options nosniff
    Referrer-Policy  strict-origin-when-cross-origin
    Strict-Transport-Security "max-age=63072000; includeSubDomains;"
    Permissions-Policy "accelerometer=(), camera=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), payment=(), usb=(), interest-cohort=()"
    X-Frame-Options SAMEORIGIN
    X-XSS-Protection 1
    X-Robots-Tag none
    -server
  }
}

element.example.com {
  encode zstd gzip
  reverse_proxy 10.10.10.3:80

  header {
    X-Content-Type-Options nosniff
    Referrer-Policy  strict-origin-when-cross-origin
    Strict-Transport-Security "max-age=63072000; includeSubDomains;"
    Permissions-Policy "accelerometer=(), camera=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), payment=(), usb=(), interest-cohort=()"
    X-Frame-Options SAMEORIGIN
    X-XSS-Protection 1
    X-Robots-Tag none
    -server
  }
}
Don’t forget to adjust the IPs and the domain names!

Reload Caddy

caddy reload