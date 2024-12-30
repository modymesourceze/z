from pyrogram import Client, filters,enums
from config import *
import asyncio
import requests,re

@Client.on_message(filters.regex("^.منصه (.*)") & filters.me )
async def search_word(c,msg):
  text = msg.text
  if "@" in text:
  	username = text.split('@')[1].lower()
  	await msg.edit("- ثوانيي..")
  	res = check(username)
  	if "Sold" in res:
  		price = res.split(':')[1]
  		await msg.edit(f"- اليوزر : @{username} \n- مرفوع فالمزاد ومتباع كمان✓\n- وسعره كان : {price}")
  	elif res == "Taken":
  		await msg.edit(f"- اليوزر : @{username} \n- مش مرفوع فالمزاد بس متاخد✓")
  	elif "On auction" in res :
  		time = res.split(':')[1]
  		price = res.split(':')[2]
  		await msg.edit(f"- اليوزر : @{username} \n- مرفوع وعليه عرض✓\n- العرض هينتهي بعد : {time}\n- وسعره : {price}")
  	elif "Available" in res:
  		price = res.split(':')[1]
  		await msg.edit(f"- اليوزر : @{username} \n- مرفوع فالموقع✓\n- وسعره : {price}")
  	elif res == "Unavailable":
  		await msg.edit(f"- اليوزر : @{username} \n- مش مرفوع فالمزاد ومش متاخد✓")
  	elif res == "error":
  		await msg.edit(f"- اليوزر : @{username} \n- غلط جرب يوزر صحيح✖️")
  	else:
  		await msg.edit(f"- اليوزر : @{username} \n- غلط جرب يوزر صحيح✖️")
  else:
  	await msg.edit(f"- اليوزر : @{username} \n- غلط جرب يوزر صحيح✖️")

def check(username):
	cookies = {
    'stel_ssid': 'e182eae071faac2b6b_18291885740355924147',
    'stel_dt': '-120',
}

	headers = {
    'Host': 'fragment.com',
    # 'content-length': '65',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': 'Android',
    'origin': 'https://fragment.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://fragment.com/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    # 'cookie': 'stel_ssid=e182eae071faac2b6b_18291885740355924147; stel_dt=-120',
}

	params = {
    'hash': '24a990babad47ec165',
}

	data = {
    'type': 'usernames',
    'query': username,
    'filter': '',
    'sort': '',
    'method': 'searchAuctions',
}
	try:
		response = requests.post('https://fragment.com/api', params=params, cookies=cookies, headers=headers, data=data).json()['html'].split('<div class="table-cell-value tm-value">@'+username+'</div>')[1]

		statue = re.findall('>(.*?)</div>',response)[0]
		if statue == "Sold":
			price = re.findall('<div class="table-cell-value tm-value icon-before icon-ton">(.*?)</div>',response)[0]
			return "Sold:"+price
		elif statue == "On auction":
			time = re.findall('data-relative="short-text">(.*?)</time>',response)[0]
			price = re.findall('<div class="table-cell-value tm-value icon-before icon-ton">(.*?)</div>',response)[0]
			return "On auction:"+time+":"+price
		elif statue == "Available":
			price = re.findall('<div class="table-cell-value tm-value icon-before icon-ton">(.*?)</div>',response)[0]
			return "Available:"+price
		elif statue == "Unavailable":
			return "Unavailable"
		elif statue == "Taken":
			return "Taken"
		else:
			return "error"
	except:
		return "error"