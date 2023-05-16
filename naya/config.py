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
SESSION1 = getenv("SESSION1", "BQAhIHQAnUF9x31kLxl9FyLnPSKHl3sNPaQa5_zaUSS3ZPWngxPmvvuNd3eLy9N4BOMcpKOftGbIFMJLyr0CJG0e08NzkkPOwIVeAywHCshwDX7ztHEfkFcKeL2PVCI1bznuz6V6285qa2ILXGEjEZG7CjHFrbmOULLu1KGnP80OteudEoQOAa52oVKpY4gFkEGPXL4cOHx3Brkeaz7kBpUwv00ia9cx5h9I-gFy1OinG2pINN70QWOxXRwDMzakSr_JGlOjS0E2WT9VBzY5zocaB_JTCZx6zqXGVjNKuNo6vESsD972I8Nra6hfgGys8V4hKeq7Icj2-p_bDX9yoys9ftiWzgAAAABQNCQsAA")
SESSION2 = getenv("SESSION2", "BQAhIHQAIv18K3mvjVvkoufvL8JQBtyUnJuNs4pBDpXu8QpLAp2P0Ca6T-CzvSP8GFRou10jZJTQc4Cmy_1FBKwW-1BADGKncaFW8jV43K3fAVLX6qsqs3Lw1oChg68GJ16cdS6YtZt2HK1Ala4lbEj-dwIVSMe27YWlMSPuilRHE_zL4VgVCHNRKfshjME5Wmg7KuxdqAw8SMBrNxikULWoYKFDjwY9xQ-QmeieS4_zU3Wk3NjG-i0Fzyuip5fa1w2JGoEmJ5Vm1ZODtFlAducE6u2jfPfqHpvmeEKAjMiDnqg6gh1z9KFaIuYBhXIcgRcukblN2JAM_6pwR9OwTXyqvQo2gwAAAABnkfUnAA")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
