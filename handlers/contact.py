from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.main_menu import main_menu
from utils import safe_edit_message

router = Router()


@router.callback_query(F.data == "contact")
async def contact_us_handler(query: CallbackQuery):
    text = (
        "📞 Менеджер: @yourmanager\n"
        "📧 Почта: bots@example.com"
    )
    await safe_edit_message(query.message, text=text, reply_markup=main_menu)
    await query.answer()
