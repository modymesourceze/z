import pyrogram
import asyncio
from pyrogram import Client, idle
from pyrogram import filters, Client
from random import randint
from config import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import Chat, User
from asyncio import sleep
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
import re
from pyrogram.types import Message
import random
import time
from asyncio import gather
import os, time
from telegraph import upload_file
from os import remove
import time
from PIL import Image
from io import BytesIO
import wget
from asyncio import sleep
from pyrogram import Client, filters
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio, MediumQualityVideo
from pytgcalls.types.stream import StreamAudioEnded
from pytgcalls.types.input_stream.quality import (HighQualityAudio,
                                                  HighQualityVideo,
                                                  LowQualityAudio,
                                                  LowQualityVideo,
                                                  MediumQualityAudio,
                                                  MediumQualityVideo)
                                                  

@Client.on_message(filters.command("مين في الكول", prefixes=f".") & filters.me, group=57658)
async def ghsdh_user(client, message):
    await message.edit("استنا اطلع اشوف مين في الكول✨♥") 
    try:
     await hoss.join_group_call(message.chat.id, AudioPiped("./FR3ON.mp3"), stream_type=StreamType().pulse_stream)
     text="😎🥰 الاشخاص المتواجدين في الكول:\n\n"
     participants = await hoss.get_participants(message.chat.id)
     k =0
     for participant in participants:
      info = participant
      if info.muted == False:
       mut="يتحدث 🗣"
      else:
       mut="ساكت 🔕"
      user = await client.get_users(participant.user_id)
      k +=1
      text +=f"{k}➤{user.mention}➤{mut}\n"
      text += f"\nعددهم : {len(participants)}\n✔️"    
      await asyncio.sleep(2.5)
      await message.edit(f"{text}")
      await hoss.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
     await message.reply(f"حبيبي الكول مش مفتوح اصلااا\n😜")
    except TelegramServerError:
     await message.reply(f"ارسل الامر تاني في مشكله في سيرفر التلجرام\n😜")
    except AlreadyJoinedError:
     text="😎🥰 الاشخاص المتواجدين في الكول:\n\n"
     participants = await hoss.get_participants(message.chat.id)
     k =0
     for participant in participants:
      info = participant
      if info.muted == False:
       mut="يتحدث 🗣"
      else:
       mut="ساكت 🔕"
      user = await client.get_users(participant.user_id)
      k +=1
      text +=f"{k}➤{user.mention}➤{mut}\n"
      text += f"\nعددهم : {len(participants)}\n✔️"    
      await asyncio.sleep(2.5)
      await message.edit(f"{text}")