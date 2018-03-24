from uuid import uuid4

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext import InlineQueryHandler

from telegram.chataction import ChatAction

from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import InputTextMessageContent
from telegram import InlineQueryResultArticle

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
    # this was normal inline buttons
    # keyboard = [
    #     [
    #         InlineKeyboardButton('باتن اولی', 'https://google.com'),
    #         InlineKeyboardButton('باتن دومی', 'https://bing.com')
    #     ]
    # ]
    keyboard = [
        [
            InlineKeyboardButton('باتن اولی', callback_data='1'),
            InlineKeyboardButton('باتن دومی', callback_data='2'),
        ],
        [
            InlineKeyboardButton('باتن سومی', callback_data='3'),
        ]
    ]
    bot.sendMessage(chat_id, 'یکی از باتنا رو شانسی انتخاب نید!', reply_markup=InlineKeyboardMarkup(keyboard))


def favor_handler_button(bot, update):
    query = update.callback_query
    data = query.data
    chat_id = query.message.chat_id
    message_id = query.message.message_id

    description = 'درباره دوره اینجا نوشته می‌شود. داده فرستاده شده {} است' .format(data)
    if data == 1:
        description = 'داده اول'
    elif data == 2:
        description = 'داده دوم'
    elif data == 3:
        description = 'داده سوم'

    bot.editMessageText(text=description, chat_id=chat_id, message_id=message_id)


def feature_inline_query(bot, update):
    query = update.inline_query.query
    inline_query_id=update.inline_query.id
    results = list()
    # import pdb
    # pdb.set_trace()
    results.append(InlineQueryResultArticle(
        id=uuid4(), title="Uppercase", input_message_content=InputTextMessageContent(query.upper())))
    results.append(InlineQueryResultArticle(
        id=uuid4(), title="Lowercase", input_message_content=InputTextMessageContent(query.lower())))
    bot.answerInlineQuery(results=results, inline_query_id=inline_query_id)


start_command = CommandHandler('start', start)
service_command = CommandHandler('service', service_keyboard)
favor_command = CommandHandler('links', favor_keyboard)

favor_handler = CallbackQueryHandler(favor_handler_button)
feature_handler = InlineQueryHandler(feature_inline_query)


updater.dispatcher.add_handler(start_command)
updater.dispatcher.add_handler(service_command)
updater.dispatcher.add_handler(favor_command)
updater.dispatcher.add_handler(favor_handler)
updater.dispatcher.add_handler(feature_handler)

updater.start_polling()
updater.idle()  # for windows, to exit terminal with ctrl-c
