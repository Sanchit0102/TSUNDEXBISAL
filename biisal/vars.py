# (c) adarsh-goel (c) @biisal (c) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
DS_bot_name = "Sɪʟᴇɴᴛ Sᴛʀᴇᴀᴍᴇʀ" #This Extra Function Added By 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
DS_bot_username = "DS_FILE_2_LINK_BOT" #Add Bot Username Without '@'
silent_channel = "https://telegram.me/THE_SILENT_TEAMS" #Update Channel Link
silent_auto_grp = "https://t.me/+CZH0JaSwih44ZTM1" #Auto Filter Group Link

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '25833520'))
    API_HASH = str(getenv('API_HASH', '7d012a6cbfabc2d0436d7a09d8362af7'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '5585418491:AAH-vV8qtcGm84k3XEIgI8sCvY70w1PSpJs'))
    name = str(getenv('name', 'bisal_file2link_bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '400'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001611644647'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1001611644647'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = [int(x) for x in os.environ.get("OWNER_ID", "1562935405").split()]
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'THE_DS_OFFICIAL'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://trumbot:trumbot@cluster0.cfkaeno.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None)) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "")).split()))   
    BAN_ALERT = str(getenv('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ. \n Pᴏʀɴ Aʟʟᴏᴡ Nʜɪ Hᴀɪ BSDK!!</b>'))
