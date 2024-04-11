import os
import dotenv
from logger import Logger
import json

dotenv.load_dotenv()
logging_level = os.environ.get('LOGGING_LEVEL')
logs_path = os.environ.get('LOGS_PATH')
payload_dir = os.environ.get('PAYLOAD_DIR')
telegram_token = os.environ.get('TELEGRAM_TOKEN')
logger = Logger(logs_path, logging_level)

filter = headers = str()
with open(os.path.join(payload_dir, 'filter.json'), 'r') as filter_file, open(os.path.join(payload_dir, 'headers.json')) as headers_file:
    filter = json.load(filter_file)
    headers = json.load(headers_file)
