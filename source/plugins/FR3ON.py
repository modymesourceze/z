import asyncio
import re
from pyrogram import Client, filters
from datetime import datetime
from pyrogram import enums
from collections import defaultdict
from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from asyncio import gather
from pyrogram.errors import FloodWait
from pyrogram.enums import ChatMembersFilter

def get_name(msg):
    if msg.from_user.last_name:
        last_name = msg.from_user.last_name
    else:
        last_name = ""
    if msg.from_user.first_name:
        first_name = msg.from_user.first_name
    else:
        first_name = ""
    return f"[{first_name} {last_name}](tg://user?id={msg.from_user.id})"


async def is_Admin(chat, id):
    admins = []
    async for m in app.get_chat_members(chat, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        admins.append(m.user.id)
    if id in admins:
        return True
    else:
        return False

mention_locked = []

@Client.on_message(filters.command("قفل المنشن", prefixes=".") & filters.me)
async def lllojgjj(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    if message.chat.id in mention_locked:
        return await message.reply_text("المنشن مقفول بالفعل ✨♥")
    mention_locked.append(message.chat.id)
    return await message.reply_text(" تم قفل المنشن بنجاح ✨♥")

@Client.on_message(filters.command("فتح المنشن", prefixes=".") & filters.me)
async def idljjopss(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    if not message.chat.id in mention_locked:
        return await message.reply_text("المنشن مفتوح بالفعل ✨♥")
    mention_locked.remove(message.chat.id)
    return await message.reply_text(" تم فتح المنشن بنجاح ✨♥")

@Client.on_message(filters.text & filters.group & filters.create(lambda _, __, message: message.chat.id in mention_locked))
async def delete_mention(client, message):
    if "@" in message.text:
        await message.delete()
        await message.reply(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل المنشن هنا .")

video_locked = []

@Client.on_message(filters.command("قفل الفديو", prefixes=".") & filters.me)
async def lllocjbvbj(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    if message.chat.id in video_locked:
        return await message.reply_text("الفديو مقفول بالفعل ✨♥")
    video_locked.append(message.chat.id)
    return await message.reply_text(" تم قفل الفديو بنجاح ✨♥")

@Client.on_message(filters.command("فتح الفديو", prefixes=".") & filters.me)
async def idljjopsgcbs(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    if not message.chat.id in video_locked:
        return await message.reply_text("الفديو مفتوح بالفعل ✨♥")
    video_locked.remove(message.chat.id)
    return await message.reply_text(" تم فتح الفديو بنجاح ✨♥")

@Client.on_message(filters.video & filters.group & filters.create(lambda _, __, message: message.chat.id in video_locked))
async def deletntiohfhn(client, message):
    await message.delete()
    await message.reply(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال الفديو هنا .")

photo_locked = []

@Client.on_message(filters.command("قفل الصور", prefixes=".") & filters.me)
async def lllsdkocjj(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    if message.chat.id in photo_locked:
        return await message.reply_text("الصور مقفول بالفعل ✨♥")
    photo_locked.append(message.chat.id)
    return await message.reply_text(" تم قفل الصور بنجاح ✨♥")

@Client.on_message(filters.command("فتح الصور", prefixes=".") & filters.me)
async def idljjoshkkpss(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    if not message.chat.id in photo_locked:
        return await message.reply_text("الصور مفتوح بالفعل ✨♥")
    photo_locked.remove(message.chat.id)
    return await message.reply_text(" تم فتح الصور بنجاح ✨♥")

@Client.on_message(filters.photo & filters.group & filters.create(lambda _, __, message: message.chat.id in photo_locked))
async def delete_fgmetion(client, message):
    await message.delete()
    await message.reply(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال الصور هنا .")

forward_locked = []

@Client.on_message(filters.command("قفل التوجيه", prefixes=".") & filters.me)
async def lllocjjvfsb(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    if message.chat.id in forward_locked:
        return await message.reply_text("التوجيه مقفول بالفعل ✨♥")
    forward_locked.append(message.chat.id)
    return await message.reply_text(" تم قفل التوجيه بنجاح ✨♥")
 
@Client.on_message(filters.command("فتح التوجيه", prefixes=".") & filters.me)
async def idljjoagkmpss(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    if not message.chat.id in forward_locked:
        return await message.reply_text("التوجيه مفتوح بالفعل ✨♥")
    forward_locked.remove(message.chat.id)
    return await message.reply_text(" تم فتح التوجيه بنجاح ✨♥")

@Client.on_message(filters.forwarded & filters.group & filters.create(lambda _, __, message: message.chat.id in forward_locked))
async def mentiojvn(client, message):
    await message.delete()
    await message.reply(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال التوجيه هنا .")

sticker_locked = []
    
@Client.on_message(filters.command("قفل الملصقات", prefixes=".") & filters.me)
async def lllqwfscocjj(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    if message.chat.id in sticker_locked:
        return await message.reply_text("الملصقات مقفول بالفعل ✨♥")
    sticker_locked.append(message.chat.id)
    return await message.reply_text(" تم قفل الملصقات بنجاح ✨♥")
 
@Client.on_message(filters.command("فتح الملصقات", prefixes=".") & filters.me)
async def idljjopscnss(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    if not message.chat.id in sticker_locked:
        return await message.reply_text("الملصقات مفتوح بالفعل ✨♥")
    sticker_locked.remove(message.chat.id)
    return await message.reply_text(" تم فتح الملصقات بنجاح ✨♥")

@Client.on_message(filters.sticker & filters.group & filters.create(lambda _, __, message: message.chat.id in sticker_locked))
async def ete_mention(client, message):
    await message.delete()
    await message.reply(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال الملصقات هنا .")  

link_locked = []

@Client.on_message(filters.command("قفل الروابط", prefixes=".") & filters.me)
async def lllwweshocjj(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    if message.chat.id in link_locked:
        return await message.reply_text("الروابط مقفول بالفعل ✨♥")
    link_locked.append(message.chat.id)
    return await message.reply_text(" تم قفل الروابط بنجاح ✨♥")
 
@Client.on_message(filters.command("فتح الروابط", prefixes=".") & filters.me)
async def idljjoyyysjpss(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    if not message.chat.id in link_locked:
        return await message.reply_text("الروابط مفتوح بالفعل ✨♥")
    link_locked.remove(message.chat.id)
    return await message.reply_text(" تم فتح الروابط بنجاح ✨♥")

@Client.on_message(filters.text & filters.group & filters.create(lambda _, __, message: message.chat.id in link_locked))
async def deleteention(client, message):
   if "https:" in message.text:       
       await message.delete()
       await message.reply_text(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال الروابط هنا .")

saap_locked = []
     
@Client.on_message(filters.command("قفل السب", prefixes=".") & filters.me)
async def lllovvmcjj(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    if message.chat.id in saap_locked:
        return await message.reply_text("السب مقفول بالفعل ✨♥")
    saap_locked.append(message.chat.id)
    return await message.reply_text(" تم قفل السب بنجاح ✨♥")
 
@Client.on_message(filters.command("فتح السب", prefixes=".") & filters.me)
async def idljjojmcbpss(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    if not message.chat.id in saap_locked:
        return await message.reply_text("السب مفتوح بالفعل ✨♥")
    saap_locked.remove(message.chat.id)
    return await message.reply_text(" تم فتح السب بنجاح ✨♥")

@Client.on_message(filters.text & filters.group & filters.create(lambda _, __, message: message.chat.id in saap_locked))
async def deleteon(client, message):
   if "احا" in message.text:
       await message.delete()
       await message.reply_text(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال السب هنا .")
   elif "خخخ" in message.text:
       await message.delete()
       await message.reply_text(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال السب هنا .")
   elif "كسك" in message.text:
       await message.delete()
       await message.reply_text(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال السب هنا .")
   elif "كسمك" in message.text:
       await message.delete()
       await message.reply_text(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال السب هنا .")
   elif "عرص" in message.text:
       await message.delete()
       await message.reply_text(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال السب هنا .")
   elif "خول" in message.text:
       await message.delete()
       await message.reply_text(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال السب هنا .")
   elif "يبن" in message.text:
       await message.delete()
       await message.reply_text(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال السب هنا .")
   elif "كلب" in message.text:
       await message.delete()
       await message.reply_text(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال السب هنا .")
   elif "علق" in message.text:
       await message.delete()
       await message.reply_text(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال السب هنا .")
   elif "كسم" in message.text:
       await message.delete()
       await message.reply_text(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال السب هنا .")
   elif "انيك" in message.text:
       await message.delete()
       await message.reply_text(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال السب هنا .")
   elif "انيكك" in message.text:
       await message.delete()
       await message.reply_text(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال السب هنا .")
   elif "اركبك" in message.text:
       await message.delete()
       await message.reply_text(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال السب هنا .")
   elif "زبي" in message.text:
       await message.delete()
       await message.reply_text(f"☭ عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n ☭ تم قفل ارسال السب هنا .")

array = []

@Client.on_message(filters.command("تاك", prefixes=".") & filters.me)
async def llluiomcjj(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return
    await message.reply_text("☭ جاري بدأ المنشن ، لايقاف الامر اكتب  .ايقاف التاك")
    i = 0
    txt = ""
    zz = message.text
    if message.photo:
        photo_id = message.photo.file_id
        photo = await client.download_media(photo_id)
        zz = message.caption
    try:
        zz = zz.replace("@all","").replace(".تاك","").replace("all","")
    except:
        pass
    array.append(message.chat.id)
    
    async for x in client.get_chat_members(message.chat.id):
        if message.chat.id not in array:
            return
        if not x.user.is_deleted:
            i += 1
            txt += f" {x.user.mention} ›"
            if i == 20:
                try:
                    if not message.photo:
                        await client.send_message(message.chat.id, f"{zz}\n{txt}")
                    else:
                        await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
                    i = 0
                    txt = ""
                    await asyncio.sleep(2)
                except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
                except Exception:
                    array.remove(message.chat.id)
                    
    array.remove(message.chat.id)
  
@Client.on_message(filters.command("ايقاف التاك", prefixes=".") & filters.me)
async def llghhmcjj(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return
    if message.chat.id not in array:
        await message.reply("☭ التاك متوقف بالفعل  ")
        return 
    if message.chat.id in array:
        array.remove(message.chat.id)
        await message.reply("☭ تم ايقاف التاك عزيزي  ")
        return
        
@Client.on_message(filters.command("طرد البوتات$", prefixes=f".") & filters.me)
async def ban_bots(client: Client, message: Message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    count = 0
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.BOTS):
        if member.user.is_bot:
            try:
                await client.ban_chat_member(message.chat.id, member.user.id)
                count += 1
            except Exception as e:
                print(f"Error banning bot: {e}")
    
    if count > 0:
        await message.reply_text(f"تم طرد {count} بوت بنجاح✅♥")
    else:
        await message.reply_text("لا توجد بوتات لطردها.")

@Client.on_message(filters.command("البوتات$", prefixes=f".") & filters.me)
async def list_bots(client: Client, message: Message):
    bot_usernames = []
    count = 0 
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.BOTS):
        if member.user.is_bot:
            bot_usernames.append("@" + member.user.username)
            count += 1

    if count > 0:
        bot_list = "\n".join(bot_usernames)
        await message.reply_text(f"عدد البوتات في المجموعة: {count} \n يوزرات البوتات: {bot_list}")
    else:
        await message.reply_text("لا يوجد بوتات في المجموعة.")

@Client.on_message(filters.command("الغاء تثبيت$", prefixes=f".") & filters.me)
async def unpin_message(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    chat_id = message.chat.id
    reply_msg_id = message.reply_to_message_id  
    try:
        await client.unpin_chat_message(chat_id, message_id=reply_msg_id) 
        await message.reply_text("تم إلغاء تثبيت الرسالة بنجاح✅♥")
    except Exception as e:
        print(e)
        await message.reply_text("حدث خطأ أثناء إلغاء تثبيت الرسالة")

@Client.on_message(filters.command("تثبيت$", prefixes=f".") & filters.me)
async def pin_message(client, message):
    chek = await is_Admin(message.chat.id, message.from_user.id)
    if chek == False:
        await message.reply("☭ يجب أن تكون مشرفًا بالمجموعة لاستخدام الأوامر")
        return False
    chat_id = message.chat.id
    reply_msg_id = message.reply_to_message_id
    try:
        await client.pin_chat_message(chat_id, reply_msg_id)
        await message.reply_text("تم تثبيت الرسالة بنجاح✅♥")
    except Exception as e:
        print(e)
        await message.reply_text("حدث خطأ أثناء تثبيت الرسالة.")