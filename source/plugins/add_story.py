from pyrogram import Client, filters,enums
from config import *
import os

@Client.on_message(filters.command(["رفع استوري$","رفع ستوري$"], prefixes=f".") & filters.me)
async def add_storyy(c, msg):
    if not msg.reply_to_message:
        await msg.edit("• قم بي الرد علي الصورة او الفيديو اولا")
        return
    message = msg.reply_to_message
    if message.photo :
        await msg.edit('• جاري الرفع ..')
        ph = await message.download()
        await c.send_story(photo=ph)
        await msg.edit('• تم رفع الصوره بنجاح الي قصتك')
        os.remove(ph)
    elif message.video :
        await msg.edit('• جاري الرفع ..')
        ph = await message.download()
        await c.send_story(video=ph)
        await msg.edit('• تم رفع الفيديو بنجاح الي قصتك')
        os.remove(ph)
    
    else : 
        await msg.edit('• يمكنك رفع الصور و الفيديو فقط !')


@Client.on_message(filters.regex("^.رفع استوري (.*?)") & filters.me)
async def add_storyy_with_caption(c, msg):
    if not msg.reply_to_message:
        await msg.edit("• قم بي الرد علي الصورة او الفيديو اولا")
        return
    text = msg.text.replace('.رفع استوري ','').replace('.رفع ستوري ','')
    message = msg.reply_to_message
    if message.photo :
        await msg.edit('• جاري الرفع ..')
        ph = await message.download()
        await c.send_story(photo=ph,caption=text)
        await msg.edit('• تم رفع الصوره بنجاح الي قصتك')
        os.remove(ph)
    elif message.video :
        await msg.edit('• جاري الرفع ..')
        ph = await message.download()
        await c.send_story(video=ph,caption=text)
        await msg.edit('• تم رفع الفيديو بنجاح الي قصتك')
        os.remove(ph)
    
    else : 
        await msg.edit('• يمكنك رفع الصور و الفيديو فقط !')

@Client.on_message(filters.regex("^.رفع ستوري (.*?)") & filters.me)
async def add_storyy_with_other_caption(c, msg):
    if not msg.reply_to_message:
        await msg.edit("• قم بي الرد علي الصورة او الفيديو اولا")
        return
    text = msg.text.replace('.رفع استوري ','').replace('.رفع ستوري ','')
    message = msg.reply_to_message
    if message.photo :
        await msg.edit('• جاري الرفع ..')
        ph = await message.download()
        await c.send_story(photo=ph,caption=text)
        await msg.edit('• تم رفع الصوره بنجاح الي قصتك')
        os.remove(ph)
    elif message.video :
        await msg.edit('• جاري الرفع ..')
        ph = await message.download()
        await c.send_story(video=ph,caption=text)
        await msg.edit('• تم رفع الفيديو بنجاح الي قصتك')
        os.remove(ph)
    
    else : 
        await msg.edit('• يمكنك رفع الصور و الفيديو فقط !')
        