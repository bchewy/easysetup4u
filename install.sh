#!/bin/bash
set -e

# Create virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

# Setup Docker and SSL
chmod +x src/docker_setup.sh
chmod +x src/ssl_setup.sh
./src/docker_setup.sh
./src/ssl_setup.sh 