 os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "26741385"))
    API_HASH = os.environ.get("API_HASH", "8221180729601e66281bff01dcc7d9ec)
    BOT_TOKEN = os.environ.get("AAHu6Rp0nBEM6ZlAhrtBKQA3LKImeyBC3r0")
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Rautela_music_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") "https://t.me/teri_yaari"
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") "https://t.me/teri_yaad"
    START_IMG = os.environ.get("START_IMG", "https://graph.org/file/5505321dd416bfe7794b2.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
