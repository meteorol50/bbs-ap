from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ASYNC_DB_URL = "mysql+aiomysql://root:root@mariadb:3306/bbs?charset=utf8"

engine = create_engine(ASYNC_DB_URL, echo=True)
session = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()


async def get_db():
    async with session():
        yield session