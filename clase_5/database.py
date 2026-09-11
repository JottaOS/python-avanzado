from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

cadena_conexion = "mysql+pymysql://root:admin@localhost:3306/street_fighter_6"

engine = create_engine(cadena_conexion, echo=True)


class Base(DeclarativeBase):
    pass
