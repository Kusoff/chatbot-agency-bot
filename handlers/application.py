from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import re
from sheets import add_lead_to_sheet

from config import ADMIN_ID

router = Router()

main_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💼 Что мы делаем", callback_data="services")],
        [InlineKeyboardButton(text="💰 Тарифы и кейсы", callback_data="tariffs_cases")],
        [InlineKeyboardButton(text="📝 Оставить заявку", callback_data="application")],
        [InlineKeyboardButton(text="❓ Частые вопросы", callback_data="faq")],
        [InlineKeyboardButton(text="📞 Связаться с нами", callback_data="contact")]
    ]
)

cancel_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="❌ Отменить", callback_data="cancel_application")]
    ]
)


class ApplicationForm(StatesGroup):
    name = State()
    contact = State()
    description = State()


@router.callback_query(F.data == "application")
async def start_application(query: CallbackQuery, state: FSMContext):
    await state.set_state(ApplicationForm.name)
    # Отправляем новое сообщение с просьбой ввести имя и сохраняем message_id
    sent = await query.message.edit_text("Введите ваше имя:", reply_markup=cancel_kb)
    # Сохраняем id сообщения бота для последующего редактирования
    await state.update_data(bot_message_id=sent.message_id)
    await query.answer()


@router.callback_query(F.data == "cancel_application")
async def cancel_handler(query: CallbackQuery, state: FSMContext):
    await state.clear()
    await query.message.edit_text("Заявка отменена ✅", reply_markup=main_menu_kb)
    await query.answer()


@router.message(ApplicationForm.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ApplicationForm.contact)
    await message.delete()

    data = await state.get_data()
    bot_message_id = data.get("bot_message_id")

    # Редактируем сообщение бота, чтобы запросить контакт
    await message.bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=bot_message_id,
        text="Укажите номер телефона или ваш @username:",
        reply_markup=cancel_kb
    )


@router.message(ApplicationForm.contact)
async def get_contact(message: Message, state: FSMContext):
    contact = message.text
    data = await state.get_data()
    bot_message_id = data.get("bot_message_id")

    if not is_valid_contact(contact):
        await message.delete()
        await message.bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=bot_message_id,
            text="❌ Введите корректный номер телефона (+7...) или @username.",
            reply_markup=cancel_kb
        )
        return

    await state.update_data(contact=contact)
    await state.set_state(ApplicationForm.description)
    await message.delete()

    await message.bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=bot_message_id,
        text="Опишите задачу / что нужно сделать:",
        reply_markup=cancel_kb
    )


@router.message(ApplicationForm.description)
async def get_description(message: Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    contact = data.get("contact")
    description = message.text
    bot_message_id = data.get("bot_message_id")

    # Сохраняем в Google Sheets
    add_lead_to_sheet(name, contact, description)

    await state.clear()
    await message.delete()

    text = (
        f"📩 Новая заявка\n\n"
        f"👤 Имя: {name}\n"
        f"📱 Контакт: {contact}\n"
        f"📝 Задача: {description}"
    )
    await message.bot.send_message(ADMIN_ID, text)

    await message.bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=bot_message_id,
        text="Спасибо! Мы свяжемся в течение 1 рабочего дня 🙌",
        reply_markup=main_menu_kb
    )


def is_valid_contact(value: str) -> bool:
    phone_pattern = r"^\+?\d{10,15}$"
    username_pattern = r"^@[\w\d_]{5,}$"
    return bool(re.match(phone_pattern, value) or re.match(username_pattern, value))
