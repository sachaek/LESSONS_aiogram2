from gino import Gino
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, DateTime

from data import config

db = Gino()


import datetime
from typing import List

import sqlalchemy as sa
from aiogram import Dispatcher
from aiogram.utils.executor import Executor
from gino import Gino
from loguru import logger

# from app import config

db = Gino()


class BaseModel(db.Model):

    # В данной строке кода model = self.__class__.__name__ выполняется следующее:
    #
    # self - это ссылка на текущий экземпляр класса, в данном случае, экземпляр класса,
    # наследующего BaseModel.
    #
    # __class__ - это атрибут, который содержит ссылку на класс,
    # к которому принадлежит текущий экземпляр.
    #
    # __name__ - это атрибут класса, который содержит его имя.
    #
    # Таким образом, self.__class__.__name__ возвращает имя класса текущего экземпляра.
    #
    # Затем полученное имя класса присваивается переменной model.
    # Это позволяет создать строковое представление модели,
    # которое будет использоваться в методе __str__ для вывода информации о модели.
    #
    # Например, если у нас есть класс User,
    #  и текущий экземпляр этого класса использует эту строку кода,
    #  то model будет содержать строку "User".
    #

    # Функция sqlalchemy.inspect() из библиотеки SQLAlchemy предоставляет возможность
    # получить метаданные (структуру) класса или объекта, связанного с базой данных.
    # Она позволяет получить информацию о таблицах, столбцах, связях и других аспектах схемы базы данных.
    #
    # Работа функции sqlalchemy.inspect() включает следующие шаги:
    #
    # Принимает в качестве аргумента класс или объект, который нужно проанализировать.
    #
    # Определяет тип объекта (класс или экземпляр) и создает соответствующий объект инспектора.
    #
    # Получает доступ к метаданным объекта, выполняя ряд операций, в зависимости от типа объекта:
    #
    # Если передан класс, инспектор изучает его структуру и атрибуты
    # для определения информации о таблицах, столбцах, связях и т.д.
    # Если передан экземпляр, инспектор использует метаданные класса
    # , связанного с экземпляром, для получения информации.
    # Возвращает объект инспектора,
    # содержащий информацию о структуре и метаданных объекта или класса.
    #
    # Полученные метаданные могут быть использованы
    # для выполнения различных операций с базой данных,
    # таких как создание таблиц, выполнение запросов,
    # получение информации о структуре и т.д.
    #
    # Пример использования функции sqlalchemy.inspect():
    #
    # python
    # Copy code
    # import sqlalchemy as sa
    #
    # class User(sa.Model):
    #     __tablename__ = 'users'
    #     id = sa.Column(sa.Integer, primary_key=True)
    #     name = sa.Column(sa.String(255))
    #     email = sa.Column(sa.String(255))
    #
    # inspector = sa.inspect(User)
    # table_name = inspector.get_table_name()  # Получение имени таблицы
    # columns = inspector.get_columns()  # Получение информации о столбцах
    #
    # for column in columns:
    #     print(column['name'], column['type'])
    # В этом примере мы создаем класс User, связанный с таблицей базы данных "users".
    # Затем мы используем функцию sqlalchemy.inspect() для получения объекта инспектора inspector,
    #  который содержит метаданные класса User. Затем мы можем получить
    # различную информацию о структуре таблицы, такую как имена столбцов и их типы.
    #

    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        # primary_key_columns: List[sa.Column] = table.primary_key.columns
        primary_key_columns: List[sa.Column] = table.columns

        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


# class TestBSModel(BaseModel):
#     __tablename__ = "bsmodel"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(255))
#
#
# print(TestBSModel)
# # <class '__main__.TestBSModel'>
# print(TestBSModel())
# # <TestBSModel id=None name=None>
#

class TimeBaseModel(BaseModel):
    __abstract__ = True

    created_at = Column(DateTime(True), server_default=db.func.now())
    updated_at = Column(DateTime(True),
                        default=db.func.now(),
                        onupdate=db.func.now(),
                        server_default=db.func.now())

    # при добавлении колонок - будут дополнительно создаваться 2 колонки -
    #created_at , updated_at


async def on_startup(dispatcher: Dispatcher):
    print("Устанавливаем связи с PostgreSQL")
    await db.set_bind(config.POSTGRES_URI)

