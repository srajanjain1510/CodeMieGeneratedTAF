import pytest
import logging

@pytest.fixture(scope='session', autouse=True)
def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info('Logging setup complete')
