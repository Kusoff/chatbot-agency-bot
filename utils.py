from aiogram.exceptions import TelegramBadRequest


async def safe_edit_message(message, text=None, reply_markup=None, **kwargs):
    try:
        await message.edit_text(text=text, reply_markup=reply_markup, **kwargs)
    except TelegramBadRequest as e:
        if "message is not modified" in str(e):
            # Игнорируем ошибку, если текст и клавиатура не изменились
            pass
        else:
            raise
