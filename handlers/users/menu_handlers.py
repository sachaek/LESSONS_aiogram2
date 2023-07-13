from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import CommandStart, Command
from aiogram.types import CallbackQuery

from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await list_catgories(message)


async def list_catgories(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await categories_keyboard()