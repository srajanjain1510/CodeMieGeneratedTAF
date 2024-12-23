import pytest
from data_flusher import DataFlusher

@pytest.fixture(scope='session', autouse=True)
def flush_data():
    base_url = 'http://localhost:5000'  # Replace with your actual base URL
    flusher = DataFlusher(base_url)
    yield
    flusher.flush_all_data()