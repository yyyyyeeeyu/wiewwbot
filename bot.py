# (c) 2021-22 < @BloodperBio >
# < @EpicEyeBots >

import logging
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# start the bot
print("Baslatiliyor...")
try:
    apiid = config("APP_ID", cast=int)
    apihash = config("API_HASH")
    bottoken = config("BOT_TOKEN")
    FRWD_CHANNEL = config("FRWD_CHANNEL", cast=int)
    EpicEyeBots = TelegramClient('EpicEyeBots', apiid, apihash).start(bot_token=bottoken)
except:
    print("Çevre değişkenleri eksik! Lütfen tekrar kontrol edin.")
    print("Bot bırakıyor...")
    exit()

@EpicEyeBots.on(events.NewMessage(pattern="/start", func=lambda e: e.is_private))
async def _(event):
    ok = await BotzHub(GetFullUserRequest(event.sender_id))
    await event.reply(f"Selam {ok.user.first_name}! \nBen Kanal Izleyici Artirici Botuyum\nBana bir kanal mesaji iletin ve ona bir görüntüleme sayısı ekleyeyim!",
                    buttons=[
                        [Button.url("Kanalimiz📣", url="https://t.me/EpicEyeBots"),
                        Button.url("Gelistirici🤙", url="https://t.me/BloodperBio")]
                    ])

@EpicEyeBots.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def countit(event):
    if event.text.startswith('/'):
        return
    x = await event.forward_to(FRWD_CHANNEL)
    await x.forward_to(event.chat_id)

print("Bot Baslatildi")
print("@EpicEyeBots Katil..")
EpicEyeBots.run_until_disconnected()
