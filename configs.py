from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23990433"))
    API_HASH = getenv("API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")
    BOT_TOKEN = getenv("BOT_TOKEN", "6621256999:AAESnf5zut8Jkt6f4w9r_uCVtfIzJK4pawU")
    FSUB = getenv("FSUB", "VillageTV")
    CHID = int(getenv("CHID", "-1001842572271"))
    SUDO = list(map(int, getenv("SUDO", "5821871362").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sankar:sankar@sankar.lldcdsx.mongodb.net/?retryWrites=true&w=majority")
    WEB_SERVER = getenv("WEB_SERVER", True)
    PORT = int(getenv("PORT", 8080))
cfg = Config()
