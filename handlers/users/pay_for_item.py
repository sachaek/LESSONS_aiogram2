from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hlink, hcode

from data import config
from data.items import items
from keyboards.inline.purchases import buy_keyboard
from loader import dp
from utils.misc.qiwi import Payment


@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    caption = """
    Название продукта: {title}
    <i>Описание продукта:</i>
    {description}
    
    <u>Цена:</u> {price:.2f} <b>руб.</b>
    """

    for item in items:
        await message.answer_photo(photo=item.photo_link,
                                   caption=caption.format(
                                       title=item.title,
                                       description=item.description,
                                       price=item.price,
                                   ),
                                   reply_markup=buy_keyboard(item_id=item.id)
                                   )


@dp.callback_query_handler(text_contains="buy")  # Текст в callback'е содержит "buy"
async def create_invoice(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)  # Чтобы нельзя было нажимать на кнопку "buy" много раз
    item_id = call.data.split(":")[-1]
    item_id = int(item_id) - 1  # Вычитаем потому что в питоне счет с 0, а в items первое id = 1
    item = items[item_id]
    amount = item.price

    payment = Payment(amount=amount)
    payment.create()
    await call.message.answer(
        "\n".join(
            [
                f"Оплатите не менее {amount:.2f} по номеру телефона или по адресу",
                "",
                hlink(config.WALLET_QIWI, url=payment.invoice),
                "И обязательно укажите ID платежа:",
                hcode(payment.id)
            ]
        ),
        reply_markup=paid_keyboard()
    )
