"""
Logging utility for the framework.
"""
import logging
import sys

def setup_logger(name: str = "api-test") -> logging.Logger:
    """
    Sets up a reusable logger for the framework.
    """
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Create console handler with a clean format
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger

# Default framework logger
logger = setup_logger()
