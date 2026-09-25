from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_engine("mysql+pymysql://root:admin@localhost:3306/clase_7", echo=True)


class Base(DeclarativeBase):
    pass
