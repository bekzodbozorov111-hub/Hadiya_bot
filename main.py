import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = "8675282028:AAHWDg1ETn7RTJm_XqR8peaw5Loa-enb1E"

# Karta ma'lumotlaringiz
CARD_NUMBER = "9860060943606529"
CARD_HOLDER = "BEKZOD B."

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="👑 Telegram Premium", callback_data="premium_menu")
    builder.button(text="⭐ Telegram Stars", callback_data="stars_menu")
    builder.button(text="🎁 Sovg'alar (Gifts)", callback_data="gifts_menu")
    builder.button(text="👤 Profilim", callback_data="profile")
    builder.adjust(1, 1, 1, 1)
    return builder.as_markup()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    await message.answer(
        "👋 **Hadiya Gift Botiga xush kelibsiz!**\n\n"
        "Bu yerda Telegram Premium, Stars va sovg'alarni anonim yoki o'z nomingizdan xarid qilishingiz mumkin.\n\n"
        "Kerakli bo'limni tanlang:",
        reply_markup=get_main_menu(),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "premium_menu")
async def premium_menu(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(text="3 oylik — 150.000 so'm", callback_data="type_prem_3")
    builder.button(text="6 oylik — 220.000 so'm", callback_data="type_prem_6")
    builder.button(text="12 oylik — 380.000 so'm", callback_data="type_prem_12")
    builder.button(text="⬅️ Ortga", callback_data="back_to_main")
    builder.adjust(1)
    
    await callback.message.edit_text(
        "👑 **Telegram Premium Obunalari**\n\n"
        "💡 *Bonus:* Premium xarid qilganlarga **1 ta bepul ayiqcha gift** qo'shib beriladi!\n\n"
        "Muddatni tanlang:",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data == "stars_menu")
async def stars_menu(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    stars_list = [
        ("100 Stars — 30.000 so'm", "type_star_100"),
        ("150 Stars — 70.000 so'm", "type_star_150"),
        ("250 Stars — 70.000 so'm", "type_star_250"),
        ("350 Stars — 90.000 so'm", "type_star_350"),
        ("500 Stars — 120.000 so'm", "type_star_500"),
        ("750 Stars — 185.000 so'm", "type_star_750"),
        ("1000 Stars — 250.000 so'm", "type_star_1000"),
        ("1500 Stars — 360.000 so'm", "type_star_1500"),
        ("2500 Stars — 590.000 so'm", "type_star_2500"),
        ("5000 Stars — 1.200.000 so'm", "type_star_5000"),
        ("10000 Stars — 2.350.000 so'm", "type_star_10000"),
    ]
    for text, cdata in stars_list:
        builder.button(text=text, callback_data=cdata)
    builder.button(text="⬅️ Ortga", callback_data="back_to_main")
    builder.adjust(2, 2, 2, 2, 2, 1)

    await callback.message.edit_text(
        "⭐ **Telegram Stars (Yulduzlar):**\n\nMiqdorni tanlang:",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data == "gifts_menu")
async def gifts_menu(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    gifts = [
        ("🧸 Ayiqcha — 5.000 so'm", "type_gift_ayiq"),
        ("❤️ Yurak — 5.000 so'm", "type_gift_yurak"),
        ("🎁 Sovg'a qutisi — 8.000 so'm", "type_gift_quti"),
        ("🌹 Qizil o'rinul — 8.000 so'm", "type_gift_gul"),
        ("🎂 Tug'ilgan kun torti — 14.000 so'm", "type_gift_tort"),
        ("💐 Gullar — 14.000 so'm", "type_gift_gullar"),
        ("🐈 Pantera — 14.000 so'm", "type_gift_pantera"),
        ("🧩 Rubik — 27.000 so'm", "type_gift_rubik"),
        ("💍 Uzuk — 27.000 so'm", "type_gift_uzuk"),
        ("💎 Olmos — 27.000 so'm", "type_gift_olmos"),
    ]
    for text, cdata in gifts:
        builder.button(text=text, callback_data=cdata)
    builder.button(text="⬅️ Ortga", callback_data="back_to_main")
    builder.adjust(2, 2, 2, 2, 2, 1)

    await callback.message.edit_text(
        "🎁 **Eksklyuziv Sovg'alar:**\n\nSovg'ani tanlang:",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("type_"))
async def select_quantity(callback: types.CallbackQuery):
    item_code = callback.data.replace("type_", "")
    builder = InlineKeyboardBuilder()
    builder.button(text="1 ta", callback_data=f"qty_{item_code}_1")
    builder.button(text="3 ta", callback_data=f"qty_{item_code}_3")
    builder.button(text="5 ta", callback_data=f"qty_{item_code}_5")
    builder.button(text="10 ta", callback_data=f"qty_{item_code}_10")
    builder.button(text="⬅️ Ortga", callback_data="gifts_menu")
    builder.adjust(2, 2, 1)

    await callback.message.edit_text(
        "🔢 **Miqdorini belgilang:**\n\nNechta xarid qilmoqchisiz?",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("qty_"))
async def select_privacy(callback: types.CallbackQuery):
    parts = callback.data.split("_")
    data_info = f"{parts[1]}_{parts[2]}" if len(parts) > 3 else parts[1]
    count = parts[-1]

    builder = InlineKeyboardBuilder()
    builder.button(text="👤 O'z ismim bilan yuborish", callback_data=f"pay_{data_info}_{count}_public")
    builder.button(text="🥷 Anonim tarzda yuborish", callback_data=f"pay_{data_info}_{count}_anon")
    builder.button(text="⬅️ Ortga", callback_data="gifts_menu")
    builder.adjust(1, 1, 1)

    await callback.message.edit_text(
        f"🕵️ **Yuborish turini tanlang:**\n\n"
        f"Tanlangan miqdor: **{count} ta**\n"
        "Qabul qiluvchiga ismingiz ko'rinsinmi yoki sir qolsinmi?",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("pay_"))
async def choose_payment_system(callback: types.CallbackQuery):
    payload = callback.data.replace("pay_", "")

    builder = InlineKeyboardBuilder()
    builder.button(text="💳 Karta raqamini olish", callback_data=f"show_card_{payload}")
    builder.button(text="⬅️ Ortga", callback_data="back_to_main")
    builder.adjust(1)

    await callback.message.edit_text(
        "💳 **To'lov usuli:**\n\n"
        "Quyidagi tugmani bosib karta raqamiga o'tkazing:",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("show_card_"))
async def show_card_details(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(text="🔄 Asosiy menyuga qaytish", callback_data="back_to_main")

    await callback.message.edit_text(
        f"💳 **To'lov uchun karta ma'lumotlari:**\n\n"
        f"• Karta raqami: `{CARD_NUMBER}`\n"
        f"• Karta egasi: **{CARD_HOLDER}**\n\n"
        f"⚠️ *Izoh:* To'lovni amalga oshirgach, chekni (skrinshotni) adminga yuboring!",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data == "profile")
async def profile_menu(callback: types.CallbackQuery):
    user = callback.from_user
    builder = InlineKeyboardBuilder()
    builder.button(text="⬅️ Ortga", callback_data="back_to_main")
    
    await callback.message.edit_text(
        f"👤 **Sizning profilingiz:**\n\n"
        f"• Ism: {user.full_name}\n"
        f"• ID: `{user.id}`\n"
        f"• Username: @{user.username if user.username else 'Mavjud emas'}\n"
        f"• Balans: **0 so'm**",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data == "back_to_main")
async def back_to_main(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "👋 **Asosiy menyu:**\n\nKerakli bo'limni tanlang:",
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
    
