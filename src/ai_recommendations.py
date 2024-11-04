from transformers import pipeline
import openai
import os
import yaml
from typing import Dict, List

class AIRecommender:
    def __init__(self, use_openai: bool = True):
        self.use_openai = use_openai
        if use_openai:
            self.openai_client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        else:
            self.classifier = pipeline("zero-shot-classification")
    
    def analyze_compose_file(self, compose_content: Dict) -> List[str]:
        if self.use_openai:
            return self._analyze_with_openai(compose_content)
        return self._analyze_with_huggingface(compose_content)
    
    def _analyze_with_openai(self, compose_content: Dict) -> List[str]:
        prompt = f"""Analyze this Docker Compose file and suggest optimizations:
        {yaml.dump(compose_content)}
        Focus on:
        1. Resource allocation
        2. Security best practices
        3. Network configuration
        4. Volume management
        """
        
        response = self.openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content.split('\n')
    
    def _analyze_with_huggingface(self, compose_content: Dict) -> List[str]:
        # Simplified analysis using zero-shot classification
        services = compose_content.get('services', {})
        recommendations = []
        
        for service_name, service in services.items():
            if not service.get('deploy'):
                recommendations.append(f"Add resource limits for {service_name}")
            if not service.get('healthcheck'):
                recommendations.append(f"Add healthcheck for {service_name}")
            
        return recommendations 