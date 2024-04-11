from parsing import Parser
import telebot 
from config import *


bot = telebot.TeleBot(telegram_token)
@bot.message_handler(commands=['orders'])
def get_all_orders(message):
    url = 'https://fl.ru'
    parser = Parser(url, filter, headers=headers)
    data = parser.parse_project_list()
    data = '\n\n'.join([' '.join([str(v) for v in item]) for item in data])

    if len(data) > 4096:
        for x in range(0, len(data), 4096):
            bot.send_message(message.chat.id, data[x:x+4096])
    else:
        bot.send_message(message.chat.id, data)

    logger.info(data)

bot.infinity_polling()