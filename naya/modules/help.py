import re
from datetime import datetime
from pyrogram.raw.functions import Ping
from pyrogram.types import *

from . import *

from .ping import START_TIME, _human_time_duration


@bots.on_message(filters.command(["help", "alive"], cmd) & filters.me)
async def _(client, message):
    if message.command[0] == "alive":
        text = f"user_alive_command {message.id} {message.from_user.id}"
    if message.command[0] == "help":
        text = "user_help_command"
    try:
        x = await client.get_inline_bot_results(app.me.username, text)
        for m in x.results:
            await message.reply_inline_bot_result(x.query_id, m.id)
    except Exception as error:
        await message.reply(error)


@app.on_inline_query(filters.regex("^user_alive_command"))
async def _(client, inline_query):
    get_id = inline_query.query.split()
    expired = "__none__"
    status1 = "premium"
    for my in botlist:
        if int(get_id[2]) == int(my.me.id):
            users = 0
            group = 0
            async for dialog in my.get_dialogs():
                if dialog.chat.type == enums.ChatType.PRIVATE:
                    users += 1
                elif dialog.chat.type in (
                    enums.ChatType.GROUP,
                    enums.ChatType.SUPERGROUP,
                ):
                    group += 1
            if int(get_id[2]) == DEVS:
                status = "founder"
                expired = "__none__"
            else:
                status = "owner"
                expired = "__none__"
            if int(get_id[2]) == DEVS:
                button = [
                    [
                        InlineKeyboardButton(
                            text="close",
                            callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}",
                        ),
                        InlineKeyboardButton(
                            text="support",
                            url=f"https://t.me/kynansupport",
                        ),
                    ],
                ]
            else:
                button = [
                    [
                        InlineKeyboardButton(
                            text="close",
                            callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}",
                        ),
                        InlineKeyboardButton(
                            text="support",
                            url=f"https://t.me/kynansupport",
                        ),
                    ]
                ]
            start = datetime.now()
            await my.invoke(Ping(ping_id=0))
            ping = (datetime.now() - start).microseconds / 1000
            uptime_sec = (datetime.utcnow() - START_TIME).total_seconds()
            uptime = await _human_time_duration(int(uptime_sec))
            msg = f"""
<b>Naya-Pyro</b>
     <b>status:</b> <code>{status1}[{status}]</code>
          <b>dc_id:</b> <code>{my.me.dc_id}
          <b>ping_dc:</b> <code>{ping} ms</code>
          <b>peer_users:</b> <code>{users} users</code>
          <b>peer_group:</b> <code>{group} group</code>
          <b>uptime:</b> <code>{uptime}</code>
          <b>expired:</b> <code>{expired}</code>
"""
            await client.answer_inline_query(
                inline_query.id,
                cache_time=60,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="💬",
                            reply_markup=InlineKeyboardMarkup(button),
                            input_message_content=InputTextMessageContent(msg),
                        )
                    )
                ],
            )


@app.on_inline_query(filters.regex("^alv_cls"))
async def _(cln, cq):
    get_id = cq.data.split()
    if not cq.from_user.id == int(get_id[2]):
        return await cq.answer(
            f"❌ GAUSAH PENCET ANJENG, GUE JIJIK.",
            True,
        )
    unPacked = unpackInlineMessage(cq.inline_message_id)
    for my in bots:
        if cq.from_user.id == int(my.me.id):
            await my.delete_messages(
                unPacked.chat_id, [int(get_id[1]), unPacked.message_id]
            )


@app.on_inline_query(filters.regex("^user_help_command"))
async def _(client, inline_query):
    msg = f"<b>Help Inline Menu\nPrefixes: <code>{cmd}</code></b>"
    await client.answer_inline_query(
        inline_query.id,
        cache_time=60,
        results=[
            (
                InlineQueryResultArticle(
                    title="Help Menu!",
                    reply_markup=InlineKeyboardMarkup(
                        paginate_modules(0, CMD_HELP, "help")
                    ),
                    input_message_content=InputTextMessageContent(msg),
                )
            )
        ],
    )


@app.on_callback_query(filters.regex(r"help_(.*?)"))
async def _(client, callback_query):
    mod_match = re.match(r"help_module\((.+?)\)", callback_query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", callback_query.data)
    next_match = re.match(r"help_next\((.+?)\)", callback_query.data)
    back_match = re.match(r"help_back", callback_query.data)
    if mod_match:
        module = (mod_match.group(1)).replace(" ", "_")
        text = (
            f"<b>Bantuan Untuk {CMD_HELP[module].__MODULE__}\n{CMD_HELP[module].__HELP__}</b>\n"
        )
        await callback_query.edit_message_text(
            text,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("❮", callback_data="help_back")]]
            ),
            disable_web_page_preview=True,
        )
     if "Animasi" in text:
            text = f"<b>Help Inline Menu\nPrefixes: <code>{COMMAND}</code></b>"
            button = [
                [
                    InlineKeyboardButton(
                        "Animasi 1", callback_data="animasi animasi_1"
                    ),
                    InlineKeyboardButton(
                        "Animasi 2", callback_data="animasi animasi_2"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Animasi 3", callback_data="animasi animasi_3"
                    ),
                    InlineKeyboardButton(
                        "Animasi 4", callback_data="animasi animasi_4"
                    ),
                ],
                [InlineKeyboardButton("❮", callback_data="help_back")],
            ]
    top_text = f"<b>Help Inline Menu\nPrefixes: <code>{cmd}</code></b>"
    if prev_match:
        curr_page = int(prev_match.group(1))
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, CMD_HELP, "help")
            ),
            disable_web_page_preview=True,
        )
    if next_match:
        next_page = int(next_match.group(1))
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, CMD_HELP, "help")
            ),
            disable_web_page_preview=True,
        )
    if back_match:
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(paginate_modules(0, CMD_HELP, "help")),
            disable_web_page_preview=True,
        )
        
        
@app.on_callback_query(filters.regex("^animasi"))
async def _(client, callback_query):
    data = callback_query.data.split()[1]
    button = [[InlineKeyboardButton("❮", callback_data="animasi animasi_back")]]
    if data == "animasi_1":
        msg = f"""
<b>Help Animasi 1
 
๏ Perintah:  <code>{cmd}dino</code>
◉ Penjelasan:  Coba sendiri.

๏ Perintah:  <code>{cmd}babi</code>
◉ Penjelasan:  Coba sendiri.

๏ Perintah: <code>{cmd}santet</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah:  <code>{cmd}gabut</code>
◉ Penjelasan:  Coba sendiri.

๏ Perintah: <code>{cmd}sayang</code>
◉ Penjelasan: Coba sendiri.</b>
"""
    if data == "animasi_2":
        msg = f"""
<b>Help Animasi 2
 
๏ Perintah:  <code>{cmd}hack</code>
◉ Penjelasan:  Coba sendiri.

๏ Perintah:  <code>{cmd}hug</code>
◉ Penjelasan:  Coba sendiri.

๏ Perintah: <code>{cmd}bomb</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah:  <code>{cmd}brain</code>
◉ Penjelasan:  Coba sendiri.

๏ Perintah: <code>{cmd}kontol</code>
◉ Penjelasan: Coba sendiri.</b>
"""
    if data == "animasi_3":
        msg = f"""
<b>Help Animasi 3
 
๏ Perintah:  <code>{cmd}penis</code>
◉ Penjelasan:  Coba sendiri.

๏ Perintah:  <code>{cmd}hmm</code>
◉ Penjelasan:  Coba sendiri.

๏ Perintah: <code>{cmd}tembak</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah:  <code>{cmd}bundir</code>
◉ Penjelasan:  Coba sendiri.

๏ Perintah: <code>{cmd}helikopter</code>
◉ Penjelasan: Coba sendiri.</b>
"""
    if data == "animasi_4":
        msg = f"""
<b>Help Animasi 4
 
๏ Perintah:  <code>{cmd}y</code>
◉ Penjelasan:  Coba sendiri.

๏ Perintah:  <code>{cmd}love</code>
◉ Penjelasan:  Coba sendiri.

๏ Perintah: <code>{cmd}awk</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah:  <code>{cmd}nah</code>
◉ Penjelasan:  Coba sendiri.

๏ Perintah: <code>{cmd}ajg</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>{cmd}loveyou</code>
◉ Penjelasan: Coba sendiri.</b>
"""
    if data == "animasi_back":
        msg = f"<b>Help Inline Menu\nPrefixes: <code>{COMMAND}</code></b>"
        button = [
            [
                InlineKeyboardButton("Animasi 1", callback_data="animasi animasi_1"),
                InlineKeyboardButton("Animasi 2", callback_data="animasi animasi_2"),
            ],
            [
                InlineKeyboardButton("Animasi 3", callback_data="animasi animasi_3"),
                InlineKeyboardButton("Animasi 4", callback_data="animasi animasi_4"),
            ],
            [InlineKeyboardButton("❮", callback_data="help_back")],
        ]
    await callback_query.edit_message_text(
        msg, reply_markup=InlineKeyboardMarkup(button)
    )
