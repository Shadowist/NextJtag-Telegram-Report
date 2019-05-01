# Standard Import
import logging
import time
import threading

# Telegram Import
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

# Local Import
import nextjtag_telegram_report
import nextjtag_telegram_utils
CONFIG = nextjtag_telegram_utils.receive_cfg()

updater = Updater(token=CONFIG['token'])
dispatcher = updater.dispatcher

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

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

# Command: /devices
def devices(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=nextjtag_telegram_report.report("devices"))
report_devices_handler = CommandHandler('devices', devices)
dispatcher.add_handler(report_devices_handler)

# Command: /report
def report(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=nextjtag_telegram_report.report("general"))
report_general_handler = CommandHandler('report', report)
dispatcher.add_handler(report_general_handler)

# Messages: Any non-command
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hi! :)")
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

# Start Bot!
updater.start_polling()

# Hack for ctrl+c on Windows 10 Powershell
def work():
    time.sleep(10000)        
t = threading.Thread(target=work)
t.daemon = True
t.start()
while(True):
    try:
        t.join(0.1)
    except KeyboardInterrupt:
        updater.stop()
        exit()
