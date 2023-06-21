from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "12857763"))
API_HASH = getenv("API_HASH", "7b71e8bca0d5e1c6d8383ae818d9ec8d")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://fadhilabdat:fadhil123@cluster0.wnpfjnd.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5921265623:AAEQGbsR32yMh1LD_kf252qlIvb-N66cars")
OPENAI_API = getenv("OPENAI_API", "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")
GIT_TOKEN = getenv("GIT_TOKEN")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/naya1503/Naya-Pyro")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SESSION1 = getenv("SESSION1", "BQAhIHQAGD8dU1rfbtwsTp7ho46_DUsVvhAMXpxC8bp0fYZkUinLRcLCMb3bJ0dO2Qi1N7rujBV57-GoyCD7WCQpU-KUdxDokNacslevt9vMoHX77wFYHENYDvHFsIFAK3exIlA36ajTx6nqJUdADQAGGLlE_XXS807j9NAgDQIeUmJeT-RyE_27WRu4wpL5wRPMe3CaC0YaQzBWveGoDfK95xLaBcdX4eNvGRlafUpTxeA-POH_R7Gpw-b3hklwos_5IvG8gLTclDq3a2WtecZcC2YFxT4eYxUf3w849iHz7JEeziR7chAajV9J0NldDTgN1nMc_koBKjNXRqjYMJW4kM8WaAAAAABqsXAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
