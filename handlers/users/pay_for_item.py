from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hlink, hcode

from data import config
from data.items import items
from keyboards.inline.purchases import buy_keyboard, paid_keyboard
from loader import dp
from utils.misc.qiwi import Payment, NoPaymentFound, NotEnoughMoney


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
        reply_markup=paid_keyboard
    )
    await state.set_state("qiwi")
    await state.update_data(payment=payment)


@dp.callback_query_handler(text="cancel", state="qiwi")
async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Отменено")
    await state.finish()


@dp.callback_query_handler(text_contains="paid", state="qiwi")
async def approve_payment(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    payment: Payment = data.get("payment")
    try:
        payment.check_payment()
    except NoPaymentFound:
        await call.message.answer("Транзакция не найдена")
        return
    except NotEnoughMoney:
        await call.message.answer("Оплаченная сумма меньше необходимой")
        return
    else:
        await call.message.answer("Успешно оплачено")
    await call.message.delete_reply_markup()
    await state.finish()