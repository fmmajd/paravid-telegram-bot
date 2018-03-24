from telegram.ext import Updater
from telegram.ext import CommandHandler

from secret import bot_token

updater = Updater(bot_token)


def start(bot, update, args):
    # import pdb
    # pdb.set_trace()
    chat_id = update.message.chat_id

    if not args:
        bot.sendMessage(
            chat_id, 'لطفا دستور استارت را با نام خود فراخوانی کنید')
    elif len(args) == 1:
        bot.sendMessage(chat_id, 'سلام به {} خوش آمدید!'.format(args[0]))
    else:
        bot.sendMessage(chat_id, 'لطفا یک اسم وارد کنید')


start_command = CommandHandler('start', start, pass_args=True)


updater.dispatcher.add_handler(start_command)

updater.start_polling()
updater.idle()  # for windows, to exit terminal with ctrl-c
