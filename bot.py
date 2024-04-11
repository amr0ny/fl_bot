from parsing import Parser
import telebot 
from config import *


bot = telebot.TeleBot(telegram_token)
@bot.message_handler(commands=['offers'])
def get_all_orders(message):
    try:
        url = 'https://www.fl.ru'
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
bot.infinity_polling()