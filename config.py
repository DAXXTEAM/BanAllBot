import os
class Config:
    API_ID=24509589
    API_HASH="717cf21d94c4934bcbe1eaa1ad86ae75"
    TOKEN="6796545941:AAGyuhnW9Gi4nCbyUsrB-SzbqUHArgtHVXg"
    SUDO = list(int(i) for i in os.environ.get("SUDO", "6691393517").split(" "))
    START_IMG="https://telegra.ph/file/52fefb8bd51289a83a49b.jpg"
    BOT_ID=6796545941
    BOT_USERNAME="ZuliaiBot"
    BOT_NAME="ZuliaiBot"
