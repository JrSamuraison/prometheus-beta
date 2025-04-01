import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Union

def scrape_webpage(url: str, selector: str = None) -> Dict[str, Union[str, List[str]]]:
    """
    Scrape data from a given web page.

    Args:
        url (str): The URL of the webpage to scrape.
        selector (str, optional): CSS selector to extract specific elements. 
                                  If None, returns page text and title.

    Returns:
        Dict containing scraped data with keys:
        - 'title': Page title 
        - 'text': Full page text or selected element text
        - 'links': List of links found on the page

    Raises:
        ValueError: If URL is invalid or empty
        requests.RequestException: For network-related errors
    """
    # Validate input
    if not url or not isinstance(url, str):
        raise ValueError("A valid URL must be provided")

    try:
        # Send GET request with a user agent to appear more like a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        # Raise an exception for bad status codes
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Prepare result dictionary
        result = {
            'title': soup.title.string if soup.title else '',
            'text': '',
            'links': []
        }

        # If selector is provided, extract specific elements
        if selector:
            selected_elements = soup.select(selector)
            result['text'] = [elem.get_text(strip=True) for elem in selected_elements]
        else:
            # If no selector, extract all text
            result['text'] = soup.get_text(strip=True)

        # Extract all links
        result['links'] = [a.get('href') for a in soup.find_all('a', href=True)]

        return result

    except requests.RequestException as e:
        raise ValueError(f"Error fetching webpage: {str(e)}")
    except Exception as e:
        raise ValueError(f"Unexpected error during scraping: {str(e)}")