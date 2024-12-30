from pyrogram import Client, filters, enums
from config import *
import os, time

os.environ['TZ'] = 'Africa/Cairo'
time.tzset()


@Client.on_message(filters.private & ~filters.bot)
async def pv_cmd(c, msg):
    log_chat = r.get(f"{sudo_id}:LOG_CHAT")
    if msg.from_user.id != sudo_id:
        try:
            await msg.forward(log_chat)
        except:
            if msg.media == enums.MessageMediaType.VIDEO:
                await msg.download("./Ttl.mp4")
                await app.send_video(log_chat, "Ttl.mp4")
                os.remove("./Ttl.mp4")
            elif msg.media == enums.MessageMediaType.PHOTO:
                await msg.download("./Ttl.jpg")
                await app.send_photo(log_chat, "Ttl.jpg")
                os.remove("./Ttl.jpg")
            pass
        if r.sismember(f"{sudo_id}mute_pv", msg.chat.id):
            await msg.delete(revoke=True)
            return
        if r.get(f"{sudo_id}welcome"):
            if not r.sismember(f"{sudo_id}accept", msg.chat.id):
                if r.get(f"{sudo_id}waiting{msg.chat.id}"):
                    r.delete(f"{sudo_id}waiting{msg.chat.id}")
                    await msg.reply("تم ارسال رسالتك بنجاح \n قام النظام بكتمك انتظر حتا يقوم مالك الحساب بالرد عليك")
                    r.sadd(f"{sudo_id}mute_pv", msg.chat.id)
                    r.delete(f"{sudo_id}waiting{msg.chat.id}")
                    return
                r.set(f"{sudo_id}waiting{msg.chat.id}", "on")
                PM_logo = r.get(f"{sudo_id}:PMG_MEDIA") or "https://envs.sh/Gb6.jpg"
                CHANNEL = r.get(f"{sudo_id}:CHANNEL") or "H_0RSE0"
                CHANNEL = CHANNEL.replace('@', '')
                PM_text = r.get(f"{sudo_id}:PM_TEXT_CUSTOM") or " مرحبا مالك الحساب ربما يكون  مشغول الان من فضلك قم بترك رسالتك وسيقوم بالرد عليك"
                send = c.send_video if PM_logo.endswith(".mp4") else c.send_photo
                try:
                    await send(
                        msg.chat.id,
                        PM_logo,
                        caption=f"<b>{PM_text}</b>\n\n [𝑴𝒀 𝑪𝑯𝑨𝑵𝑵𝑬𝑳](https://t.me/H_0RSE) | [َ𝑴𝒀 𝑫𝑬𝑽](https://t.me/SPORT_HORSE) "
                    )
                except Exception as e:
                    print(e)
                    await msg.reply(f"<b>{PM_text}</b>\n\n [𝑴𝒀 𝑪𝑯𝑨𝑵𝑵𝑬𝑳](https://t.me/H_0RSE) | [َ𝑴𝒀 𝑫𝑬𝑽](https://t.me/SPORT_HORSE)")
                return
    else:
        if msg.text == ".قبول" or msg.text == ".الغاء كتم":
            r.srem(f"{sudo_id}mute_pv", msg.chat.id)
            r.sadd(f"{sudo_id}accept", msg.chat.id)
            await msg.edit("⌔ تم السماح له بالتحدث")
        if msg.text == ".رفض":
            r.srem(f"{sudo_id}accept", msg.chat.id)
            await msg.edit("⌔ تم رفض العضو")
        if msg.text == ".كتم":
            r.sadd(f"{sudo_id}mute_pv", msg.chat.id)
            await msg.edit("⌔ تم كتم العضو")


@Client.on_message(filters.group)
async def gp(client, msg):
    log_chat = r.get(f"{sudo_id}:LOG_CHAT")
    current_time = time.strftime('%H:%M')
    chatt = str(msg.chat.id)
    chat = chatt.replace("-100", "").replace("-", "")
    msg_link = f"[ اضغط هنا لعرض الرساله](https://t.me/c/{chat}/{msg.id})"
    if msg.mentioned:
        if msg.from_user:
            try:
                txt = f"⌔ لديك منشن من العضو [{msg.from_user.first_name}](tg://user?id={msg.from_user.id}) \n⌔ اسم الجروب {msg.chat.title} \n⌔ الوقت {current_time} \n{msg_link}"
                await app.send_message(log_chat, txt)
                await msg.forward(log_chat)
            except:
                pass
        else:
            txt = f"⌔ لديك منشن من القناه {msg.sender_chat.title} \n⌔ اسم الجروب {msg.chat.title} \n⌔ الوقت {current_time} \n{msg_link}"
            await app.send_message(log_chat, txt)
            await msg.forward(log_chat)
    if msg.from_user:
        sender_id = msg.from_user.id
    elif msg.sender_chat:
        sender_id = msg.sender_chat.id
    if r.sismember(f"{sudo_id}mute", sender_id) or r.sismember(f"{sudo_id}mute{msg.chat.id}", sender_id):
        try:
            await msg.delete()
        except:
            pass
    if r.sismember(f"{sudo_id}ban", sender_id):
        try:
            await msg.delete()
            await client.ban_chat_member(msg.chat.id, msg.from_user.id)
        except:
            pass
