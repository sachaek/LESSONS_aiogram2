import asyncio

QUERY = """INSERT INTO test_table VALUES ($1, $2, $3)"""


async def make_request():
    print("Я делаю запрос в БД")
    await asyncio.sleep(0.1)


async def main():
    for x in range(10_000):
        task = asyncio.create_task(make_request())
        await asyncio.gather(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
