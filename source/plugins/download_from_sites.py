from pyrogram import Client, filters,enums
from config import *
from get_media import download as dw
from pySmartDL import SmartDL
import asyncio ,os

def download_file(url,local_filename):
    dest = f"./{local_filename}.mp4" 
    obj = SmartDL(url, dest)
    obj.start()
    return str(local_filename) + '.mp4'

@Client.on_message(filters.me & filters.regex('^.تحميل (.*?)') )
async def download_link(c,msg) :
    link = msg.text.split(' ')[1]
    message = await msg.edit('• جاري جلب البيانات ...')
    title , url = dw(link)
    await message.edit('• جاري التحميل ..')
    vid = download_file(url,msg.from_user.id)
    await message.edit('• جاري الرفع ...')
    await c.send_video(msg.chat.id,vid,caption=f'• [{title}]({url})')
    await message.delete()
    os.remove(vid)
    
    
    
    