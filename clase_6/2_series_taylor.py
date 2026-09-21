import time
from functools import reduce
from math import cos, factorial, sin


def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {fin - inicio} segundos")
        return resultado

    return wrapper


@medir_tiempo
def seno_taylor(x, n):
    termino = lambda k: ((-1) ** k) * (x ** (2 * k + 1)) / factorial(2 * k + 1)
    return reduce(lambda acc, k: acc + termino(k), range(n + 1), 0)


@medir_tiempo
def coseno_taylor(x, n):
    termino = lambda k: ((-1) ** k) * (x ** (2 * k)) / factorial(2 * k)
    return reduce(lambda acc, k: acc + termino(k), range(n + 1), 0)


if __name__ == "__main__":
    angulo = 0.5
    terminos = 10

    aprox_seno = seno_taylor(angulo, terminos)
    print(f"sin({angulo}) ≈ {aprox_seno}")
    print(f"math.sin({angulo}) = {sin(angulo)}")
    print(f"diferencia: {abs(aprox_seno - sin(angulo))}")

    aprox_coseno = coseno_taylor(angulo, terminos)
    print(f"\ncos({angulo}) ≈ {aprox_coseno}")
    print(f"math.cos({angulo}) = {cos(angulo)}")
    print(f"diferencia: {abs(aprox_coseno - cos(angulo))}")
