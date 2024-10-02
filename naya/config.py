from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "22355402"))
API_HASH = getenv("API_HASH", "5d7858e035599aa080d65e14e5e34d4d")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://ferdisyrl:buburayam1@cluster0.89myp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "7463102988:AAFQp16pBbCSchNMsH6Yd-sAtGLvvH0Q8cs")
OPENAI_API = getenv("OPENAI_API", "")
GIT_TOKEN = getenv("GIT_TOKEN")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/naya1503/Naya-Pyro")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SESSION1 = getenv("SESSION1", "BQFVHcoAQUK5hyNuxBaoPzrYKTfXE2Z_m6Ze2sI_KiSAjUzZzZrBuBnryoCab2EHb-Sg23uruVUphfYQSH0fRtuu6AZEGQ8xooTiVmfTOEOpXzF70JnQD7megmOcigpV0_Eq303aFRZcUYECyWgz2WUPLrMPVVuoQk2DRPm8DSBpdDytzQ25vgnSrn9v8VdijYnBPHdO0qOcgxe9JC_0PjvLGlC23drqpvfvlzmDJ1RpF5Sxp0iAK9RPMTgY4r8wCNlNurKnqwUfXN9DXlAUiibDLIyOCm3eFYWSfTVqPPxK8DN2_4nNhl5wAiDRK7id9MwbP12kq4CMLeuYl_qDkx_2TxXwOgAAAAGmOfANAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
