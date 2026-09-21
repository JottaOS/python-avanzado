import time
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, Numeric, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

cadena_conexion = "mysql+pymysql://root:admin@localhost:3306/catalogo"

engine = create_engine(cadena_conexion, echo=True)


class Base(DeclarativeBase):
    pass


class Producto(Base):
    __tablename__ = "productos"
    producto_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100))
    categoria: Mapped[str] = mapped_column(String(50))
    descripcion: Mapped[str] = mapped_column(Text)
    precio: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    stock: Mapped[int] = mapped_column()


class Pedido(Base):
    __tablename__ = "pedidos"
    pedido_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cliente_nombre: Mapped[str] = mapped_column(String(100))
    fecha_pedido: Mapped[datetime] = mapped_column(DateTime)
    estado: Mapped[str] = mapped_column(String(20))


def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {fin - inicio} segundos")
        return resultado

    return wrapper


@medir_tiempo
def obtener_productos():
    with Session(engine) as session:
        datos = []
        for producto in session.query(Producto).all():
            datos.append(
                {
                    "producto_id": producto.producto_id,
                    "nombre": producto.nombre,
                    "categoria": producto.categoria,
                    "descripcion": producto.descripcion,
                    "precio": producto.precio,
                    "stock": producto.stock,
                }
            )
    return datos


@medir_tiempo
def aplicar_descuento(datos):
    con_stock = filter(lambda x: x["stock"] > 20, datos)
    con_descuento = map(  # noqa: C417
        lambda x: {
            **x,
            "precio": (x["precio"] * Decimal("0.90")).quantize(Decimal("0.01")),
        },
        con_stock,
    )
    return list(con_descuento)


@medir_tiempo
def guardar_productos(datos):
    with Session(engine) as session:
        for dato in datos:
            producto = (
                session.query(Producto)
                .filter(Producto.producto_id == dato["producto_id"])
                .first()
            )
            if producto:
                producto.precio = dato["precio"]
        session.commit()


@medir_tiempo
def obtener_pedidos():
    with Session(engine) as session:
        datos = []
        for pedido in session.query(Pedido).all():
            datos.append(
                {
                    "pedido_id": pedido.pedido_id,
                    "cliente_nombre": pedido.cliente_nombre,
                    "fecha_pedido": pedido.fecha_pedido,
                    "estado": pedido.estado,
                }
            )
    return datos


@medir_tiempo
def cancelar_pendientes(datos):
    pendientes = filter(lambda x: x["estado"] == "pendiente", datos)
    cancelados = map(  # noqa: C417
        lambda x: {**x, "estado": "cancelado"}, pendientes
    )
    return list(cancelados)


@medir_tiempo
def guardar_pedidos(datos):
    with Session(engine) as session:
        for dato in datos:
            pedido = (
                session.query(Pedido)
                .filter(Pedido.pedido_id == dato["pedido_id"])
                .first()
            )
            if pedido:
                pedido.estado = dato["estado"]
        session.commit()


if __name__ == "__main__":
    productos = obtener_productos()
    print("Precios originales:")
    for producto in productos:
        print(
            f"  {producto['nombre']}: {producto['precio']} (stock {producto['stock']})"
        )

    editados = aplicar_descuento(productos)
    print("\nProductos con stock mayor a 20 (descuento 10% aplicado):")
    for producto in editados:
        print(
            f"  {producto['nombre']}: {producto['precio']} (stock {producto['stock']})"
        )

    guardar_productos(editados)
    print("\nPrecios actualizados correctamente.")

    pedidos = obtener_pedidos()
    print("\nPedidos antes de la edición:")
    for pedido in pedidos:
        print(
            f"  #{pedido['pedido_id']} {pedido['cliente_nombre']}: {pedido['estado']}"
        )

    cancelados = cancelar_pendientes(pedidos)
    print("\nPedidos pendientes marcados como cancelados:")
    for pedido in cancelados:
        print(
            f"  #{pedido['pedido_id']} {pedido['cliente_nombre']}: {pedido['estado']}"
        )

    guardar_pedidos(cancelados)
    print("\nPedidos actualizados correctamente.")
