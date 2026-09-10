import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Tokenni to'g'ridan-to'g'ri yozamiz (Render.com uchun)
BOT_TOKEN = "8675282028:AAHWDg1ETn7RTJm_XqR8peaw5Loa-enb1E"

# Proxy'siz oddiy bot yaratish (Render uchun muhim)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Assalomu alaykum! Hadiya botimiz Render.com serverida muvaffaqiyatli ishga tushdi! 🚀\n\nStars, Gifts va Premium xizmatlaridan foydalanishingiz mumkin.")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  
