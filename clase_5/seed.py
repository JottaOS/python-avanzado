import csv
from pathlib import Path

from database import engine
from models import Character
from sqlalchemy.orm import Session


def seed():
    ruta_csv = Path(__file__).resolve().with_name("data.csv")
    with Session(engine) as session:
        with open(ruta_csv, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                character = Character(
                    name=row["name"],
                    type=row["type"],
                    health=row["health"],
                    difficulty=row["difficulty"],
                    max_damage_combo=row["max_damage_combo"],
                )
                session.add(character)

        session.commit()
