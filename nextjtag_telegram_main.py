# Standard Import
import logging

# Telegram Import
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

# Local Import
import nextjtag_telegram_utils
CONFIG = nextjtag_telegram_utils.receive_cfg()

updater = Updater(token=CONFIG['token'])
dispatcher = updater.dispatcher

# Command: /start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hi! :)")
    bot.send_message(chat_id=update.message.chat_id, text=nextjtag_telegram_utils.show_commands())
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Command: /help
def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=nextjtag_telegram_utils.show_commands())
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

# Messages: Any non-command
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hi! :)")
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

# Start Bot!
updater.start_polling()
