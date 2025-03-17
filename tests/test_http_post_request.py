import pytest
import requests
from unittest.mock import patch
from src.http_post_request import send_post_request

class MockResponse:
    def __init__(self, json_data, status_code, headers=None):
        self.json_data = json_data
        self.status_code = status_code
        self.headers = headers or {}
        self.content = json_data is not None

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if 400 <= self.status_code < 600:
            raise requests.exceptions.HTTPError(f"HTTP error: {self.status_code}")

def test_successful_post_request():
    with patch('requests.post') as mock_post:
        mock_response = MockResponse(
            json_data={'message': 'success'}, 
            status_code=200,
            headers={'Content-Type': 'application/json'}
        )
        mock_post.return_value = mock_response

        result = send_post_request(
            'https://example.com/api', 
            data={'key': 'value'}, 
            headers={'Authorization': 'Bearer token'}
        )

        assert result['status_code'] == 200
        assert result['body'] == {'message': 'success'}
        mock_post.assert_called_once_with(
            'https://example.com/api', 
            json={'key': 'value'}, 
            headers={'Authorization': 'Bearer token'}, 
            timeout=10
        )

def test_empty_url_raises_error():
    with pytest.raises(ValueError, match="A valid URL must be provided"):
        send_post_request('')

def test_request_exception_handling():
    with patch('requests.post') as mock_post:
        mock_post.side_effect = requests.exceptions.ConnectionError("Network error")
        
        with pytest.raises(RuntimeError, match="POST request failed: Network error"):
            send_post_request('https://example.com/api')

def test_http_error_handling():
    with patch('requests.post') as mock_post:
        mock_response = MockResponse(
            json_data={'error': 'Bad Request'}, 
            status_code=400
        )
        mock_post.return_value = mock_response
        
        with pytest.raises(requests.exceptions.HTTPError):
            send_post_request('https://example.com/api')

def test_no_response_body():
    with patch('requests.post') as mock_post:
        mock_response = MockResponse(
            json_data=None, 
            status_code=204,
            headers={'Content-Type': 'application/json'}
        )
        mock_post.return_value = mock_response

        result = send_post_request('https://example.com/api')
        assert result['body'] is None
        assert result['status_code'] == 204

def test_default_parameters():
    with patch('requests.post') as mock_post:
        mock_response = MockResponse(
            json_data={'message': 'default'}, 
            status_code=200
        )
        mock_post.return_value = mock_response

        result = send_post_request('https://example.com/api')
        assert result['status_code'] == 200
        mock_post.assert_called_once_with(
            'https://example.com/api', 
            json={}, 
            headers={}, 
            timeout=10
        )