import os
import dotenv
from logger import Logger
import json

dotenv.load_dotenv()
logging_level = os.environ.get('LOGGING_LEVEL')
logs_path = os.environ.get('LOGS_PATH')
payload_dir = os.environ.get('PAYLOAD_DIR')
telegram_token = os.environ.get('TELEGRAM_TOKEN')
package_size = int(os.environ.get('PACKAGE_SIZE'))

logger = Logger(logs_path, logging_level)
