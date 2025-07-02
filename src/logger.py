import logging
from datetime import datetime
import os

# Sets what will be the name of the newly created log...
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Created a folder with name LOGS and File name given above...
logs_path = os.path.join(os.getcwd(),'LOGS', LOG_FILE_NAME)

# Makes folder in the directory...
os.makedirs(logs_path, exist_ok=True)

# Now after creating the file then the directory and given file name...
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH, 
    # format= how the log file will return the data shown in it...
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)