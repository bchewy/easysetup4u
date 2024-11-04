import click
import os
import yaml
import shutil
from pathlib import Path
from typing import List, Dict
from ai_recommendations import AIRecommender
import docker
from dotenv import load_dotenv

load_dotenv()

class DockerManager:
    def __init__(self):
        self.client = docker.from_env()
        self.ai = AIRecommender()
        self.base_path = Path('/opt/docker-apps')
        self.base_path.mkdir(parents=True, exist_ok=True)
    
    def deploy_app(self, app_name: str, compose_path: Path) -> None:
        """Deploy a new Docker Compose application"""
        app_dir = self.base_path / app_name
        app_dir.mkdir(exist_ok=True)
        
        # Copy compose file
        shutil.copy2(compose_path, app_dir / 'docker-compose.yml')
        
        # Load and analyze compose file
        with open(compose_path) as f:
            compose_content = yaml.safe_load(f)
        
        # Get AI recommendations
        recommendations = self.ai.analyze_compose_file(compose_content)
        click.echo("\nAI Recommendations:")
        for rec in recommendations:
            click.echo(f"- {rec}")
        
        # Add to proxy network
        if 'networks' not in compose_content:
            compose_content['networks'] = {}
        compose_content['networks']['proxy-network'] = {'external': True}
        
        # Save modified compose
        with open(app_dir / 'docker-compose.yml', 'w') as f:
            yaml.dump(compose_content, f)
        
        # Deploy
        os.chdir(app_dir)
        os.system(f"docker-compose up -d")

@click.group()
def cli():
    """Docker Apps Manager CLI"""
    pass

@cli.command()
@click.argument('app_name')
@click.argument('compose_path', type=click.Path(exists=True))
def deploy(app_name: str, compose_path: str):
    """Deploy a new Docker Compose application"""
    manager = DockerManager()
    manager.deploy_app(app_name, Path(compose_path))

@cli.command()
@click.argument('app_name')
def stop(app_name: str):
    """Stop a running application"""
    app_dir = Path('/opt/docker-apps') / app_name
    if app_dir.exists():
        os.chdir(app_dir)
        os.system("docker-compose down")

@cli.command()
def list():
    """List all deployed applications"""
    apps_dir = Path('/opt/docker-apps')
    for app_dir in apps_dir.iterdir():
        if app_dir.is_dir():
            click.echo(f"- {app_dir.name}")

if __name__ == '__main__':
    cli() 