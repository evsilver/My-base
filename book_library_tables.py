from sqlalchemy import MetaData, Table, create_engine, Column, String, Integer


metadata = MetaData()
#Ниже происходит создание колонок новой таблицы
users = Table('books', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('title', String, unique=True),
                     Column('author', String),
                     Column('year', Integer),
                     Column('status', String, default="в наличии")
        )

def engine_table():
    """Создаем движок для взаимодействия с таблицей, в аргументах указываю путь к БД"""
    engine = create_engine(url="sqlite+pysqlite:///book_data_base.db", echo=False)
    return engine

#Заносим движок в переменную eng
eng = engine_table()


def create_table():
    """Создаем БД, в аргумент передаем движок"""
    return metadata.create_all(eng)

print(create_table())

