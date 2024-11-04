#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}Starting server setup...${NC}"

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "Please run as root (use sudo)"
    exit 1
fi

# Create necessary directories
mkdir -p /opt/docker-apps
mkdir -p /opt/docker-apps/nginx-proxy
mkdir -p /opt/ssl-certs

# Copy configuration files
cp config/nginx.conf /opt/docker-apps/nginx-proxy/
cp config/docker-compose-template.yml /opt/docker-apps/

# Run setup scripts
bash src/docker_setup.sh
bash src/ssl_setup.sh

echo -e "${GREEN}Setup completed! Your server is ready to host Docker applications${NC}"
echo -e "Use the AI recommendations tool by running: python3 src/ai_recommendations.py" 