from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import *
import asyncio

@app.on_message(filters.command("^ايموجي$", prefixes=f".") & filters.me & filters.reply)
async def Prememoji(user, msg):
	if msg.reply_to_message.photo:
		format = "png"
	else:
		return await msg.edit("• ادعم الصور فقط")
	await msg.edit("• انتظر جار التحميل ..")
	await msg.reply_to_message.download(f"./emoji.{format}")
	await user.send_message("Stickers", "/start")
	result = await user.get_inline_bot_results(bot_user, query="Prememoji")
	await msg.delete()
	await user.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)