import pytest
import requests
from src.website_online_checker import is_website_online

class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code

def test_valid_online_website(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(200)
    
    monkeypatch.setattr(requests, 'get', mock_get)
    assert is_website_online('https://www.example.com') == True

def test_website_with_non_200_status(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(404)
    
    monkeypatch.setattr(requests, 'get', mock_get)
    assert is_website_online('https://www.example.com') == False

def test_website_connection_error(monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.ConnectionError()
    
    monkeypatch.setattr(requests, 'get', mock_get)
    assert is_website_online('https://www.nonexistentwebsite123456.com') == False

def test_website_timeout_error(monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.Timeout()
    
    monkeypatch.setattr(requests, 'get', mock_get)
    assert is_website_online('https://www.example.com', timeout=1) == False

def test_empty_url_raises_error():
    with pytest.raises(ValueError, match="URL cannot be empty"):
        is_website_online('')

def test_none_url_raises_error():
    with pytest.raises(ValueError, match="URL cannot be None"):
        is_website_online(None)

def test_non_string_url_raises_error():
    with pytest.raises(TypeError, match="URL must be a string"):
        is_website_online(123)

def test_whitespace_url_raises_error():
    with pytest.raises(ValueError, match="URL cannot be empty"):
        is_website_online('   ')

def test_custom_timeout():
    def mock_get(*args, **kwargs):
        assert kwargs['timeout'] == 10
        return MockResponse(200)
    
    monkeypatch.setattr(requests, 'get', mock_get)
    assert is_website_online('https://www.example.com', timeout=10) == True