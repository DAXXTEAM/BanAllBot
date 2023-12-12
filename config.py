import os
class Config:
    API_ID=
    API_HASH=""
    TOKEN=""
    SUDO = list(int(i) for i in os.environ.get("SUDO", "").split(" "))
    START_IMG="jdjsjw"
    BOT_ID=
    BOT_USERNAME=""
    BOT_NAME=""
