import os
from typing import Dict
import json
import requests

class DockerAIRecommender:
    def __init__(self):
        self.openai_key = os.getenv('OPENAI_API_KEY')
        self.default_model = "gpt-3.5-turbo"

    def get_recommendations(self, app_type: str, resources: Dict) -> Dict:
        """
        Get AI recommendations for Docker configuration based on app type and resources
        """
        prompt = f"""
        Given an application of type {app_type} with the following resources:
        RAM: {resources.get('ram_gb', 'unknown')}GB
        CPU Cores: {resources.get('cpu_cores', 'unknown')}
        Storage: {resources.get('storage_gb', 'unknown')}GB

        Provide Docker container recommendations including:
        1. Resource limits
        2. Volume configurations
        3. Network settings
        4. Security best practices
        """

        if self.openai_key:
            return self._get_openai_recommendations(prompt)
        return self._get_default_recommendations(app_type)

    def _get_openai_recommendations(self, prompt: str) -> Dict:
        headers = {
            "Authorization": f"Bearer {self.openai_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.default_model,
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            return json.loads(response.json()['choices'][0]['message']['content'])
        return self._get_default_recommendations(prompt)

    def _get_default_recommendations(self, app_type: str) -> Dict:
        # Default recommendations if OpenAI is not available
        return {
            "resource_limits": {
                "memory": "2g",
                "cpu_count": "2",
                "swap": "1g"
            },
            "volume_config": [
                "/data:/app/data",
                "/logs:/app/logs"
            ],
            "network_settings": {
                "use_nginx_proxy": True,
                "expose_ports": ["80", "443"]
            },
            "security_practices": [
                "Enable no-new-privileges",
                "Use non-root user",
                "Implement resource limits",
                "Regular security updates"
            ]
        }

if __name__ == "__main__":
    recommender = DockerAIRecommender()
    
    print("Docker Configuration AI Recommender")
    app_type = input("Enter your application type (e.g., web, database, cache): ")
    
    resources = {
        "ram_gb": input("Available RAM (GB): "),
        "cpu_cores": input("Available CPU cores: "),
        "storage_gb": input("Available Storage (GB): ")
    }

    recommendations = recommender.get_recommendations(app_type, resources)
    print("\nRecommended Docker Configuration:")
    print(json.dumps(recommendations, indent=2)) 