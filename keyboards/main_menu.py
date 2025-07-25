from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💼 Что мы делаем", callback_data="services")],
        [InlineKeyboardButton(text="💰 Тарифы и кейсы", callback_data="tariffs_cases")],
        [InlineKeyboardButton(text="📝 Оставить заявку", callback_data="application")],
        [InlineKeyboardButton(text="❓ Частые вопросы", callback_data="faq")],
        [InlineKeyboardButton(text="📞 Связаться с нами", callback_data="contact")]
    ]
)
