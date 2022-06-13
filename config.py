## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAAYS3qIMgZuuTcbLPBO-ELZ08a5KOSbvbgm4kBsFU6LMQbkYw6XB0qK5tnbsKbcyp9AMFTSD8lcOVBtdXMdOZfbrskzy015_hSxQ5nwYvi6Jacl0O2scGxdB-uomWGUzTmHG11s36GUi-rwh-b4Vc0rGDQdaDLaXS_oukJw98b_y5QqQS3orPy26cX1jx41YcX343zgL_iL1zrPpB4NBJzP6OUxp1U1SeyHtFZs_MMdToGd7dRAZqUexRRQGmrqpaNstgmtyGTeGhw2Gil-Rn4PNurmlTeMecXFd0r0gnV3OfsMpc1VuWzCHfBBwG8ox9zGlvEp7SED5tGMDjaYw6A7b7OYLAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5314045578:AAGid9KuRSFmaEHXH1mBWRB7fYzgUdDAvoU")
BOT_NAME = getenv("BOT_NAME", "music lusefr")
API_ID = int(getenv("API_ID", "8153958"))
API_HASH = getenv("API_HASH", "19183b7af816502cbafadba32f2cea4d")
OWNER_NAME = getenv("OWNER_NAME", "YYX55")
OWNER_USERNAME = getenv("OWNER_USERNAME", "YYX55")
ALIVE_NAME = getenv("ALIVE_NAME", "lusefr")
BOT_USERNAME = getenv("BOT_USERNAME", "Bomuslusbot")
OWNER_ID = getenv("OWNER_ID", "5107883171")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "king123a0")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "king1223a")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "wzwzwz1")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "wzwzwz1")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5107883171").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d70bb6fa92728763c671f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
