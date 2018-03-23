from telegram.ext import Updater
from telegram.ext import CommandHandler

updater = Updater('568438669:AAGANxKfG1HjvhfOJpWQewljIjKTXMqbd4E')


def start(bot, update, args):
    # import pdb
    # pdb.set_trace()
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, 'سلام به {} خوش آمدید!'.format(args[0]))


start_command = CommandHandler('start', start, pass_args=True)


updater.dispatcher.add_handler(start_command)

updater.start_polling()
updater.idle()  # for windows, to exit terminal with ctrl-c
