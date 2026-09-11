from consulta_insert import consulta_insert
from consulta_select import consulta_select
from database import Base, engine

if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    consulta_insert()
    consulta_select()
