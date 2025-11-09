# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "22114233"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "d7abcec5c967414fadb1d438fa05ebea")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8494390478:AAGnOwNOY4Yr8kEmHsZ07E37_Db78jG_6kI")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@Cobranew12345_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "1403488629"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1403488629").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003269370257"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://saraswatisharmapbc:L8aRiWhBbhi8mFwN@cluster0.gxhxgye.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1003269370257"))

