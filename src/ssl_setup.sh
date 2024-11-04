#!/bin/bash
set -e

# Install certbot
sudo apt-get update
sudo apt-get install -y certbot python3-certbot-nginx

# Setup SSL renewal cron job
(crontab -l 2>/dev/null; echo "0 12 * * * /usr/bin/certbot renew --quiet") | crontab - 