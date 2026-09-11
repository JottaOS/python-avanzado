from datetime import date
from decimal import Decimal

from database import Base
from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column


class Venta(Base):
    __tablename__ = "ventas"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fecha: Mapped[date]
    producto: Mapped[str] = mapped_column(String(200))
    categoria: Mapped[str] = mapped_column(String(100))
    cantidad: Mapped[int]
    precio: Mapped[Decimal] = mapped_column(Numeric(12, 0))

    def __repr__(self):
        return f"Venta(id={self.id}, fecha={self.fecha}, producto='{self.producto}', categoria='{self.categoria}', cantidad={self.cantidad}, precio={self.precio})"
