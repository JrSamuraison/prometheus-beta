import logging
import pytest
from src.multi_line_logger import log_multiline

class TestMultiLineLogger:
    def test_single_string_logging(self, caplog):
        """Test logging a single string message"""
        caplog.set_level(logging.INFO)
        log_multiline("Test message")
        
        assert len(caplog.records) == 3  # separator top, message, separator bottom
        assert caplog.records[1].message == "Test message"
        assert caplog.records[0].message == caplog.records[2].message  # separators match

    def test_multiple_strings_logging(self, caplog):
        """Test logging multiple string messages"""
        caplog.set_level(logging.INFO)
        messages = ["First line", "Second line", "Third line"]
        log_multiline(messages)
        
        assert len(caplog.records) == 5  # separators and 3 messages
        assert caplog.records[1].message == "First line"
        assert caplog.records[2].message == "Second line"
        assert caplog.records[3].message == "Third line"

    def test_custom_separator(self, caplog):
        """Test custom separator character and length"""
        caplog.set_level(logging.INFO)
        log_multiline("Custom separator", separator_char='*', separator_length=20)
        
        assert len(caplog.records[0].message) == 20
        assert caplog.records[0].message[0] == '*'

    def test_log_level(self, caplog):
        """Test different logging levels"""
        caplog.set_level(logging.ERROR)
        log_multiline("Error message", level=logging.ERROR)
        
        assert len(caplog.records) == 3
        assert all(record.levelno == logging.ERROR for record in caplog.records)

    def test_invalid_separator_char(self):
        """Test invalid separator character"""
        with pytest.raises(ValueError, match="Separator must be a single character"):
            log_multiline("Test", separator_char='too long')

    def test_invalid_separator_length(self):
        """Test invalid separator length"""
        with pytest.raises(ValueError, match="Separator length must be at least 1"):
            log_multiline("Test", separator_length=0)