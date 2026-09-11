from enum import Enum

from database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class CharacterType(Enum):
    SHOTO = "SHOTO"
    GRAPPLER = "GRAPPLER"
    ZONER = "ZONER"
    RUSHDOWN = "RUSHDOWN"
    BRAWLER = "BRAWLER"


class Difficulty(Enum):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"


class Character(Base):
    __tablename__ = "character"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200))
    type: Mapped[CharacterType]
    health: Mapped[int]
    difficulty: Mapped[Difficulty]
    max_damage_combo: Mapped[int]

    def __repr__(self) -> str:
        return f"Character(id={self.id}, name={self.name}, type={self.type}, health={self.health}, difficulty={self.difficulty}, max_damage_combo={self.max_damage_combo})"

    def __str__(self):
        return f"Character: {self.name}\nType: {self.type.value}\nHealth: {self.health}\nDifficulty: {self.difficulty.value}\nMax Damage Combo: {self.max_damage_combo}"
