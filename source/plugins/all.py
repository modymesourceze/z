from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import Chat, User
from config import *
from asyncio import sleep
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
import re
from pyrogram import Client, filters
from pyrogram.types import Message
import random
import time
import random
from asyncio import gather
import os, time
from telegraph import upload_file
from os import remove
import time
from PIL import Image
from io import BytesIO
import wget
import asyncio
from asyncio import sleep
from pyrogram import Client, filters
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL

os.environ['TZ'] = 'Africa/Cairo'
time.tzset()


async def is_Admin(chat, id):
    admins = []
    async for m in app.get_chat_members(chat, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        admins.append(m.user.id)
    if id in admins:
        return True
    else:
        return False


async def send_pv(ay, text):
    async for ahmed in ay.get_dialogs():
        if ahmed.chat.type in {ChatType.PRIVATE, ChatType.BOT}:
            try:
                await ay.send_message(ahmed.chat.id, text)
            except FloodWait as e:
                await sleep(e.value)
                await sleep(7)
            except Exception as e:
                print(e)
                await sleep(5)
                pass


async def send_gp(ay, text):
    async for ahmed in ay.get_dialogs():
        if ahmed.chat.type in {ChatType.SUPERGROUP, ChatType.GROUP}:
            try:
                await ay.send_message(ahmed.chat.id, text)
            except FloodWait as e:
                await sleep(e.value)
                await sleep(7)
            except Exception as e:
                print(e)
                await sleep(5)
                pass


async def send_ch(ay, text):
    async for ahmed in ay.get_dialogs():
        if ahmed.chat.type == ChatType.CHANNEL:
            try:
                await ay.send_message(ahmed.chat.id, text)
            except FloodWait as e:
                await sleep(e.value)
                await sleep(7)
            except Exception as e:
                print(e)
                await sleep(5)
                pass


async def fwd_pv(ay, chat, msg):
    async for ahmed in ay.get_dialogs():
        if ahmed.chat.type in {ChatType.PRIVATE, ChatType.BOT}:
            try:
                await ay.forward_messages(ahmed.chat.id, chat, msg)
            except FloodWait as e:
                await sleep(e.value)
                await sleep(7)
            except Exception as e:
                print(e)
                await sleep(5)
                pass


async def fwd_gp(ay, chat, msg):
    async for ahmed in ay.get_dialogs():
        if ahmed.chat.type in {ChatType.SUPERGROUP, ChatType.GROUP}:
            try:
                await ay.forward_messages(ahmed.chat.id, chat, msg)
            except FloodWait as e:
                await sleep(e.value)
                await sleep(7)
            except Exception as e:
                print(e)
                await sleep(5)
                pass


async def fwd_ch(ay, chat, msg):
    async for ahmed in ay.get_dialogs():
        if ahmed.chat.type == ChatType.CHANNEL:
            try:
                await ay.forward_messages(ahmed.chat.id, chat, msg)
            except FloodWait as e:
                await sleep(e.value)
                await sleep(7)
            except Exception as e:
                print(e)
                await sleep(5)
                pass


@Client.on_message(filters.command("توجيه للخاص", prefixes=f".") & filters.me & filters.reply)
async def fwdpv(client, message):
    if message.reply_to_message.from_user.id in sudo_command:
        return await message.edit("☭ لا يمكنك استخدام الامر علي مبرمجين السورس")
    await message.edit("جاري التجهيز للاذاعة")
    text = message.reply_to_message.text
    if not text:
        return await message.edit("تاكد انك تقوم بي الرد علي نص")
    await message.edit(f"جاري عمل توجيه للخاص في الحساب")
    await fwd_pv(client, message.chat.id, message.reply_to_message.id)
    await message.edit("☭ تم عمل الاذاعه")

@Client.on_message(filters.command("استيك", prefixes=f".") & filters.me & filters.reply)
async def sticker_image(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.edit("الرد على ملصق.")
    if not reply.sticker:
        return await message.edit("الرد على ملصق.")
    m = await message.edit("يتم المعالجه..")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)])
    await m.delete()
    os.remove(f)
    
@Client.on_message(filters.command("توجيه للمجموعات", prefixes=f".") & filters.me & filters.reply)
async def fwdgp(client, message):
    if message.reply_to_message.from_user.id in sudo_command:
        return await message.edit("☭ لا يمكنك استخدام الامر علي مبرمجين السورس")
    await message.edit("جاري التجهيز للاذاعة")
    text = message.reply_to_message.text
    if not text:
        return await message.edit("تاكد انك تقوم بي الرد علي نص")
    await message.edit(f"جاري عمل توجيه للمجموعات في الحساب")
    await fwd_gp(client, message.chat.id, message.reply_to_message.id)
    await message.edit("☭ تم عمل الاذاعه")


@Client.on_message(filters.command("توجيه للقنوات", prefixes=f".") & filters.me & filters.reply)
async def fwdch(client, message):
    if message.reply_to_message.from_user.id in sudo_command:
        return await message.edit("☭ لا يمكنك استخدام الامر علي مبرمجين السورس")
    await message.edit("جاري التجهيز للاذاعة")
    text = message.reply_to_message.text
    if not text:
        return await message.edit("تاكد انك تقوم بي الرد علي نص")
    await message.edit(f"جاري عمل توجيه للقنوات في الحساب")
    await fwd_ch(client, message.chat.id, message.reply_to_message.id)
    await message.edit("☭ تم عمل الاذاعه")


@Client.on_message(filters.command("اذاعه", prefixes=f".") & filters.me & filters.reply)
async def send_chats(client, message):
    if message.reply_to_message.from_user.id in sudo_command:
        return await message.edit("☭ لا يمكنك استخدام الامر علي مبرمجين السورس")
    await message.edit("جاري التجهيز للاذاعة")
    mod = message.text.split("اذاعه", 1)[1]
    text = message.reply_to_message.text
    if not mod:
        return await message.edit("تاكد انك قمت بتحديد نوع الاذاعة")
    if not text:
        return await message.edit("تاكد انك تقوم بي الرد علي نص")
    await message.edit("جاري تحديد حساب الاذاعة")
    if re.search('خاص', mod):
        await message.edit(f"جاري عمل الاذاعة للخاص في الحساب")
        await send_pv(client, text)
        await message.edit("☭ تم عمل الاذاعه")
    elif re.search('جروبات', mod):
        await message.edit(f"جاري عمل الاذاعة للجروبات في الحساب ")
        await send_gp(client, text)
        await message.edit("☭ تم عمل الاذاعه")
    elif re.search('قنوات', mod):
        await message.edit(f"جاري عمل الاذاعة للقنوات في الحساب")
        await send_ch(client, text)
        await message.edit("☭ تم عمل الاذاعه")
    else:
        await message.edit("نوع الاذاعه غير صحيح")

@Client.on_message(filters.command("الاحصائيات", prefixes=".") & filters.me)
async def fraonhossam(client, message):
    cae_s_ar = 0
    hos1 = 0
    hos2 = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]:
            cae_s_ar += 1
        elif dialog.chat.type == ChatType.CHANNEL:
            hos1 += 1 
        elif dialog.chat.type in [ChatType.PRIVATE, ChatType.BOT]:
            hos2 += 1            
    await message.edit(f"اهلا عزيزي مالك الاك :  [{message.from_user.mention}] \n أنت مشترك في {cae_s_ar} جروب \n و {hos1} قناة \n و {hos2} شخص")

@Client.on_message(filters.command("جروباتي", prefixes=".") & filters.me)
async def my_groups(client, message):
    cae_s_ar = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]:
            cae_s_ar += 1
    await message.edit(f"اهلا عزيزي مالك الاك :  [{message.from_user.mention}] \n أنت مشترك في {cae_s_ar} جروب")  

@Client.on_message(filters.command("قنواتي", prefixes=".") & filters.me)
async def my_channel(client, message):
    hos1 = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == ChatType.CHANNEL:
            hos1 += 1
    await message.edit(f"اهلا عزيزي مالك الاك :  [{message.from_user.mention}]  \n  عدد قنوات هي {hos1} ")

@Client.on_message(filters.command("الاشخاص", prefixes=".") & filters.me)
async def my_private(client, message):
    hos2 = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in [ChatType.PRIVATE, ChatType.BOT]:
            hos2 += 1
    await message.edit(f"اهلا عزيزي مالك الاك :  [{message.from_user.mention}] \n  عدد الاشخاص هي {hos2} ")   
    
@Client.on_message(filters.command("مغادرة$", prefixes=f".") & filters.me )
async def leave_group(c,msg):
  await msg.edit("☭ يتم مغادرة المجموعه ....🕷")
  await asyncio.sleep(.5)
  await msg.edit("☭ تم مغادرة المجموعه بنجاح.🕷")
  await c.leave_chat(msg.chat.id)

@Client.on_message(filters.command("تليجراف$", prefixes=f".") & filters.me)
async def tgph(c, msg):
    if not msg.reply_to_message:
        await msg.edit("قم بي الرد علي الصورة اولا")
        return
    if not msg.reply_to_message.photo:
        await msg.edit("ادعم الصور فقط")
        return
    await msg.edit("جاري تحميل الصورة")
    await msg.reply_to_message.download("./YYYBR")
    await msg.edit("جاري رفع الصورة علي تلجراف")
    response = upload_file("./YYYBR")
    remove("./YYYBR")
    await msg.edit(f"تم الرفع و استخراج الرابط :- \n<code>https://telegra.ph{response[0]}</code>")


@Client.on_message(filters.command("اضف جهاتي$", prefixes=f".") & filters.me & filters.group)
async def add_members(client, message):
    await message.edit("جاري اضافة جهاتك الي المجموعة")
    q, w, e = 0, 0, 0
    contacts = await client.get_contacts()
    await message.edit(f"جاري اضافة جهاتك الي المجموعة\nتم اضافة {w} عضو\nفشل اضافة {q} عضو")
    for a in contacts:
        e = e + 1
        try:
            await client.add_chat_members(message.chat.id, a.id)
            w = w + 1
        except:
            q = q + 1
        if e == 5:
            e = 0
            await message.edit(f"جاري اضافة جهاتك الي المجموعة\nتم اضافة {w} عضو\nفشل اضافة {q} عضو")
    await message.reply(f"تم اضافة {w} عضو\nفشل اضافة {q} عضو")
    await message.delete()


@Client.on_message(filters.command("ف", prefixes=f"."))
async def vsong(client, message):
    if message.reply_to_message:
        yad = message.reply_to_message.id
    else:
        yad = None
    text = message.text.split(None, 1)[1]
    await message.edit(f"جاري البحث عن {text}")
    if not text:
        return
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    await message.edit("جاري التحميل")
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
            video_file = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        await message.edit(f"خطأ في التحميل : {e}")
        return
    c_time = time.time()
    capy = f"[{thum}]({mo})"
    await message.edit("جاري الرفع")
    try:
        await client.send_video(
            message.chat.id,
            video=video_file,
            duration=int(ytdl_data["duration"]),
            file_name=str(ytdl_data["title"]),
            thumb=sedlyf,
            reply_to_message_id=yad,
            supports_streaming=True,
            caption=capy,
        )
        await message.delete()
        os.remove(video_file)
        os.remove(sedlyf)
    except Exception as e:
        await message.edit(f"حدث خطأ\n{e}")


@Client.on_message(filters.command("غ", prefixes=f"."))
async def msong(client, message):
    if message.reply_to_message:
        yad = message.reply_to_message.id
    else:
        yad = None
    text = message.text.split(None, 1)[1]
    if not text:
        return
    await message.edit(f"جاري البحث عن {text}")
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    mio[0]["duration"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    sedlyf = wget.download(kekme)
    opts = {
        'format': 'bestaudio[ext=m4a]',
        'keepvideo': False,
        'prefer_ffmpeg': False,
        'geo_bypass': True,
        'outtmpl': '%(title)s.%(ext)s',
        'quite': True,
    }
    await message.edit("جاري التحميل")
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(mo, download=True)
            audio_file = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        await message.edit(f"خطأ في التحميل : {e}")
        return
    c_time = time.time()
    capy = f"[{thum}]({mo})"
    file_stark = f"{ytdl_data['id']}.mp3"
    await message.edit("جاري الرفع")
    try:
        await client.send_audio(
            message.chat.id,
            audio=audio_file,
            duration=int(ytdl_data["duration"]),
            title=str(ytdl_data["title"]),
            performer=str(ytdl_data["uploader"]),
            file_name=str(ytdl_data["title"]),
            thumb=sedlyf,
            reply_to_message_id=yad,
            caption=capy,
        )
        await message.delete()
        os.remove(audio_file)
        os.remove(sedlyf)
    except Exception as e:
        await message.edit(f"حدث خطأ\n{e}")

@Client.on_message(filters.command("تخ$", prefixes=f".") & filters.me)
async def ceev(client, message):
    if message.reply_to_message.from_user.id == 1405636280:
        await message.reply_text("☭ عذرآ لا تستطيع استخدام الأمر على المبرمج فرعون ❤️‍🔥")
    else:
        fraon = await client.get_chat(message.from_user.id)
        FR3ON = fraon.username
        usr = await client.get_users(message.reply_to_message.from_user.id)
        name = usr.username
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        await message.reply_video(
          video="https://telegra.ph/file/a2c9fa6de45e0fc4fc81e.mp4",
          caption=f"☭ تم قتل هذا الشخص @{name}\n\n※ بواسطة @{FR3ON}\n\n ان لله وان اليه راجعون ⚰😭")



@Client.on_message(filters.command("مح$", prefixes=f".") & filters.me)
async def cehgkev(client, message):
    if message.reply_to_message.from_user.id == 1405636280:
        await message.reply_text("☭ عذرآ لا تستطيع استخدام الأمر على المبرمج فرعون ❤️‍🔥")
    else:
        fraon = await client.get_chat(message.from_user.id)
        FR3ON = fraon.username
        usr = await client.get_users(message.reply_to_message.from_user.id)
        name = usr.username
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        await message.reply_video(
          video="https://telegra.ph/file/f9fca108067895e042f1f.mp4",
          caption=f"☭☭القميل هذا ✨♥ @{FR3ON}\n\n※ بعتلك بوسه يا 😘♥ @{name} \n\n عيب كده اي المحن ده 😹")         


@Client.on_message(filters.command("تف$", prefixes=f".") & filters.me)
async def chhev(client, message):
    if message.reply_to_message.from_user.id == 1405636280:
        await message.reply_text("☭ عذرآ لا تستطيع استخدام الأمر على المبرمج فرعون ❤️‍🔥")
    else:
        fraon = await client.get_chat(message.from_user.id)
        FR3ON = fraon.username
        usr = await client.get_users(message.reply_to_message.from_user.id)
        name = usr.username
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        await message.reply_video(
          video="https://telegra.ph/file/7f4c6eebf2f23b41dea45.mp4",
          caption=f"☭ تم التف علي هذا الشخص @{name}\n\n※ بواسطة @{FR3ON} \n\n اععع اي القرف ده 🤢") 

azkar = ["لا إِلَهَ إِلا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ🌸",
                     "اللَّهُمَّ أَعِنِّي عَلَى ذِكْرِكَ , وَشُكْرِكَ , وَحُسْنِ عِبَادَتِكَ🎈💞",
                     "استغفر الله العظيم وأتوبُ إليه 🌹",
                     "حَسْبِيَ اللَّهُ لا إِلَـهَ إِلاَّ هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيم"
                     "ِ سبع مرات، كفاه الله تعالى ما أهمه من أمور الدنيا والآخرة🌹🌸",
                     "ربنا اغفر لنا ذنوبنا وإسرافنا فِي أمرنا وثبت أقدامنا وانصرنا على القوم الكافرين🌸",
                     "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
                     "سبحان الله وبحمده سبحان الله العظيم🌸",
                     "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
                     "اللهم إنك عفو تُحب العفو فاعفُ عنّا 🌿🌹",
                     "استغفر الله العظيم وأتوبُ إليه 🌹",
                     "لا تقطع صلاتك، إن كنت قادراً على الصلاة في الوقت فصلِي و أكثر من الدعاء لتحقيق ما تتمنى💙",
                     "قال ﷺ : ”حَيْثُمَا كُنْتُمْ فَصَلُّوا عَلَيَّ، فَإِنَّ صَلَاتَكُمْ تَبْلُغُنِي“.",
                     "يا رب أفرحني بشيئاً انتظر حدوثه،اللهم إني متفائلاً بعطائك فاكتب لي ما أتمنى🌸",
                     "﴿ رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي ﴾",
                     "‏{ تَوَفَّنِي مُسْلِمًا وَأَلْحِقْنِي بِالصَّالِحِينَ }",
                     "‏اللهّم لطفك بقلوبنا وأحوالنا وأيامنا ،‏اللهّم تولنا بسعتك وعظيم فضلك ",
                     "ومن أحسن قولاً ممن دعا إلى الله وعمل صالحاً وقال أنني من المسلمين .💕",
                     "‏إن الله لا يبتليك بشيء إلا وبه خيرٌ لك فقل الحمدلله.",
                     "رَبِّ أَوْزِعْنِي أَنْ أَشْكُرَ نِعْمَتَكَ",
                     "اللهم اشفي كل مريض يتألم ولا يعلم بحاله إلا أنت",
                     "استغفر الله العظيم وأتوبُ إليه.",
                     "‏لَم تعرف الدنيا عظيماً مِثله صلّوا عليه وسلموا تسليم",
                     " أنتَ اللّطيف وأنا عبدُك الضّعيف اغفرلي وارحمني وتجاوز عنّي.",
                     "ماتستغفر ربنا كده🥺❤️",
                     "فاضي شويه نصلي ع النبي ونحز خته فى الجنه❤️❤️",
                     "ماتوحدو ربنا يجماعه قولو لا اله الا الله❤️❤️",
                     "يلا كل واحد يقول سبحان الله وبحمده سبحان الله العظيم 3 مرات🙄❤️",
                     "قول لاحول ولا قوه الا بالله يمكن تفك كربتك🥺❤️",
                     "اللهم صلي عللى سيدنا محمد ماتصلي على النبي كده",
                     "- أسهل الطرق لإرضاء ربك، أرضي والديك 🥺💕",
                     "- اللهُم صبراً ، اللهم جبراً ، اللهم قوّة",
                     "أصبحنا وأصبح الملك لله ولا اله الا الله.",
                     "‏إنَّ اللهَ يُحِبُ المُلحِينَ فِي الدُّعَاء.",
                     "‏إن الله لا يخذل يداً رُفعت إليه أبداً.",
                     "يارب دُعاء القلب انت تسمعه فأستجب لهُ.",
                     "- اللهم القبول الذي لا يزول ❤️🍀.",
                     "- اللهُم خذ بقلبّي حيث نورك الذي لا ينطفِئ.",
                     "سبحان الله وبحمده ،سبحان الله العظيم.",
                     "لا تعودوا أنفسكم على الصمت، اذكرو الله، استغفروه، سبّحوه، احمدوه،"
                     " عودوا السنتكم على الذكر فإنها إن اعتادت لن تصمت أبدًا.",
                     "- اللهم بلغنا رمضان وأجعلنا نختم القرآن واهدنا لبر الامان يالله يا رحمان 🌙",
                     "بسم الله الذي لا يضر مع اسمه شيء في الأرض ولا في السماء وهو السميع العلي- ثلاث مرات -",
                     "- اللهم احرمني لذة معصيتك وارزقني لذة طاعتك 🌿💜.",
                     "- اللهُم إن في صوتي دُعاء وفي قلبِي أمنية اللهُم يسر لي الخير حيث كان.",
                     "‏اللهم أرني عجائب قدرتك في تيسير أموري 💜.",
                     "يغفر لمن يشاء إجعلني ممن تشاء يا الله.*",
                     "‏يارب إن قصّرنا في عبادتك فاغفرلنا، وإن سهينا عنك بمفاتن الدنيا فردنا إليك رداً جميلاً 💜🍀",
                     "صلوا على من قال في خطبة الوداع  ‏و إني مُباهٍ بكم الأمم يوم القيامة♥️⛅️",
                     "اللهـم إجعلنا ممن تشهد أصابعهم بذكـر الشهادة قبل الموت 🌿💜.",
                     "- وبك أصبحنا يا عظيم الشأن 🍃❤️.",
                     "اللهُم الجنة ونعيَّم الجنة مع من نحب💫❤️🌹",
                     "‏اللهم قلبًا سليمًا عفيفًا تقيًا نقيًا يخشاك سرًا وعلانية🤍🌱",
                     "- أسجِد لربِك وأحضِن الارض فِي ذِ  لاضَاق صَدرِك مِن هَموم المعَاصِي 🌿.",
                     "صلي على النبي بنيه الفرج❤️",
                     "استغفر ربنا كده 3 مرات هتاخد ثواب كبير اوى❤️",
                     "اشهد ان لا اله الا الله وان محمدا عبده ورسوله",
                     "لا اله الا الله سيدنا محمد رسول الله🌿💜",
                     "قول معايا - استغفر الله استفر الله استغفر الله -",
                     "مُجرد ثانية تنفعِك : أستغفُرالله العظيِم وأتوب إليّه.",
                     "أدعُ دُعاء الواثِق فالله لايُجرّبُ معه‌‏",
                     "صلي على محمد❤️",
                     "ماتيجو نقرء الفاتحه سوا🥺"]
                     
                     
is_enabled = False

@Client.on_message(filters.command("تفعيل الاذكار", prefixes=f".") & filters.me)
async def start_sending_azkar(client: Client, message: Message):
    if message.reply_to_message:
        yad = message.reply_to_message.id
    else:
        yad = None       
    text = message.text.split(None, 2)[2]        
    try:
        global is_enabled
        if not is_enabled:
            is_enabled = True
            await message.reply(f"تم تفعيل ارسال الاذكار كل {text}")        
            while is_enabled:
                random_azkar = random.choice(azkar)
                try:
                    await message.reply(f"{random_azkar}")
                    await message.edit("تم تفعيل الأذكار")
                except:
                    pass        
                time.sleep(int(text))
        else:
            await message.edit("أنا بالفعل قيد الإرسال")
    except Exception as e:
        print(f"An error occurred: {e}")

@Client.on_message(filters.command("تعطيل الاذكار", prefixes=f".") & filters.me)
async def stop_sending_azkar(client: Client, message: Message):
    global is_enabled
    is_enabled = False
    await message.edit("تم إيقاف إرسال الأذكار")