import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiohttp import web

BOT_TOKEN = "8675282028:AAHWDg1ETn7RTJm_XqR8peaw5Loa-enb1E"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Assalomu alaykum! Hadiya botimiz Render.com serverida muvaffaqiyatli ishga tushdi! 🚀\n\nStars, Gifts va Premium xizmatlaridan foydalanishingiz mumkin.")

# Render talabini bajarish uchun kichik veb-server
async def handle(request):
    return web.Response(text="Bot is active!")

async def web_server():
    app = web.Application()
    app.add_routes([web.get("/", handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot va veb-server ishga tushmoqda...")
    await asyncio.gather(
        web_server(),
        dp.start_polling(bot)
    )

if __name__ == "__main__":
    asyncio.run(main())
    
