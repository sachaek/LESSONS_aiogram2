import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(
            full_name=message.from_user.full_name,
        telegram_id=message.from_user.id,
        username=message.from_user.username)

    except asyncpg.exceptions.UniqueViolationError as e:
        user = await db.select_user(telegram_id=message.from_user.id)

    count_users = await db.count_users()
    users_data = list(user)
    user_data_dict = dict(user)

    username = user.get("username")
    full_name = user[1]

    await message.answer(
        "\n".join(
            [
                f'Привет, {message.from_user.full_name}',
                f'Ты был занесен в базу',
                f'В базе <b>{count_users}</b> пользователей',
                f'',
                f'<code>User: {username} - {full_name}',
                f'{users_data=}',
                f'{user_data_dict=}</code>'
            ]
        )
    )


    # await message.answer(f"Привет, {message.from_user.full_name}!")
