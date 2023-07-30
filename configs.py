from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23990433"))
    API_HASH = getenv("API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")
    BOT_TOKEN = getenv("BOT_TOKEN", "6324395748:AAGU-qGihOAcRgrxfdccuyySk7ST6hko4MU")
    FSUB = getenv("FSUB", "none")
    CHID = int(getenv("CHID", "-1001727782613"))
    SUDO = list(map(int, getenv("SUDO", "5821871362").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Test:1234@cluster0.2bzsp0q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    WEB_SERVER = getenv("WEB_SERVER", True)
    PORT = int(getenv("PORT", 8080))
cfg = Config()
