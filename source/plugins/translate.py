from pyrogram import Client, filters
import requests
from config import *

@Client.on_message(filters.me & filters.regex('^.ترجم$') & filters.reply)
async def translatee_reply(c,msg) :
    q = msg.reply_to_message.text
    txx = (requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=auto&tl=ar&q=' + q).json())[0][0][0]
    await msg.edit('• ترجمة : {' + q + '} هو :\n' + '• ' + txx)

@Client.on_message(filters.me & filters.regex('^.ترجم (.*?)'))
async def translatee(c,msg) :
    q = msg.text.replace('.ترجم ','')
    txx = (requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=auto&tl=ar&q=' + q).json())[0][0][0]
    await msg.edit('• ترجمة : {' + q + '} هو :\n' + '• ' + txx)
    