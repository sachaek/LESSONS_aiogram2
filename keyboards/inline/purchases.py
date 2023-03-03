from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def buy_keyboard(item_id):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Купить", callback_data=f"buy:{item_id}"),
            ]
        ]
    )


paid_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Оплатил", callback_data="paid"),
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel"),
        ],
    ]
)