import psutil
import logging
import os

def log_memory_usage(logger=None):
    """
    Log detailed memory usage statistics of the current process.
    
    Args:
        logger (logging.Logger, optional): Logger to use for reporting. 
                If None, creates a default logger.
    
    Returns:
        dict: A dictionary containing memory usage statistics
    """
    # Create a default logger if none is provided
    if logger is None:
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
    
    try:
        # Get the current process
        process = psutil.Process(os.getpid())
        
        # Collect memory information
        memory_info = process.memory_info()
        
        # Prepare memory statistics
        memory_stats = {
            'rss': memory_info.rss,  # Resident Set Size (actual physical memory used)
            'vms': memory_info.vms,  # Virtual Memory Size
            'uss': getattr(memory_info, 'uss', None),  # Unique Set Size (if available)
            'pss': getattr(memory_info, 'pss', None)   # Proportional Set Size (if available)
        }
        
        # Log the memory statistics
        logger.info(f"Memory Usage Statistics:")
        for key, value in memory_stats.items():
            if value is not None:
                logger.info(f"{key.upper()}: {value} bytes ({value / (1024*1024):.2f} MB)")
        
        return memory_stats
    
    except Exception as e:
        logger.error(f"Error collecting memory usage: {e}")
        return {}