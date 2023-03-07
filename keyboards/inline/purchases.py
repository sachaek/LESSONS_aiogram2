from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def buy_keyboard(item_id) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.insert(InlineKeyboardButton(text="Купить", callback_data=f"buy:{item_id}"))
    return keyboard


# def buy_keyboard_2(item_id) -> InlineKeyboardMarkup:
#     keyb = InlineKeyboardMarkup(
#         [
#             [InlineKeyboardButton(text="Купить", callback_data=f"buy:{item_id}")],
#         ]
#     )
#     return keyb


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