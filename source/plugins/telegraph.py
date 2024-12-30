import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message

# بيانات API الخاصة بـ Cloudinary (استبدل القيم بما لديك)
CLOUDINARY_URL = "https://api.cloudinary.com/v1_1/dtf4epkfi/upload"  # اسم السحابة الخاص بك
CLOUDINARY_API_KEY = "492628463888227"  # استبدل بـ API Key الخاص بك
CLOUDINARY_API_SECRET = "SKH0DBiBdjHkjD8Jx3y3EIT8Mco"  # استبدل بـ API Secret الخاص بك
CLOUDINARY_UPLOAD_PRESET = "hqcjg1id"  # اسم الـ upload preset الذي قمت بتعديله
CLOUDINARY_API_BASE = "https://api.cloudinary.com/v1_1/dtf4epkfi"  # اسم السحابة الخاص بك

# دالة لرفع أي نوع من الملفات (صور وفيديوهات) إلى Cloudinary
def upload_to_cloudinary(file_path: str) -> str:
    data = {
        'upload_preset': CLOUDINARY_UPLOAD_PRESET,  # تعيين preset الافتراضي
        'api_key': CLOUDINARY_API_KEY,
    }

    # فتح الملف وإرساله مع بيانات المصادقة
    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(CLOUDINARY_URL, data=data, files=files)

    if response.status_code == 200:
        response_data = response.json()
        return response_data['secure_url'], response_data['public_id']
    else:
        raise Exception(f"Error uploading to Cloudinary: {response.status_code} - {response.text}")

# دالة لحذف الملف من Cloudinary باستخدام public_id
def delete_from_cloudinary(public_id: str) -> bool:
    delete_url = f"{CLOUDINARY_API_BASE}/resources/image/upload/{public_id}"
    params = {
        'api_key': CLOUDINARY_API_KEY,
        'api_secret': CLOUDINARY_API_SECRET,
    }
    response = requests.delete(delete_url, params=params)
    
    if response.status_code == 200:
        return True
    else:
        print(f"Failed to delete from Cloudinary: {response.status_code} - {response.text}")
        return False

# دالة لاستخراج النص من الرسالة
def get_text(message: Message) -> [None, str]:
    """Extract text from commands in the message."""
    text_to_return = message.text
    if not text_to_return:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    return None

# التعامل مع الرسائل التي تحتوي على ميديا (صور، فيديوهات، مستندات)
@Client.on_message(filters.command(["تليجراف", "telegraph", "رفع صوره", "tgt"], ".") & filters.me)
async def upload_file_to_cloudinary(client: Client, message: Message):
    tex = await message.edit_text("جاري الرفع ⚡ . . .")

    if not message.reply_to_message:
        await tex.edit("**يرجى الرد على صورة أو فيديو أو مستند.**")
        return

    # التعامل مع الصور والفيديوهات
    if message.reply_to_message.photo:
        file = await message.reply_to_message.download()
        file_type = "image"
    elif message.reply_to_message.video:
        file = await message.reply_to_message.download()
        file_type = "video"
    elif message.reply_to_message.document:
        file = await message.reply_to_message.download()
        file_type = "document"
    elif message.reply_to_message.audio:
        file = await message.reply_to_message.download()
        file_type = "audio"
    elif message.reply_to_message.sticker:
        file = await convert_to_image(message, client)  # تحويل الملصق إلى صورة
        file_type = "image"
    else:
        await tex.edit("**نوع الميديا غير مدعوم.**")
        return

    try:
        # رفع الملف إلى Cloudinary
        cloudinary_url, public_id = upload_to_cloudinary(file)
    except Exception as exc:
        await tex.edit(f"**خطأ أثناء الرفع:** {exc}")
        os.remove(file)  # تنظيف الملف المحمل
        return

    # إرسال رابط الملف المرفوع بشكل مباشر
    U_done = f"**تم التحميل بنجاح**\nالرابط: {cloudinary_url}"
    await tex.edit(U_done)

    # حذف الصورة من السيرفر المحلي بعد الرفع
    os.remove(file)

    # مسح الملف من Cloudinary
    delete_success = delete_from_cloudinary(public_id)
    if delete_success:
        print(f"تم مسح الملف بنجاح من Cloudinary")
    else:
        print(f"فشل مسح الملف من Cloudinary")


# دالة لتحويل الملصق إلى صورة (إذا لزم الأمر)
from PIL import Image

async def convert_to_image(message: Message, client: Client) -> str:
    # تحميل الملصق
    sticker_file = await message.reply_to_message.sticker.download()

    # تحويل الملصق إلى صورة
    with Image.open(sticker_file) as img:
        img.save("temp_sticker.jpg")  # حفظ الصورة المؤقتة

    return "temp_sticker.jpg"