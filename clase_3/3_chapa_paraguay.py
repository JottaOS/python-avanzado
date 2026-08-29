# 3-Crear una excepción personalizada que valide número de chapa de Paraguay.
# Hay dos versiones, una con tres letras y 4 números y otra con 4 letras y 3 números.
# Recomendación: usar regex

from re import match

REGEX_CHAPA = r"^[A-Z]{3}\d{4}$|^[A-Z]{4}\d{3}$"


class ChapaParaguayError(Exception):
    pass


def validar_chapa(chapa: str):
    if not match(REGEX_CHAPA, chapa):
        raise ChapaParaguayError(f"Chapa inválida: {chapa}.")


if __name__ == "__main__":
    chapas = ["JOT1919", "WYSI727", "A1B2C3D", "PORTI13", "OB232323"]

    for chapa in chapas:
        try:
            validar_chapa(chapa)
            print(f"Chapa válida: {chapa}")
        except ChapaParaguayError as e:
            print(e)
