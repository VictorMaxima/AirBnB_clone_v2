#!/usr/bin/env bash
# to setup an nginx server 

apt-get update
apt-get install -y nginx

mkdir -p /data/webstatic
mkdir -p /data/webstatic/releases/test
mkdir -p /data/webstatic/shared
echo "VictorMaxima is here" > /data/webstatic/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data
chgrp -R ubuntu /data

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://victormaxima.pythonanywhere.com/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
