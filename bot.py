from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "FR3ON",
    api_id=21627756,
    api_hash="fe77fbf0cae9f7f5ece37659e2466cf1",
    bot_token="7673763548:AAFbgZ6TWEDKV6FKRAiNLh0jMWgS5t8HdWA",
    plugins=dict(root="FR3ON")
    )

DEVS = ["D_S_IS"] 

bot_id = bot.bot_token.split(":")[0]

async def start_ahmedbot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    for hh in DEVS:
        try:
            await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
        except:
            pass
    await idle()
