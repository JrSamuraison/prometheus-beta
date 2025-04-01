import logging
import pytest
from src.multi_value_logger import log_multiple_values

class TestMultiValueLogger:
    def test_default_logging(self, caplog):
        """Test logging with default parameters"""
        caplog.set_level(logging.INFO)
        log_multiple_values(1, "hello", [1, 2, 3])
        assert "1 hello [1, 2, 3]" in caplog.text
        assert caplog.records[0].levelno == logging.INFO

    def test_different_log_levels(self, caplog):
        """Test logging with different log levels"""
        log_levels = ['debug', 'info', 'warning', 'error', 'critical']
        
        for level in log_levels:
            caplog.clear()
            caplog.set_level(getattr(logging, level.upper()))
            
            # Use a mix of data types
            log_multiple_values("Test", 42, None, level=level)
            
            assert f"Test 42 None" in caplog.text
            assert caplog.records[0].levelno == getattr(logging, level.upper())

    def test_custom_logger(self, caplog):
        """Test logging with a custom logger"""
        custom_logger = logging.getLogger('custom_logger')
        caplog.set_level(logging.INFO, logger=custom_logger)
        
        log_multiple_values("Custom", "Logger", logger=custom_logger)
        assert "Custom Logger" in caplog.text

    def test_invalid_log_level(self):
        """Test that an invalid log level raises a ValueError"""
        with pytest.raises(ValueError, match="Invalid logging level"):
            log_multiple_values("Invalid", "Level", level="nonexistent")

    def test_empty_values(self, caplog):
        """Test logging with no values"""
        caplog.set_level(logging.INFO)
        log_multiple_values()
        assert len(caplog.records) == 0

    def test_complex_data_types(self, caplog):
        """Test logging with complex data types"""
        caplog.set_level(logging.INFO)
        complex_obj = {"key": [1, 2, 3], "nested": {"a": 1}}
        log_multiple_values(complex_obj, (1, 2), None)
        
        assert str(complex_obj) in caplog.text
        assert "(1, 2)" in caplog.text
        assert "None" in caplog.text