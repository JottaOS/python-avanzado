# 2- Crear un generador de contraseñas legibles.
# Agarrar palabras al azar de un texto palabras.txt, juntar 3 de ellas en formato PascalCase,
# y al final poner un símbolo y tres números

from pathlib import Path
from random import choice

SIMBOLOS = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
NUMEROS = "0123456789"

if __name__ == "__main__":
    palabras_file = Path(__file__).resolve().with_name("palabras.txt")
    with open(palabras_file, "r", encoding="utf-8") as f:
        palabras = [linea.strip() for linea in f if linea.strip()]

    while True:
        palabras_seleccionadas = []
        while len(palabras_seleccionadas) < 3:
            palabra = choice(palabras)
            if palabra not in palabras_seleccionadas:
                palabras_seleccionadas.append(palabra)

        palabras_unidas = "".join(
            palabra.capitalize() for palabra in palabras_seleccionadas
        )

        simbolo = choice(SIMBOLOS)
        numeros = "".join(choice(NUMEROS) for _ in range(3))

        contrasena = f"{palabras_unidas}{simbolo}{numeros}"
        print(contrasena)

        respuesta = input("¿Generar otra contraseña? (s/n): ")
        if respuesta.lower() != "s":
            break
