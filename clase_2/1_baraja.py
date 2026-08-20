# Ejercicio 1: Modificar el programa de la baraja española y hacer la baraja francesa
import random


class Carta:
    def __init__(self, palo, numero):
        self.palo = palo
        self.numero = numero

    def __str__(self):
        return f"{self.numero} de {self.palo}"


class Baraja:
    def __init__(self):
        pass

    def robar_cartas(self, cantidad):
        mano = []
        if cantidad <= 0:
            print("La cantidad de cartas a robar debe ser mayor que cero.")
            return None
        for _ in range(cantidad):
            if self.cartas:
                mano.append(self.cartas.pop())
            else:
                print("No hay más cartas en la baraja.")
                break
        return mano if mano else None

    def barajar(self):
        random.shuffle(self.cartas)

    def devolver_cartas(self, carta):
        if not carta:
            print("No se puede devolver una carta nula.")
            return
        if carta in self.cartas:
            print("La carta ya está en la baraja.")
            return
        self.cartas.append(carta)
        self.barajar()


class BarajaFrancesa(Baraja):
    def __init__(self):
        super().__init__()
        PALOS = ("Corazones", "Tréboles", "Picas", "Diamantes")
        ETIQUETA = {
            1: "A",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "10",
            11: "J",
            12: "Q",
            13: "K",
        }
        self.cartas = [
            Carta(palo, ETIQUETA.get(numero + 1))
            for palo in PALOS
            for numero in range(13)
        ]


class BarajaEspañola(Baraja):
    def __init__(self):
        super().__init__()
        PALOS = ("Oros", "Copas", "Espadas", "Bastos")
        self.cartas = [
            Carta(palo, numero)
            for palo in PALOS
            for numero in range(1, 13)
            if numero != 8 and numero != 9
        ]


if __name__ == "__main__":
    baraja = BarajaFrancesa()
    baraja.barajar()

    print("Robando 5 cartas:")
    mano = baraja.robar_cartas(5)
    if mano:
        for carta in mano:
            print(carta)

    print("\nDevolviendo una carta a la baraja:")
    if mano:
        primera_carta = mano.pop(0)
        baraja.devolver_cartas(primera_carta)
        print(f"Se devolvió: {primera_carta}")

    print("\nDevolviendo mi mano al mazo:")
    if mano:
        for carta in mano:
            baraja.devolver_cartas(carta)
            print(f"Se devolvió: {carta}")
