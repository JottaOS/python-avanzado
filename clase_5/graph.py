import matplotlib.pyplot as plt
import pandas as pd
from database import engine
from models import Character
from sqlalchemy import select
from sqlalchemy.orm import Session


def graph():
    #  Posteriormente cargar en un dataframe alguna consulta y hacer algún gráfico analítico del tipo de su preferencia

    # gráfico de barras de la cantidad de personajes por tipo
    with Session(engine) as session:
        statement = select(Character.type)
        characters = session.execute(statement).all()

        df = pd.DataFrame(characters, columns=["type"])

        type_counts = df["type"].value_counts()

        plt.figure(figsize=(10, 6))
        type_counts.plot(kind="bar", color="skyblue")
        plt.title("Cantidad de Personajes por Tipo")
        plt.xlabel("Tipo de Personaje")
        plt.ylabel("Cantidad")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
