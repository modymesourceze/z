import pyrogram, sys
from pyrogram import Client, filters, enums
from config import *
import asyncio
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton)

pyro = pyrogram.__version__
py = sys.version

@app.on_message(filters.command(["سورس","السورس"], prefixes=f"."))
async def ping(app, msg):
  await msg.delete()
  txt = f"""
• 𝗛𝗲𝗹𝗹𝗼 𝗗𝗲𝗮𝗿 : {msg.from_user.mention}
— — — — — — — — —
• 𝗗𝗲𝘃 𝗦𝗼𝘂𝗿𝗰𝗲 : @SPORT_HORSE
• 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗦𝗼𝘂𝗿𝗰𝗲 : @H_0RSE
• [𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺 {pyro}](https://docs.pyrogram.org/)
• 𝗣𝘆𝘁𝗵𝗼𝗻 {py}
  """
  await app.send_video(msg.chat.id,
  video="https://envs.sh/G8h.mp4",
  caption=txt, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐎𝐑𝐒𝐄", url=f"https://t.me/H_0RSE")]]))