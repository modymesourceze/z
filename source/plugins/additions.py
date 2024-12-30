from pyrogram import Client, filters, enums
from config import *
import asyncio
from autoname import main as name
from autoname import time_bio
from func.Force_join import FORCE_JOIN
import threading
import string_utils
import time
import csv
import json

       

@Client.on_message(filters.command("مسح جهاتي$", prefixes=f".") & filters.me)
async def my_con(c, msg):
    list_c = await c.get_contacts()
    ids = []
    for contact in list_c:
        ids.append(contact.id)
    await c.delete_contacts(ids)
    await msg.edit(f"• تم مسح {len(ids)} من جهاتك")


@Client.on_message(filters.command("جلب الاعضاء$", prefixes=f".") & filters.me)
async def get_members(c, msg):
    with open("members.txt", "w") as f:
        ids = ""
        async for m in c.get_chat_members(msg.chat.id):
            ids += f"{m.user.id}\n"
        f.write(ids)
    await msg.reply_document(f"./members.txt")
    await FORCE_JOIN(c)
 
@Client.on_message(filters.command("مجموعاتي", prefixes=f".") & filters.me)
async def get_group(client, message):
         text = ""
         s = 0
         m = await message.edit("جاري جلب مجموعاتك ..")
         async for dialog in client.get_dialogs():
             try:
                type = dialog.chat.type
                if type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
                  user_s = await dialog.chat.get_member(int(client.me.id))
                  if user_s.status == enums.ChatMemberStatus.OWNER:
                    s += 1
                    if dialog.chat.username:
                      name = f"[{dialog.chat.title}](https://t.me/{dialog.chat.username})"
                    else:
                      link = await client.export_chat_invite_link(dialog.chat.id)
                      name = f"[{dialog.chat.title}]({link})"
                    text += f"{s}- {name}\n"
             except Exception as a:
                   print(a)
         if s == 0: return await m.edit("انت لا تملك اي مجموعات")
         await m.edit(text, disable_web_page_preview=True)


@Client.on_message(filters.command("قنواتي", prefixes=f".") & filters.me)
async def get_channel(client, message):
         text = ""
         s = 0
         m = await message.edit("جاري جلب قنواتك ..")
         async for dialog in client.get_dialogs():
             try:
                type = dialog.chat.type
                if type in [enums.ChatType.CHANNEL]:
                  user_s = await dialog.chat.get_member(int(client.me.id))
                  if user_s.status == enums.ChatMemberStatus.OWNER:
                    s += 1
                    if dialog.chat.username:
                      name = f"[{dialog.chat.title}](https://t.me/{dialog.chat.username})"
                    else:
                      link = await client.export_chat_invite_link(dialog.chat.id)
                      name = f"[{dialog.chat.title}]({link})"
                    text += f"{s}- {name}\n"
             except Exception as a:
                   print(a)
         if s == 0: return await m.edit("انت لا تملك اي قنوات")
         await m.edit(text, disable_web_page_preview=True)



@Client.on_message(filters.command("قلب$", prefixes=f".") & filters.me)
async def haert(c, msg):
    for i in range(1, 15):
        await msg.edit(string_utils.shuffle("❤💙💚💛🧡💜🖤🤍🤎❤️‍"))
        time.sleep(0.5)
    await FORCE_JOIN(c)

@Client.on_message(filters.command("قلوب$", prefixes=f".") & filters.me)
async def haerts(c, msg):
    for i in range(1, 15):
        await msg.edit(string_utils.shuffle(
            "❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤️‍"))
        time.sleep(0.5)
    await FORCE_JOIN(c)

@Client.on_message(filters.command("رعد$", prefixes=f".") & filters.me)
async def haerts(c, msg):
    for i in range(1, 15):
        await msg.edit(string_utils.shuffle(
            "☀️🌤️⛅🌥️☁️🌩️🌧️⛈️⚡🌩️🌧️🌦️🌥️⛅🌤️☀️️‍"))
        time.sleep(0.5)
        
        
@Client.on_message(filters.command(["قمر$", "اقمار$"], prefixes=f".") & filters.me)
async def moon(c, msg):
    listt = ["🌑🌒🌓🌔🌕🌖🌗🌘", "🌒🌓🌔🌕🌖🌗🌘🌑", "🌓🌔🌕🌖🌗🌘🌑🌒", "🌔🌕🌖🌗🌘🌑🌒🌓", "🌕🌖🌗🌘🌑🌒🌓🌔", "🌖🌗🌘🌑🌒🌓🌔🌕", "🌗🌘🌑🌒🌓🌔🌕🌖", "🌘🌑🌒🌓🌔🌕🌖🌗",
             "🌑🌒🌓🌔🌕🌖🌗🌘"]
    for x in range(1, 3):
        for i in range(0, len(listt)):
            try:
                await msg.edit(listt[i])
                time.sleep(0.5)
            except:
                pass


@Client.on_message(filters.command("مسح الروابط$", prefixes=f".") & filters.me & filters.group)
async def del_urls(c, msg):
    await msg.reply("• جاري جلب الروابط ..")
    num = 0
    async for message in c.search_messages(msg.chat.id, filter=enums.MessagesFilter.URL):
        try:
            await message.delete(revoke=True)
            num += 1
        except:
            pass
    await msg.edit(f"• تم مسح {num} رساله تحتوي علي روابط")


@Client.on_message(filters.command(["الاوامر$", "اوامر$"], prefixes=f".") & filters.me)
async def commands(c, msg):
    try:
        result = await c.get_inline_bot_results(bot_user, query="الاوامر")
        await msg.delete()
        await c.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
    except:
        await msg.edit("• فعل الانلاين من @botFather")

@Client.on_message(filters.command("تغيير شكل الساعه$", prefixes=f".") & filters.me)
async def change_clock_style(c, msg):
    try:
        result = await c.get_inline_bot_results(bot_user, query="change_clock")
        await msg.delete()
        await c.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
    except:
        await msg.edit("• فعل الانلاين من @botFather")



@Client.on_message(filters.command("مسح الصور$", prefixes=f".") & filters.me & filters.group)
async def del_photos(c, msg):
    await msg.reply("• جاري جلب الصور ..")
    num = 0
    async for message in c.search_messages(msg.chat.id, filter=enums.MessagesFilter.PHOTO):
        try:
            await message.delete(revoke=True)
            num += 1
        except:
            pass
    await msg.edit(f"• تم مسح {num} رساله تحتوي علي صور")



@Client.on_message(filters.command("مسح الترحيب$", prefixes=f".") & filters.me)
async def dellwel(c, msg):
    r.delete(f"{sudo_id}addwelcome{msg.chat.id}")
    return await msg.reply_text("• تم مسح الترحيب")




@Client.on_message(filters.command("تفعيل الترحيب$", prefixes=f".") & filters.me)
async def wel(c, msg):
    r.set(f"{sudo_id}welcome", "on")
    await msg.edit("• تم تفعيل الترحيب")
    await FORCE_JOIN(c)

@Client.on_message(filters.command("تعطيل الترحيب$", prefixes=f".") & filters.me)
async def unwel(c, msg):
    r.delete(f"{sudo_id}welcome")
    await msg.edit("• تم تعطيل الترحيب")
    await FORCE_JOIN(c)

@Client.on_message(filters.command("تعطيل الساعه$", prefixes=f".") & filters.me)
async def clockk(c, msg):
    r.delete(f"{sudo_id}clockk")
    get = await c.get_chat("me")
    await c.update_profile(first_name=f'{get.last_name}', last_name="")
    await msg.edit("• تم تعطيل الساعه")
    await FORCE_JOIN(c)

@Client.on_message(filters.command("تفعيل الساعه$", prefixes=f".") & filters.me)
async def unclockk(c, msg):
    get = await c.get_chat("me")
    if get.last_name:
        my_name = f"{get.first_name} {get.last_name}"
    else:
        my_name = get.first_name
    r.set(f"{sudo_id}clockk", my_name)
    await msg.edit("• تم تفعيل الساعه")
    await name()
    await FORCE_JOIN(c)

@Client.on_message(filters.command("تفعيل بايو وقتي$", prefixes=f".") & filters.me)
async def unkbio(c, msg):
    get = await c.get_chat("me")
    if get.last_name:
        my_name = f"{get.first_name} {get.last_name}"
    else:
        my_name = get.first_name
    r.set(f"{sudo_id}kbio", my_name)
    threading.Thread(target=time_bio).start()
    await msg.edit("• تم تفعيل بايو وقتي")
    await FORCE_JOIN(c)

@Client.on_message(filters.command("تعطيل بايو وقتي$", prefixes=f".") & filters.me)
async def kbio(c, msg):
    r.delete(f"{sudo_id}kbio")
    get = await c.get_chat("me")
    await c.update_profile(bio=f'')
    await msg.edit("• تم تعطيل بايو وقتي")
    await FORCE_JOIN(c)
@Client.on_message(filters.regex("^.تغيير اسمي (.*)") & filters.me)
async def chang_name(c, msg):
    my_name = msg.text
    my_name = my_name.replace(".تغيير اسمي", "")
    r.set(f"{sudo_id}clockk", my_name)
    await msg.edit(f"• تم تغيير اسمك الي {my_name}")
    await name()


@Client.on_message(filters.regex("^.مسح [0-9]+$") & filters.me)
async def del_message(c, msg):
    textt = msg.text
    num = int(textt.split(" ")[1])
    list1 = []
    msg_id = msg.id
    for i in range(1, num):
        list1.append(msg_id)
        msg_id = msg_id - 1
    try:
        await c.delete_messages(msg.chat.id, list1)
    except Exception as e:
        await msg.reply(e)


@Client.on_message(filters.regex("^.سبام (.*?) [0-9]+$") & filters.me)
async def spam_message(c, msg):
    await msg.delete()
    textt = msg.text
    num = int(textt.split(" ")[2])
    word = textt.split(" ")[1]
    for i in range(1, num):
        await c.send_message(msg.chat.id, word)


@Client.on_message(filters.regex("^.بحث (.*)") & filters.me)
async def search_word(c, msg):
    textt = msg.text
    word = textt.replace(".بحث ", "")
    num = 0
    async for message in c.search_messages(msg.chat.id, query=word):
        try:
            await c.send_message(msg.chat.id, ".", reply_to_message_id=message.id)
            num += 1
        except:
            pass
    await message.reply(f"• العدد {num}")


@Client.on_message(filters.command("مسح رسايله$", prefixes=f".") & filters.me & filters.reply)
async def dell_all_msg(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    try:
        await c.delete_user_history(msg.chat.id, msg.reply_to_message.from_user.id)
        await c.send_message(msg.chat.id, "• تم مسح رسايله")
    except Exception as e:
        await msg.edit("• ليس لديك صلاحيه المسح")


@Client.on_message(filters.command("تعين الجروب", prefixes=f".") & filters.me)
async def settgrouup(client, message):
     print("🐾")
     id = int(message.text.replace(".تعين الجروب ", ""))
     r.set(f"{sudo_id}:LOG_CHAT", id)
     await message.edit("تم تعين جروب التخزين")

@Client.on_message(filters.command("مجموعاتي", prefixes=f".") & filters.me)
async def get_group(client, message):
         text = ""
         s = 0
         m = await message.edit("جاري جلب مجموعاتك ..")
         async for dialog in client.get_dialogs():
             try:
                type = dialog.chat.type
                if type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
                  user_s = await dialog.chat.get_member(int(client.me.id))
                  if user_s.status == enums.ChatMemberStatus.OWNER:
                    s += 1
                    if dialog.chat.username:
                      name = f"[{dialog.chat.title}](https://t.me/{dialog.chat.username})"
                    else:
                      link = await client.export_chat_invite_link(dialog.chat.id)
                      name = f"[{dialog.chat.title}]({link})"
                    text += f"{s}- {name}\n"
             except Exception as a:
                   print(a)
         if s == 0: return await m.edit("انت لا تملك اي مجموعات")
         await m.edit(text, disable_web_page_preview=True)


@Client.on_message(filters.command("قنواتي", prefixes=f".") & filters.me)
async def get_channel(client, message):
         text = ""
         s = 0
         m = await message.edit("جاري جلب قنواتك ..")
         async for dialog in client.get_dialogs():
             try:
                type = dialog.chat.type
                if type in [enums.ChatType.CHANNEL]:
                  user_s = await dialog.chat.get_member(int(client.me.id))
                  if user_s.status == enums.ChatMemberStatus.OWNER:
                    s += 1
                    if dialog.chat.username:
                      name = f"[{dialog.chat.title}](https://t.me/{dialog.chat.username})"
                    else:
                      link = await client.export_chat_invite_link(dialog.chat.id)
                      name = f"[{dialog.chat.title}]({link})"
                    text += f"{s}- {name}\n"
             except Exception as a:
                   print(a)
         if s == 0: return await m.edit("انت لا تملك اي قنوات")
         await m.edit(text, disable_web_page_preview=True)

@Client.on_message(filters.command(["م1$", "اوامر الخاص$"], prefixes=f".") & filters.me)
async def crist(c, msg):
    await msg.edit("""
⦇  اوامر الخاص ⦈

❀  ⦗ .تلجراف ⦘  بالرد علي الصوره

❀  ⦗ .وش يقول ⦘  بالرد علي الصوت 

❀  ⦗ .تغيير اسمي + كتابه الاسم ⦘ . تغيير اسمي سوريا

❀  ⦗ .تفعيل الترحيب ⦘

❀  ⦗ .تعطيل الساعه ⦘ 

❀  ⦗ .تفعيل الساعه ⦘

❀  ⦗ .تعطيل الساعه ⦘

❀  ⦗ .سبام + كتابه الكلمه + كتابه الرقم ⦘

❀  ⦗ .سورس ⦘ 

❀  ⦗ .قبول ⦘

❀  ⦗ .رفض ⦘

❀  ⦗ .كتم ⦘

❀  ⦗ .الغاء كتم ⦘

◉ اوامر الفارت ⦂

❀  الأمر ⦂ ⦗ .ايدي ⦘ 
◉ الشرح ⦂ بالرد علي الشخص

❀  الأمر ⦂ ⦗ .ضبط PMG_MEDIA ⦘ 
◉ الشرح ⦂ لوضع صوره ترحيب في الخاص

❀  الأمر ⦂ ⦗ .الغاء ضبط PMG_MEDIA ⦘
◉ الشرح ⦂ للرجوع لصورة الترحيب الافتراضيه

❀  الأمر ⦂ ⦗ .ضبط PM_TEXT_CUSTOM ⦘ 
◉ الشرح ⦂ لتغير النص تحت صورة الترحيب

❀  الأمر ⦂ ⦗ .الغاء ضبط PM_TEXT_CUSTOM ⦘ 
◉ الشرح ⦂ لحذف النص والرجوع للنص الافتراضي

❀  الأمر ⦂ ⦗ .ضبط CHANNEL ⦘ 
◉ الشرح ⦂ لوضع قناتك في كليشة الترحيب

❀  الأمر ⦂ ⦗ .الغاء ضبط CHANNEL ⦘ ◉ الشرح ⦂ لوضع قناتك في كليشة الترحيب

""") 

@Client.on_message(filters.command(["م12$", "الفارات$"], prefixes=f".") & filters.me)
async def siri(c, msg):
    await msg.edit(
"•━═━═━═『ٓ᥆』═━═━═━•\n• ↯︙❬ .ضبط PMG_MEDIA  ❭ لوضع صوره ترحيب في الخاص\n• ↯︙❬ .الغاء ضبط PMG_MEDIA ❭ للرجوع لصورة الترحيب الافتراضيه\n• ↯︙❬ .ضبط PM_TEXT_CUSTOM ❭ لتغير النص تحت صورة الترحيب\n• ↯︙❬ .الغاء ضبط PM_TEXT_CUSTOM ❭ لحذف النص والرجوع للنص الافتراضي\n• ↯︙❬ .ضبط CHANNEL ❭ لوضع قناتك في كليشة الترحيب\n• ↯︙❬ .الغاء ضبط CHANNEL ❭ لرجوع الي  قناه السورس\n••━═━═━═『ٓ᥆』═━═━═━•")
  
@Client.on_message(filters.command(["م2$", "اوامر المجموعات$"], prefixes=f".") & filters.me)
async def shiko(c, msg):
    await msg.edit("""
⧉
⦇ اومر المجموعات ⦈
❀  الأمر ⦂ ⦗ .حظر ⦘
◉ شرح ⦂ يقوم بحظر الشخص من المجموعه

❀  الأمر ⦂ ⦗ .الغاء حظر ⦘
◉ شرح ⦂ يقوم بإلغاء حظر الشخص من المجموعه

❀  الأمر ⦂ ⦗ .حظر عام  ⦘
◉ شرح ⦂ يقوم بحظر الشخص عام

❀  الأمر ⦂ ⦗ .مسح المحظورين ⦘
◉ شرح ⦂ يقوم بمسح جميع المحظورين

❀  الأمر ⦂ ⦗ .كتم عام ⦘
◉ شرح ⦂ يقوم بكتم الشخص عام في الخاص ، المجموعه

❀  الأمر ⦂ ⦗ .الغاء كتم عام ⦘
◉ شرح ⦂ يقوم بالغاء كتم الشخص عام من الخاص ، المجموعه

❀  الأمر ⦂ ⦗ .مسح المكتومين ⦘
◉ شرح ⦂ يقوم بمسح جميع المكتومين

❀  الأمر ⦂ ⦗ .مسح قائمه العام ⦘
◉ شرح ⦂ يقوم بمسح قائمه العام

❀  الأمر ⦂ ⦗ .مسح رسايله ، بالرد ⦘
◉ شرح ⦂ يقوم بمسح جميع رسايل العض

❀  الأمر ⦂ ⦗ .تدمير ⦘
◉ شرح ⦂ يقوم بحظر جميع اعضاء المجموعه

❀  الأمر ⦂ ⦗ .مسح الروابط ⦘
◉ شرح ⦂ يقوم بمسح جميع الروابط

❀  الأمر ⦂ ⦗ .مسح الصور ⦘
◉ شرح ⦂ يقوم بمسح جميع الصور

❀  الأمر ⦂ ⦗ .فتح الكول ⦘
◉ شرح ⦂ يقوم بفتح الكول في المجموعه

❀  الأمر ⦂ ⦗ .قفل الكول ⦘
◉ شرح ⦂ يقوم بقفل الكول في المجموعه

❀  الأمر ⦂ ⦗ .غادر ⦘
◉ شرح ⦂  يقوم بمغادره المجموعه 

❀  الأمر ⦂ ⦗ .رفع مشرف ⦘
◉ شرح ⦂ يقوم برفع الشخص مشرف بالمجموعه

❀  الأمر ⦂ ⦗ .اهمس بالرد علي الشخص ⦘
◉ شرح ⦂ بقوم بعمل همسه ل الشخص

❀  الأمر ⦂ ⦗الرابط ⦘
◉ شرح ⦂ لجلب رابط المجموعه

❀  الأمر ⦂ ⦗ قبول الطلبات ⦘
◉ شرح ⦂  لقبول جميع طلبات الانضمام

❀  الأمر ⦂ ⦗ .lock all ⦘
◉ شرح ⦂ يقوم بقفل الدردشه في المجموعه 

❀  الأمر ⦂ ⦗ .umlock ⦘
◉ شرح ⦂ يقوم بفتح الدردشه في المجموعه

◉ جميع الاوامر تكون بدايتها نقطة .
⧉
""")  


@Client.on_message(filters.command(["م3$", "اوامر اليوتيوب$"], prefixes=f".") & filters.me)
async def adam(c, msg):
    await msg.edit("""
⦁           ﹎﹎﹎﹎﹎﹎﹎﹎              ⦁

⦇ اوامر اليوتيوب ⦈

❀  الأمر ⦂ ⦗ .غ + اسم الاغنيه ⦘
◉ شرح ⦂ يقوم بتنزيل الاغنيه من اليوتيوب 

❀  الأمر ⦂ ⦗ .ف + اسم الفديو ⦘
◉ شرح ⦂ يقوم بتنزيل الفديو من اليوتيوب

❀  الأمر ⦂ ⦗ سوش + الرابط ⦘
◉ شرح ⦂ يقوم بجلب الفيديو من التيك توك بدون حقوق

 ⦁           ﹎﹎﹎﹎﹎﹎﹎﹎             ⦁
""")  

@Client.on_message(filters.command(["م17$", "اوامر الكتابه والخط$"], prefixes=f".") & filters.me)
async def ktabtkat(c, msg):
    await msg.edit("""
⦁             ﹎﹎﹎﹎﹎﹎﹎﹎             ⦁

⧉  اوامر الكتابه والخط  ⦂
❀  الأمر ⦂ ⦗ .تفعيل تعديل الخط ⦘
◉ شرح ⦂ يقوم يقوم بعرض اوامر تغيير الخط اليك
❀  الأمر ⦂ ⦗ .تعطيل تعديل الخط ⦘
◉ شرح ⦂ لاسترجاع خط الكتابه العادي

⦁            ﹎﹎﹎﹎﹎﹎﹎﹎              ⦁
""")  


@Client.on_message(filters.command(["م16$", "اوامر الوقتيه $"], prefixes=f".") & filters.me)
async def wkteaa(c, msg):
    await msg.edit("""
⦁             ﹎﹎﹎﹎﹎﹎﹎﹎              ⦁

⧉ اوامر الوقتيه  ⦂
❀  تفعيل بايو وقتي
◉ تعطيل بايو وقتي
❀  تفعيل الساعه 
◉ تعطيل الساعه 
❀  لضبط قناتك في البايو 
◉ استخدم الفار ⦗ .ضبط CHANNEL ⦘
❀  تفعيل الصوره الوقتيه
◉ تعطيل الصوره الوقتيه

◉ جميع الاوامر تكون بدايتها نقطة .

⦁           ﹎﹎﹎﹎﹎﹎﹎﹎               ⦁
""") 
  
  

@Client.on_message(filters.command(["م4$", "اوامر الاذاعة$"], prefixes=f".") & filters.me)
async def hussin(c, msg):
    await msg.edit("""
⦁               ﹎﹎﹎﹎﹎﹎﹎﹎             ⦁

⦇ اوامر الاذاعه ⦈

❀  الأمر ⦂ ⦗ .اذاعه خاص ⦘
◉ شرح ⦂ يقوم بعمل اذاعه في الخاص 

❀  الأمر ⦂ ⦗ .اذاعه للمجموعات ⦘
◉ شرح ⦂ يقوم بعمل اذاعه في جميع المجموعات 

❀  الأمر ⦂ ⦗ .اذاعه للقنوات ⦘
◉ شرح ⦂ يقوم بعمل اذاعه في جميع القنوات

❀  الأمر ⦂ ⦗ .توجيه للخاص ⦘
◉ شرح ⦂ يقوم بعمل توجيه في الخاص 

❀  الأمر ⦂ ⦗ توجيه للمجوعات ⦘
◉ شرح ⦂ يقوم بعمل توجيه في جميع المجموعات
 
❀  الأمر ⦂ ⦗ .توجيه للقنوات ⦘
◉ شرح ⦂ يقوم بعمل توجيه في جميع القنوات 

◉ جميع الاوامر تكون بدايتها نقطة .

⦁              ﹎﹎﹎﹎﹎﹎﹎﹎              ⦁
""")


@Client.on_message(filters.command(["م5$", "اوامر الرفع$"], prefixes=f".") & filters.me)
async def zaid(c, msg):
    await msg.edit("""
⦁              ﹎﹎﹎﹎﹎﹎﹎﹎            ⦁

◉ زواج ، طلاق  زوجاتي  مسح زوجاتي
◉ رفع ، تنزيل خول  الخولات  مسح الخولات 
◉ رفع ، تنزيل بنتي  بناتي  مسح بناتي
◉ رفع ، تنزيل شاذ  الشواذ  مسح الشواذ
◉ رفع ، تنزيل عرص  المعرصين  مسح المعرصين
◉ رفع ، تنزيل كلب  الكلاب  مسح الكلاب
◉ رفع ، تنزيل متوحد  المتوحدين  مسح المتوحدين
◉ رفع ، تنزيل متوحد  المتوحدين  مسح المتوحدين
◉ رفع ، تنزيل حمار  الحمير  مسح الحمير
◉ رفع ، تنزيل بقلبي  القلوب  مسح القلوب
◉ رفع ، تنزيل ابني ، اولادي ، مسح اولادي

⦁             ﹎﹎﹎﹎﹎﹎﹎﹎             ⦁
""")

 
@Client.on_message(filters.command(["م6$", "اوامر النسب$"], prefixes=f".") & filters.me)
async def eyad(c, msg):
    await msg.edit("""
⦁            ﹎﹎﹎﹎﹎﹎﹎﹎              ⦁

 ⦇ اوامر النسب ⦈

❀  الأمر ⦂ ⦗ .نسبة الحب ⦘
◉ شرح ⦂ يقوم بمعرفه نسبة الحب بينك وبين الشخص 

❀  الأمر ⦂ ⦗ .نسبة الذكاء ⦘
◉ شرح ⦂ يقوم بمعرفه نسبة الذكاء بينك وبين الشخص

❀  الأمر ⦂ ⦗ .نسبة الكره ⦘
◉ شرح ⦂ يقوم بمعرفه نسبة الكره بينك وبين الشخص

❀  الأمر ⦂ ⦗ .الشذوذ ⦘
◉ شرح ⦂ يقوم بمعرفه نسبة الشذوذ بينك وبين الشخص 

❀  الأمر ⦂ ⦗ .نسبة الهطل ⦘
◉ شرح ⦂ يقوم بمعرفه نسبة الهطل بينك وبين الشخص

❀  الأمر ⦂ ⦗ .نسبة العفانه ⦘
◉ شرح ⦂ يقوم بمعرفه نسبة العفانه بينك وبين الشخص

❀  الأمر ⦂ ⦗ .نسبة العبط ⦘
◉ شرح ⦂ يقوم بمعرفه نسبة العبط بينك وبين الشخص

❀  الأمر ⦂ ⦗ .نسبة القوة ⦘
◉ شرح ⦂ يقوم بمعرفه نسبة القوة بينك وبين الشخص 

❀  الأمر ⦂ ⦗ .نسبة الغباء ⦘
◉ شرح ⦂ يقوم بمعرفه نسبة الغباء بينك وبين الشخص

❀  الأمر ⦂ ⦗ .نسبة الانوثه ⦘
◉ شرح ⦂ يقوم بمعرفه نسبة الانوثه بينك وبين الشخص

❀  الأمر ⦂ ⦗ .نسبة الضعف ⦘
◉ شرح ⦂ يقوم بمعرفه نسبة الضعف بينك وبين الشخص 

◉ جميع الاوامر تكون بدايتها نقطة .

⦁            ﹎﹎﹎﹎﹎﹎﹎﹎               ⦁
""")  

@Client.on_message(filters.command(["م7$", "اوامر اضافية$"], prefixes=f".") & filters.me)
async def khapold(c, msg):
    await msg.edit("""
⦁             ﹎﹎﹎﹎﹎﹎﹎﹎            ⦁

 ⦇ اوامر اضافيه ⦈

❀  الأمر ⦂ ⦗ .تلجراف ⦘
◉ شرح ⦂ يقوم برفع الصوره ، الفديو علي تلجراف

❀  الأمر ⦂ ⦗ .وش يقول ⦘
◉ شرح ⦂ يقوم بجلب الكلام من الريكورد 

❀  الأمر ⦂ ⦗ .سورس ⦘
◉ شرح ⦂ يقوم بجلب معلومات السورس

◉ جميع الاوامر تكون بدايتها نقطة .

⦁            ﹎﹎﹎﹎﹎﹎﹎﹎             ⦁
""") 


@Client.on_message(filters.command(["م8$", "اوامر تسلية$"], prefixes=f".") & filters.me)
async def pokrmon(c, msg):
    await msg.edit("""
⦇  اوامر اضافيه ⦈

◉ ⦗ .شرطه ⦘ بالرد علي الشخص

◉ ⦗ .تهكير ⦘ بالرد علي الشخص 

◉ ⦗ .قتل ⦘ بالرد علي الشخص

◉ ⦗ .اقمار ⦘ ، ⦗ .قمور ⦘

◉ ⦗ .مربع ⦘ ، ⦗ .دائره ⦘

◉ ⦗ .يد ⦘ ، ⦗ .قياس ⦘

◉ ⦗ .تحميل ⦘

◉ ⦗ .بشره ⦘ ، ⦗ .العدد التنازلي ⦘

◉ ⦗ .معاكسه ⦘ ، ⦗ .عبقري ⦘

◉ ⦗ .افعي ⦘ ،  ⦗ .الارض ⦘

◉ ⦗ .ولد ⦘ ، ⦗ .مايكرو ⦘ 

◉ ⦗ .فايروس ⦘ ، ⦗ .نيكول ⦘

◉ ⦗ .رسم ⦘ ، ⦗ .نجمه ⦘

◉ ⦗ .مكعبات ⦘ ، ⦗ .مطر ⦘ 

◉ ⦗ .تفريغ ⦘ ، ⦗ .النظام الشمسي ⦘ 

◉ ⦗ .افكار ⦘ ، ⦗ .متت ⦘

◉ ⦗ .زعلت ⦘ ، ⦗ .ساعه ⦘ 

◉ ⦗ .مح ⦘ ، ⦗.جيم ⦘
""") 


@Client.on_message(filters.command(["م9$", "اوامر تسلية2$"], prefixes=f".") & filters.me)
async def ferska(c, msg):
    await msg.edit("""
⦁              ﹎﹎﹎﹎﹎﹎﹎﹎               ⦁
◉ متت
◉ زعلت
◉ ساعه
◉ مح
◉ جيم
◉ الارض
◉ اقمار
◉ قمور
◉ تنصيب
◉ كلب
◉ خنزير
◉ اعمل ليك
◉ اجري
◉ رعد
◉ دبابه
◉ انتحر
◉ قناص
◉ غبي
◉ قنبلة
◉ كبلز
◉ مدينة
◉ سبونج
◉ صدمه
◉ فيل
◉ ريفيرسي
 ⦁                 ﹎﹎﹎﹎﹎﹎﹎﹎           ⦁
""") 

@Client.on_message(filters.command(["م21$", "اوامر االمساعده$"], prefixes=f".") & filters.me)
async def cmd_m21(c, msg):
    await msg.edit("""
⦁              ﹎﹎﹎﹎﹎﹎﹎﹎            ⦁ 

⧉ اوامر االمساعده

❀  الامر ⦂ ⦗ رنلي + اضف صديق +حذف صديق+الاصدقاء+ليك حد معين 3 رنات بس في اليوم ⦘
◉ الشرح ⦂ ميزه جديده  اضف صديق
بتضيف اتنين من اصحابك اصدقاء عندك
لو واحد منهم معهوش رصيد ومحتاجك ضروري يعمل اي وانتا قافل
هيكتبلك في الشات رنلي
التليثون هيرن علي رقمك رنه خفيفه كدا يعرفك ان حد محتاجك علي التليجرام
◉ مثال . رنلي بلرد علي الشخص

⦁               ﹎﹎﹎﹎﹎﹎﹎﹎          ⦁
""") 
@Client.on_message(filters.command(["م22$", "اوامر التحميل والترجمه$"], prefixes=f".") & filters.me)
async def cmd_m22(c, msg):
    await msg.edit("""
⦁              ﹎﹎﹎﹎﹎﹎﹎﹎            ⦁ 

⧉ اوامر التحميل والترجمه

❀  الامر ⦂ ⦗ ترجم + الجمله او ريب علي الجمله ⦘
◉ الشرح ⦂ يقوم بترجمة اي جمله من اي لغه الي اللغه العربيه
◉ مثال .ترجم  𝗈𝗋𝖽𝖾𝗋 𝗍𝖾𝗅𝖾𝗍𝗁𝗈𝗇

❀  الامر ⦂ ⦗ تحميل + اي رابط من اي موقع ⦘
 ◉ الشرح ⦂ تحميل فيديو بدون علامات مائيه من اي موقع سوشيال ميديا انستا تيك توك فيس بوك 

⦁               ﹎﹎﹎﹎﹎﹎﹎﹎          ⦁
""") 

@Client.on_message(filters.command(["م23$", "اوامر الاستيت$"], prefixes=f".") & filters.me)
async def cmd_m23(c, msg):
    await msg.edit("""
⦁              ﹎﹎﹎﹎﹎﹎﹎﹎            ⦁ 

⧉ اوامر الاستيت

❀  الامر ⦂ ⦗ رفع ستوري + وصف الحاله+ ريب علي الفيديو او الصوره ⦘
◉ الشرح ⦂ يقوم برفع الفيديو الخاص بك الي حالتك ويمكنك ايضا رفع صوره ويمكنك الوصول للحد الاقصي من الحالات اليوميه
◉ مثال .رفع ستوري تجربه

⦁               ﹎﹎﹎﹎﹎﹎﹎﹎          ⦁
""") 
@Client.on_message(filters.command("رموز1$", prefixes=f".") & filters.me)
async def rmozo(c, msg):
    await msg.edit(
        "`𓅄 𓅅 𓅆 𓅇 𓅈 𓅉 𓅊 𓅋 𓅌 𓅍 𓅎 𓅏 𓅐 𓅑 𓅒 𓅓 𓅔𓅕 𓅖 𓅗 𓅘 𓅙 𓅚 𓅛 𓅜 𓅝 𓅞 𓅟 𓅠 𓅡 𓅢 𓅣 𓅤 𓅥 𓅦 𓅧 𓅨 𓅩 𓅫 𓅬 𓅭 𓅮 𓅯 𓅰 𓅱 𓅲 𓅳 𓅴 \n𓅵 𓅶 𓅷 𓅸 𓅹 𓅺 𓅻\n☤ 𓅾 𓅿 𓆀 𓆁 𓆂\n𓀀 𓀁 𓀂 𓀃 𓀄 𓀅 𓀆 𓀇 𓀈 𓀉 𓀊 𓀋 𓀌 𓀍 𓀎 𓀏 𓀐 𓀑 𓀒 𓀓 𓀔 𓀕 𓀖 𓀗 𓀘 𓀙 𓀚 𓀛 𓀜 𓀝 𓀞 𓀟 𓀠 𓀡 𓀢 𓀣 𓀤 𓀥 𓀦 𓀧 𓀨 𓀩 𓀪 𓀫 𓀬 𓀭 𓀮 𓀯 𓀰 𓀱 𓀲 𓀳 𓀴 𓀵 𓀶 𓀷 𓀸 𓀹 𓀺 𓀻 𓀼 𓀽 𓀾 𓀿 𓁀 𓁁 𓁂 𓁃 𓁄 𓁅 𓁆 𓁇 𓁈 𓁉 𓁊 𓁋 𓁌 𓁍 𓁎 𓁏 𓁐 𓁑 𓁒 𓁓 𓁔 𓁕 𓁖 𓁗 𓁘 𓁙 𓁚 𓁛 𓁜 𓁝 𓁞 𓁟 𓁠 𓁡 𓁢 𓁣 𓁤 𓁥 𓁦 𓁧 𓁨 𓁩 𓁪 𓁫 𓁬 𓁭 𓁮 𓁯 𓁰 𓁱 𓁲 𓁳 𓁴 𓁵 𓁶 𓁷 𓁸 𓁹 𓁺 𓁻 𓁼 𓁽 𓁾 𓁿 𓂀𓂅 𓂆 𓂇 𓂈 𓂉 𓂊 𓂋 𓂌 𓂍 𓂎 𓂏 𓂐 𓂑 𓂒 𓂓 𓂔 𓂕 𓂖 𓂗 𓂘 𓂙 𓂚 𓂛 𓂜 𓂝 𓂞 𓂟 𓂠 𓂡 𓂢 𓂣 𓂤 𓂥 𓂦 𓂧 𓂨 𓂩 𓂪 𓂫 𓂬 𓂭 𓂮 𓂯 𓂰 𓂱 𓂲 𓂳 𓂴 𓂵 𓂶 𓂷 𓂸 𓂹 𓂺 𓂻 𓂼 𓂽 𓂾 𓂿 𓃀 𓃁 𓃂 𓃃 𓃅 𓃆 𓃇 𓃈 𓃉 𓃊 𓃋 𓃌 𓃍 𓃎 𓃏 𓃐 𓃑 𓃒 𓃓 𓃔 𓃕 𓃖 𓃗 𓃘 𓃙 𓃚 𓃛 𓃜 𓃝 𓃞 𓃟 𓃠 𓃡 𓃢 𓃣 𓃤 𓃥 𓃦 𓃧 𓃨 𓃩 𓃪 𓃫 𓃬 𓃭 𓃮 𓃯 𓃰 𓃱 𓃲 𓃳 𓃴 𓃵 𓃶 𓃷 𓃸 𓃹 𓃺 𓃻 𓃼 𓃽 𓃾 𓃿 𓄀 𓄁 𓄂 𓄃 𓄄 𓄅 𓄆 𓄇 𓄈 𓄉 𓄊 𓄋 𓄌 𓄍 𓄎 𓄏 𓄐 𓄑 𓄒 𓄓 𓄔 𓄕 𓄖 𓄙 𓄚 𓄛 𓄜 𓄝 𓄞 𓄟 𓄠 𓄡 𓄢 𓄣 𓄤 𓄥 𓄦 𓄧 𓄨 𓄩 𓄪 𓄫 𓄬 𓄭 𓄮 𓄯 𓄰 𓄱 𓄲 𓄳 𓄴 𓄵 𓄶 𓄷 𓄸 𓄹 𓄺   𓄼 𓄽 𓄾 𓄿 𓅀 𓅁 𓅂 𓅃 𓅄 𓅅 𓅆 𓅇 𓅈 𓅉 𓅊 𓅋 𓅌 𓅍 𓅎 𓅏 𓅐 𓅑 𓅒 𓅓 𓅔 𓅕 𓅖 𓅗 𓅘 𓅙 𓅚 𓅛 𓅜 𓅝 𓅞 𓅟 𓅠 𓅡 𓅢 𓅣 𓅤 𓅥 𓅦 𓅧 𓅨 𓅩 𓅪 𓅫 𓅬 𓅭 𓅮 𓅯 𓅰 𓅱 𓅲 𓅳 𓅴 𓅵 𓅶 𓅷 𓅸 𓅹 𓅺 𓅻 𓅼 𓅽 𓅾 𓅿 𓆀 𓆁 𓆂 𓆃 𓆄 𓆅 𓆆 𓆇 𓆈 𓆉 𓆊 𓆋 𓆌 𓆍 𓆎 𓆐 𓆑 𓆒 𓆓 𓆔 𓆕 𓆖 𓆗 𓆘 𓆙 𓆚 𓆛 𓆜 𓆝 𓆞 𓆟 𓆠 𓆡 𓆢 𓆣 𓆤 𓆥 𓆦 𓆧 𓆨 𓆩𓆪 𓆫 𓆬 𓆭 𓆮 𓆯 𓆰 𓆱 𓆲 𓆳 𓆴 𓆵 𓆶 𓆷 𓆸 𓆹 𓆺 𓆻 𓆼 𓆽 𓆾 𓆿 𓇀 𓇁 𓇂 𓇃 𓇄 𓇅 ?? 𓇇 𓇈 𓇉 𓇊 𓇋 𓇌 𓇍 𓇎 𓇏 𓇐 𓇑 𓇒 𓇓 𓇔 𓇕 𓇖 𓇗 𓇘 𓇙 𓇚 𓇛 𓇜 𓇝 𓇞 𓇟 𓇠 𓇡 𓇢 𓇣 𓇤 𓇥 𓇦 𓇧 𓇨 𓇩 𓇪 𓇫 𓇬 𓇭 𓇮 𓇯 𓇰 𓇱 𓇲 𓇳 𓇴 𓇵 𓇶 𓇷 𓇸 𓇹 𓇺 𓇻 𓇼 𓇾 𓇿 𓈀 𓈁 𓈂 𓈃 𓈄 𓈅 𓈆 𓈇 𓈈 𓈉 𓈊 𓈋 𓈌 𓈍 𓈎 𓈏 𓈐 𓈑 𓈒 𓈓 𓈔 𓈕 𓈖 𓈗 𓈘 𓈙 𓈚 𓈛 𓈜 𓈝 𓈞 𓈟 𓈠 𓈡 𓈢 𓈣 𓈤  𓈥 𓈦 𓈧 𓈨 𓈩 𓈪 𓈫 𓈬 𓈭 𓈮 𓈯 𓈰 𓈱 𓈲 𓈳 𓈴 𓈵 𓈶 𓈷 𓈸 𓈹 𓈺 𓈻 𓈼 𓈽 𓈾 𓈿 𓉀 𓉁 𓉂 𓉃 𓉄 𓉅 𓉆 𓉇 𓉈 𓉉 𓉊 𓉋 𓉌 𓉍 𓉎 𓉏 𓉐 𓉑 𓉒 𓉓 𓉔 𓉕 𓉖 𓉗 𓉘 𓉙 𓉚 𓉛 𓉜 𓉝 𓉞 𓉟 𓉠 𓉡 𓉢 𓉣 𓉤 𓉥 𓉦 𓉧 𓉨 𓉩 𓉪 𓉫 𓉬 𓉭 𓉮 𓉯 𓉰 𓉱 𓉲 𓉳 𓉴 𓉵 𓉶 𓉷 𓉸 𓉹 𓉺 𓉻 𓉼 𓉽 𓉾 𓉿 𓊀 𓊁 𓊂 𓊃 𓊄 𓊅 𓊈 𓊉 𓊊 𓊋 𓊌 𓊍 𓊎 𓊏 𓊐 𓊑 𓊒 ?? 𓊔 𓊕 ?? ?? 𓊘 𓊙 𓊚 𓊛 𓊜 𓊝 𓊞 𓊟 𓊠 𓊡 𓊢 𓊣 𓊤 𓊥 𓊦 𓊧 𓊨 𓊩 𓊪 𓊫 𓊬 𓊭 𓊮 𓊯 𓊰 𓊱 𓊲 𓊳 𓊴 𓊵 𓊶 𓊷 𓊸 𓊹 𓊺 𓊻 𓊼 ?? ?? 𓊿 𓋀 𓋁 𓋂 𓋃 𓋄 𓋅 𓋆 𓋇 𓋈 𓋉 𓋊 𓋋 𓋌 𓋍 𓋎 𓋏 𓋐 𓋑 𓋒 𓋓 𓋔 𓋕 𓋖 𓋗 𓋘 𓋙 𓋚 𓋛 𓋜 𓋝 𓋞 𓋟 𓌰 𓌱 𓌲 𓌳 𓌴 𓌵 𓌶 𓌷 𓌸 𓌹 𓌺 𓌻 𓌼 𓌽 𓌾 𓌿 𓍀 𓍁 𓍂 𓍃 𓍄 𓍅 𓍆 𓍇 𓍈 𓍉 𓍊 𓍋 𓍌 𓍍 𓍎 𓍏 𓍐 𓍑 𓍒 𓍓 𓍔 𓍕 𓍖 𓍗 𓍘 𓍙 𓍚 𓍛 𓍜 𓍝 𓍞 𓍟 𓍠 𓍡 𓍢 𓍣 𓍤 𓍥 𓍦 𓍧 𓍨 𓍩 𓍪 𓍫 𓍬 𓍭 𓍮 𓍯 𓍰 𓍱 𓍲 𓍳 𓍴 𓍵 𓍶 𓍷 𓍸 𓍹 𓍺 𓍻 𓍼 𓍽 𓍾 𓍿 𓎀 𓎁 𓎂 𓎃 𓎄 𓎅 𓎆 𓎇 𓎈 𓎉 𓎊 𓎋 𓎌 𓎍 𓎎 𓎏 𓎐 𓎑 𓎒 𓎓 𓎔 𓎕 𓎖 𓎗 𓎘 𓎙 𓎚 𓎛 𓎜 𓎝 𓎞 𓎟 𓎠 𓎡 𓏋 𓏌 𓏍 𓏎 𓏏 𓏐 𓏑 𓏒 𓏓\n  𓏕 𓏖 𓏗 𓏘 𓏙 𓏚 𓏛 𓏜 𓏝 𓏞 𓏟 𓏠 𓏡 𓏢 𓏣 𓏤 𓏥 𓏦 𓏧 𓏨 𓏩 𓏪 𓏫 𓏬 𓏭 𓏮 𓏯 𓏰 𓏱 𓏲 𓏳 𓏴 𓏶 𓏷 𓏸 𓏹 𓏺 𓏻 𓏼 𓏽 𓏾 𓏿 𓐀 𓐁 𓐂 𓐃 𓐄 𓐅 𓐆\n- 𖣨 ، ෴ ، 𖡺  ، 𖣐 ، ✜ ، ✘ ، 𖡻 ،\n- ༄ ، ༺༻ ، ༽༼ ،  ╰☆╮،  \n- ɵ̷᷄ˬɵ̷᷅ ، ⠉̮⃝ ، ࿇࿆ ، ꔚ، ま ، ☓ ،\n𓆉 . 𓃠 .𓅿 . 𓃠 . 𓃒 . 𓅰 . 𓃱 . 𓅓 . 𐂃  . ꕥ  . ⌘ . ♾ .    ꙰  .  . ᤑ .  ﾂ .\n✦ ,✫ ,✯, ✮ ,✭ ,✰, ✬ ,✧, ✤, ❅ , 𒀭,✵ , ✶ , ✷ , ✸ , ✹ ,⧫, . 𐂂 \n-〘 𖢐 ، 𒍦 ، 𒍧 ، 𖢣 ، 𝁫 ، 𒍭 ، 𝁅 ، 𝁴 ، 𒍮 ، 𝁵 ، 𝀄 ، 𓏶 ، 𓏧 ، 𓏷 ، 𓏯 ، 𓏴 ، 𓏳 ، 𓏬 ، 𓏦 ، ?? ، 𓏱 ، ᳱ ، ᯼ ، 𐃕 ، ᯥ ، ᯤ ، ᯾ ، ᳶ ، ᯌ ، ᢆ ،\n ᥦ ، ᨙ ، ᨚ  ، ᨔ  ، ⏢ ، ⍨ ، ⍃ ، ⏃ ، ⍦ ، ⏕ ، ⏤ ، ⏁ ، ⏂ ، ⏆ ، ⌳ ، ࿅ ، ࿕ ، ࿇ ، ᚙ ، ࿊ ، ࿈ ، ྿ \n ࿂ ، ࿑ ،  ᛥ ، ࿄ ، 𐀁 ، 𐀪 ، 𐀔 ، 𐀴 ، 𐀤 ، 𐀦 ، 𐀂 ، 𐀣 ، 𐀢 ، 𐀶 ، 𐀷 ، 𐂭 ، 𐂦 ، 𐂐 ، 𐂅 ، 𐂡 ، 𐂢 ، 𐂠 ، 𐂓 ، 𐂑 ، 𐃸 ، 𐃶 ، 𐂴 ، 𐃭 ، 𐃳 ، 𐃣 ، 𐂰 ، 𐃟 ، 𐃐 ، 𐃙 ، 𐃀 ، 𐇮 ، 𐇹 ، 𐇲 ، 𐇩 ، 𐇪 ، 𐇶 ، 𐇻 ، 𐇡 ، 𐇸 ، 𐇣 ، 𐇤 ، 𐎅 ، 𐏍 ، 𐎃 ، 𐏒 ، 𐎄 ، 𐏕 〙.\n╔ ╗. 𓌹  𓌺 .〝  〞. ‹ ›  .「  」.〖 〗. 《》 .  < > . « »  . ﹄﹃\n₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ ₀\n𝟏 𝟐 𝟑 𝟒 𝟓 𝟔 𝟕 𝟖 𝟗 𝟎\n𝟭 𝟮 𝟯 𝟰 𝟱 𝟲 𝟳 𝟴 𝟵 𝟬\n①②③④⑤⑥⑦⑧⑨⓪\n❶❷❸❹❺❻❼❽❾⓿\n⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴ `") 
        
        

@Client.on_message(filters.command("رموز2$", prefixes=f".") & filters.me)
async def rmozos(c, msg):
    await msg.edit(
        " 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾  𝟿\n ? 𝟙  𝟚  𝟛  𝟜  𝟝  𝟞  𝟟  𝟠 𝟡\n 𝟬 𝟭  𝟮  𝟯  𝟰  𝟱   𝟲  𝟳  𝟴  𝟵  \n 𝟎  𝟏  𝟐  𝟑  𝟒   𝟓   𝟔  𝟕   𝟖   𝟗\n０ １ ２ ３ ４ ５ ６ ７８９\n•━═━═━═『ٓ᥆』═━═━═━•\n ᾋ ᾌ ᾍ ᾎ ᾏ ᾐ ᾑ ᾒ ᾓ ᾔ ᾕ ᾖ ᾗ ᾘ ᾙ ᾚ ᾛ ᾜ ᾝ ᾞ ᾟ ᾠ ᾡ ᾢ ᾣ ᾤ ᾥ ᾦ ᾧ ᾨ ᾩ ᾪ ᾫ ᾬ ᾭ ᾮ ᾯ ᾰ ᾱ ᾲ ᾳ ᾴ ᾶ ᾷ Ᾰ Ᾱ Ὰ Ά ᾼ ᾽ ι ᾿ ῀ ῁ ῂ ῃ ῄ ῆ ῇ Ὲ Έ Ὴ Ή ῌ ῍ ῎ ῏ ῐ ῑ ῒ ΐ ῖ ῗ Ῐ Ῑ Ὶ Ί ῝ ῞ ῟ ῠ ῡ ῢ ΰ ῤ ῥ ῦ ῧ Ῠ Ῡ Ὺ Ύ Ῥ ῭ ΅ ` ῲ ῳ ῴ ῶ ῷ Ὸ Ό Ὼ Ώ ῼ ´ ῾ ῿                         ‌ ‍ ‎ ‏ ‐ ‑ ‒ – — ― ‖ ‗ ‘ ’ ‚ ‛ “ ” „ ‟ † ‡ • ‣ ․ ‥ … ‧       ‰ ‱ ′ ″ ‴ ‵ ‶ ‷ ‸ ‹ › ※  ‽ ‾ ‿ ⁀ ⁁ ⁂ ⁃ ⁄ ⁅ ⁆ ⁇  ⁊ ⁋ ⁌ ⁍ ⁎ ⁏ ⁐ ⁑ ⁒ ⁓ ⁔ ⁕ ⁖ ⁗ ⁘ ⁙ ⁚ ⁛ ⁜ ⁝ ⁞   ⁠ ⁡ ⁢ ⁣ ⁤ ⁥ ‌ ‌ ⁨ ⁩ ⁪ ⁫ ⁬ ⁭ ⁮ ⁯ ⁰ ⁱ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁿ ₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ ₐ ₑ ₒ ₓ ₕ ₖ ₗ ₘ ₙ ₚ ₛ ₜ ₝ ₞ ₟ ₠ ₡ ₢ ₣ ₤ ₥ ₦ ₧ ₨ ₩ ₪ ₫ € ₭ ₮ ₯ ₰ ₱ ₲ ₳ ₴ ₵ ℀ ℁ ℂ ℃ ℄ ℅ ℆ ℇ ℈ ℉ ℊ ℋ ℌ ℍ ℎ ℏ ℐ ℑ ℒ ℓ ℔ ℕ № ℗ ℘ ℙ ℚ ℛ ℜ ℝ ℞ ℟ ℠ ℡ ™ ℣ ℤ ℥ Ω ℧ ℨ ℩ K Å ℬ ℭ ℮ ℯ ℰ ℱ Ⅎ ℳ ℴ ℵ ℶ ℷ ℸ  ℺ ℻ ℼ ℽ ℾ ℿ ⅀ ⅁ ⅂ ⅃ ⅄ ⅅ ⅆ ⅇ ⅈ ⅉ ⅊ ⅋ ⅌ ⅍ ⅎ ⅏ ⅐ ⅑ ⅒ ⅓ ⅔ ⅕ ⅖ ⅗ ⅘ ⅙ ⅚ ⅛ ⅜ ⅝ ⅞ ↀ ↁ ↂ Ↄ ↉ ↊ ↋ ← ↑ → ↓  ↚ ↛ ↜ ↝ ↞ ↟ ↠ ↡ ↢ ↣ ↤ ↥ ↦ ↧ ↨  ↫ ↬ ↭ ↮ ↯ ↰ ↱ ↲ ↳ ↴ ↵ ↶ ↷ ↸ ↹ ↺ ↻ ↼ ↽ ↾ ↿ ⇀ ⇁ ⇂ ⇃ ⇄ ⇅ ⇆ ⇇ ⇈ ⇉ ⇊ ⇋ ⇌ ⇍ ⇎ ⇏ ⇐ ⇑ ⇒ ⇓ ⇔ ⇕ ⇖ ⇗ ⇘ ⇙ ⇚ ⇛ ⇜ ⇝ ⇞ ⇟ ⇠ ⇡ ⇢ ⇣ ⇤ ⇥ ⇦ ⇧ ⇨ ⇩ ⇪ ⇫ ⇬ ⇭ ⇮ ⇯ ⇰ ⇱ ⇲ ⇳ ⇴ ⇵ ⇶ ⇷ ⇸ ⇹ ⇺ ⇻ ⇼ ⇽ ⇾ ⇿ ∀ ∁ ∂ ∃ ∄ ∅ ∆ ∇ ∈ ∉ ∊ ∋ ∌ ∍ ∎ ∏ ∐ ∑ − ∓ ∔ ∕ ∖ ∗ ∘ ∙ √ ∛ ∜ ∝ ∞ ∟ ∠ ∡ ∢ ∣ ∤ ∥ ∦ ∧ ∨ ∩ ∪ ∫ ∬ ∭ ∮ ∯ ∰ ∱ ∲ ∳ ∴ ∵ ∶ ∷ ∸ ∹ ∺ ∻ ∼ ∽ ∾ ∿ ≀ ≁ ≂ ≃ ≄ ≅ ≆ ≇ ≈ ≉ ≊ ≋ ≌ ≍ ≎ ≏ ≐ ≑ ≒ ≓ ≔ ≕ ≖ ≗ ≘ ≙ ≚ ≛ ≜ ≝ ≞ ≟ ≠ ≡ ≢ ≣ ≤ ≥ ≦ ≧ ≨ ≩ ≪ ≫ ≬ ≭ ≮ ≯ ≰ ≱ ≲ ≳ ≴ ≵ ≶ ≷ ≸ ≹ ≺ ≻ ≼ ≽ ≾ ≿ ⊀ ⊁ ⊂ ⊃ ⊄ ⊅ ⊆ ⊇ ⊈ ⊉ ⊊ ⊋ ⊌ ⊍ ⊎ ⊏ ⊐ ⊑ ⊒ ⊓ ⊔ ⊕ ⊖ ⊗ ⊘ ⊙ ⊚ ⊛ ⊜ ⊝ ⊞ ⊟ ⊠ ⊡ ⊢ ⊣ ⊤ ⊥ ⊦ ⊧ ⊨ ⊩ ⊪ ⊫ ⊬ ⊭ ⊮ ⊯ ⊰ ⊱ ⊲ ⊳ ⊴ ⊵ ⊶ ⊷ ⊸ ⊹ ⊺ ⊻ ⊼ ⊽ ⊾ ⊿ ⋀ ⋁ ⋂ ⋃ ⋄ ⋅ ⋆ ⋇ ⋈ ⋉ ⋊ ⋋ ⋌ ⋍ ⋎ ⋏ ⋐ ⋑ ⋒ ⋓ ⋔ ⋕ ⋖ ⋗ ⋘ ⋙ ⋚ ⋛ ⋜ ⋝ ⋞ ⋟ ⋠ ⋡ ⋢ ⋣ ⋤ ⋥ ⋦ ⋧ ⋨ ⋩ ⋪ ⋫ ⋬ ⋭ ⋮ ⋯ ⋰ ⋱ ⋲ ⋳ ⋴ ⋵ ⋶ ⋷ ⋸ ⋹ ⋺ ⋻ ⋼ ⋽ ⋾ ⋿ ⌀ ⌁ ⌂ ⌃ ⌄ ⌅ ⌆ ⌇ ⌈ ⌉ ⌊ ⌋ ⌌ ⌍ ⌎ ⌏ ⌐ ⌑ ⌒ ⌓ • ⌕ ⌖ ⌗ ⌘ ⌙  ⌛️ ⌜ ⌝ ⌞ ⌟ ⌠ ⌡ ⌢ ⌣ ⌤ ⌥ ⌦ ⌧ ⌨️ 〈 〉 ⌫ ⌬ ⌭ ⌮ ⌯ ⌰ ⌱ ⌲ ⌳ ⌴ ⌵ ⌶ ⌷ ⌸ ⌹ ⌺ ⌻ ⌼ ⌽ ⌾ ⌿ ⍀ ⍁ ⍂ ⍃ ⍄ ⍅ ⍆ ⍇ ⍈ ⍉ ⍊ ⍋ ⍌ ⍍ ⍎ ⍏ ⍐ ⍑ ⍒ ⍓ ⍔ ⍕ ⍖ ⍗ ⍘ ⍙ ⍚ ⍛ ⍜ ⍝ ⍞ ⍟ ⍠ ⍡ ⍢ ⍣ ⍤ ⍥ ⍦ ⍧ ⍨ ⍩ ⍪ ⍫ ⍬ ⍭ ⍮ ⍯ ⍰ ⍱ ⍲ ⍳ ⍴ ⍵ ⍶ ⍷ ⍸ ⍹ ⍺ ⍻ ⍼ ⍽ ⍾ ⍿ ⎀ ⎁ ⎂ ⎃ ⎄ ⎅ ⎆ ⎇ ⎈ ⎉ ⎊ ⎋ ⎌ ⎍ ⎎ ⎏ ⎐ ⎑ ⎒ ⎓ ⎔ ⎕ ⎖ ⎗ ⎘ ⎙ ⎚ ⎛ ⎜ ⎝ ⎞ ⎟ ⎠ ⎡ ⎢ ⎣ ⎤ ⎥ ⎦ ⎧ ⎨ ⎩ ⎪ ⎫ ⎬ ⎭ ⎮ ⎯ ⎰ ⎱ ⎲ ⎳ ⎴ ⎵ ⎶ ⎷ ⎸ ⎹ ⎺ ⎻ ⎼ ⎽ ⎾ ⎿ ⏀ ⏁ ⏂ ⏃ ⏄ ⏅ ⏆ ⏇ ⏈ ⏉ ⏋ ⏌ ⏍ ⏎  ⏐ ⏑ ⏒ ⏓ ⏔ ⏕ ⏖ ⏗ ⏘ ⏙ ⏚ ⏛ ⏜ ⏝ ⏞ ⏟ ⏠ ⏡ ⏢ ⏣ ⏤ ⏥ ⏦ ␋ ␢ ␣ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ⑴ ⑵ ⑶ ⑷ ⑸ ⑹ ⑺ ⑻ ⑼ ⑽ ⑾ ⑿ ⒀ ⒁ ⒂ ⒃ ⒄ ⒅ ⒆ ⒇ ⒈ ⒉ ⒊ ⒋ ⒌ ⒍ ⒎ ⒏ ⒐ ⒑ ⒒ ⒓ ⒔ ⒕ ⒖ ⒗ ⒘ ⒙ ⒚ ⒛ ⒜ ⒝ ⒞ ⒟ ⒠ ⒡ ⒢ ⒣ ⒤ ⒥ ⒦ ⒧ ⒨ ⒩ ⒪ ⒫ ⒬ ⒭ ⒮ ⒯ ⒰ ⒱ ⒲ ⒳ ⒴ ⒵ Ⓐ Ⓑ Ⓒ Ⓓ Ⓔ Ⓕ Ⓖ Ⓗ Ⓘ Ⓙ Ⓚ Ⓛ  Ⓝ Ⓞ Ⓟ Ⓠ Ⓡ Ⓢ Ⓣ Ⓤ Ⓥ Ⓦ Ⓧ Ⓨ Ⓩ ⓐ ⓑ ⓒ ⓓ ⓔ ⓕ ⓖ ⓗ ⓘ ⓙ ⓚ ⓛ ⓜ ⓝ ⓞ ⓟ ⓠ ⓡ ⓢ ⓣ ⓤ ⓥ ⓦ ⓧ ⓨ ⓩ ⓪ ⓫ ⓬ ⓭ ⓮ ⓯ ⓰ ⓱ ⓲ ⓳ ⓴ ⓵ ⓶ ⓷ ⓸ ⓹ ⓺ ⓻ ⓼ ⓽ ⓾ ⓿ ─ ━ │ ┃ ┄ ┅ ┆ ┇ ┈ ┉ ┊ ┋ ┌ ┍ ┎ ┏ ┐ ┑ ┒ ┓ └ ┕ ┖ ┗ ┘ ┙ ┚ ┛ ├ ┝ ┞ ┟ ┠ ┡ ┢ ┣ ┤ ┥ ┦ ┧ ┨ ┩ ┪ ┫ ┬ ┭ ┮ ┯ ┰ ┱ ┲ ┳ ┴ ┵ ┶ ┷ ┸ ┹ ┺ ┻ ┼ ┽ ┾ ┿ ╀ ╁ ╂ ╃ ╄ ╅ ╆ ╇ ╈ ╉ ╊ ╋ ╌ ╍ ╎ ╏ ═ ║ ╒ ╓ ╔ ╕ ╖ ╗ ╘ ╙ ╚ ╛ ╜ ╝ ╞ ╟ ╠ ╡ ╢ ╣ ╤ ╥ ╦ ╧ ╨ ╩ ╪ ╫ ╬ ╬﹌ ╭ ╮ ╯ ╰ ╰☆╮ ╱ ╲ ╳ ╴ ╵ ╶ ╷ ╸ ╹ ╺ ╻ ╼ ╽ ╾ ╿ ▀ ▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▉ ▊ ▋ ▌ ▍ ▎ ▏ ▐ ░ ▒ ▓ ▔ ▕ ▖ ▗ ▘ ▙ ▚ ▛ ▜ ▝ ▞ ▟ ■ □ ▢ ▣ ▤ ▥ ▦ ▧ ▨ ▩ ▪️ ▫️ ▬ ▭ ▮ ▯ ▰ ▱ ▲ △ ▴ ▵ ▷ ▸ ▹ ► ▻ ▼ ▽ ▾ ▿  ◁ ◂ ◃ ◄ ◅ ◆ ◇ ◈ ◉ ◊ ○ ◌ ◍ ◎ ● ◐ ◑ ◒ ◓ ◔ ◔ʊ ◕ ◖ ◗ ◘ ◙ ◚ ◛ ◜ ◝ ◞ ◟ ◠ ◡ ◢ ◣ ◤ ◥ ◦ ◧ ◨ ◩ ◪ ◫ ◬ ◭ ◮ ◯ ◰ ◱ ◲ ◳ ◴ ◵ ◶ ◷ ◸ ◹ ◺  ☓ ☰ ☱ ☲ ☳ ☴ ☵ ☶ ☷  ♡ ♢   ♰ ♱  ⚆   ⚊ ⚋ ⚌ ⚍ ⚎ ⚏  ✐ ✑  ✓ ✔️ ✕ ✖️ ✗ ✘ ✙ ✚ ✛ ✜  ✞ ✟ ✠ ✢ ✣ ✤ ✥ ✦ ✧ ✧♱ ✩ ✪ ✫ ✬ ✭ ✮ ✯ ✰ ✱ ✲  ✵ ✶ ✷ ✸ ✹ ✺ ✻ ✼ ✽ ✾ ✿ ❀ ❁ ❂ ❃ ❅ • ❈ ❉ ❊ ❋ ❍ ❏ ❐ ❑ ❒ ❖  ❘ ❙ ❚ ❛ ❜ ❝ ❞ ❡ ❢ ❥ ❦ ❧ ❨ ❩ ❪ ❫ ❬ ❭ ❮ ❯ ❰ ❱ ❲ ❳ ❴ ❵ ❶ ❷ ❸ ❹ ❺ ❻ ❼ ❽ ❾ ❿ ➀ ➁ ➂ ➃ ➄ ➅ ➆ ➇ ➈ ➉ ➊ ➋ ➌ ➍ ➎ ➏ ➐➑ ➒ ➓ ➔ ➘ ➙ ➚ ➛ ➜ ➝ ➞ ➟ ➠  ➢ ➣ ➤ ➥ ➦ ➧ ➨ ➩ ➪ ➫ ➬ ➭ ➮ ➯ ➱ ➲ ➳ ➴ ➵ ➶ ➷ ➸ ➹ ❀  ➻ ➼ ➽ ➾ ⟀ ⟁ ⟂ ⟃ ⟄ ⟇ ⟈ ⟉ ⟊ ⟐ ⟑ ⟒ ⟓ ⟔ ⟕ ⟖ ⟗ ⟘ ⟙ ⟚ ⟛ ⟜ ⟝ ⟞ ⟟ ⟠ ⟡ ⟢ ⟣ ⟤ ⟥ ⟦ ⟧ ⟨ ⟩ ⟪ ⟫ ⟰ ⟱ ⟲ ⟳ ⟴ ⟵ ⟶ ⟷ ⟸ ⟹ ⟺ ⟻ ⟼ ⟽ ⟾ ⟿ ⤀ ⤁ ⤂ ⤃ ⤄ ⤅ ⤆ ⤇ ⤈ ⤉ ⤊ ⤋ ⤌ ⤍ ⤎ ⤏ ⤐ ⤑ ⤒ ⤓ ⤔ ⤕ ⤖ ⤗ ⤘ ⤙ ⤚ ⤛ ⤜ ⤝ ⤞ ⤟ ⤠ ⤡ ⤢ ⤣ ⤤ ⤥ ⤦ ⤧ ⤨ ⤩ ⤪ ⤫ ⤬ ⤭ ⤮ ⤯ ⤰ ⤱ ⤲ ⤳ ⤶ ⤷ ⤸ ⤹ ⤺ ⤻ ⤼ ⤽ ⤾ ⤿ ⥀ ⥁ ⥂ ⥃ ⥄ ⥅ ⥆ ⥇ ⥈ ⥉ ⥊ ⥋ ⥌ ⥍ ⥎ ⥏ ⥐ ⥑ ⥒ ⥓ ⥔ ⥕ ⥖ ⥗ ⥘ ⥙ ⥚ ⥛ ⥜ ⥝ ⥞ ⥟ ⥠ ⥡ ⥢ ⥣ ⥤ ⥥ ⥦ ⥧ ⥨ ⥩ ⥪ ⥫ ⥬ ⥭ ⥮ ⥯ ⥰ ⥱ ⥲ ⥳ ⥴ ⥵ ⥶ ⥷ ⥸ ⥹ ⥺ ⥻ ⥼ ⥽ ⥾ ⥿ ⦀ ⦁ ⦂ ⦃ ⦄ ⦅ ⦆ ⦇ ⦈ ⦉ ⦊ ⦋ ⦌ ⦍ ⦎ ⦏ ⦐ ⦑ ⦒ ⦓ ⦔ ⦕ ⦖ ⦗ ⦘ ⦙ ⦚ ⦛ ⦜ ⦝ ⦞ ⦟ ⦠ ⦡ ⦢ ⦣ ⦤ ⦥ ⦦ ⦧ ⦨ ⦩ ⦪ ⦫ ⦬ ⦭ ⦮ ⦯ ⦰ ⦱ ⦲ ⦳ ⦴ ⦵ ⦶ ⦷ ⦸ ⦹ ⦺ ⦻ ⦼ ⦽ ⦾ ⦿ ⧀ ⧁ ⧂ ⧃ ⧄ ⧅ ⧆ ⧇ ⧈ ⧉ ⧊ ⧋ ⧌ ⧍ ⧎ ⧏ ⧐ ⧑ ⧒ ⧓ ⧔ ⧕ ⧖ ⧗ ⧘ ⧙ ⧚ ⧛ ⧜ ⧝ ⧞ ⧟ ⧡ ⧢ ⧣ ⧤ ⧥ ⧦ ⧧ ⧨ ⧩ ⧪ ⧫ ⧬ ⧭ ⧮ ⧯ ⧰ ⧱ ⧲ ⧳ ⧴ ⧵ ⧶ ⧷ ⧸ ⧹ ⧺ɷ") 


@Client.on_message(filters.command("اشهر مزغرفة$", prefixes=f".") & filters.me)
async def ahhowr(c, msg):
    await msg.edit(
        "-₁₉₉₀\n-₁₉₉₁\n-₁₉₉₂\n-₁₉₉₃\n -₁₉₉₄\n-₁₉₉₅\n -₁₉₉₆\n -₁₉₉₇\n-₁₉₉₈\n-₁₉₉₉\n -₂₀₀₀\n -₂₀₀₁\n -₂₀₀₂\n -₂₀₀₃\n-₂₀₀₄\n -₂₀₀₅-\n -₂₀₀₆\n -₂₀₀₇\n---\n-𝒋𝒂𝒏𝒖𝒂𝒓𝒚.💞\n -𝒇𝒆𝒃𝒓𝒖𝒂𝒓𝒚.💞\n  -𝒎𝒂𝒓𝒄𝒉.💞\n 𝒂𝒑𝒓𝒊𝒍.💞\n -𝒎𝒂𝒚.💞\n -𝒋𝒖𝒏𝒆.💞\n -𝒋𝒖𝒍𝒚.💞\n -𝒂𝒖𝒈𝒖𝒔𝒕 .💞\n -𝒔𝒆𝒑𝒕𝒆𝒎𝒃𝒆𝒓 .💞\n-𝒐𝒄𝒕𝒐𝒃𝒆𝒓.💞\n-𝒏𝒐𝒗𝒆𝒎𝒃𝒆𝒓.💞\n-𝒅𝒆𝒄𝒆𝒎𝒃𝒆𝒓.💞\n------\n-𝐒𝐔𝐍𝐃𝐀𝐘.♡\n -𝐌𝐎𝐍𝐃𝐀𝐘.♡\n -𝐓𝐔𝐄𝐒𝐃𝐀𝐘.♡\n-𝐖𝐄𝐃𝐍𝐄𝐒𝐃𝐀𝐘.♡\n𝐓𝐇𝐔𝐑𝐒𝐃𝐀𝐘.♡\n -𝐅𝐑𝐈𝐃𝐀𝐘.♡\n -𝐒𝐀𝐓𝐔𝐑𝐃𝐀𝐘.♡") 
        
        
@Client.on_message(filters.command("المواليد$", prefixes=f".") & filters.me)
async def mwaled(c, msg):
    await msg.edit(
        "₁₉₉₅\n₁₉₉₆\n₁₉₉₇\n₁₉₉₈\n₁₉₉₉\n₂₀₀₀\n₂₀₀₁\n₂₀₀₂\n₂₀₀₃") 
                
      
@Client.on_message(filters.command("بايو1$", prefixes=f".") & filters.me)
async def bioo(c, msg):
    await msg.edit(
        "☁️ : 🕊\n☁️ :   ✨\n☁️ :   🤍\n\n بريئۃ ۿي، بصورۿ لطيفۃ ڪالاطفال🎀") 
        
        
@Client.on_message(filters.command("بايو2$", prefixes=f".") & filters.me)
async def boio(c, msg):
    await msg.edit(
        "☘️ 💕\n☘️ 💕\n☘️ 💕\n☘️ دمت لي شيئاً جميلاً لا ينتهي💕")


@Client.on_message(filters.command("بايو3$", prefixes=f".") & filters.me)
async def bozi(c, msg):
    await msg.edit(
        "𓋜┊𓆩 ➝  ˛⁽🇮🇶₎⇣ 𓆪\n𓋜┊𓆩  𓆪\n𓋜┊𓆩  𓆪\n𓋜┊𓆩  𓆪\n𓋜┊𓆩 ﭑميرۿ ـلآ يُليق بها ﭑلانحنا🍂 𓆪\n⁞ ωєℓ¢σмє тo му ρяσƒιℓє ⁞") 


@Client.on_message(filters.command("بايو4$", prefixes=f".") & filters.me)
async def slam(c, msg):
    await msg.edit(
        "🜟 ↬ ᑎᗩᗰE ، • •😌❤️\n🜟 ↬ ᖴᖇOᗰ ، Ҽɠყρƚ 🇮\n🜟 ↬ ᗩGE ، y.o ♥️.\n\n🧿🍃  .....  🧿🍃.") 
        
 
@Client.on_message(filters.command("البايو$", prefixes=f".") & filters.me)
async def tarq(c, msg):
    await msg.edit(
        "**⎈ ⦙  - 𝑩𝑰𝑶 𝑳𝑰𝑺𝑻 : **\n•━═━═━═『ٓ᥆』═━═━═━•\n **⎈ ⦙  قائـمه البايو :** \n⎈ ⦙  `.بايو1 ` \n⎈ ⦙  `.بايو2` \n⎈ ⦙  `.بايو3 ` \n⎈ ⦙  `.بايو4 ` \n⎈ ⦙  `.بايو5` \n•━═━═━═『ٓ᥆』═━═━═━•")   


@Client.on_message(filters.command("قنوات$", prefixes=f".") & filters.me)
async def kanwat(c, msg):
    await msg.edit(
        "𝙁𝙍𝘼𝙉𝘾𝙊𝙄𝙎 𝟐𝟎𝟐𝟏 🎄꙳.\n𝙆𝙀𝙑𝙄𝙉 𝟐𝟎𝟐𝟏 🎄꙳.\n𝘼𝙉𝙇𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n𝘾𝙃𝙄𝙏𝙏𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n𝙎𝘼𝙑𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n𝘾𝙃𝙄𝘾𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n𝘾𝙃𝙄𝘾𝘼𝙂𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n𝙀𝘾𝙃𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n𝙔𝘼𝙔𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n𝙈𝘼𝙍𝘾𝙀𝙑𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n𝙔𝙄𝙎𝙆𝘼 𝟐𝟎𝟐𝟏 🎄꙳.\n﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎\n𝐌𝐈𝐋𝐀𝐍 🌵\n𝐀𝐍𝐈𝐒𝐀𝐔 🌵\n𝐅𝐑𝐀𝐍𝐂𝐈𝐒𝐎 🌵\n𝐀𝐏𝐑𝐈𝐋  🌵\n𝙛𝙞𝙘𝙤 🎄\n﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎\n𝙞𝙨𝙝𝙤 🎄\n𝙖𝙗𝙧𝙖𝙨 🎄\n*..⌠𝐒𝐞𝐥𝐯𝐚𝐧𝐚⌡𓊑.\n..⌠𝐓𝐨𝐛𝐚𝐤⌡𓊑.\n..⌠𝐄𝐥𝐤𝐚𝐫⌡𓊑.\n..⌠𝐌𝐚𝐲𝐚⌡𓊑.\n..⌠𝐓𝐞𝐨𝐨⌡𓊑.\n﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎\n..⌠𝐌𝐞𝐚⌡𓊑.\n..⌠𝐋𝐞𝐥𝐞⌡𓊑.\n⌯ ˹𝙆𝙖𝙧𝙖˼ \n⌯ ˹𝙉𝙖𝙖𝙧˼ \n⌯ ˹𝙂𝙢𝙧˼ \n⌯ ˹𝘿𝙚𝙫˼\n⌯ ˹𝙀𝙫𝙖˼\n﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎\n:   ˹𝘾𝘼𝙍𝙊𝙇𝙄𝙉𝙀˼ 𓆪 .\n:   ˹𝘾𝙍𝙔𝙎𝙏𝘼𝙇˼ 𓆪 .\n:   ˹𝙇𝘼𝙐𝙍𝙀𝙉˼ 𓆪 .\n:   ˹𝙆𝘼𝙈𝙄𝙇𝘼˼ 𓆪 .\n:   ˹𝘿𝘼𝙉𝘼˼ 𓆪 .\n:   ˹𝙍𝙄𝙏𝘼˼ 𓆪 .") 


@Client.on_message(filters.command("شباب$", prefixes=f".") & filters.me)
async def shpap(c, msg):
    await msg.edit(
       "-𓆩𝗠𝗨𝗛𝗔𝗠𝗠𝗔𝗗.𖤐𓆪\n-𓆩𝗔𝗠𝗔𝗔𝗥.𖤐𓆪\n-𓆩𝗔𝗬𝗔𝗗.𖤐𓆪\n-𓆩𝗠𝗔𝗟𝗘𝗞.𖤐𓆪\n-𓆩𝗥𝗔𝗙𝗜𝗗.𖤐𓆪\n-𓆩𝗦𝗕𝗔𝗛.𖤐??\n-𓆩𝗔𝗕𝗔𝗦.𖤐𓆪\n-𓆩𝗛𝗔𝗕𝗜𝗕.𖤐𓆪\n┉ ┉ ┉ ┉ ┉\n⌯『𝐀𝐋𝐈』𖤍᭄𓄹\n⌯『𝐋𝐁𝐍𝐀 』𖤍᭄𓄹\n⌯『𝐀𝐒𝐄𝐄𝐋』𖤍᭄𓄹\n⌯『𝐒𝐇𝐄𝐑𝐄𝐍』𖤍᭄𓄹\n⌯『𝐌𝐔𝐒𝐓𝐀𝐅𝐀』𖤍᭄𓄹\n┉ ┉ ┉ ┉ ┉\n𓆩𝒌𝒉𝒂𝒍𝒆𝒅?? ??.\n𓆩𝑯𝒂𝒛𝒂𝒎𓆪 🖤.\n𓆩𝑶𝒎𝒂𝒓𓆪 🖤.\n𓆩𝑯𝒂𝒕𝒂𝒎𓆪 🖤.\n𓆩𝑶𝒔𝒂𝒎𝒂𓆪 🖤.\n𓆩??𝒂𝒅𝒐𓆪 🖤.\n𓆩𝑯𝒂𝒊𝒅𝒂𝒓𓆪 🖤.\n𓆩𝑮𝒉𝒂𝒍𝒆𝒃𓆪 🖤.\n??𝑨𝒌𝒓𝒂𝒎𓆪 🖤.\n𓆩𝑨𝒌𝒓𝒂𝒎𓆪 🖤.\n𓆩𝒗𝒊𝒓𝒐𝒔𓆪 🖤.\n「𝘋𝘮𝘢𝘳 𐃣.")


@Client.on_message(filters.command("بنات$", prefixes=f".") & filters.me)
async def banat(c, msg):
    await msg.edit( 
       "•˹𝙻𝚈𝙽𝙽˼⛈💞.\n•˹𝙽𝙾𝙾᥆˼⛈💞.\n•˹𝚂𝙰𝙼𝙰᥆˼⛈💞.\n•˹𝙽𝙾᥆𝙷𝙰𝙽˼⛈💞.\n•˹𝚂𝙰𝙱᥆𝙴𝙴𝙽˼⛈💞.\n•𝙼𝙰᥆𝚈𝙰𝙼⋆  🧚🏻‍♀♥️ .\n•𝙱𝙰𝚃𝙾𝙻⋆ 🧚🏻‍♀♥️ .\n•𝚉𝙰𝙷᥆𝙰𝙰⋆  🧚🏻‍♀♥️ .\n𓂐 𝙍𝘼𝙕𝘼𝙉 𖠛.\n𖥻 𓆩𝙍𝙚𝙚𝙢𓆪،𖤍\n𓂐 𝙀𝙈𝙀𝙇𝙔 𖠛 .\n- 𝙏 𝙊 𝙏 𝘼 : 🇺🇸Ꮠ\n⌯ ˹ѕᴀʀᴀ˼ ❀ .\n- 𝙎 𝘼 𝙉 𝘿 𝙍 𝙄 𝙇 𝘼 : 🇺🇸Ꮠ\n- 𝙍 𝘽 𝘼 𝙉 𝙕 𝙇 : 🇺🇸Ꮠ\n- 𝙆 𝘼 𝘿 𝙄 𝘼 : 🇺🇸Ꮠ\n𖥻 𓆩𝙉𝙤𝙨𝙖𓆪،𖤍") 


@Client.on_message(filters.command(["م10$", "اوامر الزغرفة$"], prefixes=f".") & filters.me)
async def tota(c, msg):
    await msg.edit(
        "•━═━═━═『ٓ᥆』═━═━═━•\n **⎈ ⦙  قائـمه اوامر الزغرفه :** \n⎈ ⦙  `.المواليد ` \n⎈ ⦙  `.اشهر مزغرفة` \n⎈ ⦙  `.البايو` \n⎈ ⦙  `.قنوات` \n⎈ ⦙  `.الرموز` \n⎈ ⦙  `.اسماء` \n [Ⴆ᥆ƚ ᖇᎥ᥆](http://t.me/S_ll_A_bot)\n•━═━═━═『ٓ᥆』═━═━═━•") 


@Client.on_message(filters.command(["اوامري$", "اوامر السورس$"], prefixes=f".") & filters.me)
async def more(c, msg):
    await msg.edit("""
⦇ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐎𝐑𝐒𝐄  ⦈
❀   اوامر الخاص ⤝ ⦗ .م1 ⦘
❀   اوامر المجموعات ⤝ ⦗ .م2 ⦘
❀   اوامر اليوتيوب ⤝ ⦗ .م3 ⦘
❀   اوامر الاذاعه ⤝ ⦗ .م4 ⦘
❀   اوامر الرفع ⤝ ⦗ .م5 ⦘
❀   اوامر النسب ⤝ ⦗ .م6 ⦘
❀   اوامر اضافيه  ⤝ ⦗ .م7 ⦘
❀  اوامر التسلية 1 ⤝ ⦗ .م8 ⦘
❀  اوامر التسلية 2 ⤝ ⦗ .م9 ⦘
❀   اوامر الزخرفه ⤝ ⦗ .م10 ⦘
❀   اوامر المميز ⤝ ⦗ .م11 ⦘
❀  اوامر الفارات ⤝ ⦗ .م12 ⦘
❀   اوامر التوقيت ⤝ ⦗ .م13 ⦘ 
❀   اوامر الالعاب ⤝ ⦗ .م14 ⦘
❀  اوامر التسليه والكاركتير ⤝ ⦗ .م15 ⦘
❀   اوامر الوقتيه ⤝ ⦗ .م 16 ⦘
❀   اوامر الكتابه والخط⤝ ⦗ .م17⦘
❀   اوامر التخزين ⤝ ⦗ .م18 ⦘ 
❀  اوامر الاستيكر والمتحركه ⤝ ⦗ .م19 ⦘
❀  اضافات جديده ⤝⦗ .م20 ⦘
❀  اوامر االمساعده ⤝⦗ .م21 ⦘
❀  اوامر التحميل والترجمه ⤝⦗ .م22 ⦘
❀  اوامر الاستيت ⤝⦗ .م23 ⦘
❀  اوامر الحمايه ⤝⦗ .م24 ⦘
❀  اوامر الكول  ⤝⦗ .م25 ⦘
❀  اوامر الحساب  ⤝⦗ .م26 ⦘

◉ جميع الاوامر تكون بدايتها نقطة .

""")


@Client.on_message(filters.command(["م18$", "اوامر السورس$"], prefixes=f".") & filters.me)
async def takzen(c, msg):
    await msg.edit("""
⦑  اوامر التخزين  ⦒  :
———————×———————
الأمر ⦙ ( .تعين الجروب +ايدي الجروب )
شرح : يقوم بتغيير جروب التخزين لجروب جديد مثال
تعين الجروب -100165331262829
———————×———————
""")

@Client.on_message(filters.command(["م25$", "اوامر الكول$"], prefixes=f".") & filters.me)
async def takzen(c, msg):
    await msg.edit("""
⦑  اوامر الكول ⦒  :
———————×———————
الأمر : ‹ .افتح الكول ›
شرح : تقوم بكتابة الامر لفتح الكول بالمحادثه 
———×———×———×———×——
الأمر : ‹ .اقفل الكول ›
شرح : تقوم بكتابة الامر لقفل الكول بالمحادثه 
———×———×———×———×——
الأمر : ‹ .مين في الكول ›
شرح : تقوم بكتابة الامر لاظهار قائمة بالاشخاص الوجودين بالكول   
———×———×———×———×——
الأمر : ‹ .بث ›
شرح : تقوم بكتابة الامر للحصول ع رابط البث الخاص بالكول واستخدامه ف الاستريم   
———×———×———×———×——
""")

@Client.on_message(filters.command(["م24$", "اوامر الحمايه$"], prefixes=f".") & filters.me)
async def takzen(c, msg):
    await msg.edit("""
⦑  اوامر الحمايه ⦒  :
———————×———————
📽 قفل الفيديو _ فتح الفيديو ←لمنع الفيديوهات 
———×———×———×———×——
 🖼 قفل الصور _ فتح الصور ←لمنع الصور
 ———×———×———×———×——
 🔁 قفل التوجيه _ فتح التوجيه ←لمنع التوجيهات او التحويلات
 ———×———×———×———×——
 🎆 قفل الملصقات _ فتح الملصقات ←لمنع الملصقات
 ———×———×———×———×——
 🌐 قفل الروابط _ فتح الروابط ←لمنع الروابط
 ———×———×———×———×——
 🔞 قفل السب _ فتح السب ←لمنع السب
 ———×———×———×———×——
🌀 قفل المنشن _ فتح المنشن ← لمنع المنشن @
———×———×———×———×——
""")


@Client.on_message(filters.command(["م26$", "اوامر الحساب$"], prefixes=f".") & filters.me)
async def takzen(c, msg):
    await msg.edit("""
⦑  اوامر الحساب ⦒  :
⦁              ﹎﹎﹎﹎﹎﹎﹎﹎            ⦁ 

❀  الامر ⦂ ⦗

- الاوامر :
• احصائيات الحساب : بيعرض احصائيات حسابك
• تصفيه القنوات : دا بيخرجك من كل القنوات الي ف الحساب
• تصفيه الجروبات : دا بيخرجك من كل الجروبات
• تصفيه الحسابات المحذوفه : بيمسح شاتات الحسابات المحذوفه
• تصفيه الشاتات : بيمسح شاتات البرايفت كلها
• تصفيه البوتات : بيصفي شاتات البوتات
• طير : بيمسح الشات ( في البرايفت )
• طير + ريب : بيمسح الشات ( في الجروب ) ⦘

⦁               ﹎﹎﹎﹎﹎﹎﹎﹎          ⦁
""")

@Client.on_message(filters.command(["م15$", "اوامر التسليه والكاريكتر $"], prefixes=f".") & filters.me)
async def karektr(c, msg):
    await msg.edit("""
⦁            ﹎﹎﹎﹎﹎﹎﹎﹎              ⦁

⧉ اوامـر التسليـه والكاريكتـر ⦂
◉ نادم 
◉ مصه 
◉ سبونج 
◉ كلبي 
◉ خنزير 
◉ معصب 
◉ فيل 
◉ ثعلب 
◉ صدمه 
◉ جميع الاوامر تكون بدايتها نقطة .
  ⦁           ﹎﹎﹎﹎﹎﹎﹎﹎             ⦁
""") 
  
  
@Client.on_message(filters.command(["م14$", "اوامر الالعاب $"], prefixes=f".") & filters.me)
async def alabyw(c, msg):
    await msg.edit("""
⦁           ﹎﹎﹎﹎﹎﹎﹎﹎              ⦁

⧉ اوامر الالعاب في سورس هورس ⦂

◉ لعبة اكس او ⦂ قم بكتابه الامر .xo 

◉ لعبة ريفيرسي ⦂ قم بكتابة الامر ريفيرسي 

◉ جميع الاوامر تكون بدايتها نقطة .
⦁            ﹎﹎﹎﹎﹎﹎﹎﹎              ⦁
""") 
  

@Client.on_message(filters.command(["م13$", "اوامر التوقيت $"], prefixes=f".") & filters.me)
async def twke(c, msg):
    await msg.edit("""
⦁             ﹎﹎﹎﹎﹎﹎﹎﹎              ⦁

❀  الـوقـت الاسـاسي هـو وقـت مصـر
◉ يمكنك تغييره من خلال الاوامر التي في اسفل القائمه ⦂
❀  ⦗ .ضبط TIME_ZONE Africa/Cairo ⦘
◉ لضبط الوقت بتوقيت القاهره مصر

❀  ⦗ .ضبط TIME_ZONE Asia/Baghdad ⦘
◉ لضبط الوقت ع حسب توقيت العراق

❀  ⦗ .ضبط TIME_ZONE Asia/Damascus ⦘
◉ لضبط الوقت ع حسب توقيت سوريا

◉ جميع الاوامر تكون بدايتها نقطة .
⦁              ﹎﹎﹎﹎﹎﹎﹎﹎             ⦁
""") 
  
@Client.on_message(filters.command(["م20$", "اوامر التوقيت $"], prefixes=f".") & filters.me)
async def adafat(c, msg):
    await msg.edit("""
⦁              ﹎﹎﹎﹎﹎﹎﹎﹎            ⦁ 

⧉ الاضافات الجديده

❀  الامر ⦂ ⦗ منصه + المعرف ⦘
◉ الشرح ⦂ يقوم بجلب معلومات المعرف ما ان كان متاح للبيع او تم بيعه والسعر الذي تم بيعه به
◉ مثال منصه @H_0RSE

❀  الامر ⦂ ⦗ منع التصفيه ⦘
 ◉ الشرح ⦂ لحمايه مجموعتك او قناتك من التصفيه قم بترفع البوت الخاص بالتليثون في قناتك او مجموعتك

⦁               ﹎﹎﹎﹎﹎﹎﹎﹎          ⦁
""")

@Client.on_message(filters.command(["م19$", "اوامر التوقيت $"], prefixes=f".") & filters.me)
async def astekk(c, msg):
    await msg.edit("""
⦁             ﹎﹎﹎﹎﹎﹎﹎﹎             ⦁

⧉ اوامر الاستيكر والمتحركه

❀  استيكر ⦂ بالرد علي صوره او استيكر ثابت او متحرك
◉ الشرح ⦂ يقوم بعمل حزمه استيكر خاصه بك واضافه الاستيكر به

❀  اكتب ⦂ بالرد علي المتحركه 
◉ الشرح ⦂ لكتابة كلمه علي المتحركه gif
مثال اكتب هورس

⦁             ﹎﹎﹎﹎﹎﹎﹎﹎             ⦁
""") 
@Client.on_message(filters.command("الرموز$", prefixes=f".") & filters.me)
async def soska(c, msg):
    await msg.edit(
        "•━═━═━═『ٓ᥆』═━═━═━•\n **⎈ ⦙  قائـمه اوامر الرموز :** \n⎈ ⦙  `.رموز1 ` \n⎈ ⦙  `.رموز2` \n •━═━═━═『ٓ᥆』═━═━═━•") 


@Client.on_message(filters.command("اسماء$", prefixes=f".") & filters.me)
async def meraad(c, msg):
    await msg.edit(
        "•━═━═━═『ٓ᥆』═━═━═━•\n **⎈ قائـمه اوامر الاسماء :** \n⎈ ⦙ `.شباب ` \n⎈ ⦙  `.بنات` \n •━═━═━═『ٓ᥆』═━═━═━•") 

@Client.on_message(filters.command("زخرفه$", prefixes=f".") & filters.me)
async def botattt(c, msg):
    await msg.edit(
        "[َ𝗁َٰᥲ️ِّّꪔُِ᥆](http://t.me/S_ll_A_bot)")
        
@Client.on_message(filters.command("اجمد كده", prefixes=f".") & filters.me)
async def agmad(c, msg):    
     await msg.reply_voice("https://t.me/MemesVoices/33")        
     await msg.delete()
@Client.on_message(filters.command("يالهوي", prefixes=f".") & filters.me)
async def yalhowe(c, msg):    
     await msg.reply_voice("https://t.me/MemesVoices/35")      
     await msg.delete() 
@Client.on_message(filters.command("احترمي نفسك", prefixes=f".") & filters.me)
async def ehtrmy(c, msg):    
     await msg.reply_voice("https://t.me/MemesVoices/71")           
     await msg.delete()
@Client.on_message(filters.command("عيب", prefixes=f".") & filters.me)
async def eeeb(c, msg):    
     await msg.reply_voice("https://t.me/MemesVoices/66")          
     await msg.delete()
@Client.on_message(filters.command("مينفعش", prefixes=f".") & filters.me)
async def maynah(c, msg):    
     await msg.reply_voice("https://t.me/MemesVoices/58")  
     await msg.delete()
@Client.on_message(filters.command("مديك قلبي", prefixes=f".") & filters.me)
async def alby(c, msg):    
     await msg.reply_voice("https://t.me/MemesVoices/51")      
     await msg.delete()
@Client.on_message(filters.command("اهلا بيك", prefixes=f".") & filters.me)
async def ahlnbek(c, msg):    
     await msg.reply_voice("https://t.me/MemesVoices/52")      
     await msg.delete()
@Client.on_message(filters.command("هعوره", prefixes=f".") & filters.me)
async def hworo(c, msg):    
     await msg.reply_voice("https://t.me/MemesVoices/37")       
     await msg.delete()
@Client.on_message(filters.command("حفل", prefixes=f".") & filters.me)
async def kfel(c, msg):    
     await msg.reply_voice("https://t.me/MemesVoices/31")                
     await msg.delete()
@Client.on_message(filters.command("خد نفس", prefixes=f".") & filters.me)
async def nafs(c, msg):    
     await msg.reply_voice("https://t.me/MemesVoices/39")    
     await msg.delete()
@Client.on_message(filters.command("امال", prefixes=f".") & filters.me)
async def omal(c, msg):    
     await msg.reply_voice("https://t.me/MemesVoices/50")             
     await msg.delete()
@Client.on_message(filters.command("هتولعو", prefixes=f".") & filters.me)
async def yyleh(c, msg):        
     await msg.reply_voice("https://t.me/MemesVoices/67")    
     await msg.delete()                       
@Client.on_message(filters.command("انا تعبان", prefixes=f".") & filters.me)
async def taban(c, msg):        
     await msg.reply_voice("https://t.me/MemesVoices/62")    
     await msg.delete()
@Client.on_message(filters.command("عملت اي", prefixes=f".") & filters.me)
async def anaemlt(c, msg):    
     await msg.reply_voice("https://t.me/MemesVoices/65")         
     await msg.delete()
@Client.on_message(filters.command("المخدرات", prefixes=f".") & filters.me)
async def mokde(c, msg):
    await msg.reply_voice("https://t.me/MemesVoices/63")       
    await msg.delete()
@Client.on_message(filters.command("يا يمرا", prefixes=f".") & filters.me)
async def mrara(c, msg):    
     await msg.reply_voice("https://t.me/MemesVoices/55")  
     await msg.delete()
@Client.on_message(filters.command("بتحرجني", prefixes=f".") & filters.me)
async def aklak(c, msg):     
     await msg.reply_voice("https://t.me/MemesVoices/53")      
     await msg.delete()
@Client.on_message(filters.command("انضف", prefixes=f".") & filters.me)
async def endaf(c, msg):    
     await msg.reply_voice("https://t.me/MemesVoices/59")      
     await msg.delete()                                                                                                       
@Client.on_message(filters.command("هنضحك", prefixes=f".") & filters.me)
async def hantk(c, msg):    
     await msg.reply_voice("https://t.me/MemesVoices/61")      
     await msg.delete()
@Client.on_message(filters.command("يا راجل", prefixes=f".") & filters.me)
async def ragel(c, msg):       
     await msg.reply_voice("https://t.me/MemesVoices/64")           
     await msg.delete()    
@Client.on_message(filters.command("في رمضان", prefixes=f".") & filters.me)
async def rmdan(c, msg):       
     await msg.reply_voice("https://t.me/MemesVoices/72")           
     await msg.delete()
@Client.on_message(filters.command("م11$", prefixes=f".") & filters.me)
async def memess(c, msg):
    await msg.edit("""
⦁            ﹎﹎﹎﹎﹎﹎﹎﹎             ⦁

⦇ اوامر الميمز ⦈

◉ .امال  
◉ .خد نفس 
◉ .حفل 
◉ .اهلا بيك 
◉ .هعوره 
◉ .مديك قلبي 
◉ .مينفعش 
◉ .عيب 
◉ .احترمي نفسك 
◉ .اجمد كده 
◉ .يالهوي 
◉ .يا راجل 
◉ .هنضحك
◉ .انضف
◉ .بتحرجني
◉ .يا مرا
◉ .المخدرات
◉ .عملت اي
◉ .انا تعبان
◉ .هتولعو
◉ .في رمضان

◉ جميع الاوامر تكون بدايتها نقطة .

⦁             ﹎﹎﹎﹎﹎﹎﹎﹎            ⦁
""")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       