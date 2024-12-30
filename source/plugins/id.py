from pyrogram import Client, filters,enums
from config import *
import asyncio


def get_name(msg):
  if msg.from_user.last_name :
    last_name = msg.from_user.last_name
  else:
    last_name = ""
  if msg.from_user.first_name :
    first_name = msg.from_user.first_name
  else:
    first_name = ""
  return f"[{first_name} {last_name}](tg://user?id={msg.from_user.id})"

@Client.on_message(filters.command(["ايدي$","ا$","id$"], prefixes=f".") & filters.me )
async def get_info(c,msg):
  if msg.reply_to_message :
    if msg.reply_to_message.sender_chat :
      return await msg.edit("☭ دي قناه ي ليفه")
    if msg.reply_to_message.from_user.username :
      username = f"@{msg.reply_to_message.from_user.username}"
    else :
      username = "لا يوجد"
    get_bio = await c.get_chat(msg.reply_to_message.from_user.id)
    if get_bio.bio :
      bio = f"{get_bio.bio}"
    else :
      bio = "لا يوجد"
    txx = f"[ٍ𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐎𝐑𝐒𝐄](t.me/H_0RSE)\n☭ ɴᴀᴍᴇ ➼ {get_name(msg.reply_to_message)}\n☭ ᴜsᴇʀ ➼ {username} \n☭ ɪᴅ ➼ `{msg.reply_to_message.from_user.id}` \n☭ ʙɪᴏ ➼ {bio}\n[❪ 𝑴𝒀 𝑪𝑯𝑨𝑵𝑵𝑬𝑳 ❫](t.me/H_0RSE) ⋮ [❪ 𝑴𝒀 𝑫𝑬𝑽 ❫](t.me/SPORT_HORSE)"
    if msg.reply_to_message.from_user.photo :
      await msg.delete(revoke=True)
      async for photo in c.get_chat_photos(msg.reply_to_message.from_user.id):
        await msg.reply_photo(photo.file_id,caption=txx)
        break 
    else :
      await msg.edit(txx)
  else :
    get_bio = await c.get_chat("me")
    if get_bio.bio :
      bio = f"{get_bio.bio}"
    else :
      bio = "لا يوجد"
    if get_bio.username :
      username = f"@{get_bio.username}"
    else :
      username = "لا يوجد"
    txx = f"[َ𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐎𝐑𝐒𝐄](t.me/H_0RSE)\n☭ ɴᴀᴍᴇ ➼ {get_name(msg)}\n☭ ᴜsᴇʀ ➼ {username} \n☭ ɪᴅ ➼ `{msg.from_user.id}` \n☭ ʙɪᴏ ➼ {bio}\n[❪ 𝑴𝒀 𝑪𝑯𝑨𝑵𝑵𝑬𝑳 ❫](t.me/H_0RSE) ⋮ [❪ 𝑴𝒀 𝑫𝑬𝑽 ❫](t.me/SPORT_HORSE)"
    if msg.from_user.photo :
      await msg.delete(revoke=True)
      async for photo in c.get_chat_photos(msg.from_user.id):
        await msg.reply_photo(photo.file_id,caption=txx)
        break 
    else :
      await msg.edit(txx)