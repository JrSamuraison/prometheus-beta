import pytest
import logging
import io
from src.memory_logger import log_memory_usage

def test_log_memory_usage():
    """
    Test that log_memory_usage function works correctly
    """
    # Capture log output
    log_capture = io.StringIO()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(log_capture)
    logger.addHandler(handler)
    
    # Call the function
    result = log_memory_usage(logger)
    
    # Check return value
    assert isinstance(result, dict), "Should return a dictionary"
    
    # Check that some memory metrics are present
    assert 'rss' in result, "RSS memory metric should be present"
    assert result['rss'] > 0, "RSS memory should be a positive number"
    
    # Check logging output
    log_output = log_capture.getvalue()
    assert "Memory Usage Statistics:" in log_output
    assert "RSS:" in log_output
    
    # Clean up
    logger.removeHandler(handler)
    log_capture.close()

def test_log_memory_usage_with_default_logger():
    """
    Test that function works with default logger
    """
    result = log_memory_usage()
    
    assert isinstance(result, dict), "Should return a dictionary with default logger"
    assert 'rss' in result, "RSS memory metric should be present with default logger"

def test_log_memory_usage_error_handling(monkeypatch):
    """
    Test error handling in log_memory_usage
    """
    # Capture log output
    log_capture = io.StringIO()
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)
    handler = logging.StreamHandler(log_capture)
    logger.addHandler(handler)
    
    # Simulate an error by monkeypatching psutil.Process
    def mock_process_raise(*args, **kwargs):
        raise Exception("Simulated error")
    
    monkeypatch.setattr('psutil.Process', mock_process_raise)
    
    # Call the function and check for empty dict return
    result = log_memory_usage(logger)
    
    # Verify
    assert result == {}, "Should return an empty dict on error"
    
    # Check error logging
    log_output = log_capture.getvalue()
    assert "Error collecting memory usage" in log_output
    
    # Clean up
    logger.removeHandler(handler)
    log_capture.close()