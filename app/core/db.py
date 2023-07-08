from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings

class PreBase:

    @declared_attr
    def __tablename__(cls):
        # Именем таблицы будет название модели в нижнем регистре.
        return cls.__name__.lower()

    # Во все таблицы будет добавлено поле ID.
    id = Column(Integer, primary_key=True)

# Базовый класс для моделей
Base = declarative_base(cls=PreBase)

# Создание асинхронного движка
engine = create_async_engine(settings.database_url)

# Класс для асинхронной работы и множественного создания сессий
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession) 


# Асинхронный генератор сессий.
async def get_async_session():
    # Через асинхронный контекстный менеджер и sessionmaker
    # открывается сессия.
    async with AsyncSessionLocal() as async_session:
        # Генератор с сессией передается в вызывающую функцию.
        yield async_session
        # Когда HTTP-запрос отработает - выполнение кода вернётся сюда,
        # и при выходе из контекстного менеджера сессия будет закрыта.
