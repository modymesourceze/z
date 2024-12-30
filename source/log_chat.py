from config import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def Creat_log_chat():
    if not r.get(f"{sudo_id}:LOG_CHAT"):
        bot_user = bot.me.username
        try:
            log_chat = await app.create_supergroup("-تخزين سورس هورس ", "_ هذه المجموعة هي عبارة عن سجل الرسائل\n\n✯𝑫𝒆𝒗 »» @SPORT_HORSE\n✯ 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 »» @H_0RSE")
        except Exception as e:
            print(f"--------=> LOG CHAT ERROR | {e}")
        try:
            await app.add_chat_members(log_chat.id, bot_user)
        except Exception as e:
            print(f"--------=> LOG CHAT ERROR | {e}")
        try:
            await app.promote_chat_member(log_chat.id, bot_user)
        except Exception as e:
            print(f"--------=> LOG CHAT ERROR | {e}")
        r.set(f"{sudo_id}:LOG_CHAT", log_chat.id)
        print(f"--------=> LOG CHAT CREATED | {log_chat.id}")
        try :
            await app.set_chat_photo(log_chat.id,photo="photo.jpg")
            await app.send_message(log_chat.id, " لمعرفة الاوامر قم بكتابة اوامري**تم تنصيب حسابك علي سورس هورس  مبرمج السورس @SPORT_HORSE**")
            await app.send_photo(log_chat.id, photo=f"https://envs.sh/Gb6.jpg", caption=f"""تم التنصيب علي سورس هورس\nلمعرفة الاوامر الخاصه بك قم بكتابة\n.اوامري""" , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐎𝐑𝐒𝐄", url=f"https://t.me/H_0RSE")]]))
        except :
            pass
    else:
        log_chat = r.get(f"{sudo_id}:LOG_CHAT")
        print(f"--------=> LOG CHAT | {log_chat}")
