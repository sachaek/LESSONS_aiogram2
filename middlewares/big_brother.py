import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import banner_users


class BigBrother(BaseMiddleware):
    # async def <>on_point</>_<>event_type</>:
    #1
    async def on_pre_process_update(self, update: types.Update, data: dict):
        logging.info("[----------Новый апдейт!----------")
        logging.info("1. Pre Process Update")
        logging.info("Следующая точка: Process Update")
        data['middleware_data'] = "Это пройдет до on_post_process_update"
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return

        if user in banner_users:  # желательно баннер юзерс чтоб был из db
            raise CancelHandler()  # прекращается обработка апдейта

    #2
    async def on_process_update(self, update: types.Update, data: dict):
        logging.info(f"2 on process Update, {data=}")
        logging.info("Следующая точка: Pre Process Message")

    #3
    async def on_pre_process_message(self, message: types.Message, data: dict):  # there is other data
        logging.info(f'3.pre process message, {data=}')
        logging.info("Следующая точка: Filters, Process Message")
        data["middleware_data"] = "Это попадет в on_process_message"

    #4 filters

    #5
    async def on_process_message(self, message: types.Message, data: dict):
        logging.info(f'5. on process message, {data=}')
        logging.info('Следующая точка handler')
        data['middleware_data']= "это попадет в хендлер"

# executor.py [LINE:362] #INFO     [2023-02-22 17:59:17,975]  Bot: Test [@sacha_ekb_bot]
# executor.py [LINE:358] #WARNING  [2023-02-22 17:59:18,113]  Updates were skipped successfully.
# dispatcher.py [LINE:358] #INFO     [2023-02-22 17:59:18,287]  Start polling.
# big_brother.py [LINE:14] #INFO     [2023-02-22 17:59:30,917]  [----------Новый апдейт!----------
# big_brother.py [LINE:15] #INFO     [2023-02-22 17:59:30,917]  1. Pre Process Update
# big_brother.py [LINE:16] #INFO     [2023-02-22 17:59:30,917]  Следующая точка: Process Update
# big_brother.py [LINE:30] #INFO     [2023-02-22 17:59:30,917]  2 on process Update, data={'middleware_data': 'Это пройдет до on_post_process_update'}
# big_brother.py [LINE:31] #INFO     [2023-02-22 17:59:30,917]  Следующая точка: Pre Process Message
# big_brother.py [LINE:35] #INFO     [2023-02-22 17:59:30,917]  3.pre process message, data={}
# big_brother.py [LINE:36] #INFO     [2023-02-22 17:59:30,917]  Следующая точка: Filters, Process Message
# big_brother.py [LINE:43] #INFO     [2023-02-22 17:59:30,918]  5. on process message, data={'middleware_data': 'Это попадет в on_process_message', 'state': <aiogram.dispatcher.storage.FSMContext object at 0x000001716E16BE10>, 'raw_state': None, 'command': Command.CommandObj(prefix='/', command='start', mention='')}
# big_brother.py [LINE:44] #INFO     [2023-02-22 17:59:30,918]  Следующая точка handler

    #6 handler

    #7
    async def on_post_process_message(self, message: types.Message, data_from_handler: list, data: dict):
        logging.info(f'7. on post process message, {data=}, {data_from_handler}')
        logging.info("Следующая тока: Post Process Update")


    #8
    async def on_post_process_update(self, update: types.Update, data_from_handler: list, data: dict):
        logging.info(f'8. on post process update, {data=}, {data_from_handler=}')
        logging.info(f'-------------end--------------')



    #3.5
    # async def on_pre_process_callback_query(self, callback: types.CallbackQuery, data: dict):  # there is other data
    #     await callback.answer() # этот мидлварь позволит не дожидаться ответа на кнопку


    async def on_post_process_callback_query(self, callback: types.CallbackQuery, data: dict):  # there is other data
        await callback.answer() # этот мидлварь позволит не дожидаться ответа на кнопку
