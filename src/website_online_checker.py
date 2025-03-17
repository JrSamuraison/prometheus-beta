import requests

def is_website_online(url: str, timeout: int = 5) -> bool:
    """
    Check if a website is online by attempting to connect to the URL.

    Args:
        url (str): The full URL of the website to check (including http:// or https://)
        timeout (int, optional): Connection timeout in seconds. Defaults to 5.

    Returns:
        bool: True if the website is online and responds, False otherwise.

    Raises:
        ValueError: If the URL is empty or None
        TypeError: If the URL is not a string
    """
    # Validate input
    if url is None:
        raise ValueError("URL cannot be None")
    
    if not isinstance(url, str):
        raise TypeError("URL must be a string")
    
    # Remove whitespace and validate URL is not empty
    url = url.strip()
    if not url:
        raise ValueError("URL cannot be empty")

    try:
        # Attempt to connect to the website
        response = requests.get(url, timeout=timeout)
        
        # Check if the response was successful (status code 200-299)
        return 200 <= response.status_code < 300
    
    except (requests.ConnectionError, requests.Timeout, requests.RequestException):
        # Any connection-related errors mean the website is not accessible
        return False