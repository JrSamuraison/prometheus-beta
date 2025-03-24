import pytest
import requests
from unittest.mock import patch
from src.get_public_ip import get_public_ip, _validate_ip_address

class MockResponse:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code
    
    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError("Mock HTTP Error")

def test_get_public_ip_successful():
    """Test successful retrieval of public IP"""
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse('8.8.8.8')
        assert get_public_ip() == '8.8.8.8'

def test_get_public_ip_connection_error():
    """Test connection error handling"""
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.ConnectionError("Connection failed")
        with pytest.raises(ConnectionError):
            get_public_ip()

def test_get_public_ip_http_error():
    """Test HTTP error handling"""
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse('Error', 404)
        with pytest.raises(ConnectionError):
            get_public_ip()

def test_get_public_ip_invalid_format():
    """Test invalid IP address format"""
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse('invalid.ip')
        with pytest.raises(ValueError):
            get_public_ip()

def test_validate_ip_address():
    """Test IP address validation"""
    assert _validate_ip_address('8.8.8.8') == True
    assert _validate_ip_address('255.255.255.255') == True
    assert _validate_ip_address('0.0.0.0') == True
    
    # Invalid cases
    assert _validate_ip_address('256.0.0.0') == False
    assert _validate_ip_address('8.8.8') == False
    assert _validate_ip_address('8.8.8.8.8') == False
    assert _validate_ip_address('abc.def.ghi.jkl') == False
    assert _validate_ip_address('') == False