# Ejercicio 4: Expandir el servicio de tickets,
# con gestión de una lista de clientes registrados con sus datos en lista de diccionarios
from collections import deque


def add_ticket(customer: dict, ticket: str):
    tickets = customer["tickets"]

    if ticket in tickets:
        print(f"Ticket {ticket} ya existe en la lista de tickets")
        return

    tickets.append(ticket)


def remove_ticket(customer: dict):
    tickets = customer["tickets"]

    if tickets:
        return tickets.popleft()

    print("No hay tickets para remover")
    return None


def simulate_service(customers: list[dict]):
    for customer in customers:
        print(f"\n{customer['name']} {customer['surname']} ingresa al evento")
        print(
            f"Tickets de {customer['name']} {customer['surname']}: "
            f"{list(customer['tickets'])}"
        )

        while customer["tickets"]:
            ticket = remove_ticket(customer)
            print(f"Ticket {ticket} validado")

        print(f"{customer['name']} validó todos sus tickets")


if __name__ == "__main__":
    customers = [
        {
            "name": "Juan",
            "surname": "Pérez",
            "email": "juanperez@gmail.com",
            "tickets": deque(),
        },
        {
            "name": "Ana",
            "surname": "Gómez",
            "email": "anagomez@gmail.com",
            "tickets": deque(),
        },
    ]

    add_ticket(customers[0], "A01")
    add_ticket(customers[0], "B02")
    add_ticket(customers[0], "C03")

    add_ticket(customers[1], "D04")
    add_ticket(customers[1], "E05")

    simulate_service(customers)
