from pathlib import Path

from database import engine
from models import Base
from query import (
    actualizar_cliente,
    consultar_clientes,
    consultar_producto_por_id,
    crear_cliente,
    crear_compra_con_detalle,
    crear_producto,
    crear_venta_con_detalle,
    productos_mas_vendidos,
    total_comprado_por_proveedor,
    total_vendido_por_cliente,
    ventas_con_cliente,
    ventas_mayores_a,
)
from sqlalchemy import text
from sqlalchemy.orm import Session

if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with open(Path(__file__).parent / "insert.sql") as f:
        sql = f.read()
    with Session(engine) as session:
        for sentencia in sql.split(";"):
            if sentencia.strip():
                session.execute(text(sentencia))
        session.commit()
        print("Insert SQL completado")
    crear_producto()
    crear_cliente()
    crear_venta_con_detalle()
    consultar_clientes()
    consultar_producto_por_id(1)
    ventas_mayores_a(100000)
    actualizar_cliente(1)
    ventas_con_cliente()
    total_vendido_por_cliente()
    crear_compra_con_detalle([(1, 10), (3, 5)], id_proveedor=1)
    crear_compra_con_detalle([(2, 20), (6, 8)], id_proveedor=2)
    crear_compra_con_detalle([(4, 15)], id_proveedor=3)
    total_comprado_por_proveedor()
    productos_mas_vendidos()
