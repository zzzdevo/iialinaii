from strings.filters import command
from AnonXMusic import app
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from pyrogram.enums import ParseMode, ChatMemberStatus

stiklok = []


@app.on_message(
    command(["داخستنی ستیکەر"])
    & filters.group

)
async def block_stickers(client: Client, message: Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in stiklok:
            return await message.reply_text(f"•⎆┊**{message.from_user.mention} ستیکەر پێشتر داخستراوە♥•**",parse_mode=enums.ParseMode.MARKDOWN)
        stiklok.append(message.chat.id)
        return await message.reply_text(f"•⎆┊**ستیکەر داخسترا\n\n پێشتر ←{message.from_user.mention}♥•**",parse_mode=enums.ParseMode.MARKDOWN)
    else:
        return await message.reply_text(f"•⎆┊**{message.from_user.mention}ببورە تۆ ئەدمین نیت🗿•**",parse_mode=enums.ParseMode.MARKDOWN)


@app.on_message(
    command(["کردنەوەی ستیکەر"])
    & filters.group

)
async def unblock_stickers(client: Client, message: Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in stiklok:
            return await message.reply_text(f"•⎆┊**{message.from_user.mention} ستیکەر پێشتر کراوەتەوە♥•**",parse_mode=enums.ParseMode.MARKDOWN)
        stiklok.remove(message.chat.id)
        return await message.reply_text(f"•⎆┊**ستیکەر کراوەتەوە\n\n پێشتر ←{message.from_user.mention}♥•**",parse_mode=enums.ParseMode.MARKDOWN)
    else:
        return await message.reply_text(f"•⎆┊**{message.from_user.mention}ببورە تۆ ئەدمین نیت🗿•**",parse_mode=enums.ParseMode.MARKDOWN)
