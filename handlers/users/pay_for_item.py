from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    caption = """
    Название продукта: {title}
    <i>Описание продукта:</i>
    {description}
    
    <u>Цена:</u> {price:.2f} <b>руб.</b>
    """
    items = []
    for item in items:
        await message.answer_photo(photo=item.photo_link,
                                   caption=caption.format(
                                       title=item.title,
                                       description=item.description,
                                       price=item.price,
                                   ),
                                   reply_markup=buy_keyboard(item.id)
                                   )
