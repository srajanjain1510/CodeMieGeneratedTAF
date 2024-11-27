import pytest
import yaml
from utils.api_client import APIClient

@pytest.fixture(scope='session')
def config():
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

@pytest.fixture(scope='session')
def api_client(config):
    return APIClient(config['base_url'])