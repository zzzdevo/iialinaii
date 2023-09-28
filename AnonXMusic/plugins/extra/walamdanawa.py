import asyncio


import random
from AnonXMusic import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
from config import OWNER_ID

dev = OWNER_ID


txt = [
            "<b>هەردەم پێبکەنە ♥️😻</b>",


             "😂😂😂😂😂😂😂",
            

    
            
            
            "<b>پیبکانا پیبکانە هەر دەم بە زەردەخەنە 😂😂</b>",
            
            
 
            
            

        ]
txt1 = [

            "<b>بمێنی گەشەپێدەر♥️😻</b>",


             "<b>هەموو کات زەردەخەنە😂😂</b>",
            

            "<b>احح لەو پیکنینە 😂😂</b>",
            
            
          
            
 
            
            

        ]

        
        


@app.on_message(command(["ههه","😂😂","😂😂😂","😂🤣","ههههههههههههههههههه","😂😂😂😂😂😂"]))


async def cutt(client: Client, message: Message):

     dev = OWNER_ID
     if message.from_user.id in dev:


         b = random.choice(txt1)


         await message.reply(

         f"{b}")
     else:
         a = random.choice(txt)


         await message.reply(


         f"{a}")
       
