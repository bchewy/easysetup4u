from setuptools import setup, find_packages

setup(
    name="docker-apps-manager",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'docker',
        'python-dotenv',
        'pyyaml',
        'openai',
        'transformers',
        'torch',
    ],
    entry_points={
        'console_scripts': [
            'docker-apps=src.cli:cli',
        ],
    },
) 