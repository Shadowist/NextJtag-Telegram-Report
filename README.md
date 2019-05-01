# NextJtag-Telegram-Report
NextJtag reporting through Telegram!

[![D77-DB9-B1-2-C4-E-42-B2-8-A3-E-EBEAD2-DBA949.jpg](https://i.postimg.cc/yxxW0r82/D77-DB9-B1-2-C4-E-42-B2-8-A3-E-EBEAD2-DBA949.jpg)](https://postimg.cc/q6fkTwnG)

# Under Construction

This is just a little helper tool to query temperatures and voltages on-the-go.

Requirements
1. Python 3
2. https://github.com/python-telegram-bot/python-telegram-bot

The Python Telegram Bot can be installed via pip, so that's easy enough :)

Installation

1. Make sure the requirements are set.
- https://www.python.org
	- Just grab latest
	- Then run `pip install python-telegram-bot`

2. Add the files to the folder containing nextjtag.exe
3. Make a Telegram bot
- Install Telegram (Desktop, phone, wherever)
- Create a new bot: https://core.telegram.org/bots
	- Go down to step 6 for BotFather instructions
- Take note of your new bot's token

4. Replace the token in nextjtag_telegram.cfg
5. Run `python nextjtag_telegram_main.py`! (Or use the included batch file)

# Description

The bot supports two commands:
- `/devices`: Runs `nextjtag` by itself. Queries all devices.
- `/report`: Runs `nextjtag -a -t -v`. There's some extra formatting instructions in the script to make it mobile friendly.

This is a little pet project of mine. If it's helpful in anyway, I take beer donations ;)

BTC: 13mjkM59ydce8cuJiBCg2Bn4XxzTUVEEY3
