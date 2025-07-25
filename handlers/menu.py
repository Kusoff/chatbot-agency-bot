from aiogram import Router, types, F
from keyboards.main_menu import main_menu

router = Router()


@router.message(F.text == "/start")
async def cmd_start(message: types.Message):
    await message.answer(
        "<b>Привет!</b>\nЯ — бот студии по созданию чат-ботов.\nВыберите, что вас интересует:",
        reply_markup=main_menu
    )
