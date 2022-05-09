import pytest
from App import app

@pytest.fixture
def client():
    yield app.test_client()
