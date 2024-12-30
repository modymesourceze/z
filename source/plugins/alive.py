from pyrogram import Client, filters, enums
from config import *
from pyrogram import __version__ as pyro
from platform import python_version
from time import time


@Client.on_message(filters.command("عايش", prefixes=f".") & filters.me)
async def alive_msg(c, m):
    start_time = time()
    msg = await m.edit("⚡")
    alive_logo = r.get(f"{sudo_id}:ALIVE_MEDIA") or "https://envs.sh/Gb6.jpg"
    emoji = r.get(f"{sudo_id}:ALIVE_EMOJI") or "⚡️"
    alive_text = r.get(f"{sudo_id}:ALIVE_TEXT_CUSTOM") or "ايوا انا عايش.!!"
    CHANNEL = r.get(f"{sudo_id}:ALIVE_CHANNEL") or "H_0RSE"
    send = c.send_video if alive_logo.endswith(".mp4") else c.send_photo
    await msg.delete()
    all_time = time() - start_time
    rep = m.reply_to_message.id if m.reply_to_message else 0
    if c.me.is_premium:
        alive_ = (
            f"<b>{alive_text}</b>\n\n"
            f'<emoji id="5352542184493031170">🔥</emoji> <b>Your Userbot is horse</b> {m.from_user.first_name}'
            f'\n<emoji id="5257977338326425596">🔥</emoji> <b>Pyrogram version :</b> <code>{pyro}</code>'
            f'\n<emoji id="4985626654563894116">♥️</emoji> <b>Python version :</b> <code>{python_version()}</code>'
            f'\n<emoji id="5431449001532594346">⚡️</emoji> <b>Ping :</b> <code>{all_time * 1000:.3f} ms</code>'
            f'\n\n**[ꪔY ᥴ𝗁](https://t.me/{CHANNEL})** | **[᥆᭙ꪀᥱᖇ](tg://user?id={c.me.id})**'
        )
    else:
        alive_ = (
            f"<b>{alive_text}</b>\n\n"
            f"{emoji} <b>Master :</b> {c.me.mention} \n"
            f"{emoji} <b>Python Version :</b> <code>{python_version()}</code> \n"
            f"{emoji} <b>Pyrogram Version :</b> <code>{pyro}</code> \n"
            f"{emoji} <b>Ping :</b> <code>{all_time * 1000:.3f} ms</code> \n\n"
            f"{emoji} **[ꪔY ᥴ𝗁](https://t.me/{CHANNEL})** | **[᥆᭙ꪀᥱᖇ](tg://user?id={c.me.id})**"
            )
    await send(
                m.chat.id,
                alive_logo,
                caption=alive_,
                reply_to_message_id=rep,
            )