import requests

def get_public_ip() -> str:
    """
    Retrieve the public IP address of the system.

    Returns:
        str: The public IP address as a string.

    Raises:
        ConnectionError: If unable to connect to IP lookup service.
        ValueError: If the IP address cannot be parsed or retrieved.
    """
    try:
        # Use a reliable public IP lookup service
        response = requests.get('https://api.ipify.org', timeout=10)
        
        # Raise an exception for bad responses
        response.raise_for_status()
        
        # Validate the IP address format
        ip_address = response.text.strip()
        
        # Basic IP address validation 
        if not _validate_ip_address(ip_address):
            raise ValueError("Invalid IP address format")
        
        return ip_address
    
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to retrieve public IP: {str(e)}") from e

def _validate_ip_address(ip: str) -> bool:
    """
    Validate the format of an IP address.

    Args:
        ip (str): IP address to validate.

    Returns:
        bool: True if IP address is valid, False otherwise.
    """
    # Simple IP validation: split into 4 octets, check each is between 0-255
    try:
        octets = ip.split('.')
        if len(octets) != 4:
            return False
        
        return all(
            octet.isdigit() and 
            0 <= int(octet) <= 255 
            for octet in octets
        )
    except Exception:
        return False