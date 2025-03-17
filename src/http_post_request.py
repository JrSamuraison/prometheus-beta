import requests
from typing import Dict, Any, Optional

def send_post_request(url: str, 
                      data: Optional[Dict[str, Any]] = None, 
                      headers: Optional[Dict[str, str]] = None, 
                      timeout: int = 10) -> Dict[str, Any]:
    """
    Send an HTTP POST request to the specified URL.

    Args:
        url (str): The target URL for the POST request.
        data (dict, optional): Payload to send in the request body. Defaults to None.
        headers (dict, optional): Additional headers to include in the request. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        dict: Response from the server, including status code and body.

    Raises:
        ValueError: If URL is empty or invalid.
        requests.exceptions.RequestException: For network-related errors.
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("A valid URL must be provided")

    # Default empty dictionary for data and headers if not provided
    data = data or {}
    headers = headers or {}

    # Send POST request
    response = requests.post(
        url, 
        json=data, 
        headers=headers, 
        timeout=timeout
    )

    # Raise an exception for HTTP errors
    response.raise_for_status()

    # Return response details
    return {
        'status_code': response.status_code,
        'body': response.json() if response.content else None,
        'headers': dict(response.headers)
    }