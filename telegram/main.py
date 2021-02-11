# import requests
# import pprint
#
#
# api_link = 'https://api.telegram.org/bot1676501133:AAE3PILf55H9AWs0YvFCcFmpYdQuFuPnM6w'
#
# updates = requests.get(api_link + "/getUpdates?offset=-1").json()
#
# pprint.pprint(updates)
#
# massage = updates['result'][0]['message']
#
# chat_id = massage['from']['id']
# text = massage['text']
#
# sent_massage = requests.get(api_link + f"/sendMessage?chat_id={chat_id}&text=Привет!!! Ты написал: {text}")


import asyncio
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)



