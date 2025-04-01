import pytest
import requests
from unittest.mock import patch
from src.web_scraper import scrape_webpage

# Sample HTML for mocking
MOCK_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Test Page</title>
</head>
<body>
    <div class="content">Sample content</div>
    <div class="another-content">Another content</div>
    <a href="https://example.com">Link 1</a>
    <a href="https://another-example.com">Link 2</a>
</body>
</html>
"""

class MockResponse:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code
    
    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError("HTTP Error")

def test_scrape_webpage_full_page():
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse(MOCK_HTML)
        
        result = scrape_webpage('https://example.com')
        
        assert result['title'] == 'Test Page'
        assert 'Sample content' in result['text']
        assert len(result['links']) == 2
        assert 'https://example.com' in result['links']

def test_scrape_webpage_with_selector():
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse(MOCK_HTML)
        
        result = scrape_webpage('https://example.com', '.content')
        
        assert result['text'] == ['Sample content']

def test_scrape_webpage_invalid_url():
    with pytest.raises(ValueError, match="A valid URL must be provided"):
        scrape_webpage('')

def test_scrape_webpage_network_error():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.RequestException("Network Error")
        
        with pytest.raises(ValueError, match="Error fetching webpage"):
            scrape_webpage('https://example.com')

def test_scrape_webpage_http_error():
    with patch('requests.get') as mock_get:
        mock_response = MockResponse("Error Page", status_code=404)
        mock_get.return_value = mock_response
        
        with pytest.raises(ValueError, match="HTTP Error"):
            scrape_webpage('https://example.com')