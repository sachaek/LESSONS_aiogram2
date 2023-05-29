import logging

from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.db_api import db_gino
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from loader import db


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    logging.info("Подключение к базе данных")
    await db_gino.on_startup(dp)
    logging.info("Готово")

    logging.info("Чистим базуданных")
    await db.gino.drop_all() # можно не чистить

    logging.info("Создаем таблицу пользователей")
    await db.gino.create_all()
    logging.info("Готово")

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

