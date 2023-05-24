import logging

from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from loader import db


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    logging.info("Подключение к базе данных")
    await db.create()
    await db.test_connection()
    await db.drop_users() # для тестового режима
    logging.info("Создаем таблицу пользователей")
    await db.create_table()
    logging.info("Готово")
    await set_default_commands(dispatcher)



    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

