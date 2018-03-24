from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.chataction import ChatAction

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


start_command = CommandHandler('start', start)


updater.dispatcher.add_handler(start_command)

updater.start_polling()
updater.idle()  # for windows, to exit terminal with ctrl-c
