from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from utils import safe_edit_message

router = Router()

# Импорт клавиатуры главного меню с правильным именем
from keyboards.main_menu import main_menu

# Кнопки с вопросами FAQ (расширенный список)
faq_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💸 Сколько стоит бот?", callback_data="faq_price")],
        [InlineKeyboardButton(text="⏳ За сколько сделаете?", callback_data="faq_time")],
        [InlineKeyboardButton(text="🛠 Какие технологии используете?", callback_data="faq_technologies")],
        [InlineKeyboardButton(text="🔑 Можете ли сделать под ключ?", callback_data="faq_full_service")],
        [InlineKeyboardButton(text="🏢 Работаете с юр. лицами?", callback_data="faq_corporate")],
        [InlineKeyboardButton(text="◀️ Назад в меню", callback_data="to_main")]
    ]
)


# Показываем список FAQ
@router.callback_query(F.data == "faq")
async def show_faq_menu(query: CallbackQuery):
    text = "📌 <b>Частые вопросы:</b>\n\nВыберите интересующий вопрос:"
    await safe_edit_message(query.message, text=text, reply_markup=faq_kb, parse_mode="HTML")
    await query.answer()


# Ответ: стоимость
@router.callback_query(F.data == "faq_price")
async def faq_price(query: CallbackQuery):
    text = (
        "<b>💸 Сколько стоит бот?</b>\n\n"
        "Базовые боты начинаются от 10 000 ₽.\n"
        "Проекты с интеграциями и AI — от 25 000 до 50 000 ₽.\n"
        "Точная стоимость зависит от задач — расскажите, что нужно, и мы подготовим предложение."
    )
    await safe_edit_message(query.message, text=text, reply_markup=faq_kb, parse_mode="HTML")
    await query.answer()


# Ответ: сроки
@router.callback_query(F.data == "faq_time")
async def faq_time(query: CallbackQuery):
    text = (
        "<b>⏳ За сколько сделаете?</b>\n\n"
        "В среднем разработка занимает от 2 до 7 дней в зависимости от сложности.\n"
        "Для срочных задач обсуждаем сроки индивидуально."
    )
    await safe_edit_message(query.message, text=text, reply_markup=faq_kb, parse_mode="HTML")
    await query.answer()


# Ответ: технологии
@router.callback_query(F.data == "faq_technologies")
async def faq_technologies(query: CallbackQuery):
    text = (
        "<b>🛠 Какие технологии используете?</b>\n\n"
        "Мы работаем с Telegram, WhatsApp, CRM-системами, сайтами, а также интегрируем AI-сервисы:\n"
        "- ChatGPT API\n"
        "- Dialogflow\n"
        "- Другие современные технологии и платформы под ваши задачи."
    )
    await safe_edit_message(query.message, text=text, reply_markup=faq_kb, parse_mode="HTML")
    await query.answer()


# Ответ: под ключ
@router.callback_query(F.data == "faq_full_service")
async def faq_full_service(query: CallbackQuery):
    text = (
        "<b>🔑 Можете ли сделать под ключ?</b>\n\n"
        "Да, мы можем разработать бота под ключ — от идеи и дизайна до полной интеграции и запуска."
    )
    await safe_edit_message(query.message, text=text, reply_markup=faq_kb, parse_mode="HTML")
    await query.answer()


# Ответ: юридические лица
@router.callback_query(F.data == "faq_corporate")
async def faq_corporate(query: CallbackQuery):
    text = (
        "<b>🏢 Работаете с юридическими лицами?</b>\n\n"
        "Да, мы сотрудничаем как с физическими, так и с юридическими лицами.\n"
        "Возможна работа по договорам и выставление счетов."
    )
    await safe_edit_message(query.message, text=text, reply_markup=faq_kb, parse_mode="HTML")
    await query.answer()


# Назад в главное меню
@router.callback_query(F.data == "to_main")
async def back_to_main(query: CallbackQuery):
    await safe_edit_message(query.message, text="Вы в главном меню 👇", reply_markup=main_menu)
    await query.answer()
