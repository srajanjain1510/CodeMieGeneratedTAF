import pytest
import yaml
from utils.api_client import APIClient

@pytest.fixture(scope='session')
def config():
    with open('config/config.yaml', 'r') as config_file:
        return yaml.safe_load(config_file)

@pytest.fixture(scope='session')
def api_client(config):
    return APIClient(base_url=config['base_url'], headers=config['headers'])