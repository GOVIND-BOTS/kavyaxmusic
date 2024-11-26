import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables
load_dotenv()

# Pyrogram and Bot configuration
API_ID = int(getenv("API_ID", "23861270"))
API_HASH = getenv("API_HASH", "5b8eb94346561060b0074aa574a92a6f")
BOT_TOKEN = getenv("BOT_TOKEN", "6858692873:AAHIb3j5bQQqDQShBj7lG0oUYXfX24rgzsY")

# YouTube API Key
YOUTUBE_API_KEY = getenv("YOUTUBE_API_KEY", "AIzaSyDeqyflL1tvNXIr4rf7OXw9bHpyA5gCPrM")

# MongoDB
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority")

# Other configurations
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002379786490"))
OWNER_ID = int(getenv("OWNER_ID", "6117113351"))

# Heroku settings
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# GitHub repository
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/GOVIND-BOTS/kavyaxmusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support links
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kavya_music_update")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kavya_music_spport")

# Audio/video file size limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# Spotify configuration
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Playlist fetch limit
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Pyrogram string sessions
STRING1 = getenv("STRING_SESSION", "BQDNvmIAtGzC1yEf3jNt_6ZrGAukssAGQklXXU6NrXeIoPukRt_z-qcJEioZz06qRAqJy4UsmTsTMobAd6KZSLQjprHa02Oh9-URlUUInoLs6hlvMusyL0T-V8jiAwG-cTJUpZodYjUH2gh8y-mqm04LdaF3HdxUvodZ3ExGpmOqKTs9tqlVslWpVBn-UipYXoQ3WelYaNKMT9R8qbMnjjp1ce5ZDauJP5eAsJV0znGM73FNrTuhZropyie1O-E5_a7Y3o6hGwIYOA4-uauXROBHzLMMotQ2zuorFXeyrt99kn_YQdA89pzKlZWRJLi6bR-OVbFnihdxX5gxzFxfyuBpFbTN-QAAAAFsm74HAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Bot URLs and images
START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/25efe6aa029c6baea73ea.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg")

# Helper functions
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Validate URLs
if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Ensure it starts with https://")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Ensure it starts with https://")
