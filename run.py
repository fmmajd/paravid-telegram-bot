from telegram.ext import Updater
from telegram.ext import CommandHandler

updater = Updater('568438669:AAGANxKfG1HjvhfOJpWQewljIjKTXMqbd4E')


def start(bot, update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, 'hello dear user!')


start_command = CommandHandler('start', start)


updater.dispatcher.add_handler(start_command)

updater.start_polling()
updater.idle()  # for windows, to exit with ctrl-c
