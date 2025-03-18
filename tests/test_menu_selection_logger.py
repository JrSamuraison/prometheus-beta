import os
import pytest
from src.menu_selection_logger import MenuSelectionLogger

class TestMenuSelectionLogger:
    @pytest.fixture
    def log_file(self, tmp_path):
        """Create a temporary log file for testing."""
        return str(tmp_path / "test_menu_selections.log")
    
    def test_log_single_selection(self, log_file):
        """Test logging a single menu selection."""
        logger = MenuSelectionLogger(log_file)
        logger.log_selection("Main Menu", "Option 1")
        
        log_contents = logger.get_log_contents()
        assert len(log_contents) == 1
        assert "Menu: Main Menu - Selection: Option 1" in log_contents[0]
    
    def test_log_multiple_selections(self, log_file):
        """Test logging multiple menu selections."""
        logger = MenuSelectionLogger(log_file)
        logger.log_selection("Settings Menu", ["Volume", "Brightness"])
        
        log_contents = logger.get_log_contents()
        assert len(log_contents) == 1
        assert "Menu: Settings Menu - Selection: Volume, Brightness" in log_contents[0]
    
    def test_log_numeric_selection(self, log_file):
        """Test logging numeric menu selections."""
        logger = MenuSelectionLogger(log_file)
        logger.log_selection("Number Menu", 42)
        
        log_contents = logger.get_log_contents()
        assert len(log_contents) == 1
        assert "Menu: Number Menu - Selection: 42" in log_contents[0]
    
    def test_empty_menu_name_raises_error(self, log_file):
        """Test that empty menu name raises a ValueError."""
        logger = MenuSelectionLogger(log_file)
        
        with pytest.raises(ValueError, match="Menu name cannot be empty"):
            logger.log_selection("", "Option")
    
    def test_none_selection_raises_error(self, log_file):
        """Test that None selection raises a ValueError."""
        logger = MenuSelectionLogger(log_file)
        
        with pytest.raises(ValueError, match="Selection cannot be None"):
            logger.log_selection("Menu", None)
    
    def test_clear_log(self, log_file):
        """Test clearing the log file."""
        logger = MenuSelectionLogger(log_file)
        logger.log_selection("Test Menu", "Option")
        
        # Verify log is not empty
        log_contents = logger.get_log_contents()
        assert len(log_contents) > 0
        
        # Clear log
        logger.clear_log()
        
        # Verify log is empty
        log_contents = logger.get_log_contents()
        assert len(log_contents) == 0
    
    def test_get_log_contents_nonexistent_file(self):
        """Test get_log_contents with a nonexistent file."""
        non_existent_file = "/path/to/nonexistent/file.log"
        logger = MenuSelectionLogger(non_existent_file)
        
        log_contents = logger.get_log_contents()
        assert log_contents == []