import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message
from AnonXMusic import app

@app.on_message(command(["بەستەر","/link","لینک","لینك"]) & ~filters.bot & ~filters.private)
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("<b>سەرەتا بمکە ئەدمین</b>",parse_mode=enums.ParseMode.MARKDOWN)
    await message.reply_text(f"<b>بە سەرکەوتوویی بەستەری گرووپ دروست کرا :</b>\n\n <code>{invitelink}</code>")
    
