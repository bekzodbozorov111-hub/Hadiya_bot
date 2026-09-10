import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = "8675282028:AAG00ys5IwGEFP_PxHsTkaT93muiYPqRgP4"

CARD_NUMBER = "9860060943606529"
CARD_HOLDER = "BEKZOD B."
REVIEWS_LINK = "https://t.me/+YU4o3av-C5w2MjZi"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="🎁 Sovg'alar", callback_data="gifts_menu")
    builder.button(text="👑 Telegram Premium", callback_data="premium_menu")
    builder.button(text="💬 Otzivlar", url=REVIEWS_LINK)
    builder.button(text="📊 Statistikam", callback_data="stats")
    builder.button(text="👤 Profil", callback_data="profile")
    builder.button(text="ℹ️ Bot haqida", callback_data="about")
    builder.button(text="🌐 Til", callback_data="lang")
    builder.adjust(1, 1, 1, 2, 2)
    return builder.as_markup()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    await message.answer(
        f"👋 Assalomu alaykum, {message.from_user.first_name} Xush kelibsiz!\n\n"
        "🎁 SovgaBot orqali siz yaqinlaringizga sovg'alar ulashishingiz mumkin.\n\n"
        "🟩 Quyidagi menyudan kerakli xizmatni tanlang. 👇",
        reply_markup=get_main_menu(),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "gifts_menu")
async def gifts_menu(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    gifts = [
        ("💖 | 2,900 so'm", "gift_bantik"),
        ("🧸 | 3,000 so'm", "gift_ayiq"),
        ("🌹 | 5,100 so'm", "gift_gul"),
        ("🎁 | 5,250 so'm", "gift_quti"),
        ("🧸 | 10,999 so'm", "gift_bear1"),
        ("🧸 | 11,000 so'm", "gift_bear2"),
        ("💖 | 11,200 so'm", "gift_heart"),
        ("🧸 | 11,500 so'm", "gift_bear3"),
        ("🎉 | 11,500 so'm", "gift_party"),
        ("🐰 | 11,500 so'm", "gift_rabbit"),
        ("🧸 | 11,500 so'm", "gift_bear4"),
        ("🎄 | 11,500 so'm", "gift_tree"),
        ("🥳 | 11,500 so'm", "gift_party2"),
        ("🍀 | 11,500 so'm", "gift_clover"),
        ("🌸 | 11,500 so'm", "gift_sakura"),
        ("🍾 | 11,500 so'm", "gift_shampan"),
        ("🚀 | 11,500 so'm", "gift_rocket"),
        ("💐 | 11,500 so'm", "gift_gullar"),
        ("🎂 | 11,500 so'm", "gift_tort"),
        ("🏆 | 23,000 so'm", "gift_kubok"),
        ("💍 | 23,000 so'm", "gift_uzuk"),
        ("💎 | 23,000 so'm", "gift_olmos")
    ]
    for text, cdata in gifts:
        builder.button(text=text, callback_data=cdata)
    builder.button(text="⬅️ Orqaga", callback_data="back_to_main")
    builder.adjust(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1)

    await callback.message.edit_text(
        "🖼️ Iltimos, yuborish uchun kerakli Giftni tanlang:",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data == "premium_menu")
async def premium_menu(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(text="👑 3 oylik — 150.000 so'm", callback_data="prem_3")
    builder.button(text="👑 6 oylik — 220.000 so'm", callback_data="prem_6")
    builder.button(text="👑 12 oylik — 380.000 so'm", callback_data="prem_12")
    builder.button(text="⬅️ Orqaga", callback_data="back_to_main")
    builder.adjust(1)
    
    await callback.message.edit_text(
        "👑 **Telegram Premium Obunalari**\n\n"
        "Muddatni tanlang:",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("gift_"))
async def gift_configure(callback: types.CallbackQuery):
    gift_id = callback.data
    builder = InlineKeyboardBuilder()
    builder.button(text="🟢 Anonim yuborish", callback_data=f"anon_toggle_{gift_id}")
    builder.button(text="💬 Izoh qo'shish", callback_data=f"comment_{gift_id}")
    builder.button(text="➖", callback_data=f"dec_{gift_id}_1")
    builder.button(text="1 ta", callback_data="none")
    builder.button(text="➕", callback_data=f"inc_{gift_id}_1")
    builder.button(text="✅ Tasdiqlash", callback_data=f"recipient_{gift_id}_1")
    builder.button(text="⬅️ Orqaga", callback_data="gifts_menu")
    builder.adjust(1, 1, 3, 1, 1)

    await callback.message.edit_text(
        "🧸 **Gift xaridi**\n\n"
        "▪️ Narxi: 3 000 so'm / dona\n"
        "▪️ Miqdori: 1 ta\n"
        "▪️ Jami: 3 000 so'm\n\n"
        "👇 Sozlamalarni tanlab, pastdagi \"Tasdiqlash\" tugmasini bosing.",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("recipient_"))
async def choose_recipient(callback: types.CallbackQuery):
    payload = callback.data.replace("recipient_", "")
    builder = InlineKeyboardBuilder()
    builder.button(text=f"👤 O'zimga (@{callback.from_user.username or 'user'})", callback_data=f"pay_self_{payload}")
    builder.button(text="👥 Do'stiga yuborish", callback_data=f"pay_friend_{payload}")
    builder.button(text="❌ Bekor qilish", callback_data="back_to_main")
    builder.adjust(1, 1, 1)

    await callback.message.edit_text(
        "🎯 **Foydalanuvchi nomi**\n\n"
        "👉 Biz Telegram Gift'ni qaysi profilga yuborishimizni aniqlashtirib olishimiz kerak\n\n"
        "Masalan: `@SovgaManager`",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("pay_"))
async def show_final_payment(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(text="🔄 Asosiy menyuga qaytish", callback_data="back_to_main")

    await callback.message.edit_text(
        f"✨ **Haridingiz uchun tashakkur!**\n\n"
        f"💳 **To'lov uchun karta ma'lumotlari:**\n\n"
        f"• Karta raqami: `{CARD_NUMBER}`\n"
        f"• Karta egasi: **{CARD_HOLDER}**\n\n"
        f"⚠️ *Izoh:* To'lovni amalga oshirgach, chekni adminga yuboring! "
        f"Tasdiqlangandan so'ng bot sovg'ani avtomatik tarzda taqdim etadi.",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data == "profile")
async def profile_menu(callback: types.CallbackQuery):
    user = callback.from_user
    builder = InlineKeyboardBuilder()
    builder.button(text="⬅️ Orqaga", callback_data="back_to_main")
    
    await callback.message.edit_text(
        f"👤 **Sizning profilingiz:**\n\n"
        f"• Ism: {user.full_name}\n"
        f"• ID: `{user.id}`\n"
        f"• Username: @{user.username if user.username else 'Mavjud emas'}",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data.in_({"stats", "about", "lang"}))
async def dummy_menus(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(text="⬅️ Orqaga", callback_data="back_to_main")
    await callback.message.edit_text("Tez kunda ishga tushadi! 🚀", reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "back_to_main")
async def back_to_main(callback: types.CallbackQuery):
    await callback.message.edit_text(
        f"👋 Assalomu alaykum, {callback.from_user.first_name} Xush kelibsiz!\n\n"
        "🎁 SovgaBot orqali siz yaqinlaringizga sovg'alar ulashishingiz mumkin.\n\n"
        "🟩 Quyidagi menyudan kerakli xizmatni tanlang. 👇",
        reply_markup=get_main_menu(),
        parse_mode="Markdown"
    )
    await callback.answer()

async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
