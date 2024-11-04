# Docker Apps Manager

CLI tool to automatically deploy and manage multiple Docker Compose applications on a single Ubuntu 22.04 server with AI-powered recommendations.

## Quick Start

1. Clone this repository
2. Add your OpenAI API key to .env file:
   ```
   OPENAI_API_KEY=your_key_here
   ```
3. Run the installer:
   ```
   ./install.sh
   ```

## Usage

Deploy a new app:
```
docker-apps deploy myapp /path/to/docker-compose.yml
```

List running apps:
```
docker-apps list
```

Stop an app:
```
docker-apps stop myapp
```

## Features

- Automatic Docker and SSL setup
- AI recommendations for container optimization
- Nginx reverse proxy configuration
- Multiple apps isolation
- Automatic network configuration
- SSL certificate management

## Requirements

- Ubuntu 22.04
- Python 3.8+
- OpenAI API key (or use Hugging Face offline mode)

## Directory Structure

- /opt/docker-apps/{app_name} - Where apps are deployed
- config/ - Nginx and Docker templates
- src/ - Core Python modules

## License

MIT 