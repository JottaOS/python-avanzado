from pathlib import Path

from analytics import parte_3
from database import engine
from models import Base
from pipeline import parte_2
from sqlalchemy import text
from sqlalchemy.orm import Session
from visualization import parte_4

if __name__ == "__main__":
    # parte 1
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with open(Path(__file__).parent / "seed.sql") as f:
        sql = f.read()
    with Session(engine) as session:
        for sentencia in sql.split(";"):
            if sentencia.strip():
                session.execute(text(sentencia))
        session.commit()
        print("Insert SQL completado")

    parte_2()
    df = parte_3()
    parte_4(df)
