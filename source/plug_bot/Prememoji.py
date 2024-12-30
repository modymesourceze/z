from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
from PIL import Image
import asyncio, re, os, random

@bot.on_inline_query(filters.regex("^Prememoji$"))
async def Prememoj(client, inline_query):
	reply_markup = InlineKeyboardMarkup([
		[InlineKeyboardButton("• رمز تعبيري ثابت •", callback_data="RmzNo")]
	])
	await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="نوع الايموجي",
                input_message_content=InputTextMessageContent(
                    "↯︙قم ب اختيار نوع الايموجي"
                ),
                url="https://t.me/f_r_3_a_o_n",
                description="FR3ON",
                reply_markup=reply_markup
            ),
        ],
        cache_time=1
    )

@bot.on_callback_query(filters.regex("^RmzNo$") & filters.user(sudo_id))
async def RmzNo(client, callback_query):
	await app.send_message("Stickers", "/cancel")
	await asyncio.sleep(0.2)
	LastMsg = await app.send_message("Stickers", "/addemoji")
	await asyncio.sleep(0.2)
	LastMsgId = LastMsg.id + 1
	msg = await app.get_messages("Stickers", LastMsgId)
	if re.findall(r"(.*?)newemojipack(.*?)", msg.text):
		await callback_query.edit_message_text("• يتم انشاء حزمه ..")
		await app.send_message("Stickers", "/newemojipack")
		await asyncio.sleep(0.3)
		await app.send_message("Stickers", "Static emoji")
		await asyncio.sleep(0.3)
		await app.send_message("Stickers", app.me.first_name)
		await callback_query.edit_message_text("• يتم تعديل حجم الصوره ..")
		image = Image.open("./emoji.png")
		new_size = (100, 100)
		resized_image = image.resize(new_size)
		resized_image.save("./resized.png")
		os.remove("./emoji.png")
		await app.send_document("Stickers", "./resized.png")
		os.remove("./resized.png")
		emojis_list = ['😂', '❤️', '😘', '😍', '😊', '😁', '👍', '☺️', '😔', '😄', '😭', '💋', '😒', '😳', '😜', '🙈', '😉', '😢', '😃', '😝', '😱', '😡', '😏', '😞', '😅', '😚', '🙊', '😌', '😀', '😋', '😆', '👌']
		random_emoji = random.choice(emojis_list)
		await callback_query.edit_message_text("• يتم انهاء الحزمه ..")
		await asyncio.sleep(0.2)
		await app.send_message("Stickers", random_emoji)
		await asyncio.sleep(0.3)
		await app.send_message("Stickers", "/publish")
		await asyncio.sleep(0.3)
		await app.send_message("Stickers", "/skip")
		await asyncio.sleep(0.3)
		EmojiName = app.me.username + str(random.randint(1, 1000))
		await app.send_message("Stickers", f"{EmojiName}Emoji")
		await asyncio.sleep(0.3)
		await callback_query.edit_message_text(f"• تم انشاء الحزمه بنجاح ..\n~ https://t.me/addemoji/{EmojiName}Emoji")
	elif msg.text == "Choose an emoji set.":
		reply_markup = msg.reply_markup.keyboard
		keyboard = []
		for keyboardnn in reply_markup:
			for key in keyboardnn:
				keyboard.append(InlineKeyboardButton(key[:-6], callback_data=f"Pack:{key}"))
		key = [keyboard[i:i+2] for i in range(0, len(keyboard), 2)]
		await callback_query.edit_message_text("• اختار الحزمه التي تريد اضافه الايموجي لها ..", reply_markup=InlineKeyboardMarkup(key))

@bot.on_callback_query(filters.regex("^Pack:"))
async def PackEmoji(client, callback_query):
	EmojiName = callback_query.data.split(":")[1]
	await callback_query.edit_message_text("• يتم اضافه الاستيكر ..")
	await app.send_message("Stickers", EmojiName)
	await asyncio.sleep(0.3)
	await callback_query.edit_message_text("• يتم تعديل حجم الصوره ..")
	image = Image.open("./emoji.png")
	new_size = (100, 100)
	resized_image = image.resize(new_size)
	resized_image.save("./resized.png")
	os.remove("./emoji.png")
	await app.send_document("Stickers", "./resized.png")
	os.remove("./resized.png")
	emojis_list = ['😂', '❤️', '😘', '😍', '😊', '😁', '👍', '☺️', '😔', '😄', '😭', '💋', '😒', '😳', '😜', '🙈', '😉', '😢', '😃', '😝', '😱', '😡', '😏', '😞', '😅', '😚', '🙊', '😌', '😀', '😋', '😆', '👌']
	random_emoji = random.choice(emojis_list)
	await callback_query.edit_message_text("• يتم انهاء الاضافه ..")
	await asyncio.sleep(0.2)
	await app.send_message("Stickers", random_emoji)
	await asyncio.sleep(0.3)
	await app.send_message("Stickers", "/done")
	await callback_query.edit_message_text("• تم اضافه الايموجي بنجاح ..")