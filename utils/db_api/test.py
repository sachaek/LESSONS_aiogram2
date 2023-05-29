import asyncio

from data import config
from utils.db_api.db_gino import db
from utils.db_api.schemas import quick_commands


async def test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    print("Добавляем пользователей")
    await quick_commands.add_user(1, "One", "email")
    await quick_commands.add_user(2, "ga", "randomuser1234@gmail.com")
    await quick_commands.add_user(3, "asf", "testmail456@hotmail.com")
    await quick_commands.add_user(4, "asg", "examplemail789@yahoo.com")
    await quick_commands.add_user(5, "tgd", "asgsag3432@yahoo.com")
    print("Готово")

    users = await quick_commands.select_all_users()
    print(f"Получил всех пользователей: {users}")

    user = await quick_commands.select_user(id=4)
    print(f"Получил пользователя: {user}")

    count = await quick_commands.count_users()
    print(f"Всего пользователей: {count}")

    users = list(map(str, await quick_commands.select_all_users()))
    print(f"строки пользователей:\n "
          f"==================\n"
          f" {users}\n"
          f"==================\n")

loop = asyncio.get_event_loop()
loop.run_until_complete(test())

