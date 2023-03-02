from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def buy_keyboard(item_id):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Купить", callback_data=f"buy:{item_id}"),
            ]
        ]
    )