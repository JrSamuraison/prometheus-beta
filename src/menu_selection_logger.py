import logging
from typing import List, Union

class MenuSelectionLogger:
    """
    A class to log user selections from a menu with various logging capabilities.
    
    Attributes:
        log_file (str): Path to the log file.
        logger (logging.Logger): Logger instance for recording selections.
    """
    
    def __init__(self, log_file: str = 'menu_selections.log'):
        """
        Initialize the MenuSelectionLogger.
        
        Args:
            log_file (str, optional): Path to the log file. Defaults to 'menu_selections.log'.
        """
        # Configure logging
        logging.basicConfig(
            filename=log_file, 
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        self.log_file = log_file
    
    def log_selection(self, menu_name: str, selection: Union[str, int, List[Union[str, int]]]) -> None:
        """
        Log a user's menu selection.
        
        Args:
            menu_name (str): Name or identifier of the menu.
            selection (Union[str, int, List[Union[str, int]]]): Selected item(s).
        
        Raises:
            ValueError: If menu_name is empty or selection is None.
        """
        # Validate inputs
        if not menu_name:
            raise ValueError("Menu name cannot be empty")
        
        if selection is None:
            raise ValueError("Selection cannot be None")
        
        # Convert selection to a string representation for logging
        if isinstance(selection, list):
            selection_str = ', '.join(str(item) for item in selection)
        else:
            selection_str = str(selection)
        
        # Log the selection
        log_message = f"Menu: {menu_name} - Selection: {selection_str}"
        self.logger.info(log_message)
    
    def clear_log(self) -> None:
        """
        Clear the contents of the log file.
        """
        with open(self.log_file, 'w'):
            pass
        self.logger.info("Log file cleared")
    
    def get_log_contents(self) -> List[str]:
        """
        Read and return the contents of the log file.
        
        Returns:
            List[str]: Lines from the log file.
        """
        try:
            with open(self.log_file, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            return []