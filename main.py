
import httpx
r = httpx.get('https://api.telegram.org/bot1868356667:AAH8O2GmcSGEJ3x3Xm-VqzlNGmMBagI4Fpg/getUpdates')

import asyncio
from aiogram import Bot, Dispatcher, types
from keep_alive import keep_alive

BOT_TOKEN = "1868356667:AAH8O2GmcSGEJ3x3Xm-VqzlNGmMBagI4Fpg"

async def start_handler(event: types.Message):
    await event.answer(
        f"Hello, {event.from_user.get_mention(as_html=True)} 👋!",
        parse_mode=types.ParseMode.HTML,
    )

async def main():
    bot = Bot(token=BOT_TOKEN)
    try:
        disp = Dispatcher(bot=bot)
        disp.register_message_handler(start_handler, commands={"start", "restart"})
        await disp.start_polling()
    finally:
        await bot.close()

asyncio.run(main())
keep_aiive()