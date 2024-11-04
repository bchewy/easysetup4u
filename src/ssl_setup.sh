#!/bin/bash

# Install certbot
apt-get install -y certbot python3-certbot-nginx

# Create directory for SSL certificates
mkdir -p /opt/ssl-certs
chmod 755 /opt/ssl-certs 