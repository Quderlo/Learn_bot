import logging
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings


PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет!')
    update.message.reply_text('Список команд: \n 1) /start \n 2) /joke \n 3) /iq ')

def joke_user(update, context):
    update.message.reply_text('Знаете почему нельзя шутить про подлодку Курск?')
    update.message.reply_text('Потому что в материале слишком много воды')


def iq_user(update, context):
    update.message.reply_text('Твой iq = ' + str(random.randint(1,200)))



def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("joke", joke_user))
    dp.add_handler(CommandHandler("iq", iq_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('ВКЛ')
    logging.basicConfig(filename='bot.log', level=logging.INFO)
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
