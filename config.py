import os
import dotenv
from logger import Logger
from state import State
from storage import JsonFileStorage
import telebot

dotenv.load_dotenv()
logging_level = os.environ.get('LOGGING_LEVEL')
logs_path = os.environ.get('LOGS_PATH')
payload_dir = os.environ.get('PAYLOAD_DIR')
telegram_token = os.environ.get('TELEGRAM_TOKEN')
package_size = int(os.environ.get('PACKAGE_SIZE'))
monitor_timeout = int(os.environ.get('MONITOR_TIMEOUT'))
chat_id = os.environ.get('CHAT_ID')
logger = Logger(logs_path, logging_level)
storage = JsonFileStorage('storage.json')
state = State(storage)
bot = telebot.TeleBot(telegram_token)
is_filter_enabled = False