from telegram.ext import Updater
from telegram.ext import CommandHandler

from telegram.chataction import ChatAction

from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

from secret import bot_token

updater = Updater(bot_token)


def start(bot, update):
    # import pdb
    # pdb.set_trace()
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name

    bot.send_chat_action(chat_id, ChatAction.TYPING)
    bot.sendMessage(chat_id, 'سلام به {} {} خوش آمدید!'.format(first_name, last_name))


def service_keyboard(bot, update):
    keyboard = [
        ['سلام کن', 'خداحافظی کن'],
        ['بیکاریا', 'بیخیال', 'ولم کن'],
        ['یه سطر گنده اینجاس']
    ]
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, 'دوست داری چیکار گنی؟', reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True))


def favor_keyboard(bot, update):
    chat_id = update.message.chat_id
    keyboard = [
        [
            InlineKeyboardButton('باتن اولی', 'https://google.com'),
            InlineKeyboardButton('باتن دومی', 'https://bing.com')
        ]
    ]
    bot.sendMessage(chat_id, 'یکی از باتنا رو شانسی انتخاب نید!', reply_markup=InlineKeyboardMarkup(keyboard))


start_command = CommandHandler('start', start)
service_command = CommandHandler('service', service_keyboard)
favor_command = CommandHandler('links', favor_keyboard)


updater.dispatcher.add_handler(start_command)
updater.dispatcher.add_handler(service_command)
updater.dispatcher.add_handler(favor_command)

updater.start_polling()
updater.idle()  # for windows, to exit terminal with ctrl-c
