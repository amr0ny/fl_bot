from parsing import Parser
from config import payload_dir, package_size, telegram_token, logger, bot, is_filter_enabled
import os
import json
from monitor import run_monitor
import threading
from utils import extract_args

@bot.message_handler(commands=['offers'])
def get_all_orders(message):
    try:
        url = 'https://www.fl.ru'
        with open(os.path.join(payload_dir, 'filter.json'), 'r') as filter_file, open(os.path.join(payload_dir, 'headers.json')) as headers_file:
            filter = json.load(filter_file)
            headers = json.load(headers_file)
        parser = Parser(url, filter, headers=headers, package_size=package_size)
        data = parser.parse_project_list()
        data = '\n\n'.join([' '.join([str(v) for v in item]) for item in data])
        if len(data) > 4096:
            for x in range(0, len(data), 4096):
                bot.send_message(message.chat.id, data[x:x+4096])
        else:
            bot.send_message(message.chat.id, data)

        logger.info(data)
    except Exception as err:
        logger.error('An arror occured:', err)
        bot.send_message(message.chat.id, f'If you see this you may need to configure either parser or bot: {err}')

@bot.message_handler(commands=['token'])
def set_token(message):
    global is_filter_enabled
    try:
        logger.debug(message.chat.id)
        args = extract_args(message.text)
        if len(args) < 1 or args is None:
            raise Exception('The command "token" must contain at least one argument')
        token = args[0]
        with open(os.path.join(payload_dir, 'headers.json'), 'r+') as headers_file:
            headers = json.load(headers_file)
            headers['Cookie'] = f'PHPSESSID={token};'
            headers_file.seek(0)
            json.dump(headers, headers_file, indent=2)
            headers_file.truncate()

        msg = 'Session token updated.'
        is_filter_enabled = True
        logger.info(msg)
        bot.send_message(message.chat.id, msg)

    except Exception as err:
        logger.error('An arror occured:', err)
        bot.send_message(message.chat.id, f'An error occured while updating token: {err}')

monitor = threading.Thread(target=run_monitor)
monitor.start()
bot.infinity_polling()
monitor.join()