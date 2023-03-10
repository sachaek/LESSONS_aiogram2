from aiogram.types import InlineKeyboardMarkup, inline_keyboard, InlineKeyboardButton

from keyboards.inline.callback_datas import callback_task_3


# buttons = """
# Edit Name            Edit Description
# Edit About           Edit Botpic
# Edit Commands        <<Back to Bot"""
#
# keyboard = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
#     [
#         InlineKeyboardButton(text='Edit Name', callback_data=callback_task_3.new(action="Name")),
#         InlineKeyboardButton(text='Edit Description', callback_data=callback_task_3.new(action="Description"))
#     ],
#     [
#         InlineKeyboardButton(text='Edit About', callback_data=callback_task_3.new(action="About")),
#         InlineKeyboardButton(text='Edit Botpic', callback_data=callback_task_3.new(action="Botpic"))
#     ],
#     [
#         InlineKeyboardButton(text='Edit Commands', callback_data=callback_task_3.new(action="Commands")),
#         InlineKeyboardButton(text='<<Back to Bot', callback_data=callback_task_3.new(action="Back"))
#     ]
# ])
#

def keyboard_fruit(item):
    item_id = item['item_id']
    keyboard = InlineKeyboardMarkup()
    button_buy = InlineKeyboardButton(text="Купить товар", callback_data=callback_task_3.new(action=f"Buy_{item_id}"))
    button_like = InlineKeyboardButton(text="👍", callback_data=callback_task_3.new(action=f"like_{item_id}"))
    button_dislike = InlineKeyboardButton(text="👎", callback_data=callback_task_3.new(action=f"dislike_{item_id}"))
    button_share = InlineKeyboardButton(text="Поделиться с другом", switch_inline_query=f"Share_{item_id}")
    keyboard.add(button_buy).add(button_like, button_dislike).add(button_share)
    return keyboard



