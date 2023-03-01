from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from .privat_chat import IsPrivate
from .test_middleware import SomeF

if __name__ == "filters":
    # dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(SomeF)
    pass
