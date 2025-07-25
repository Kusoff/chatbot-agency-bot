from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from utils import safe_edit_message

router = Router()

tariffs_cases_text = (
    "Наши тарифы:\n\n"
    "🟢 Базовый\n"
    "Цена: 10 000 ₽\n"
    "Создание простого чат-бота для Telegram или WhatsApp.\n\n"
    "🟡 Оптимум\n"
    "Цена: 25 000 ₽\n"
    "Бот с расширенной логикой, интеграция с CRM, поддержка.\n\n"
    "🔴 Премиум\n"
    "Цена: от 50 000 ₽\n"
    "Полный комплекс: AI-боты, геймификация, аналитика, поддержка.\n\n"
    "Примеры кейсов:\n"
    "- Продажа товаров через Telegram-бот\n"
    "- Автоматизация службы поддержки\n"
    "- Интеграция с CRM и AI\n\n"
    "Для подробностей — оставьте заявку."
)

tariffs_cases_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🟢 Базовый", callback_data="tariff_basic")],
    [InlineKeyboardButton(text="🟡 Оптимум", callback_data="tariff_optimum")],
    [InlineKeyboardButton(text="🔴 Премиум", callback_data="tariff_premium")],
    [InlineKeyboardButton(text="📂 Подробнее о кейсах", callback_data="show_cases")],
    [InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_to_main")]
])

back_to_tariffs_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад к тарифам и кейсам", callback_data="back_to_tariffs_cases")]
])

cases_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад к тарифам и кейсам", callback_data="back_to_tariffs_cases")]
])


@router.callback_query(F.data == "tariffs_cases")
async def show_tariffs_cases(query: CallbackQuery):
    await safe_edit_message(
        query.message,
        text=tariffs_cases_text,
        reply_markup=tariffs_cases_kb
    )
    await query.answer()


@router.callback_query(F.data == "tariff_basic")
async def show_basic_tariff(query: CallbackQuery):
    text = (
        "🟢 *Базовый*\n\n"
        "Цена: 10 000 ₽\n"
        "Создание простого чат-бота для Telegram или WhatsApp.\n"
        "Идеально подходит для старта.\n"
    )
    await safe_edit_message(
        query.message,
        text=text,
        parse_mode="Markdown",
        reply_markup=back_to_tariffs_kb
    )
    await query.answer()


@router.callback_query(F.data == "tariff_optimum")
async def show_optimum_tariff(query: CallbackQuery):
    text = (
        "🟡 *Оптимум*\n\n"
        "Цена: 25 000 ₽\n"
        "Бот с расширенной логикой, интеграция с CRM, поддержка.\n"
        "Подходит для бизнеса, который хочет автоматизировать процессы.\n"
    )
    await safe_edit_message(
        query.message,
        text=text,
        parse_mode="Markdown",
        reply_markup=back_to_tariffs_kb
    )
    await query.answer()


@router.callback_query(F.data == "tariff_premium")
async def show_premium_tariff(query: CallbackQuery):
    text = (
        "🔴 *Премиум*\n\n"
        "Цена: от 50 000 ₽\n"
        "Полный комплекс: AI-боты, геймификация, аналитика, поддержка.\n"
        "Максимальные возможности для вашего бизнеса.\n"
    )
    await safe_edit_message(
        query.message,
        text=text,
        parse_mode="Markdown",
        reply_markup=back_to_tariffs_kb
    )
    await query.answer()


@router.callback_query(F.data == "show_cases")
async def show_cases(query: CallbackQuery):
    text = (
        "*Примеры кейсов:*\n"
        "- Продажа товаров через Telegram-бот\n"
        "- Автоматизация службы поддержки\n"
        "- Интеграция с CRM и AI\n"
    )
    await safe_edit_message(
        query.message,
        text=text,
        parse_mode="Markdown",
        reply_markup=cases_kb
    )
    await query.answer()


@router.callback_query(F.data == "back_to_tariffs_cases")
async def back_to_tariffs_cases(query: CallbackQuery):
    await safe_edit_message(
        query.message,
        text=tariffs_cases_text,
        reply_markup=tariffs_cases_kb
    )
    await query.answer()


@router.callback_query(F.data == "back_to_main")
async def back_to_main(query: CallbackQuery):
    from services import main_menu_kb  # замени на актуальный импорт
    await safe_edit_message(
        query.message,
        text="Главное меню:",
        reply_markup=main_menu_kb
    )
    await query.answer()
