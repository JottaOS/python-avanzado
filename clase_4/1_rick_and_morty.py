import matplotlib.pyplot as plt
import pandas as pd
import requests


def buscar_personajes(nombre):
    nombre = nombre.strip().lower()
    url = f"https://rickandmortyapi.com/api/character/?name={nombre}"

    personajes = []
    pagina = 1
    while True:
        try:
            respuesta = requests.get(url, params={"page": pagina}, timeout=10)
            respuesta.raise_for_status()
            datos = respuesta.json()
        except requests.exceptions.HTTPError as e:
            if respuesta.status_code == 404:
                print("No se encontraron personajes con ese nombre.")
            else:
                print(f"Error HTTP {respuesta.status_code}: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la solicitud: {e}")
            return None

        for dato in datos["results"]:
            personajes.append(
                {
                    "Nombre": dato["name"],
                    "Estado": dato["status"],
                    "Especie": dato["species"],
                    "Género": dato["gender"],
                    "Origen": dato["origin"]["name"],
                    "Ubicación": dato["location"]["name"],
                    "Número de episodios": len(dato["episode"]),
                }
            )

        if datos["info"]["next"]:
            pagina += 1
        else:
            break

    return pd.DataFrame(personajes)


if __name__ == "__main__":
    nombre = input("Introduzca el nombre del personaje de Rick and Morty a buscar: ")
    df = buscar_personajes(nombre)
    if df is None:
        raise SystemExit

    print(f"\nSe encontraron {len(df)} personajes. Primeras filas del DataFrame:")
    print(df.head())

    print("\nResumen de la columna 'Número de episodios':")
    print(df["Número de episodios"].describe())

    df_especies = df["Especie"].value_counts()
    plt.figure()
    df_especies.plot(kind="pie")
    plt.title("Distribución de personajes por especie")
    plt.show()

    df_vivos = df[df["Estado"] == "Alive"]
    df_top_vivos = df_vivos.nlargest(10, "Número de episodios")
    plt.figure()
    df_top_vivos.set_index("Nombre")["Número de episodios"].plot(kind="barh")
    plt.title("Top 10 personajes vivos con más episodios")
    plt.show()
