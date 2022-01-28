import os
from pyrogram import Client, filters
from pyrogram.types import Message, User



@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Bienvenido {message.from_user.mention} a {message.chat.username} ,  Esperamos te sea util este espacio",chat_id=chatid)
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Nos vemos ,  {message.from_user.mention} , Que tengas un buen dia",chat_id=chatid)
	

