import os 
import pandas as pd
from file_reader import configure_logger

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
    configure_logger.error(f"File was not found.", e)
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