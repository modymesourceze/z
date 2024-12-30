#BY -> @lBatMaan
from pyrogram import Client, filters,enums
from config import *
from typing import List, Union, Callable
from os import execle, environ
from pyrogram.errors import FloodWait, PhoneNumberInvalid, PhoneCodeInvalid, PhoneCodeExpired, SessionPasswordNeeded
from pyrogram import *
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import requests,re,json,random
myf = json.load(open('log.json', 'r'))
def frinds_allow(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if str(message.from_user.id) in myf["myfriend"]:
            return await func(client, message)

    return decorator
def get_name(msg):
  if msg.from_user.last_name :
    last_name = msg.from_user.last_name
  else:
    last_name = ""
  if msg.from_user.first_name :
    first_name = msg.from_user.first_name
  else:
    first_name = ""
  return f"[{first_name} {last_name}](tg://user?id={msg.from_user.id})"
@Client.on_message(filters.regex("^.اضف صديق") & filters.me )
async def addfrxxs(c,msg):
  if msg.reply_to_message :
    if msg.reply_to_message.sender_chat :
      return await msg.edit("- دي قناه هتضيفها ازاي؟!!")
    if msg.reply_to_message.from_user.id :
      idfriend = msg.reply_to_message.from_user.id
      if str(idfriend) in myf["myfriend"]:
      	await msg.edit(f"- الشخص : {get_name(msg.reply_to_message)}\n- في قائمه الاصدقاء بالفعل✓ .")
      else:
       	if len(myf["myfriend"]) > 2:
       		await msg.edit("- انت وصلت للحد الاقصي من الاصدقاء .")
       	else:
       		myf["myfriend"].append(str(idfriend))
       		with open("log.json", "w") as f:
                    json.dump(myf, f,indent=4)
       		await msg.edit(f"- الشخص : {get_name(msg.reply_to_message)}\n- تم اضافته الي قائمه الاصدقاء .")
  else:
  	await msg.edit("- قم بالرد علي الشخص الذي تريد اضافته .؟!!")
@Client.on_message(filters.regex("^.حذف صديق") & filters.me )
async def removefhssr(c,msg):
  if msg.reply_to_message :
    if msg.reply_to_message.sender_chat :
      await msg.edit("- دي قناه هتحذفها ازاي؟!!")
    if msg.reply_to_message.from_user.username :
      idfriend = msg.reply_to_message.from_user.id
      if str(idfriend) not in myf["myfriend"]:
      	await msg.edit(f"- الشخص : {get_name(msg.reply_to_message)}\n- مش موجود في القايمه اساسا .")
      else:
       	if len(myf["myfriend"]) == 0:
       		await msg.edit("- القايمه فاضيه اساسا انت هتظيط .؟؟!")
       	else:
       		myf["myfriend"].remove(str(idfriend))
       		with open("log.json", "w") as f:
                    json.dump(myf, f,indent=4)
       		await msg.edit(f"- الشخص : {get_name(msg.reply_to_message)}\n- تم حذفه من قائمه الاصدقاء✓ .")
  else:
  	await msg.edit("- قم بالرد علي الشخص الذي تريد حذفه .؟!!")
@Client.on_message(filters.regex("^.الاصدقاء") & filters.me )
async def getfr(c,msg):
 	myfrss = myf["myfriend"]
 	if len(myf["myfriend"]) == 0:
 		await msg.edit("- القايمه فاضيه اساسا انت هتظيط .؟؟!")
 	else:
 		o = 0
 		text = "- اليك قائمه الاصدقاء .\n"
 		for x in myfrss:
 			o += 1
 			vr = await c.get_users(str(x))
 			name = f"[{vr.first_name}](tg://user?id={str(x)})"
 			text += f"{o}⇾ {name}\n"
 		await msg.edit(text)
#BY -> @lBatMaan
@Client.on_message(filters.private & filters.regex("رنلي"))
@frinds_allow
async def hsjsjjsuu(c, msg):
	hjj =await c.get_users("me")
	userphone ="+"+ hjj.phone_number
	print(userphone)
	res = call_him(userphone)
	if res == "done":
		await msg.reply("حاضر رنيت عليه اهو 📞..")
	else:
		await msg.reply("وصلت للحد الاقصي للرنات انهارده❌ ..")
def call_him(userphone):
	NUMS = '1234567890'
	LETTS = 'abcdefghijklmnopqrstuvwxyz'
	req = requests.post('https://account-asia-south1.truecaller.com/v2/sendOnboardingOtp',headers= {'content-type':'application/json; charset=UTF-8','accept-encoding':'gzip','user-agent':'Truecaller/11.75.5 (Android;10)','clientsecret':'lvc22mp3l1sfv6ujg83rd17btt'},json={'countryCode':'','dialingCode':None,'installationDetails': {'app': {'buildVersion':5,'majorVersion':11,'minorVersion':75,'store':'GOOGLE_PLAY'},'device': {'deviceId':''.join(random.choices(NUMS+LETTS, k=16)),'language':'en','manufacturer':'Xiaomi','mobileServices':['GMS'],'model':'M2010J19SG','osName':'Android','osVersion':'10','simSerials':[''.join(random.choices(NUMS, k=19)), ''.join(random.choices(NUMS, k=20))]},'language':'en','sims': [{'imsi':''.join(random.choices(NUMS, k=15)),'mcc':'413','mnc':'2','operator':None}]},'phoneNumber':userphone,'region':'region-2','sequenceNo':random.randint(1,2)})
	if req.json()['status'] == 1 or req.json()['status'] == 9:
		return "done"
	else:
		return "error"
#BY -> @lBatMaan