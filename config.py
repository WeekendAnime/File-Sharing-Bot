import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "8132535187:AAHsm0JsBwr9k8-XuwkzMMXPMViTju-8Zhw")
API_ID = int(os.environ.get("API_ID", "28744454"))
API_HASH = os.environ.get("API_HASH", "debd37cef0ad1a1ce45d0be8e8c3c5e7")


OWNER_ID = int(os.environ.get("OWNER_ID", "6266529037"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://jeffreymosesdj:Jeffrey@cluster2.cuiux.mongodb.net/?retryWrites=true&w=majority&appName=Cluster2")
DB_NAME = os.environ.get("DB_NAME", "Cluster2")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002289759099"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002076655534"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002369384920"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002172787340"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1002397319343"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "6000")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6266529037]
    for x in (os.environ.get("ADMINS", "6266529037").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("@Ongoing_Weekends", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "ᴀʀᴀ!! ᴀʀᴀ!! ɪᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ғᴏʀ ᴍʏ ʟᴏᴠᴇʟʏ ᴋᴀᴡᴀɪɪ 🥰 @JeffreySama !"

START_MSG = os.environ.get("START_MESSAGE", "ᴋᴏɴɪᴄʜɪᴡᴀ {mention}\n\nᴋᴏɴɪᴄʜɪᴡᴀ ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴀɴɪᴍᴇ / ᴍᴏᴠɪᴇ ғɪʟᴇs ɪɴ @Ongoing_Weekends ᴄʜᴀɴɴᴇʟ  ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ. .")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ᴀʀᴀ ᴀʀᴀ!! {mention}\n\n<b> ʜᴀᴘᴘɪɴᴇss ᴀs ᴀ ᴍᴏᴛʜᴇʀ ᴀɴᴅ ʜᴀᴘᴘɪɴᴇss ᴀs ᴀɴ ɪᴅᴏʟ. ɪᴛ ᴍɪɢʜᴛ ʙᴇ ɴᴏʀᴍᴀʟ ᴛᴏ ʜᴀᴠᴇ ᴏɴʟʏ ᴏɴᴇ ʙᴜᴛ ɪ ᴡᴀɴᴛ ʙᴏᴛʜ\n\nKindly ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(6848088376)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
