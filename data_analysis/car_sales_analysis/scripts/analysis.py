import os 
import pandas as pd
import logging

def configure_logger(log_file: str, log_name: str) -> logging.Logger:
    """Configure and return a logger with file and console handlers"""
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    
    # Prevent duplicate handlers if logger already exists
    if logger.handlers:
        return logger
    
    # File handler
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

logger = configure_logger(log_file="app.log", log_name='car-sales-analysis')

def read_file(file_path):
  """Read a CSV file with error handling and logging"""

  if not os.path.isfile(file_path):
    print(f"{file_path} doesn't exist or is invalid.")
    return None
  
  try:
    with open(file_path, "r") as file:
      print(f"Opening file: {file_path}")

      content = pd.read_csv(file)
      return content
  except FileNotFoundError as e:
    logger.error(f"File was not found.", e)
    return None
  except PermissionError as e:
    logger.error("You don't have permission to open this file.")
    return None
  except pd.errors.EmptyDataError as e:
    logger.error(f"Error parsing CSV file: {file_path} - {e}")
    return None
  except Exception as e:
    logger.error(f"Unexpected error reading file {file_path}: {e}")
    return None