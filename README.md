One-Click Docker Server Setup with AI Recommendations

A lightweight script to set up a dedicated Ubuntu 22.04 server for hosting multiple Docker Compose applications with automatic SSL and AI-powered configuration recommendations.

Requirements:
- Ubuntu 22.04 LTS
- Root access
- Domain names pointed to your server (for SSL)
- OpenAI API key (optional - for AI recommendations)

Quick Start:
1. Clone this repository
2. Run: sudo ./install.sh
3. Export your OpenAI key (optional):
   export OPENAI_API_KEY="your-key-here"

Adding New Applications:
1. Create a new directory for your app:
   mkdir -p /opt/docker-apps/your-app-name

2. Get AI recommendations for your app (optional):
   python3 src/ai_recommendations.py

3. Copy your docker-compose.yml to the new directory:
   cp your-docker-compose.yml /opt/docker-apps/your-app-name/

4. Add your app to the nginx-proxy network by adding this to your docker-compose.yml:
   networks:
     - nginx-proxy-network

   networks:
     nginx-proxy-network:
       external: true

5. Start your application:
   cd /opt/docker-apps/your-app-name
   docker compose up -d

SSL Certificates:
- Certificates are stored in /opt/ssl-certs
- To add a new certificate:
  certbot certonly --nginx -d your-domain.com

Directory Structure:
/opt/docker-apps/           - All Docker applications
/opt/docker-apps/nginx-proxy - Nginx reverse proxy
/opt/ssl-certs/             - SSL certificates

Troubleshooting:
- Check nginx logs: docker logs nginx-proxy
- Verify network: docker network ls
- Check SSL certs: ls /opt/ssl-certs

Security Notes:
- All traffic is automatically redirected to HTTPS
- SSL configuration uses modern security standards
- Container isolation through dedicated networks
- Regular updates recommended

For issues or contributions:
[Your GitHub repository URL] # easysetup4u
