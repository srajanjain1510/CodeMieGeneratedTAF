
import logging
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
def pytest_configure(config):
    # Configure logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

@pytest.fixture(scope='session', autouse=True)
def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger

@pytest.fixture(scope='session')
def config():
    with open('config/config.yaml', 'r') as config_file:
        return yaml.safe_load(config_file)

@pytest.fixture(scope='session')
def api_client(config):
    return APIClient(base_url=config['base_url'], headers=config['headers'])
