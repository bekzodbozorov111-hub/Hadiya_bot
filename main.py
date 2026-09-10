import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "8675282028:AAHWDg1ETn7RTJm_XqR8peaw5Loa-enb1E"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    await message.answer("Salom! Botimiz muvaffaqiyatli ishga tushdi! 🚀")

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer("Xabaringiz qabul qilindi!")

async def main():
    logging.basicConfig(level=logging.INFO)
    # Oldingi webhook'larni tozalab, pollingni boshlash
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
