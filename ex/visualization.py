import matplotlib.pyplot as plt
import pandas as pd


def parte_4(df: pd.DataFrame):
    plt.figure(figsize=(8, 5))
    plt.bar(
        df["profesor.nombre"],
        df["promedio"],
        color="skyblue",
    )
    plt.title("Gráfico parte 4")
    plt.xlabel("Profesor")
    plt.ylabel("Promedio")
    plt.tight_layout()
    plt.grid()
    plt.show()
