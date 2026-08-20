# Ejercicio 2: Crear una calculadora polaca inversa
print("=====\nCalculadora con notación polaca inversa\n=====\n")


def parse_input(value):
    try:
        return int(value)
    except ValueError:
        pass

    parsed = value
    if len(value) > 1:
        parsed = value[0]

    return parsed


def is_valid_input(value: int | str, parts: list):
    if type(value) == int:
        return True

    if value == "":
        return True

    if len(value) > 1:
        print("El valor ingresado no es válido")
        return False

    if not is_operator(value):
        print(f"El operador ingresado ({value}) no es válido")
        return False
    else:
        if len(parts) < 2:
            print(
                f"No hay suficientes números para realizar la operación ({value})",
            )
            return False

        if parts[-1] == 0 and value == "/":
            print("No se puede dividir por cero")
            return False

    return True


def is_operator(value: str):
    VALID_OPERATORS = ["+", "-", "*", "/"]
    return value in VALID_OPERATORS


def calculate(operator: str, parts: list):
    new_parts = parts.copy()

    b = new_parts.pop()
    a = new_parts.pop()

    result = 0
    match operator:
        case "+":
            result = a + b
        case "-":
            result = a - b
        case "*":
            result = a * b
        case "/":
            result = a / b

    new_parts.append(round(result, 2))
    return new_parts


def main():
    parts = []
    while True:
        value = input(
            "Ingresa un número u operador aritmético (+, -, *, /) [ENTER para terminar]:\n> "
        )

        parsed_value = parse_input(value)
        is_valid = is_valid_input(parsed_value, parts)

        if not is_valid:
            continue

        if value == "":
            break

        if is_operator(value):
            new_parts = calculate(value, parts)
            parts[:] = new_parts
        else:
            parts.append(parsed_value)

        print(f"\nPila: {parts}")

    print(f"\n\nTotal calculado: {parts[-1]}")
    print("Fin del programa.")


if __name__ == "__main__":
    main()
