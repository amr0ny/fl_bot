from parsing import Parser
from time import sleep
from parsing import Parser
import telebot 
from config import payload_dir, package_size, is_filter_enabled, monitor_timeout, logger, state, chat_id, bot
import os
import json

def run_monitor():
    global is_filter_enabled
    url = 'https://www.fl.ru'
    while True:
        try:
            with open(os.path.join(payload_dir, 'filter.json'), 'r') as filter_file, open(os.path.join(payload_dir, 'headers.json')) as headers_file:
                filter = json.load(filter_file)
                headers = json.load(headers_file)
            parser = Parser(url, filter, headers=headers, package_size=package_size)
            data = parser.parse_project_list()
            recent_project = tuple(state.get_state('recent_project'))
            if recent_project is not None and data[0] != recent_project:
                bot.send_message(chat_id, ' '.join([str(v) for v in data[0]]))
                state.set_state('recent_project', data[0])
            else:
                state.set_state('recent_project', data[0])
        except Exception as err:
            
            if is_filter_enabled:
                bot.send_message(chat_id, f'If you see this you may need to configure either parser or bot: {err}')
                is_filter_enabled = False

        sleep(monitor_timeout)      


        
        
        