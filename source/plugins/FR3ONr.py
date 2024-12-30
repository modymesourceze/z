from pyrogram import Client, filters, enums
from config import *

@Client.on_message(filters.command("احصائيات الحساب", prefixes=f".") & filters.me)
async def Dialogs_count(c, m):
    CHANNELS = 0
    GROUPS = 0
    DELETED = 0
    BOTS = 0
    PRIVATE = 0

    msg = await m.edit("~ جاري الاحصاء..")

    async for dialog in c.get_dialogs():
        if dialog.chat.type == enums.ChatType.CHANNEL:
            CHANNELS += 1
        elif dialog.chat.type == enums.ChatType.GROUP:
            GROUPS += 1
        elif dialog.chat.type == enums.ChatType.SUPERGROUP:
            GROUPS += 1
        elif dialog.chat.type == enums.ChatType.PRIVATE:
            if dialog.chat.first_name:
                PRIVATE +=1
            else:
                DELETED += 1
        elif dialog.chat.type == enums.ChatType.BOT:
            BOTS +=1

    t = (
        "~ احصائيات الحساب :\n\n"
        f"- `{CHANNELS}` قناه \n"
        f"- `{GROUPS}` جروب \n"
        f"- `{PRIVATE}` شات مستخدم \n"
        f"- `{BOTS}` شات بوت \n"
        f"- `{DELETED}` حساب محذوف \n"
        )
    await msg.edit(t)


@Client.on_message(filters.command("تصفيه القنوات", prefixes=f".") & filters.me)
async def Leave_Channels(c, m):
    CHANNELS = 0
    msg = await m.edit("~ جاري الخروج من القنوات..")
    async for dialog in c.get_dialogs():
        if dialog.chat.type == enums.ChatType.CHANNEL:
            await c.leave_chat(dialog.chat.id, delete=True)
            CHANNELS += 1
    t = f"~ تم الخروج من  `{CHANNELS}` قناه "
    await msg.edit(t)


@Client.on_message(filters.command("تصفيه الجروبات", prefixes=f".") & filters.me)
async def Leave_Groups(c, m):
    GROUPS = 0
    msg = await m.edit("~ جاري الخروج من الجروبات..")
    async for dialog in c.get_dialogs():
        if dialog.chat.type == enums.ChatType.GROUP:
            await c.leave_chat(dialog.chat.id, delete=True)
            GROUPS += 1
        elif dialog.chat.type == enums.ChatType.SUPERGROUP:
            await c.leave_chat(dialog.chat.id, delete=True)
            GROUPS += 1
    t = f"~ تم الخروج من  `{GROUPS}` قناه "
    await msg.edit(t)


@Client.on_message(filters.command("تصفيه الحسابات المحذوفه", prefixes=f".") & filters.me)
async def Clear_DeleteUsers(c, m):
    DELETES = 0
    msg = await m.edit("~ جاري حذف شاتات الحسابات المحذوفه..")
    async for dialog in c.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            if not dialog.chat.first_name:
                async for message in c.get_chat_history(dialog.chat.id):
                    await message.delete()
                DELETES +=1
    t = f"~ تم حذف  `{DELETES}` شات حساب محذوف "
    await msg.edit(t)

@Client.on_message(filters.command("تصفيه الشاتات", prefixes=f".") & filters.me)
async def Clear_DeleteUsers(c, m):
    DELETES = 0
    msg = await m.edit("~ جاري حذف شاتات..")
    async for dialog in c.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            async for message in c.get_chat_history(dialog.chat.id):
                await message.delete()
                DELETES +=1
    t = f"~ تم حذف  `{DELETES}` شات"
    await msg.edit(t)

@Client.on_message(filters.command("تصفيه البوتات", prefixes=f".") & filters.me)
async def Clear_BOTS(c, m):
    BOTS = 0
    msg = await m.edit("~ جاري حذف البوتات..")
    async for dialog in c.get_dialogs():
        if dialog.chat.type == enums.ChatType.BOT:
            async for message in c.get_chat_history(dialog.chat.id):
                await message.delete()
                BOTS +=1
    t = f"~ تم حذف  `{BOTS}` شات"
    await msg.edit(t)

@Client.on_message(filters.command("طير", prefixes=f".") & filters.me & filters.private)
async def Clear_Chat(c, m):
    async for message in c.get_chat_history(m.chat.id):
        await message.delete()

@Client.on_message(filters.command("طير", prefixes=f".") & filters.me & filters.reply)
async def Clear_Chat(c, m):
    if m.reply_to_message.from_user.id in sudo_command:
        return await m.edit("⌔ لا يمكنك استخدام الامر علي مبرمجين السورس")
    msg = await m.edit("~ جاري تطير الشات..")
    try:
        async for message in c.get_chat_history(m.reply_to_message.from_user.id):
            await message.delete()
        await msg.edit("~ تم تطير الشات")
    except:
        await msg.edit("~ حدث خطأ.")