#main.py
import os
import telegram
import asyncio
import requests


async def formatMessage(bot, tradingFile):
    signal = tradingFile['from']
    pair = tradingFile['pair']
    side = tradingFile['side']
    price = str(tradingFile['price'])
    leverage = str(tradingFile['leverage'])
    buyOrSell = tradingFile['type']
    emojiBuyOrSell = ""
    if buyOrSell == "BUY":
        emojiBuyOrSell = "\U00002705"
    else:
        emojiBuyOrSell = "\U0000274C"
    try: 
        await bot.sendPhoto(chat_id=-1001877018535, photo="https://cryptoicons.org/api/icon/" + pair.split('-')[0].lower() + "/100")
    except:
        print("photo not available")
    message = await bot.sendMessage(chat_id=-1001877018535, text="\U0001F4CC*" + signal + "*" + "\n*" + side + " " + 
        pair + "*\n" + "*Price*: " + price + " USDT\n" + "*Leverage*: " + leverage + "x" + "\n" + emojiBuyOrSell + buyOrSell, 
        parse_mode="Markdown")
    await bot.pinChatMessage(chat_id=-1001877018535, message_id=message['message_id'])

async def generateChatLink(bot):
    chatInviteLink = await bot.createChatInviteLink(chat_id=-1001877018535, member_limit=1)
    return chatInviteLink['invite_link']

def trading_bot(request):
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    if request.method == "POST":
        tradingFile = request.get_json()
        for key, value in tradingFile.items():
	        print(key, value)
        asyncio.run(formatMessage(bot, tradingFile))
    if request.method == "GET":
        return asyncio.run(generateChatLink(bot))
    return "AVENIR_TRADER"