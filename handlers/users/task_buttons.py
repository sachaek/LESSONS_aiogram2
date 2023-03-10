from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from keyboards.inline.keyboard_task_3 import keyboard_fruit
from loader import dp, bot
from aiogram import types


apple_photo = "https://images.unsplash.com/photo-1579613832125-5d34a13ffe2a?ixlib=rb-4.0.3&ixid" \
              "=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
orange_photo = "https://images.unsplash.com/photo-1557800636-894a64c1696f?ixlib=rb-4.0.3&ixid" \
               "=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=765&q=80"

items = [
    {'item_id': 1, 'item_name': 'apple', 'item_photo': apple_photo},
    {'item_id': 2, 'item_name': 'orange', 'item_photo': orange_photo}
]


@dp.message_handler(Command("items"))
async def start(message: types.Message):
    for item in items:
        await message.answer_photo(photo=item['item_photo'],
                                   caption=item['item_name'],
                                   reply_markup=keyboard_fruit(item))


@dp.callback_query_handler(text_contains="Buy")  # Текст в callback'е содержит "buy"
async def create_invoice(call: types.CallbackQuery):
    await call.answer(cache_time=60)  # Чтобы нельзя было нажимать на кнопку "buy" много раз
    item_id = call.data.split("_")[-1]
    item_id = int(item_id)
    item: dict = items[item_id]
    await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f"Покупай товар номер Buy_{item_id}")
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message, reply_markup=None)


@dp.callback_query_handler(text_contains="dislike")
async def cancel_payment(call: types.CallbackQuery):
    await call.answer(text="Тебе не понравился этот товар", cache_time=3)


@dp.callback_query_handler(text_contains="like")
async def cancel_payment(call: types.CallbackQuery):
    await call.answer(text="Тебе понравился этот товар", cache_time=3)



