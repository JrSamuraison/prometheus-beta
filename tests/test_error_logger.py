import io
import sys
import pytest
from src.error_logger import log_error

def test_basic_error_logging(capsys):
    """Test basic error logging functionality."""
    log_error("Test error message")
    captured = capsys.readouterr()
    assert "ERROR: Test error message" in captured.err

def test_error_logging_with_type(capsys):
    """Test error logging with an error type."""
    log_error("Network error", "network")
    captured = capsys.readouterr()
    assert "NETWORK ERROR: Network error" in captured.err

def test_invalid_message_type():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(123)
    
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(None)

def test_empty_string_logging(capsys):
    """Test logging an empty string."""
    log_error("")
    captured = capsys.readouterr()
    assert "ERROR: " in captured.err