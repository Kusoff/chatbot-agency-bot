from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from utils import safe_edit_message

router = Router()

main_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Что мы делаем", callback_data="services")],
        [InlineKeyboardButton(text="Тарифы и кейсы", callback_data="tariffs_cases")],
        [InlineKeyboardButton(text="Оставить заявку", callback_data="application")],
        [InlineKeyboardButton(text="Частые вопросы", callback_data="faq")],
        [InlineKeyboardButton(text="Связаться с нами", callback_data="contact")]
    ]
)

services_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔹 Боты для продаж", callback_data="service_sales")],
        [InlineKeyboardButton(text="🔹 Поддержка клиентов", callback_data="service_support")],
        [InlineKeyboardButton(text="🔹 Автоматизация HR и обучения", callback_data="service_hr")],
        [InlineKeyboardButton(text="🔹 Игровые боты (геймификация)", callback_data="service_gamification")],
        [InlineKeyboardButton(text="🔹 AI-боты (ChatGPT API, Dialogflow)", callback_data="service_ai")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")]
    ]
)


@router.callback_query(F.data == "services")
async def show_services(query: CallbackQuery):
    await safe_edit_message(
        query.message,
        text="Что мы делаем? Выберите направление:",
        reply_markup=services_kb
    )
    await query.answer()


@router.callback_query(F.data == "service_sales")
async def service_sales_handler(query: CallbackQuery):
    await safe_edit_message(
        query.message,
        text="🔹 *Боты для продаж*\n\nМы создаём ботов, которые помогают увеличить продажи, автоматизируют воронки и делают продажи 24/7.",
        parse_mode="Markdown",
        reply_markup=services_kb
    )
    await query.answer()


@router.callback_query(F.data == "service_support")
async def service_support_handler(query: CallbackQuery):
    await safe_edit_message(
        query.message,
        text="🔹 *Поддержка клиентов*\n\nБоты, которые быстро отвечают на вопросы клиентов, решают стандартные задачи и экономят время вашей службы поддержки.",
        parse_mode="Markdown",
        reply_markup=services_kb
    )
    await query.answer()


@router.callback_query(F.data == "service_hr")
async def service_hr_handler(query: CallbackQuery):
    await safe_edit_message(
        query.message,
        text="🔹 *Автоматизация HR и обучения*\n\nБоты для рекрутинга, адаптации новых сотрудников и проведения тренингов и опросов.",
        parse_mode="Markdown",
        reply_markup=services_kb
    )
    await query.answer()


@router.callback_query(F.data == "service_gamification")
async def service_gamification_handler(query: CallbackQuery):
    await safe_edit_message(
        query.message,
        text="🔹 *Игровые боты (геймификация)*\n\nИгровые механики и викторины для вовлечения клиентов и сотрудников.",
        parse_mode="Markdown",
        reply_markup=services_kb
    )
    await query.answer()


@router.callback_query(F.data == "service_ai")
async def service_ai_handler(query: CallbackQuery):
    await safe_edit_message(
        query.message,
        text="🔹 *AI-боты (ChatGPT API, Dialogflow)*\n\nИнтеграции с AI-моделями для интеллектуального общения и автоматизации сложных задач.",
        parse_mode="Markdown",
        reply_markup=services_kb
    )
    await query.answer()


@router.callback_query(F.data == "back_to_main")
async def back_to_main_handler(query: CallbackQuery):
    await safe_edit_message(
        query.message,
        text="Главное меню:",
        reply_markup=main_menu_kb
    )
    await query.answer()
