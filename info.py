import re
import os
from os import environ
from Script import script
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5397984467').split()]
USERNAME = environ.get('USERNAME', "https://telegram.me/biisal")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001949498981'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/+4RB2-U2o9yE4ZmQ9')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001934462631').split()]
DATABASE_URI = environ.get('DATABASE_URI', "")

DATABASE_NAME = environ.get('DATABASE_NAME', "TELEGRAM_BOT_INFO")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1001949498981'))
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/ccb9db43e62a2e524928e.jpg')
START_IMG = environ.get('START_IMG', 'https://graph.org/file/4dad0cc16f190468454ee.jpg')
#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','-1001943068381'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1001905000346'))
URL = environ.get('URL', 'mytestbot-308325bcba17.herokuapp.com')
OMNI = 'omnifly.in.net'
STICKERS_IDS = ('CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME').split()
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1001949498981'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/Movie_Url_link_downloader/17")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "5bb6e402dd86fb8774690a5f4a65d2a2c0c04877")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", OMNI)
SHORTENER_API2 = environ.get("SHORTENER_API2", "41a89e7a1f16e7dbec0ee52d743f3b5a38a09613")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", OMNI)
SHORTENER_API3 = environ.get("SHORTENER_API3", "f287e7e9b1a23c34f542f77787d39607cae36a4d")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", OMNI)
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
auth_channel = environ.get('AUTH_CHANNEL', '-1001734958816')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1001812797837'))

# hastags request features
request_channel = environ.get('REQUEST_CHANNEL', '-1001949498981')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
UPI_PAY_LOGS = int(environ.get('UPI_PAY_LOGS', '-1002000054678'))
# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)