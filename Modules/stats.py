from datetime import datetime
from pyrogram import filters, Client
from pyrogram.types import Message
from config import (bot, HNDLR, SUDO_USERS, LOGS_CHANNEL )
from pyrogram import Client, filters


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["stats"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["stats"], prefixes=HNDLR))
async def stats(client: Client, message: Message):
    await message.edit_text("Collecting stats")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    Meh=await client.get_me()
    group = ["supergroup", "group"]
    async for dialog in client.iter_dialogs():
        if dialog.chat.type == "private":
            u += 1
        elif dialog.chat.type == "bot":
            b += 1
        elif dialog.chat.type == "group":
            g += 1
        elif dialog.chat.type == "supergroup":
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
            if user_s.status in ("creator", "administrator"):
                a_chat += 1
        elif dialog.chat.type == "channel":
            c += 1

    end = datetime.now()
    ms = (end - start).seconds
    await message.edit_text(
        """**ʏᴏᴜʀ ꜱᴛᴀᴛꜱ ꜰᴇᴀᴛᴄʜᴇᴅ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ 🚩**

🚩**ʏᴏᴜ ʜᴀᴠᴇ {} ᴘʀɪᴠᴀᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ.**
🚩**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ɢʀᴏᴜᴘꜱ.**
🚩**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ꜱᴜᴘᴇʀ ɢʀᴏᴜᴘꜱ.**
🚩**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ᴄʜᴀɴɴᴇʟꜱ.**
**ʏᴏᴜ ᴀʀᴇ ᴀᴅᴍɪɴꜱ ɪɴ {} ᴄʜᴀᴛꜱ.**
🚩**ʙᴏᴛꜱ ɪɴ ʏᴏᴜʀ ᴘʀɪᴠᴀᴛᴇ = {}**

🚩**ꜰᴇᴀᴛᴄʜᴇᴅ ʙʏ ᴜꜱɪɴɢ Meow userbotot**""".format(
            ms, u, g, sg, c, a_chat, b
        )
    )




