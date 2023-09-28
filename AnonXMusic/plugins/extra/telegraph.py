from pyrogram import Client, filters, enums
from pyrogram.types import Message
from telegraph import upload_file
import os
from strings.filters import command
from AnonXMusic import app

@app.on_message(command(["تێلەگراف","telegraph"]))
async def get_link_group(client, message):
    try:
        text = await message.reply("<b>•⎆┊دروست دەکرێت ..</b>")
        async def progress(current, total):
            await text.edit_text(f"<b>•⎆┊میدیا دروست کرا🕷  ...</b> {current * 100 / total:.1f}%",parse_mode=enums.ParseMode.MARKDOWN)
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("<b>•⎆┊بەستەری میدیا لە هێناندایە ..🕷️•</b>")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"<b>•⎆┊  𝒕𝒆𝒍𝒆 𝒍𝒊𝒏𝒌 :</b>\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"<b>•⎆┊فایلەکە شکستی هێنا♥•\n\nهۆکار: {e} </b>")
            os.remove(local_path) 
            return         
    except Exception:
        pass
