import logging
import pytest
import yaml

from utils.api_client import APIClient


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

@pytest.fixture(scope='module')
def base_url():
    return 'http://localhost:8000'  # Example base URL, replace with actual base URL

@pytest.fixture(scope='session')
def api_client(config, base_url):
    return APIClient(base_url=base_url, headers=config['headers'])